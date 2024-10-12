# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_server import DataServer
from openapi_server.models.data_server_license import DataServerLicense
from openapi_server.models.enumeration_set import EnumerationSet
from openapi_server.models.errors import Errors
from openapi_server.models.items_data_server import ItemsDataServer
from openapi_server.models.items_enumeration_set import ItemsEnumerationSet
from openapi_server.models.items_point import ItemsPoint
from openapi_server.models.point import Point


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_data_server_create_enumeration_set(client):
    """Test case for data_server_create_enumeration_set

    Create an enumeration set on the Data Server.
    """
    enumeration_set = {"Path":"\\\\MyAssetServer\\MyDatabase\\EnumerationSets[Model Number]","Description":"Model numbers by brand of vehicle","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1MSRDqD5loBNH0erqeqJodtALAT_x3jpGsKUCB1vtmvQHUMQ","Links":{"SecurityEntries":"SecurityEntries","DataServer":"DataServer","Database":"Database","Values":"Values","Self":"Self","Security":"Security"},"Id":"8e77fc4f-ac91-4029-81d6-fb66bd01d431","SerializeDescription":True,"Name":"Model Number"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/dataservers/{web_id}/enumerationsets'.format(web_id='web_id_example'),
        headers=headers,
        json=enumeration_set,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_data_server_create_point(client):
    """Test case for data_server_create_point

    Create a point in the specified Data Server.
    """
    point_dto = {"Path":"\\\\MyPIServer\\PointName","Zero":0.0,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"DisplayDigits":-5,"Step":False,"Span":100.0,"Name":"PointName","PointClass":"classic","WebId":"I1DPa70Wf0zBA06CLkV9ovNQgQCAAAAA","Descriptor":"12 Hour Sine Wave","Future":False,"Links":{"PlotData":"PlotData","DataServer":"DataServer","Attributes":"Attributes","SummaryData":"SummaryData","Value":"Value","EndValue":"EndValue","Self":"Self","InterpolatedData":"InterpolatedData","RecordedData":"RecordedData"},"PointType":"Float32","Id":82,"DigitalSetName":"","EngineeringUnits":""}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/dataservers/{web_id}/points'.format(web_id='web_id_example'),
        headers=headers,
        json=point_dto,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_server_get(client):
    """Test case for data_server_get

    Retrieve a Data Server.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/dataservers/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_server_get_by_name(client):
    """Test case for data_server_get_by_name

    Retrieve a Data Server by name.
    """
    params = [('name', 'name_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/dataservers#name',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_server_get_by_path(client):
    """Test case for data_server_get_by_path

    Retrieve a Data Server by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/dataservers#path',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_server_get_enumeration_sets(client):
    """Test case for data_server_get_enumeration_sets

    Retrieve enumeration sets for given Data Server.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/dataservers/{web_id}/enumerationsets'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_server_get_license(client):
    """Test case for data_server_get_license

    Retrieves the specified license for the given Data Server. The fields of the response object are string representations of the numerical values reported by the Data Server, with \"Infinity\" representing a license field with no limit.
    """
    params = [('module', 'module_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/dataservers/{web_id}/license'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_server_get_points(client):
    """Test case for data_server_get_points

    Retrieve a list of points on a specified Data Server.
    """
    params = [('maxCount', 56),
                    ('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('startIndex', 56),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/dataservers/{web_id}/points'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_server_list(client):
    """Test case for data_server_list

    Retrieve a list of Data Servers known to this service.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/dataservers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

