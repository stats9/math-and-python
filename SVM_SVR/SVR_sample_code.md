# Support Vector Regression (SVR)


- [Using python](#using-python)
  - [loading require libraries](#loading-require-libraries)
  - [Generate data](#generate-data)
    - [add noise to data](#add-noise-to-data)
  - [Fit SVR Model with linear
    kernel](#fit-svr-model-with-linear-kernel)

<br><br><br>

# Using python

------------------------------------------------------------------------

## loading require libraries

``` python
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.svm import SVR 
import matplotlib.animation as animation  
from celluloid import Camera
```

## Generate data

``` python
np.random.seed(1234)
xx = np.sort(5 * np.random.rand(40, 1), axis = 0)
# xx
yy = np.sin(xx).flatten()
# yy
```

### add noise to data

``` python
np.random.seed(1234)
err = np.random.rand(40)
yy += err 
```

## Fit SVR Model with linear kernel

``` python
Tol = [0.01, 0.05, 0.1, 0.2, 0.5, 1, 5]


fig = plt.figure(figsize = (9, 9))
camera = Camera(fig)

for k in Tol: 
    Model_temp = SVR(kernel = 'linear', tol = k)
    Model_temp.fit(xx, yy)
    pred = Model_temp.predict(xx) 
    plt.scatter(x = xx, y = yy, color = 'red', s = 50)
    snapp = plt.plot(xx, pred)
    plt.legend(snapp, [f'Tolerance:{k}'])
    camera.snap() 
# animation = camera.animate()

animation = camera.animate(interval=500, blit=True)  
animation.save('animation.mp4', writer='ffmpeg', fps = 1.5)  
plt.show()
```

![see this
video:](https://github.com/stats9/math-and-python/blob/master/SVM_SVR/animation.mp4)

------------------------------------------------------------------------
