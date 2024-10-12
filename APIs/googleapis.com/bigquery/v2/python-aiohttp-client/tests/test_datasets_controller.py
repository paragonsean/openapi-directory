# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dataset import Dataset
from openapi_server.models.dataset_list import DatasetList
from openapi_server.models.undelete_dataset_request import UndeleteDatasetRequest


pytestmark = pytest.mark.asyncio

async def test_bigquery_datasets_delete(client):
    """Test case for bigquery_datasets_delete

    
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
                    ('deleteContents', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}'.format(project_id='project_id_example', dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_datasets_get(client):
    """Test case for bigquery_datasets_get

    
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
                    ('datasetView', 'dataset_view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}'.format(project_id='project_id_example', dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_datasets_insert(client):
    """Test case for bigquery_datasets_insert

    
    """
    body = {"defaultRoundingMode":"ROUNDING_MODE_UNSPECIFIED","access":[{"view":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"role":"role","routine":{"datasetId":"datasetId","projectId":"projectId","routineId":"routineId"},"userByEmail":"userByEmail","domain":"domain","specialGroup":"specialGroup","dataset":{"dataset":{"datasetId":"datasetId","projectId":"projectId"},"targetTypes":["TARGET_TYPE_UNSPECIFIED","TARGET_TYPE_UNSPECIFIED"]},"iamMember":"iamMember","groupByEmail":"groupByEmail"},{"view":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"role":"role","routine":{"datasetId":"datasetId","projectId":"projectId","routineId":"routineId"},"userByEmail":"userByEmail","domain":"domain","specialGroup":"specialGroup","dataset":{"dataset":{"datasetId":"datasetId","projectId":"projectId"},"targetTypes":["TARGET_TYPE_UNSPECIFIED","TARGET_TYPE_UNSPECIFIED"]},"iamMember":"iamMember","groupByEmail":"groupByEmail"}],"lastModifiedTime":"lastModifiedTime","creationTime":"creationTime","description":"description","satisfiesPzs":True,"storageBillingModel":"STORAGE_BILLING_MODEL_UNSPECIFIED","type":"type","defaultCollation":"defaultCollation","linkedDatasetSource":{"sourceDataset":{"datasetId":"datasetId","projectId":"projectId"}},"id":"id","friendlyName":"friendlyName","defaultEncryptionConfiguration":{"kmsKeyName":"kmsKeyName"},"kind":"bigquery#dataset","isCaseInsensitive":True,"datasetReference":{"datasetId":"datasetId","projectId":"projectId"},"labels":{"key":"labels"},"selfLink":"selfLink","tags":[{"tagValue":"tagValue","tagKey":"tagKey"},{"tagValue":"tagValue","tagKey":"tagKey"}],"defaultPartitionExpirationMs":"defaultPartitionExpirationMs","maxTimeTravelHours":"maxTimeTravelHours","externalDatasetReference":{"connection":"connection","externalSource":"externalSource"},"etag":"etag","location":"location","defaultTableExpirationMs":"defaultTableExpirationMs","satisfiesPzi":True}
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
        path='/bigquery/v2/projects/{project_id}/datasets'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_datasets_list(client):
    """Test case for bigquery_datasets_list

    
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
                    ('all', True),
                    ('filter', 'filter_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bigquery/v2/projects/{project_id}/datasets'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_datasets_patch(client):
    """Test case for bigquery_datasets_patch

    
    """
    body = {"defaultRoundingMode":"ROUNDING_MODE_UNSPECIFIED","access":[{"view":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"role":"role","routine":{"datasetId":"datasetId","projectId":"projectId","routineId":"routineId"},"userByEmail":"userByEmail","domain":"domain","specialGroup":"specialGroup","dataset":{"dataset":{"datasetId":"datasetId","projectId":"projectId"},"targetTypes":["TARGET_TYPE_UNSPECIFIED","TARGET_TYPE_UNSPECIFIED"]},"iamMember":"iamMember","groupByEmail":"groupByEmail"},{"view":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"role":"role","routine":{"datasetId":"datasetId","projectId":"projectId","routineId":"routineId"},"userByEmail":"userByEmail","domain":"domain","specialGroup":"specialGroup","dataset":{"dataset":{"datasetId":"datasetId","projectId":"projectId"},"targetTypes":["TARGET_TYPE_UNSPECIFIED","TARGET_TYPE_UNSPECIFIED"]},"iamMember":"iamMember","groupByEmail":"groupByEmail"}],"lastModifiedTime":"lastModifiedTime","creationTime":"creationTime","description":"description","satisfiesPzs":True,"storageBillingModel":"STORAGE_BILLING_MODEL_UNSPECIFIED","type":"type","defaultCollation":"defaultCollation","linkedDatasetSource":{"sourceDataset":{"datasetId":"datasetId","projectId":"projectId"}},"id":"id","friendlyName":"friendlyName","defaultEncryptionConfiguration":{"kmsKeyName":"kmsKeyName"},"kind":"bigquery#dataset","isCaseInsensitive":True,"datasetReference":{"datasetId":"datasetId","projectId":"projectId"},"labels":{"key":"labels"},"selfLink":"selfLink","tags":[{"tagValue":"tagValue","tagKey":"tagKey"},{"tagValue":"tagValue","tagKey":"tagKey"}],"defaultPartitionExpirationMs":"defaultPartitionExpirationMs","maxTimeTravelHours":"maxTimeTravelHours","externalDatasetReference":{"connection":"connection","externalSource":"externalSource"},"etag":"etag","location":"location","defaultTableExpirationMs":"defaultTableExpirationMs","satisfiesPzi":True}
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
        method='PATCH',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}'.format(project_id='project_id_example', dataset_id='dataset_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_datasets_undelete(client):
    """Test case for bigquery_datasets_undelete

    
    """
    body = {"deletionTime":"deletionTime"}
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
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_idundelet}'.format(project_id='project_id_example', dataset_id='dataset_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_datasets_update(client):
    """Test case for bigquery_datasets_update

    
    """
    body = {"defaultRoundingMode":"ROUNDING_MODE_UNSPECIFIED","access":[{"view":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"role":"role","routine":{"datasetId":"datasetId","projectId":"projectId","routineId":"routineId"},"userByEmail":"userByEmail","domain":"domain","specialGroup":"specialGroup","dataset":{"dataset":{"datasetId":"datasetId","projectId":"projectId"},"targetTypes":["TARGET_TYPE_UNSPECIFIED","TARGET_TYPE_UNSPECIFIED"]},"iamMember":"iamMember","groupByEmail":"groupByEmail"},{"view":{"datasetId":"datasetId","tableId":"tableId","projectId":"projectId"},"role":"role","routine":{"datasetId":"datasetId","projectId":"projectId","routineId":"routineId"},"userByEmail":"userByEmail","domain":"domain","specialGroup":"specialGroup","dataset":{"dataset":{"datasetId":"datasetId","projectId":"projectId"},"targetTypes":["TARGET_TYPE_UNSPECIFIED","TARGET_TYPE_UNSPECIFIED"]},"iamMember":"iamMember","groupByEmail":"groupByEmail"}],"lastModifiedTime":"lastModifiedTime","creationTime":"creationTime","description":"description","satisfiesPzs":True,"storageBillingModel":"STORAGE_BILLING_MODEL_UNSPECIFIED","type":"type","defaultCollation":"defaultCollation","linkedDatasetSource":{"sourceDataset":{"datasetId":"datasetId","projectId":"projectId"}},"id":"id","friendlyName":"friendlyName","defaultEncryptionConfiguration":{"kmsKeyName":"kmsKeyName"},"kind":"bigquery#dataset","isCaseInsensitive":True,"datasetReference":{"datasetId":"datasetId","projectId":"projectId"},"labels":{"key":"labels"},"selfLink":"selfLink","tags":[{"tagValue":"tagValue","tagKey":"tagKey"},{"tagValue":"tagValue","tagKey":"tagKey"}],"defaultPartitionExpirationMs":"defaultPartitionExpirationMs","maxTimeTravelHours":"maxTimeTravelHours","externalDatasetReference":{"connection":"connection","externalSource":"externalSource"},"etag":"etag","location":"location","defaultTableExpirationMs":"defaultTableExpirationMs","satisfiesPzi":True}
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
        method='PUT',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}'.format(project_id='project_id_example', dataset_id='dataset_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

