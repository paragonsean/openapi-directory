# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.api_error import APIError
from openapi_server.models.file_delete_response import FileDeleteResponse
from openapi_server.models.file_upload_response import FileUploadResponse
from openapi_server.models.flag_request import FlagRequest
from openapi_server.models.flag_response import FlagResponse
from openapi_server.models.get_many_messages_response import GetManyMessagesResponse
from openapi_server.models.get_og_response import GetOGResponse
from openapi_server.models.get_reactions_response import GetReactionsResponse
from openapi_server.models.get_replies_response import GetRepliesResponse
from openapi_server.models.image_size_request import ImageSizeRequest
from openapi_server.models.image_upload_response import ImageUploadResponse
from openapi_server.models.mark_channels_read_request import MarkChannelsReadRequest
from openapi_server.models.mark_read_request import MarkReadRequest
from openapi_server.models.mark_read_response import MarkReadResponse
from openapi_server.models.mark_unread_request import MarkUnreadRequest
from openapi_server.models.message_action_request import MessageActionRequest
from openapi_server.models.message_response import MessageResponse
from openapi_server.models.message_with_pending_metadata_response import MessageWithPendingMetadataResponse
from openapi_server.models.only_user_id_request import OnlyUserIDRequest
from openapi_server.models.query_message_flags_request import QueryMessageFlagsRequest
from openapi_server.models.query_message_flags_response import QueryMessageFlagsResponse
from openapi_server.models.reaction_removal_response import ReactionRemovalResponse
from openapi_server.models.reaction_response import ReactionResponse
from openapi_server.models.response import Response
from openapi_server.models.search_request import SearchRequest
from openapi_server.models.search_response import SearchResponse
from openapi_server.models.send_message_request import SendMessageRequest
from openapi_server.models.send_reaction_request import SendReactionRequest
from openapi_server.models.translate_message_request import TranslateMessageRequest
from openapi_server.models.update_message_partial_request import UpdateMessagePartialRequest
from openapi_server.models.update_message_request import UpdateMessageRequest


pytestmark = pytest.mark.asyncio

