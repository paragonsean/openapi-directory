# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attribute_template import AttributeTemplate
from openapi_server.models.element_template import ElementTemplate
from openapi_server.models.errors import Errors
from openapi_server.models.items_analysis_template import ItemsAnalysisTemplate
from openapi_server.models.items_attribute_template import ItemsAttributeTemplate
from openapi_server.models.items_element_category import ItemsElementCategory
from openapi_server.models.items_element_template import ItemsElementTemplate
from openapi_server.models.items_notification_rule_template import ItemsNotificationRuleTemplate
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.notification_rule_template import NotificationRuleTemplate
from openapi_server.models.security_entry import SecurityEntry


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_element_template_create_attribute_template(client):
    """Test case for element_template_create_attribute_template

    Create an attribute template.
    """
    template = {"IsManualDataEntry":False,"Path":"\\\\MyAssetServer\\MyDatabase\\ElementTemplates[MachineName]|Water(2008)","ConfigString":"SELECT [Water Use] FROM [Energy Use 2008] WHERE [Asset ID] = '%Element%'","IsHidden":False,"DefaultUnitsName":"liter","Description":"2008 Water Use","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"DefaultUnitsNameAbbreviation":"L","Name":"Water(2008)","IsExcluded":False,"DefaultValue":0,"HasChildren":False,"TraitName":"LimitLoLo","Type":"Int32","CategoryNames":["Energy Savings Targets"],"IsConfigurationItem":False,"WebId":"I1ATEG_auSSsvuECG8ad_p8b25QQkxqWDwIWU6zC4vmgpd4kgtSfQI9VdxUGA8fi1yf9DVg","Links":{"AttributeTemplates":"AttributeTemplates","Categories":"Categories","Parent":"Parent","Self":"Self","Trait":"Trait","ElementTemplate":"ElementTemplate"},"Id":"23d027b5-5dd5-41c5-80f1-f8b5c9ff4356","DataReferencePlugIn":"Table Lookup","TypeQualifier":""}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/elementtemplates/{web_id}/attributetemplates'.format(web_id='web_id_example'),
        headers=headers,
        json=template,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_element_template_create_notification_rule_template(client):
    """Test case for element_template_create_notification_rule_template

    Create a notification rule template.
    """
    notification_rule_template = {"Path":"\\\\MyAssetServer\\MyDatabase\\CityName\\ElementTemplates[Template3]\\NotificationRuleTemplates[Notification Rule Template]","Status":"Functioning","MultiTriggerEventOption":"HighestSeverity","Description":"Description entered by the user","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"ResendInterval":"PT5S","Criteria":"Name: EventFrameCriteriaName","Name":"MachineName","CategoryNames":["MachineNameAlerts"],"WebId":"I1NTDqD5loBNH0erqeqJodtALAtdcX5JH_5xGEKAAVXTSaAg","TemplateName":"MachineName Notification Rule Template","Id":"e9a984d0-f47c-11e7-8454-00155d029708","NonrepetitionInterval":"PT3S"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/elementtemplates/{web_id}/notificationruletemplates'.format(web_id='web_id_example'),
        headers=headers,
        json=notification_rule_template,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_element_template_create_security_entry(client):
    """Test case for element_template_create_security_entry

    Create a security entry owned by the element template.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/elementtemplates/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_template_delete(client):
    """Test case for element_template_delete

    Delete an element template.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/elementtemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_template_delete_security_entry(client):
    """Test case for element_template_delete_security_entry

    Delete a security entry owned by the element template.
    """
    params = [('applyToChildren', True)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/elementtemplates/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_template_get(client):
    """Test case for element_template_get

    Retrieve an element template.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elementtemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_template_get_analysis_templates(client):
    """Test case for element_template_get_analysis_templates

    Get analysis templates for an element template.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elementtemplates/{web_id}/analysistemplates'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_template_get_attribute_templates(client):
    """Test case for element_template_get_attribute_templates

    Get child attribute templates for an element template.
    """
    params = [('depthFirstTraverse', True),
                    ('maxCount', 56),
                    ('selectedFields', 'selected_fields_example'),
                    ('showDescendants', True),
                    ('showInherited', True),
                    ('startIndex', 56),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elementtemplates/{web_id}/attributetemplates'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_template_get_base_element_templates(client):
    """Test case for element_template_get_base_element_templates

    Get base element templates for an element template.
    """
    params = [('maxCount', 56),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elementtemplates/{web_id}/baseelementtemplates'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_template_get_by_path(client):
    """Test case for element_template_get_by_path

    Retrieve an element template by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elementtemplates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_template_get_categories(client):
    """Test case for element_template_get_categories

    Get an element template's categories.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('showInherited', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elementtemplates/{web_id}/categories'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_template_get_derived_element_templates(client):
    """Test case for element_template_get_derived_element_templates

    Get derived element templates for an element template.
    """
    params = [('maxCount', 56),
                    ('selectedFields', 'selected_fields_example'),
                    ('showDescendants', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elementtemplates/{web_id}/derivedelementtemplates'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_template_get_notification_rule_templates(client):
    """Test case for element_template_get_notification_rule_templates

    Get notification rule templates for an element template
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elementtemplates/{web_id}/notificationruletemplates'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_template_get_security(client):
    """Test case for element_template_get_security

    Get the security information of the specified security item associated with the element template for a specified user.
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
        path='/piwebapi/elementtemplates/{web_id}/security'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_template_get_security_entries(client):
    """Test case for element_template_get_security_entries

    Retrieve the security entries associated with the element template based on the specified criteria. By default, all security entries for this element template are returned.
    """
    params = [('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elementtemplates/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_template_get_security_entry_by_name(client):
    """Test case for element_template_get_security_entry_by_name

    Retrieve the security entry associated with the element template with the specified name.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elementtemplates/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_element_template_update(client):
    """Test case for element_template_update

    Update an element template by replacing items in its definition.
    """
    template = {"Path":"\\\\MyAssetServer\\MyDatabase\\ElementTemplates[Boiler]","CanBeAcknowledged":False,"Description":"Manufacturing Machine MachineName","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"NamingPattern":"%TEMPLATE%","Severity":"None","BaseTemplate":"Equipment","ExtendedProperties":{"key":{"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Exception":{"Errors":["An error has occurred."]}}},"Name":"MachineName","CategoryNames":["Equipment Assets"],"WebId":"I1ETDqD5loBNH0erqeqJodtALAkpSYp6uykE2Ku0yChDU91g","Links":{"AttributeTemplates":"AttributeTemplates","SecurityEntries":"SecurityEntries","DerivedTemplates":"DerivedTemplates","Categories":"Categories","BaseTemplates":"BaseTemplates","AnalysisTemplates":"AnalysisTemplates","Database":"Database","DefaultAttribute":"DefaultAttribute","Self":"Self","BaseTemplate":"BaseTemplate","Security":"Security","NotificationRuleTemplates":"NotificationRuleTemplates"},"Id":"a7989492-b2ab-4d90-8abb-4c8284353dd6","AllowElementToExtend":False,"InstanceType":"Element"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/elementtemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=template,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_element_template_update_security_entry(client):
    """Test case for element_template_update_security_entry

    Update a security entry owned by the element template.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True)]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/piwebapi/elementtemplates/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

