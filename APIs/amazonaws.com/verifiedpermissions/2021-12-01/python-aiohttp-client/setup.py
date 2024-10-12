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
    description="Amazon Verified Permissions",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Verified Permissions"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Amazon Verified Permissions is a permissions management service from Amazon Web Services. You can use Verified Permissions to manage permissions for your application, and authorize user access based on those permissions. Using Verified Permissions, application developers can grant access based on information about the users, resources, and requested actions. You can also evaluate additional information like group membership, attributes of the resources, and session context, such as time of request and IP addresses. Verified Permissions manages these permissions by letting you create and store authorization policies for your applications, such as consumer-facing web sites and enterprise business systems.&lt;/p&gt; &lt;p&gt;Verified Permissions uses Cedar as the policy language to express your permission requirements. Cedar supports both role-based access control (RBAC) and attribute-based access control (ABAC) authorization models.&lt;/p&gt; &lt;p&gt;For more information about configuring, administering, and using Amazon Verified Permissions in your applications, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/\&quot;&gt;Amazon Verified Permissions User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information about the Cedar policy language, see the &lt;a href&#x3D;\&quot;https://docs.cedarpolicy.com/\&quot;&gt;Cedar Policy Language Guide&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When you write Cedar policies that reference principals, resources and actions, you can define the unique identifiers used for each of those elements. We strongly recommend that you follow these best practices:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Use values like universally unique identifiers (UUIDs) for all principal and resource identifiers.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;For example, if user &lt;code&gt;jane&lt;/code&gt; leaves the company, and you later let someone else use the name &lt;code&gt;jane&lt;/code&gt;, then that new user automatically gets access to everything granted by policies that still reference &lt;code&gt;User::\&quot;jane\&quot;&lt;/code&gt;. Cedar can’t distinguish between the new user and the old. This applies to both principal and resource identifiers. Always use identifiers that are guaranteed unique and never reused to ensure that you don’t unintentionally grant access because of the presence of an old identifier in a policy.&lt;/p&gt; &lt;p&gt;Where you use a UUID for an entity, we recommend that you follow it with the // comment specifier and the ‘friendly’ name of your entity. This helps to make your policies easier to understand. For example: principal &#x3D;&#x3D; User::\&quot;a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111\&quot;, // alice&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Do not include personally identifying, confidential, or sensitive information as part of the unique identifier for your principals or resources.&lt;/b&gt; These identifiers are included in log entries shared in CloudTrail trails.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/important&gt; &lt;p&gt;Several operations return structures that appear similar, but have different purposes. As new functionality is added to the product, the structure used in a parameter of one operation might need to change in a way that wouldn&#39;t make sense for the same parameter in a different operation. To help you understand the purpose of each, the following naming convention is used for the structures:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Parameter type structures that end in &lt;code&gt;Detail&lt;/code&gt; are used in &lt;code&gt;Get&lt;/code&gt; operations.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Parameter type structures that end in &lt;code&gt;Item&lt;/code&gt; are used in &lt;code&gt;List&lt;/code&gt; operations.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Parameter type structures that use neither suffix are used in the mutating (create and update) operations.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

