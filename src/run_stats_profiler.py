from cProfile import Profile
from pstats import Stats

def run_stats_profiler(func,test_data):
    lambda_func = lambda: func(test_data)
    profiler = Profile()
    profiler.runcall(lambda_func)

    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()