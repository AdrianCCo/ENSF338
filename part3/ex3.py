import cProfile
import timeit

def sub_function(n):
    # Sub Function calculates the factorial of n
    if n == 0:
        return 1
    return n * sub_function(n-1)


def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data


def third_function():
    # Third Function that calculates the square of the numbers from 0 to 999
    return [i ** 2 for i in range(100_000_000)]


with cProfile.Profile() as profile:
    test_function()
    third_function()

    profile.print_stats(sort="cumtime")


# 1. What is a profiler and what does it do?
# - A profiler is a tool that aids programmers in finding out how much time their program spends on different tasks such as function calls.

# 2. How does profiling differs from benchmarking?
# - Profiling
# -- Measuring relative system statistics (fine-grained)

# - Benchmarking
# -- Manually measure elapsed time for a code region of interest (coarse-grained information)

# 4. Discuss a sample output. Where does execution time go?
# - At the top of the output, we can see the total amount of time that it took for the program to run which is 10.000 (relative to my computer)
# - Most of the time (cumtime) spent running the code is in the function third_function which uses 9.930 seconds (relative to my computer)