async def test_delete_file(client):
    """Test case for delete_file

    Delete file
    """
    params = [('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{type}/{id}/file'.format(type='type_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_image(client):
    """Test case for delete_image

    Delete image
    """
    params = [('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{type}/{id}/image'.format(type='type_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_message(client):
    """Test case for delete_message

    Delete message
    """
    params = [('hard', True)]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/messages/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_reaction(client):
    """Test case for delete_reaction

    Delete reaction
    """
    params = [('user_id', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/messages/{id}/reaction/{type}'.format(id='id_example', type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flag_0(client):
    """Test case for flag_0

    Flag
    """
    body = {"user_id":"user_id","target_message_id":"target_message_id","target_user_id":"target_user_id","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/moderation/flag',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_many_messages(client):
    """Test case for get_many_messages

    Get many messages
    """
    params = [('ids', ['ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{type}/{id}/messages'.format(type='type_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_message(client):
    """Test case for get_message

    Get message
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/messages/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_og(client):
    """Test case for get_og

    Get OG
    """
    params = [('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/og',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reactions(client):
    """Test case for get_reactions

    Get reactions
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/messages/{id}/reactions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_replies(client):
    """Test case for get_replies

    Get replies
    """
    params = [('id_gte', 'id_gte_example'),
                    ('id_gt', 'id_gt_example'),
                    ('id_lte', 'id_lte_example'),
                    ('id_lt', 'id_lt_example'),
                    ('created_at_after_or_equal', '2013-10-20T19:20:30+01:00'),
                    ('created_at_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at_before_or_equal', '2013-10-20T19:20:30+01:00'),
                    ('created_at_before', '2013-10-20T19:20:30+01:00'),
                    ('id_around', 'id_around_example'),
                    ('created_at_around', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/messages/{parent_id}/replies'.format(parent_id='parent_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mark_channels_read_0(client):
    """Test case for mark_channels_read_0

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

async def test_mark_read_0(client):
    """Test case for mark_read_0

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

async def test_mark_unread_0(client):
    """Test case for mark_unread_0

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

async def test_query_message_flags(client):
    """Test case for query_message_flags

    Query Message Flags
    """
    params = [('payload', openapi_server.QueryMessageFlagsRequest())]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/moderation/flags/message',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_message_action(client):
    """Test case for run_message_action

    Run message command action
    """
    body = {"form_data":{"key":"form_data"},"user_id":"user_id","ID":"ID","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/messages/{id}/action'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_0(client):
    """Test case for search_0

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

async def test_send_message(client):
    """Test case for send_message

    Send new message
    """
    body = {"skip_enrich_url":True,"skip_push":True,"keep_channel_hidden":True,"message":{"parent":[1,1],"pinned":True,"silent":True,"attachments":[{"author_name":"author_name","original_width":6,"thumb_url":"thumb_url","giphy":{"fixed_height":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"original":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"}},"color":"color","footer":"footer","image_url":"image_url","footer_icon":"footer_icon","title_link":"title_link","asset_url":"asset_url","title":"title","type":"type","author_icon":"author_icon","author_link":"author_link","og_scrape_url":"og_scrape_url","pretext":"pretext","original_height":0,"text":"text","fields":[{"short":True,"title":"title","value":"value"},{"short":True,"title":"title","value":"value"}],"actions":[{"name":"name","style":"style","text":"text","type":"type","value":"value"},{"name":"name","style":"style","text":"text","type":"type","value":"value"}],"fallback":"fallback"},{"author_name":"author_name","original_width":6,"thumb_url":"thumb_url","giphy":{"fixed_height":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"original":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"}},"color":"color","footer":"footer","image_url":"image_url","footer_icon":"footer_icon","title_link":"title_link","asset_url":"asset_url","title":"title","type":"type","author_icon":"author_icon","author_link":"author_link","og_scrape_url":"og_scrape_url","pretext":"pretext","original_height":0,"text":"text","fields":[{"short":True,"title":"title","value":"value"},{"short":True,"title":"title","value":"value"}],"actions":[{"name":"name","style":"style","text":"text","type":"type","value":"value"},{"name":"name","style":"style","text":"text","type":"type","value":"value"}],"fallback":"fallback"}],"show_in_channel":True,"reaction_scores":[5,5],"type":"regular","mml":"mml","pin_expires":"2000-01-23T04:56:07.000+00:00","pinned_by":[5,5],"user_id":"user_id","parent_id":"parent_id","pinned_at":"2000-01-23T04:56:07.000+00:00","html":"html","id":"id","text":"text","mentioned_users":["mentioned_users","mentioned_users"],"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"},"cid":[6,6],"quoted_message_id":"quoted_message_id"},"force_moderation":True,"pending_message_metadata":{"key":"pending_message_metadata"},"is_pending_message":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{type}/{id}/message'.format(type='type_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_reaction(client):
    """Test case for send_reaction

    Send reaction
    """
    body = {"skip_push":True,"reaction":{"score":7,"user_id":"user_id","message_id":"message_id","type":"type","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}},"enforce_unique":True,"ID":"ID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/messages/{id}/reaction'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_message(client):
    """Test case for translate_message

    Translate message
    """
    body = {"language":"af"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/messages/{id}/translate'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unflag_0(client):
    """Test case for unflag_0

    Unflag
    """
    body = {"user_id":"user_id","target_message_id":"target_message_id","target_user_id":"target_user_id","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/moderation/unflag',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_message(client):
    """Test case for update_message

    Update message
    """
    body = {"skip_enrich_url":True,"message":{"parent":[1,1],"pinned":True,"silent":True,"attachments":[{"author_name":"author_name","original_width":6,"thumb_url":"thumb_url","giphy":{"fixed_height":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"original":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"}},"color":"color","footer":"footer","image_url":"image_url","footer_icon":"footer_icon","title_link":"title_link","asset_url":"asset_url","title":"title","type":"type","author_icon":"author_icon","author_link":"author_link","og_scrape_url":"og_scrape_url","pretext":"pretext","original_height":0,"text":"text","fields":[{"short":True,"title":"title","value":"value"},{"short":True,"title":"title","value":"value"}],"actions":[{"name":"name","style":"style","text":"text","type":"type","value":"value"},{"name":"name","style":"style","text":"text","type":"type","value":"value"}],"fallback":"fallback"},{"author_name":"author_name","original_width":6,"thumb_url":"thumb_url","giphy":{"fixed_height":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"original":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"}},"color":"color","footer":"footer","image_url":"image_url","footer_icon":"footer_icon","title_link":"title_link","asset_url":"asset_url","title":"title","type":"type","author_icon":"author_icon","author_link":"author_link","og_scrape_url":"og_scrape_url","pretext":"pretext","original_height":0,"text":"text","fields":[{"short":True,"title":"title","value":"value"},{"short":True,"title":"title","value":"value"}],"actions":[{"name":"name","style":"style","text":"text","type":"type","value":"value"},{"name":"name","style":"style","text":"text","type":"type","value":"value"}],"fallback":"fallback"}],"show_in_channel":True,"reaction_scores":[5,5],"type":"regular","mml":"mml","pin_expires":"2000-01-23T04:56:07.000+00:00","pinned_by":[5,5],"user_id":"user_id","parent_id":"parent_id","pinned_at":"2000-01-23T04:56:07.000+00:00","html":"html","id":"id","text":"text","mentioned_users":["mentioned_users","mentioned_users"],"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"},"cid":[6,6],"quoted_message_id":"quoted_message_id"},"pending_message_metadata":{"key":"pending_message_metadata"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/messages/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_message_partial(client):
    """Test case for update_message_partial

    Partially message update
    """
    body = {"skip_enrich_url":True,"set":{"key":""},"user_id":"user_id","unset":["unset","unset"],"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/messages/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_file(client):
    """Test case for upload_file

    Upload file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    data = FormData()
    data.add_field('file', 'file_example')
    data.add_field('user', openapi_server.OnlyUserIDRequest())
    response = await client.request(
        method='POST',
        path='/channels/{type}/{id}/file'.format(type='type_example', id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_image(client):
    """Test case for upload_image

    Upload image
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    data = FormData()
    data.add_field('file', 'file_example')
    data.add_field('upload_sizes', [openapi_server.ImageSizeRequest()])
    data.add_field('user', openapi_server.OnlyUserIDRequest())
    response = await client.request(
        method='POST',
        path='/channels/{type}/{id}/image'.format(type='type_example', id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

