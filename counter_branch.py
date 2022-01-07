from metaflow import FlowSpec, step
import time

def fib(n):
    if n <= 2: return 1
    else: return fib(n-1) + fib(n-2)
 
class CounterBranchFlow(FlowSpec):
    @step
    def start(self):
        self.t0 = time.time()
        self.creature = "dog"
        self.count = 0
        self.foo  = "bar"
        self.next(self.add_two, self.add_one)
    
    @step
    def add_one(self):
        self.count += 1
        self.next(self.join)
        
    
    @step
    def add_two(self):
        self.count += 2
        self.next(self.join)
        
 
    @step
    def join(self, inputs):
        self.t1 = time.time()
        self.count = max(inp.count for inp in inputs)
        self.t0 = inputs[0].t0
        print("count from add_one", inputs.add_one.count)
        print("count from add_two", inputs.add_two.count)
        print("the count thing", self.count)
        print("total-time:", self.t1-self.t0)
        
        # self.creature = inputs[0].creature
        self.merge_artifacts(inputs)
        self.foo = inputs[0].foo
        self.next(self.end)
        
 
    @step
    def end(self):
        print("The creature is", self.creature)
        print("The final count is", self.count)
 
if __name__ == '__main__':
    # t0 = time.time()
    # fib(35)
    # t1 = time.time()
    # print("total-time for fib:", t1-t0)
    CounterBranchFlow()
