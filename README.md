# Fall 2018 Dealing with Data Class - Professor Norman White

This class is designed to teach students some of the basic concepts of Dealing with Data, especially for data scientists.
It introduces many of the skills and technologies that data scientists use to retrieve, manipulate, store and analyze data sets.
Students will learn the basics of linux, python, SQL, regular expressions, using APIs, common data sources, as well as some  data mining examples.

The class is taught in a hands-on environment,  where every student has their own dedicated machine that runs the [jupyter](http://jupyter.org) interactive python environment. Students are expected to bring their notebook computers to each class, as we will be going through the exercises together, including in-class mini assignments.
There are prebuilt Jupyter notebooks that have working examples of python, pandas, SQL, linux, ... code that can be run interactively and easily modified. The Jupyter notebooks allow students to intermix code and output, so they can see and save the work they have done.

New and changed notebooks are automatically downloaded during the term. Students do in-class exercises using their notebooks, and submit notebooks as their homework assignments.


### How to access your  jupyterhub server. (Your server is setup and deployed the first time you login to the class.)

* [Accessing your Data Science Environment](https://docs.google.com/document/d/1A5Y53eqBRRlrVMV-yLrpA9-3xZ3jQmv9i6qhOU5gn44/edit?usp=sharing)

We setup and deploy our data science environment (effectively, Jupyter with Python and R support, plus MySQL) using [docker containers](https://docker.com/resources/what-container). Each student has their own docker container, preloaded with notebooks and data for the course. Docker containers give each student the equivalent of their own computer, isolated from the other students systems. [Kubernetes](https://kubernetes.io) is a system for automatically deploying docker containers, and allows us to support many classes and students. As our default option, we allow students to connect to a [JupyterHub server](http://jupyter.org/hub) that runs on Kubernetes. When a student logs into the server, their private docker container is deployed. We also give the option to students to run the same environment locally on their laptops, or deploy the Docker image on AWS or Google Cloud. These options allow students some flexibility, but don't support all of the capabilities of the default Jupyterhub environment.

## Data Sets

* [List of interesting data sets](DATA_SOURCES.md)

## Related Courses

* [List of related courses](COURSES.md)
