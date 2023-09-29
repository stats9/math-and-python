# Joint Probability for iid Variables

## Problem

$$
\begin{align}
& \text{Prove that if} \quad X_1, X_2, \dots, X_n \overset{iid}{\sim} F(X), \quad \text{and}\\
& X_i ~~\text{is continuous variable}, \quad i \in (1, 2, \dots, n), \\
& \implies \mathcal{P}(X_{k_1} \leq X_{k_2} \leq X_{k_3} \leq \cdots \leq X_{k_n}) = \frac{1}{n!}, \\
& \text{and} \quad k_i \in (1, 2, 3, \dots, n), \quad k_i \ne k_j, ~~ \forall ~~ i, j \in  (1, 2, 3, \dots, n), ~~ i \ne j.
\end{align}
$$

   

## We will prove this relation for a specific case, we will generalize it for other cases.

  
  

$$
\begin{aligned}
& \text{if}\quad \langle k_1, k_2, k_3, \dots, k_n\rangle  = \langle 1, 2, 3, \dots, n \rangle \implies \\
& \mathbb{P} = \mathcal{P}(X_{k_1} \leq X_{k_2} \leq X_{k_3}\leq \cdots \leq X_{k_n}) = \mathcal{P}(X_1 \leq X_2 \leq X_3 \leq \cdots \leq X_n), \\
& \mathbb{P} = \int_{-\infty}^{+\infty}\int_{x_1}^{+\infty}\int_{x_2}^{+\infty}\int_{x_3}^{+\infty}\cdots\int_{x_{n-1}}^{+\infty}\prod_{i = 1}^n f(x_i)~dx_ndx_{n-1}dx_{n-2}\cdots dx_2dx_1 = \\
& \int_{-\infty}^{+\infty}f(x_1)\int_{x_1}^{+\infty}f(x_2)\int_{x_2}^{+\infty}f(x_3)\int_{x_3}^{+\infty}f(x_4)\cdots\int_{x_{n-1}}^{+\infty}f(x_n)dx_{n-1}dx_{n-2}\cdots dx_2dx_1 = \\
& \int_{-\infty}^{+\infty}f(x_1)\int_{x_1}^{+\infty}f(x_2)\int_{x_2}^{+\infty}f(x_3)\int_{x_3}^{+\infty}f(x_4)\cdots\int_{x_{n-1}}^{+\infty}\frac{d}{dx_n}F(x_n)dx_{n-1}dx_{n-2}\cdots dx_2dx_1, \\
\end{aligned}
$$

$$
\begin{aligned}
& \text{We know that if}~~X_i ~~\text{is continuous Variable}\implies F(X_i)\sim \text{Unif}(0, 1) \implies \\
& \mathbb{P} = \int_{-\infty}^{+\infty}f(x_1)\int_{x_1}^{+\infty}f(x_2)\cdots
\int_{x_{n-1}}^{+\infty}dF(x_{n})dx_{n-1}\cdots dx_2dx_1 = \\
& \int_{x_{n-1}}^{+\infty}f(x_1)\int_{x_2}^{+\infty}f(x_2)\cdots
\int_{x_{n-2}}^{+\infty}f(x_{n-1})(1 - F(x_{n-1}))dx_{n-1}\cdots dx_2dx_1 = \\
& \int_{x_{n-1}}^{+\infty}f(x_1)\int_{x_2}^{+\infty}f(x_2)\cdots
\int_{x_{n-2}}^{+\infty}\frac{d}{dx_{n-1}}F(x_{n-1})(1 - F(x_{n-1}))dx_{n-1}\cdots dx_2dx_1 = \\
& \int_{-\infty}^{+\infty}f(x_1) \int_{x_1}^{+\infty} f(x_2)\cdots \int_{F(x_{n-2})}^1 (1 - F(x_{n-1}))dF(x_{n-1})\cdots dx_1 =\\
& \int_{-\infty}^{+\infty}f(x_1)\int_{x_1}^{+\infty}\int\cdots\int_{x_{n-3}}^{+\infty}\frac{1}{2} - (F(x_{n-2}-\frac{F(x_{n-2})^2}{2}))dx_{n-2}\cdots dx_1, 
\end{aligned}
$$

##### as before

