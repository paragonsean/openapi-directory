from typing import List, Dict
from aiohttp import web

from openapi_server.models.video_v1_recording_settings import VideoV1RecordingSettings
from openapi_server import util


async def create_recording_settings(request: web.Request, friendly_name, aws_credentials_sid=None, aws_s3_url=None, aws_storage_enabled=None, encryption_enabled=None, encryption_key_sid=None) -> web.Response:
    """create_recording_settings

    

    :param friendly_name: A descriptive string that you create to describe the resource and be shown to users in the console
    :type friendly_name: str
    :param aws_credentials_sid: The SID of the stored Credential resource.
    :type aws_credentials_sid: str
    :param aws_s3_url: The URL of the AWS S3 bucket where the recordings should be stored. We only support DNS-compliant URLs like &#x60;https://documentation-example-twilio-bucket/recordings&#x60;, where &#x60;recordings&#x60; is the path in which you want the recordings to be stored. This URL accepts only URI-valid characters, as described in the [RFC 3986](https://tools.ietf.org/html/rfc3986#section-2).
    :type aws_s3_url: str
    :param aws_storage_enabled: Whether all recordings should be written to the &#x60;aws_s3_url&#x60;. When &#x60;false&#x60;, all recordings are stored in our cloud.
    :type aws_storage_enabled: bool
    :param encryption_enabled: Whether all recordings should be stored in an encrypted form. The default is &#x60;false&#x60;.
    :type encryption_enabled: bool
    :param encryption_key_sid: The SID of the Public Key resource to use for encryption.
    :type encryption_key_sid: str

    """
    return web.Response(status=200)


async def fetch_recording_settings(request: web.Request, ) -> web.Response:
    """fetch_recording_settings

    


    """
    return web.Response(status=200)
