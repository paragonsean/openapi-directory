# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analysis import Analysis
from openapi_server.models.attribute import Attribute
from openapi_server.models.element import Element
from openapi_server.models.errors import Errors
from openapi_server.models.items_analysis import ItemsAnalysis
from openapi_server.models.items_attribute import ItemsAttribute
from openapi_server.models.items_element import ItemsElement
from openapi_server.models.items_element_category import ItemsElementCategory
from openapi_server.models.items_event_frame import ItemsEventFrame
from openapi_server.models.items_item_element import ItemsItemElement
from openapi_server.models.items_notification_rule import ItemsNotificationRule
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.items_string import ItemsString
from openapi_server.models.notification_rule import NotificationRule
from openapi_server.models.search_by_attribute import SearchByAttribute
from openapi_server.models.security_entry import SecurityEntry


pytestmark = pytest.mark.asyncio

async def test_element_add_referenced_element(client):
    """Test case for element_add_referenced_element

    Add a reference to an existing element to the child elements collection.
    """
    params = [('referencedElementWebId', ['referenced_element_web_id_example']),
                    ('referenceType', 'reference_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/elements/{web_id}/referencedelements'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_element_create_analysis(client):
    """Test case for element_create_analysis

    Create an Analysis.
    """
    analysis = {"Path":"\\\\MyAssetServer\\MyDatabase\\MyElement\\Analyses[MyAnalysis]","Status":"Disabled","IsTimeRuleDefinedByTemplate":False,"Description":"","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"HasNotification":False,"Priority":"High","HasTarget":True,"OutputTime":"","HasTemplate":False,"PublishResults":False,"GroupId":0,"Name":"MyAnalysis","TargetWebId":"I1ETDqD5loBNH0erqeqJodtALAjFPVfUpY-02A8uioGDSgIg","CategoryNames":["MyAnalysisCategory"],"AutoCreated":False,"AnalysisRulePlugInName":"PerformanceEquation","TimeRulePlugInName":"Periodic","WebId":"I1XsDqD5loBNH0erqeqJodtALAWDOFEb-U5xGEQwAVXYTCAA","Links":{"SecurityEntries":"SecurityEntries","Target":"Target","TimeRulePlugIn":"TimeRulePlugIn","Categories":"Categories","Database":"Database","Self":"Self","Security":"Security","AnalysisRule":"AnalysisRule","TimeRule":"TimeRule","AnalysisRulePlugIn":"AnalysisRulePlugIn","Template":"Template"},"TemplateName":"","Id":"11853358-94bf-11e7-8443-00155d84c200","MaximumQueueSize":0,"IsConfigured":False}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/elements/{web_id}/analyses'.format(web_id='web_id_example'),
        headers=headers,
        json=analysis,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_element_create_attribute(client):
    """Test case for element_create_attribute

    Create a new attribute of the specified element.
    """
    attribute = {"Description":"2008 Water Use","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"DefaultUnitsNameAbbreviation":"L","Step":False,"Span":100.0,"Name":"Water","IsExcluded":False,"CategoryNames":["Energy Savings Targets"],"IsConfigurationItem":False,"WebId":"I1AbEDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBAGyPedZG1sUmxOOclp3Flwg","Paths":["\\\\MyAssetServer\\MyDatabase\\MyElement|MyAttribute","\\\\MyAssetServer\\MyDatabase\\ReferencingElement\\MyElement|MyAttribute"],"IsManualDataEntry":False,"Path":"\\\\MyAssetServer\\MyDatabase\\CityName\\EngineeringProcess\\Equipment\\MachineName|Water(2008)","ConfigString":"SELECT [Water Use] FROM [Energy Use 2008] WHERE [Asset ID] = '%Element%'","IsHidden":False,"Zero":0.0,"DefaultUnitsName":"liter","DisplayDigits":-5,"HasChildren":False,"TraitName":"LimitLoLo","Type":"Int32","Links":{"PlotData":"PlotData","EnumerationSet":"EnumerationSet","Categories":"Categories","Parent":"Parent","Element":"Element","Attributes":"Attributes","Point":"Point","Self":"Self","EventFrame":"EventFrame","Template":"Template","SummaryData":"SummaryData","Value":"Value","EndValue":"EndValue","Trait":"Trait","InterpolatedData":"InterpolatedData","EnumerationValues":"EnumerationValues","RecordedData":"RecordedData"},"Id":"75de231b-b591-49b1-b138-e725a77165c2","DataReferencePlugIn":"Table Lookup","TypeQualifier":"","DataReference":{"Type":"PI Point","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"PIPoint":{"Path":"\\\\MyPIServer\\PointName","Zero":0.0,"DisplayDigits":-5,"Step":False,"Span":100.0,"Name":"PointName","PointClass":"classic","WebId":"I1DPa70Wf0zBA06CLkV9ovNQgQCAAAAA","Descriptor":"12 Hour Sine Wave","Future":False,"PointType":"Float32","Id":82,"DigitalSetName":"","EngineeringUnits":""}}}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/elements/{web_id}/attributes'.format(web_id='web_id_example'),
        headers=headers,
        json=attribute,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_create_config(client):
    """Test case for element_create_config

    Executes the create configuration function of the data references found within the attributes of the element, and optionally, its children.
    """
    params = [('includeChildElements', True)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/elements/{web_id}/config'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_element_create_element(client):
    """Test case for element_create_element

    Create a child element.
    """
    element = {"Path":"\\\\MyAssetServer\\MyDatabase\\CityName\\EngineeringProcess\\Equipment\\MachineName","Description":"Manufacturing Equipment MachineName","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"ExtendedProperties":{"key":{"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Exception":{"Errors":["An error has occurred."]}}},"Name":"MachineName","Errors":[{"Message":["An error has occurred."],"FieldName":"Value"},{"Message":["An error has occurred."],"FieldName":"Value"}],"HasChildren":False,"CategoryNames":["Equipment Assets"],"WebId":"I1EmDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBA","Links":{"PlotData":"PlotData","Categories":"Categories","Parent":"Parent","Attributes":"Attributes","Analyses":"Analyses","Self":"Self","Elements":"Elements","Security":"Security","Template":"Template","SecurityEntries":"SecurityEntries","NotificationRules":"NotificationRules","Database":"Database","SummaryData":"SummaryData","Value":"Value","EventFrames":"EventFrames","EndValue":"EndValue","DefaultAttribute":"DefaultAttribute","InterpolatedData":"InterpolatedData","RecordedData":"RecordedData"},"TemplateName":"MachineName","Id":"cbb28260-853d-11e4-80c5-00155d844304","Paths":["Paths","Paths"]}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/elements/{web_id}/elements'.format(web_id='web_id_example'),
        headers=headers,
        json=element,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_element_create_notification_rule(client):
    """Test case for element_create_notification_rule

    Create a notification rule.
    """
    notification_rule = {"Path":"\\\\MyAssetServer\\MyDatabase\\CityName\\EngineeringProcess\\Equipment\\MachineName\\NotificationRules[RuleName]","Status":"Disabled","MultiTriggerEventOption":"HighestSeverity","Description":"Manufacturing Equipment MachineName","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"ResendInterval":"PT5S","Criteria":"Name: EventFrameCriteriaName","Name":"MachineName","CategoryNames":["Equipment Assets"],"AutoCreated":True,"WebId":"I1NRDqD5loBNH0erqeqJodtALA5bYfWno26BGgMQAVXYR0Ag","TemplateName":"MachineName Notification Rule","Id":"e9a984d0-f47c-11e7-8454-00155d029708","NonrepetitionInterval":"PT3S"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/elements/{web_id}/notificationrules'.format(web_id='web_id_example'),
        headers=headers,
        json=notification_rule,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_element_create_search_by_attribute(client):
    """Test case for element_create_search_by_attribute

    Create a link for a \"Search Elements By Attribute Value\" operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root Element. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the Elements. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators.
    """
    query = {"SearchRoot":"I1RDDqD5loBNH0erqeqJodtALA8fbgUnyQW02v-gLGIxumSg","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"ValueQueries":[{"AttributeValue":12.3,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AttributeUOM":"pound-force per square inch","SearchOperator":"LessThan","AttributeName":"Pressure"},{"AttributeValue":12.3,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AttributeUOM":"pound-force per square inch","SearchOperator":"LessThan","AttributeName":"Pressure"}],"ElementTemplate":"I1ETDqD5loBNH0erqeqJodtALAjFPVfUpY-02A8uioGDSgIg"}
    params = [('associations', 'associations_example'),
                    ('noResults', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/elements/searchbyattribute',
        headers=headers,
        json=query,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_element_create_security_entry(client):
    """Test case for element_create_security_entry

    Create a security entry owned by the element.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/elements/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_delete(client):
    """Test case for element_delete

    Delete an element.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/elements/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_delete_security_entry(client):
    """Test case for element_delete_security_entry

    Delete a security entry owned by the element.
    """
    params = [('applyToChildren', True)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/elements/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_execute_search_by_attribute(client):
    """Test case for element_execute_search_by_attribute

    Execute a \"Search Elements By Attribute Value\" operation.
    """
    params = [('associations', 'associations_example'),
                    ('categoryName', 'category_name_example'),
                    ('descriptionFilter', 'description_filter_example'),
                    ('maxCount', 56),
                    ('nameFilter', 'name_filter_example'),
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
        path='/piwebapi/elements/searchbyattribute/{search_id}'.format(search_id='search_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_find_element_attributes(client):
    """Test case for element_find_element_attributes

    Retrieves a list of element attributes matching the specified filters from the specified element.
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
        path='/piwebapi/elements/{web_id}/elementattributes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get(client):
    """Test case for element_get

    Retrieve an element.
    """
    params = [('associations', 'associations_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elements/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get_analyses(client):
    """Test case for element_get_analyses

    Retrieve analyses based on the specified conditions.
    """
    params = [('maxCount', 56),
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
        path='/piwebapi/elements/{web_id}/analyses'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get_attributes(client):
    """Test case for element_get_attributes

    Get the attributes of the specified element.
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
        path='/piwebapi/elements/{web_id}/attributes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get_by_path(client):
    """Test case for element_get_by_path

    Retrieve an element by path.
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
        path='/piwebapi/elements',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get_categories(client):
    """Test case for element_get_categories

    Get an element's categories.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elements/{web_id}/categories'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get_elements(client):
    """Test case for element_get_elements

    Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified element.
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
        path='/piwebapi/elements/{web_id}/elements'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get_elements_query(client):
    """Test case for element_get_elements_query

    Retrieve elements based on the specified conditions. By default, returns all the elements.
    """
    params = [('associations', 'associations_example'),
                    ('databaseWebId', 'database_web_id_example'),
                    ('maxCount', 56),
                    ('query', 'query_example'),
                    ('queryDate', 'query_date_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('startIndex', 56),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elements/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get_event_frames(client):
    """Test case for element_get_event_frames

    Retrieve event frames that reference this element based on the specified conditions. By default, returns all event frames that reference this element that have been active in the past 8 hours.
    """
    params = [('canBeAcknowledged', True),
                    ('categoryName', 'category_name_example'),
                    ('endTime', 'end_time_example'),
                    ('isAcknowledged', True),
                    ('maxCount', 56),
                    ('nameFilter', 'name_filter_example'),
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
        path='/piwebapi/elements/{web_id}/eventframes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get_multiple(client):
    """Test case for element_get_multiple

    Retrieve multiple elements by web id or path.
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
        path='/piwebapi/elements/multiple',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get_notification_rules(client):
    """Test case for element_get_notification_rules

    Retrieve notification rules for an element
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elements/{web_id}/notificationrules'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get_paths(client):
    """Test case for element_get_paths

    Get a list of the full or relative paths to this element.
    """
    params = [('relativePath', 'relative_path_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elements/{web_id}/paths'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get_referenced_elements(client):
    """Test case for element_get_referenced_elements

    Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements of the current resource.
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
        path='/piwebapi/elements/{web_id}/referencedelements'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get_security(client):
    """Test case for element_get_security

    Get the security information of the specified security item associated with the element for a specified user.
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
        path='/piwebapi/elements/{web_id}/security'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get_security_entries(client):
    """Test case for element_get_security_entries

    Retrieve the security entries associated with the element based on the specified criteria. By default, all security entries for this element are returned.
    """
    params = [('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elements/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_get_security_entry_by_name(client):
    """Test case for element_get_security_entry_by_name

    Retrieve the security entry associated with the element with the specified name.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/elements/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_element_remove_referenced_element(client):
    """Test case for element_remove_referenced_element

    Remove a reference to an existing element from the child elements collection.
    """
    params = [('referencedElementWebId', ['referenced_element_web_id_example'])]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/elements/{web_id}/referencedelements'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_element_update(client):
    """Test case for element_update

    Update an element by replacing items in its definition.
    """
    element = {"Path":"\\\\MyAssetServer\\MyDatabase\\CityName\\EngineeringProcess\\Equipment\\MachineName","Description":"Manufacturing Equipment MachineName","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"ExtendedProperties":{"key":{"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Exception":{"Errors":["An error has occurred."]}}},"Name":"MachineName","Errors":[{"Message":["An error has occurred."],"FieldName":"Value"},{"Message":["An error has occurred."],"FieldName":"Value"}],"HasChildren":False,"CategoryNames":["Equipment Assets"],"WebId":"I1EmDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBA","Links":{"PlotData":"PlotData","Categories":"Categories","Parent":"Parent","Attributes":"Attributes","Analyses":"Analyses","Self":"Self","Elements":"Elements","Security":"Security","Template":"Template","SecurityEntries":"SecurityEntries","NotificationRules":"NotificationRules","Database":"Database","SummaryData":"SummaryData","Value":"Value","EventFrames":"EventFrames","EndValue":"EndValue","DefaultAttribute":"DefaultAttribute","InterpolatedData":"InterpolatedData","RecordedData":"RecordedData"},"TemplateName":"MachineName","Id":"cbb28260-853d-11e4-80c5-00155d844304","Paths":["Paths","Paths"]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/elements/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=element,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_element_update_security_entry(client):
    """Test case for element_update_security_entry

    Update a security entry owned by the element.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True)]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/piwebapi/elements/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

