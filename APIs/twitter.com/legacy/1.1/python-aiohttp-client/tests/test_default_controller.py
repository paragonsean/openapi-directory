# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_account_settings_get(client):
    """Test case for account_settings_get

    
    """
    params = [('trend_location_woeid', 'trend_location_woeid_example'),
                    ('sleep_time_enabled', 'sleep_time_enabled_example'),
                    ('start_sleep_time', 'start_sleep_time_example'),
                    ('end_sleep_time', 'end_sleep_time_example'),
                    ('time_zone', 'time_zone_example'),
                    ('lang', 'lang_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/account/settings.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_settings_post(client):
    """Test case for account_settings_post

    
    """
    params = [('trend_location_woeid', 'trend_location_woeid_example'),
                    ('sleep_time_enabled', 'sleep_time_enabled_example'),
                    ('start_sleep_time', 'start_sleep_time_example'),
                    ('end_sleep_time', 'end_sleep_time_example'),
                    ('time_zone', 'time_zone_example'),
                    ('lang', 'lang_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/account/settings.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_update_delivery_device(client):
    """Test case for account_update_delivery_device

    
    """
    params = [('device', 'device_example'),
                    ('include_entities', 'include_entities_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/account/update_delivery_device.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_update_profile(client):
    """Test case for account_update_profile

    
    """
    params = [('name', 'name_example'),
                    ('url', 'url_example'),
                    ('location', 'location_example'),
                    ('description', 'description_example'),
                    ('include_entities', 'include_entities_example'),
                    ('skip_status', 'skip_status_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/account/update_profile.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_update_profile_background_image(client):
    """Test case for accounts_update_profile_background_image

    
    """
    params = [('tile', 'tile_example'),
                    ('use', 'use_example'),
                    ('include_entities', 'include_entities_example'),
                    ('skip_status', 'skip_status_example')]
    headers = { 
        'content_type': 'multipart/form-data',
    }
    response = await client.request(
        method='POST',
        path='/1.1/account/update_profile_background_image.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_update_profile_colors(client):
    """Test case for accounts_update_profile_colors

    
    """
    params = [('profile_background_color', 'profile_background_color_example'),
                    ('profile_link_color', 'profile_link_color_example'),
                    ('profile_sidebar_border_color', 'profile_sidebar_border_color_example'),
                    ('profile_sidebar_fill_color', 'profile_sidebar_fill_color_example'),
                    ('profile_text_color', 'profile_text_color_example'),
                    ('include_entities', 'include_entities_example'),
                    ('skip_status', 'skip_status_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/account/update_profile_colors.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_update_profile_image(client):
    """Test case for accounts_update_profile_image

    
    """
    params = [('skip_status', 'skip_status_example')]
    headers = { 
        'content_type': 'multipart/form-data',
    }
    response = await client.request(
        method='POST',
        path='/1.1/account/update_profile_image.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_rate_limit_status(client):
    """Test case for application_rate_limit_status

    
    """
    params = [('resources', 'resources_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/application/rate_limit_status.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blocks_create(client):
    """Test case for blocks_create

    
    """
    params = [('include_entities', 'include_entities_example'),
                    ('skip_status', 'skip_status_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/blocks/create.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blocks_destroy(client):
    """Test case for blocks_destroy

    
    """
    params = [('include_entities', 'include_entities_example'),
                    ('skip_status', 'skip_status_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/blocks/destroy.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blocks_ids(client):
    """Test case for blocks_ids

    
    """
    params = [('stringify_ids', 'stringify_ids_example'),
                    ('cursor', 'cursor_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/blocks/ids.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blocks_list(client):
    """Test case for blocks_list

    
    """
    params = [('include_entities', 'include_entities_example'),
                    ('skip_status', 'skip_status_example'),
                    ('cursor', 'cursor_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/blocks/list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_direct_messages(client):
    """Test case for direct_messages

    
    """
    params = [('count', 'count_example'),
                    ('since_id', 'since_id_example'),
                    ('max_id', 'max_id_example'),
                    ('include_entities', 'include_entities_example'),
                    ('page', 'page_example'),
                    ('skip_status', 'skip_status_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/direct_messages.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_direct_messages_destroy(client):
    """Test case for direct_messages_destroy

    
    """
    params = [('id', 'id_example'),
                    ('include_entities', 'include_entities_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/direct_messages/destroy.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_direct_messages_new(client):
    """Test case for direct_messages_new

    
    """
    params = [('text', 'text_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/direct_messages/new.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_direct_messages_sent(client):
    """Test case for direct_messages_sent

    
    """
    params = [('count', 'count_example'),
                    ('since_id', 'since_id_example'),
                    ('max_id', 'max_id_example'),
                    ('include_entities', 'include_entities_example'),
                    ('page', 'page_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/direct_messages/sent.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_direct_messages_show(client):
    """Test case for direct_messages_show

    
    """
    params = [('id', 'id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/direct_messages/show.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_favorites_create(client):
    """Test case for favorites_create

    
    """
    params = [('id', 'id_example'),
                    ('include_entities', 'include_entities_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/favorites/create.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_favorites_destroy(client):
    """Test case for favorites_destroy

    
    """
    params = [('id', 'id_example'),
                    ('include_entities', 'include_entities_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/favorites/destroy.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_favorites_list(client):
    """Test case for favorites_list

    
    """
    params = [('count', 'count_example'),
                    ('since_id', 'since_id_example'),
                    ('max_id', 'max_id_example'),
                    ('include_entities', 'include_entities_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/favorites/list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_followers_ids(client):
    """Test case for followers_ids

    
    """
    params = [('stringify_ids', 'stringify_ids_example'),
                    ('cursor', 'cursor_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/followers/ids.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_friends_ids(client):
    """Test case for friends_ids

    
    """
    params = [('stringify_ids', 'stringify_ids_example'),
                    ('cursor', 'cursor_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/friends/ids.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_friendships_create(client):
    """Test case for friendships_create

    
    """
    params = [('follow', 'follow_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/friendships/create.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_friendships_destroy(client):
    """Test case for friendships_destroy

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/friendships/destroy.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_friendships_incoming(client):
    """Test case for friendships_incoming

    
    """
    params = [('stringify_ids', 'stringify_ids_example'),
                    ('cursor', 'cursor_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/friendships/incoming.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_friendships_lookup(client):
    """Test case for friendships_lookup

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/friendships/lookup.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_friendships_outgoing(client):
    """Test case for friendships_outgoing

    
    """
    params = [('stringify_ids', 'stringify_ids_example'),
                    ('cursor', 'cursor_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/friendships/outgoing.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_friendships_show(client):
    """Test case for friendships_show

    
    """
    params = [('source_id', 'source_id_example'),
                    ('source_screen_name', 'source_screen_name_example'),
                    ('target_id', 'target_id_example'),
                    ('target_screen_name', 'target_screen_name_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/friendships/show.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_friendships_update(client):
    """Test case for friendships_update

    
    """
    params = [('device', 'device_example'),
                    ('retweets', 'retweets_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/friendships/update.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_geo_place_id(client):
    """Test case for geo_place_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/geo/id/{place_id_jso}'.format(place_id='place_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_geo_places(client):
    """Test case for geo_places

    
    """
    params = [('attribute:street_address', 'attributestreet_address_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/geo/places.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_geo_reverse_geocode(client):
    """Test case for geo_reverse_geocode

    
    """
    params = [('lat', 'lat_example'),
                    ('long', 'long_example'),
                    ('accuracy', 'accuracy_example'),
                    ('granularity', 'granularity_example'),
                    ('max_results', 'max_results_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/geo/reverse_geocode.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_geo_search(client):
    """Test case for geo_search

    
    """
    params = [('accuracy', 'accuracy_example'),
                    ('granularity', 'granularity_example'),
                    ('contained_within', 'contained_within_example'),
                    ('attribute:street_address', 'attributestreet_address_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/geo/search.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_geo_similar_places(client):
    """Test case for geo_similar_places

    
    """
    params = [('contained_within', 'contained_within_example'),
                    ('attribute:street_address', 'attributestreet_address_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/geo/similar_places.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_help_configurations(client):
    """Test case for help_configurations

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/help/configuration.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_help_languages(client):
    """Test case for help_languages

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/help/languages.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_help_privacy(client):
    """Test case for help_privacy

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/help/privacy.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_help_tos(client):
    """Test case for help_tos

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/help/tos.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_create(client):
    """Test case for lists_create

    
    """
    params = [('name', 'name_example'),
                    ('mode', 'mode_example'),
                    ('description', 'description_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/lists/create.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_destroy(client):
    """Test case for lists_destroy

    
    """
    params = [('owner_screen_name', 'owner_screen_name_example'),
                    ('owner_id', 'owner_id_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/lists/destroy.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_list(client):
    """Test case for lists_list

    
    """
    params = [('screen_name', 'screen_name_example'),
                    ('user_id', 'user_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/lists/list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_members(client):
    """Test case for lists_members

    
    """
    params = [('owner_screen_name', 'owner_screen_name_example'),
                    ('owner_id', 'owner_id_example'),
                    ('include_entities', 'include_entities_example'),
                    ('skip_status', 'skip_status_example'),
                    ('cursor', 'cursor_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/lists/members.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_members_create(client):
    """Test case for lists_members_create

    
    """
    params = [('owner_screen_name', 'owner_screen_name_example'),
                    ('owner_id', 'owner_id_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/lists/members/create.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_members_create_all(client):
    """Test case for lists_members_create_all

    
    """
    params = [('owner_screen_name', 'owner_screen_name_example'),
                    ('owner_id', 'owner_id_example'),
                    ('user_id', 'user_id_example'),
                    ('screen_name', 'screen_name_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/lists/members/create_all.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_members_destroy(client):
    """Test case for lists_members_destroy

    
    """
    params = [('list_id', 'list_id_example'),
                    ('slug', 'slug_example'),
                    ('owner_screen_name', 'owner_screen_name_example'),
                    ('owner_id', 'owner_id_example'),
                    ('user_id', 'user_id_example'),
                    ('screen_name', 'screen_name_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/lists/members/destroy.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_members_destroy_all(client):
    """Test case for lists_members_destroy_all

    
    """
    params = [('owner_screen_name', 'owner_screen_name_example'),
                    ('owner_id', 'owner_id_example'),
                    ('screen_name', 'screen_name_example'),
                    ('user_id', 'user_id_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/lists/members/destroy_all.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_members_show(client):
    """Test case for lists_members_show

    
    """
    params = [('owner_screen_name', 'owner_screen_name_example'),
                    ('owner_id', 'owner_id_example'),
                    ('include_entities', 'include_entities_example'),
                    ('skip_status', 'skip_status_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/lists/members/show.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_memberships(client):
    """Test case for lists_memberships

    
    """
    params = [('user_id', 'user_id_example'),
                    ('screen_name', 'screen_name_example'),
                    ('cursor', 'cursor_example'),
                    ('filter_to_owned_lists', 'filter_to_owned_lists_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/lists/memberships.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_show(client):
    """Test case for lists_show

    
    """
    params = [('owner_screen_name', 'owner_screen_name_example'),
                    ('owner_id', 'owner_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/lists/show.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_statuses(client):
    """Test case for lists_statuses

    
    """
    params = [('owner_screen_name', 'owner_screen_name_example'),
                    ('owner_id', 'owner_id_example'),
                    ('since_id', 'since_id_example'),
                    ('max_id', 'max_id_example'),
                    ('count', 'count_example'),
                    ('include_entities', 'include_entities_example'),
                    ('include_rts', 'include_rts_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/lists/statuses.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_subscribers(client):
    """Test case for lists_subscribers

    
    """
    params = [('owner_screen_name', 'owner_screen_name_example'),
                    ('owner_id', 'owner_id_example'),
                    ('cursor', 'cursor_example'),
                    ('include_entities', 'include_entities_example'),
                    ('skip_status', 'skip_status_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/lists/subscribers.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_subscribers_create(client):
    """Test case for lists_subscribers_create

    
    """
    params = [('owner_screen_name', 'owner_screen_name_example'),
                    ('owner_id', 'owner_id_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/lists/subscribers/create.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_subscribers_destroy(client):
    """Test case for lists_subscribers_destroy

    
    """
    params = [('owner_screen_name', 'owner_screen_name_example'),
                    ('owner_id', 'owner_id_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/lists/subscribers/destroy.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_subscribers_show(client):
    """Test case for lists_subscribers_show

    
    """
    params = [('owner_screen_name', 'owner_screen_name_example'),
                    ('owner_id', 'owner_id_example'),
                    ('include_entities', 'include_entities_example'),
                    ('skip_status', 'skip_status_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/lists/subscribers/show.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_subscriptions(client):
    """Test case for lists_subscriptions

    
    """
    params = [('count', 'count_example'),
                    ('cursor', 'cursor_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/lists/subscriptions.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_update(client):
    """Test case for lists_update

    
    """
    params = [('owner_screen_name', 'owner_screen_name_example'),
                    ('owner_id', 'owner_id_example'),
                    ('name', 'name_example'),
                    ('mode', 'mode_example'),
                    ('description', 'description_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/lists/update.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_saved_searches_create(client):
    """Test case for saved_searches_create

    
    """
    params = [('query', 'query_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/saved_searches/create.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_saved_searches_destroy(client):
    """Test case for saved_searches_destroy

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/saved_searches/destroy/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_saved_searches_list(client):
    """Test case for saved_searches_list

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/saved_searches/list.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_savedsearchesid(client):
    """Test case for savedsearchesid

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/saved_searches/show/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_tweets(client):
    """Test case for search_tweets

    
    """
    params = [('q', 'q_example'),
                    ('geocode', 'geocode_example'),
                    ('lang', 'lang_example'),
                    ('locale', 'locale_example'),
                    ('result_type', 'result_type_example'),
                    ('count', 'count_example'),
                    ('until', 'until_example'),
                    ('since_id', 'since_id_example'),
                    ('max_id', 'max_id_example'),
                    ('include_entities', 'include_entities_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/search/tweets.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_statuses_destroy(client):
    """Test case for statuses_destroy

    
    """
    params = [('trim_user', 'trim_user_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/statuses/destroy/{id_jso}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_statuses_home_timeline(client):
    """Test case for statuses_home_timeline

    
    """
    params = [('count', 56),
                    ('max_id', 56),
                    ('since_id', 56),
                    ('trim_user', 'trim_user_example'),
                    ('exclude_replies', 'exclude_replies_example'),
                    ('contributor_details', 'contributor_details_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/statuses/home_timeline.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_statuses_mentions_timeline(client):
    """Test case for statuses_mentions_timeline

    
    """
    params = [('count', 56),
                    ('since_id', 56),
                    ('max_id', 56),
                    ('trim_user', 'trim_user_example'),
                    ('contributor_details', 'contributor_details_example'),
                    ('include_entities', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/statuses/mentions_timeline.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_statuses_oembed(client):
    """Test case for statuses_oembed

    
    """
    params = [('maxwidth', 56),
                    ('hide_media', 'hide_media_example'),
                    ('hide_thread', 'hide_thread_example'),
                    ('omit_script', 'omit_script_example'),
                    ('align', 'align_example'),
                    ('related', 'related_example'),
                    ('lang', 'lang_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/statuses/oembed.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_statuses_retweets(client):
    """Test case for statuses_retweets

    
    """
    params = [('count', 'count_example'),
                    ('trim_user', 'trim_user_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/statuses/retweets/{id_jso}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_statuses_show(client):
    """Test case for statuses_show

    
    """
    params = [('trim_user', 'trim_user_example'),
                    ('include_my_retweet', 'include_my_retweet_example'),
                    ('include_entities', 'include_entities_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/statuses/show/{id_jso}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_statuses_update(client):
    """Test case for statuses_update

    
    """
    params = [('status', 'Posting from @apigee's API test console. It's like a command line for the Twitter API! #apitools'),
                    ('in_reply_to_status_id', 'in_reply_to_status_id_example'),
                    ('lat', '37.426363'),
                    ('long', '-122.141114'),
                    ('place_id', 'place_id_example'),
                    ('display_coordinates', false),
                    ('trim_user', 'trim_user_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/statuses/update.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_statuses_update_with_media(client):
    """Test case for statuses_update_with_media

    
    """
    params = [('status', 'status_example'),
                    ('media', 'media_example'),
                    ('possibly_sensitive', 'possibly_sensitive_example'),
                    ('in_reply_to_status_id', 'in_reply_to_status_id_example'),
                    ('lat', 'lat_example'),
                    ('long', 'long_example'),
                    ('place_id', 'place_id_example'),
                    ('display_coordinates', 'display_coordinates_example')]
    headers = { 
        'content_type': 'multipart/form-data',
    }
    response = await client.request(
        method='POST',
        path='/1.1/statuses/update_with_media.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_statuses_user_timeline(client):
    """Test case for statuses_user_timeline

    
    """
    params = [('count', 56),
                    ('since_id', 56),
                    ('max_id', 56),
                    ('trim_user', 'trim_user_example'),
                    ('exclude_replies', True),
                    ('contributor_details', True),
                    ('include_rts', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/statuses/user_timeline.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_statusesretweetid(client):
    """Test case for statusesretweetid

    
    """
    params = [('trim_user', 'trim_user_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/statuses/retweet/{id_jso}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trends_available(client):
    """Test case for trends_available

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/trends/available.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trends_closest(client):
    """Test case for trends_closest

    
    """
    params = [('lat', 'lat_example'),
                    ('long', 'long_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/trends/closest.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trends_place(client):
    """Test case for trends_place

    
    """
    params = [('id', 'id_example'),
                    ('exclude', 'exclude_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/trends/place.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_contributees(client):
    """Test case for users_contributees

    
    """
    params = [('include_entities', 'include_entities_example'),
                    ('skip_status', 'skip_status_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/users/contributees.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_contributors(client):
    """Test case for users_contributors

    
    """
    params = [('include_entities', 'include_entities_example'),
                    ('skip_status', 'skip_status_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/users/contributors.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_lookup(client):
    """Test case for users_lookup

    
    """
    params = [('screen_name', 'screen_name_example'),
                    ('user_id', 'user_id_example'),
                    ('include_entities', 'include_entities_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/users/lookup.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_report_spam(client):
    """Test case for users_report_spam

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/1.1/users/report_spam.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_search(client):
    """Test case for users_search

    
    """
    params = [('q', 'q_example'),
                    ('page', 'page_example'),
                    ('count', 'count_example'),
                    ('include_entities', 'include_entities_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/users/search.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_show(client):
    """Test case for users_show

    
    """
    params = [('screen_name', 'screen_name_example'),
                    ('user_id', 'user_id_example'),
                    ('include_entities', 'include_entities_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/users/show.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_suggestions(client):
    """Test case for users_suggestions

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/users/suggestions.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_suggestions_slug(client):
    """Test case for users_suggestions_slug

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/users/suggestions/{slug_jso}'.format(slug='slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_suggestionsslugmembers(client):
    """Test case for users_suggestionsslugmembers

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1.1/users/suggestions/{slug}/members.json'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

