# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analysis_category import AnalysisCategory
from openapi_server.models.analysis_template import AnalysisTemplate
from openapi_server.models.asset_database import AssetDatabase
from openapi_server.models.attribute_category import AttributeCategory
from openapi_server.models.element import Element
from openapi_server.models.element_category import ElementCategory
from openapi_server.models.element_template import ElementTemplate
from openapi_server.models.enumeration_set import EnumerationSet
from openapi_server.models.errors import Errors
from openapi_server.models.event_frame import EventFrame
from openapi_server.models.items_analysis import ItemsAnalysis
from openapi_server.models.items_analysis_category import ItemsAnalysisCategory
from openapi_server.models.items_analysis_template import ItemsAnalysisTemplate
from openapi_server.models.items_attribute import ItemsAttribute
from openapi_server.models.items_attribute_category import ItemsAttributeCategory
from openapi_server.models.items_element import ItemsElement
from openapi_server.models.items_element_category import ItemsElementCategory
from openapi_server.models.items_element_template import ItemsElementTemplate
from openapi_server.models.items_enumeration_set import ItemsEnumerationSet
from openapi_server.models.items_event_frame import ItemsEventFrame
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.items_table import ItemsTable
from openapi_server.models.items_table_category import ItemsTableCategory
from openapi_server.models.security_entry import SecurityEntry
from openapi_server.models.table import Table
from openapi_server.models.table_category import TableCategory


pytestmark = pytest.mark.asyncio

