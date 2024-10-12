# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response200_o_kish import ErrorResponse200OKish
from openapi_server.models.error_response400_bad_admin_or_value import ErrorResponse400BadAdminOrValue
from openapi_server.models.error_response401_bad_key_for_basic_auth import ErrorResponse401BadKeyForBasicAuth
from openapi_server.models.error_response404_not_found import ErrorResponse404NotFound
from openapi_server.models.float_value_object import FloatValueObject
from openapi_server.models.int32_value_object import Int32ValueObject
from openapi_server.models.int64_string_value_object import Int64StringValueObject
from openapi_server.models.int64_value_object import Int64ValueObject
from openapi_server.models.string_value_object import StringValueObject
from openapi_server.models.table_def import TableDef


pytestmark = pytest.mark.asyncio

async def test_read_float_table_0(client):
    """Test case for read_float_table_0

    
    """
    params = [('startIndex', 56),
                    ('numElements', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/tables/floats/{table_name}'.format(table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_float_table_element_0(client):
    """Test case for read_float_table_element_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/tables/floats/{table_name}/{index}'.format(table_name='table_name_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_float_tables_0(client):
    """Test case for read_float_tables_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/tables/floats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_int32_table_0(client):
    """Test case for read_int32_table_0

    
    """
    params = [('startIndex', 56),
                    ('numElements', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/tables/int32s/{table_name}'.format(table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_int32_table_element_0(client):
    """Test case for read_int32_table_element_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/tables/int32s/{table_name}/{index}'.format(table_name='table_name_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_int32_tables_0(client):
    """Test case for read_int32_tables_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/tables/int32s',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_int64_table_0(client):
    """Test case for read_int64_table_0

    
    """
    params = [('startIndex', 56),
                    ('numElements', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/tables/int64s/{table_name}'.format(table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_int64_table_as_string_0(client):
    """Test case for read_int64_table_as_string_0

    
    """
    params = [('startIndex', 56),
                    ('numElements', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/tables/int64s/{table_name}/_string'.format(table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_int64_table_element_0(client):
    """Test case for read_int64_table_element_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/tables/int64s/{table_name}/{index}'.format(table_name='table_name_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_int64_table_element_as_string_0(client):
    """Test case for read_int64_table_element_as_string_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/tables/int64s/{table_name}/{index}/_string'.format(table_name='table_name_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_int64_tables_0(client):
    """Test case for read_int64_tables_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/tables/int64s',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_string_table_0(client):
    """Test case for read_string_table_0

    
    """
    params = [('startIndex', 56),
                    ('numElements', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/tables/strings/{table_name}'.format(table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_string_table_element_0(client):
    """Test case for read_string_table_element_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/tables/strings/{table_name}/{index}'.format(table_name='table_name_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_string_tables_0(client):
    """Test case for read_string_tables_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/tables/strings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_float_table_0(client):
    """Test case for write_float_table_0

    
    """
    float_array = [3.4]
    params = [('startIndex', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/tables/floats/{table_name}'.format(table_name='table_name_example'),
        headers=headers,
        json=float_array,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_float_table_element_0(client):
    """Test case for write_float_table_element_0

    
    """
    float_element_object = {"value":0.8008282}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/tables/floats/{table_name}/{index}'.format(table_name='table_name_example', index=56),
        headers=headers,
        json=float_element_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_int32_table_0(client):
    """Test case for write_int32_table_0

    
    """
    int32_array = [56]
    params = [('startIndex', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/tables/int32s/{table_name}'.format(table_name='table_name_example'),
        headers=headers,
        json=int32_array,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_int32_table_element_0(client):
    """Test case for write_int32_table_element_0

    
    """
    int32_element_object = {"value":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/tables/int32s/{table_name}/{index}'.format(table_name='table_name_example', index=56),
        headers=headers,
        json=int32_element_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_int64_table_0(client):
    """Test case for write_int64_table_0

    
    """
    int64_array = [56]
    params = [('startIndex', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/tables/int64s/{table_name}'.format(table_name='table_name_example'),
        headers=headers,
        json=int64_array,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_int64_table_as_string_0(client):
    """Test case for write_int64_table_as_string_0

    
    """
    int64_as_string_array = ['int64_as_string_array_example']
    params = [('startIndex', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/tables/int64s/{table_name}/_string'.format(table_name='table_name_example'),
        headers=headers,
        json=int64_as_string_array,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_int64_table_element_0(client):
    """Test case for write_int64_table_element_0

    
    """
    int64_element_object = {"value":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/tables/int64s/{table_name}/{index}'.format(table_name='table_name_example', index=56),
        headers=headers,
        json=int64_element_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_int64_table_element_as_string_0(client):
    """Test case for write_int64_table_element_as_string_0

    
    """
    int64_element_object = {"value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/tables/int64s/{table_name}/{index}/_string'.format(table_name='table_name_example', index=56),
        headers=headers,
        json=int64_element_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_string_table_0(client):
    """Test case for write_string_table_0

    
    """
    string_array = ['string_array_example']
    params = [('startIndex', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/tables/strings/{table_name}'.format(table_name='table_name_example'),
        headers=headers,
        json=string_array,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_string_table_element_0(client):
    """Test case for write_string_table_element_0

    
    """
    string_element_object = {"value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/tables/strings/{table_name}/{index}'.format(table_name='table_name_example', index=56),
        headers=headers,
        json=string_element_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

