# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analysis_template import AnalysisTemplate
from openapi_server.models.errors import Errors
from openapi_server.models.items_analysis_category import ItemsAnalysisCategory
from openapi_server.models.items_analysis_template import ItemsAnalysisTemplate
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.security_entry import SecurityEntry


pytestmark = pytest.mark.asyncio

async def test_analysis_template_create_from_analysis(client):
    """Test case for analysis_template_create_from_analysis

    Create an Analysis template based upon a specified Analysis.
    """
    params = [('analysisWebId', 'analysis_web_id_example'),
                    ('name', 'name_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/analysistemplates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analysis_template_create_security_entry(client):
    """Test case for analysis_template_create_security_entry

    Create a security entry owned by the analysis template.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/analysistemplates/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_template_delete(client):
    """Test case for analysis_template_delete

    Delete an analysis template.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/analysistemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_template_delete_security_entry(client):
    """Test case for analysis_template_delete_security_entry

    Delete a security entry owned by the analysis template.
    """
    params = [('applyToChildren', True)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/analysistemplates/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_template_get(client):
    """Test case for analysis_template_get

    Retrieve an analysis template.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analysistemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_template_get_analysis_templates_query(client):
    """Test case for analysis_template_get_analysis_templates_query

    Retrieve analysis templates based on the specified conditions. By default, returns all analysis templates.
    """
    params = [('databaseWebId', 'database_web_id_example'),
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
        path='/piwebapi/analysistemplates/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_template_get_by_path(client):
    """Test case for analysis_template_get_by_path

    Retrieve an analysis template by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analysistemplates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_template_get_categories(client):
    """Test case for analysis_template_get_categories

    Get an analysis template's categories.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analysistemplates/{web_id}/categories'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_template_get_security(client):
    """Test case for analysis_template_get_security

    Get the security information of the specified security item associated with the analysis template for a specified user.
    """
    params = [('userIdentity', ['user_identity_example']),
                    ('forceRefresh', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analysistemplates/{web_id}/security'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_template_get_security_entries(client):
    """Test case for analysis_template_get_security_entries

    Retrieve the security entries associated with the analysis template based on the specified criteria. By default, all security entries for this analysis template are returned.
    """
    params = [('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analysistemplates/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_template_get_security_entry_by_name(client):
    """Test case for analysis_template_get_security_entry_by_name

    Retrieve the security entry associated with the analysis template with the specified name.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analysistemplates/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analysis_template_update(client):
    """Test case for analysis_template_update

    Update an analysis template by replacing items in its definition.
    """
    template = {"Path":"\\\\MyAssetServer\\MyDatabase\\AnalysisTemplates[MyAnalysisTemplate]","Description":"","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"HasTarget":False,"OutputTime":"","HasNotificationTemplate":False,"TargetName":"MyElementTemplate","GroupId":0,"Name":"MyAnalysisTemplate","CreateEnabled":True,"CategoryNames":["MyAnalysisCategory"],"AnalysisRulePlugInName":"PerformanceEquation","TimeRulePlugInName":"Periodic","WebId":"I1XTG_auSSsvuECG8ad_p8b25QEZgtYQY_J06YnELl5cALiA","Links":{"SecurityEntries":"SecurityEntries","Target":"Target","TimeRulePlugIn":"TimeRulePlugIn","Categories":"Categories","Database":"Database","Self":"Self","Security":"Security","AnalysisRule":"AnalysisRule","TimeRule":"TimeRule","AnalysisRulePlugIn":"AnalysisRulePlugIn"},"Id":"612d9811-3f06-4e27-989c-42e5e5c00b88"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/analysistemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=template,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analysis_template_update_security_entry(client):
    """Test case for analysis_template_update_security_entry

    Update a security entry owned by the analysis template.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True)]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/piwebapi/analysistemplates/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

