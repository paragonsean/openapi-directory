# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_action_organization_activity_list_get(client):
    """Test case for action_organization_activity_list_get

    Get the activity stream of an organization
    """
    params = [('id', 'ministry-of-agriculture')]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/organization_activity_list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_organization_activity_list_html_get(client):
    """Test case for action_organization_activity_list_html_get

    Get the activity stream of an organization, HTML format
    """
    params = [('id', 'ministry-of-agriculture')]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/organization_activity_list_html',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_organization_autocomplete_get(client):
    """Test case for action_organization_autocomplete_get

    Get names of organizations that match a query string
    """
    params = [('q', 'ministry'),
                    ('limit', 20)]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/organization_autocomplete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_organization_follower_count_get(client):
    """Test case for action_organization_follower_count_get

    Get number of followers of an organization
    """
    params = [('id', 'ministry-of-agriculture')]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/organization_follower_count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_organization_follower_list_get(client):
    """Test case for action_organization_follower_list_get

    Get users following an organization
    """
    params = [('id', 'ministry-of-agriculture')]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/organization_follower_list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_organization_list_for_user_get(client):
    """Test case for action_organization_list_for_user_get

    Get organizations that a user has a given permission for
    """
    params = [('permission', '"edit_group"')]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/organization_list_for_user',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_organization_list_get(client):
    """Test case for action_organization_list_get

    Get names of all organizations
    """
    params = [('offset', 0),
                    ('limit', 100)]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/organization_list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_organization_revision_list_get(client):
    """Test case for action_organization_revision_list_get

    Get organization revisions
    """
    params = [('id', 'ministry-of-agriculture')]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/organization_revision_list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_organization_show_get(client):
    """Test case for action_organization_show_get

    Get details of a specific organization
    """
    params = [('id', 'ministry-of-agriculture'),
                    ('include_datasets', True)]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/organization_show',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_package_activity_list_get(client):
    """Test case for action_package_activity_list_get

    Get the activity stream of a package (dataset)
    """
    params = [('id', 'grizzly-bear-population-units'),
                    ('offset', 0),
                    ('limit', 31)]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/package_activity_list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_package_activity_list_html_get(client):
    """Test case for action_package_activity_list_html_get

    Get the activity stream of a package (dataset), HTML format
    """
    params = [('id', 'grizzly-bear-population-units'),
                    ('offset', 0),
                    ('limit', 31)]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/package_activity_list_html',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_package_autocomplete_get(client):
    """Test case for action_package_autocomplete_get

    Find packages (datasets) matching a query
    """
    params = [('q', '"Okanagan Lake"'),
                    ('limit', 10)]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/package_autocomplete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_package_list_get(client):
    """Test case for action_package_list_get

    Get a list of all packages (datasets)
    """
    params = [('offset', 0),
                    ('limit', 100)]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/package_list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_package_relationships_list_get(client):
    """Test case for action_package_relationships_list_get

    Get package (dataset) relationships
    """
    params = [('id', 'grizzly-bear-population-units'),
                    ('id2', 'important-fossil-areas'),
                    ('rel', 'rel_example')]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/package_relationships_list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_package_revision_list_get(client):
    """Test case for action_package_revision_list_get

    Get list of revisions for a package (dataset)
    """
    params = [('id', 'grizzly-bear-population-units')]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/package_revision_list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_package_search_get(client):
    """Test case for action_package_search_get

    Find packages (datasets) matching query terms
    """
    params = [('q', '"Okanagan Lake"')]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/package_search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_package_show_get(client):
    """Test case for action_package_show_get

    Get metadata about one specific package (dataset)
    """
    params = [('id', 'grizzly-bear-population-units')]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/package_show',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_related_list_get(client):
    """Test case for action_related_list_get

    Gets items related to a package (dataset)
    """
    params = [('id', 'id_example'),
                    ('dataset', 'dataset_example'),
                    ('type_filter', 'type_filter_example'),
                    ('sort', 'sort_example'),
                    ('featured', 'featured_example')]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/related_list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_resource_search_get(client):
    """Test case for action_resource_search_get

    Find resources
    """
    params = [('query', 'format:csv'),
                    ('fields', 'fields_example'),
                    ('order_by', 'order_by_example'),
                    ('offset', 0),
                    ('limit', 0)]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/resource_search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_resource_show_get(client):
    """Test case for action_resource_show_get

    Get metadata for a specific resource
    """
    params = [('id', 'e6c8bb1d-3726-418b-9b7e-1d97a9bbb817'),
                    ('include_tracking', False)]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/resource_show',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_status_show_get(client):
    """Test case for action_status_show_get

    Get the site status
    """
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/status_show',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_tag_list_get(client):
    """Test case for action_tag_list_get

    Get a list of tags
    """
    params = [('offset', 0),
                    ('limit', 100)]
    headers = { 
        'internalApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/3/action/tag_list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

