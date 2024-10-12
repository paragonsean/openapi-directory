# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.document import Document
from openapi_server.models.organization import Organization
from openapi_server.models.paginated_response_of_document import PaginatedResponseOfDocument
from openapi_server.models.paginated_response_of_history_item import PaginatedResponseOfHistoryItem
from openapi_server.models.route import Route
from openapi_server.models.who_is_response import WhoIsResponse


pytestmark = pytest.mark.asyncio

async def test_get_public_document(client):
    """Test case for get_public_document

    Retrieve a public document (meta-data only, no content)
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/public/documents/{id4n}/{organization_id}/{file_name}/metadata'.format(organization_id='organization_id_example', id4n='id4n_example', file_name='file_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_routes(client):
    """Test case for get_routes

    Retrieve all public routes for a GUID
    """
    params = [('type', 'web'),
                    ('interpolate', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/public/routes/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_go(client):
    """Test case for go

    Forward
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/go/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_public_documents(client):
    """Test case for list_all_public_documents

    List public documents
    """
    params = [('organizationId', 'organization_id_example'),
                    ('owner', 'owner_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/public/documents/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_public_history(client):
    """Test case for list_public_history

    Shows the public history of the given GUID
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/public/history/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_organization_info(client):
    """Test case for read_organization_info

    Read public organization information
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/public/organizations/{organization_id}'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_public_document(client):
    """Test case for read_public_document

    Read public document contents
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/public/documents/{id4n}/{organization_id}/{file_name}'.format(organization_id='organization_id_example', id4n='id4n_example', file_name='file_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resolve_image_using_get_0(client):
    """Test case for resolve_image_using_get_0

    Resolve image
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/public/image/{image_id}'.format(image_id='image_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resolve_who_is_entry(client):
    """Test case for resolve_who_is_entry

    Resolve owner of id4n
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/whois/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

