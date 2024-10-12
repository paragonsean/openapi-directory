# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.check_push_request import CheckPushRequest
from openapi_server.models.check_push_response import CheckPushResponse
from openapi_server.models.check_sqs_request import CheckSQSRequest
from openapi_server.models.check_sqs_response import CheckSQSResponse
from openapi_server.models.create_block_list_request import CreateBlockListRequest
from openapi_server.models.create_channel_type_request import CreateChannelTypeRequest
from openapi_server.models.create_channel_type_response import CreateChannelTypeResponse
from openapi_server.models.get_application_response import GetApplicationResponse
from openapi_server.models.get_block_list_response import GetBlockListResponse
from openapi_server.models.get_rate_limits_response import GetRateLimitsResponse
from openapi_server.models.list_block_list_response import ListBlockListResponse
from openapi_server.models.list_channel_types_response import ListChannelTypesResponse
from openapi_server.models.list_push_providers_response import ListPushProvidersResponse
from openapi_server.models.response import Response
from openapi_server.models.update_app_request import UpdateAppRequest
from openapi_server.models.update_block_list_request import UpdateBlockListRequest
from openapi_server.models.update_channel_type_request import UpdateChannelTypeRequest
from openapi_server.models.update_channel_type_response import UpdateChannelTypeResponse
from openapi_server.models.upsert_push_provider_request import UpsertPushProviderRequest
from openapi_server.models.upsert_push_provider_response import UpsertPushProviderResponse


pytestmark = pytest.mark.asyncio

