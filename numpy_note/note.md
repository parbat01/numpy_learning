# NumPy Complete Course Notes

> Beginner-friendly notes covering NumPy from the basics through practical array manipulation, vectorisation, and missing-value handling.

## Learning Goal

We’ll learn NumPy from scratch through:

- Practical array manipulation
- Array creation and properties
- Indexing and slicing
- Filtering with Boolean masks
- Reshaping and flattening
- Modifying, stacking, and splitting arrays
- Broadcasting
- Vectorisation
- Missing-value and infinity handling

---

# 1. Introduction to NumPy

## 1.1 What is NumPy?

**NumPy** stands for **Numerical Python**.

It is a Python library designed for working efficiently with large amounts of numerical data.

We need NumPy because of the following major problems:

- Python loops can become slow when processing very large datasets.
- Normal Python lists are not designed for high-performance numerical computing.
- NumPy provides specialised arrays and fast mathematical operations.

NumPy plays a significant role in:

- Data Science
- Data Analysis
- Machine Learning
- Artificial Intelligence
- Scientific Computing
- Finance
- Medical Research
- Image Processing

## 1.2 Main Idea

Instead of repeatedly processing individual values with Python loops, NumPy allows many operations to be performed directly on an entire array.

The common convention (universal habit which programmers mutually agreed to follow for consistency and readability) used in NumPy code is:

```python
import numpy as np
```

`np` is an alias (short form) for NumPy.

For example:

```python
import numpy as np

arr = np.array([10, 20, 30])

print(arr)
```

Using `np` makes NumPy code shorter and easier to read.

---

# 2. NumPy Arrays

A NumPy array is a collection of data stored in an organised structure.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)
```

Output:

```text
[10 20 30 40 50]
```

## 2.1 NumPy Array vs Python List

### Python list

```python
numbers = [10, 20, 30]
```

### NumPy array

```python
numbers = np.array([10, 20, 30])
```

We can perform efficient mathematical operations directly on NumPy arrays.

Example:

```python
arr = np.array([10, 20, 30])

print(arr * 2)
```

Output:

```text
[20 40 60]
```

The operation is applied to all elements.

## 2.2 Array Dimensions

### 1D Array

A 1D array is a simple sequence of values. It can be thought of as a row in an Excel sheet.

```python
arr = np.array([10, 20, 30, 40, 50])
```

Conceptually:

```text
10 20 30 40 50
```

It contains values along one dimension.

### 2D Array

A 2D array has rows and columns. It is similar to a table.

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
```

Conceptually:

```text
1 2 3
4 5 6
```

### 3D / Multidimensional Arrays

A multidimensional array contains multiple layers of data.

These structures are useful for applications such as:

- Deep Learning
- AI
- MRI/scientific data
- 3D modelling
- Other multidimensional numerical data

---

# 3. Matrix

A matrix can be understood here as a 2D array of numbers, similar to what we learn in mathematics.

Example:

```python
matrix = np.array([[2, 4, 6], [8, 10, 12]])
```

Matrices are commonly used for mathematical operations.

---

# 4. Creating Arrays

## 4.1 Create an Array from a Python List

### 1D array

```python
arr = np.array([10, 20, 30, 40])
```

### 2D array

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
```

## 4.2 `np.zeros()`

`np.zeros()` creates an array filled with zeros.

### 1D

```python
arr = np.zeros(4)
```

Conceptually:

```text
[0 0 0 0]
```

This creates 4 zeros.

### 2D

```python
arr = np.zeros((2, 3))
```

Conceptually:

```text
0 0 0
0 0 0
```

The tuple `(2, 3)` means:

- 2 rows
- 3 columns

## 4.3 `np.ones()`

Creates an array filled with ones.

```python
arr = np.ones((2, 3))
```

Output:

```text
1 1 1
1 1 1
```

## 4.4 `np.full()`

Creates an array filled with a specific value.

```python
arr = np.full((2, 2), 7)
```

Output:

```text
7 7
7 7
```

General pattern:

```python
np.full(shape, value)
```

## 4.5 `np.arange()`

`np.arange()` is similar to Python's `range()`, but returns a NumPy array.

General form:

```python
np.arange(start, stop, step)
```

Example:

```python
arr = np.arange(1, 10, 2)

