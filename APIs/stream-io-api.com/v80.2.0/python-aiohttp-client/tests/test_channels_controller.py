# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.channel_get_or_create_request import ChannelGetOrCreateRequest
from openapi_server.models.channel_state_response import ChannelStateResponse
from openapi_server.models.channel_stop_watching_request import ChannelStopWatchingRequest
from openapi_server.models.channels_response import ChannelsResponse
from openapi_server.models.delete_channel_response import DeleteChannelResponse
from openapi_server.models.delete_channels_request import DeleteChannelsRequest
from openapi_server.models.delete_channels_response import DeleteChannelsResponse
from openapi_server.models.export_channels_request import ExportChannelsRequest
from openapi_server.models.export_channels_response import ExportChannelsResponse
from openapi_server.models.get_export_channels_status_response import GetExportChannelsStatusResponse
from openapi_server.models.hide_channel_request import HideChannelRequest
from openapi_server.models.hide_channel_response import HideChannelResponse
from openapi_server.models.mark_channels_read_request import MarkChannelsReadRequest
from openapi_server.models.mark_read_request import MarkReadRequest
from openapi_server.models.mark_read_response import MarkReadResponse
from openapi_server.models.mark_unread_request import MarkUnreadRequest
from openapi_server.models.members_response import MembersResponse
from openapi_server.models.mute_channel_request import MuteChannelRequest
from openapi_server.models.mute_channel_response import MuteChannelResponse
from openapi_server.models.query_channels_request import QueryChannelsRequest
from openapi_server.models.query_members_request import QueryMembersRequest
from openapi_server.models.response import Response
from openapi_server.models.search_request import SearchRequest
from openapi_server.models.search_response import SearchResponse
from openapi_server.models.show_channel_request import ShowChannelRequest
from openapi_server.models.show_channel_response import ShowChannelResponse
from openapi_server.models.stop_watching_response import StopWatchingResponse
from openapi_server.models.sync_request import SyncRequest
from openapi_server.models.sync_response import SyncResponse
from openapi_server.models.truncate_channel_request import TruncateChannelRequest
from openapi_server.models.truncate_channel_response import TruncateChannelResponse
from openapi_server.models.unmute_channel_request import UnmuteChannelRequest
from openapi_server.models.unmute_response import UnmuteResponse
from openapi_server.models.update_channel_partial_request import UpdateChannelPartialRequest
from openapi_server.models.update_channel_partial_response import UpdateChannelPartialResponse
from openapi_server.models.update_channel_request import UpdateChannelRequest
from openapi_server.models.update_channel_response import UpdateChannelResponse


pytestmark = pytest.mark.asyncio

