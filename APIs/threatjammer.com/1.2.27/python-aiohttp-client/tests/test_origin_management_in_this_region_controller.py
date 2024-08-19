# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.body_query_origin_status_v1_origin_status_post import BodyQueryOriginStatusV1OriginStatusPost
from openapi_server.models.body_update_configuration_origin_v1_origin_put import BodyUpdateConfigurationOriginV1OriginPut
from openapi_server.models.body_update_origin_status_v1_origin_status_put import BodyUpdateOriginStatusV1OriginStatusPut
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.origin_address_status_collection_output import OriginAddressStatusCollectionOutput
from openapi_server.models.origin_client_analysis_collection_output import OriginClientAnalysisCollectionOutput
from openapi_server.models.origin_collection_output import OriginCollectionOutput
from openapi_server.models.origin_cookie_id_status_collection_output import OriginCookieIdStatusCollectionOutput
from openapi_server.models.origin_output import OriginOutput
from openapi_server.models.origin_scripts_output import OriginScriptsOutput
from openapi_server.models.origin_status_details_collection_output import OriginStatusDetailsCollectionOutput
from openapi_server.models.origin_status_details_output import OriginStatusDetailsOutput
from openapi_server.models.origin_status_output import OriginStatusOutput
from openapi_server.models.origin_traffic_analysis_collection_output import OriginTrafficAnalysisCollectionOutput


pytestmark = pytest.mark.asyncio

async def test_query_all_origin_information_v1_origin_all_get(client):
    """Test case for query_all_origin_information_v1_origin_all_get

    Get the information of the origins of the user in the region.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/origin/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_origin_address_status_information_v1_origin_addresses_get(client):
    """Test case for query_origin_address_status_information_v1_origin_addresses_get

    Get the address status of the origin of the user in the region.
    """
    params = [('query', 'query_example'),
                    ('page', 1),
                    ('page_size', 20)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/origin/addresses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_origin_cookie_id_status_information_v1_origin_cookies_get(client):
    """Test case for query_origin_cookie_id_status_information_v1_origin_cookies_get

    Get the tracking cookie ID status of the origin of the user in the region.
    """
    params = [('query', 'query_example'),
                    ('page', 1),
                    ('page_size', 20)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/origin/cookies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_origin_information_v1_origin_get(client):
    """Test case for query_origin_information_v1_origin_get

    Get the information of an origin of the user in the region.
    """
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/origin',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_origin_scripts_v1_origin_scripts_get(client):
    """Test case for query_origin_scripts_v1_origin_scripts_get

    Get the code snippets of an origin of the user in the region.
    """
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/origin/scripts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_origin_status_detail_v1_origin_status_detail_status_id_get(client):
    """Test case for query_origin_status_detail_v1_origin_status_detail_status_id_get

    Get detail of a status available in the platform.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/origin/status/detail/{status_id}'.format(status_id='status_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_origin_status_details_v1_origin_status_details_get(client):
    """Test case for query_origin_status_details_v1_origin_status_details_get

    Get the list of different status available in the platform.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/origin/status/details',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_origin_status_v1_origin_status_post(client):
    """Test case for query_origin_status_v1_origin_status_post

    Get the current cookie ID and IP address status of the origin of user in the region.
    """
    body = openapi_server.BodyQueryOriginStatusV1OriginStatusPost()
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/origin/status',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_origin_traffic_analysis_v1_origin_traffic_analysis_get(client):
    """Test case for query_origin_traffic_analysis_v1_origin_traffic_analysis_get

    Get the traffic analysis of the origin.
    """
    params = [('query', 'query_example'),
                    ('interval', 'interval_example'),
                    ('from_timestamp', 56),
                    ('to_timestamp', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/origin/traffic/analysis',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_origin_traffic_client_v1_origin_client_analysis_get(client):
    """Test case for query_origin_traffic_client_v1_origin_client_analysis_get

    Get the type of clients of the trafffic of the origin.
    """
    params = [('query', 'query_example'),
                    ('interval', 'interval_example'),
                    ('from_timestamp', 56),
                    ('to_timestamp', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/origin/client/analysis',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_configuration_origin_v1_origin_put(client):
    """Test case for update_configuration_origin_v1_origin_put

    Update the configuration of an origin of the user in the region.
    """
    body = openapi_server.BodyUpdateConfigurationOriginV1OriginPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/origin',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_origin_status_v1_origin_status_put(client):
    """Test case for update_origin_status_v1_origin_status_put

    Update the status of a given origin event in the platform.
    """
    body = openapi_server.BodyUpdateOriginStatusV1OriginStatusPut()
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/origin/status',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

