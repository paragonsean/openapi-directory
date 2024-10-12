# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.items_item_point import ItemsItemPoint
from openapi_server.models.items_point_attribute import ItemsPointAttribute
from openapi_server.models.point import Point
from openapi_server.models.point_attribute import PointAttribute


pytestmark = pytest.mark.asyncio

async def test_point_delete(client):
    """Test case for point_delete

    Delete a point.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/points/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_point_get(client):
    """Test case for point_get

    Get a point.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/points/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_point_get_attribute_by_name(client):
    """Test case for point_get_attribute_by_name

    Get a point attribute by name.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/points/{web_id}/attributes/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_point_get_attributes(client):
    """Test case for point_get_attributes

    Get point attributes.
    """
    params = [('name', ['name_example']),
                    ('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/points/{web_id}/attributes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_point_get_by_path(client):
    """Test case for point_get_by_path

    Get a point by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/points',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_point_get_multiple(client):
    """Test case for point_get_multiple

    Retrieve multiple points by web id or path.
    """
    params = [('asParallel', True),
                    ('includeMode', 'include_mode_example'),
                    ('path', ['path_example']),
                    ('selectedFields', 'selected_fields_example'),
                    ('webId', ['web_id_example']),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/points/multiple',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_point_update(client):
    """Test case for point_update

    Update a point. The only PI Point attributes that can be updated include: Name, Descriptor, EngineeringUnits, Step, and DisplayDigits. Other PI Point attributes cannot be updated through PI Web API.
    """
    point_dto = {"Path":"\\\\MyPIServer\\PointName","Zero":0.0,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"DisplayDigits":-5,"Step":False,"Span":100.0,"Name":"PointName","PointClass":"classic","WebId":"I1DPa70Wf0zBA06CLkV9ovNQgQCAAAAA","Descriptor":"12 Hour Sine Wave","Future":False,"Links":{"PlotData":"PlotData","DataServer":"DataServer","Attributes":"Attributes","SummaryData":"SummaryData","Value":"Value","EndValue":"EndValue","Self":"Self","InterpolatedData":"InterpolatedData","RecordedData":"RecordedData"},"PointType":"Float32","Id":82,"DigitalSetName":"","EngineeringUnits":""}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/points/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=point_dto,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

