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
    description="AWS CodeStar",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS CodeStar"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;AWS CodeStar&lt;/fullname&gt; &lt;p&gt;This is the API reference for AWS CodeStar. This reference provides descriptions of the operations and data types for the AWS CodeStar API along with usage examples.&lt;/p&gt; &lt;p&gt;You can use the AWS CodeStar API to work with:&lt;/p&gt; &lt;p&gt;Projects and their resources, by calling the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeleteProject&lt;/code&gt;, which deletes a project.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DescribeProject&lt;/code&gt;, which lists the attributes of a project.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ListProjects&lt;/code&gt;, which lists all projects associated with your AWS account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ListResources&lt;/code&gt;, which lists the resources associated with a project.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ListTagsForProject&lt;/code&gt;, which lists the tags associated with a project.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TagProject&lt;/code&gt;, which adds tags to a project.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UntagProject&lt;/code&gt;, which removes tags from a project.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UpdateProject&lt;/code&gt;, which updates the attributes of a project.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Teams and team members, by calling the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AssociateTeamMember&lt;/code&gt;, which adds an IAM user to the team for a project.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DisassociateTeamMember&lt;/code&gt;, which removes an IAM user from the team for a project.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ListTeamMembers&lt;/code&gt;, which lists all the IAM users in the team for a project, including their roles and attributes.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UpdateTeamMember&lt;/code&gt;, which updates a team member&#39;s attributes in a project.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Users, by calling the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreateUserProfile&lt;/code&gt;, which creates a user profile that contains data associated with the user across all projects.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeleteUserProfile&lt;/code&gt;, which deletes all user profile information across all projects.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DescribeUserProfile&lt;/code&gt;, which describes the profile of a user.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ListUserProfiles&lt;/code&gt;, which lists all user profiles.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UpdateUserProfile&lt;/code&gt;, which updates the profile for a user.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

