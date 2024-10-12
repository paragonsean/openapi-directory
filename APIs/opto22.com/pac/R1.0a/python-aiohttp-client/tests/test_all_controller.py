# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.controller_response import ControllerResponse
from openapi_server.models.digital_point_state_object import DigitalPointStateObject
from openapi_server.models.digital_point_state_var import DigitalPointStateVar
from openapi_server.models.error_response200_o_kish import ErrorResponse200OKish
from openapi_server.models.error_response400_bad_admin_or_value import ErrorResponse400BadAdminOrValue
from openapi_server.models.error_response401_bad_key_for_basic_auth import ErrorResponse401BadKeyForBasicAuth
from openapi_server.models.error_response404_not_found import ErrorResponse404NotFound
from openapi_server.models.float_value_object import FloatValueObject
from openapi_server.models.float_var import FloatVar
from openapi_server.models.int32_value_object import Int32ValueObject
from openapi_server.models.int32_var import Int32Var
from openapi_server.models.int64_string_value_object import Int64StringValueObject
from openapi_server.models.int64_value_object import Int64ValueObject
from openapi_server.models.int64_var import Int64Var
from openapi_server.models.int64_var_as_string import Int64VarAsString
from openapi_server.models.strategy_response import StrategyResponse
from openapi_server.models.string_value_object import StringValueObject
from openapi_server.models.string_var import StringVar
from openapi_server.models.table_def import TableDef


pytestmark = pytest.mark.asyncio

async def test_read_analog_input_eu(client):
    """Test case for read_analog_input_eu

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/ios/analogInputs/{io_name}/eu'.format(io_name='io_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_analog_inputs(client):
    """Test case for read_analog_inputs

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/ios/analogInputs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_analog_output_eu(client):
    """Test case for read_analog_output_eu

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/ios/analogOutputs/{io_name}/eu'.format(io_name='io_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_analog_outputs(client):
    """Test case for read_analog_outputs

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/ios/analogOutputs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_device_details(client):
    """Test case for read_device_details

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_digital_input_state(client):
    """Test case for read_digital_input_state

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/ios/digitalInputs/{io_name}/state'.format(io_name='io_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_digital_inputs(client):
    """Test case for read_digital_inputs

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/ios/digitalInputs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_digital_output_state(client):
    """Test case for read_digital_output_state

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/ios/digitalOutputs/{io_name}/state'.format(io_name='io_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_digital_outputs(client):
    """Test case for read_digital_outputs

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/ios/digitalOutputs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_down_timer_value(client):
    """Test case for read_down_timer_value

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/vars/downTimers/{down_timer_name}/value'.format(down_timer_name='down_timer_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_down_timer_vars(client):
    """Test case for read_down_timer_vars

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/vars/downTimers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_float_table(client):
    """Test case for read_float_table

    
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

async def test_read_float_table_element(client):
    """Test case for read_float_table_element

    
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

async def test_read_float_tables(client):
    """Test case for read_float_tables

    
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

async def test_read_float_var(client):
    """Test case for read_float_var

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/vars/floats/{float_name}'.format(float_name='float_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_float_vars(client):
    """Test case for read_float_vars

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/vars/floats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_int32_table(client):
    """Test case for read_int32_table

    
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

async def test_read_int32_table_element(client):
    """Test case for read_int32_table_element

    
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

async def test_read_int32_tables(client):
    """Test case for read_int32_tables

    
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

async def test_read_int32_var(client):
    """Test case for read_int32_var

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/vars/int32s/{int32_name}'.format(int32_name='int32_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_int32_vars(client):
    """Test case for read_int32_vars

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/vars/int32s',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_int64_table(client):
    """Test case for read_int64_table

    
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

async def test_read_int64_table_as_string(client):
    """Test case for read_int64_table_as_string

    
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

async def test_read_int64_table_element(client):
    """Test case for read_int64_table_element

    
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

async def test_read_int64_table_element_as_string(client):
    """Test case for read_int64_table_element_as_string

    
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

async def test_read_int64_tables(client):
    """Test case for read_int64_tables

    
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

async def test_read_int64_var(client):
    """Test case for read_int64_var

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/vars/int64s/{int64_name}'.format(int64_name='int64_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_int64_var_as_string(client):
    """Test case for read_int64_var_as_string

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/vars/int64s/{int64_name}/_string'.format(int64_name='int64_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_int64_vars(client):
    """Test case for read_int64_vars

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/vars/int64s',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_int64_vars_as_strings(client):
    """Test case for read_int64_vars_as_strings

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/vars/int64s/_string',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_strategy_details(client):
    """Test case for read_strategy_details

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_string_table(client):
    """Test case for read_string_table

    
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

async def test_read_string_table_element(client):
    """Test case for read_string_table_element

    
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

async def test_read_string_tables(client):
    """Test case for read_string_tables

    
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

async def test_read_string_var(client):
    """Test case for read_string_var

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/vars/strings/{string_name}'.format(string_name='string_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_string_vars(client):
    """Test case for read_string_vars

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/vars/strings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_up_timer_value(client):
    """Test case for read_up_timer_value

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/vars/upTimers/{up_timer_name}/value'.format(up_timer_name='up_timer_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_up_timer_vars(client):
    """Test case for read_up_timer_vars

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy/vars/upTimers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_analog_output_eu(client):
    """Test case for write_analog_output_eu

    
    """
    body = {"value":0.8008282}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/ios/analogOutputs/{io_name}/eu'.format(io_name='io_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_digital_output_state(client):
    """Test case for write_digital_output_state

    
    """
    body = {"value":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/ios/digitalOutputs/{io_name}/state'.format(io_name='io_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_float_table(client):
    """Test case for write_float_table

    
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

async def test_write_float_table_element(client):
    """Test case for write_float_table_element

    
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

async def test_write_float_var(client):
    """Test case for write_float_var

    
    """
    body = {"value":0.8008282}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/vars/floats/{float_name}'.format(float_name='float_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_int32_table(client):
    """Test case for write_int32_table

    
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

async def test_write_int32_table_element(client):
    """Test case for write_int32_table_element

    
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

async def test_write_int32_var(client):
    """Test case for write_int32_var

    
    """
    body = {"value":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/vars/int32s/{int32_name}'.format(int32_name='int32_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_int64_table(client):
    """Test case for write_int64_table

    
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

async def test_write_int64_table_as_string(client):
    """Test case for write_int64_table_as_string

    
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

async def test_write_int64_table_element(client):
    """Test case for write_int64_table_element

    
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

async def test_write_int64_table_element_as_string(client):
    """Test case for write_int64_table_element_as_string

    
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

async def test_write_int64_var(client):
    """Test case for write_int64_var

    
    """
    body = {"value":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/vars/int64s/{int64_name}'.format(int64_name='int64_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_int64_var_as_string(client):
    """Test case for write_int64_var_as_string

    
    """
    body = {"value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/vars/int64s/{int64_name}/_string'.format(int64_name='int64_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_string_table(client):
    """Test case for write_string_table

    
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

async def test_write_string_table_element(client):
    """Test case for write_string_table_element

    
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


pytestmark = pytest.mark.asyncio

async def test_write_string_var(client):
    """Test case for write_string_var

    
    """
    body = {"value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/strategy/vars/strings/{string_name}'.format(string_name='string_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

