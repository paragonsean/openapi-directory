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
    description="ContentGroove API",
    author_email="",
    url="",
    keywords=["OpenAPI", "ContentGroove API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    # Overview  The ContentGroove Developer API enables you to add the power of ContentGroove&#39;s video AI to your own applications and workflows.  Webhooks are a way for ContentGroove to send video information to your application, to update your system and/or trigger other business processes.  You can use Webhooks and the Developer API separately or together.  # Getting Started with Webhooks  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Read \&quot;Using Webhooks\&quot; on the [API Reference page](https://developers.contentgroove.com/api_reference) - Visit the [Webhooks page](https://app.contentgroove.com/webhook_subscriptions) and create a new webhook  # Using Webhooks  Webhooks, also known as callbacks, are a way for ContentGroove to notify your application as soon as possible after an event has occurred in ContentGroove. For example after a media completes processing, ContentGroove can use a webhook to notify your application with information about the video: Suggested clips, transcription, and so on. You can use the information sent to update your system and/or use the webhook to trigger other business processes.  The webhook request is sent as an HTTP POST containing a payload of JSON-formatted data. For the details of the payload format see the \&quot;CALLBACKS\&quot; sections below.  When your application receives the webhook request, it must respond with a 200 HTTP status code (success). If a 200 HTTP status code is not returned, ContentGroove will assume that the webhook was not delivered and will retry a limited number of times, using an exponential backoff algorithm.  ContentGroove makes a best effort to attempt to send the webhook at least once. Applications receiving webhooks must tolerate the possibility of a single webhook payload being sent more than once (idempotent behavior). Applications receiving webhooks should tolerate the possibility that a webhook could not be delivered (for example your application was down when delivery was attempted).  # Getting Started with the Developer API  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Visit the [API Keys page](https://app.contentgroove.com/api_keys)   - Create a new API Key then copy and save the value.     &gt; ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️ - View all available endpoints, and try the API, on our [API Reference page](https://developers.contentgroove.com/api_reference)  # Using the Developer API  - Create a new media (video or audio) in ContentGroove   - If the video or audio is available from a URL, you can create a media by providing the &#x60;source_url&#x60; parameter. ContentGroove will fetch the video or audio from the URL if possible.   - Or, you can create a media from a video or audio file which you upload directly to ContentGroove (see File Uploading section below). - After the new media is created, at first it will be in a \&quot;processing\&quot; state.   Depending on the size and duration of the video or audio file, it will take some time for processing to complete.   - You can use ContentGroove Webhooks to be notified immediately when processing has completed. (Details coming soon.)   - You can also use the API to read the state of the media, to determine if the media has completed processing yet. - After the media has completed processing, you can access all of these details about the media:   - The media name and description   - The transcription of spoken words   - Topics and keywords which were discussed in the transcription   - Suggested video clips are automatically created - In addition to the automatically created video clips, you can create more video clips from the media  # Response Codes  The following is a comprehensive list of the status codes you may receive while using the ContentGroove API:  - 200 \&quot;Ok\&quot;   - The request was valid - 400 \&quot;Bad Request   - This is returned when there was a problem parsing the JSON body of your request if you supplied the &#39;Content-Type&#39;: &#39;application/json&#39; header, or if your request is missing the &#39;Content-Type&#39; header altogether - 401 \&quot;Unauthorized\&quot;   - This is returned when you are attempting to perform an action on a resource that you are not authorized to do - 402 \&quot;Payment Required\&quot;   - This is returned when you are attempting to perform an action that would push your account above a usage limit. You can view your usage at: https://app.contentgroove.com/quota_usage - 404 \&quot;Not Found\&quot;   - This is returned when the resource you are trying to view does not exist - 429 \&quot;Too Many Requests\&quot;   - This is returned when you have performed too many requests within a given period of time - 500 \&quot;Internal Server Error\&quot;   - This is returned when your request was valid but there was a problem on our end  # File Uploading  - Step 1: Make a GET request to the direct uploads URL endpoint (/api/v1/direct_uploads) to receive an upload URL to upload the file to and an upload id. - Step 2: Make a PUT request with the file as the body to the upload URL received in step 1. The response will have a 200 status with no body if the upload is successful.   &#x60;&#x60;&#x60;   curl -T /path/to/file upload_url   &#x60;&#x60;&#x60; - Step 3: After uploading the file to the upload URL, make a POST request to the create medias endpoint (/api/v1/medias), with the upload id and optionally a name and description for the new media.   &gt; At this time, file uploads are limited to 5gb per file.  # Allowed media types  Video:  - Supported: Most common video formats and codecs are supported. - Recommended: mp4  Audio:  - Supported: aac, mp3, flac, ogg, wav, and wma - Recommended: aac  # Authentication  You can use the API Key to authenticate your API requests using any of these methods. (Replace abc123 with your actual API Key.)  - Request header &#x60;Authorization: Bearer abc123&#x60; - Request header &#x60;X-API-KEY: abc123&#x60; - Query parameter &#x60;api_key&#x3D;abc123&#x60;   &gt; ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️  # Link to openapi.json spec  - https://api.contentgroove.com/api-docs/v1/openapi.json 
    """
)

