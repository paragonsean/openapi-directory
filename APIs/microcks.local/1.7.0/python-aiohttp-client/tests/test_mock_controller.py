# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.counter import Counter
from openapi_server.models.get_service200_response import GetService200Response
from openapi_server.models.metadata import Metadata
from openapi_server.models.operation_override_dto import OperationOverrideDTO
from openapi_server.models.service import Service


pytestmark = pytest.mark.asyncio

async def test_delete_service(client):
    """Test case for delete_service

    Delete Service
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/services/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_snapshot(client):
    """Test case for export_snapshot

    Export a snapshot
    """
    params = [('serviceIds', ['service_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/export',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service(client):
    """Test case for get_service

    Get Service
    """
    params = [('messages', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/services/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_services(client):
    """Test case for get_services

    Get Services and APIs
    """
    params = [('page', 56),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/services',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_services_counter(client):
    """Test case for get_services_counter

    Get the Services counter
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/services/count',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_services_labels(client):
    """Test case for get_services_labels

    Get the already used labels for Services
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/services/labels',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_import_snapshot(client):
    """Test case for import_snapshot

    Import a snapshot
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/import',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_override_service_operation(client):
    """Test case for override_service_operation

    Override Service Operation
    """
    body = {"parameterConstraints":[{"in":"path","mustMatchRegexp":"mustMatchRegexp","name":"name","recopy":True,"required":True},{"in":"path","mustMatchRegexp":"mustMatchRegexp","name":"name","recopy":True,"required":True}],"defaultDelay":0,"dispatcherRules":"dispatcherRules","dispatcher":"dispatcher"}
    params = [('operationName', 'operation_name_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/services/{id}/operation'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_services(client):
    """Test case for search_services

    Search for Services and APIs
    """
    params = [('queryMap', {'key': 'query_map_example'})]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/services/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_service_metadata(client):
    """Test case for update_service_metadata

    Update Service Metadata
    """
    body = {"lastUpdate":6,"annotations":{"key":"annotations"},"createdOn":0,"labels":{"key":"labels"}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/services/{id}/metadata'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

