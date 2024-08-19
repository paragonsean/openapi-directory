# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attribute_template import AttributeTemplate
from openapi_server.models.items_attribute_category import ItemsAttributeCategory
from openapi_server.models.items_attribute_template import ItemsAttributeTemplate


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_attribute_template_create_attribute_template(client):
    """Test case for attribute_template_create_attribute_template

    Create an attribute template as a child of another attribute template.
    """
    template = {"IsManualDataEntry":False,"Path":"\\\\MyAssetServer\\MyDatabase\\ElementTemplates[MachineName]|Water(2008)","ConfigString":"SELECT [Water Use] FROM [Energy Use 2008] WHERE [Asset ID] = '%Element%'","IsHidden":False,"DefaultUnitsName":"liter","Description":"2008 Water Use","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"DefaultUnitsNameAbbreviation":"L","Name":"Water(2008)","IsExcluded":False,"DefaultValue":0,"HasChildren":False,"TraitName":"LimitLoLo","Type":"Int32","CategoryNames":["Energy Savings Targets"],"IsConfigurationItem":False,"WebId":"I1ATEG_auSSsvuECG8ad_p8b25QQkxqWDwIWU6zC4vmgpd4kgtSfQI9VdxUGA8fi1yf9DVg","Links":{"AttributeTemplates":"AttributeTemplates","Categories":"Categories","Parent":"Parent","Self":"Self","Trait":"Trait","ElementTemplate":"ElementTemplate"},"Id":"23d027b5-5dd5-41c5-80f1-f8b5c9ff4356","DataReferencePlugIn":"Table Lookup","TypeQualifier":""}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/attributetemplates/{web_id}/attributetemplates'.format(web_id='web_id_example'),
        headers=headers,
        json=template,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_template_delete(client):
    """Test case for attribute_template_delete

    Delete an attribute template.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/attributetemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_template_get(client):
    """Test case for attribute_template_get

    Retrieve an attribute template.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/attributetemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_template_get_attribute_templates(client):
    """Test case for attribute_template_get_attribute_templates

    Retrieve an attribute template's child attribute templates.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/attributetemplates/{web_id}/attributetemplates'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_template_get_by_path(client):
    """Test case for attribute_template_get_by_path

    Retrieve an attribute template by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/attributetemplates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_template_get_categories(client):
    """Test case for attribute_template_get_categories

    Get an attribute template's categories.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/attributetemplates/{web_id}/categories'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_attribute_template_update(client):
    """Test case for attribute_template_update

    Update an existing attribute template by replacing items in its definition.
    """
    template = {"IsManualDataEntry":False,"Path":"\\\\MyAssetServer\\MyDatabase\\ElementTemplates[MachineName]|Water(2008)","ConfigString":"SELECT [Water Use] FROM [Energy Use 2008] WHERE [Asset ID] = '%Element%'","IsHidden":False,"DefaultUnitsName":"liter","Description":"2008 Water Use","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"DefaultUnitsNameAbbreviation":"L","Name":"Water(2008)","IsExcluded":False,"DefaultValue":0,"HasChildren":False,"TraitName":"LimitLoLo","Type":"Int32","CategoryNames":["Energy Savings Targets"],"IsConfigurationItem":False,"WebId":"I1ATEG_auSSsvuECG8ad_p8b25QQkxqWDwIWU6zC4vmgpd4kgtSfQI9VdxUGA8fi1yf9DVg","Links":{"AttributeTemplates":"AttributeTemplates","Categories":"Categories","Parent":"Parent","Self":"Self","Trait":"Trait","ElementTemplate":"ElementTemplate"},"Id":"23d027b5-5dd5-41c5-80f1-f8b5c9ff4356","DataReferencePlugIn":"Table Lookup","TypeQualifier":""}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/attributetemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=template,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