print(arr)
```

Output:

```text
[1 3 5 7 9]
```

### Important points

- `start` is included.
- `stop` is excluded.
- `step` controls the increment.

## 4.6 `np.eye()`

Creates an identity matrix.

```python
identity = np.eye(3)
```

Output:

```text
1 0 0
0 1 0
0 0 1
```

An identity matrix is a square matrix with:

- `1` on the main diagonal
- `0` elsewhere

---

# 5. Array Properties

Before performing operations on an array, it is important to understand its structure.

Important properties:

- `.shape`
- `.size`
- `.ndim`
- `.dtype`

## 5.1 `.shape`

Returns the dimensions of the array.

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)
```

Output:

```text
(2, 3)
```

Meaning:

- 2 rows
- 3 columns

## 5.2 `.size`

Returns the total number of elements.

```python
arr = np.array([[10, 20, 30], [40, 50, 60]])

print(arr.size)
```

Output:

```text
6
```

## 5.3 `.ndim`

Returns the number of dimensions.

Examples:

```text
1D array -> 1
2D array -> 2
3D array -> 3
```

Example:

```python
arr.ndim
```

## 5.4 `.dtype`

Returns the data type stored in the array.

```python
arr = np.array([10, 20, 30])

print(arr.dtype)
```

Output may be:

```text
int64
```

If an array contains decimal values, NumPy may use a floating-point dtype such as `float64`.

Example:

```python
arr = np.array([10, 20, 30.5])

print(arr.dtype)
```

---

# 6. Indexing

Indexing means accessing a specific element from an array.

NumPy uses **zero-based indexing**.

Example:

```python
arr = np.array([10, 20, 30, 40, 50])
```

Indexes:

```text
Value:  10  20  30  40  50
Index:   0   1   2   3   4
```

So:

```python
print(arr[0])  # 10
print(arr[2])  # 30
```

## 6.1 Negative Indexing

Negative indexes start from the end.

```python
arr[-1]
```

returns the last element.

Example:

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[-1])  # 50
print(arr[-2])  # 40
```

## 6.2 2D Indexing

For a 2D array:

```python
arr = np.array([[10, 20, 30], [40, 50, 60]])
```

Use:

```python
arr[row, column]
```

Example:

```python
print(arr[0, 1])
```

Output:

```text
20
```

---

# 7. Slicing

Slicing extracts a subset of an array.

General syntax:

```python
array[start:stop:step]
```

### Important

The `stop` index is excluded.

Example:

```python
arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[1:4])
```

Output:

```text
[20 30 40]
```

Indexes `1`, `2`, and `3` are selected.

## 7.1 Start Omitted

```python
arr[:4]
```

Means:

- Start from the beginning.
- Stop before index `4`.

## 7.2 Stop Omitted

```python
arr[2:]
```

Means:

- Start at index `2`.
- Continue to the end.

## 7.3 Step

```python
arr[::2]
```

Selects every second element.

## 7.4 Reverse an Array

A useful NumPy technique:

```python
arr[::-1]
```

This reverses the array without a loop.

---

# 8. Fancy Indexing

Fancy indexing allows multiple specific indexes to be selected at once.

Example:

```python
arr = np.array([10, 20, 30, 40, 50])

result = arr[[0, 2, 4]]

print(result)
```

Output:

```text
[10 30 50]
```

Use fancy indexing when you need non-sequential elements.

General pattern:

```python
array[[index1, index2, index3]]
```

The selected result is treated as a separate selection rather than a normal contiguous slice.

---

# 9. Boolean Masking / Filtering

Boolean masking filters values according to a condition.

Example:

```python
arr = np.array([10, 20, 30, 40, 50])

result = arr[arr > 25]

print(result)
```

Output:

```text
[30 40 50]
```

The condition:

```python
arr > 25
```

creates a Boolean mask containing `True` and `False`.

Only values where the condition is `True` are returned.

## Why does it matter?

Boolean masking is extremely useful for:

- Filtering datasets
- Selecting values based on conditions
- Machine learning preprocessing
- Data analysis

It avoids writing manual loops for many filtering operations.

---

# 10. Reshaping

Reshaping changes an array's structure without changing its data.

Example:

```python
arr = np.array([1, 2, 3, 4, 5, 6])

reshaped = arr.reshape(2, 3)

