class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs, n):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    result = [False] * n
    job_sequence = [-1] * n

    total_profit = 0
    for job in jobs:
        for j in range(min(n - 1, job.deadline - 1), -1, -1):
            if not result[j]:
                result[j] = True
                job_sequence[j] = job.id
                total_profit += job.profit
                break

    print("Job Sequence:", [f"Job {x}" for x in job_sequence if x != -1])
    print("Max Profit:", total_profit)

if __name__ == "__main__":
    jobs = [Job(1, 2, 100), Job(2, 1, 19), Job(3, 2, 27), Job(4, 1, 25), Job(5, 3, 15)]
    n = 3
    job_sequencing(jobs, n)
