# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asset_database import AssetDatabase
from openapi_server.models.asset_server import AssetServer
from openapi_server.models.errors import Errors
from openapi_server.models.items_analysis_rule_plug_in import ItemsAnalysisRulePlugIn
from openapi_server.models.items_asset_database import ItemsAssetDatabase
from openapi_server.models.items_asset_server import ItemsAssetServer
from openapi_server.models.items_notification_contact_template import ItemsNotificationContactTemplate
from openapi_server.models.items_notification_plug_in import ItemsNotificationPlugIn
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_identity import ItemsSecurityIdentity
from openapi_server.models.items_security_mapping import ItemsSecurityMapping
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.items_time_rule_plug_in import ItemsTimeRulePlugIn
from openapi_server.models.items_unit_class import ItemsUnitClass
from openapi_server.models.notification_contact_template import NotificationContactTemplate
from openapi_server.models.security_entry import SecurityEntry
from openapi_server.models.security_identity import SecurityIdentity
from openapi_server.models.security_mapping import SecurityMapping
from openapi_server.models.unit_class import UnitClass


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_server_create_asset_database(client):
    """Test case for asset_server_create_asset_database

    Create an asset database.
    """
    database = {"Path":"\\\\MyAssetServer\\MyDatabase","Description":"PI BI Project Asset Model","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1RDDqD5loBNH0erqeqJodtALAquulo6433EKdHra7fsmL0g","Links":{"ElementTemplates":"ElementTemplates","AnalysisTemplates":"AnalysisTemplates","ElementCategories":"ElementCategories","Self":"Self","Elements":"Elements","Security":"Security","AssetServer":"AssetServer","EnumerationSets":"EnumerationSets","SecurityEntries":"SecurityEntries","AnalysisCategories":"AnalysisCategories","EventFrames":"EventFrames","Tables":"Tables","TableCategories":"TableCategories","AttributeCategories":"AttributeCategories"},"Id":"a3a5ebaa-37ae-42dc-9d1e-b6bb7ec98bd2","ExtendedProperties":{"key":{"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Exception":{"Errors":["An error has occurred."]}}},"Name":"MyDatabase"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetservers/{web_id}/assetdatabases'.format(web_id='web_id_example'),
        headers=headers,
        json=database,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_server_create_notification_contact_template(client):
    """Test case for asset_server_create_notification_contact_template

    Create a notification contact template.
    """
    notification_contact_template = {"Path":"\\\\MyAssetServer\\NotificationContactTemplates[Plant Manager]","ConfigString":"","NotifyWhenInstanceEnded":True,"ContactType":"Individual","Description":"","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"MaximumRetries":5,"Name":"Plant Manager","HasChildren":False,"EscalationTimeout":"PT3S","WebId":"I1NCEDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBAGyPedZG1sUmxOOclp3Flwg","MinimumAcknowledgements":2,"Links":{"SecurityEntries":"SecurityEntries","NotificationPlugIn":"NotificationPlugIn","NotificationContactTemplates":"NotificationContactTemplates","Self":"Self","Security":"Security","AssetServer":"AssetServer"},"Available":True,"Id":"cbb28260-853d-11e4-80c5-00155d844304","RetryInterval":"PT5S","PlugInName":""}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetservers/{web_id}/notificationcontacttemplates'.format(web_id='web_id_example'),
        headers=headers,
        json=notification_contact_template,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_server_create_security_entry(client):
    """Test case for asset_server_create_security_entry

    Create a security entry owned by the asset server.
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
        path='/piwebapi/assetservers/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_server_create_security_identity(client):
    """Test case for asset_server_create_security_identity

    Create a security identity.
    """
    security_identity = {"Path":"\\\\MyAssetServer\\SecurityIdentities[MySecurityIdentity]","Description":"","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"IsEnabled":True,"WebId":"I1SIDqD5loBNH0erqeqJodtALASe6l8zgYokqdeeFilFI9tw","Links":{"SecurityEntries":"SecurityEntries","SecurityMappings":"SecurityMappings","Self":"Self","Security":"Security","AssetServer":"AssetServer"},"Id":"f3a5ee49-1838-4aa2-9d79-e16294523db7","Name":"MySecurityIdentity"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetservers/{web_id}/securityidentities'.format(web_id='web_id_example'),
        headers=headers,
        json=security_identity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_server_create_security_mapping(client):
    """Test case for asset_server_create_security_mapping

    Create a security mapping.
    """
    security_mapping = {"Path":"\\\\MyAssetServer\\SecurityMappings[MySecurityMapping]","Account":"domain\\user","Description":"","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1SMDqD5loBNH0erqeqJodtALAgu8UrMAZB0qWp9H7C4TAXQ","SecurityIdentityWebId":"I1SIEDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBAGyPedZG1sUmxOOclp3Flwg","Links":{"SecurityIdentity":"SecurityIdentity","SecurityEntries":"SecurityEntries","Self":"Self","Security":"Security","AssetServer":"AssetServer"},"Id":"ac14ef82-19c0-4a07-96a7-d1fb0b84c05d","Name":"MySecurityMapping"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetservers/{web_id}/securitymappings'.format(web_id='web_id_example'),
        headers=headers,
        json=security_mapping,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_server_create_unit_class(client):
    """Test case for asset_server_create_unit_class

    Create a unit class in the specified Asset Server.
    """
    unit_class = {"Path":"\\\\MyAssetServer\\UOMDatabase\\UOMClasses[Power]","Description":"Power Unit Class","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"CanonicalUnitAbbreviation":"W","WebId":"I1UCDqD5loBNH0erqeqJodtALATbkl-fxulEulDQAVw5HySQ","Links":{"CanonicalUnit":"CanonicalUnit","Self":"Self","AssetServer":"AssetServer","Units":"Units"},"Id":"f925b94d-6efc-4b94-a50d-0015c391f249","CanonicalUnitName":"watt","Name":"Power"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/assetservers/{web_id}/unitclasses'.format(web_id='web_id_example'),
        headers=headers,
        json=unit_class,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_delete_security_entry(client):
    """Test case for asset_server_delete_security_entry

    Delete a security entry owned by the asset server.
    """
    params = [('applyToChildren', True),
                    ('securityItem', 'security_item_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/assetservers/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get(client):
    """Test case for asset_server_get

    Retrieve an Asset Server.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetservers/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get_analysis_rule_plug_ins(client):
    """Test case for asset_server_get_analysis_rule_plug_ins

    Retrieve a list of all Analysis Rule Plug-in's.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetservers/{web_id}/analysisruleplugins'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get_by_name(client):
    """Test case for asset_server_get_by_name

    Retrieve an Asset Server by name.
    """
    params = [('name', 'name_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetservers#name',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get_by_path(client):
    """Test case for asset_server_get_by_path

    Retrieve an Asset Server by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetservers#path',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get_databases(client):
    """Test case for asset_server_get_databases

    Retrieve a list of all Asset Databases on the specified Asset Server.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetservers/{web_id}/assetdatabases'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get_notification_contact_templates(client):
    """Test case for asset_server_get_notification_contact_templates

    Retrieve a list of all notification contact templates on the specified Asset Server.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetservers/{web_id}/notificationcontacttemplates'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get_notification_plug_ins(client):
    """Test case for asset_server_get_notification_plug_ins

    Retrieve a list of all notification plugins on the specified Asset Server.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetservers/{web_id}/notificationplugins'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get_security(client):
    """Test case for asset_server_get_security

    Get the security information of the specified security item associated with the asset server for a specified user.
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
        path='/piwebapi/assetservers/{web_id}/security'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get_security_entries(client):
    """Test case for asset_server_get_security_entries

    Retrieve the security entries of the specified security item associated with the asset server based on the specified criteria. By default, all security entries for this asset server are returned.
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
        path='/piwebapi/assetservers/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get_security_entry_by_name(client):
    """Test case for asset_server_get_security_entry_by_name

    Retrieve the security entry of the specified security item associated with the asset server with the specified name.
    """
    params = [('securityItem', 'security_item_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetservers/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get_security_identities(client):
    """Test case for asset_server_get_security_identities

    Retrieve security identities based on the specified criteria. By default, all security identities in the specified Asset Server are returned.
    """
    params = [('field', '_field_example'),
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
        path='/piwebapi/assetservers/{web_id}/securityidentities'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get_security_identities_for_user(client):
    """Test case for asset_server_get_security_identities_for_user

    Retrieve security identities for a specific user.
    """
    params = [('userIdentity', 'user_identity_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetservers/{web_id}/securityidentities#userIdentity'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get_security_mappings(client):
    """Test case for asset_server_get_security_mappings

    Retrieve security mappings based on the specified criteria. By default, all security mappings in the specified Asset Server are returned.
    """
    params = [('field', '_field_example'),
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
        path='/piwebapi/assetservers/{web_id}/securitymappings'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get_time_rule_plug_ins(client):
    """Test case for asset_server_get_time_rule_plug_ins

    Retrieve a list of all Time Rule Plug-in's.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetservers/{web_id}/timeruleplugins'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_get_unit_classes(client):
    """Test case for asset_server_get_unit_classes

    Retrieve a list of all unit classes on the specified Asset Server.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetservers/{web_id}/unitclasses'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_server_list(client):
    """Test case for asset_server_list

    Retrieve a list of all Asset Servers known to this service.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/assetservers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_asset_server_update_security_entry(client):
    """Test case for asset_server_update_security_entry

    Update a security entry owned by the asset server.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True),
                    ('securityItem', 'security_item_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/piwebapi/assetservers/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

