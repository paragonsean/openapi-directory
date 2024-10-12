# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="AWS App Mesh",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS App Mesh"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;AWS App Mesh is a service mesh based on the Envoy proxy that makes it easy to monitor and          control containerized microservices. App Mesh standardizes how your microservices          communicate, giving you end-to-end visibility and helping to ensure high-availability for          your applications.&lt;/p&gt;          &lt;p&gt;App Mesh gives you consistent visibility and network traffic controls for every          microservice in an application. You can use App Mesh with Amazon ECS          (using the Amazon EC2 launch type), Amazon EKS, and Kubernetes on AWS.&lt;/p&gt;          &lt;note&gt;             &lt;p&gt;App Mesh supports containerized microservice applications that use service discovery             naming for their components. To use App Mesh, you must have a containerized application             running on Amazon EC2 instances, hosted in either Amazon ECS, Amazon EKS, or Kubernetes on AWS. For             more information about service discovery on Amazon ECS, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html\&quot;&gt;Service Discovery&lt;/a&gt; in the                &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;. Kubernetes &lt;code&gt;kube-dns&lt;/code&gt; is supported.             For more information, see &lt;a href&#x3D;\&quot;https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/\&quot;&gt;DNS                for Services and Pods&lt;/a&gt; in the Kubernetes documentation.&lt;/p&gt;          &lt;/note&gt;
    """
)

