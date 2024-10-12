from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_eulas_request import AcceptEulasRequest
from openapi_server.models.accept_eulas_response import AcceptEulasResponse
from openapi_server.models.create_launch_profile_request import CreateLaunchProfileRequest
from openapi_server.models.create_launch_profile_response import CreateLaunchProfileResponse
from openapi_server.models.create_streaming_image_request import CreateStreamingImageRequest
from openapi_server.models.create_streaming_image_response import CreateStreamingImageResponse
from openapi_server.models.create_streaming_session_request import CreateStreamingSessionRequest
from openapi_server.models.create_streaming_session_response import CreateStreamingSessionResponse
from openapi_server.models.create_streaming_session_stream_request import CreateStreamingSessionStreamRequest
from openapi_server.models.create_streaming_session_stream_response import CreateStreamingSessionStreamResponse
from openapi_server.models.create_studio_component_request import CreateStudioComponentRequest
from openapi_server.models.create_studio_component_response import CreateStudioComponentResponse
from openapi_server.models.create_studio_request import CreateStudioRequest
from openapi_server.models.create_studio_response import CreateStudioResponse
from openapi_server.models.delete_launch_profile_response import DeleteLaunchProfileResponse
from openapi_server.models.delete_streaming_image_response import DeleteStreamingImageResponse
from openapi_server.models.delete_streaming_session_response import DeleteStreamingSessionResponse
from openapi_server.models.delete_studio_component_response import DeleteStudioComponentResponse
from openapi_server.models.delete_studio_response import DeleteStudioResponse
from openapi_server.models.get_eula_response import GetEulaResponse
from openapi_server.models.get_launch_profile_details_response import GetLaunchProfileDetailsResponse
from openapi_server.models.get_launch_profile_initialization_response import GetLaunchProfileInitializationResponse
from openapi_server.models.get_launch_profile_member_response import GetLaunchProfileMemberResponse
from openapi_server.models.get_launch_profile_response import GetLaunchProfileResponse
from openapi_server.models.get_streaming_image_response import GetStreamingImageResponse
from openapi_server.models.get_streaming_session_backup_response import GetStreamingSessionBackupResponse
from openapi_server.models.get_streaming_session_response import GetStreamingSessionResponse
from openapi_server.models.get_streaming_session_stream_response import GetStreamingSessionStreamResponse
from openapi_server.models.get_studio_component_response import GetStudioComponentResponse
from openapi_server.models.get_studio_member_response import GetStudioMemberResponse
from openapi_server.models.get_studio_response import GetStudioResponse
from openapi_server.models.launch_profile_state import LaunchProfileState
from openapi_server.models.list_eula_acceptances_response import ListEulaAcceptancesResponse
from openapi_server.models.list_eulas_response import ListEulasResponse
from openapi_server.models.list_launch_profile_members_response import ListLaunchProfileMembersResponse
from openapi_server.models.list_launch_profiles_response import ListLaunchProfilesResponse
from openapi_server.models.list_streaming_images_response import ListStreamingImagesResponse
from openapi_server.models.list_streaming_session_backups_response import ListStreamingSessionBackupsResponse
from openapi_server.models.list_streaming_sessions_response import ListStreamingSessionsResponse
from openapi_server.models.list_studio_components_response import ListStudioComponentsResponse
from openapi_server.models.list_studio_members_response import ListStudioMembersResponse
from openapi_server.models.list_studios_response import ListStudiosResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_launch_profile_members_request import PutLaunchProfileMembersRequest
from openapi_server.models.put_studio_members_request import PutStudioMembersRequest
from openapi_server.models.start_streaming_session_request import StartStreamingSessionRequest
from openapi_server.models.start_streaming_session_response import StartStreamingSessionResponse
from openapi_server.models.start_studio_sso_configuration_repair_response import StartStudioSSOConfigurationRepairResponse
from openapi_server.models.stop_streaming_session_request import StopStreamingSessionRequest
from openapi_server.models.stop_streaming_session_response import StopStreamingSessionResponse
from openapi_server.models.studio_component_state import StudioComponentState
from openapi_server.models.studio_component_type import StudioComponentType
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_launch_profile_member_request import UpdateLaunchProfileMemberRequest
from openapi_server.models.update_launch_profile_member_response import UpdateLaunchProfileMemberResponse
from openapi_server.models.update_launch_profile_request import UpdateLaunchProfileRequest
from openapi_server.models.update_launch_profile_response import UpdateLaunchProfileResponse
from openapi_server.models.update_streaming_image_request import UpdateStreamingImageRequest
from openapi_server.models.update_streaming_image_response import UpdateStreamingImageResponse
from openapi_server.models.update_studio_component_request import UpdateStudioComponentRequest
from openapi_server.models.update_studio_component_response import UpdateStudioComponentResponse
from openapi_server.models.update_studio_request import UpdateStudioRequest
from openapi_server.models.update_studio_response import UpdateStudioResponse
from openapi_server import util


