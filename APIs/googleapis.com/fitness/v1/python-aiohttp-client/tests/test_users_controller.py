# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aggregate_request import AggregateRequest
from openapi_server.models.aggregate_response import AggregateResponse
from openapi_server.models.data_source import DataSource
from openapi_server.models.dataset import Dataset
from openapi_server.models.list_data_point_changes_response import ListDataPointChangesResponse
from openapi_server.models.list_data_sources_response import ListDataSourcesResponse
from openapi_server.models.list_sessions_response import ListSessionsResponse
from openapi_server.models.session import Session


pytestmark = pytest.mark.asyncio

async def test_fitness_users_data_sources_create(client):
    """Test case for fitness_users_data_sources_create

    
    """
    body = {"dataStreamName":"dataStreamName","application":{"detailsUrl":"detailsUrl","name":"name","packageName":"packageName","version":"version"},"dataType":{"field":[{"format":"integer","name":"name","optional":True},{"format":"integer","name":"name","optional":True}],"name":"name"},"name":"name","dataQualityStandard":["dataQualityUnknown","dataQualityUnknown"],"type":"raw","device":{"uid":"uid","model":"model","type":"unknown","version":"version","manufacturer":"manufacturer"},"dataStreamId":"dataStreamId"}
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
        path='/fitness/v1/users/{user_id}/dataSources'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fitness_users_data_sources_data_point_changes_list(client):
    """Test case for fitness_users_data_sources_data_point_changes_list

    
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
                    ('limit', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/fitness/v1/users/{user_id}/dataSources/{data_source_id}/dataPointChanges'.format(user_id='user_id_example', data_source_id='data_source_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fitness_users_data_sources_datasets_delete(client):
    """Test case for fitness_users_data_sources_datasets_delete

    
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
        path='/fitness/v1/users/{user_id}/dataSources/{data_source_id}/datasets/{dataset_id}'.format(user_id='user_id_example', data_source_id='data_source_id_example', dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fitness_users_data_sources_datasets_get(client):
    """Test case for fitness_users_data_sources_datasets_get

    
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
                    ('limit', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/fitness/v1/users/{user_id}/dataSources/{data_source_id}/datasets/{dataset_id}'.format(user_id='user_id_example', data_source_id='data_source_id_example', dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fitness_users_data_sources_datasets_patch(client):
    """Test case for fitness_users_data_sources_datasets_patch

    
    """
    body = {"dataSourceId":"dataSourceId","maxEndTimeNs":"maxEndTimeNs","minStartTimeNs":"minStartTimeNs","nextPageToken":"nextPageToken","point":[{"originDataSourceId":"originDataSourceId","endTimeNanos":"endTimeNanos","dataTypeName":"dataTypeName","startTimeNanos":"startTimeNanos","modifiedTimeMillis":"modifiedTimeMillis","rawTimestampNanos":"rawTimestampNanos","computationTimeMillis":"computationTimeMillis","value":[{"intVal":6,"fpVal":0.8008281904610115,"stringVal":"stringVal","mapVal":[{"value":{"fpVal":1.4658129805029452},"key":"key"},{"value":{"fpVal":1.4658129805029452},"key":"key"}]},{"intVal":6,"fpVal":0.8008281904610115,"stringVal":"stringVal","mapVal":[{"value":{"fpVal":1.4658129805029452},"key":"key"},{"value":{"fpVal":1.4658129805029452},"key":"key"}]}]},{"originDataSourceId":"originDataSourceId","endTimeNanos":"endTimeNanos","dataTypeName":"dataTypeName","startTimeNanos":"startTimeNanos","modifiedTimeMillis":"modifiedTimeMillis","rawTimestampNanos":"rawTimestampNanos","computationTimeMillis":"computationTimeMillis","value":[{"intVal":6,"fpVal":0.8008281904610115,"stringVal":"stringVal","mapVal":[{"value":{"fpVal":1.4658129805029452},"key":"key"},{"value":{"fpVal":1.4658129805029452},"key":"key"}]},{"intVal":6,"fpVal":0.8008281904610115,"stringVal":"stringVal","mapVal":[{"value":{"fpVal":1.4658129805029452},"key":"key"},{"value":{"fpVal":1.4658129805029452},"key":"key"}]}]}]}
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
        path='/fitness/v1/users/{user_id}/dataSources/{data_source_id}/datasets/{dataset_id}'.format(user_id='user_id_example', data_source_id='data_source_id_example', dataset_id='dataset_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fitness_users_data_sources_delete(client):
    """Test case for fitness_users_data_sources_delete

    
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
        method='DELETE',
        path='/fitness/v1/users/{user_id}/dataSources/{data_source_id}'.format(user_id='user_id_example', data_source_id='data_source_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fitness_users_data_sources_get(client):
    """Test case for fitness_users_data_sources_get

    
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
        method='GET',
        path='/fitness/v1/users/{user_id}/dataSources/{data_source_id}'.format(user_id='user_id_example', data_source_id='data_source_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fitness_users_data_sources_list(client):
    """Test case for fitness_users_data_sources_list

    
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
                    ('dataTypeName', ['data_type_name_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/fitness/v1/users/{user_id}/dataSources'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fitness_users_data_sources_update(client):
    """Test case for fitness_users_data_sources_update

    
    """
    body = {"dataStreamName":"dataStreamName","application":{"detailsUrl":"detailsUrl","name":"name","packageName":"packageName","version":"version"},"dataType":{"field":[{"format":"integer","name":"name","optional":True},{"format":"integer","name":"name","optional":True}],"name":"name"},"name":"name","dataQualityStandard":["dataQualityUnknown","dataQualityUnknown"],"type":"raw","device":{"uid":"uid","model":"model","type":"unknown","version":"version","manufacturer":"manufacturer"},"dataStreamId":"dataStreamId"}
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
        path='/fitness/v1/users/{user_id}/dataSources/{data_source_id}'.format(user_id='user_id_example', data_source_id='data_source_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fitness_users_dataset_aggregate(client):
    """Test case for fitness_users_dataset_aggregate

    
    """
    body = {"bucketBySession":{"minDurationMillis":"minDurationMillis"},"endTimeMillis":"endTimeMillis","startTimeMillis":"startTimeMillis","bucketByActivitySegment":{"minDurationMillis":"minDurationMillis","activityDataSourceId":"activityDataSourceId"},"bucketByActivityType":{"minDurationMillis":"minDurationMillis","activityDataSourceId":"activityDataSourceId"},"filteredDataQualityStandard":["dataQualityUnknown","dataQualityUnknown"],"bucketByTime":{"period":{"timeZoneId":"timeZoneId","type":"day","value":0},"durationMillis":"durationMillis"},"aggregateBy":[{"dataSourceId":"dataSourceId","dataTypeName":"dataTypeName"},{"dataSourceId":"dataSourceId","dataTypeName":"dataTypeName"}]}
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
        path='/fitness/v1/users/{user_id}/dataset:aggregate'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fitness_users_sessions_delete(client):
    """Test case for fitness_users_sessions_delete

    
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
        path='/fitness/v1/users/{user_id}/sessions/{session_id}'.format(user_id='user_id_example', session_id='session_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fitness_users_sessions_list(client):
    """Test case for fitness_users_sessions_list

    
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
                    ('activityType', [56]),
                    ('endTime', 'end_time_example'),
                    ('includeDeleted', True),
                    ('pageToken', 'page_token_example'),
                    ('startTime', 'start_time_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/fitness/v1/users/{user_id}/sessions'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fitness_users_sessions_update(client):
    """Test case for fitness_users_sessions_update

    
    """
    body = {"activeTimeMillis":"activeTimeMillis","endTimeMillis":"endTimeMillis","application":{"detailsUrl":"detailsUrl","name":"name","packageName":"packageName","version":"version"},"startTimeMillis":"startTimeMillis","name":"name","description":"description","modifiedTimeMillis":"modifiedTimeMillis","id":"id","activityType":6}
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
        path='/fitness/v1/users/{user_id}/sessions/{session_id}'.format(user_id='user_id_example', session_id='session_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