async def test_delete_channel(client):
    """Test case for delete_channel

    Delete channel
    """
    params = [('hard_delete', True)]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{type}/{id}'.format(type='type_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channels(client):
    """Test case for delete_channels

    Deletes channels asynchronously
    """
    body = {"cids":["cids","cids"],"hard_delete":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_channels(client):
    """Test case for export_channels

    Export channels
    """
    body = {"channels":[{"messages_until":"2000-01-23T04:56:07.000+00:00","id":"id","messages_since":"2000-01-23T04:56:07.000+00:00","type":"type","cid":"cid"},{"messages_until":"2000-01-23T04:56:07.000+00:00","id":"id","messages_since":"2000-01-23T04:56:07.000+00:00","type":"type","cid":"cid"}],"clear_deleted_message_text":True,"include_truncated_messages":True,"version":"version","export_users":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/export_channels',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_export_channels_status(client):
    """Test case for get_export_channels_status

    Export channels status
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/export_channels/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_or_create_channel_type1(client):
    """Test case for get_or_create_channel_type1

    Get or create channel (type)
    """
    body = {"data":{"auto_translation_enabled":True,"config_overrides":{"blocklist":"blocklist","grants":{"key":["grants","grants"]},"replies":True,"reactions":True,"max_message_length":1601,"url_enrichment":True,"typing_events":True,"commands":["commands","commands"],"blocklist_behavior":"flag","quotes":True,"uploads":True},"own_capabilities":[6,6],"truncated_at":[1,1],"auto_translation_language":"auto_translation_language","members":[{"role":"member","invite_accepted_at":"2000-01-23T04:56:07.000+00:00","invited":True,"created_at":"2000-01-23T04:56:07.000+00:00","ban_expires":"2000-01-23T04:56:07.000+00:00","is_moderator":True,"deleted_at":"2000-01-23T04:56:07.000+00:00","shadow_banned":True,"updated_at":"2000-01-23T04:56:07.000+00:00","user_id":"user_id","banned":True,"channel_role":"channel_role","invite_rejected_at":"2000-01-23T04:56:07.000+00:00","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}},{"role":"member","invite_accepted_at":"2000-01-23T04:56:07.000+00:00","invited":True,"created_at":"2000-01-23T04:56:07.000+00:00","ban_expires":"2000-01-23T04:56:07.000+00:00","is_moderator":True,"deleted_at":"2000-01-23T04:56:07.000+00:00","shadow_banned":True,"updated_at":"2000-01-23T04:56:07.000+00:00","user_id":"user_id","banned":True,"channel_role":"channel_role","invite_rejected_at":"2000-01-23T04:56:07.000+00:00","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}],"truncated_by":[5,5],"frozen":True,"disabled":True,"team":"team","created_by":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"},"truncated_by_id":"truncated_by_id"},"connection_id":"connection_id","watch":True,"members":{"id_lte":9,"offset":2,"id_gt":5,"limit":0,"id_lt":7,"id_gte":2},"hide_for_creator":True,"messages":{"created_at_around":"2000-01-23T04:56:07.000+00:00","created_at_after_or_equal":"2000-01-23T04:56:07.000+00:00","id_lte":"id_lte","offset":7,"id_around":"id_around","created_at_before_or_equal":"2000-01-23T04:56:07.000+00:00","id_gt":"id_gt","created_at_before":"2000-01-23T04:56:07.000+00:00","limit":0,"id_lt":"id_lt","created_at_after":"2000-01-23T04:56:07.000+00:00","id_gte":"id_gte"},"watchers":{"id_lte":9,"offset":2,"id_gt":5,"limit":0,"id_lt":7,"id_gte":2},"state":True,"presence":True,"client_id":"client_id"}
    params = [('client_id', 'client_id_example'),
                    ('connection_id', 'connection_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{type}/query'.format(type='type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_or_create_channel_type_id0(client):
    """Test case for get_or_create_channel_type_id0

    Get or create channel (type, id)
    """
    body = {"data":{"auto_translation_enabled":True,"config_overrides":{"blocklist":"blocklist","grants":{"key":["grants","grants"]},"replies":True,"reactions":True,"max_message_length":1601,"url_enrichment":True,"typing_events":True,"commands":["commands","commands"],"blocklist_behavior":"flag","quotes":True,"uploads":True},"own_capabilities":[6,6],"truncated_at":[1,1],"auto_translation_language":"auto_translation_language","members":[{"role":"member","invite_accepted_at":"2000-01-23T04:56:07.000+00:00","invited":True,"created_at":"2000-01-23T04:56:07.000+00:00","ban_expires":"2000-01-23T04:56:07.000+00:00","is_moderator":True,"deleted_at":"2000-01-23T04:56:07.000+00:00","shadow_banned":True,"updated_at":"2000-01-23T04:56:07.000+00:00","user_id":"user_id","banned":True,"channel_role":"channel_role","invite_rejected_at":"2000-01-23T04:56:07.000+00:00","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}},{"role":"member","invite_accepted_at":"2000-01-23T04:56:07.000+00:00","invited":True,"created_at":"2000-01-23T04:56:07.000+00:00","ban_expires":"2000-01-23T04:56:07.000+00:00","is_moderator":True,"deleted_at":"2000-01-23T04:56:07.000+00:00","shadow_banned":True,"updated_at":"2000-01-23T04:56:07.000+00:00","user_id":"user_id","banned":True,"channel_role":"channel_role","invite_rejected_at":"2000-01-23T04:56:07.000+00:00","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}],"truncated_by":[5,5],"frozen":True,"disabled":True,"team":"team","created_by":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"},"truncated_by_id":"truncated_by_id"},"connection_id":"connection_id","watch":True,"members":{"id_lte":9,"offset":2,"id_gt":5,"limit":0,"id_lt":7,"id_gte":2},"hide_for_creator":True,"messages":{"created_at_around":"2000-01-23T04:56:07.000+00:00","created_at_after_or_equal":"2000-01-23T04:56:07.000+00:00","id_lte":"id_lte","offset":7,"id_around":"id_around","created_at_before_or_equal":"2000-01-23T04:56:07.000+00:00","id_gt":"id_gt","created_at_before":"2000-01-23T04:56:07.000+00:00","limit":0,"id_lt":"id_lt","created_at_after":"2000-01-23T04:56:07.000+00:00","id_gte":"id_gte"},"watchers":{"id_lte":9,"offset":2,"id_gt":5,"limit":0,"id_lt":7,"id_gte":2},"state":True,"presence":True,"client_id":"client_id"}
    params = [('client_id', 'client_id_example'),
                    ('connection_id', 'connection_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{type}/{id}/query'.format(type='type_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hide_channel(client):
    """Test case for hide_channel

    Hide channel
    """
    body = {"user_id":"user_id","clear_history":True,"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{type}/{id}/hide'.format(type='type_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mark_channels_read(client):
    """Test case for mark_channels_read

    Mark channels as read
    """
    body = {"user_id":"user_id","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/read',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mark_read(client):
    """Test case for mark_read

    Mark read
    """
    body = {"user_id":"user_id","message_id":"message_id","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{type}/{id}/read'.format(type='type_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mark_unread(client):
    """Test case for mark_unread

    Mark unread
    """
    body = {"user_id":"user_id","message_id":"message_id","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{type}/{id}/unread'.format(type='type_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mute_channel(client):
    """Test case for mute_channel

    Mute channel
    """
    body = {"channel_cids":["channel_cids","channel_cids"],"user_id":"user_id","expiration":0,"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/moderation/mute/channel',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_channels(client):
    """Test case for query_channels

    Query channels
    """
    body = {"member_limit":60,"offset":5,"sort":[{"field":"field","direction":5},{"field":"field","direction":5}],"client_id":"client_id","connection_id":"connection_id","message_limit":0,"user_id":"user_id","watch":True,"limit":0,"state":True,"presence":True,"filter_conditions":{"key":""},"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    params = [('client_id', 'client_id_example'),
                    ('connection_id', 'connection_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_members(client):
    """Test case for query_members

    Query members
    """
    params = [('payload', openapi_server.QueryMembersRequest())]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/members',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    Search messages
    """
    params = [('payload', openapi_server.SearchRequest())]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_channel(client):
    """Test case for show_channel

    Show channel
    """
    body = {"user_id":"user_id","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{type}/{id}/show'.format(type='type_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_watching_channel(client):
    """Test case for stop_watching_channel

    Stop watching channel
    """
    body = {"connection_id":"connection_id","client_id":"client_id"}
    params = [('client_id', 'client_id_example'),
                    ('connection_id', 'connection_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{type}/{id}/stop-watching'.format(type='type_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync(client):
    """Test case for sync

    Sync
    """
    body = {"last_sync_at":"2000-01-23T04:56:07.000+00:00","channel_cids":["channel_cids","channel_cids"],"connection_id":"connection_id","user_id":"user_id","watch":True,"with_inaccessible_cids":True,"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"},"client_id":"client_id"}
    params = [('with_inaccessible_cids', True),
                    ('watch', True),
                    ('client_id', 'client_id_example'),
                    ('connection_id', 'connection_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_truncate_channel(client):
    """Test case for truncate_channel

    Truncate channel
    """
    body = {"skip_push":True,"truncated_at":"2000-01-23T04:56:07.000+00:00","user_id":"user_id","message":{"parent":[1,1],"pinned":True,"silent":True,"attachments":[{"author_name":"author_name","original_width":6,"thumb_url":"thumb_url","giphy":{"fixed_height":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"original":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"}},"color":"color","footer":"footer","image_url":"image_url","footer_icon":"footer_icon","title_link":"title_link","asset_url":"asset_url","title":"title","type":"type","author_icon":"author_icon","author_link":"author_link","og_scrape_url":"og_scrape_url","pretext":"pretext","original_height":0,"text":"text","fields":[{"short":True,"title":"title","value":"value"},{"short":True,"title":"title","value":"value"}],"actions":[{"name":"name","style":"style","text":"text","type":"type","value":"value"},{"name":"name","style":"style","text":"text","type":"type","value":"value"}],"fallback":"fallback"},{"author_name":"author_name","original_width":6,"thumb_url":"thumb_url","giphy":{"fixed_height":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"original":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"}},"color":"color","footer":"footer","image_url":"image_url","footer_icon":"footer_icon","title_link":"title_link","asset_url":"asset_url","title":"title","type":"type","author_icon":"author_icon","author_link":"author_link","og_scrape_url":"og_scrape_url","pretext":"pretext","original_height":0,"text":"text","fields":[{"short":True,"title":"title","value":"value"},{"short":True,"title":"title","value":"value"}],"actions":[{"name":"name","style":"style","text":"text","type":"type","value":"value"},{"name":"name","style":"style","text":"text","type":"type","value":"value"}],"fallback":"fallback"}],"show_in_channel":True,"reaction_scores":[5,5],"type":"regular","mml":"mml","pin_expires":"2000-01-23T04:56:07.000+00:00","pinned_by":[5,5],"user_id":"user_id","parent_id":"parent_id","pinned_at":"2000-01-23T04:56:07.000+00:00","html":"html","id":"id","text":"text","mentioned_users":["mentioned_users","mentioned_users"],"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"},"cid":[6,6],"quoted_message_id":"quoted_message_id"},"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"},"hard_delete":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{type}/{id}/truncate'.format(type='type_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unmute_channel(client):
    """Test case for unmute_channel

    Unmute channel
    """
    body = {"channel_cids":["channel_cids","channel_cids"],"user_id":"user_id","channel_cid":"channel_cid","expiration":0,"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/moderation/unmute/channel',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_channel(client):
    """Test case for update_channel

    Update channel
    """
    body = {"add_moderators":["add_moderators","add_moderators"],"skip_push":True,"data":{"auto_translation_enabled":True,"config_overrides":{"blocklist":"blocklist","grants":{"key":["grants","grants"]},"replies":True,"reactions":True,"max_message_length":1601,"url_enrichment":True,"typing_events":True,"commands":["commands","commands"],"blocklist_behavior":"flag","quotes":True,"uploads":True},"own_capabilities":[6,6],"truncated_at":[1,1],"auto_translation_language":"auto_translation_language","members":[{"role":"member","invite_accepted_at":"2000-01-23T04:56:07.000+00:00","invited":True,"created_at":"2000-01-23T04:56:07.000+00:00","ban_expires":"2000-01-23T04:56:07.000+00:00","is_moderator":True,"deleted_at":"2000-01-23T04:56:07.000+00:00","shadow_banned":True,"updated_at":"2000-01-23T04:56:07.000+00:00","user_id":"user_id","banned":True,"channel_role":"channel_role","invite_rejected_at":"2000-01-23T04:56:07.000+00:00","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}},{"role":"member","invite_accepted_at":"2000-01-23T04:56:07.000+00:00","invited":True,"created_at":"2000-01-23T04:56:07.000+00:00","ban_expires":"2000-01-23T04:56:07.000+00:00","is_moderator":True,"deleted_at":"2000-01-23T04:56:07.000+00:00","shadow_banned":True,"updated_at":"2000-01-23T04:56:07.000+00:00","user_id":"user_id","banned":True,"channel_role":"channel_role","invite_rejected_at":"2000-01-23T04:56:07.000+00:00","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}],"truncated_by":[5,5],"frozen":True,"disabled":True,"team":"team","created_by":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"},"truncated_by_id":"truncated_by_id"},"remove_members":["remove_members","remove_members"],"add_members":[{"role":"member","invite_accepted_at":"2000-01-23T04:56:07.000+00:00","invited":True,"created_at":"2000-01-23T04:56:07.000+00:00","ban_expires":"2000-01-23T04:56:07.000+00:00","is_moderator":True,"deleted_at":"2000-01-23T04:56:07.000+00:00","shadow_banned":True,"updated_at":"2000-01-23T04:56:07.000+00:00","user_id":"user_id","banned":True,"channel_role":"channel_role","invite_rejected_at":"2000-01-23T04:56:07.000+00:00","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}},{"role":"member","invite_accepted_at":"2000-01-23T04:56:07.000+00:00","invited":True,"created_at":"2000-01-23T04:56:07.000+00:00","ban_expires":"2000-01-23T04:56:07.000+00:00","is_moderator":True,"deleted_at":"2000-01-23T04:56:07.000+00:00","shadow_banned":True,"updated_at":"2000-01-23T04:56:07.000+00:00","user_id":"user_id","banned":True,"channel_role":"channel_role","invite_rejected_at":"2000-01-23T04:56:07.000+00:00","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}],"message":{"parent":[1,1],"pinned":True,"silent":True,"attachments":[{"author_name":"author_name","original_width":6,"thumb_url":"thumb_url","giphy":{"fixed_height":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"original":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"}},"color":"color","footer":"footer","image_url":"image_url","footer_icon":"footer_icon","title_link":"title_link","asset_url":"asset_url","title":"title","type":"type","author_icon":"author_icon","author_link":"author_link","og_scrape_url":"og_scrape_url","pretext":"pretext","original_height":0,"text":"text","fields":[{"short":True,"title":"title","value":"value"},{"short":True,"title":"title","value":"value"}],"actions":[{"name":"name","style":"style","text":"text","type":"type","value":"value"},{"name":"name","style":"style","text":"text","type":"type","value":"value"}],"fallback":"fallback"},{"author_name":"author_name","original_width":6,"thumb_url":"thumb_url","giphy":{"fixed_height":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"original":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"}},"color":"color","footer":"footer","image_url":"image_url","footer_icon":"footer_icon","title_link":"title_link","asset_url":"asset_url","title":"title","type":"type","author_icon":"author_icon","author_link":"author_link","og_scrape_url":"og_scrape_url","pretext":"pretext","original_height":0,"text":"text","fields":[{"short":True,"title":"title","value":"value"},{"short":True,"title":"title","value":"value"}],"actions":[{"name":"name","style":"style","text":"text","type":"type","value":"value"},{"name":"name","style":"style","text":"text","type":"type","value":"value"}],"fallback":"fallback"}],"show_in_channel":True,"reaction_scores":[5,5],"type":"regular","mml":"mml","pin_expires":"2000-01-23T04:56:07.000+00:00","pinned_by":[5,5],"user_id":"user_id","parent_id":"parent_id","pinned_at":"2000-01-23T04:56:07.000+00:00","html":"html","id":"id","text":"text","mentioned_users":["mentioned_users","mentioned_users"],"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"},"cid":[6,6],"quoted_message_id":"quoted_message_id"},"hide_history":True,"assign_roles":[{"role":"member","invite_accepted_at":"2000-01-23T04:56:07.000+00:00","invited":True,"created_at":"2000-01-23T04:56:07.000+00:00","ban_expires":"2000-01-23T04:56:07.000+00:00","is_moderator":True,"deleted_at":"2000-01-23T04:56:07.000+00:00","shadow_banned":True,"updated_at":"2000-01-23T04:56:07.000+00:00","user_id":"user_id","banned":True,"channel_role":"channel_role","invite_rejected_at":"2000-01-23T04:56:07.000+00:00","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}},{"role":"member","invite_accepted_at":"2000-01-23T04:56:07.000+00:00","invited":True,"created_at":"2000-01-23T04:56:07.000+00:00","ban_expires":"2000-01-23T04:56:07.000+00:00","is_moderator":True,"deleted_at":"2000-01-23T04:56:07.000+00:00","shadow_banned":True,"updated_at":"2000-01-23T04:56:07.000+00:00","user_id":"user_id","banned":True,"channel_role":"channel_role","invite_rejected_at":"2000-01-23T04:56:07.000+00:00","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}],"reject_invite":True,"user_id":"user_id","cooldown":9,"invites":[{"role":"member","invite_accepted_at":"2000-01-23T04:56:07.000+00:00","invited":True,"created_at":"2000-01-23T04:56:07.000+00:00","ban_expires":"2000-01-23T04:56:07.000+00:00","is_moderator":True,"deleted_at":"2000-01-23T04:56:07.000+00:00","shadow_banned":True,"updated_at":"2000-01-23T04:56:07.000+00:00","user_id":"user_id","banned":True,"channel_role":"channel_role","invite_rejected_at":"2000-01-23T04:56:07.000+00:00","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}},{"role":"member","invite_accepted_at":"2000-01-23T04:56:07.000+00:00","invited":True,"created_at":"2000-01-23T04:56:07.000+00:00","ban_expires":"2000-01-23T04:56:07.000+00:00","is_moderator":True,"deleted_at":"2000-01-23T04:56:07.000+00:00","shadow_banned":True,"updated_at":"2000-01-23T04:56:07.000+00:00","user_id":"user_id","banned":True,"channel_role":"channel_role","invite_rejected_at":"2000-01-23T04:56:07.000+00:00","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}],"demote_moderators":["demote_moderators","demote_moderators"],"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"},"accept_invite":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{type}/{id}'.format(type='type_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_channel_partial(client):
    """Test case for update_channel_partial

    Partially update channel
    """
    body = {"set":{"key":""},"user_id":"user_id","unset":["unset","unset"],"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/channels/{type}/{id}'.format(type='type_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