async def accept_eulas(request: web.Request, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """accept_eulas

    Accept EULAs.

    :param studio_id: The studio ID.
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = AcceptEulasRequest.from_dict(body)
    return web.Response(status=200)


async def create_launch_profile(request: web.Request, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """create_launch_profile

    Create a launch profile.

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = CreateLaunchProfileRequest.from_dict(body)
    return web.Response(status=200)


async def create_streaming_image(request: web.Request, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """create_streaming_image

    Creates a streaming image resource in a studio.

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = CreateStreamingImageRequest.from_dict(body)
    return web.Response(status=200)


async def create_streaming_session(request: web.Request, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """create_streaming_session

    &lt;p&gt;Creates a streaming session in a studio.&lt;/p&gt; &lt;p&gt;After invoking this operation, you must poll GetStreamingSession until the streaming session is in the &lt;code&gt;READY&lt;/code&gt; state.&lt;/p&gt;

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = CreateStreamingSessionRequest.from_dict(body)
    return web.Response(status=200)


async def create_streaming_session_stream(request: web.Request, session_id, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """create_streaming_session_stream

    &lt;p&gt;Creates a streaming session stream for a streaming session.&lt;/p&gt; &lt;p&gt;After invoking this API, invoke GetStreamingSessionStream with the returned streamId to poll the resource until it is in the &lt;code&gt;READY&lt;/code&gt; state.&lt;/p&gt;

    :param session_id: The streaming session ID.
    :type session_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = CreateStreamingSessionStreamRequest.from_dict(body)
    return web.Response(status=200)


async def create_studio(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """create_studio

    &lt;p&gt;Create a new studio.&lt;/p&gt; &lt;p&gt;When creating a studio, two IAM roles must be provided: the admin role and the user role. These roles are assumed by your users when they log in to the Nimble Studio portal.&lt;/p&gt; &lt;p&gt;The user role must have the &lt;code&gt;AmazonNimbleStudio-StudioUser&lt;/code&gt; managed policy attached for the portal to function properly.&lt;/p&gt; &lt;p&gt;The admin role must have the &lt;code&gt;AmazonNimbleStudio-StudioAdmin&lt;/code&gt; managed policy attached for the portal to function properly.&lt;/p&gt; &lt;p&gt;You may optionally specify a KMS key in the &lt;code&gt;StudioEncryptionConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;In Nimble Studio, resource names, descriptions, initialization scripts, and other data you provide are always encrypted at rest using an KMS key. By default, this key is owned by Amazon Web Services and managed on your behalf. You may provide your own KMS key when calling &lt;code&gt;CreateStudio&lt;/code&gt; to encrypt this data using a key you own and manage.&lt;/p&gt; &lt;p&gt;When providing an KMS key during studio creation, Nimble Studio creates KMS grants in your account to provide your studio user and admin roles access to these KMS keys.&lt;/p&gt; &lt;p&gt;If you delete this grant, the studio will no longer be accessible to your portal users.&lt;/p&gt; &lt;p&gt;If you delete the studio KMS key, your studio will no longer be accessible.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = CreateStudioRequest.from_dict(body)
    return web.Response(status=200)


async def create_studio_component(request: web.Request, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """create_studio_component

    Creates a studio component resource.

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = CreateStudioComponentRequest.from_dict(body)
    return web.Response(status=200)


async def delete_launch_profile(request: web.Request, launch_profile_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """delete_launch_profile

    Permanently delete a launch profile.

    :param launch_profile_id: The ID of the launch profile used to control access from the streaming session.
    :type launch_profile_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    return web.Response(status=200)


async def delete_launch_profile_member(request: web.Request, launch_profile_id, principal_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """delete_launch_profile_member

    Delete a user from launch profile membership.

    :param launch_profile_id: The ID of the launch profile used to control access from the streaming session.
    :type launch_profile_id: str
    :param principal_id: The principal ID. This currently supports a IAM Identity Center UserId. 
    :type principal_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    return web.Response(status=200)


async def delete_streaming_image(request: web.Request, streaming_image_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """delete_streaming_image

    Delete streaming image.

    :param streaming_image_id: The streaming image ID.
    :type streaming_image_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    return web.Response(status=200)


async def delete_streaming_session(request: web.Request, session_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """delete_streaming_session

    &lt;p&gt;Deletes streaming session resource.&lt;/p&gt; &lt;p&gt;After invoking this operation, use GetStreamingSession to poll the resource until it transitions to a &lt;code&gt;DELETED&lt;/code&gt; state.&lt;/p&gt; &lt;p&gt;A streaming session will count against your streaming session quota until it is marked &lt;code&gt;DELETED&lt;/code&gt;.&lt;/p&gt;

    :param session_id: The streaming session ID.
    :type session_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    return web.Response(status=200)


async def delete_studio(request: web.Request, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """delete_studio

    Delete a studio resource.

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    return web.Response(status=200)


async def delete_studio_component(request: web.Request, studio_component_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """delete_studio_component

    Deletes a studio component resource.

    :param studio_component_id: The studio component ID.
    :type studio_component_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    return web.Response(status=200)


async def delete_studio_member(request: web.Request, principal_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """delete_studio_member

    Delete a user from studio membership.

    :param principal_id: The principal ID. This currently supports a IAM Identity Center UserId. 
    :type principal_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    return web.Response(status=200)


async def get_eula(request: web.Request, eula_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_eula

    Get EULA.

    :param eula_id: The EULA ID.
    :type eula_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_launch_profile(request: web.Request, launch_profile_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_launch_profile

    Get a launch profile.

    :param launch_profile_id: The ID of the launch profile used to control access from the streaming session.
    :type launch_profile_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_launch_profile_details(request: web.Request, launch_profile_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_launch_profile_details

    Launch profile details include the launch profile resource and summary information of resources that are used by, or available to, the launch profile. This includes the name and description of all studio components used by the launch profiles, and the name and description of streaming images that can be used with this launch profile.

    :param launch_profile_id: The ID of the launch profile used to control access from the streaming session.
    :type launch_profile_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_launch_profile_initialization(request: web.Request, launch_profile_id, launch_profile_protocol_versions, launch_purpose, platform, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_launch_profile_initialization

    Get a launch profile initialization.

    :param launch_profile_id: The ID of the launch profile used to control access from the streaming session.
    :type launch_profile_id: str
    :param launch_profile_protocol_versions: The launch profile protocol versions supported by the client.
    :type launch_profile_protocol_versions: List[str]
    :param launch_purpose: The launch purpose.
    :type launch_purpose: str
    :param platform: The platform where this Launch Profile will be used, either Windows or Linux.
    :type platform: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_launch_profile_member(request: web.Request, launch_profile_id, principal_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_launch_profile_member

    Get a user persona in launch profile membership.

    :param launch_profile_id: The ID of the launch profile used to control access from the streaming session.
    :type launch_profile_id: str
    :param principal_id: The principal ID. This currently supports a IAM Identity Center UserId. 
    :type principal_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_streaming_image(request: web.Request, streaming_image_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_streaming_image

    Get streaming image.

    :param streaming_image_id: The streaming image ID.
    :type streaming_image_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_streaming_session(request: web.Request, session_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_streaming_session

    &lt;p&gt;Gets StreamingSession resource.&lt;/p&gt; &lt;p&gt;Invoke this operation to poll for a streaming session state while creating or deleting a session.&lt;/p&gt;

    :param session_id: The streaming session ID.
    :type session_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_streaming_session_backup(request: web.Request, backup_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_streaming_session_backup

    &lt;p&gt;Gets &lt;code&gt;StreamingSessionBackup&lt;/code&gt; resource.&lt;/p&gt; &lt;p&gt;Invoke this operation to poll for a streaming session backup while stopping a streaming session.&lt;/p&gt;

    :param backup_id: The ID of the backup.
    :type backup_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_streaming_session_stream(request: web.Request, session_id, stream_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_streaming_session_stream

    &lt;p&gt;Gets a StreamingSessionStream for a streaming session.&lt;/p&gt; &lt;p&gt;Invoke this operation to poll the resource after invoking &lt;code&gt;CreateStreamingSessionStream&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;After the &lt;code&gt;StreamingSessionStream&lt;/code&gt; changes to the &lt;code&gt;READY&lt;/code&gt; state, the url property will contain a stream to be used with the DCV streaming client.&lt;/p&gt;

    :param session_id: The streaming session ID.
    :type session_id: str
    :param stream_id: The streaming session stream ID.
    :type stream_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_studio(request: web.Request, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_studio

    Get a studio resource.

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_studio_component(request: web.Request, studio_component_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_studio_component

    Gets a studio component resource.

    :param studio_component_id: The studio component ID.
    :type studio_component_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_studio_member(request: web.Request, principal_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_studio_member

    Get a user&#39;s membership in a studio.

    :param principal_id: The principal ID. This currently supports a IAM Identity Center UserId. 
    :type principal_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_eula_acceptances(request: web.Request, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, eula_ids=None, next_token=None) -> web.Response:
    """list_eula_acceptances

    List EULA acceptances.

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param eula_ids: The list of EULA IDs that have been previously accepted.
    :type eula_ids: List[str]
    :param next_token: The token for the next set of results, or null if there are no more results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_eulas(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, eula_ids=None, next_token=None) -> web.Response:
    """list_eulas

    List EULAs.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param eula_ids: The list of EULA IDs that should be returned
    :type eula_ids: List[str]
    :param next_token: The token for the next set of results, or null if there are no more results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_launch_profile_members(request: web.Request, launch_profile_id, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_launch_profile_members

    Get all users in a given launch profile membership.

    :param launch_profile_id: The ID of the launch profile used to control access from the streaming session.
    :type launch_profile_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The max number of results to return in the response.
    :type max_results: int
    :param next_token: The token for the next set of results, or null if there are no more results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_launch_profiles(request: web.Request, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, principal_id=None, states=None) -> web.Response:
    """list_launch_profiles

    List all the launch profiles a studio.

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The max number of results to return in the response.
    :type max_results: int
    :param next_token: The token for the next set of results, or null if there are no more results.
    :type next_token: str
    :param principal_id: The principal ID. This currently supports a IAM Identity Center UserId. 
    :type principal_id: str
    :param states: Filter this request to launch profiles in any of the given states.
    :type states: list | bytes

    """
    states = [LaunchProfileState.from_dict(d) for d in states]
    return web.Response(status=200)


async def list_streaming_images(request: web.Request, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, owner=None) -> web.Response:
    """list_streaming_images

    &lt;p&gt;List the streaming image resources available to this studio.&lt;/p&gt; &lt;p&gt;This list will contain both images provided by Amazon Web Services, as well as streaming images that you have created in your studio.&lt;/p&gt;

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results, or null if there are no more results.
    :type next_token: str
    :param owner: Filter this request to streaming images with the given owner
    :type owner: str

    """
    return web.Response(status=200)


async def list_streaming_session_backups(request: web.Request, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, owned_by=None) -> web.Response:
    """list_streaming_session_backups

    Lists the backups of a streaming session in a studio.

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results, or null if there are no more results.
    :type next_token: str
    :param owned_by: The user ID of the user that owns the streaming session.
    :type owned_by: str

    """
    return web.Response(status=200)


async def list_streaming_sessions(request: web.Request, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, created_by=None, next_token=None, owned_by=None, session_ids=None) -> web.Response:
    """list_streaming_sessions

    Lists the streaming sessions in a studio.

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param created_by: Filters the request to streaming sessions created by the given user.
    :type created_by: str
    :param next_token: The token for the next set of results, or null if there are no more results.
    :type next_token: str
    :param owned_by: Filters the request to streaming session owned by the given user
    :type owned_by: str
    :param session_ids: Filters the request to only the provided session IDs.
    :type session_ids: str

    """
    return web.Response(status=200)


async def list_studio_components(request: web.Request, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, states=None, types=None) -> web.Response:
    """list_studio_components

    Lists the &lt;code&gt;StudioComponents&lt;/code&gt; in a studio.

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The max number of results to return in the response.
    :type max_results: int
    :param next_token: The token for the next set of results, or null if there are no more results.
    :type next_token: str
    :param states: Filters the request to studio components that are in one of the given states. 
    :type states: list | bytes
    :param types: Filters the request to studio components that are of one of the given types.
    :type types: list | bytes

    """
    states = [StudioComponentState.from_dict(d) for d in states]
    types = [StudioComponentType.from_dict(d) for d in types]
    return web.Response(status=200)


async def list_studio_members(request: web.Request, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_studio_members

    &lt;p&gt;Get all users in a given studio membership.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ListStudioMembers&lt;/code&gt; only returns admin members.&lt;/p&gt; &lt;/note&gt;

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The max number of results to return in the response.
    :type max_results: int
    :param next_token: The token for the next set of results, or null if there are no more results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_studios(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_studios

    List studios in your Amazon Web Services accounts in the requested Amazon Web Services Region.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results, or null if there are no more results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Gets the tags for a resource, given its Amazon Resource Names (ARN).&lt;/p&gt; &lt;p&gt;This operation supports ARNs for all resource types in Nimble Studio that support tags, including studio, studio component, launch profile, streaming image, and streaming session. All resources that can be tagged will contain an ARN property, so you do not have to create this ARN yourself.&lt;/p&gt;

    :param resource_arn: The Amazon Resource Name (ARN) of the resource for which you want to list tags.
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def put_launch_profile_members(request: web.Request, launch_profile_id, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """put_launch_profile_members

    Add/update users with given persona to launch profile membership.

    :param launch_profile_id: The ID of the launch profile used to control access from the streaming session.
    :type launch_profile_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = PutLaunchProfileMembersRequest.from_dict(body)
    return web.Response(status=200)


async def put_studio_members(request: web.Request, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """put_studio_members

    Add/update users with given persona to studio membership.

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = PutStudioMembersRequest.from_dict(body)
    return web.Response(status=200)


async def start_streaming_session(request: web.Request, session_id, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """start_streaming_session

    Transitions sessions from the &lt;code&gt;STOPPED&lt;/code&gt; state into the &lt;code&gt;READY&lt;/code&gt; state. The &lt;code&gt;START_IN_PROGRESS&lt;/code&gt; state is the intermediate state between the &lt;code&gt;STOPPED&lt;/code&gt; and &lt;code&gt;READY&lt;/code&gt; states.

    :param session_id: The streaming session ID for the &lt;code&gt;StartStreamingSessionRequest&lt;/code&gt;.
    :type session_id: str
    :param studio_id: The studio ID for the StartStreamingSessionRequest.
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = StartStreamingSessionRequest.from_dict(body)
    return web.Response(status=200)


async def start_studio_sso_configuration_repair(request: web.Request, studio_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """start_studio_sso_configuration_repair

    &lt;p&gt;Repairs the IAM Identity Center configuration for a given studio.&lt;/p&gt; &lt;p&gt;If the studio has a valid IAM Identity Center configuration currently associated with it, this operation will fail with a validation error.&lt;/p&gt; &lt;p&gt;If the studio does not have a valid IAM Identity Center configuration currently associated with it, then a new IAM Identity Center application is created for the studio and the studio is changed to the &lt;code&gt;READY&lt;/code&gt; state.&lt;/p&gt; &lt;p&gt;After the IAM Identity Center application is repaired, you must use the Amazon Nimble Studio console to add administrators and users to your studio.&lt;/p&gt;

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    return web.Response(status=200)


async def stop_streaming_session(request: web.Request, session_id, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """stop_streaming_session

    Transitions sessions from the &lt;code&gt;READY&lt;/code&gt; state into the &lt;code&gt;STOPPED&lt;/code&gt; state. The &lt;code&gt;STOP_IN_PROGRESS&lt;/code&gt; state is the intermediate state between the &lt;code&gt;READY&lt;/code&gt; and &lt;code&gt;STOPPED&lt;/code&gt; states.

    :param session_id: The streaming session ID for the &lt;code&gt;StopStreamingSessionRequest&lt;/code&gt;.
    :type session_id: str
    :param studio_id: The studioId for the StopStreamingSessionRequest.
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = StopStreamingSessionRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Creates tags for a resource, given its ARN.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource you want to add tags to. 
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Deletes the tags for a resource.

    :param resource_arn: Identifies the Amazon Resource Name(ARN) key from which you are removing tags. 
    :type resource_arn: str
    :param tag_keys: One or more tag keys. Specify only the tag keys, not the tag values.
    :type tag_keys: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def update_launch_profile(request: web.Request, launch_profile_id, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """update_launch_profile

    Update a launch profile.

    :param launch_profile_id: The ID of the launch profile used to control access from the streaming session.
    :type launch_profile_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = UpdateLaunchProfileRequest.from_dict(body)
    return web.Response(status=200)


async def update_launch_profile_member(request: web.Request, launch_profile_id, principal_id, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """update_launch_profile_member

    Update a user persona in launch profile membership.

    :param launch_profile_id: The ID of the launch profile used to control access from the streaming session.
    :type launch_profile_id: str
    :param principal_id: The principal ID. This currently supports a IAM Identity Center UserId. 
    :type principal_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = UpdateLaunchProfileMemberRequest.from_dict(body)
    return web.Response(status=200)


async def update_streaming_image(request: web.Request, streaming_image_id, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """update_streaming_image

    Update streaming image.

    :param streaming_image_id: The streaming image ID.
    :type streaming_image_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = UpdateStreamingImageRequest.from_dict(body)
    return web.Response(status=200)


async def update_studio(request: web.Request, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """update_studio

    &lt;p&gt;Update a Studio resource.&lt;/p&gt; &lt;p&gt;Currently, this operation only supports updating the displayName of your studio.&lt;/p&gt;

    :param studio_id: The studio ID. 
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = UpdateStudioRequest.from_dict(body)
    return web.Response(status=200)


async def update_studio_component(request: web.Request, studio_component_id, studio_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_token=None) -> web.Response:
    """update_studio_component

    Updates a studio component resource.

    :param studio_component_id: The studio component ID.
    :type studio_component_id: str
    :param studio_id: The studio ID. 
    :type studio_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_token: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
    :type x_amz_client_token: str

    """
    body = UpdateStudioComponentRequest.from_dict(body)
    return web.Response(status=200)
