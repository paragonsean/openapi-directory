# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_accept_eulas(client):
    """Test case for accept_eulas

    
    """
    body = {"eulaIds":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2020-08-01/studios/{studio_id}/eula-acceptances'.format(studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_launch_profile(client):
    """Test case for create_launch_profile

    
    """
    body = {"ec2SubnetIds":"","studioComponentIds":"","launchProfileProtocolVersions":"","name":"","description":"","streamConfiguration":{"automaticTerminationMode":"","volumeConfiguration":{"size":"","iops":"","throughput":""},"clipboardMode":"","ec2InstanceTypes":"","sessionStorage":{"mode":"","root":{"linux":"","windows":""}},"streamingImageIds":"","maxSessionLengthInMinutes":"","sessionBackup":{"mode":"","maxBackupsToRetain":""},"maxStoppedSessionLengthInMinutes":"","sessionPersistenceMode":""},"tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2020-08-01/studios/{studio_id}/launch-profiles'.format(studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_streaming_image(client):
    """Test case for create_streaming_image

    
    """
    body = {"name":"","description":"","ec2ImageId":"","tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2020-08-01/studios/{studio_id}/streaming-images'.format(studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_streaming_session(client):
    """Test case for create_streaming_session

    
    """
    body = {"streamingImageId":"","ec2InstanceType":"","launchProfileId":"","ownedBy":"","tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2020-08-01/studios/{studio_id}/streaming-sessions'.format(studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_streaming_session_stream(client):
    """Test case for create_streaming_session_stream

    
    """
    body = {"expirationInSeconds":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2020-08-01/studios/{studio_id}/streaming-sessions/{session_id}/streams'.format(session_id='session_id_example', studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_studio(client):
    """Test case for create_studio

    
    """
    body = {"studioEncryptionConfiguration":{"keyArn":"","keyType":""},"displayName":"","studioName":"","adminRoleArn":"","tags":"","userRoleArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2020-08-01/studios',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_studio_component(client):
    """Test case for create_studio_component

    
    """
    body = {"initializationScripts":"","scriptParameters":"","runtimeRoleArn":"","configuration":{"licenseServiceConfiguration":{"endpoint":""},"activeDirectoryConfiguration":{"computerAttributes":"","directoryId":"","organizationalUnitDistinguishedName":""},"computeFarmConfiguration":{"activeDirectoryUser":"","endpoint":""},"sharedFileSystemConfiguration":{"windowsMountDrive":"","endpoint":"","fileSystemId":"","linuxMountPoint":"","shareName":""}},"subtype":"","name":"","description":"","ec2SecurityGroupIds":"","secureInitializationRoleArn":"","type":"","tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2020-08-01/studios/{studio_id}/studio-components'.format(studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_launch_profile(client):
    """Test case for delete_launch_profile

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2020-08-01/studios/{studio_id}/launch-profiles/{launch_profile_id}'.format(launch_profile_id='launch_profile_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_launch_profile_member(client):
    """Test case for delete_launch_profile_member

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2020-08-01/studios/{studio_id}/launch-profiles/{launch_profile_id}/membership/{principal_id}'.format(launch_profile_id='launch_profile_id_example', principal_id='principal_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_streaming_image(client):
    """Test case for delete_streaming_image

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2020-08-01/studios/{studio_id}/streaming-images/{streaming_image_id}'.format(streaming_image_id='streaming_image_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_streaming_session(client):
    """Test case for delete_streaming_session

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2020-08-01/studios/{studio_id}/streaming-sessions/{session_id}'.format(session_id='session_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_studio(client):
    """Test case for delete_studio

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2020-08-01/studios/{studio_id}'.format(studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_studio_component(client):
    """Test case for delete_studio_component

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2020-08-01/studios/{studio_id}/studio-components/{studio_component_id}'.format(studio_component_id='studio_component_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_studio_member(client):
    """Test case for delete_studio_member

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2020-08-01/studios/{studio_id}/membership/{principal_id}'.format(principal_id='principal_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_eula(client):
    """Test case for get_eula

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/eulas/{eula_id}'.format(eula_id='eula_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_launch_profile(client):
    """Test case for get_launch_profile

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/launch-profiles/{launch_profile_id}'.format(launch_profile_id='launch_profile_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_launch_profile_details(client):
    """Test case for get_launch_profile_details

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/launch-profiles/{launch_profile_id}/details'.format(launch_profile_id='launch_profile_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_launch_profile_initialization(client):
    """Test case for get_launch_profile_initialization

    
    """
    params = [('launchProfileProtocolVersions', ['launch_profile_protocol_versions_example']),
                    ('launchPurpose', 'launch_purpose_example'),
                    ('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/launch-profiles/{launch_profile_id}/init#launchProfileProtocolVersions&launchPurpose&platform'.format(launch_profile_id='launch_profile_id_example', studio_id='studio_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_launch_profile_member(client):
    """Test case for get_launch_profile_member

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/launch-profiles/{launch_profile_id}/membership/{principal_id}'.format(launch_profile_id='launch_profile_id_example', principal_id='principal_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_streaming_image(client):
    """Test case for get_streaming_image

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/streaming-images/{streaming_image_id}'.format(streaming_image_id='streaming_image_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_streaming_session(client):
    """Test case for get_streaming_session

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/streaming-sessions/{session_id}'.format(session_id='session_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_streaming_session_backup(client):
    """Test case for get_streaming_session_backup

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/streaming-session-backups/{backup_id}'.format(backup_id='backup_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_streaming_session_stream(client):
    """Test case for get_streaming_session_stream

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/streaming-sessions/{session_id}/streams/{stream_id}'.format(session_id='session_id_example', stream_id='stream_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_studio(client):
    """Test case for get_studio

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}'.format(studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_studio_component(client):
    """Test case for get_studio_component

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/studio-components/{studio_component_id}'.format(studio_component_id='studio_component_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_studio_member(client):
    """Test case for get_studio_member

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/membership/{principal_id}'.format(principal_id='principal_id_example', studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_eula_acceptances(client):
    """Test case for list_eula_acceptances

    
    """
    params = [('eulaIds', ['eula_ids_example']),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/eula-acceptances'.format(studio_id='studio_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_eulas(client):
    """Test case for list_eulas

    
    """
    params = [('eulaIds', ['eula_ids_example']),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/eulas',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_launch_profile_members(client):
    """Test case for list_launch_profile_members

    
    """
    params = [('maxResults', 56),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/launch-profiles/{launch_profile_id}/membership'.format(launch_profile_id='launch_profile_id_example', studio_id='studio_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_launch_profiles(client):
    """Test case for list_launch_profiles

    
    """
    params = [('maxResults', 56),
                    ('nextToken', 'next_token_example'),
                    ('principalId', 'principal_id_example'),
                    ('states', [openapi_server.LaunchProfileState()])]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/launch-profiles'.format(studio_id='studio_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_streaming_images(client):
    """Test case for list_streaming_images

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('owner', 'owner_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/streaming-images'.format(studio_id='studio_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_streaming_session_backups(client):
    """Test case for list_streaming_session_backups

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('ownedBy', 'owned_by_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/streaming-session-backups'.format(studio_id='studio_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_streaming_sessions(client):
    """Test case for list_streaming_sessions

    
    """
    params = [('createdBy', 'created_by_example'),
                    ('nextToken', 'next_token_example'),
                    ('ownedBy', 'owned_by_example'),
                    ('sessionIds', 'session_ids_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/streaming-sessions'.format(studio_id='studio_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_studio_components(client):
    """Test case for list_studio_components

    
    """
    params = [('maxResults', 56),
                    ('nextToken', 'next_token_example'),
                    ('states', [openapi_server.StudioComponentState()]),
                    ('types', [openapi_server.StudioComponentType()])]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/studio-components'.format(studio_id='studio_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_studio_members(client):
    """Test case for list_studio_members

    
    """
    params = [('maxResults', 56),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios/{studio_id}/membership'.format(studio_id='studio_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_studios(client):
    """Test case for list_studios

    
    """
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/studios',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2020-08-01/tags/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_launch_profile_members(client):
    """Test case for put_launch_profile_members

    
    """
    body = {"members":"","identityStoreId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2020-08-01/studios/{studio_id}/launch-profiles/{launch_profile_id}/membership'.format(launch_profile_id='launch_profile_id_example', studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_studio_members(client):
    """Test case for put_studio_members

    
    """
    body = {"members":"","identityStoreId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2020-08-01/studios/{studio_id}/membership'.format(studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_streaming_session(client):
    """Test case for start_streaming_session

    
    """
    body = {"backupId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2020-08-01/studios/{studio_id}/streaming-sessions/{session_id}/start'.format(session_id='session_id_example', studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_studio_sso_configuration_repair(client):
    """Test case for start_studio_sso_configuration_repair

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/2020-08-01/studios/{studio_id}/sso-configuration'.format(studio_id='studio_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_streaming_session(client):
    """Test case for stop_streaming_session

    
    """
    body = {"volumeRetentionMode":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2020-08-01/studios/{studio_id}/streaming-sessions/{session_id}/stop'.format(session_id='session_id_example', studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_resource(client):
    """Test case for tag_resource

    
    """
    body = {"tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2020-08-01/tags/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_resource(client):
    """Test case for untag_resource

    
    """
    params = [('tagKeys', ['tag_keys_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2020-08-01/tags/{resource_arntag_key}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_launch_profile(client):
    """Test case for update_launch_profile

    
    """
    body = {"studioComponentIds":"","launchProfileProtocolVersions":"","name":"","description":"","streamConfiguration":{"automaticTerminationMode":"","volumeConfiguration":{"size":"","iops":"","throughput":""},"clipboardMode":"","ec2InstanceTypes":"","sessionStorage":{"mode":"","root":{"linux":"","windows":""}},"streamingImageIds":"","maxSessionLengthInMinutes":"","sessionBackup":{"mode":"","maxBackupsToRetain":""},"maxStoppedSessionLengthInMinutes":"","sessionPersistenceMode":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/2020-08-01/studios/{studio_id}/launch-profiles/{launch_profile_id}'.format(launch_profile_id='launch_profile_id_example', studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_launch_profile_member(client):
    """Test case for update_launch_profile_member

    
    """
    body = {"persona":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/2020-08-01/studios/{studio_id}/launch-profiles/{launch_profile_id}/membership/{principal_id}'.format(launch_profile_id='launch_profile_id_example', principal_id='principal_id_example', studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_streaming_image(client):
    """Test case for update_streaming_image

    
    """
    body = {"name":"","description":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/2020-08-01/studios/{studio_id}/streaming-images/{streaming_image_id}'.format(streaming_image_id='streaming_image_id_example', studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_studio(client):
    """Test case for update_studio

    
    """
    body = {"displayName":"","adminRoleArn":"","userRoleArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/2020-08-01/studios/{studio_id}'.format(studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_studio_component(client):
    """Test case for update_studio_component

    
    """
    body = {"initializationScripts":"","scriptParameters":"","runtimeRoleArn":"","configuration":{"licenseServiceConfiguration":{"endpoint":""},"activeDirectoryConfiguration":{"computerAttributes":"","directoryId":"","organizationalUnitDistinguishedName":""},"computeFarmConfiguration":{"activeDirectoryUser":"","endpoint":""},"sharedFileSystemConfiguration":{"windowsMountDrive":"","endpoint":"","fileSystemId":"","linuxMountPoint":"","shareName":""}},"subtype":"","name":"","description":"","ec2SecurityGroupIds":"","secureInitializationRoleArn":"","type":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_client_token': 'x_amz_client_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/2020-08-01/studios/{studio_id}/studio-components/{studio_component_id}'.format(studio_component_id='studio_component_id_example', studio_id='studio_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

