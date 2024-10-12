# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.media_item_wrapped import MediaItemWrapped
from openapi_server.models.tag_language_marshaller_wrapped import TagLanguageMarshallerWrapped
from openapi_server.models.tag_marshaller_wrapped import TagMarshallerWrapped
from openapi_server.models.tag_type_marshaller_wrapped import TagTypeMarshallerWrapped


pytestmark = pytest.mark.asyncio

async def test_resources_tags_format_get(client):
    """Test case for resources_tags_format_get

    Get Tags
    """
    params = [('sort', 'sort_example'),
                    ('max', 56),
                    ('offset', 56),
                    ('name', 'name_example'),
                    ('nameContains', 'name_contains_example'),
                    ('mediaId', 56),
                    ('typeId', 56),
                    ('typeName', 'type_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/tags.{format}'.format(format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_tags_id_format_get(client):
    """Test case for resources_tags_id_format_get

    Get Tag by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/tags/{id_format}'.format(id=56, format='format_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_tags_id_media_format_get(client):
    """Test case for resources_tags_id_media_format_get

    Get MediaItems for Tag
    """
    params = [('sort', 'sort_example'),
                    ('max', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/tags/{id}/media.{format}'.format(id=56, format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_tags_id_related_format_get(client):
    """Test case for resources_tags_id_related_format_get

    Get related Tags by ID
    """
    params = [('sort', 'sort_example'),
                    ('max', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/tags/{id}/related.{format}'.format(id=56, format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_tags_id_syndicate_format_get(client):
    """Test case for resources_tags_id_syndicate_format_get

    Get MediaItems for Tag
    """
    params = [('displayMethod', 'display_method_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/tags/{id}/syndicate.{format}'.format(id=56, format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_tags_tag_languages_format_get(client):
    """Test case for resources_tags_tag_languages_format_get

    Get TagLanguages
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/tags/tagLanguages.{format}'.format(format='format_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_tags_tag_types_format_get(client):
    """Test case for resources_tags_tag_types_format_get

    Get MediaItems for Tag
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/tags/tagTypes.{format}'.format(format='format_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

