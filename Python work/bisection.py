# %% [markdown]
# ## Bisection Method

# %% [markdown]
# The Bisection method is used to find the roots of a equation by repeatedly dividing the interval. This method will divide the interval until the resulting interval is found, which is extremely small. <br/>
# 
# 

# %%
from typing import Callable


# %%
def bisection(function: Callable[[float], float], a: float, b: float) -> float:
    start: float = a
    end: float = b
    if function(a) == 0:
        return a
    elif function(b) == 0:
        return b
    elif (function(a) * function(b) > 0): 
        raise ValueError("could not find root in given interval.")
    else:
        mid: float = start + (end - start) / 2.0
        while abs(start - mid) > 10**-7:  # until precisely equals to 10^-7
            if function(mid) == 0:
                return mid
            elif function(mid) * function(start) < 0:
                end = mid
            else:
                start = mid
            mid = start + (end - start) / 2.0
        return mid
def f(x: float) -> float:
    return x**3 - 2 * x - 5

if __name__ == "__main__":
    print(bisection(f, 1, 1000))

    import doctest

    doctest.testmod()

# %%
bisection(lambda x: x ** 3 - 1, -5, 5)

# %%
bisection(lambda x: x ** 3 - 1, 2, 1000)

# %%
bisection(lambda x: x ** 2 - 4 * x + 3, 0, 2)

# %% [markdown]
# ### Python function arguments with colon:<br/>
# ```python
# def bisection(function: Callable[[float], float], a: float, b: float) -> float:
# ```
# colons serve as a function annotation; function arguments and the return value can be tagged with arbitrary Python expressions. Python itself ignores the annotation (other than saving it), but third-party tools can make use of them.
# in this case
# ```python
# function: Callable[[float]
# a: float
# b: float
# ```

# %% [markdown]
# # Bisection Method Algorithm

# %% [markdown]
# ##### 1. one of the a or b is a root for the function
# ##### 2. if none of these are root and they are both positive or negative,
# 
# 1. For any continous function f(x):
# - a is the root for the function if f(a) == 0
# - b is the root for the function if f(b) == 0
# - for two points, say a and b such that a < b and f(a)* f(b) < 0
# 
# 
# ```python
# if function(a) == 0:  # one of the a or b is a root for the function
#         return a
# elif function(b) == 0:
#     return b
# elif (function(a) * function(b) > 0):  # if none of these are root and they are both positive or negative,
#     # then this algorithm can't find the root
#     raise ValueError("could not find root in given interval.")
# ```
# 

# %% [markdown]
# # Step 3
# 
# ```python
#     else:
#         mid: float = start + (end - start) / 2.0
#         while abs(start - mid) > 10**-7:  # until precisely equals to 10^-7
#             if function(mid) == 0:
#                 return mid
#             elif function(mid) * function(start) < 0:
#                 end = mid
#             else:
#                 start = mid
#             mid = start + (end - start) / 2.0
#         return mid
# ```
# 3. Find the midpoint of a and b, say “t”
#  ```python
# mid: float = start + (end - start) / 2.0
# ````
# - t is the root of the given function if f(t) = 0; else follow the next step
# - Divide the interval [a, b] – If f(t)*f(a) <0, there exist a root between t and a
# else if f(t) *f (b) < 0, there exist a root between t and b
# - Repeat above three steps until f(t) = 0.
# 
# #### abs() function
# The abs() function returns the absolute value of the specified number and remove the negative sign of a number in Python. 
# 
# 

# %% [markdown]
# 


