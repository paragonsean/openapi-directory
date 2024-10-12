# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_iam_policy_request import GetIamPolicyRequest
from openapi_server.models.policy import Policy
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.table import Table
from openapi_server.models.table_list import TableList
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse


pytestmark = pytest.mark.asyncio

async def test_bigquery_tables_delete(client):
    """Test case for bigquery_tables_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}'.format(project_id='project_id_example', dataset_id='dataset_id_example', table_id='table_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_tables_get(client):
    """Test case for bigquery_tables_get

    
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
                    ('selectedFields', 'selected_fields_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}'.format(project_id='project_id_example', dataset_id='dataset_id_example', table_id='table_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_tables_get_iam_policy(client):
    """Test case for bigquery_tables_get_iam_policy

    
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
        path='/bigquery/v2/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_tables_insert(client):
    """Test case for bigquery_tables_insert

    
    """
    body = {"schema":{"fields":[{"defaultValueExpression":"defaultValueExpression","precision":"precision","description":"description","scale":"scale","type":"type","mode":"mode","policyTags":{"names":["names","names"]},"roundingMode":"ROUNDING_MODE_UNSPECIFIED","name":"name","categories":{"names":["names","names"]},"collation":"collation","fields":[null,null],"maxLength":"maxLength","rangeElementType":{"type":"type"}},{"defaultValueExpression":"defaultValueExpression","precision":"precision","description":"description","scale":"scale","type":"type","mode":"mode","policyTags":{"names":["names","names"]},"roundingMode":"ROUNDING_MODE_UNSPECIFIED","name":"name","categories":{"names":["names","names"]},"collation":"collation","fields":[null,null],"maxLength":"maxLength","rangeElementType":{"type":"type"}}]},"defaultRoundingMode":"ROUNDING_MODE_UNSPECIFIED","lastModifiedTime":"lastModifiedTime","materializedViewStatus":{"lastRefreshStatus":{"reason":"reason","location":"location","debugInfo":"debugInfo","message":"message"},"refreshWatermark":"refreshWatermark"},"creationTime":"creationTime","numRows":"numRows","description":"description","numLongTermLogicalBytes":"numLongTermLogicalBytes","requirePartitionFilter":False,"type":"type","defaultCollation":"defaultCollation","numBytes":"numBytes","resourceTags":{"key":"resourceTags"},"externalDataConfiguration":{"schema":{"fields":[{"defaultValueExpression":"defaultValueExpression","precision":"precision","description":"description","scale":"scale","type":"type","mode":"mode","policyTags":{"names":["names","names"]},"roundingMode":"ROUNDING_MODE_UNSPECIFIED","name":"name","categories":{"names":["names","names"]},"collation":"collation","fields":[null,null],"maxLength":"maxLength","rangeElementType":{"type":"type"}},{"defaultValueExpression":"defaultValueExpression","precision":"precision","description":"description","scale":"scale","type":"type","mode":"mode","policyTags":{"names":["names","names"]},"roundingMode":"ROUNDING_MODE_UNSPECIFIED","name":"name","categories":{"names":["names","names"]},"collation":"collation","fields":[null,null],"maxLength":"maxLength","rangeElementType":{"type":"type"}}]},"jsonExtension":"JSON_EXTENSION_UNSPECIFIED","objectMetadata":"OBJECT_METADATA_UNSPECIFIED","sourceUris":["sourceUris","sourceUris"],"decimalTargetTypes":["DECIMAL_TARGET_TYPE_UNSPECIFIED","DECIMAL_TARGET_TYPE_UNSPECIFIED"],"ignoreUnknownValues":True,"fileSetSpecType":"FILE_SET_SPEC_TYPE_FILE_SYSTEM_MATCH","jsonOptions":{"encoding":"encoding"},"googleSheetsOptions":{"skipLeadingRows":"skipLeadingRows","range":"range"},"metadataCacheMode":"METADATA_CACHE_MODE_UNSPECIFIED","avroOptions":{"useAvroLogicalTypes":True},"autodetect":True,"referenceFileSchemaUri":"referenceFileSchemaUri","hivePartitioningOptions":{"mode":"mode","sourceUriPrefix":"sourceUriPrefix","fields":["fields","fields"],"requirePartitionFilter":False},"bigtableOptions":{"columnFamilies":[{"familyId":"familyId","columns":[{"qualifierEncoded":"qualifierEncoded","fieldName":"fieldName","encoding":"encoding","qualifierString":"qualifierString","type":"type","onlyReadLatest":True},{"qualifierEncoded":"qualifierEncoded","fieldName":"fieldName","encoding":"encoding","qualifierString":"qualifierString","type":"type","onlyReadLatest":True}],"encoding":"encoding","type":"type","onlyReadLatest":True},{"familyId":"familyId","columns":[{"qualifierEncoded":"qualifierEncoded","fieldName":"fieldName","encoding":"encoding","qualifierString":"qualifierString","type":"type","onlyReadLatest":True},{"qualifierEncoded":"qualifierEncoded","fieldName":"fieldName","encoding":"encoding","qualifierString":"qualifierString","type":"type","onlyReadLatest":True}],"encoding":"encoding","type":"type","onlyReadLatest":True}],"ignoreUnspecifiedColumnFamilies":True,"outputColumnFamiliesAsJson":True,"readRowkeyAsString":True},"csvOptions":{"allowQuotedNewlines":True,"skipLeadingRows":"skipLeadingRows","quote":"\"","preserveAsciiControlCharacters":True,"nullMarker":"nullMarker","encoding":"encoding","fieldDelimiter":"fieldDelimiter","allowJaggedRows":True},"connectionId":"connectionId","compression":"compression","sourceFormat":"sourceFormat","maxBadRecords":0,"parquetOptions":{"enumAsString":True,"enableListInference":True}},"view":{"useExplicitColumnNames":True,"userDefinedFunctionResources":[{"resourceUri":"resourceUri","inlineCode":"inlineCode"},{"resourceUri":"resourceUri","inlineCode":"inlineCode"}],"privacyPolicy":{"aggregationThresholdPolicy":{"privacyUnitColumns":["privacyUnitColumns","privacyUnitColumns"],"threshold":"threshold"}},"query":"query","useLegacySql":True},"numLongTermBytes":"numLongTermBytes","maxStaleness":"maxStaleness","biglakeConfiguration":{"tableFormat":"TABLE_FORMAT_UNSPECIFIED","storageUri":"storageUri","connectionId":"connectionId","fileFormat":"FILE_FORMAT_UNSPECIFIED"},"numActiveLogicalBytes":"numActiveLogicalBytes","encryptionConfiguration":{"kmsKeyName":"kmsKeyName"},"model":{"trainingRuns":[{"trainingOptions":{"earlyStop":True,"l1Reg":2.3021358869347655,"maxIteration":"maxIteration","l2Reg":7.061401241503109,"learnRate":9.301444243932576,"lineSearchInitLearnRate":3.616076749251911,"warmStart":True,"learnRateStrategy":"learnRateStrategy","minRelProgress":2.027123023002322},"iterationResults":[{"index":1,"learnRate":5.962133916683182,"durationMs":"durationMs","evalLoss":6.027456183070403,"trainingLoss":5.637376656633329},{"index":1,"learnRate":5.962133916683182,"durationMs":"durationMs","evalLoss":6.027456183070403,"trainingLoss":5.637376656633329}],"startTime":"2000-01-23T04:56:07.000+00:00","state":"state"},{"trainingOptions":{"earlyStop":True,"l1Reg":2.3021358869347655,"maxIteration":"maxIteration","l2Reg":7.061401241503109,"learnRate":9.301444243932576,"lineSearchInitLearnRate":3.616076749251911,"warmStart":True,"learnRateStrategy":"learnRateStrategy","minRelProgress":2.027123023002322},"iterationResults":[{"index":1,"learnRate":5.962133916683182,"durationMs":"durationMs","evalLoss":6.027456183070403,"trainingLoss":5.637376656633329},{"index":1,"learnRate":5.962133916683182,"durationMs":"durationMs","evalLoss":6.027456183070403,"trainingLoss":5.637376656633329}],"startTime":"2000-01-23T04:56:07.000+00:00","state":"state"}],"modelOptions":{"lossType":"lossType","modelType":"modelType","labels":["labels","labels"]}},"numTotalLogicalBytes":"numTotalLogicalBytes","id":"id","numTotalPhysicalBytes":"numTotalPhysicalBytes","friendlyName":"friendlyName","materializedView":{"refreshIntervalMs":"refreshIntervalMs","allowNonIncrementalDefinition":True,"enableRefresh":True,"maxStaleness":"maxStaleness","query":"query","lastRefreshTime":"lastRefreshTime"},"snapshotDefinition":{"baseTableReference":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"snapshotTime":"2000-01-23T04:56:07.000+00:00"},"tableReplicationInfo":{"replicatedSourceLastRefreshTime":"replicatedSourceLastRefreshTime","replicationError":{"reason":"reason","location":"location","debugInfo":"debugInfo","message":"message"},"sourceTable":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"replicationStatus":"REPLICATION_STATUS_UNSPECIFIED","replicationIntervalMs":"replicationIntervalMs"},"timePartitioning":{"field":"field","expirationMs":"expirationMs","requirePartitionFilter":False,"type":"type"},"streamingBuffer":{"estimatedBytes":"estimatedBytes","oldestEntryTime":"oldestEntryTime","estimatedRows":"estimatedRows"},"kind":"bigquery#table","replicas":[{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"}],"numActivePhysicalBytes":"numActivePhysicalBytes","numTimeTravelPhysicalBytes":"numTimeTravelPhysicalBytes","numLongTermPhysicalBytes":"numLongTermPhysicalBytes","tableConstraints":{"foreignKeys":[{"referencedTable":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"name":"name","columnReferences":[{"referencedColumn":"referencedColumn","referencingColumn":"referencingColumn"},{"referencedColumn":"referencedColumn","referencingColumn":"referencingColumn"}]},{"referencedTable":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"name":"name","columnReferences":[{"referencedColumn":"referencedColumn","referencingColumn":"referencingColumn"},{"referencedColumn":"referencedColumn","referencingColumn":"referencingColumn"}]}],"primaryKey":{"columns":["columns","columns"]}},"labels":{"key":"labels"},"selfLink":"selfLink","numPhysicalBytes":"numPhysicalBytes","cloneDefinition":{"baseTableReference":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"cloneTime":"2000-01-23T04:56:07.000+00:00"},"tableReference":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"expirationTime":"expirationTime","numPartitions":"numPartitions","rangePartitioning":{"field":"field","range":{"start":"start","end":"end","interval":"interval"}},"clustering":{"fields":["fields","fields"]},"etag":"etag","location":"location"}
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
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables'.format(project_id='project_id_example', dataset_id='dataset_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_tables_list(client):
    """Test case for bigquery_tables_list

    
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
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables'.format(project_id='project_id_example', dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_tables_patch(client):
    """Test case for bigquery_tables_patch

    
    """
    body = {"schema":{"fields":[{"defaultValueExpression":"defaultValueExpression","precision":"precision","description":"description","scale":"scale","type":"type","mode":"mode","policyTags":{"names":["names","names"]},"roundingMode":"ROUNDING_MODE_UNSPECIFIED","name":"name","categories":{"names":["names","names"]},"collation":"collation","fields":[null,null],"maxLength":"maxLength","rangeElementType":{"type":"type"}},{"defaultValueExpression":"defaultValueExpression","precision":"precision","description":"description","scale":"scale","type":"type","mode":"mode","policyTags":{"names":["names","names"]},"roundingMode":"ROUNDING_MODE_UNSPECIFIED","name":"name","categories":{"names":["names","names"]},"collation":"collation","fields":[null,null],"maxLength":"maxLength","rangeElementType":{"type":"type"}}]},"defaultRoundingMode":"ROUNDING_MODE_UNSPECIFIED","lastModifiedTime":"lastModifiedTime","materializedViewStatus":{"lastRefreshStatus":{"reason":"reason","location":"location","debugInfo":"debugInfo","message":"message"},"refreshWatermark":"refreshWatermark"},"creationTime":"creationTime","numRows":"numRows","description":"description","numLongTermLogicalBytes":"numLongTermLogicalBytes","requirePartitionFilter":False,"type":"type","defaultCollation":"defaultCollation","numBytes":"numBytes","resourceTags":{"key":"resourceTags"},"externalDataConfiguration":{"schema":{"fields":[{"defaultValueExpression":"defaultValueExpression","precision":"precision","description":"description","scale":"scale","type":"type","mode":"mode","policyTags":{"names":["names","names"]},"roundingMode":"ROUNDING_MODE_UNSPECIFIED","name":"name","categories":{"names":["names","names"]},"collation":"collation","fields":[null,null],"maxLength":"maxLength","rangeElementType":{"type":"type"}},{"defaultValueExpression":"defaultValueExpression","precision":"precision","description":"description","scale":"scale","type":"type","mode":"mode","policyTags":{"names":["names","names"]},"roundingMode":"ROUNDING_MODE_UNSPECIFIED","name":"name","categories":{"names":["names","names"]},"collation":"collation","fields":[null,null],"maxLength":"maxLength","rangeElementType":{"type":"type"}}]},"jsonExtension":"JSON_EXTENSION_UNSPECIFIED","objectMetadata":"OBJECT_METADATA_UNSPECIFIED","sourceUris":["sourceUris","sourceUris"],"decimalTargetTypes":["DECIMAL_TARGET_TYPE_UNSPECIFIED","DECIMAL_TARGET_TYPE_UNSPECIFIED"],"ignoreUnknownValues":True,"fileSetSpecType":"FILE_SET_SPEC_TYPE_FILE_SYSTEM_MATCH","jsonOptions":{"encoding":"encoding"},"googleSheetsOptions":{"skipLeadingRows":"skipLeadingRows","range":"range"},"metadataCacheMode":"METADATA_CACHE_MODE_UNSPECIFIED","avroOptions":{"useAvroLogicalTypes":True},"autodetect":True,"referenceFileSchemaUri":"referenceFileSchemaUri","hivePartitioningOptions":{"mode":"mode","sourceUriPrefix":"sourceUriPrefix","fields":["fields","fields"],"requirePartitionFilter":False},"bigtableOptions":{"columnFamilies":[{"familyId":"familyId","columns":[{"qualifierEncoded":"qualifierEncoded","fieldName":"fieldName","encoding":"encoding","qualifierString":"qualifierString","type":"type","onlyReadLatest":True},{"qualifierEncoded":"qualifierEncoded","fieldName":"fieldName","encoding":"encoding","qualifierString":"qualifierString","type":"type","onlyReadLatest":True}],"encoding":"encoding","type":"type","onlyReadLatest":True},{"familyId":"familyId","columns":[{"qualifierEncoded":"qualifierEncoded","fieldName":"fieldName","encoding":"encoding","qualifierString":"qualifierString","type":"type","onlyReadLatest":True},{"qualifierEncoded":"qualifierEncoded","fieldName":"fieldName","encoding":"encoding","qualifierString":"qualifierString","type":"type","onlyReadLatest":True}],"encoding":"encoding","type":"type","onlyReadLatest":True}],"ignoreUnspecifiedColumnFamilies":True,"outputColumnFamiliesAsJson":True,"readRowkeyAsString":True},"csvOptions":{"allowQuotedNewlines":True,"skipLeadingRows":"skipLeadingRows","quote":"\"","preserveAsciiControlCharacters":True,"nullMarker":"nullMarker","encoding":"encoding","fieldDelimiter":"fieldDelimiter","allowJaggedRows":True},"connectionId":"connectionId","compression":"compression","sourceFormat":"sourceFormat","maxBadRecords":0,"parquetOptions":{"enumAsString":True,"enableListInference":True}},"view":{"useExplicitColumnNames":True,"userDefinedFunctionResources":[{"resourceUri":"resourceUri","inlineCode":"inlineCode"},{"resourceUri":"resourceUri","inlineCode":"inlineCode"}],"privacyPolicy":{"aggregationThresholdPolicy":{"privacyUnitColumns":["privacyUnitColumns","privacyUnitColumns"],"threshold":"threshold"}},"query":"query","useLegacySql":True},"numLongTermBytes":"numLongTermBytes","maxStaleness":"maxStaleness","biglakeConfiguration":{"tableFormat":"TABLE_FORMAT_UNSPECIFIED","storageUri":"storageUri","connectionId":"connectionId","fileFormat":"FILE_FORMAT_UNSPECIFIED"},"numActiveLogicalBytes":"numActiveLogicalBytes","encryptionConfiguration":{"kmsKeyName":"kmsKeyName"},"model":{"trainingRuns":[{"trainingOptions":{"earlyStop":True,"l1Reg":2.3021358869347655,"maxIteration":"maxIteration","l2Reg":7.061401241503109,"learnRate":9.301444243932576,"lineSearchInitLearnRate":3.616076749251911,"warmStart":True,"learnRateStrategy":"learnRateStrategy","minRelProgress":2.027123023002322},"iterationResults":[{"index":1,"learnRate":5.962133916683182,"durationMs":"durationMs","evalLoss":6.027456183070403,"trainingLoss":5.637376656633329},{"index":1,"learnRate":5.962133916683182,"durationMs":"durationMs","evalLoss":6.027456183070403,"trainingLoss":5.637376656633329}],"startTime":"2000-01-23T04:56:07.000+00:00","state":"state"},{"trainingOptions":{"earlyStop":True,"l1Reg":2.3021358869347655,"maxIteration":"maxIteration","l2Reg":7.061401241503109,"learnRate":9.301444243932576,"lineSearchInitLearnRate":3.616076749251911,"warmStart":True,"learnRateStrategy":"learnRateStrategy","minRelProgress":2.027123023002322},"iterationResults":[{"index":1,"learnRate":5.962133916683182,"durationMs":"durationMs","evalLoss":6.027456183070403,"trainingLoss":5.637376656633329},{"index":1,"learnRate":5.962133916683182,"durationMs":"durationMs","evalLoss":6.027456183070403,"trainingLoss":5.637376656633329}],"startTime":"2000-01-23T04:56:07.000+00:00","state":"state"}],"modelOptions":{"lossType":"lossType","modelType":"modelType","labels":["labels","labels"]}},"numTotalLogicalBytes":"numTotalLogicalBytes","id":"id","numTotalPhysicalBytes":"numTotalPhysicalBytes","friendlyName":"friendlyName","materializedView":{"refreshIntervalMs":"refreshIntervalMs","allowNonIncrementalDefinition":True,"enableRefresh":True,"maxStaleness":"maxStaleness","query":"query","lastRefreshTime":"lastRefreshTime"},"snapshotDefinition":{"baseTableReference":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"snapshotTime":"2000-01-23T04:56:07.000+00:00"},"tableReplicationInfo":{"replicatedSourceLastRefreshTime":"replicatedSourceLastRefreshTime","replicationError":{"reason":"reason","location":"location","debugInfo":"debugInfo","message":"message"},"sourceTable":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"replicationStatus":"REPLICATION_STATUS_UNSPECIFIED","replicationIntervalMs":"replicationIntervalMs"},"timePartitioning":{"field":"field","expirationMs":"expirationMs","requirePartitionFilter":False,"type":"type"},"streamingBuffer":{"estimatedBytes":"estimatedBytes","oldestEntryTime":"oldestEntryTime","estimatedRows":"estimatedRows"},"kind":"bigquery#table","replicas":[{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"}],"numActivePhysicalBytes":"numActivePhysicalBytes","numTimeTravelPhysicalBytes":"numTimeTravelPhysicalBytes","numLongTermPhysicalBytes":"numLongTermPhysicalBytes","tableConstraints":{"foreignKeys":[{"referencedTable":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"name":"name","columnReferences":[{"referencedColumn":"referencedColumn","referencingColumn":"referencingColumn"},{"referencedColumn":"referencedColumn","referencingColumn":"referencingColumn"}]},{"referencedTable":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"name":"name","columnReferences":[{"referencedColumn":"referencedColumn","referencingColumn":"referencingColumn"},{"referencedColumn":"referencedColumn","referencingColumn":"referencingColumn"}]}],"primaryKey":{"columns":["columns","columns"]}},"labels":{"key":"labels"},"selfLink":"selfLink","numPhysicalBytes":"numPhysicalBytes","cloneDefinition":{"baseTableReference":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"cloneTime":"2000-01-23T04:56:07.000+00:00"},"tableReference":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"expirationTime":"expirationTime","numPartitions":"numPartitions","rangePartitioning":{"field":"field","range":{"start":"start","end":"end","interval":"interval"}},"clustering":{"fields":["fields","fields"]},"etag":"etag","location":"location"}
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
                    ('autodetect_schema', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}'.format(project_id='project_id_example', dataset_id='dataset_id_example', table_id='table_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_tables_set_iam_policy(client):
    """Test case for bigquery_tables_set_iam_policy

    
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
        path='/bigquery/v2/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_tables_test_iam_permissions(client):
    """Test case for bigquery_tables_test_iam_permissions

    
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
        path='/bigquery/v2/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_tables_update(client):
    """Test case for bigquery_tables_update

    
    """
    body = {"schema":{"fields":[{"defaultValueExpression":"defaultValueExpression","precision":"precision","description":"description","scale":"scale","type":"type","mode":"mode","policyTags":{"names":["names","names"]},"roundingMode":"ROUNDING_MODE_UNSPECIFIED","name":"name","categories":{"names":["names","names"]},"collation":"collation","fields":[null,null],"maxLength":"maxLength","rangeElementType":{"type":"type"}},{"defaultValueExpression":"defaultValueExpression","precision":"precision","description":"description","scale":"scale","type":"type","mode":"mode","policyTags":{"names":["names","names"]},"roundingMode":"ROUNDING_MODE_UNSPECIFIED","name":"name","categories":{"names":["names","names"]},"collation":"collation","fields":[null,null],"maxLength":"maxLength","rangeElementType":{"type":"type"}}]},"defaultRoundingMode":"ROUNDING_MODE_UNSPECIFIED","lastModifiedTime":"lastModifiedTime","materializedViewStatus":{"lastRefreshStatus":{"reason":"reason","location":"location","debugInfo":"debugInfo","message":"message"},"refreshWatermark":"refreshWatermark"},"creationTime":"creationTime","numRows":"numRows","description":"description","numLongTermLogicalBytes":"numLongTermLogicalBytes","requirePartitionFilter":False,"type":"type","defaultCollation":"defaultCollation","numBytes":"numBytes","resourceTags":{"key":"resourceTags"},"externalDataConfiguration":{"schema":{"fields":[{"defaultValueExpression":"defaultValueExpression","precision":"precision","description":"description","scale":"scale","type":"type","mode":"mode","policyTags":{"names":["names","names"]},"roundingMode":"ROUNDING_MODE_UNSPECIFIED","name":"name","categories":{"names":["names","names"]},"collation":"collation","fields":[null,null],"maxLength":"maxLength","rangeElementType":{"type":"type"}},{"defaultValueExpression":"defaultValueExpression","precision":"precision","description":"description","scale":"scale","type":"type","mode":"mode","policyTags":{"names":["names","names"]},"roundingMode":"ROUNDING_MODE_UNSPECIFIED","name":"name","categories":{"names":["names","names"]},"collation":"collation","fields":[null,null],"maxLength":"maxLength","rangeElementType":{"type":"type"}}]},"jsonExtension":"JSON_EXTENSION_UNSPECIFIED","objectMetadata":"OBJECT_METADATA_UNSPECIFIED","sourceUris":["sourceUris","sourceUris"],"decimalTargetTypes":["DECIMAL_TARGET_TYPE_UNSPECIFIED","DECIMAL_TARGET_TYPE_UNSPECIFIED"],"ignoreUnknownValues":True,"fileSetSpecType":"FILE_SET_SPEC_TYPE_FILE_SYSTEM_MATCH","jsonOptions":{"encoding":"encoding"},"googleSheetsOptions":{"skipLeadingRows":"skipLeadingRows","range":"range"},"metadataCacheMode":"METADATA_CACHE_MODE_UNSPECIFIED","avroOptions":{"useAvroLogicalTypes":True},"autodetect":True,"referenceFileSchemaUri":"referenceFileSchemaUri","hivePartitioningOptions":{"mode":"mode","sourceUriPrefix":"sourceUriPrefix","fields":["fields","fields"],"requirePartitionFilter":False},"bigtableOptions":{"columnFamilies":[{"familyId":"familyId","columns":[{"qualifierEncoded":"qualifierEncoded","fieldName":"fieldName","encoding":"encoding","qualifierString":"qualifierString","type":"type","onlyReadLatest":True},{"qualifierEncoded":"qualifierEncoded","fieldName":"fieldName","encoding":"encoding","qualifierString":"qualifierString","type":"type","onlyReadLatest":True}],"encoding":"encoding","type":"type","onlyReadLatest":True},{"familyId":"familyId","columns":[{"qualifierEncoded":"qualifierEncoded","fieldName":"fieldName","encoding":"encoding","qualifierString":"qualifierString","type":"type","onlyReadLatest":True},{"qualifierEncoded":"qualifierEncoded","fieldName":"fieldName","encoding":"encoding","qualifierString":"qualifierString","type":"type","onlyReadLatest":True}],"encoding":"encoding","type":"type","onlyReadLatest":True}],"ignoreUnspecifiedColumnFamilies":True,"outputColumnFamiliesAsJson":True,"readRowkeyAsString":True},"csvOptions":{"allowQuotedNewlines":True,"skipLeadingRows":"skipLeadingRows","quote":"\"","preserveAsciiControlCharacters":True,"nullMarker":"nullMarker","encoding":"encoding","fieldDelimiter":"fieldDelimiter","allowJaggedRows":True},"connectionId":"connectionId","compression":"compression","sourceFormat":"sourceFormat","maxBadRecords":0,"parquetOptions":{"enumAsString":True,"enableListInference":True}},"view":{"useExplicitColumnNames":True,"userDefinedFunctionResources":[{"resourceUri":"resourceUri","inlineCode":"inlineCode"},{"resourceUri":"resourceUri","inlineCode":"inlineCode"}],"privacyPolicy":{"aggregationThresholdPolicy":{"privacyUnitColumns":["privacyUnitColumns","privacyUnitColumns"],"threshold":"threshold"}},"query":"query","useLegacySql":True},"numLongTermBytes":"numLongTermBytes","maxStaleness":"maxStaleness","biglakeConfiguration":{"tableFormat":"TABLE_FORMAT_UNSPECIFIED","storageUri":"storageUri","connectionId":"connectionId","fileFormat":"FILE_FORMAT_UNSPECIFIED"},"numActiveLogicalBytes":"numActiveLogicalBytes","encryptionConfiguration":{"kmsKeyName":"kmsKeyName"},"model":{"trainingRuns":[{"trainingOptions":{"earlyStop":True,"l1Reg":2.3021358869347655,"maxIteration":"maxIteration","l2Reg":7.061401241503109,"learnRate":9.301444243932576,"lineSearchInitLearnRate":3.616076749251911,"warmStart":True,"learnRateStrategy":"learnRateStrategy","minRelProgress":2.027123023002322},"iterationResults":[{"index":1,"learnRate":5.962133916683182,"durationMs":"durationMs","evalLoss":6.027456183070403,"trainingLoss":5.637376656633329},{"index":1,"learnRate":5.962133916683182,"durationMs":"durationMs","evalLoss":6.027456183070403,"trainingLoss":5.637376656633329}],"startTime":"2000-01-23T04:56:07.000+00:00","state":"state"},{"trainingOptions":{"earlyStop":True,"l1Reg":2.3021358869347655,"maxIteration":"maxIteration","l2Reg":7.061401241503109,"learnRate":9.301444243932576,"lineSearchInitLearnRate":3.616076749251911,"warmStart":True,"learnRateStrategy":"learnRateStrategy","minRelProgress":2.027123023002322},"iterationResults":[{"index":1,"learnRate":5.962133916683182,"durationMs":"durationMs","evalLoss":6.027456183070403,"trainingLoss":5.637376656633329},{"index":1,"learnRate":5.962133916683182,"durationMs":"durationMs","evalLoss":6.027456183070403,"trainingLoss":5.637376656633329}],"startTime":"2000-01-23T04:56:07.000+00:00","state":"state"}],"modelOptions":{"lossType":"lossType","modelType":"modelType","labels":["labels","labels"]}},"numTotalLogicalBytes":"numTotalLogicalBytes","id":"id","numTotalPhysicalBytes":"numTotalPhysicalBytes","friendlyName":"friendlyName","materializedView":{"refreshIntervalMs":"refreshIntervalMs","allowNonIncrementalDefinition":True,"enableRefresh":True,"maxStaleness":"maxStaleness","query":"query","lastRefreshTime":"lastRefreshTime"},"snapshotDefinition":{"baseTableReference":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"snapshotTime":"2000-01-23T04:56:07.000+00:00"},"tableReplicationInfo":{"replicatedSourceLastRefreshTime":"replicatedSourceLastRefreshTime","replicationError":{"reason":"reason","location":"location","debugInfo":"debugInfo","message":"message"},"sourceTable":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"replicationStatus":"REPLICATION_STATUS_UNSPECIFIED","replicationIntervalMs":"replicationIntervalMs"},"timePartitioning":{"field":"field","expirationMs":"expirationMs","requirePartitionFilter":False,"type":"type"},"streamingBuffer":{"estimatedBytes":"estimatedBytes","oldestEntryTime":"oldestEntryTime","estimatedRows":"estimatedRows"},"kind":"bigquery#table","replicas":[{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"}],"numActivePhysicalBytes":"numActivePhysicalBytes","numTimeTravelPhysicalBytes":"numTimeTravelPhysicalBytes","numLongTermPhysicalBytes":"numLongTermPhysicalBytes","tableConstraints":{"foreignKeys":[{"referencedTable":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"name":"name","columnReferences":[{"referencedColumn":"referencedColumn","referencingColumn":"referencingColumn"},{"referencedColumn":"referencedColumn","referencingColumn":"referencingColumn"}]},{"referencedTable":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"name":"name","columnReferences":[{"referencedColumn":"referencedColumn","referencingColumn":"referencingColumn"},{"referencedColumn":"referencedColumn","referencingColumn":"referencingColumn"}]}],"primaryKey":{"columns":["columns","columns"]}},"labels":{"key":"labels"},"selfLink":"selfLink","numPhysicalBytes":"numPhysicalBytes","cloneDefinition":{"baseTableReference":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"cloneTime":"2000-01-23T04:56:07.000+00:00"},"tableReference":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"expirationTime":"expirationTime","numPartitions":"numPartitions","rangePartitioning":{"field":"field","range":{"start":"start","end":"end","interval":"interval"}},"clustering":{"fields":["fields","fields"]},"etag":"etag","location":"location"}
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
                    ('autodetect_schema', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}'.format(project_id='project_id_example', dataset_id='dataset_id_example', table_id='table_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