$$
\begin{aligned}
& \mathbb{P} = \int_{-\infty}^{+\infty}f(x_1)\int_{x_1}^{+\infty}\int\cdots\int_{x_{n-4}}^{+\infty}\frac{1}{3!} - (\frac{F(x_{n-3})}{2}-\frac{F(x_{n-3})^2}{2}+\frac{F(x_{n-3})^3}{3!})dF(x_{n-3})\cdots dx_1 = \\
& \int_{-\infty}^{+\infty}f(x_1)\int_{x_1}^{+\infty}\int\cdots\int_{x_{n-5}}^{+\infty}\frac{1}{4!} - (\frac{F(x_{n-4})}{3!}-\frac{F(x_{n-4})^2}{2\times 2!}+\frac{F(x_{n-3})^3}{3!} - \frac{F(x_{n-4})^4}{4!})dF(x_{n-4})\cdots dx_1, 
\end{aligned}
$$

##### If we continue in the same way, in the following, we will reach an expression set in the form below in each time of integration;

$$
\mathbb{P} = \int_{-\infty}^{+\infty} f(x_1) \int_{x_1}^{+\infty}f(x_2) \cdots \int_{x_{n-k}}^{+\infty}g(F(x_{n-(k-1)}), k)dF(x_{n-(k-1)})\cdots dx_1 \to 
$$

##### that `g` function is a polynomial function of degree `K`

  

###### form of `g` function

$$
\begin{aligned}
& \int g(x, 1)~dx = x, \\
& \int g(x, 2)~dx = x - \frac{x^2}{2}, \\
& \int g(x, 3)~dx = \frac{x}{2}-\frac{x^2}{2} + \frac{x^3}{3!}, \\
& \int g(x, 4)~dx = \frac{x}{3!} -\frac{x^2}{2 \times 2!} + \frac{x^3}{3!} - \frac{x^4}{4!}, \\
& \int g(x, 5) ~ dx = \frac{x}{4!} -\frac{x^2}{2 \times 3!} + \frac{x^3}{2 \times 3!} - \frac{x^4}{4!} + \frac{x^5}{5!}, \\
& \int g(x, 6) ~ dx = \frac{x}{5!} -\frac{x^2}{2 \times 4!} + \frac{x^3}{3 \times 3!} - \frac{x^4}{2 \times 4!} + \frac{x^5}{5!} - \frac{x^6}{6!}, \\
& \int g(x, 7) ~ dx = \frac{x}{6!} -\frac{x^2}{2 \times 5!} + \frac{x^3}{4! \times 3!} - \frac{x^4}{3! \times 4!} + \frac{x^5}{2 \times 5!} - \frac{x^6}{6!} + \frac{x^7}{7!}, \\
& \vdots \\
& \int g(x, k)~ dx = \sum_{i = 1}^k (-1)^{i + 1} \times \frac{x^i}{i! \times (k - i)!} \implies 
\end{aligned}
$$

 

$$
\mathbb{P} = \int_{-\infty}^{+\infty} g(F(x_1), n)~dx_1 = \sum_{i = 1}^n (-1)^{i + 1} \times \frac{F(x_1)^i}{i! \times (k-i)!}|_{-\infty}^{+\infty} 
$$

###### We Know That

$$
F(+\infty) = 1, \quad F(-\infty) = 0 \implies 
$$

 

$$
\begin{aligned}
& \mathbb{P} = \sum{i = 1}^n (-1)^{i + 1} \frac{1}{i! \times (n-i)!} = \\
& \frac{1}{n!} \times \sum_{i = 1}^n (-1)^{i + 1} \frac{n!}{i! \times (n-i)!} = \\
& \frac{1}{n!} \sum_{i = 1}^n {n \choose i} (-1)^{i + 1} = \\
& \frac{-1}{n!} \sum_{i = 1}^n {n \choose i} (-1)^{i} = \\
& \frac{-1}{n!} \sum_{i = 1}^n {n \choose i} (-1)^{i} \times (1)^{(n - i)} = \\
& \frac{-1}{n!} ((-1 + 1)^n - (-1)^0 = \\
\frac{1}{n!}
\end{aligned}
$$

------------------------------------------------------------------------

------------------------------------------------------------------------

#### Experimental proof for n<sup>th</sup> equal to 3 and 4
