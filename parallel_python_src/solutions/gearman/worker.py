import cPickle
import gearman

class CustomGearmanWorker(gearman.GearmanWorker):
    def on_job_execute(self, current_job):
        print "Job started"
        return super(CustomGearmanWorker, self).on_job_execute(current_job)

    def on_job_exception(self, current_job, exc_info):
        print "Job failed, CAN stop last gasp GEARMAN_COMMAND_WORK_FAIL"
        return super(CustomGearmanWorker, self).on_job_exception(current_job, exc_info)

    def on_job_complete(self, current_job, job_result):
        print "Job complete"
        return super(CustomGearmanWorker, self).send_job_complete(current_job, job_result)

    def after_poll(self, any_activity):
        # Return True if you want to continue polling, replaces callback_fxn
        return True


def calculate_z(gearman_worker, job):
    """Pure python with complex datatype, iterating over list of q and z"""
    q, maxiter = cPickle.loads(job.data)
    output = [0] * len(q)
    for i in range(len(q)):
        zi = 0+0j
        qi = q[i]
        if i % 1000 == 0:
            # print out some progress info since it is so slow...
            print "%0.2f%% complete" % (1.0/len(q) * i * 100)

        output[i] = maxiter # force max value if we exceed maxiter

        for iteration in range(maxiter):
            zi = zi * zi + qi
            if abs(zi) > 2.0:
                output[i] = iteration
                break
    output_string = cPickle.dumps(output)
    return output_string

# the CustomGearmanWorker is useful for debugging
#new_worker = CustomGearmanWorker(['localhost:4730'])

# We'll use the basic one for coding
new_worker = gearman.GearmanWorker(['localhost:4730'])

# register our function and work forever
new_worker.register_task("calculate_z", calculate_z)
new_worker.work()
