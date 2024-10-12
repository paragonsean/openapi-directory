# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.failed_property_batch_info import FailedPropertyBatchInfo
from openapi_server.models.name_description import NameDescription
from openapi_server.models.paged_property_info_list import PagedPropertyInfoList
from openapi_server.models.paged_sub_name_info_list import PagedSubNameInfoList
from openapi_server.models.property_batch_description_list import PropertyBatchDescriptionList
from openapi_server.models.property_description import PropertyDescription
from openapi_server.models.property_info import PropertyInfo
from openapi_server.models.successful_property_batch_info import SuccessfulPropertyBatchInfo


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_name(client):
    """Test case for create_name

    Creates a Service Fabric name.
    """
    name_description = openapi_server.NameDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Names/$/Create',
        headers=headers,
        json=name_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_name(client):
    """Test case for delete_name

    Deletes a Service Fabric name.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/Names/{name_id}'.format(name_id='name_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_property(client):
    """Test case for delete_property

    Deletes the specified Service Fabric property.
    """
    params = [('api-version', 6.0),
                    ('PropertyName', 'property_name_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/Names/{name_id}/$/GetProperty'.format(name_id='name_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_name_exists_info(client):
    """Test case for get_name_exists_info

    Returns whether the Service Fabric name exists.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Names/{name_id}'.format(name_id='name_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_property_info(client):
    """Test case for get_property_info

    Gets the specified Service Fabric property.
    """
    params = [('api-version', 6.0),
                    ('PropertyName', 'property_name_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Names/{name_id}/$/GetProperty'.format(name_id='name_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_property_info_list(client):
    """Test case for get_property_info_list

    Gets information on all Service Fabric properties under a given name.
    """
    params = [('api-version', 6.0),
                    ('IncludeValues', False),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Names/{name_id}/$/GetProperties'.format(name_id='name_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sub_name_info_list(client):
    """Test case for get_sub_name_info_list

    Enumerates all the Service Fabric names under a given name.
    """
    params = [('api-version', 6.0),
                    ('Recursive', False),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Names/{name_id}/$/GetSubNames'.format(name_id='name_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_put_property(client):
    """Test case for put_property

    Creates or updates a Service Fabric property.
    """
    property_description = openapi_server.PropertyDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/Names/{name_id}/$/GetProperty'.format(name_id='name_id_example'),
        headers=headers,
        json=property_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_submit_property_batch(client):
    """Test case for submit_property_batch

    Submits a property batch.
    """
    property_batch_description_list = openapi_server.PropertyBatchDescriptionList()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Names/{name_id}/$/GetProperties/$/SubmitBatch'.format(name_id='name_id_example'),
        headers=headers,
        json=property_batch_description_list,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

