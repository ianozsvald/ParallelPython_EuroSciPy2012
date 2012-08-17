import sys
import datetime
import cPickle
from gearman import GearmanClient
import gearman

# area of space to investigate
x1, x2, y1, y2 = -2.13, 0.77, -1.3, 1.3


def show(output):
    """Convert list to numpy array, show using PIL"""
    try:
        import Image
        # convert our output to PIL-compatible input
        import array
        # scale the output to a 0..255 range for plotting
        max_val = max(output)
        output=[int(float(o)/max_val*255) for o in output]
        output = ((o + (256*o) + (256**2)*o) * 8 for o in output)
        output = array.array('I', output)
        # display with PIL
        im = Image.new("RGB", (w/2, h/2))
        im.fromstring(output.tostring(), "raw", "RGBX", 0, -1)
        im.show()
    except ImportError as err:
        # Bail gracefully if we don't have PIL
        print "Couldn't import Image:", str(err)



def calc_pure_python(show_output):
    # make a list of x and y values which will represent q
    # xx and yy are the co-ordinates, for the default configuration they'll look like:
    # if we have a 1000x1000 plot
    # xx = [-2.13, -2.1242, -2.1184000000000003, ..., 0.7526000000000064, 0.7584000000000064, 0.7642000000000064]
    # yy = [1.3, 1.2948, 1.2895999999999999, ..., -1.2844000000000058, -1.2896000000000059, -1.294800000000006]
    x_step = (float(x2 - x1) / float(w)) * 2
    y_step = (float(y1 - y2) / float(h)) * 2
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    q = []
    for ycoord in y:
        for xcoord in x:
            q.append(complex(xcoord, ycoord))
    z = [0+0j] * len(q)

    print "Total elements:", len(z)

    # split work list into continguous chunks, one per CPU
    # build this into chunks which we'll apply to map_async
    nbr_chunks = 128 # experiment with different nbrs of chunks
    chunk_size = len(q) / nbr_chunks

    # a chunk will look like:
    # ([(-2.13+1.3j), (-2.1242+1.3j), ...,  (-0.685799999999998+1.3j)], 1000)

    # split our long work list into smaller chunks
    # make sure we handle the edge case where nbr_chunks doesn't evenly fit into len(q)
    if len(q) % nbr_chunks != 0:
        # make sure we get the last few items of data when we have
        # an odd size to chunks (e.g. len(q) == 100 and nbr_chunks == 3
        nbr_chunks += 1
    chunks = [(q[x*chunk_size:(x+1)*chunk_size], maxiter) \
              for x in xrange(nbr_chunks)]
    print chunk_size, len(chunks), len(chunks[0][0])

    jobs = []
    output = []
    start_time = datetime.datetime.now()
    for job_nbr, chunk in enumerate(chunks):
        data = cPickle.dumps(chunk)
        job=client.submit_job('calculate_z', data, wait_until_complete=False)
        jobs.append(job)
        print "DONE JOB", job_nbr
        print job.state

    print "Waiting..."
    client.wait_until_jobs_completed(jobs)
    print "All done"

    # rebuild the output in the order we submitted the jobs
    for job in jobs:
        output_string = job.result
        output_item = cPickle.loads(output_string)
        output += output_item

    end_time = datetime.datetime.now()

    secs = end_time - start_time
    print "Main took", secs

    validation_sum = sum(output)
    print "Total sum of elements (for validation):", validation_sum

    if show_output:
        show(output)

    return validation_sum


if __name__ == "__main__":
    # get width, height and max iterations from cmd line
    if len(sys.argv) == 1:
        w = h = 1000
        maxiter = 1000
    else:
        w = int(sys.argv[1])
        h = int(sys.argv[1])
        maxiter = int(sys.argv[2])

    client = GearmanClient(["127.0.0.1"])

    # we can show_output for Python, not for PyPy
    validation_sum = calc_pure_python(True)

    # confirm validation output for our known test case
    # we do this because we've seen some odd behaviour due to subtle student
    # bugs
    if w == 1000 and h == 1000 and maxiter == 1000:
        assert validation_sum == 51214485 # if False then we have a bug