async def test_asset_database_add_referenced_element(client):
    """Test case for asset_database_add_referenced_element

    Add a reference to an existing element to the specified database.
    """
    params = [('referencedElementWebId', ['referenced_element_web_id_example']),
                    ('referenceType', 'reference_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetdatabases/{web_id}/referencedelements'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_database_create_analysis_category(client):
    """Test case for asset_database_create_analysis_category

    Create an analysis category at the Asset Database root.
    """
    analysis_category = {"Path":"\\\\MyAssetServer\\Database\\CategoriesAnalysis[CategoryName]","Description":"Relative energy use per ton of process feed.","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1XCDqD5loBNH0erqeqJodtALAoko2-UoOVEibhTWQCk1MDw","Links":{"SecurityEntries":"SecurityEntries","Database":"Database","Self":"Self","Security":"Security"},"Id":"f9364aa2-0e4a-4854-9b85-35900a4d4c0f","Name":"CategoryName"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetdatabases/{web_id}/analysiscategories'.format(web_id='web_id_example'),
        headers=headers,
        json=analysis_category,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_database_create_analysis_template(client):
    """Test case for asset_database_create_analysis_template

    Create an analysis template at the Asset Database root.
    """
    template = {"Path":"\\\\MyAssetServer\\MyDatabase\\AnalysisTemplates[MyAnalysisTemplate]","Description":"","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"HasTarget":False,"OutputTime":"","HasNotificationTemplate":False,"TargetName":"MyElementTemplate","GroupId":0,"Name":"MyAnalysisTemplate","CreateEnabled":True,"CategoryNames":["MyAnalysisCategory"],"AnalysisRulePlugInName":"PerformanceEquation","TimeRulePlugInName":"Periodic","WebId":"I1XTG_auSSsvuECG8ad_p8b25QEZgtYQY_J06YnELl5cALiA","Links":{"SecurityEntries":"SecurityEntries","Target":"Target","TimeRulePlugIn":"TimeRulePlugIn","Categories":"Categories","Database":"Database","Self":"Self","Security":"Security","AnalysisRule":"AnalysisRule","TimeRule":"TimeRule","AnalysisRulePlugIn":"AnalysisRulePlugIn"},"Id":"612d9811-3f06-4e27-989c-42e5e5c00b88"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetdatabases/{web_id}/analysistemplates'.format(web_id='web_id_example'),
        headers=headers,
        json=template,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_database_create_attribute_category(client):
    """Test case for asset_database_create_attribute_category

    Create an attribute category at the Asset Database root.
    """
    attribute_category = {"Path":"\\\\MyAssetServer\\Database\\CategoriesAttribute[CategoryName]","Description":"Relative energy use per ton of process feed.","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1ACDqD5loBNH0erqeqJodtALAofQgBVRE3E-0dk03Hqa1ng","Links":{"SecurityEntries":"SecurityEntries","Database":"Database","Self":"Self","Security":"Security"},"Id":"0520f4a1-4454-4fdc-b476-4d371ea6b59e","Name":"CategoryName"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetdatabases/{web_id}/attributecategories'.format(web_id='web_id_example'),
        headers=headers,
        json=attribute_category,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_database_create_element(client):
    """Test case for asset_database_create_element

    Create a child element.
    """
    element = {"Path":"\\\\MyAssetServer\\MyDatabase\\CityName\\EngineeringProcess\\Equipment\\MachineName","Description":"Manufacturing Equipment MachineName","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"ExtendedProperties":{"key":{"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Exception":{"Errors":["An error has occurred."]}}},"Name":"MachineName","Errors":[{"Message":["An error has occurred."],"FieldName":"Value"},{"Message":["An error has occurred."],"FieldName":"Value"}],"HasChildren":False,"CategoryNames":["Equipment Assets"],"WebId":"I1EmDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBA","Links":{"PlotData":"PlotData","Categories":"Categories","Parent":"Parent","Attributes":"Attributes","Analyses":"Analyses","Self":"Self","Elements":"Elements","Security":"Security","Template":"Template","SecurityEntries":"SecurityEntries","NotificationRules":"NotificationRules","Database":"Database","SummaryData":"SummaryData","Value":"Value","EventFrames":"EventFrames","EndValue":"EndValue","DefaultAttribute":"DefaultAttribute","InterpolatedData":"InterpolatedData","RecordedData":"RecordedData"},"TemplateName":"MachineName","Id":"cbb28260-853d-11e4-80c5-00155d844304","Paths":["Paths","Paths"]}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetdatabases/{web_id}/elements'.format(web_id='web_id_example'),
        headers=headers,
        json=element,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_database_create_element_category(client):
    """Test case for asset_database_create_element_category

    Create an element category at the Asset Database root.
    """
    element_category = {"Path":"\\\\MyAssetServer\\Database\\CategoriesElement[CategoryName]","Description":"Relative energy use per ton of process feed.","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1ECDqD5loBNH0erqeqJodtALAQ_lRME1-QUKrnEUKhMgEUA","Links":{"SecurityEntries":"SecurityEntries","Database":"Database","Self":"Self","Security":"Security"},"Id":"3051f943-7e4d-4241-ab9c-450a84c80450","Name":"CategoryName"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetdatabases/{web_id}/elementcategories'.format(web_id='web_id_example'),
        headers=headers,
        json=element_category,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_database_create_element_template(client):
    """Test case for asset_database_create_element_template

    Create a template at the Asset Database root. Specify InstanceType of \"Element\" or \"EventFrame\" to create element or event frame template respectively. Only these two types of templates can be created.
    """
    template = {"Path":"\\\\MyAssetServer\\MyDatabase\\ElementTemplates[Boiler]","CanBeAcknowledged":False,"Description":"Manufacturing Machine MachineName","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"NamingPattern":"%TEMPLATE%","Severity":"None","BaseTemplate":"Equipment","ExtendedProperties":{"key":{"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Exception":{"Errors":["An error has occurred."]}}},"Name":"MachineName","CategoryNames":["Equipment Assets"],"WebId":"I1ETDqD5loBNH0erqeqJodtALAkpSYp6uykE2Ku0yChDU91g","Links":{"AttributeTemplates":"AttributeTemplates","SecurityEntries":"SecurityEntries","DerivedTemplates":"DerivedTemplates","Categories":"Categories","BaseTemplates":"BaseTemplates","AnalysisTemplates":"AnalysisTemplates","Database":"Database","DefaultAttribute":"DefaultAttribute","Self":"Self","BaseTemplate":"BaseTemplate","Security":"Security","NotificationRuleTemplates":"NotificationRuleTemplates"},"Id":"a7989492-b2ab-4d90-8abb-4c8284353dd6","AllowElementToExtend":False,"InstanceType":"Element"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetdatabases/{web_id}/elementtemplates'.format(web_id='web_id_example'),
        headers=headers,
        json=template,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_database_create_enumeration_set(client):
    """Test case for asset_database_create_enumeration_set

    Create an enumeration set at the Asset Database.
    """
    enumeration_set = {"Path":"\\\\MyAssetServer\\MyDatabase\\EnumerationSets[Model Number]","Description":"Model numbers by brand of vehicle","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1MSRDqD5loBNH0erqeqJodtALAT_x3jpGsKUCB1vtmvQHUMQ","Links":{"SecurityEntries":"SecurityEntries","DataServer":"DataServer","Database":"Database","Values":"Values","Self":"Self","Security":"Security"},"Id":"8e77fc4f-ac91-4029-81d6-fb66bd01d431","SerializeDescription":True,"Name":"Model Number"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetdatabases/{web_id}/enumerationsets'.format(web_id='web_id_example'),
        headers=headers,
        json=enumeration_set,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_database_create_event_frame(client):
    """Test case for asset_database_create_event_frame

    Create an event frame.
    """
    event_frame = {"IsAcknowledged":True,"Path":"\\\\MyAssetServer\\MyDatabase\\EventFrames[EF20140725-001]","CanBeAcknowledged":True,"AcknowledgedBy":"MyDomain\\UserA","Description":"Event Frame of Past Week","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"EndTime":"2014-07-25T14:45:29Z","StartTime":"2014-07-18T14:45:29Z","IsLocked":False,"Severity":"None","Security":{"CanWrite":True,"Rights":["Read","WriteData"],"CanReadData":True,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"HasAdmin":True,"CanWriteData":True,"CanDelete":True,"CanRead":True,"CanAnnotate":True,"CanExecute":True,"CanSubscribe":True,"CanSubscribeOthers":True},"ExtendedProperties":{"key":{"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Exception":{"Errors":["An error has occurred."]}}},"Name":"EF20140725-001","IsAnnotated":False,"AcknowledgedDate":"2014-07-30T11:04:23Z","HasChildren":False,"CategoryNames":["Processing Plant"],"AreValuesCaptured":False,"WebId":"I1FmDqD5loBNH0erqeqJodtALADqD5loBNH0cAAAAAAASwAg","Links":{"PlotData":"PlotData","PrimaryReferencedElement":"PrimaryReferencedElement","Categories":"Categories","Parent":"Parent","Attributes":"Attributes","ReferencedElements":"ReferencedElements","Self":"Self","Security":"Security","Template":"Template","SecurityEntries":"SecurityEntries","Annotations":"Annotations","Database":"Database","SummaryData":"SummaryData","Value":"Value","EventFrames":"EventFrames","EndValue":"EndValue","DefaultAttribute":"DefaultAttribute","InterpolatedData":"InterpolatedData","RecordedData":"RecordedData"},"TemplateName":"Template","Id":"96f9a00e-4d80-471f-0000-00000004b002","RefElementWebIds":["I1EmDqD5loBNH0erqeqJodtALAaqQoQHk26BGgMQAVXYR0Ag"]}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetdatabases/{web_id}/eventframes'.format(web_id='web_id_example'),
        headers=headers,
        json=event_frame,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_database_create_security_entry(client):
    """Test case for asset_database_create_security_entry

    Create a security entry owned by the asset database.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True),
                    ('securityItem', 'security_item_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetdatabases/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_database_create_table(client):
    """Test case for asset_database_create_table

    Create a table on the Asset Database.
    """
    table = {"Path":"\\\\MyAssetServer\\MyDatabase\\Tables[CarInfo]","TimeZone":"Eastern Standard Time","CategoryNames":["Table Category"],"Description":"Table of car info.","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"ConvertToLocalTime":False,"WebId":"I1BlDqD5loBNH0erqeqJodtALAmLr4X86Jmkeynt3QVwlqXw","Links":{"SecurityEntries":"SecurityEntries","Categories":"Categories","Database":"Database","Data":"Data","Self":"Self","Security":"Security"},"Id":"5ff8ba98-89ce-479a-b29e-ddd057096a5f","Name":"CarInfo"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetdatabases/{web_id}/tables'.format(web_id='web_id_example'),
        headers=headers,
        json=table,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_database_create_table_category(client):
    """Test case for asset_database_create_table_category

    Create a table category on the Asset Database.
    """
    table_category = {"Path":"\\\\MyAssetServer\\Database\\CategoriesTable[CategoryName]","Description":"Relative energy use per ton of process feed.","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1BCDqD5loBNH0erqeqJodtALAwgzHiSFSd06HP4lKPqYefQ","Links":{"SecurityEntries":"SecurityEntries","Database":"Database","Self":"Self","Security":"Security"},"Id":"89c70cc2-5221-4e77-873f-894a3ea61e7d","Name":"CategoryName"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetdatabases/{web_id}/tablecategories'.format(web_id='web_id_example'),
        headers=headers,
        json=table_category,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_delete(client):
    """Test case for asset_database_delete

    Delete an asset database.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/assetdatabases/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_delete_security_entry(client):
    """Test case for asset_database_delete_security_entry

    Delete a security entry owned by the asset database.
    """
    params = [('applyToChildren', True),
                    ('securityItem', 'security_item_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/assetdatabases/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_export(client):
    """Test case for asset_database_export

    Export the asset database.
    """
    params = [('endTime', 'end_time_example'),
                    ('exportMode', ['export_mode_example']),
                    ('startTime', 'start_time_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/export'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_find_analyses(client):
    """Test case for asset_database_find_analyses

    Retrieve analyses based on the specified conditions.
    """
    params = [('field', ['_field_example']),
                    ('maxCount', 56),
                    ('query', 'query_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('startIndex', 56),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/analyses'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_find_element_attributes(client):
    """Test case for asset_database_find_element_attributes

    Retrieves a list of element attributes matching the specified filters from the specified asset database.
    """
    params = [('associations', 'associations_example'),
                    ('attributeCategory', 'attribute_category_example'),
                    ('attributeDescriptionFilter', 'attribute_description_filter_example'),
                    ('attributeNameFilter', 'attribute_name_filter_example'),
                    ('attributeType', 'attribute_type_example'),
                    ('elementCategory', 'element_category_example'),
                    ('elementDescriptionFilter', 'element_description_filter_example'),
                    ('elementNameFilter', 'element_name_filter_example'),
                    ('elementTemplate', 'element_template_example'),
                    ('elementType', 'element_type_example'),
                    ('maxCount', 56),
                    ('searchFullHierarchy', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('startIndex', 56),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/elementattributes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_find_event_frame_attributes(client):
    """Test case for asset_database_find_event_frame_attributes

    Retrieves a list of event frame attributes matching the specified filters from the specified asset database.
    """
    params = [('associations', 'associations_example'),
                    ('attributeCategory', 'attribute_category_example'),
                    ('attributeDescriptionFilter', 'attribute_description_filter_example'),
                    ('attributeNameFilter', 'attribute_name_filter_example'),
                    ('attributeType', 'attribute_type_example'),
                    ('endTime', 'end_time_example'),
                    ('eventFrameCategory', 'event_frame_category_example'),
                    ('eventFrameDescriptionFilter', 'event_frame_description_filter_example'),
                    ('eventFrameNameFilter', 'event_frame_name_filter_example'),
                    ('eventFrameTemplate', 'event_frame_template_example'),
                    ('maxCount', 56),
                    ('referencedElementNameFilter', 'referenced_element_name_filter_example'),
                    ('searchFullHierarchy', True),
                    ('searchMode', 'search_mode_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('startIndex', 56),
                    ('startTime', 'start_time_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/eventframeattributes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get(client):
    """Test case for asset_database_get

    Retrieve an Asset Database.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_analysis_categories(client):
    """Test case for asset_database_get_analysis_categories

    Retrieve analysis categories for a given Asset Database.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/analysiscategories'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_analysis_templates(client):
    """Test case for asset_database_get_analysis_templates

    Retrieve analysis templates based on the specified criteria. By default, all analysis templates in the specified Asset Database are returned.
    """
    params = [('field', ['_field_example']),
                    ('maxCount', 56),
                    ('query', 'query_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/analysistemplates'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_attribute_categories(client):
    """Test case for asset_database_get_attribute_categories

    Retrieve attribute categories for a given Asset Database.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/attributecategories'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_by_path(client):
    """Test case for asset_database_get_by_path

    Retrieve an Asset Database by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_element_categories(client):
    """Test case for asset_database_get_element_categories

    Retrieve element categories for a given Asset Database.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/elementcategories'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_element_templates(client):
    """Test case for asset_database_get_element_templates

    Retrieve element templates based on the specified criteria. Only templates of instance type \"Element\" and \"EventFrame\" are returned. By default, all element and event frame templates in the specified Asset Database are returned.
    """
    params = [('field', ['_field_example']),
                    ('maxCount', 56),
                    ('query', 'query_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/elementtemplates'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_elements(client):
    """Test case for asset_database_get_elements

    Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified asset database.
    """
    params = [('associations', 'associations_example'),
                    ('categoryName', 'category_name_example'),
                    ('descriptionFilter', 'description_filter_example'),
                    ('elementType', 'element_type_example'),
                    ('maxCount', 56),
                    ('nameFilter', 'name_filter_example'),
                    ('searchFullHierarchy', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('startIndex', 56),
                    ('templateName', 'template_name_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/elements'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_enumeration_sets(client):
    """Test case for asset_database_get_enumeration_sets

    Retrieve enumeration sets for given asset database.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/enumerationsets'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_event_frames(client):
    """Test case for asset_database_get_event_frames

    Retrieve event frames based on the specified conditions. By default, returns all children of the specified root resource that have been active in the past 8 hours.
    """
    params = [('canBeAcknowledged', True),
                    ('categoryName', 'category_name_example'),
                    ('endTime', 'end_time_example'),
                    ('isAcknowledged', True),
                    ('maxCount', 56),
                    ('nameFilter', 'name_filter_example'),
                    ('referencedElementNameFilter', 'referenced_element_name_filter_example'),
                    ('referencedElementTemplateName', 'referenced_element_template_name_example'),
                    ('searchFullHierarchy', True),
                    ('searchMode', 'search_mode_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('severity', ['severity_example']),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('startIndex', 56),
                    ('startTime', 'start_time_example'),
                    ('templateName', 'template_name_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/eventframes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_referenced_elements(client):
    """Test case for asset_database_get_referenced_elements

    Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements at the root level of the asset database.
    """
    params = [('associations', 'associations_example'),
                    ('categoryName', 'category_name_example'),
                    ('descriptionFilter', 'description_filter_example'),
                    ('elementType', 'element_type_example'),
                    ('maxCount', 56),
                    ('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('startIndex', 56),
                    ('templateName', 'template_name_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/referencedelements'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_security(client):
    """Test case for asset_database_get_security

    Get the security information of the specified security item associated with the asset database for a specified user.
    """
    params = [('securityItem', ['security_item_example']),
                    ('userIdentity', ['user_identity_example']),
                    ('forceRefresh', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/security'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_security_entries(client):
    """Test case for asset_database_get_security_entries

    Retrieve the security entries of the specified security item associated with the asset database based on the specified criteria. By default, all security entries for this asset database are returned.
    """
    params = [('nameFilter', 'name_filter_example'),
                    ('securityItem', 'security_item_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_security_entry_by_name(client):
    """Test case for asset_database_get_security_entry_by_name

    Retrieve the security entry of the specified security item associated with the asset database with the specified name.
    """
    params = [('securityItem', 'security_item_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_table_categories(client):
    """Test case for asset_database_get_table_categories

    Retrieve table categories for a given Asset Database.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/tablecategories'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_get_tables(client):
    """Test case for asset_database_get_tables

    Retrieve tables for given Asset Database.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetdatabases/{web_id}/tables'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_import(client):
    """Test case for asset_database_import

    Import an asset database.
    """
    params = [('importMode', ['import_mode_example'])]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetdatabases/{web_id}/import'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_database_remove_referenced_element(client):
    """Test case for asset_database_remove_referenced_element

    Remove a reference to an existing element from the specified database.
    """
    params = [('referencedElementWebId', ['referenced_element_web_id_example'])]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/assetdatabases/{web_id}/referencedelements'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_database_update(client):
    """Test case for asset_database_update

    Update an asset database by replacing items in its definition.
    """
    database = {"Path":"\\\\MyAssetServer\\MyDatabase","Description":"PI BI Project Asset Model","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1RDDqD5loBNH0erqeqJodtALAquulo6433EKdHra7fsmL0g","Links":{"ElementTemplates":"ElementTemplates","AnalysisTemplates":"AnalysisTemplates","ElementCategories":"ElementCategories","Self":"Self","Elements":"Elements","Security":"Security","AssetServer":"AssetServer","EnumerationSets":"EnumerationSets","SecurityEntries":"SecurityEntries","AnalysisCategories":"AnalysisCategories","EventFrames":"EventFrames","Tables":"Tables","TableCategories":"TableCategories","AttributeCategories":"AttributeCategories"},"Id":"a3a5ebaa-37ae-42dc-9d1e-b6bb7ec98bd2","ExtendedProperties":{"key":{"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Exception":{"Errors":["An error has occurred."]}}},"Name":"MyDatabase"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/assetdatabases/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=database,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_database_update_security_entry(client):
    """Test case for asset_database_update_security_entry

    Update a security entry owned by the asset database.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True),
                    ('securityItem', 'security_item_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/piwebapi/assetdatabases/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