async def test_check_push(client):
    """Test case for check_push

    Check push
    """
    body = {"skip_devices":True,"firebase_template":"firebase_template","user_id":"user_id","apn_template":"apn_template","push_provider_name":"push_provider_name","push_provider_type":"firebase","firebase_data_template":"firebase_data_template","message_id":"message_id","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/check_push',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_sqs(client):
    """Test case for check_sqs

    Check SQS
    """
    body = {"sqs_key":"sqs_key","sqs_url":"sqs_url","sqs_secret":"sqs_secret"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/check_sqs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_block_list(client):
    """Test case for create_block_list

    Create block list
    """
    body = {"name":"name","words":["words","words"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/blocklists',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_channel_type(client):
    """Test case for create_channel_type

    Create channel type
    """
    body = {"blocklist":"blocklist","grants":{"key":["grants","grants"]},"push_notifications":True,"custom_events":True,"automod":"disabled","message_retention":"message_retention","url_enrichment":True,"mutes":True,"read_events":True,"blocklist_behavior":"flag","uploads":True,"connect_events":True,"automod_behavior":"flag","search":True,"replies":True,"permissions":[{"owner":True,"roles":["roles","roles"],"name":"name","action":"Deny","resources":["resources","resources"],"priority":602},{"owner":True,"roles":["roles","roles"],"name":"name","action":"Deny","resources":["resources","resources"],"priority":602}],"name":"name","reactions":True,"max_message_length":0,"typing_events":True,"commands":["commands","commands"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channeltypes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_block_list(client):
    """Test case for delete_block_list

    Delete block list
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/blocklists/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel_type(client):
    """Test case for delete_channel_type

    Delete channel type
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channeltypes/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_push_provider_0(client):
    """Test case for delete_push_provider_0

    Delete a push provider
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/push_providers/{type}/{name}'.format(type='type_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_app(client):
    """Test case for get_app

    Get App Settings
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/app',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_block_list(client):
    """Test case for get_block_list

    Get block list
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/blocklists/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_type(client):
    """Test case for get_channel_type

    Get channel type
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channeltypes/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rate_limits(client):
    """Test case for get_rate_limits

    Get rate limits
    """
    params = [('server_side', True),
                    ('android', True),
                    ('ios', True),
                    ('web', True),
                    ('endpoints', 'endpoints_example')]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rate_limits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_block_lists(client):
    """Test case for list_block_lists

    List block lists
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/blocklists',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channel_types(client):
    """Test case for list_channel_types

    List channel types
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channeltypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_push_providers_0(client):
    """Test case for list_push_providers_0

    List push providers
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/push_providers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_app(client):
    """Test case for update_app

    Update App Settings
    """
    body = {"auto_translation_enabled":True,"channel_hide_members_only":True,"image_moderation_labels":["image_moderation_labels","image_moderation_labels"],"push_config":{"offline_only":True,"version":"v1"},"permission_version":"v1","sqs_url":"sqs_url","file_upload_config":{"blocked_file_extensions":["blocked_file_extensions","blocked_file_extensions"],"blocked_mime_types":["blocked_mime_types","blocked_mime_types"],"allowed_mime_types":["allowed_mime_types","allowed_mime_types"],"allowed_file_extensions":["allowed_file_extensions","allowed_file_extensions"]},"before_message_send_hook_url":"before_message_send_hook_url","custom_action_handler_url":"custom_action_handler_url","firebase_config":{"credentials_json":"credentials_json","apn_template":"apn_template","notification_template":"notification_template","Disabled":True,"data_template":"data_template","server_key":"server_key"},"video_provider":"agora","async_url_enrich_enabled":True,"agora_options":{"app_certificate":"app_certificate","role_map":{"key":"role_map"},"default_role":"attendee","app_id":"app_id"},"apn_config":{"auth_type":"certificate","development":True,"p12_cert":"p12_cert","key_id":"key_id","bundle_id":"bundle_id","notification_template":"notification_template","host":"host","auth_key":"auth_key","team_id":"team_id","Disabled":True},"huawei_config":{"id":"id","secret":"secret","Disabled":True},"multi_tenant_enabled":True,"sqs_secret":"sqs_secret","grants":{"key":["grants","grants"]},"migrate_permissions_to_v2":True,"user_search_disallowed_roles":["user_search_disallowed_roles","user_search_disallowed_roles"],"reminders_interval":12715,"enforce_unique_usernames":"false","webhook_url":"webhook_url","disable_auth_checks":True,"disable_permissions_checks":True,"image_moderation_block_labels":["image_moderation_block_labels","image_moderation_block_labels"],"cdn_expiration_seconds":734801,"hms_options":{"app_certificate":"app_certificate","role_map":{"key":"role_map"},"default_role":"attendee","app_id":"app_id"},"webhook_events":["webhook_events","webhook_events"],"image_upload_config":{"blocked_file_extensions":["blocked_file_extensions","blocked_file_extensions"],"blocked_mime_types":["blocked_mime_types","blocked_mime_types"],"allowed_mime_types":["allowed_mime_types","allowed_mime_types"],"allowed_file_extensions":["allowed_file_extensions","allowed_file_extensions"]},"async_moderation_config":{"callback":{"mode":"CALLBACK_MODE_NONE","server_url":"server_url"},"timeout_ms":0},"xiaomi_config":{"package_name":"package_name","secret":"secret","Disabled":True},"sqs_key":"sqs_key","revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","image_moderation_enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/app',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_block_list(client):
    """Test case for update_block_list

    Update block list
    """
    body = {"words":["words","words"],"Name":"Name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/blocklists/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_channel_type(client):
    """Test case for update_channel_type

    Update channel type
    """
    body = {"blocklist":"blocklist","grants":{"key":["grants","grants"]},"push_notifications":True,"reminders":True,"custom_events":True,"automod":"disabled","message_retention":"message_retention","url_enrichment":True,"mutes":True,"read_events":True,"NameFromPath":"NameFromPath","blocklist_behavior":"flag","quotes":True,"uploads":True,"connect_events":True,"automod_behavior":"flag","search":True,"replies":True,"automod_thresholds":{"explicit":{"flag":0.5637377,"block":0.5962134},"toxic":{"flag":0.5637377,"block":0.5962134},"spam":{"flag":0.5637377,"block":0.5962134}},"permissions":[{"owner":True,"roles":["roles","roles"],"name":"name","action":"Deny","resources":["resources","resources"],"priority":602},{"owner":True,"roles":["roles","roles"],"name":"name","action":"Deny","resources":["resources","resources"],"priority":602}],"reactions":True,"max_message_length":1601,"typing_events":True,"commands":["commands","commands"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channeltypes/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert_push_provider_0(client):
    """Test case for upsert_push_provider_0

    Upsert a push provider
    """
    body = {"push_provider":{"xiaomi_package_name":"xiaomi_package_name","apn_key_id":"apn_key_id","created_at":"2000-01-23T04:56:07.000+00:00","description":"description","firebase_data_template":"firebase_data_template","type":0,"firebase_credentials":"firebase_credentials","apn_p12_cert":"apn_p12_cert","updated_at":"2000-01-23T04:56:07.000+00:00","firebase_apn_template":"firebase_apn_template","apn_auth_key":"apn_auth_key","apn_topic":"apn_topic","apn_host":"apn_host","apn_development":True,"apn_auth_type":"apn_auth_type","disabled_at":"2000-01-23T04:56:07.000+00:00","xiaomi_app_secret":"xiaomi_app_secret","firebase_server_key":"firebase_server_key","apn_team_id":"apn_team_id","disabled_reason":"disabled_reason","huawei_app_secret":"huawei_app_secret","huawei_app_id":"huawei_app_id","name":"name","firebase_notification_template":"firebase_notification_template","apn_notification_template":"apn_notification_template"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/push_providers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

