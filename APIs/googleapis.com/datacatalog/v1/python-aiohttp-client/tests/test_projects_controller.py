# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_iam_policy_request import GetIamPolicyRequest
from openapi_server.models.google_cloud_datacatalog_v1_contacts import GoogleCloudDatacatalogV1Contacts
from openapi_server.models.google_cloud_datacatalog_v1_entry import GoogleCloudDatacatalogV1Entry
from openapi_server.models.google_cloud_datacatalog_v1_entry_group import GoogleCloudDatacatalogV1EntryGroup
from openapi_server.models.google_cloud_datacatalog_v1_entry_overview import GoogleCloudDatacatalogV1EntryOverview
from openapi_server.models.google_cloud_datacatalog_v1_export_taxonomies_response import GoogleCloudDatacatalogV1ExportTaxonomiesResponse
from openapi_server.models.google_cloud_datacatalog_v1_import_entries_request import GoogleCloudDatacatalogV1ImportEntriesRequest
from openapi_server.models.google_cloud_datacatalog_v1_import_taxonomies_request import GoogleCloudDatacatalogV1ImportTaxonomiesRequest
from openapi_server.models.google_cloud_datacatalog_v1_import_taxonomies_response import GoogleCloudDatacatalogV1ImportTaxonomiesResponse
from openapi_server.models.google_cloud_datacatalog_v1_list_entries_response import GoogleCloudDatacatalogV1ListEntriesResponse
from openapi_server.models.google_cloud_datacatalog_v1_list_entry_groups_response import GoogleCloudDatacatalogV1ListEntryGroupsResponse
from openapi_server.models.google_cloud_datacatalog_v1_list_policy_tags_response import GoogleCloudDatacatalogV1ListPolicyTagsResponse
from openapi_server.models.google_cloud_datacatalog_v1_list_tags_response import GoogleCloudDatacatalogV1ListTagsResponse
from openapi_server.models.google_cloud_datacatalog_v1_list_taxonomies_response import GoogleCloudDatacatalogV1ListTaxonomiesResponse
from openapi_server.models.google_cloud_datacatalog_v1_modify_entry_contacts_request import GoogleCloudDatacatalogV1ModifyEntryContactsRequest
from openapi_server.models.google_cloud_datacatalog_v1_modify_entry_overview_request import GoogleCloudDatacatalogV1ModifyEntryOverviewRequest
from openapi_server.models.google_cloud_datacatalog_v1_policy_tag import GoogleCloudDatacatalogV1PolicyTag
from openapi_server.models.google_cloud_datacatalog_v1_reconcile_tags_request import GoogleCloudDatacatalogV1ReconcileTagsRequest
from openapi_server.models.google_cloud_datacatalog_v1_rename_tag_template_field_enum_value_request import GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequest
from openapi_server.models.google_cloud_datacatalog_v1_replace_taxonomy_request import GoogleCloudDatacatalogV1ReplaceTaxonomyRequest
from openapi_server.models.google_cloud_datacatalog_v1_tag import GoogleCloudDatacatalogV1Tag
from openapi_server.models.google_cloud_datacatalog_v1_tag_template import GoogleCloudDatacatalogV1TagTemplate
from openapi_server.models.google_cloud_datacatalog_v1_tag_template_field import GoogleCloudDatacatalogV1TagTemplateField
from openapi_server.models.google_cloud_datacatalog_v1_taxonomy import GoogleCloudDatacatalogV1Taxonomy
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_entry_groups_create(client):
    """Test case for datacatalog_projects_locations_entry_groups_create

    
    """
    body = {"dataCatalogTimestamps":{"expireTime":"expireTime","createTime":"createTime","updateTime":"updateTime"},"displayName":"displayName","name":"name","description":"description"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('entryGroupId', 'entry_group_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/entryGroups'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_entry_groups_entries_create(client):
    """Test case for datacatalog_projects_locations_entry_groups_entries_create

    
    """
    body = {"databaseTableSpec":{"databaseViewSpec":{"sqlQuery":"sqlQuery","viewType":"VIEW_TYPE_UNSPECIFIED","baseTable":"baseTable"},"type":"TABLE_TYPE_UNSPECIFIED","dataplexTable":{"externalTables":[{"dataCatalogEntry":"dataCatalogEntry","system":"INTEGRATED_SYSTEM_UNSPECIFIED","googleCloudResource":"googleCloudResource","fullyQualifiedName":"fullyQualifiedName"},{"dataCatalogEntry":"dataCatalogEntry","system":"INTEGRATED_SYSTEM_UNSPECIFIED","googleCloudResource":"googleCloudResource","fullyQualifiedName":"fullyQualifiedName"}],"dataplexSpec":{"dataFormat":{"orc":"{}","protobuf":{"text":"text"},"csv":"{}","thrift":{"text":"text"},"avro":{"text":"text"},"parquet":"{}"},"compressionFormat":"compressionFormat","asset":"asset","projectId":"projectId"},"userManaged":True}},"schema":{"columns":[{"mode":"mode","highestIndexingType":"INDEXING_TYPE_UNSPECIFIED","gcRule":"gcRule","defaultValue":"defaultValue","lookerColumnSpec":{"type":"LOOKER_COLUMN_TYPE_UNSPECIFIED"},"column":"column","description":"description","ordinalPosition":0,"type":"type","rangeElementType":{"type":"type"},"subcolumns":[null,null]},{"mode":"mode","highestIndexingType":"INDEXING_TYPE_UNSPECIFIED","gcRule":"gcRule","defaultValue":"defaultValue","lookerColumnSpec":{"type":"LOOKER_COLUMN_TYPE_UNSPECIFIED"},"column":"column","description":"description","ordinalPosition":0,"type":"type","rangeElementType":{"type":"type"},"subcolumns":[null,null]}]},"sqlDatabaseSystemSpec":{"sqlEngine":"sqlEngine","databaseVersion":"databaseVersion","instanceHost":"instanceHost"},"filesetSpec":{"dataplexFileset":{"dataplexSpec":{"dataFormat":{"orc":"{}","protobuf":{"text":"text"},"csv":"{}","thrift":{"text":"text"},"avro":{"text":"text"},"parquet":"{}"},"compressionFormat":"compressionFormat","asset":"asset","projectId":"projectId"}}},"displayName":"displayName","routineSpec":{"bigqueryRoutineSpec":{"importedLibraries":["importedLibraries","importedLibraries"]},"routineType":"ROUTINE_TYPE_UNSPECIFIED","language":"language","definitionBody":"definitionBody","returnType":"returnType","routineArguments":[{"mode":"MODE_UNSPECIFIED","name":"name","type":"type"},{"mode":"MODE_UNSPECIFIED","name":"name","type":"type"}]},"gcsFilesetSpec":{"filePatterns":["filePatterns","filePatterns"],"sampleGcsFileSpecs":[{"gcsTimestamps":{"expireTime":"expireTime","createTime":"createTime","updateTime":"updateTime"},"filePath":"filePath","sizeBytes":"sizeBytes"},{"gcsTimestamps":{"expireTime":"expireTime","createTime":"createTime","updateTime":"updateTime"},"filePath":"filePath","sizeBytes":"sizeBytes"}]},"description":"description","type":"ENTRY_TYPE_UNSPECIFIED","usageSignal":{"commonUsageWithinTimeRange":{"key":{"viewCount":"viewCount"}},"usageWithinTimeRange":{"key":{"totalFailures":5.637377,"totalCancellations":6.0274563,"totalExecutionTimeForCompletionsMillis":5.962134,"totalCompletions":1.4658129}},"updateTime":"updateTime","favoriteCount":"favoriteCount"},"integratedSystem":"INTEGRATED_SYSTEM_UNSPECIFIED","cloudBigtableSystemSpec":{"instanceDisplayName":"instanceDisplayName"},"datasetSpec":{"vertexDatasetSpec":{"dataType":"DATA_TYPE_UNSPECIFIED","dataItemCount":"dataItemCount"}},"lookerSystemSpec":{"parentModelId":"parentModelId","parentViewDisplayName":"parentViewDisplayName","parentModelDisplayName":"parentModelDisplayName","parentViewId":"parentViewId","parentInstanceDisplayName":"parentInstanceDisplayName","parentInstanceId":"parentInstanceId"},"bigqueryDateShardedSpec":{"latestShardResource":"latestShardResource","tablePrefix":"tablePrefix","dataset":"dataset","shardCount":"shardCount"},"serviceSpec":{"cloudBigtableInstanceSpec":{"cloudBigtableClusterSpecs":[{"linkedResource":"linkedResource","displayName":"displayName","location":"location","type":"type"},{"linkedResource":"linkedResource","displayName":"displayName","location":"location","type":"type"}]}},"modelSpec":{"vertexModelSpec":{"versionDescription":"versionDescription","versionAliases":["versionAliases","versionAliases"],"versionId":"versionId","containerImageUri":"containerImageUri","vertexModelSourceInfo":{"sourceType":"MODEL_SOURCE_TYPE_UNSPECIFIED","copy":True}}},"featureOnlineStoreSpec":{"storageType":"STORAGE_TYPE_UNSPECIFIED"},"businessContext":{"entryOverview":{"overview":"overview"},"contacts":{"people":[{"designation":"designation","email":"email"},{"designation":"designation","email":"email"}]}},"sourceSystemTimestamps":{"expireTime":"expireTime","createTime":"createTime","updateTime":"updateTime"},"dataSourceConnectionSpec":{"bigqueryConnectionSpec":{"cloudSql":{"database":"database","instanceId":"instanceId","type":"DATABASE_TYPE_UNSPECIFIED"},"connectionType":"CONNECTION_TYPE_UNSPECIFIED","hasCredential":True}},"fullyQualifiedName":"fullyQualifiedName","userSpecifiedSystem":"userSpecifiedSystem","labels":{"key":"labels"},"linkedResource":"linkedResource","userSpecifiedType":"userSpecifiedType","name":"name","personalDetails":{"starTime":"starTime","starred":True},"bigqueryTableSpec":{"tableSpec":{"groupedEntry":"groupedEntry"},"viewSpec":{"viewQuery":"viewQuery"},"tableSourceType":"TABLE_SOURCE_TYPE_UNSPECIFIED"},"dataSource":{"sourceEntry":"sourceEntry","resource":"resource","service":"SERVICE_UNSPECIFIED","storageProperties":{"filePattern":["filePattern","filePattern"],"fileType":"fileType"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('entryId', 'entry_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/entries'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_entry_groups_entries_import(client):
    """Test case for datacatalog_projects_locations_entry_groups_entries_import

    
    """
    body = {"jobId":"jobId","gcsBucketPath":"gcsBucketPath"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/entries:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_entry_groups_entries_list(client):
    """Test case for datacatalog_projects_locations_entry_groups_entries_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/entries'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_entry_groups_entries_modify_entry_contacts(client):
    """Test case for datacatalog_projects_locations_entry_groups_entries_modify_entry_contacts

    
    """
    body = {"contacts":{"people":[{"designation":"designation","email":"email"},{"designation":"designation","email":"email"}]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namemodify_entry_contact}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_entry_groups_entries_modify_entry_overview(client):
    """Test case for datacatalog_projects_locations_entry_groups_entries_modify_entry_overview

    
    """
    body = {"entryOverview":{"overview":"overview"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namemodify_entry_overvie}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_entry_groups_entries_star(client):
    """Test case for datacatalog_projects_locations_entry_groups_entries_star

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namesta}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_entry_groups_entries_tags_reconcile(client):
    """Test case for datacatalog_projects_locations_entry_groups_entries_tags_reconcile

    
    """
    body = {"tagTemplate":"tagTemplate","forceDeleteMissing":True,"tags":[{"template":"template","column":"column","name":"name","fields":{"key":{"stringValue":"stringValue","enumValue":{"displayName":"displayName"},"richtextValue":"richtextValue","displayName":"displayName","timestampValue":"timestampValue","boolValue":True,"doubleValue":0.8008281904610115,"order":6}},"templateDisplayName":"templateDisplayName"},{"template":"template","column":"column","name":"name","fields":{"key":{"stringValue":"stringValue","enumValue":{"displayName":"displayName"},"richtextValue":"richtextValue","displayName":"displayName","timestampValue":"timestampValue","boolValue":True,"doubleValue":0.8008281904610115,"order":6}},"templateDisplayName":"templateDisplayName"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/tags:reconcile'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_entry_groups_entries_unstar(client):
    """Test case for datacatalog_projects_locations_entry_groups_entries_unstar

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameunsta}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_entry_groups_list(client):
    """Test case for datacatalog_projects_locations_entry_groups_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/entryGroups'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_entry_groups_tags_create(client):
    """Test case for datacatalog_projects_locations_entry_groups_tags_create

    
    """
    body = {"template":"template","column":"column","name":"name","fields":{"key":{"stringValue":"stringValue","enumValue":{"displayName":"displayName"},"richtextValue":"richtextValue","displayName":"displayName","timestampValue":"timestampValue","boolValue":True,"doubleValue":0.8008281904610115,"order":6}},"templateDisplayName":"templateDisplayName"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/tags'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_entry_groups_tags_list(client):
    """Test case for datacatalog_projects_locations_entry_groups_tags_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/tags'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_operations_cancel(client):
    """Test case for datacatalog_projects_locations_operations_cancel

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_operations_list(client):
    """Test case for datacatalog_projects_locations_operations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_tag_templates_create(client):
    """Test case for datacatalog_projects_locations_tag_templates_create

    
    """
    body = {"displayName":"displayName","name":"name","fields":{"key":{"isRequired":True,"displayName":"displayName","name":"name","description":"description","type":{"enumType":{"allowedValues":[{"displayName":"displayName"},{"displayName":"displayName"}]},"primitiveType":"PRIMITIVE_TYPE_UNSPECIFIED"},"order":0}},"isPubliclyReadable":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('tagTemplateId', 'tag_template_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/tagTemplates'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_tag_templates_fields_create(client):
    """Test case for datacatalog_projects_locations_tag_templates_fields_create

    
    """
    body = {"isRequired":True,"displayName":"displayName","name":"name","description":"description","type":{"enumType":{"allowedValues":[{"displayName":"displayName"},{"displayName":"displayName"}]},"primitiveType":"PRIMITIVE_TYPE_UNSPECIFIED"},"order":0}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('tagTemplateFieldId', 'tag_template_field_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/fields'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_tag_templates_fields_enum_values_rename(client):
    """Test case for datacatalog_projects_locations_tag_templates_fields_enum_values_rename

    
    """
    body = {"newEnumValueDisplayName":"newEnumValueDisplayName"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namerenam}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_taxonomies_create(client):
    """Test case for datacatalog_projects_locations_taxonomies_create

    
    """
    body = {"activatedPolicyTypes":["POLICY_TYPE_UNSPECIFIED","POLICY_TYPE_UNSPECIFIED"],"displayName":"displayName","service":{"identity":"identity","name":"MANAGING_SYSTEM_UNSPECIFIED"},"name":"name","description":"description","policyTagCount":0,"taxonomyTimestamps":{"expireTime":"expireTime","createTime":"createTime","updateTime":"updateTime"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/taxonomies'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_taxonomies_export(client):
    """Test case for datacatalog_projects_locations_taxonomies_export

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('serializedTaxonomies', True),
                    ('taxonomies', ['taxonomies_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/taxonomies:export'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_taxonomies_import(client):
    """Test case for datacatalog_projects_locations_taxonomies_import

    
    """
    body = {"crossRegionalSource":{"taxonomy":"taxonomy"},"inlineSource":{"taxonomies":[{"policyTags":[{"childPolicyTags":[null,null],"policyTag":"policyTag","displayName":"displayName","description":"description"},{"childPolicyTags":[null,null],"policyTag":"policyTag","displayName":"displayName","description":"description"}],"activatedPolicyTypes":["POLICY_TYPE_UNSPECIFIED","POLICY_TYPE_UNSPECIFIED"],"displayName":"displayName","description":"description"},{"policyTags":[{"childPolicyTags":[null,null],"policyTag":"policyTag","displayName":"displayName","description":"description"},{"childPolicyTags":[null,null],"policyTag":"policyTag","displayName":"displayName","description":"description"}],"activatedPolicyTypes":["POLICY_TYPE_UNSPECIFIED","POLICY_TYPE_UNSPECIFIED"],"displayName":"displayName","description":"description"}]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/taxonomies:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_taxonomies_list(client):
    """Test case for datacatalog_projects_locations_taxonomies_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/taxonomies'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_taxonomies_policy_tags_create(client):
    """Test case for datacatalog_projects_locations_taxonomies_policy_tags_create

    
    """
    body = {"childPolicyTags":["childPolicyTags","childPolicyTags"],"displayName":"displayName","name":"name","description":"description","parentPolicyTag":"parentPolicyTag"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/policyTags'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_taxonomies_policy_tags_delete(client):
    """Test case for datacatalog_projects_locations_taxonomies_policy_tags_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('force', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_taxonomies_policy_tags_get(client):
    """Test case for datacatalog_projects_locations_taxonomies_policy_tags_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_taxonomies_policy_tags_get_iam_policy(client):
    """Test case for datacatalog_projects_locations_taxonomies_policy_tags_get_iam_policy

    
    """
    body = {"options":{"requestedPolicyVersion":0}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_taxonomies_policy_tags_list(client):
    """Test case for datacatalog_projects_locations_taxonomies_policy_tags_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/policyTags'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_taxonomies_policy_tags_patch(client):
    """Test case for datacatalog_projects_locations_taxonomies_policy_tags_patch

    
    """
    body = {"childPolicyTags":["childPolicyTags","childPolicyTags"],"displayName":"displayName","name":"name","description":"description","parentPolicyTag":"parentPolicyTag"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_taxonomies_policy_tags_set_iam_policy(client):
    """Test case for datacatalog_projects_locations_taxonomies_policy_tags_set_iam_policy

    
    """
    body = {"policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_taxonomies_policy_tags_test_iam_permissions(client):
    """Test case for datacatalog_projects_locations_taxonomies_policy_tags_test_iam_permissions

    
    """
    body = {"permissions":["permissions","permissions"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacatalog_projects_locations_taxonomies_replace(client):
    """Test case for datacatalog_projects_locations_taxonomies_replace

    
    """
    body = {"serializedTaxonomy":{"policyTags":[{"childPolicyTags":[null,null],"policyTag":"policyTag","displayName":"displayName","description":"description"},{"childPolicyTags":[null,null],"policyTag":"policyTag","displayName":"displayName","description":"description"}],"activatedPolicyTypes":["POLICY_TYPE_UNSPECIFIED","POLICY_TYPE_UNSPECIFIED"],"displayName":"displayName","description":"description"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namereplac}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

