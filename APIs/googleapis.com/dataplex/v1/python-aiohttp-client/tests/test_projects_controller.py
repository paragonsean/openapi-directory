# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_dataplex_v1_asset import GoogleCloudDataplexV1Asset
from openapi_server.models.google_cloud_dataplex_v1_content import GoogleCloudDataplexV1Content
from openapi_server.models.google_cloud_dataplex_v1_data_attribute import GoogleCloudDataplexV1DataAttribute
from openapi_server.models.google_cloud_dataplex_v1_data_attribute_binding import GoogleCloudDataplexV1DataAttributeBinding
from openapi_server.models.google_cloud_dataplex_v1_data_scan import GoogleCloudDataplexV1DataScan
from openapi_server.models.google_cloud_dataplex_v1_data_taxonomy import GoogleCloudDataplexV1DataTaxonomy
from openapi_server.models.google_cloud_dataplex_v1_entity import GoogleCloudDataplexV1Entity
from openapi_server.models.google_cloud_dataplex_v1_environment import GoogleCloudDataplexV1Environment
from openapi_server.models.google_cloud_dataplex_v1_lake import GoogleCloudDataplexV1Lake
from openapi_server.models.google_cloud_dataplex_v1_list_actions_response import GoogleCloudDataplexV1ListActionsResponse
from openapi_server.models.google_cloud_dataplex_v1_list_assets_response import GoogleCloudDataplexV1ListAssetsResponse
from openapi_server.models.google_cloud_dataplex_v1_list_content_response import GoogleCloudDataplexV1ListContentResponse
from openapi_server.models.google_cloud_dataplex_v1_list_data_attribute_bindings_response import GoogleCloudDataplexV1ListDataAttributeBindingsResponse
from openapi_server.models.google_cloud_dataplex_v1_list_data_attributes_response import GoogleCloudDataplexV1ListDataAttributesResponse
from openapi_server.models.google_cloud_dataplex_v1_list_data_scans_response import GoogleCloudDataplexV1ListDataScansResponse
from openapi_server.models.google_cloud_dataplex_v1_list_data_taxonomies_response import GoogleCloudDataplexV1ListDataTaxonomiesResponse
from openapi_server.models.google_cloud_dataplex_v1_list_entities_response import GoogleCloudDataplexV1ListEntitiesResponse
from openapi_server.models.google_cloud_dataplex_v1_list_environments_response import GoogleCloudDataplexV1ListEnvironmentsResponse
from openapi_server.models.google_cloud_dataplex_v1_list_jobs_response import GoogleCloudDataplexV1ListJobsResponse
from openapi_server.models.google_cloud_dataplex_v1_list_lakes_response import GoogleCloudDataplexV1ListLakesResponse
from openapi_server.models.google_cloud_dataplex_v1_list_partitions_response import GoogleCloudDataplexV1ListPartitionsResponse
from openapi_server.models.google_cloud_dataplex_v1_list_sessions_response import GoogleCloudDataplexV1ListSessionsResponse
from openapi_server.models.google_cloud_dataplex_v1_list_tasks_response import GoogleCloudDataplexV1ListTasksResponse
from openapi_server.models.google_cloud_dataplex_v1_list_zones_response import GoogleCloudDataplexV1ListZonesResponse
from openapi_server.models.google_cloud_dataplex_v1_partition import GoogleCloudDataplexV1Partition
from openapi_server.models.google_cloud_dataplex_v1_run_task_request import GoogleCloudDataplexV1RunTaskRequest
from openapi_server.models.google_cloud_dataplex_v1_run_task_response import GoogleCloudDataplexV1RunTaskResponse
from openapi_server.models.google_cloud_dataplex_v1_task import GoogleCloudDataplexV1Task
from openapi_server.models.google_cloud_dataplex_v1_zone import GoogleCloudDataplexV1Zone
from openapi_server.models.google_cloud_location_list_locations_response import GoogleCloudLocationListLocationsResponse
from openapi_server.models.google_iam_v1_policy import GoogleIamV1Policy
from openapi_server.models.google_iam_v1_set_iam_policy_request import GoogleIamV1SetIamPolicyRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_request import GoogleIamV1TestIamPermissionsRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_response import GoogleIamV1TestIamPermissionsResponse
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_data_attribute_bindings_create(client):
    """Test case for dataplex_projects_locations_data_attribute_bindings_create

    
    """
    body = {"uid":"uid","createTime":"createTime","resource":"resource","displayName":"displayName","paths":[{"name":"name","attributes":["attributes","attributes"]},{"name":"name","attributes":["attributes","attributes"]}],"name":"name","description":"description","attributes":["attributes","attributes"],"etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}}
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
                    ('dataAttributeBindingId', 'data_attribute_binding_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/dataAttributeBindings'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_data_attribute_bindings_list(client):
    """Test case for dataplex_projects_locations_data_attribute_bindings_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/dataAttributeBindings'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_data_scans_create(client):
    """Test case for dataplex_projects_locations_data_scans_create

    
    """
    body = {"data":{"resource":"resource","entity":"entity"},"displayName":"displayName","executionSpec":{"field":"field","trigger":{"onDemand":"{}","schedule":{"cron":"cron"}}},"executionStatus":{"latestJobEndTime":"latestJobEndTime","latestJobStartTime":"latestJobStartTime"},"dataQualitySpec":{"samplingPercent":1.1730742,"postScanActions":{"bigqueryExport":{"resultsTable":"resultsTable"}},"rules":[{"ignoreNull":True,"statisticRangeExpectation":{"minValue":"minValue","statistic":"STATISTIC_UNDEFINED","strictMinEnabled":True,"strictMaxEnabled":True,"maxValue":"maxValue"},"column":"column","setExpectation":{"values":["values","values"]},"description":"description","threshold":6.84685269835264,"rangeExpectation":{"minValue":"minValue","strictMinEnabled":True,"strictMaxEnabled":True,"maxValue":"maxValue"},"regexExpectation":{"regex":"regex"},"uniquenessExpectation":"{}","tableConditionExpectation":{"sqlExpression":"sqlExpression"},"rowConditionExpectation":{"sqlExpression":"sqlExpression"},"name":"name","nonNullExpectation":"{}","dimension":"dimension"},{"ignoreNull":True,"statisticRangeExpectation":{"minValue":"minValue","statistic":"STATISTIC_UNDEFINED","strictMinEnabled":True,"strictMaxEnabled":True,"maxValue":"maxValue"},"column":"column","setExpectation":{"values":["values","values"]},"description":"description","threshold":6.84685269835264,"rangeExpectation":{"minValue":"minValue","strictMinEnabled":True,"strictMaxEnabled":True,"maxValue":"maxValue"},"regexExpectation":{"regex":"regex"},"uniquenessExpectation":"{}","tableConditionExpectation":{"sqlExpression":"sqlExpression"},"rowConditionExpectation":{"sqlExpression":"sqlExpression"},"name":"name","nonNullExpectation":"{}","dimension":"dimension"}],"rowFilter":"rowFilter"},"description":"description","updateTime":"updateTime","type":"DATA_SCAN_TYPE_UNSPECIFIED","dataQualityResult":{"scannedData":{"incrementalField":{"field":"field","start":"start","end":"end"}},"postScanActionsResult":{"bigqueryExportResult":{"state":"STATE_UNSPECIFIED","message":"message"}},"score":7.4577446,"columns":[{"score":1.2315135,"column":"column"},{"score":1.2315135,"column":"column"}],"rules":[{"failingRowsQuery":"failingRowsQuery","evaluatedCount":"evaluatedCount","passRatio":1.4894159098541704,"nullCount":"nullCount","rule":{"ignoreNull":True,"statisticRangeExpectation":{"minValue":"minValue","statistic":"STATISTIC_UNDEFINED","strictMinEnabled":True,"strictMaxEnabled":True,"maxValue":"maxValue"},"column":"column","setExpectation":{"values":["values","values"]},"description":"description","threshold":6.84685269835264,"rangeExpectation":{"minValue":"minValue","strictMinEnabled":True,"strictMaxEnabled":True,"maxValue":"maxValue"},"regexExpectation":{"regex":"regex"},"uniquenessExpectation":"{}","tableConditionExpectation":{"sqlExpression":"sqlExpression"},"rowConditionExpectation":{"sqlExpression":"sqlExpression"},"name":"name","nonNullExpectation":"{}","dimension":"dimension"},"passedCount":"passedCount","passed":True},{"failingRowsQuery":"failingRowsQuery","evaluatedCount":"evaluatedCount","passRatio":1.4894159098541704,"nullCount":"nullCount","rule":{"ignoreNull":True,"statisticRangeExpectation":{"minValue":"minValue","statistic":"STATISTIC_UNDEFINED","strictMinEnabled":True,"strictMaxEnabled":True,"maxValue":"maxValue"},"column":"column","setExpectation":{"values":["values","values"]},"description":"description","threshold":6.84685269835264,"rangeExpectation":{"minValue":"minValue","strictMinEnabled":True,"strictMaxEnabled":True,"maxValue":"maxValue"},"regexExpectation":{"regex":"regex"},"uniquenessExpectation":"{}","tableConditionExpectation":{"sqlExpression":"sqlExpression"},"rowConditionExpectation":{"sqlExpression":"sqlExpression"},"name":"name","nonNullExpectation":"{}","dimension":"dimension"},"passedCount":"passedCount","passed":True}],"passed":True,"rowCount":"rowCount","dimensions":[{"score":1.0246457,"passed":True,"dimension":{"name":"name"}},{"score":1.0246457,"passed":True,"dimension":{"name":"name"}}]},"labels":{"key":"labels"},"uid":"uid","dataProfileResult":{"scannedData":{"incrementalField":{"field":"field","start":"start","end":"end"}},"postScanActionsResult":{"bigqueryExportResult":{"state":"STATE_UNSPECIFIED","message":"message"}},"profile":{"fields":[{"mode":"mode","profile":{"distinctRatio":0.8008281904610115,"stringProfile":{"averageLength":2.027123023002322,"minLength":"minLength","maxLength":"maxLength"},"nullRatio":3.616076749251911,"doubleProfile":{"average":6.027456183070403,"min":5.962133916683182,"max":1.4658129805029452,"quartiles":[5.637376656633329,5.637376656633329],"standardDeviation":2.3021358869347655},"integerProfile":{"average":7.061401241503109,"min":"min","max":"max","quartiles":["quartiles","quartiles"],"standardDeviation":9.301444243932576},"topNValues":[{"count":"count","value":"value","ratio":4.145608029883936},{"count":"count","value":"value","ratio":4.145608029883936}]},"name":"name","type":"type"},{"mode":"mode","profile":{"distinctRatio":0.8008281904610115,"stringProfile":{"averageLength":2.027123023002322,"minLength":"minLength","maxLength":"maxLength"},"nullRatio":3.616076749251911,"doubleProfile":{"average":6.027456183070403,"min":5.962133916683182,"max":1.4658129805029452,"quartiles":[5.637376656633329,5.637376656633329],"standardDeviation":2.3021358869347655},"integerProfile":{"average":7.061401241503109,"min":"min","max":"max","quartiles":["quartiles","quartiles"],"standardDeviation":9.301444243932576},"topNValues":[{"count":"count","value":"value","ratio":4.145608029883936},{"count":"count","value":"value","ratio":4.145608029883936}]},"name":"name","type":"type"}]},"rowCount":"rowCount"},"dataProfileSpec":{"samplingPercent":7.386282,"postScanActions":{"bigqueryExport":{"resultsTable":"resultsTable"}},"includeFields":{"fieldNames":["fieldNames","fieldNames"]},"excludeFields":{"fieldNames":["fieldNames","fieldNames"]},"rowFilter":"rowFilter"},"createTime":"createTime","name":"name","state":"STATE_UNSPECIFIED"}
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
                    ('dataScanId', 'data_scan_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/dataScans'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_data_scans_list(client):
    """Test case for dataplex_projects_locations_data_scans_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/dataScans'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_data_taxonomies_attributes_create(client):
    """Test case for dataplex_projects_locations_data_taxonomies_attributes_create

    
    """
    body = {"uid":"uid","createTime":"createTime","resourceAccessSpec":{"readers":["readers","readers"],"owners":["owners","owners"],"writers":["writers","writers"]},"displayName":"displayName","dataAccessSpec":{"readers":["readers","readers"]},"name":"name","attributeCount":0,"description":"description","etag":"etag","updateTime":"updateTime","parentId":"parentId","labels":{"key":"labels"}}
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
                    ('dataAttributeId', 'data_attribute_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/attributes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_data_taxonomies_attributes_list(client):
    """Test case for dataplex_projects_locations_data_taxonomies_attributes_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/attributes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_data_taxonomies_create(client):
    """Test case for dataplex_projects_locations_data_taxonomies_create

    
    """
    body = {"uid":"uid","classCount":6,"createTime":"createTime","displayName":"displayName","name":"name","attributeCount":0,"description":"description","etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}}
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
                    ('dataTaxonomyId', 'data_taxonomy_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/dataTaxonomies'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_data_taxonomies_list(client):
    """Test case for dataplex_projects_locations_data_taxonomies_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/dataTaxonomies'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_content_create(client):
    """Test case for dataplex_projects_locations_lakes_content_create

    
    """
    body = {"path":"path","uid":"uid","createTime":"createTime","dataText":"dataText","sqlScript":{"engine":"QUERY_ENGINE_UNSPECIFIED"},"name":"name","description":"description","updateTime":"updateTime","labels":{"key":"labels"},"notebook":{"kernelType":"KERNEL_TYPE_UNSPECIFIED"}}
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
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/content'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_content_list(client):
    """Test case for dataplex_projects_locations_lakes_content_list

    
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
        path='/v1/{parent}/content'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_contentitems_create(client):
    """Test case for dataplex_projects_locations_lakes_contentitems_create

    
    """
    body = {"path":"path","uid":"uid","createTime":"createTime","dataText":"dataText","sqlScript":{"engine":"QUERY_ENGINE_UNSPECIFIED"},"name":"name","description":"description","updateTime":"updateTime","labels":{"key":"labels"},"notebook":{"kernelType":"KERNEL_TYPE_UNSPECIFIED"}}
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
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/contentitems'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_contentitems_list(client):
    """Test case for dataplex_projects_locations_lakes_contentitems_list

    
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
        path='/v1/{parent}/contentitems'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_create(client):
    """Test case for dataplex_projects_locations_lakes_create

    
    """
    body = {"metastore":{"service":"service"},"uid":"uid","createTime":"createTime","displayName":"displayName","metastoreStatus":{"endpoint":"endpoint","updateTime":"updateTime","state":"STATE_UNSPECIFIED","message":"message"},"name":"name","description":"description","serviceAccount":"serviceAccount","updateTime":"updateTime","state":"STATE_UNSPECIFIED","assetStatus":{"activeAssets":0,"securityPolicyApplyingAssets":6,"updateTime":"updateTime"},"labels":{"key":"labels"}}
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
                    ('lakeId', 'lake_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/lakes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_environments_create(client):
    """Test case for dataplex_projects_locations_lakes_environments_create

    
    """
    body = {"uid":"uid","endpoints":{"notebooks":"notebooks","sql":"sql"},"infrastructureSpec":{"compute":{"maxNodeCount":6,"nodeCount":1,"diskSizeGb":0},"osImage":{"imageVersion":"imageVersion","pythonPackages":["pythonPackages","pythonPackages"],"javaLibraries":["javaLibraries","javaLibraries"],"properties":{"key":"properties"}}},"createTime":"createTime","displayName":"displayName","name":"name","sessionStatus":{"active":True},"description":"description","sessionSpec":{"maxIdleDuration":"maxIdleDuration","enableFastStartup":True},"updateTime":"updateTime","state":"STATE_UNSPECIFIED","labels":{"key":"labels"}}
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
                    ('environmentId', 'environment_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/environments'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_environments_list(client):
    """Test case for dataplex_projects_locations_lakes_environments_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/environments'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_environments_sessions_list(client):
    """Test case for dataplex_projects_locations_lakes_environments_sessions_list

    
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
        path='/v1/{parent}/sessions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_list(client):
    """Test case for dataplex_projects_locations_lakes_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/lakes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_tasks_create(client):
    """Test case for dataplex_projects_locations_lakes_tasks_create

    
    """
    body = {"displayName":"displayName","executionSpec":{"args":{"key":"args"},"kmsKey":"kmsKey","project":"project","serviceAccount":"serviceAccount","maxJobExecutionLifetime":"maxJobExecutionLifetime"},"executionStatus":{"latestJob":{"uid":"uid","executionSpec":{"args":{"key":"args"},"kmsKey":"kmsKey","project":"project","serviceAccount":"serviceAccount","maxJobExecutionLifetime":"maxJobExecutionLifetime"},"retryCount":0,"service":"SERVICE_UNSPECIFIED","name":"name","serviceJob":"serviceJob","startTime":"startTime","endTime":"endTime","state":"STATE_UNSPECIFIED","trigger":"TRIGGER_UNSPECIFIED","message":"message","labels":{"key":"labels"}},"updateTime":"updateTime"},"description":"description","updateTime":"updateTime","labels":{"key":"labels"},"uid":"uid","createTime":"createTime","spark":{"infrastructureSpec":{"batch":{"maxExecutorsCount":6,"executorsCount":0},"vpcNetwork":{"networkTags":["networkTags","networkTags"],"network":"network","subNetwork":"subNetwork"},"containerImage":{"pythonPackages":["pythonPackages","pythonPackages"],"image":"image","javaJars":["javaJars","javaJars"],"properties":{"key":"properties"}}},"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"sqlScript":"sqlScript","mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"pythonScriptFile":"pythonScriptFile","sqlScriptFile":"sqlScriptFile"},"name":"name","triggerSpec":{"schedule":"schedule","maxRetries":1,"disabled":True,"startTime":"startTime","type":"TYPE_UNSPECIFIED"},"state":"STATE_UNSPECIFIED","notebook":{"infrastructureSpec":{"batch":{"maxExecutorsCount":6,"executorsCount":0},"vpcNetwork":{"networkTags":["networkTags","networkTags"],"network":"network","subNetwork":"subNetwork"},"containerImage":{"pythonPackages":["pythonPackages","pythonPackages"],"image":"image","javaJars":["javaJars","javaJars"],"properties":{"key":"properties"}}},"archiveUris":["archiveUris","archiveUris"],"fileUris":["fileUris","fileUris"],"notebook":"notebook"}}
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
                    ('taskId', 'task_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/tasks'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_tasks_jobs_list(client):
    """Test case for dataplex_projects_locations_lakes_tasks_jobs_list

    
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
        path='/v1/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_tasks_list(client):
    """Test case for dataplex_projects_locations_lakes_tasks_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/tasks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_tasks_run(client):
    """Test case for dataplex_projects_locations_lakes_tasks_run

    
    """
    body = {"args":{"key":"args"},"labels":{"key":"labels"}}
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
        path='/v1/{nameru}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_zones_assets_actions_list(client):
    """Test case for dataplex_projects_locations_lakes_zones_assets_actions_list

    
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
        path='/v1/{parent}/actions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_zones_assets_create(client):
    """Test case for dataplex_projects_locations_lakes_zones_assets_create

    
    """
    body = {"displayName":"displayName","discoveryStatus":{"lastRunTime":"lastRunTime","lastRunDuration":"lastRunDuration","stats":{"tables":"tables","dataItems":"dataItems","dataSize":"dataSize","filesets":"filesets"},"updateTime":"updateTime","state":"STATE_UNSPECIFIED","message":"message"},"description":"description","updateTime":"updateTime","securityStatus":{"updateTime":"updateTime","state":"STATE_UNSPECIFIED","message":"message"},"labels":{"key":"labels"},"uid":"uid","resourceStatus":{"managedAccessIdentity":"managedAccessIdentity","updateTime":"updateTime","state":"STATE_UNSPECIFIED","message":"message"},"createTime":"createTime","discoverySpec":{"schedule":"schedule","excludePatterns":["excludePatterns","excludePatterns"],"csvOptions":{"disableTypeInference":True,"delimiter":"delimiter","headerRows":0,"encoding":"encoding"},"includePatterns":["includePatterns","includePatterns"],"jsonOptions":{"disableTypeInference":True,"encoding":"encoding"},"enabled":True},"name":"name","state":"STATE_UNSPECIFIED","resourceSpec":{"name":"name","readAccessMode":"ACCESS_MODE_UNSPECIFIED","type":"TYPE_UNSPECIFIED"}}
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
                    ('assetId', 'asset_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/assets'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_zones_assets_get_iam_policy(client):
    """Test case for dataplex_projects_locations_lakes_zones_assets_get_iam_policy

    
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
                    ('options.requestedPolicyVersion', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_zones_assets_list(client):
    """Test case for dataplex_projects_locations_lakes_zones_assets_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/assets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_zones_assets_patch(client):
    """Test case for dataplex_projects_locations_lakes_zones_assets_patch

    
    """
    body = {"displayName":"displayName","discoveryStatus":{"lastRunTime":"lastRunTime","lastRunDuration":"lastRunDuration","stats":{"tables":"tables","dataItems":"dataItems","dataSize":"dataSize","filesets":"filesets"},"updateTime":"updateTime","state":"STATE_UNSPECIFIED","message":"message"},"description":"description","updateTime":"updateTime","securityStatus":{"updateTime":"updateTime","state":"STATE_UNSPECIFIED","message":"message"},"labels":{"key":"labels"},"uid":"uid","resourceStatus":{"managedAccessIdentity":"managedAccessIdentity","updateTime":"updateTime","state":"STATE_UNSPECIFIED","message":"message"},"createTime":"createTime","discoverySpec":{"schedule":"schedule","excludePatterns":["excludePatterns","excludePatterns"],"csvOptions":{"disableTypeInference":True,"delimiter":"delimiter","headerRows":0,"encoding":"encoding"},"includePatterns":["includePatterns","includePatterns"],"jsonOptions":{"disableTypeInference":True,"encoding":"encoding"},"enabled":True},"name":"name","state":"STATE_UNSPECIFIED","resourceSpec":{"name":"name","readAccessMode":"ACCESS_MODE_UNSPECIFIED","type":"TYPE_UNSPECIFIED"}}
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
                    ('updateMask', 'update_mask_example'),
                    ('validateOnly', True)]
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

async def test_dataplex_projects_locations_lakes_zones_assets_set_iam_policy(client):
    """Test case for dataplex_projects_locations_lakes_zones_assets_set_iam_policy

    
    """
    body = {"updateMask":"updateMask","policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0,"auditConfigs":[{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"},{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"}]}}
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

async def test_dataplex_projects_locations_lakes_zones_assets_test_iam_permissions(client):
    """Test case for dataplex_projects_locations_lakes_zones_assets_test_iam_permissions

    
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

async def test_dataplex_projects_locations_lakes_zones_create(client):
    """Test case for dataplex_projects_locations_lakes_zones_create

    
    """
    body = {"uid":"uid","createTime":"createTime","displayName":"displayName","discoverySpec":{"schedule":"schedule","excludePatterns":["excludePatterns","excludePatterns"],"csvOptions":{"disableTypeInference":True,"delimiter":"delimiter","headerRows":0,"encoding":"encoding"},"includePatterns":["includePatterns","includePatterns"],"jsonOptions":{"disableTypeInference":True,"encoding":"encoding"},"enabled":True},"name":"name","description":"description","updateTime":"updateTime","state":"STATE_UNSPECIFIED","type":"TYPE_UNSPECIFIED","assetStatus":{"activeAssets":0,"securityPolicyApplyingAssets":6,"updateTime":"updateTime"},"labels":{"key":"labels"},"resourceSpec":{"locationType":"LOCATION_TYPE_UNSPECIFIED"}}
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
                    ('validateOnly', True),
                    ('zoneId', 'zone_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/zones'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_zones_entities_create(client):
    """Test case for dataplex_projects_locations_lakes_zones_entities_create

    
    """
    body = {"schema":{"partitionFields":[{"name":"name","type":"TYPE_UNSPECIFIED"},{"name":"name","type":"TYPE_UNSPECIFIED"}],"fields":[{"mode":"MODE_UNSPECIFIED","name":"name","description":"description","fields":[null,null],"type":"TYPE_UNSPECIFIED"},{"mode":"MODE_UNSPECIFIED","name":"name","description":"description","fields":[null,null],"type":"TYPE_UNSPECIFIED"}],"userManaged":True,"partitionStyle":"PARTITION_STYLE_UNSPECIFIED"},"access":{"read":"ACCESS_MODE_UNSPECIFIED"},"dataPathPattern":"dataPathPattern","displayName":"displayName","format":{"csv":{"quote":"quote","delimiter":"delimiter","headerRows":0,"encoding":"encoding"},"format":"FORMAT_UNSPECIFIED","iceberg":{"metadataLocation":"metadataLocation"},"compressionFormat":"COMPRESSION_FORMAT_UNSPECIFIED","json":{"encoding":"encoding"},"mimeType":"mimeType"},"description":"description","updateTime":"updateTime","type":"TYPE_UNSPECIFIED","dataPath":"dataPath","uid":"uid","system":"STORAGE_SYSTEM_UNSPECIFIED","createTime":"createTime","name":"name","etag":"etag","id":"id","asset":"asset","catalogEntry":"catalogEntry","compatibility":{"hiveMetastore":{"reason":"reason","compatible":True},"bigquery":{"reason":"reason","compatible":True}}}
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
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/entities'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_zones_entities_list(client):
    """Test case for dataplex_projects_locations_lakes_zones_entities_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/entities'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_zones_entities_partitions_create(client):
    """Test case for dataplex_projects_locations_lakes_zones_entities_partitions_create

    
    """
    body = {"values":["values","values"],"name":"name","etag":"etag","location":"location"}
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
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/partitions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_zones_entities_partitions_list(client):
    """Test case for dataplex_projects_locations_lakes_zones_entities_partitions_list

    
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
        path='/v1/{parent}/partitions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_zones_entities_update(client):
    """Test case for dataplex_projects_locations_lakes_zones_entities_update

    
    """
    body = {"schema":{"partitionFields":[{"name":"name","type":"TYPE_UNSPECIFIED"},{"name":"name","type":"TYPE_UNSPECIFIED"}],"fields":[{"mode":"MODE_UNSPECIFIED","name":"name","description":"description","fields":[null,null],"type":"TYPE_UNSPECIFIED"},{"mode":"MODE_UNSPECIFIED","name":"name","description":"description","fields":[null,null],"type":"TYPE_UNSPECIFIED"}],"userManaged":True,"partitionStyle":"PARTITION_STYLE_UNSPECIFIED"},"access":{"read":"ACCESS_MODE_UNSPECIFIED"},"dataPathPattern":"dataPathPattern","displayName":"displayName","format":{"csv":{"quote":"quote","delimiter":"delimiter","headerRows":0,"encoding":"encoding"},"format":"FORMAT_UNSPECIFIED","iceberg":{"metadataLocation":"metadataLocation"},"compressionFormat":"COMPRESSION_FORMAT_UNSPECIFIED","json":{"encoding":"encoding"},"mimeType":"mimeType"},"description":"description","updateTime":"updateTime","type":"TYPE_UNSPECIFIED","dataPath":"dataPath","uid":"uid","system":"STORAGE_SYSTEM_UNSPECIFIED","createTime":"createTime","name":"name","etag":"etag","id":"id","asset":"asset","catalogEntry":"catalogEntry","compatibility":{"hiveMetastore":{"reason":"reason","compatible":True},"bigquery":{"reason":"reason","compatible":True}}}
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
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_lakes_zones_list(client):
    """Test case for dataplex_projects_locations_lakes_zones_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/zones'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_list(client):
    """Test case for dataplex_projects_locations_list

    
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
        path='/v1/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_operations_cancel(client):
    """Test case for dataplex_projects_locations_operations_cancel

    
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
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataplex_projects_locations_operations_delete(client):
    """Test case for dataplex_projects_locations_operations_delete

    
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
                    ('etag', 'etag_example')]
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

async def test_dataplex_projects_locations_operations_get(client):
    """Test case for dataplex_projects_locations_operations_get

    
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
                    ('view', 'view_example')]
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

async def test_dataplex_projects_locations_operations_list(client):
    """Test case for dataplex_projects_locations_operations_list

    
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