print(reshaped)
```

Output:

```text
1 2 3
4 5 6
```

The original data still contains six values.

## Important Rule

The total number of elements must remain the same.

For example:

```text
6 elements -> 2 x 3
6 elements -> 3 x 2
6 elements -> 1 x 6
```

But:

```text
6 elements -> 2 x 4
```

is invalid because `2 x 4 = 8` elements.

## 10.1 `reshape()`

General form:

```python
arr.reshape(rows, columns)
```

Example:

```python
arr.reshape(2, 3)
```

Reshaping returns a view when possible rather than simply creating an independent copy.

---

# 11. Flattening: `ravel()` vs `flatten()`

Flattening converts a multidimensional array into a 1D array.

Suppose:

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
```

## 11.1 `ravel()`

```python
result = arr.ravel()
```

`ravel()` returns a view when possible.

Therefore, changes to the resulting view can affect the original array.

## 11.2 `flatten()`

```python
result = arr.flatten()
```

`flatten()` returns a copy.

Changes to the flattened copy do not modify the original array.

### Quick comparison

| Method | Result |
|---|---|
| `ravel()` | View when possible |
| `flatten()` | Copy |

---

# 12. Modifying Arrays

Real-world datasets change constantly.

You may need to:

- Add new values
- Remove unnecessary values
- Combine arrays
- Split arrays

NumPy arrays have a fixed-size structure, so operations such as insertion and deletion produce a new array rather than behaving like an in-place Python list operation.

## 12.1 `np.insert()`

Inserts values at a specified index.

General form:

```python
np.insert(array, index, value)
```

Example:

```python
arr = np.array([10, 20, 30, 40])

new_arr = np.insert(arr, 2, 100)

print(new_arr)
```

Result:

```text
[10 20 100 30 40]
```

The original array remains unchanged.

### 2D Arrays

For 2D arrays, `axis` controls whether insertion is row-wise or column-wise.

- `axis=0` means row-wise.
- `axis=1` means column-wise.

## 12.2 `np.append()`

Adds values to the end of an array.

```python
arr = np.array([10, 20, 30])

new_arr = np.append(arr, [40, 50, 60])

print(new_arr)
```

Result:

```text
[10 20 30 40 50 60]
```

## 12.3 `np.concatenate()`

Combines multiple arrays.

General form:

```python
np.concatenate((arr1, arr2), axis=...)
```

For 1D arrays:

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.concatenate((arr1, arr2))

print(result)
```

Result:

```text
[1 2 3 4 5 6]
```

For multidimensional arrays, `axis` determines how they are joined.

## 12.4 `np.delete()`

Deletes an element or section.

General form:

```python
np.delete(array, index, axis=...)
```

Example:

```python
arr = np.array([10, 20, 30, 40])

new_arr = np.delete(arr, 0)

print(new_arr)
```

Result:

```text
[20 30 40]
```

For a 2D array:

- `axis=0` deletes rows.
- `axis=1` deletes columns.

---

# 13. Stacking and Splitting

## 13.1 `np.vstack()`

Vertical stacking combines arrays row-wise.

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.vstack((arr1, arr2))
```

Conceptually:

```text
1 2 3
4 5 6
```

## 13.2 `np.hstack()`

Horizontal stacking combines arrays side-by-side.

```python
result = np.hstack((arr1, arr2))
```

Conceptually:

```text
1 2 3 4 5 6
```

### Remember

```text
vstack -> vertical
hstack -> horizontal
```

## 13.3 `np.split()`

Splits an array into multiple sub-arrays.

Example:

```python
arr = np.array([10, 20, 30, 40, 50, 60])

result = np.split(arr, 2)
```

Conceptually:

```text
[10 20 30]
[40 50 60]
```

The split must be compatible with the array's size.

For example, trying to divide six elements into twenty equal parts produces a `ValueError`.

## 13.4 `np.hsplit()` and `np.vsplit()`

For multidimensional arrays:

- `hsplit()` → horizontal splitting
- `vsplit()` → vertical splitting

---

# 14. Broadcasting

Broadcasting allows NumPy to perform operations on arrays of compatible shapes without explicitly writing loops.

Example:

```python
prices = np.array([100, 200, 300])
discount = 10

final_prices = prices - (prices * discount / 100)

print(final_prices)
```

Result:

```text
[ 90. 180. 270.]
```

The scalar `10` is automatically applied to every element.

Without NumPy, you might write a loop.

With broadcasting, NumPy applies the operation automatically.

## 14.1 Broadcasting Rules

### Rule 1: Matching Dimensions

If two arrays have compatible/same shapes, operations can be performed element-wise.

Example:

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr1 + arr2
```

Result:

```text
[5 7 9]
```

### Rule 2: Single Value / Scalar Expansion

A single value can be applied to every element.

```python
arr = np.array([100, 200, 300])

