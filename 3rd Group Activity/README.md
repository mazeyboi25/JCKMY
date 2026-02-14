# 1. Differentiate Task and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division.
#### - Task Parallelism and Data Parallelism are different in how the work is divided. Task Parallelism separates the program into different operations that run at the same time on the same data. In the ThreadPoolExecutor code, each deduction (SSS, PhilHealth, Pag-IBIG, and Withholding Tax) is a separate function, but all of them use the same salary. The work is divided based on the type of task. On the other hand, Data Parallelism divides the work based on the data. In the ProcessPoolExecutor code, one payroll function is used, but it is applied to different employees at the same time. This means the same process is repeated for different data entries. Task Parallelism focuses on different functions, while Data Parallelism focuses on different data.

# 2. Explain how concurrent.futures managed execution, including submit(), map(), and Future objects. Discuss the purpose of with when creating an Executor.
#### - The concurrent.futures module controls how tasks are run in the background. The submit() function sends a task to be executed and immediately returns a Future object. A Future holds the result that will be produced later, and calling result() gets the final value once the task is done. In Data Parallelism, map() is used to apply one function to many data items automatically. The with statement is used to make sure the executor starts properly and shuts down correctly after finishing, so system resources are cleaned up safely.

# 3. Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did true parallelism occur?
#### - Because of the Global Interpreter Lock (GIL) in Python, ThreadPoolExecutor does not create true parallelism for CPU-heavy tasks. Even if multiple threads are running, only one thread can execute Python code at a time. This means the tasks were running in turns, not truly at the same time on multiple CPU cores. Real parallelism happens when using ProcessPoolExecutor, because each process runs separately with its own Python interpreter, allowing multiple CPU cores to work at the same time.

# 4. Explain why ProcessPoolExecutor enables true parallelism, including memory space separation and GIL behavior.
#### - 

# 5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which approach scales better and why?
#### - 

# 6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use.
#### - 

ok na? g nana