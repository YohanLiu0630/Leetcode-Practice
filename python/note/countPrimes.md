先把“找素数”分成两类，因为不同任务适合的算法完全不一样：
- 判断一个数 \(x\) 是不是素数
- 找出 \(1\sim n\) 之间所有素数

### 1. 试验法
俗称一个个尝试，用于判断某一个数是不是素数
```python
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
```
但是可以将 i 的范围优化到 $[2,\sqrt{n}]$，因为如果一个数存在质数因子则必然有一个银子小于$\sqrt{n}$，于是有了
```python
def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True
```
### 2. 埃拉托色尼筛法

如果题目是：

> 找出 1～1000000 中所有素数

你如果对每个数都做一次 $\sqrt{n}$ 试除，就比较浪费。

埃氏筛的想法就是：

> 我知道 2 是素数，那么 2 的所有倍数都不可能是素数。  
> 我知道 3 是素数，那么 3 的所有倍数都不可能是素数。

例如：

```text
2 3 4 5 6 7 8 9 10 11 12 ...
```

先找到 `2`：

```text
2 3 X 5 X 7 X 9 X 11 X ...
```

然后 `3`：

```text
2 3 X 5 X 7 X X X 11 X ...
```
以此类推排除掉所有的合数剩下的就是素数了
```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]
```
复杂度非常漂亮：

$$
O(n\log\log n)
$$

基本接近线性。

---

其中两个埃氏筛的优化点
1. 优化 1：只筛到 $\sqrt{n}$

外层：

```python
for i in range(2, int(n ** 0.5) + 1):
```

为什么？

因为大于 $\sqrt{n}$ 的合数早就已经被前面的因数筛掉了。

---

2. 优化 2：从 `i * i` 开始筛

这一点非常重要：

```python
for j in range(i * i, n + 1, i):
```

而不是：

```python
for j in range(i * 2, n + 1, i):
```

比如现在 `i = 5`。

你没必要再筛：

```text
10 = 5 × 2
15 = 5 × 3
20 = 5 × 4
```

因为：

- `10` 已经被 `2` 筛掉
- `15` 已经被 `3` 筛掉
- `20` 已经被 `2` 筛掉

所以直接：

```text
25 = 5 × 5
```

开始就可以了。

这也是为什么：

$$
i^2
$$

是一个很自然的起点。

---

3. 优化 3：只筛选奇数
因为偶数（除了2）一定不是素数，于是可以在第一层循环里调整一下，便可以排除所有的偶数，并且第二层循环里改变一下步长将偶数因子排除考虑，因为偶数因子乘出来一定是偶数，但是偶数已经被排除了无需再考虑

```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(4, n+ 1, 2):
            is_Prime[i] = False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if is_prime[i]:
            for j in range(i * i, n + 1, 2 * i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]
```

### 欧拉筛 / 线性筛
欧拉筛第一次看确实比埃氏筛绕，因为它不是“看到一个素数就把它的倍数全划掉”，而是在做一件更精细的事：

>让每一个合数，只被它的最小质因数筛掉一次。
```python
def euler_sieve(n):
    primes = []
    is_prime = [True] * (n + 1)

    for i in range(2, n + 1):

        if is_prime[i]:
            primes.append(i)

        for p in primes:

            if i * p > n:
                break

            is_prime[i * p] = False

            if i % p == 0:
                break

    return primes
```