arr * 2
```

Result:

```text
[200 400 600]
```

No loop is required.

### Rule 3: Incompatible Shapes

If shapes cannot be made compatible through broadcasting, NumPy raises an error.

For example, arrays with incompatible dimensions cannot simply be combined element-wise.

## 14.2 1D + 2D Broadcasting

A 1D array can sometimes be broadcast across a 2D array when their shapes are compatible.

Example:

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])

vector = np.array([10, 20, 30])

result = matrix + vector
```

The vector is applied across the rows.

---

# 15. Vectorisation

Vectorisation means applying an operation to an entire array without manually writing Python loops.

Example:

```python
arr = np.array([10, 20, 30])

result = arr * 3
```

The multiplication is applied to every element.

## 15.1 Python Loop Approach

Conceptually:

```python
result = []

for value in values:
    result.append(value * 3)
```

## 15.2 NumPy Vectorised Approach

```python
result = np.array(values) * 3
```

The NumPy approach is concise and designed for efficient numerical computation.

## 15.3 Broadcasting vs Vectorisation

### Broadcasting

- Describes how NumPy handles compatible arrays of different shapes/scalars.
- Allows smaller data to be expanded logically to match larger data.

### Vectorisation

- Describes applying an operation to many/all elements without explicit Python loops.

They are related, but they are **not the same concept**.

---

# 16. Handling Missing Values and Infinity

Real-world datasets often contain:

- Missing values
- Invalid values
- Infinite values
- Duplicate records
- Incorrect values

NumPy provides functions to help detect and handle numerical missing/infinite values.

## 16.1 `np.isnan()`

Used to detect `NaN` values.

`NaN` means **Not a Number**.

Example:

```python
arr = np.array([1, 2, np.nan, 4, np.nan])

print(np.isnan(arr))
```

The result is a Boolean array.

`True` indicates a `NaN` value.

## 16.2 `np.nan_to_num()`

Can replace `NaN` and infinite values with usable numerical values.

Example:

```python
arr = np.array([1, np.nan, 3])

clean = np.nan_to_num(arr)
```

By default, `NaN` values are replaced with zero.

You can specify replacement values as needed.

This is useful before numerical calculations or machine-learning preprocessing.

## 16.3 `np.isinf()`

Used to detect infinite values.

Example:

```python
arr = np.array([1, np.inf, -np.inf])

print(np.isinf(arr))
```

The result identifies infinite entries with Boolean values.

Positive and negative infinity can occur in numerical computations, for example when calculations approach values outside the useful numerical range or involve problematic division.

---

# NumPy Quick Reference

| Topic | Main Function / Property |
|---|---|
| Create array | `np.array()` |
| Zeros | `np.zeros()` |
| Ones | `np.ones()` |
| Specific value | `np.full()` |
| Number sequence | `np.arange()` |
| Identity matrix | `np.eye()` |
| Dimensions | `.shape` |
| Number of elements | `.size` |
| Number of dimensions | `.ndim` |
| Data type | `.dtype` |
| Indexing | `arr[index]` |
| 2D indexing | `arr[row, column]` |
| Slicing | `arr[start:stop:step]` |
| Fancy indexing | `arr[[...]]` |
| Boolean filtering | `arr[condition]` |
| Reshape | `.reshape()` |
| View flattening | `.ravel()` |
| Copy flattening | `.flatten()` |
| Insert | `np.insert()` |
| Append | `np.append()` |
| Combine | `np.concatenate()` |
| Delete | `np.delete()` |
| Vertical stack | `np.vstack()` |
| Horizontal stack | `np.hstack()` |
| Split | `np.split()` |
| Horizontal split | `np.hsplit()` |
| Vertical split | `np.vsplit()` |
| Missing values | `np.isnan()` |
| Replace NaN/infinity | `np.nan_to_num()` |
| Detect infinity | `np.isinf()` |

---

## What I Learned

Through these notes, I learned the fundamentals of NumPy, including:

- Creating and understanding NumPy arrays
- Working with 1D, 2D, and multidimensional arrays
- Array indexing and slicing
- Fancy indexing and Boolean masking
- Reshaping and flattening
- Modifying and combining arrays
- Stacking and splitting
- Broadcasting
- Vectorisation
- Handling `NaN` and infinite values

These concepts form an important foundation for **Data Analysis, Data Science, Machine Learning, and Scientific Computing with Python**.
