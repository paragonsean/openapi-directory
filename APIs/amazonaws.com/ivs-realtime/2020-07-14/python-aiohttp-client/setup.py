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
    description="Amazon Interactive Video Service RealTime",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Interactive Video Service RealTime"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt; &lt;b&gt;Introduction&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The Amazon Interactive Video Service (IVS) real-time API is REST compatible, using a standard HTTP API and an AWS EventBridge event stream for responses. JSON is used for both requests and responses, including errors. &lt;/p&gt; &lt;p&gt;Terminology:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A &lt;i&gt;stage&lt;/i&gt; is a virtual space where participants can exchange video in real time.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;i&gt;participant token&lt;/i&gt; is a token that authenticates a participant when they join a stage.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;i&gt;participant object&lt;/i&gt; represents participants (people) in the stage and contains information about them. When a token is created, it includes a participant ID; when a participant uses that token to join a stage, the participant is associated with that participant ID There is a 1:1 mapping between participant tokens and participants.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Resources&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The following resources contain information about your IVS live stream (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started.html\&quot;&gt;Getting Started with Amazon IVS Real-Time Streaming&lt;/a&gt;):&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Stage&lt;/b&gt; — A stage is a virtual space where participants can exchange video in real time.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Tagging&lt;/b&gt; &lt;/p&gt; &lt;p&gt;A &lt;i&gt;tag&lt;/i&gt; is a metadata label that you assign to an AWS resource. A tag comprises a &lt;i&gt;key&lt;/i&gt; and a &lt;i&gt;value&lt;/i&gt;, both set by you. For example, you might set a tag as &lt;code&gt;topic:nature&lt;/code&gt; to label a particular video category. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging AWS Resources&lt;/a&gt; for more information, including restrictions that apply to tags and \&quot;Tag naming limits and requirements\&quot;; Amazon IVS stages has no service-specific constraints beyond what is documented there.&lt;/p&gt; &lt;p&gt;Tags can help you identify and organize your AWS resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\&quot;&gt;Access Tags&lt;/a&gt;).&lt;/p&gt; &lt;p&gt;The Amazon IVS real-time API has these tag-related endpoints: &lt;a&gt;TagResource&lt;/a&gt;, &lt;a&gt;UntagResource&lt;/a&gt;, and &lt;a&gt;ListTagsForResource&lt;/a&gt;. The following resource supports tagging: Stage.&lt;/p&gt; &lt;p&gt;At most 50 tags can be applied to a resource.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Stages Endpoints&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateParticipantToken&lt;/a&gt; — Creates an additional token for a specified stage. This can be done after stage creation or when tokens expire.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateStage&lt;/a&gt; — Creates a new stage (and optionally participant tokens).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStage&lt;/a&gt; — Shuts down and deletes the specified stage (disconnecting all participants).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DisconnectParticipant&lt;/a&gt; — Disconnects a specified participant and revokes the participant permanently from a specified stage.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetParticipant&lt;/a&gt; — Gets information about the specified participant token.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetStage&lt;/a&gt; — Gets information for the specified stage.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetStageSession&lt;/a&gt; — Gets information for the specified stage session.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListParticipantEvents&lt;/a&gt; — Lists events for a specified participant that occurred during a specified stage session.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListParticipants&lt;/a&gt; — Lists all participants in a specified stage session.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStages&lt;/a&gt; — Gets summary information about all stages in your account, in the AWS region where the API request is processed.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStageSessions&lt;/a&gt; — Gets all sessions for a specified stage.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateStage&lt;/a&gt; — Updates a stage’s configuration.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Tags Endpoints&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListTagsForResource&lt;/a&gt; — Gets information about AWS tags for the specified ARN.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;TagResource&lt;/a&gt; — Adds or updates tags for the AWS resource with the specified ARN.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UntagResource&lt;/a&gt; — Removes tags from the resource with the specified ARN.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

