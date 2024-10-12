# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.nitro import Nitro


pytestmark = pytest.mark.asyncio

async def test_list_availability(client):
    """Test case for list_availability

    Discover details of on-demand availability for programmes and their versions
    """
    params = [('sort', 'sort_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('availability', ['availability_example']),
                    ('descendants_of', ['descendants_of_example']),
                    ('media_set', ['media_set_example']),
                    ('page', 1),
                    ('page_size', 10),
                    ('territory', ['territory_example']),
                    ('debug', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/availabilities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_broadcasts(client):
    """Test case for list_broadcasts

    Build schedules and find metadata for TV and radio broadcasts
    """
    params = [('sort', 'sort_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('mixin', ['mixin_example']),
                    ('authority', ['authority_example']),
                    ('descendants_of', ['descendants_of_example']),
                    ('end_from', '2013-10-20T19:20:30+01:00'),
                    ('end_to', '2013-10-20T19:20:30+01:00'),
                    ('format', ['format_example']),
                    ('genre', ['genre_example']),
                    ('id', ['id_example']),
                    ('item', ['item_example']),
                    ('page', 1),
                    ('page_size', 10),
                    ('people', 'people_example'),
                    ('pid', ['pid_example']),
                    ('q', 'q_example'),
                    ('schedule_day', '2013-10-20'),
                    ('schedule_day_from', '2013-10-20'),
                    ('schedule_day_to', '2013-10-20'),
                    ('service_master_brand', ['service_master_brand_example']),
                    ('sid', ['sid_example']),
                    ('start_from', '2013-10-20T19:20:30+01:00'),
                    ('start_to', '2013-10-20T19:20:30+01:00'),
                    ('version', ['version_example'])]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/broadcasts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_groups(client):
    """Test case for list_groups

    Find metadata for curated groups: seasons, collections, galleries or franchises
    """
    params = [('sort', 'sort_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('mixin', ['mixin_example']),
                    ('for_descendants_of', 'for_descendants_of_example'),
                    ('for_programme', 'for_programme_example'),
                    ('group', 'group_example'),
                    ('group_type', ['group_type_example']),
                    ('member', 'member_example'),
                    ('page', 1),
                    ('page_size', 10),
                    ('partner_id', ['partner_id_example']),
                    ('partner_pid', ['partner_pid_example']),
                    ('pid', ['pid_example']),
                    ('q', 'q_example'),
                    ('embargoed', 'embargoed_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_images(client):
    """Test case for list_images

    Find metadata for images
    """
    params = [('sort', 'sort_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('group', 'group_example'),
                    ('image_type', ['image_type_example']),
                    ('is_alternate_image_for', 'is_alternate_image_for_example'),
                    ('is_image_for', 'is_image_for_example'),
                    ('page', 1),
                    ('page_size', 10),
                    ('partner_id', ['partner_id_example']),
                    ('partner_pid', ['partner_pid_example']),
                    ('pid', ['pid_example']),
                    ('q', 'q_example'),
                    ('embargoed', 'embargoed_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/images',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_items(client):
    """Test case for list_items

    Look inside programmes to find segments: chapters, tracks and more
    """
    params = [('sort', 'sort_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('mixin', ['mixin_example']),
                    ('authority', 'authority_example'),
                    ('id', ['id_example']),
                    ('id_type', 'id_type_example'),
                    ('item_type', ['item_type_example']),
                    ('page', 1),
                    ('page_size', 10),
                    ('partner_id', ['partner_id_example']),
                    ('partner_pid', ['partner_pid_example']),
                    ('people', 'people_example'),
                    ('pid', ['pid_example']),
                    ('programme', 'programme_example'),
                    ('q', 'q_example'),
                    ('segment_event', 'segment_event_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/items',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_masterbrands(client):
    """Test case for list_masterbrands

    List all Master Brands
    """
    params = [('sort', 'sort_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('mixin', ['mixin_example']),
                    ('mid', ['mid_example']),
                    ('page', 1),
                    ('page_size', 10),
                    ('partner_id', ['partner_id_example']),
                    ('partner_pid', ['partner_pid_example']),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/master_brands',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_people(client):
    """Test case for list_people

    Find the people behind and in programmes: cast, crew, guests and more
    """
    params = [('authority', 'authority_example'),
                    ('has_external_id', ['has_external_id_example']),
                    ('id', ['id_example']),
                    ('id_type', 'id_type_example'),
                    ('page', 1),
                    ('page_size', 10),
                    ('partner_id', ['partner_id_example']),
                    ('partner_pid', ['partner_pid_example']),
                    ('pid', ['pid_example']),
                    ('programme', 'programme_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/people',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_pips(client):
    """Test case for list_pips

    Look inside pips entities
    """
    params = [('page', 1),
                    ('page_size', 10),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pips',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_programme_details(client):
    """Test case for list_programme_details

    Exposes programme information for a single pid
    """
    params = [('page', 1),
                    ('page_size', 10),
                    ('partner_pid', 'partner_pid_example'),
                    ('pid', 'pid_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/programme_details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_programmes(client):
    """Test case for list_programmes

    Start here for programmes metadata: Brands, Series, Episodes and Clips
    """
    params = [('sort', 'sort_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('mixin', ['mixin_example']),
                    ('audio_described', ['audio_described_example']),
                    ('availability', ['availability_example']),
                    ('availability_entity_type', ['availability_entity_type_example']),
                    ('availability_from', '2013-10-20T19:20:30+01:00'),
                    ('availability_type', ['availability_type_example']),
                    ('children_of', ['children_of_example']),
                    ('descendants_of', ['descendants_of_example']),
                    ('duration', ['duration_example']),
                    ('entity_type', ['entity_type_example']),
                    ('format', ['format_example']),
                    ('genre', ['genre_example']),
                    ('group', 'group_example'),
                    ('initial_letter', 'initial_letter_example'),
                    ('initial_letter_end', 'initial_letter_end_example'),
                    ('initial_letter_start', 'initial_letter_start_example'),
                    ('initial_letter_strict', ['initial_letter_strict_example']),
                    ('item', ['item_example']),
                    ('master_brand', ['master_brand_example']),
                    ('media_set', 'media_set_example'),
                    ('media_type', ['media_type_example']),
                    ('page', 1),
                    ('page_size', 10),
                    ('partner_id', ['partner_id_example']),
                    ('partner_pid', ['partner_pid_example']),
                    ('payment_type', ['payment_type_example']),
                    ('people', 'people_example'),
                    ('pid', ['pid_example']),
                    ('promoted_for', 'promoted_for_example'),
                    ('q', 'q_example'),
                    ('signed', ['signed_example']),
                    ('tag_name', 'tag_name_example'),
                    ('tag_scheme', 'tag_scheme_example'),
                    ('tleo', ['tleo_example']),
                    ('version', ['version_example']),
                    ('embargoed', 'embargoed_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/programmes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_promotions(client):
    """Test case for list_promotions

    Discover metadata for content promotions
    """
    params = [('mixin', ['mixin_example']),
                    ('context', 'context_example'),
                    ('page', 1),
                    ('page_size', 10),
                    ('partner_id', ['partner_id_example']),
                    ('partner_pid', ['partner_pid_example']),
                    ('pid', ['pid_example']),
                    ('promoted_by', ['promoted_by_example']),
                    ('promoted_for', ['promoted_for_example']),
                    ('q', 'q_example'),
                    ('status', ['status_example'])]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/promotions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_schedules(client):
    """Test case for list_schedules

    Build schedules and find metadata for TV and radio broadcasts and webcasts
    """
    params = [('sort', 'sort_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('mixin', ['mixin_example']),
                    ('authority', ['authority_example']),
                    ('descendants_of', ['descendants_of_example']),
                    ('end_from', '2013-10-20T19:20:30+01:00'),
                    ('end_to', '2013-10-20T19:20:30+01:00'),
                    ('format', ['format_example']),
                    ('genre', ['genre_example']),
                    ('group', 'group_example'),
                    ('id', ['id_example']),
                    ('id_type', ['id_type_example']),
                    ('item', ['item_example']),
                    ('page', 1),
                    ('page_size', 10),
                    ('partner_id', ['partner_id_example']),
                    ('partner_pid', ['partner_pid_example']),
                    ('people', 'people_example'),
                    ('pid', ['pid_example']),
                    ('q', 'q_example'),
                    ('repeat', True),
                    ('schedule_day', '2013-10-20'),
                    ('schedule_day_from', '2013-10-20'),
                    ('schedule_day_to', '2013-10-20'),
                    ('service_master_brand', ['service_master_brand_example']),
                    ('sid', ['sid_example']),
                    ('start_from', '2013-10-20T19:20:30+01:00'),
                    ('start_to', '2013-10-20T19:20:30+01:00'),
                    ('version', ['version_example'])]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/schedules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_services(client):
    """Test case for list_services

    Information about the linear services used for broadcast transmissions
    """
    params = [('end_from', '2013-10-20T19:20:30+01:00'),
                    ('end_to', '2013-10-20T19:20:30+01:00'),
                    ('mid', ['mid_example']),
                    ('page', 1),
                    ('page_size', 10),
                    ('partner_id', ['partner_id_example']),
                    ('partner_pid', ['partner_pid_example']),
                    ('q', 'q_example'),
                    ('service_type', ['service_type_example']),
                    ('sid', ['sid_example']),
                    ('start_from', '2013-10-20T19:20:30+01:00'),
                    ('start_to', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/services',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_versions(client):
    """Test case for list_versions

    Metadata on editorial programme versions: original, signed, audio-described, etc
    """
    params = [('availability', ['availability_example']),
                    ('descendants_of', ['descendants_of_example']),
                    ('media_set', ['media_set_example']),
                    ('page', 1),
                    ('page_size', 10),
                    ('partner_id', ['partner_id_example']),
                    ('partner_pid', ['partner_pid_example']),
                    ('payment_type', ['payment_type_example']),
                    ('pid', ['pid_example']),
                    ('embargoed', 'embargoed_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/versions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

