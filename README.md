


# Scientific Computing with Python - Second Edition

<a href="https://www.packtpub.com/product/Scientific-Computing-with-Python-Second-Edition/9781838822323?utm_source=github&utm_medium=repository&utm_campaign=9781838982881"><img src="https://static.packt-cdn.com/products/9781838822323/cover/smaller" alt="Scientific Computing with Python - Second Edition" height="256px" align="right"></a>

This is the code repository for [Scientific Computing with Python - Second Edition](https://www.packtpub.com/product/Scientific-Computing-with-Python-Second-Edition/9781838822323?utm_source=github&utm_medium=repository&utm_campaign=9781838822323), published by Packt.

**High-performance scientific computing with NumPy, SciPy, and pandas**

## What is this book about?
Python has tremendous potential within the scientific computing domain. This updated edition of Scientific Computing with Python features new chapters on graphical user interfaces, efficient data processing, and parallel computing to help you perform mathematical and scientific computing efficiently using Python.

This book will help you to explore new Python syntax features and create different models using scientific computing principles. The book presents Python alongside mathematical applications and demonstrates how to apply Python concepts in computing with the help of examples involving Python 3.8. You'll use pandas for basic data analysis to understand the modern needs of scientific computing, and cover data module improvements and built-in features. You'll also explore numerical computation modules such as NumPy and SciPy, which enable fast access to highly efficient numerical algorithms. By learning to use the plotting module Matplotlib, you will be able to represent your computational results in talks and publications. A special chapter is devoted to SymPy, a tool for bridging symbolic and numerical computations.

By the end of this Python book, you'll have gained a solid understanding of task automation and how to implement and test mathematical algorithms within the realm of scientific computing.

This book covers the following exciting features: 
* Understand the building blocks of computational mathematics, linear algebra, and related Python objects
* Use Matplotlib to create high-quality figures and graphics to draw and visualize results
* Apply object-oriented programming (OOP) to scientific computing in Python
* Discover how to use pandas to enter the world of data processing
* Handle exceptions for writing reliable and usable code
* Cover manual and automatic aspects of testing for scientific programming
* Get to grips with parallel computing to increase computation speed

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1838822321) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders.

The code will look like the following:
```
t=symbols('t')
x=[0,t,1]

# The Vandermonde Matrix
V = Matrix([[0, 0, 1], [t**2, t, 1], [1, 1,1]])
y = Matrix([0,1,-1]) # the data vector
a = simplify(V.LUsolve(y)) # the coefficients
# the leading coefficient as a function of the parameter
a2 = Lambda(t,a[0])

```

**Following is what you need for this book:**
This book is for students with a mathematical background, university teachers designing modern courses in programming, data scientists, researchers, developers, and anyone who wants to perform scientific computation in Python. The book evolved from 13 years of Python teaching in undergraduate science and engineering programs, as special industry in-house courses and specialization courses for high school teachers. The typical reader has the need to use Python in areas like mathematics, big data processings, machine learning and simulation. Therefore a basic knowledge of vectors and matrices as well of notions like convergence and iterative processes is beneficial.

This book is intended for beginners or readers who have some experience in programming. You can read the book either from the first page to the last, or by picking the bits that seem most interesting. Prior knowledge of Python is not mandatory.

With the following software and hardware list you can run all code files present in the book (Chapter 1-9).

### Software and Hardware List

| Chapter  | Software required                                                                    | OS required                        |
| -------- | -------------------------------------------------------------------------------------| -----------------------------------|
|  1 - 19  |   Anaconda, Python 3.8, JupyterLab                                           				| Windows, Mac OS X, and Linux (Any) |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781838822323_ColorImages.pdf).


### Related products <Other books you may enjoy>
* Learn Amazon SageMaker [[Packt]](https://www.packtpub.com/product/learn-amazon-sagemaker/9781800208919) [[Amazon]](https://www.amazon.com/dp/180020891X)

* Python Data Cleaning Cookbook [[Packt]](https://www.packtpub.com/product/python-data-cleaning-cookbook/9781800565661) [[Amazon]](https://www.amazon.com/dp/1800565666)

## Get to Know the Author
**Claus Führer** is a professor of scientific computations at Lund University, Sweden. He has an extensive teaching record that includes intensive programming courses in numerical analysis and engineering mathematics across various levels in many different countries and teaching environments. Claus also develops numerical software in research collaboration with industry and received Lund University’s Faculty of Engineering Best Teacher Award in 2016.

**Olivier Verdier** began using Python for scientific computing back in 2007 and received a PhD in mathematics from Lund University in 2009. He has held post-doctoral positions in Cologne, Trondheim, Bergen, and Ume and is now an associate professor of mathematics at Bergen University College, Norway.

**Jan Erik Solem** is a Python enthusiast, former associate professor, and computer vision entrepreneur. He co-founded several computer vision startups, most recently Mapillary, a street imagery computer vision company, and has worked in the tech industry for two decades. Jan Erik is a World Economic Forum technology pioneer and won the Best Nordic Thesis Award 2005-2006 for his dissertation on image analysis and pattern recognition. He is also the author of "Programming Computer Vision with Python" (O'Reilly 2012).

### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781838822323">https://packt.link/free-ebook/9781838822323 </a> </p>