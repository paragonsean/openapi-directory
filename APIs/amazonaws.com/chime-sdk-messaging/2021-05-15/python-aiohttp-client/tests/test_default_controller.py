# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.associate_channel_flow_request import AssociateChannelFlowRequest
from openapi_server.models.batch_create_channel_membership_request import BatchCreateChannelMembershipRequest
from openapi_server.models.batch_create_channel_membership_response import BatchCreateChannelMembershipResponse
from openapi_server.models.channel_flow_callback_request import ChannelFlowCallbackRequest
from openapi_server.models.channel_flow_callback_response import ChannelFlowCallbackResponse
from openapi_server.models.create_channel_ban_request import CreateChannelBanRequest
from openapi_server.models.create_channel_ban_response import CreateChannelBanResponse
from openapi_server.models.create_channel_flow_request import CreateChannelFlowRequest
from openapi_server.models.create_channel_flow_response import CreateChannelFlowResponse
from openapi_server.models.create_channel_membership_request import CreateChannelMembershipRequest
from openapi_server.models.create_channel_membership_response import CreateChannelMembershipResponse
from openapi_server.models.create_channel_moderator_request import CreateChannelModeratorRequest
from openapi_server.models.create_channel_moderator_response import CreateChannelModeratorResponse
from openapi_server.models.create_channel_request import CreateChannelRequest
from openapi_server.models.create_channel_response import CreateChannelResponse
from openapi_server.models.describe_channel_ban_response import DescribeChannelBanResponse
from openapi_server.models.describe_channel_flow_response import DescribeChannelFlowResponse
from openapi_server.models.describe_channel_membership_for_app_instance_user_response import DescribeChannelMembershipForAppInstanceUserResponse
from openapi_server.models.describe_channel_membership_response import DescribeChannelMembershipResponse
from openapi_server.models.describe_channel_moderated_by_app_instance_user_response import DescribeChannelModeratedByAppInstanceUserResponse
from openapi_server.models.describe_channel_moderator_response import DescribeChannelModeratorResponse
from openapi_server.models.describe_channel_response import DescribeChannelResponse
from openapi_server.models.get_channel_membership_preferences_response import GetChannelMembershipPreferencesResponse
from openapi_server.models.get_channel_message_response import GetChannelMessageResponse
from openapi_server.models.get_channel_message_status_response import GetChannelMessageStatusResponse
from openapi_server.models.get_messaging_session_endpoint_response import GetMessagingSessionEndpointResponse
from openapi_server.models.get_messaging_streaming_configurations_response import GetMessagingStreamingConfigurationsResponse
from openapi_server.models.list_channel_bans_response import ListChannelBansResponse
from openapi_server.models.list_channel_flows_response import ListChannelFlowsResponse
from openapi_server.models.list_channel_memberships_for_app_instance_user_response import ListChannelMembershipsForAppInstanceUserResponse
from openapi_server.models.list_channel_memberships_response import ListChannelMembershipsResponse
from openapi_server.models.list_channel_messages_response import ListChannelMessagesResponse
from openapi_server.models.list_channel_moderators_response import ListChannelModeratorsResponse
from openapi_server.models.list_channels_associated_with_channel_flow_response import ListChannelsAssociatedWithChannelFlowResponse
from openapi_server.models.list_channels_moderated_by_app_instance_user_response import ListChannelsModeratedByAppInstanceUserResponse
from openapi_server.models.list_channels_response import ListChannelsResponse
from openapi_server.models.list_sub_channels_response import ListSubChannelsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_channel_expiration_settings_request import PutChannelExpirationSettingsRequest
from openapi_server.models.put_channel_expiration_settings_response import PutChannelExpirationSettingsResponse
from openapi_server.models.put_channel_membership_preferences_request import PutChannelMembershipPreferencesRequest
from openapi_server.models.put_channel_membership_preferences_response import PutChannelMembershipPreferencesResponse
from openapi_server.models.put_messaging_streaming_configurations_request import PutMessagingStreamingConfigurationsRequest
from openapi_server.models.put_messaging_streaming_configurations_response import PutMessagingStreamingConfigurationsResponse
from openapi_server.models.redact_channel_message_request import RedactChannelMessageRequest
from openapi_server.models.redact_channel_message_response import RedactChannelMessageResponse
from openapi_server.models.search_channels_request import SearchChannelsRequest
from openapi_server.models.search_channels_response import SearchChannelsResponse
from openapi_server.models.send_channel_message_request import SendChannelMessageRequest
from openapi_server.models.send_channel_message_response import SendChannelMessageResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_channel_flow_request import UpdateChannelFlowRequest
from openapi_server.models.update_channel_flow_response import UpdateChannelFlowResponse
from openapi_server.models.update_channel_message_request import UpdateChannelMessageRequest
from openapi_server.models.update_channel_message_response import UpdateChannelMessageResponse
from openapi_server.models.update_channel_read_marker_response import UpdateChannelReadMarkerResponse
from openapi_server.models.update_channel_request import UpdateChannelRequest
from openapi_server.models.update_channel_response import UpdateChannelResponse


