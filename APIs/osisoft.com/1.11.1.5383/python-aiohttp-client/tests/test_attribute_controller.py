# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attribute import Attribute
from openapi_server.models.items_attribute import ItemsAttribute
from openapi_server.models.items_attribute_category import ItemsAttributeCategory
from openapi_server.models.items_item_attribute import ItemsItemAttribute
from openapi_server.models.timed_value import TimedValue


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_attribute_create_attribute(client):
    """Test case for attribute_create_attribute

    Create a new attribute as a child of the specified attribute.
    """
    attribute = {"Description":"2008 Water Use","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"DefaultUnitsNameAbbreviation":"L","Step":False,"Span":100.0,"Name":"Water","IsExcluded":False,"CategoryNames":["Energy Savings Targets"],"IsConfigurationItem":False,"WebId":"I1AbEDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBAGyPedZG1sUmxOOclp3Flwg","Paths":["\\\\MyAssetServer\\MyDatabase\\MyElement|MyAttribute","\\\\MyAssetServer\\MyDatabase\\ReferencingElement\\MyElement|MyAttribute"],"IsManualDataEntry":False,"Path":"\\\\MyAssetServer\\MyDatabase\\CityName\\EngineeringProcess\\Equipment\\MachineName|Water(2008)","ConfigString":"SELECT [Water Use] FROM [Energy Use 2008] WHERE [Asset ID] = '%Element%'","IsHidden":False,"Zero":0.0,"DefaultUnitsName":"liter","DisplayDigits":-5,"HasChildren":False,"TraitName":"LimitLoLo","Type":"Int32","Links":{"PlotData":"PlotData","EnumerationSet":"EnumerationSet","Categories":"Categories","Parent":"Parent","Element":"Element","Attributes":"Attributes","Point":"Point","Self":"Self","EventFrame":"EventFrame","Template":"Template","SummaryData":"SummaryData","Value":"Value","EndValue":"EndValue","Trait":"Trait","InterpolatedData":"InterpolatedData","EnumerationValues":"EnumerationValues","RecordedData":"RecordedData"},"Id":"75de231b-b591-49b1-b138-e725a77165c2","DataReferencePlugIn":"Table Lookup","TypeQualifier":"","DataReference":{"Type":"PI Point","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"PIPoint":{"Path":"\\\\MyPIServer\\PointName","Zero":0.0,"DisplayDigits":-5,"Step":False,"Span":100.0,"Name":"PointName","PointClass":"classic","WebId":"I1DPa70Wf0zBA06CLkV9ovNQgQCAAAAA","Descriptor":"12 Hour Sine Wave","Future":False,"PointType":"Float32","Id":82,"DigitalSetName":"","EngineeringUnits":""}}}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/attributes/{web_id}/attributes'.format(web_id='web_id_example'),
        headers=headers,
        json=attribute,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_create_config(client):
    """Test case for attribute_create_config

    Create or update an attribute's DataReference configuration (Create/Update PI point for PI Point DataReference).
    """
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/attributes/{web_id}/config'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_delete(client):
    """Test case for attribute_delete

    Delete an attribute.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/attributes/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_get(client):
    """Test case for attribute_get

    Retrieve an attribute.
    """
    params = [('associations', 'associations_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/attributes/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_get_attributes(client):
    """Test case for attribute_get_attributes

    Get the child attributes of the specified attribute.
    """
    params = [('associations', 'associations_example'),
                    ('categoryName', 'category_name_example'),
                    ('maxCount', 56),
                    ('nameFilter', 'name_filter_example'),
                    ('searchFullHierarchy', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('showExcluded', True),
                    ('showHidden', True),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('startIndex', 56),
                    ('templateName', 'template_name_example'),
                    ('trait', ['trait_example']),
                    ('traitCategory', ['trait_category_example']),
                    ('valueType', 'value_type_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/attributes/{web_id}/attributes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_get_attributes_query(client):
    """Test case for attribute_get_attributes_query

    Retrieve attributes based on the specified conditions. Returns attributes using the specified search query string.
    """
    params = [('associations', 'associations_example'),
                    ('databaseWebId', 'database_web_id_example'),
                    ('maxCount', 56),
                    ('query', 'query_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('startIndex', 56),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/attributes/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_get_by_path(client):
    """Test case for attribute_get_by_path

    Retrieve an attribute by path.
    """
    params = [('path', 'path_example'),
                    ('associations', 'associations_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/attributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_get_categories(client):
    """Test case for attribute_get_categories

    Get an attribute's categories.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/attributes/{web_id}/categories'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_get_multiple(client):
    """Test case for attribute_get_multiple

    Retrieve multiple attributes by web id or path.
    """
    params = [('asParallel', True),
                    ('associations', 'associations_example'),
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
        path='/piwebapi/attributes/multiple',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_get_value(client):
    """Test case for attribute_get_value

    Get the attribute's value. This call is intended for use with attributes that have no data reference only. For attributes with a data reference, consult the documentation for Streams.
    """
    params = [('selectedFields', 'selected_fields_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/attributes/{web_id}/value'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_attribute_set_value(client):
    """Test case for attribute_set_value

    Set the value of a configuration item attribute. For attributes with a data reference or non-configuration item attributes, consult the documentation for streams.
    """
    value = {"Annotated":False,"Errors":[{"Message":["An error has occurred."],"FieldName":"Value"},{"Message":["An error has occurred."],"FieldName":"Value"}],"UnitsAbbreviation":"m","Substituted":False,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Good":True,"Timestamp":"2014-07-22T14:00:00Z","Questionable":False}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/piwebapi/attributes/{web_id}/value'.format(web_id='web_id_example'),
        headers=headers,
        json=value,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_attribute_update(client):
    """Test case for attribute_update

    Update an attribute by replacing items in its definition.
    """
    attribute = {"Description":"2008 Water Use","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"DefaultUnitsNameAbbreviation":"L","Step":False,"Span":100.0,"Name":"Water","IsExcluded":False,"CategoryNames":["Energy Savings Targets"],"IsConfigurationItem":False,"WebId":"I1AbEDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBAGyPedZG1sUmxOOclp3Flwg","Paths":["\\\\MyAssetServer\\MyDatabase\\MyElement|MyAttribute","\\\\MyAssetServer\\MyDatabase\\ReferencingElement\\MyElement|MyAttribute"],"IsManualDataEntry":False,"Path":"\\\\MyAssetServer\\MyDatabase\\CityName\\EngineeringProcess\\Equipment\\MachineName|Water(2008)","ConfigString":"SELECT [Water Use] FROM [Energy Use 2008] WHERE [Asset ID] = '%Element%'","IsHidden":False,"Zero":0.0,"DefaultUnitsName":"liter","DisplayDigits":-5,"HasChildren":False,"TraitName":"LimitLoLo","Type":"Int32","Links":{"PlotData":"PlotData","EnumerationSet":"EnumerationSet","Categories":"Categories","Parent":"Parent","Element":"Element","Attributes":"Attributes","Point":"Point","Self":"Self","EventFrame":"EventFrame","Template":"Template","SummaryData":"SummaryData","Value":"Value","EndValue":"EndValue","Trait":"Trait","InterpolatedData":"InterpolatedData","EnumerationValues":"EnumerationValues","RecordedData":"RecordedData"},"Id":"75de231b-b591-49b1-b138-e725a77165c2","DataReferencePlugIn":"Table Lookup","TypeQualifier":"","DataReference":{"Type":"PI Point","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"PIPoint":{"Path":"\\\\MyPIServer\\PointName","Zero":0.0,"DisplayDigits":-5,"Step":False,"Span":100.0,"Name":"PointName","PointClass":"classic","WebId":"I1DPa70Wf0zBA06CLkV9ovNQgQCAAAAA","Descriptor":"12 Hour Sine Wave","Future":False,"PointType":"Float32","Id":82,"DigitalSetName":"","EngineeringUnits":""}}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/attributes/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=attribute,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

