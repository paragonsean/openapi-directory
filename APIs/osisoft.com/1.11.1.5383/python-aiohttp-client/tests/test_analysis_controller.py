# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analysis import Analysis
from openapi_server.models.errors import Errors
from openapi_server.models.items_analysis import ItemsAnalysis
from openapi_server.models.items_analysis_category import ItemsAnalysisCategory
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.security_entry import SecurityEntry


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analysis_create_security_entry(client):
    """Test case for analysis_create_security_entry

    Create a security entry owned by the analysis.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/analyses/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_delete(client):
    """Test case for analysis_delete

    Delete an Analysis.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/analyses/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_delete_security_entry(client):
    """Test case for analysis_delete_security_entry

    Delete a security entry owned by the analysis.
    """
    params = [('applyToChildren', True)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/analyses/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_get(client):
    """Test case for analysis_get

    Retrieve an Analysis.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analyses/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_get_analyses_query(client):
    """Test case for analysis_get_analyses_query

    Retrieve analyses based on the specified conditions. By default, returns all analyses.
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
        path='/piwebapi/analyses/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_get_by_path(client):
    """Test case for analysis_get_by_path

    Retrieve an Analysis by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analyses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_get_categories(client):
    """Test case for analysis_get_categories

    Get an Analysis' categories.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analyses/{web_id}/categories'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_get_security(client):
    """Test case for analysis_get_security

    Get the security information of the specified security item associated with the Analysis for a specified user.
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
        path='/piwebapi/analyses/{web_id}/security'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_get_security_entries(client):
    """Test case for analysis_get_security_entries

    Retrieve the security entries associated with the analysis based on the specified criteria. By default, all security entries for this analysis are returned.
    """
    params = [('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analyses/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_get_security_entry_by_name(client):
    """Test case for analysis_get_security_entry_by_name

    Retrieve the security entry associated with the analysis with the specified name.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analyses/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analysis_update(client):
    """Test case for analysis_update

    Update an Analysis.
    """
    analysis = {"Path":"\\\\MyAssetServer\\MyDatabase\\MyElement\\Analyses[MyAnalysis]","Status":"Disabled","IsTimeRuleDefinedByTemplate":False,"Description":"","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"HasNotification":False,"Priority":"High","HasTarget":True,"OutputTime":"","HasTemplate":False,"PublishResults":False,"GroupId":0,"Name":"MyAnalysis","TargetWebId":"I1ETDqD5loBNH0erqeqJodtALAjFPVfUpY-02A8uioGDSgIg","CategoryNames":["MyAnalysisCategory"],"AutoCreated":False,"AnalysisRulePlugInName":"PerformanceEquation","TimeRulePlugInName":"Periodic","WebId":"I1XsDqD5loBNH0erqeqJodtALAWDOFEb-U5xGEQwAVXYTCAA","Links":{"SecurityEntries":"SecurityEntries","Target":"Target","TimeRulePlugIn":"TimeRulePlugIn","Categories":"Categories","Database":"Database","Self":"Self","Security":"Security","AnalysisRule":"AnalysisRule","TimeRule":"TimeRule","AnalysisRulePlugIn":"AnalysisRulePlugIn","Template":"Template"},"TemplateName":"","Id":"11853358-94bf-11e7-8443-00155d84c200","MaximumQueueSize":0,"IsConfigured":False}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/analyses/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=analysis,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analysis_update_security_entry(client):
    """Test case for analysis_update_security_entry

    Update a security entry owned by the analysis.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True)]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/piwebapi/analyses/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

