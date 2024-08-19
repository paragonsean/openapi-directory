# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.annotation import Annotation
from openapi_server.models.attribute import Attribute
from openapi_server.models.errors import Errors
from openapi_server.models.event_frame import EventFrame
from openapi_server.models.items_annotation import ItemsAnnotation
from openapi_server.models.items_attribute import ItemsAttribute
from openapi_server.models.items_element import ItemsElement
from openapi_server.models.items_element_category import ItemsElementCategory
from openapi_server.models.items_event_frame import ItemsEventFrame
from openapi_server.models.items_item_event_frame import ItemsItemEventFrame
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.media_metadata import MediaMetadata
from openapi_server.models.search_by_attribute import SearchByAttribute
from openapi_server.models.security_entry import SecurityEntry


pytestmark = pytest.mark.asyncio

async def test_event_frame_acknowledge(client):
    """Test case for event_frame_acknowledge

    Calls the EventFrame's Acknowledge method.
    """
    headers = { 
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/eventframes/{web_id}/acknowledge'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_capture_values(client):
    """Test case for event_frame_capture_values

    Calls the EventFrame's CaptureValues method.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/eventframes/{web_id}/attributes/capture'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_event_frame_create_annotation(client):
    """Test case for event_frame_create_annotation

    Create an annotation on an event frame.
    """
    annotation = {"CreationDate":"2016-06-21T14:45:50.2988321Z","Errors":[{"Message":["An error has occurred."],"FieldName":"Value"},{"Message":["An error has occurred."],"FieldName":"Value"}],"Description":"Signifies a spike in temperature.","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"ModifyDate":"2016-06-21T14:45:50.2988321Z","Value":"The temperature spiked because of a malfunction with a unit in our west plant.","Links":{"MediaData":"MediaData","Owner":"Owner","MediaMetadata":"MediaMetadata","Self":"Self"},"Creator":"MyDomain\\UserA","Id":"512b6616-ce39-4f70-9048-8c6a025fb592","Modifier":"MyDomain\\UserA","Name":"Temperature Annotation"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/eventframes/{web_id}/annotations'.format(web_id='web_id_example'),
        headers=headers,
        json=annotation,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_event_frame_create_attribute(client):
    """Test case for event_frame_create_attribute

    Create a new attribute of the specified event frame.
    """
    attribute = {"Description":"2008 Water Use","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"DefaultUnitsNameAbbreviation":"L","Step":False,"Span":100.0,"Name":"Water","IsExcluded":False,"CategoryNames":["Energy Savings Targets"],"IsConfigurationItem":False,"WebId":"I1AbEDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBAGyPedZG1sUmxOOclp3Flwg","Paths":["\\\\MyAssetServer\\MyDatabase\\MyElement|MyAttribute","\\\\MyAssetServer\\MyDatabase\\ReferencingElement\\MyElement|MyAttribute"],"IsManualDataEntry":False,"Path":"\\\\MyAssetServer\\MyDatabase\\CityName\\EngineeringProcess\\Equipment\\MachineName|Water(2008)","ConfigString":"SELECT [Water Use] FROM [Energy Use 2008] WHERE [Asset ID] = '%Element%'","IsHidden":False,"Zero":0.0,"DefaultUnitsName":"liter","DisplayDigits":-5,"HasChildren":False,"TraitName":"LimitLoLo","Type":"Int32","Links":{"PlotData":"PlotData","EnumerationSet":"EnumerationSet","Categories":"Categories","Parent":"Parent","Element":"Element","Attributes":"Attributes","Point":"Point","Self":"Self","EventFrame":"EventFrame","Template":"Template","SummaryData":"SummaryData","Value":"Value","EndValue":"EndValue","Trait":"Trait","InterpolatedData":"InterpolatedData","EnumerationValues":"EnumerationValues","RecordedData":"RecordedData"},"Id":"75de231b-b591-49b1-b138-e725a77165c2","DataReferencePlugIn":"Table Lookup","TypeQualifier":"","DataReference":{"Type":"PI Point","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"PIPoint":{"Path":"\\\\MyPIServer\\PointName","Zero":0.0,"DisplayDigits":-5,"Step":False,"Span":100.0,"Name":"PointName","PointClass":"classic","WebId":"I1DPa70Wf0zBA06CLkV9ovNQgQCAAAAA","Descriptor":"12 Hour Sine Wave","Future":False,"PointType":"Float32","Id":82,"DigitalSetName":"","EngineeringUnits":""}}}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/eventframes/{web_id}/attributes'.format(web_id='web_id_example'),
        headers=headers,
        json=attribute,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_create_config(client):
    """Test case for event_frame_create_config

    Executes the create configuration function of the data references found within the attributes of the event frame, and optionally, its children.
    """
    params = [('includeChildElements', True)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/eventframes/{web_id}/config'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_event_frame_create_event_frame(client):
    """Test case for event_frame_create_event_frame

    Create an event frame as a child of the specified event frame.
    """
    event_frame = {"IsAcknowledged":True,"Path":"\\\\MyAssetServer\\MyDatabase\\EventFrames[EF20140725-001]","CanBeAcknowledged":True,"AcknowledgedBy":"MyDomain\\UserA","Description":"Event Frame of Past Week","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"EndTime":"2014-07-25T14:45:29Z","StartTime":"2014-07-18T14:45:29Z","IsLocked":False,"Severity":"None","Security":{"CanWrite":True,"Rights":["Read","WriteData"],"CanReadData":True,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"HasAdmin":True,"CanWriteData":True,"CanDelete":True,"CanRead":True,"CanAnnotate":True,"CanExecute":True,"CanSubscribe":True,"CanSubscribeOthers":True},"ExtendedProperties":{"key":{"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Exception":{"Errors":["An error has occurred."]}}},"Name":"EF20140725-001","IsAnnotated":False,"AcknowledgedDate":"2014-07-30T11:04:23Z","HasChildren":False,"CategoryNames":["Processing Plant"],"AreValuesCaptured":False,"WebId":"I1FmDqD5loBNH0erqeqJodtALADqD5loBNH0cAAAAAAASwAg","Links":{"PlotData":"PlotData","PrimaryReferencedElement":"PrimaryReferencedElement","Categories":"Categories","Parent":"Parent","Attributes":"Attributes","ReferencedElements":"ReferencedElements","Self":"Self","Security":"Security","Template":"Template","SecurityEntries":"SecurityEntries","Annotations":"Annotations","Database":"Database","SummaryData":"SummaryData","Value":"Value","EventFrames":"EventFrames","EndValue":"EndValue","DefaultAttribute":"DefaultAttribute","InterpolatedData":"InterpolatedData","RecordedData":"RecordedData"},"TemplateName":"Template","Id":"96f9a00e-4d80-471f-0000-00000004b002","RefElementWebIds":["I1EmDqD5loBNH0erqeqJodtALAaqQoQHk26BGgMQAVXYR0Ag"]}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/eventframes/{web_id}/eventframes'.format(web_id='web_id_example'),
        headers=headers,
        json=event_frame,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_event_frame_create_search_by_attribute(client):
    """Test case for event_frame_create_search_by_attribute

    Create a link for a \"Search EventFrames By Attribute Value\" operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root EventFrame. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the EventFrames. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators.
    """
    query = {"SearchRoot":"I1RDDqD5loBNH0erqeqJodtALA8fbgUnyQW02v-gLGIxumSg","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"ValueQueries":[{"AttributeValue":12.3,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AttributeUOM":"pound-force per square inch","SearchOperator":"LessThan","AttributeName":"Pressure"},{"AttributeValue":12.3,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AttributeUOM":"pound-force per square inch","SearchOperator":"LessThan","AttributeName":"Pressure"}],"ElementTemplate":"I1ETDqD5loBNH0erqeqJodtALAjFPVfUpY-02A8uioGDSgIg"}
    params = [('noResults', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/eventframes/searchbyattribute',
        headers=headers,
        json=query,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_event_frame_create_security_entry(client):
    """Test case for event_frame_create_security_entry

    Create a security entry owned by the event frame.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/eventframes/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_delete(client):
    """Test case for event_frame_delete

    Delete an event frame.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/eventframes/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_delete_annotation(client):
    """Test case for event_frame_delete_annotation

    Delete an annotation on an event frame. If the annotation has attached media, the attached media will also be deleted.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/eventframes/{web_id}/annotations/{id}'.format(id='id_example', web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_delete_annotation_attachment_media_by_id(client):
    """Test case for event_frame_delete_annotation_attachment_media_by_id

    Delete attached media from an annotation on an event frame.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/eventframes/{web_id}/annotations/{id}/attachment/media'.format(id='id_example', web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_delete_security_entry(client):
    """Test case for event_frame_delete_security_entry

    Delete a security entry owned by the event frame.
    """
    params = [('applyToChildren', True)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/eventframes/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_execute_search_by_attribute(client):
    """Test case for event_frame_execute_search_by_attribute

    Execute a \"Search EventFrames By Attribute Value\" operation.
    """
    params = [('canBeAcknowledged', True),
                    ('endTime', 'end_time_example'),
                    ('isAcknowledged', True),
                    ('maxCount', 56),
                    ('nameFilter', 'name_filter_example'),
                    ('referencedElementNameFilter', 'referenced_element_name_filter_example'),
                    ('searchFullHierarchy', True),
                    ('searchMode', 'search_mode_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('severity', ['severity_example']),
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
        path='/piwebapi/eventframes/searchbyattribute/{search_id}'.format(search_id='search_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_find_event_frame_attributes(client):
    """Test case for event_frame_find_event_frame_attributes

    Retrieves a list of event frame attributes matching the specified filters from the specified event frame.
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
        path='/piwebapi/eventframes/{web_id}/eventframeattributes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_get(client):
    """Test case for event_frame_get

    Retrieve an event frame.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/eventframes/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_get_annotation_attachment_media_metadata_by_id(client):
    """Test case for event_frame_get_annotation_attachment_media_metadata_by_id

    Gets the metadata of the media attached to the specified annotation.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/eventframes/{web_id}/annotations/{id}/attachment/media/metadata'.format(id='id_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_get_annotation_by_id(client):
    """Test case for event_frame_get_annotation_by_id

    Get a specific annotation on an event frame.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/eventframes/{web_id}/annotations/{id}'.format(id='id_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_get_annotations(client):
    """Test case for event_frame_get_annotations

    Get an event frame's annotations.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/eventframes/{web_id}/annotations'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_get_attributes(client):
    """Test case for event_frame_get_attributes

    Get the attributes of the specified event frame.
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
        path='/piwebapi/eventframes/{web_id}/attributes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_get_by_path(client):
    """Test case for event_frame_get_by_path

    Retrieve an event frame by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/eventframes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_get_categories(client):
    """Test case for event_frame_get_categories

    Get an event frame's categories.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/eventframes/{web_id}/categories'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_get_event_frames(client):
    """Test case for event_frame_get_event_frames

    Retrieve event frames based on the specified conditions. By default, returns all children of the specified root event frame that have been active in the past 8 hours.
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
        path='/piwebapi/eventframes/{web_id}/eventframes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_get_event_frames_query(client):
    """Test case for event_frame_get_event_frames_query

    Retrieve event frames based on the specified conditions. Returns event frames using the specified search query string.
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
        path='/piwebapi/eventframes/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_get_multiple(client):
    """Test case for event_frame_get_multiple

    Retrieve multiple event frames by web ids or paths.
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
        path='/piwebapi/eventframes/multiple',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_get_referenced_elements(client):
    """Test case for event_frame_get_referenced_elements

    Retrieve the event frame's referenced elements.
    """
    params = [('associations', 'associations_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/eventframes/{web_id}/referencedelements'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_get_security(client):
    """Test case for event_frame_get_security

    Get the security information of the specified security item associated with the event frame for a specified user.
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
        path='/piwebapi/eventframes/{web_id}/security'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_get_security_entries(client):
    """Test case for event_frame_get_security_entries

    Retrieve the security entries associated with the event frame based on the specified criteria. By default, all security entries for this event frame are returned.
    """
    params = [('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/eventframes/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_frame_get_security_entry_by_name(client):
    """Test case for event_frame_get_security_entry_by_name

    Retrieve the security entry associated with the event frame with the specified name.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/eventframes/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_event_frame_update(client):
    """Test case for event_frame_update

    Update an event frame by replacing items in its definition.
    """
    event_frame = {"IsAcknowledged":True,"Path":"\\\\MyAssetServer\\MyDatabase\\EventFrames[EF20140725-001]","CanBeAcknowledged":True,"AcknowledgedBy":"MyDomain\\UserA","Description":"Event Frame of Past Week","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"EndTime":"2014-07-25T14:45:29Z","StartTime":"2014-07-18T14:45:29Z","IsLocked":False,"Severity":"None","Security":{"CanWrite":True,"Rights":["Read","WriteData"],"CanReadData":True,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"HasAdmin":True,"CanWriteData":True,"CanDelete":True,"CanRead":True,"CanAnnotate":True,"CanExecute":True,"CanSubscribe":True,"CanSubscribeOthers":True},"ExtendedProperties":{"key":{"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Exception":{"Errors":["An error has occurred."]}}},"Name":"EF20140725-001","IsAnnotated":False,"AcknowledgedDate":"2014-07-30T11:04:23Z","HasChildren":False,"CategoryNames":["Processing Plant"],"AreValuesCaptured":False,"WebId":"I1FmDqD5loBNH0erqeqJodtALADqD5loBNH0cAAAAAAASwAg","Links":{"PlotData":"PlotData","PrimaryReferencedElement":"PrimaryReferencedElement","Categories":"Categories","Parent":"Parent","Attributes":"Attributes","ReferencedElements":"ReferencedElements","Self":"Self","Security":"Security","Template":"Template","SecurityEntries":"SecurityEntries","Annotations":"Annotations","Database":"Database","SummaryData":"SummaryData","Value":"Value","EventFrames":"EventFrames","EndValue":"EndValue","DefaultAttribute":"DefaultAttribute","InterpolatedData":"InterpolatedData","RecordedData":"RecordedData"},"TemplateName":"Template","Id":"96f9a00e-4d80-471f-0000-00000004b002","RefElementWebIds":["I1EmDqD5loBNH0erqeqJodtALAaqQoQHk26BGgMQAVXYR0Ag"]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/eventframes/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=event_frame,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_event_frame_update_annotation(client):
    """Test case for event_frame_update_annotation

    Update an annotation on an event frame by replacing items in its definition.
    """
    annotation = {"CreationDate":"2016-06-21T14:45:50.2988321Z","Errors":[{"Message":["An error has occurred."],"FieldName":"Value"},{"Message":["An error has occurred."],"FieldName":"Value"}],"Description":"Signifies a spike in temperature.","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"ModifyDate":"2016-06-21T14:45:50.2988321Z","Value":"The temperature spiked because of a malfunction with a unit in our west plant.","Links":{"MediaData":"MediaData","Owner":"Owner","MediaMetadata":"MediaMetadata","Self":"Self"},"Creator":"MyDomain\\UserA","Id":"512b6616-ce39-4f70-9048-8c6a025fb592","Modifier":"MyDomain\\UserA","Name":"Temperature Annotation"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/eventframes/{web_id}/annotations/{id}'.format(id='id_example', web_id='web_id_example'),
        headers=headers,
        json=annotation,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_event_frame_update_security_entry(client):
    """Test case for event_frame_update_security_entry

    Update a security entry owned by the event frame.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True)]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/piwebapi/eventframes/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

