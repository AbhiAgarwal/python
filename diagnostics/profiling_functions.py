# It's a collection of decorators for profiling functions
# example taken from: http://mg.pov.lt/profilehooks/
# pip install profilehooks
# https://github.com/mgedmin/profilehooks

from profilehooks import profile

class SampleClass:
    @profile
    def silly_fibonacci_example(self, n):
        if n < 1:
            raise ValueError('n must be >= 1, got %s' % n)
        if n in (1, 2):
            return 1
        else:
            return (self.silly_fibonacci_example(n - 1) +
                    self.silly_fibonacci_example(n - 2))

if __name__ == '__main__':
    fib = SampleClass().silly_fibonacci_example
    print fib(10)
