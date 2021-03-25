# Pre course instructions


## Packages

This introduction to machine learning in python course requires you to have a range of packages installed on your machine.

The versions of these packages required are new, and therefore may need to be reinstalled.

To guarantee that you can run all of the code in this course it is expected that you have the following versions of the following packages:

* matplotlib==3.3.3
* numpy==1.19.5
* pandas==1.1.5
* scikit-learn==0.24.1
* scipy==1.5.4

Newer or older versions may work, however this is not guarenteed.

### Overwriting your current package versions

Within this /pre_course/ folder is a file called `requirements.txt`. This contains all packages, their versions and their dependencies required for this course.

You can install all the packages at once, assuming you have set up `pip` on your machine.

This is done in **Anaconda Prompt** or your prefered command line interface.

Write out:

```
>pip install -r requirements.txt
```

You may need to add a path to `requirements.txt` depending on where your working directory is.

This will install the versions **OVER** any existing versions you have on your computer. If this is not the be

If you prefer to install each package one by one you can use:

```
>pip install scipy==1.5.4
```

In the example of `scipy` and our chosen version number.

### Virtual Environments

It is recommended to use a virtual environment to protect package dependencies for projects. 

To install the packages for this course with a virtual enviornment see the instructions within `/pre_course/venv.html`.