pytestmark = pytest.mark.asyncio

async def test_associate_channel_flow(client):
    """Test case for associate_channel_flow

    
    """
    body = {"ChannelFlowArn":""}
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_arn}/channel-flow#x-amz-chime-bearer'.format(channel_arn='channel_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_create_channel_membership(client):
    """Test case for batch_create_channel_membership

    
    """
    body = {"SubChannelId":"","Type":"","MemberArns":""}
    params = [('operation', 'operation_example')]
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{channel_arn}/memberships#operation=batch-create&x-amz-chime-bearer'.format(channel_arn='channel_arn_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_channel_flow_callback(client):
    """Test case for channel_flow_callback

    
    """
    body = {"CallbackId":"","DeleteResource":"","ChannelMessage":{"SubChannelId":"","MessageAttributes":"","ContentType":"","Content":"","Metadata":"","PushNotification":{"Type":"","Title":"","Body":""},"MessageId":""}}
    params = [('operation', 'operation_example')]
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
        path='/channels/{channel_arnoperationchannel_flow_callbac}'.format(channel_arn='channel_arn_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_channel(client):
    """Test case for create_channel

    
    """
    body = {"Privacy":"","ClientRequestToken":"","ElasticChannelConfiguration":{"MinimumMembershipPercentage":"","MaximumSubChannels":"","TargetMembershipsPerSubChannel":""},"ModeratorArns":"","ExpirationSettings":{"ExpirationCriterion":"","ExpirationDays":""},"Mode":"","Metadata":"","MemberArns":"","ChannelId":"","AppInstanceArn":"","Tags":"","Name":""}
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels#x-amz-chime-bearer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_channel_ban(client):
    """Test case for create_channel_ban

    
    """
    body = {"MemberArn":""}
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{channel_arn}/bans#x-amz-chime-bearer'.format(channel_arn='channel_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_channel_flow(client):
    """Test case for create_channel_flow

    
    """
    body = {"ClientRequestToken":"","AppInstanceArn":"","Processors":"","Tags":"","Name":""}
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
        path='/channel-flows',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_channel_membership(client):
    """Test case for create_channel_membership

    
    """
    body = {"SubChannelId":"","MemberArn":"","Type":""}
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{channel_arn}/memberships#x-amz-chime-bearer'.format(channel_arn='channel_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_channel_moderator(client):
    """Test case for create_channel_moderator

    
    """
    body = {"ChannelModeratorArn":""}
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{channel_arn}/moderators#x-amz-chime-bearer'.format(channel_arn='channel_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel(client):
    """Test case for delete_channel

    
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_arnx_amz_chime_beare}'.format(channel_arn='channel_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel_ban(client):
    """Test case for delete_channel_ban

    
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_arn}/bans/{member_arnx_amz_chime_beare}'.format(channel_arn='channel_arn_example', member_arn='member_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel_flow(client):
    """Test case for delete_channel_flow

    
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
        method='DELETE',
        path='/channel-flows/{channel_flow_arn}'.format(channel_flow_arn='channel_flow_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel_membership(client):
    """Test case for delete_channel_membership

    
    """
    params = [('sub-channel-id', 'sub_channel_id_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_arn}/memberships/{member_arnx_amz_chime_beare}'.format(channel_arn='channel_arn_example', member_arn='member_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel_message(client):
    """Test case for delete_channel_message

    
    """
    params = [('sub-channel-id', 'sub_channel_id_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_arn}/messages/{message_idx_amz_chime_beare}'.format(channel_arn='channel_arn_example', message_id='message_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel_moderator(client):
    """Test case for delete_channel_moderator

    
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_arn}/moderators/{channel_moderator_arnx_amz_chime_beare}'.format(channel_arn='channel_arn_example', channel_moderator_arn='channel_moderator_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_messaging_streaming_configurations(client):
    """Test case for delete_messaging_streaming_configurations

    
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
        method='DELETE',
        path='/app-instances/{app_instance_arn}/streaming-configurations'.format(app_instance_arn='app_instance_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_channel(client):
    """Test case for describe_channel

    
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_arnx_amz_chime_beare}'.format(channel_arn='channel_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_channel_ban(client):
    """Test case for describe_channel_ban

    
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_arn}/bans/{member_arnx_amz_chime_beare}'.format(channel_arn='channel_arn_example', member_arn='member_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_channel_flow(client):
    """Test case for describe_channel_flow

    
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
        path='/channel-flows/{channel_flow_arn}'.format(channel_flow_arn='channel_flow_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_channel_membership(client):
    """Test case for describe_channel_membership

    
    """
    params = [('sub-channel-id', 'sub_channel_id_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_arn}/memberships/{member_arnx_amz_chime_beare}'.format(channel_arn='channel_arn_example', member_arn='member_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_channel_membership_for_app_instance_user(client):
    """Test case for describe_channel_membership_for_app_instance_user

    
    """
    params = [('app-instance-user-arn', 'app_instance_user_arn_example'),
                    ('scope', 'scope_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_arnscopeapp_instance_user_membershipapp_instance_user_arnx_amz_chime_beare}'.format(channel_arn='channel_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_channel_moderated_by_app_instance_user(client):
    """Test case for describe_channel_moderated_by_app_instance_user

    
    """
    params = [('app-instance-user-arn', 'app_instance_user_arn_example'),
                    ('scope', 'scope_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_arnscopeapp_instance_user_moderated_channelapp_instance_user_arnx_amz_chime_beare}'.format(channel_arn='channel_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_channel_moderator(client):
    """Test case for describe_channel_moderator

    
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_arn}/moderators/{channel_moderator_arnx_amz_chime_beare}'.format(channel_arn='channel_arn_example', channel_moderator_arn='channel_moderator_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disassociate_channel_flow(client):
    """Test case for disassociate_channel_flow

    
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_arn}/channel-flow/{channel_flow_arnx_amz_chime_beare}'.format(channel_arn='channel_arn_example', channel_flow_arn='channel_flow_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_membership_preferences(client):
    """Test case for get_channel_membership_preferences

    
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_arn}/memberships/{member_arn}/preferences#x-amz-chime-bearer'.format(channel_arn='channel_arn_example', member_arn='member_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_message(client):
    """Test case for get_channel_message

    
    """
    params = [('sub-channel-id', 'sub_channel_id_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_arn}/messages/{message_idx_amz_chime_beare}'.format(channel_arn='channel_arn_example', message_id='message_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_message_status(client):
    """Test case for get_channel_message_status

    
    """
    params = [('sub-channel-id', 'sub_channel_id_example'),
                    ('scope', 'scope_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_arn}/messages/{message_idscopemessage_statusx_amz_chime_beare}'.format(channel_arn='channel_arn_example', message_id='message_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_messaging_session_endpoint(client):
    """Test case for get_messaging_session_endpoint

    
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
        path='/endpoints/messaging-session',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_messaging_streaming_configurations(client):
    """Test case for get_messaging_streaming_configurations

    
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
        path='/app-instances/{app_instance_arn}/streaming-configurations'.format(app_instance_arn='app_instance_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channel_bans(client):
    """Test case for list_channel_bans

    
    """
    params = [('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_arn}/bans#x-amz-chime-bearer'.format(channel_arn='channel_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channel_flows(client):
    """Test case for list_channel_flows

    
    """
    params = [('app-instance-arn', 'app_instance_arn_example'),
                    ('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        path='/channel-flows#app-instance-arn',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channel_memberships(client):
    """Test case for list_channel_memberships

    
    """
    params = [('type', 'type_example'),
                    ('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('sub-channel-id', 'sub_channel_id_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_arn}/memberships#x-amz-chime-bearer'.format(channel_arn='channel_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channel_memberships_for_app_instance_user(client):
    """Test case for list_channel_memberships_for_app_instance_user

    
    """
    params = [('app-instance-user-arn', 'app_instance_user_arn_example'),
                    ('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example'),
                    ('scope', 'scope_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels#scope=app-instance-user-memberships&x-amz-chime-bearer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channel_messages(client):
    """Test case for list_channel_messages

    
    """
    params = [('sort-order', 'sort_order_example'),
                    ('not-before', '2013-10-20T19:20:30+01:00'),
                    ('not-after', '2013-10-20T19:20:30+01:00'),
                    ('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('sub-channel-id', 'sub_channel_id_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_arn}/messages#x-amz-chime-bearer'.format(channel_arn='channel_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channel_moderators(client):
    """Test case for list_channel_moderators

    
    """
    params = [('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_arn}/moderators#x-amz-chime-bearer'.format(channel_arn='channel_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channels(client):
    """Test case for list_channels

    
    """
    params = [('app-instance-arn', 'app_instance_arn_example'),
                    ('privacy', 'privacy_example'),
                    ('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels#app-instance-arn&x-amz-chime-bearer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channels_associated_with_channel_flow(client):
    """Test case for list_channels_associated_with_channel_flow

    
    """
    params = [('channel-flow-arn', 'channel_flow_arn_example'),
                    ('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example'),
                    ('scope', 'scope_example')]
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
        path='/channels#scope=channel-flow-associations&channel-flow-arn',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channels_moderated_by_app_instance_user(client):
    """Test case for list_channels_moderated_by_app_instance_user

    
    """
    params = [('app-instance-user-arn', 'app_instance_user_arn_example'),
                    ('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example'),
                    ('scope', 'scope_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels#scope=app-instance-user-moderated-channels&x-amz-chime-bearer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sub_channels(client):
    """Test case for list_sub_channels

    
    """
    params = [('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_arn}/subchannels#x-amz-chime-bearer'.format(channel_arn='channel_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    params = [('arn', 'arn_example')]
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
        path='/tags#arn',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_channel_expiration_settings(client):
    """Test case for put_channel_expiration_settings

    
    """
    body = {"ExpirationSettings":{"ExpirationCriterion":"","ExpirationDays":""}}
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_arn}/expiration-settings'.format(channel_arn='channel_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_channel_membership_preferences(client):
    """Test case for put_channel_membership_preferences

    
    """
    body = {"Preferences":{"PushNotifications":{"AllowNotifications":"","FilterRule":""}}}
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_arn}/memberships/{member_arn}/preferences#x-amz-chime-bearer'.format(channel_arn='channel_arn_example', member_arn='member_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_messaging_streaming_configurations(client):
    """Test case for put_messaging_streaming_configurations

    
    """
    body = {"StreamingConfigurations":""}
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
        method='PUT',
        path='/app-instances/{app_instance_arn}/streaming-configurations'.format(app_instance_arn='app_instance_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redact_channel_message(client):
    """Test case for redact_channel_message

    
    """
    body = {"SubChannelId":""}
    params = [('operation', 'operation_example')]
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{channel_arn}/messages/{message_idoperationredactx_amz_chime_beare}'.format(channel_arn='channel_arn_example', message_id='message_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_channels(client):
    """Test case for search_channels

    
    """
    body = {"Fields":""}
    params = [('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example'),
                    ('operation', 'operation_example')]
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels#operation=search',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_channel_message(client):
    """Test case for send_channel_message

    
    """
    body = {"Persistence":"","SubChannelId":"","ClientRequestToken":"","MessageAttributes":"","Type":"","Target":"","ContentType":"","Content":"","Metadata":"","PushNotification":{"Type":"","Title":"","Body":""}}
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{channel_arn}/messages#x-amz-chime-bearer'.format(channel_arn='channel_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_resource(client):
    """Test case for tag_resource

    
    """
    body = {"ResourceARN":"","Tags":""}
    params = [('operation', 'operation_example')]
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
        path='/tags#operation=tag-resource',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_resource(client):
    """Test case for untag_resource

    
    """
    body = {"ResourceARN":"","TagKeys":""}
    params = [('operation', 'operation_example')]
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
        path='/tags#operation=untag-resource',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_channel(client):
    """Test case for update_channel

    
    """
    body = {"Mode":"","Metadata":"","Name":""}
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_arnx_amz_chime_beare}'.format(channel_arn='channel_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_channel_flow(client):
    """Test case for update_channel_flow

    
    """
    body = {"Processors":"","Name":""}
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
        method='PUT',
        path='/channel-flows/{channel_flow_arn}'.format(channel_flow_arn='channel_flow_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_channel_message(client):
    """Test case for update_channel_message

    
    """
    body = {"SubChannelId":"","ContentType":"","Content":"","Metadata":""}
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_arn}/messages/{message_idx_amz_chime_beare}'.format(channel_arn='channel_arn_example', message_id='message_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_channel_read_marker(client):
    """Test case for update_channel_read_marker

    
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
        'x_amz_chime_bearer': 'x_amz_chime_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_arn}/readMarker#x-amz-chime-bearer'.format(channel_arn='channel_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

