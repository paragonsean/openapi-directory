# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aggregate_datasets200_response import AggregateDatasets200Response
from openapi_server.models.get_dataset_attachements200_response import GetDatasetAttachements200Response
from openapi_server.models.get_dataset_reuse200_response import GetDatasetReuse200Response
from openapi_server.models.get_dataset_reuses200_response import GetDatasetReuses200Response
from openapi_server.models.get_dataset_snapshots200_response import GetDatasetSnapshots200Response
from openapi_server.models.get_datasets200_response_datasets_inner import GetDatasets200ResponseDatasetsInner
from openapi_server.models.get_records200_response import GetRecords200Response
from openapi_server.models.get_records200_response_records_inner import GetRecords200ResponseRecordsInner
from openapi_server.models.get_records_facets200_response import GetRecordsFacets200Response
from openapi_server.models.send_dataset_feedback_request import SendDatasetFeedbackRequest


pytestmark = pytest.mark.asyncio

async def test_aggregate_records(client):
    """Test case for aggregate_records

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('group_by', 'group_by_example'),
                    ('order_by', ['order_by_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/aggregates'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_dataset_attachement(client):
    """Test case for download_dataset_attachement

    
    """
    headers = { 
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/attachments/{attachment_id}'.format(source=catalog, dataset_id='dataset_id_example', attachment_id='attachment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_dataset_snapshot(client):
    """Test case for download_dataset_snapshot

    
    """
    params = [('timezone', 'UTC')]
    headers = { 
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/snapshots/{snapshot_id}'.format(source=catalog, dataset_id='dataset_id_example', snapshot_id='snapshot_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dataset(client):
    """Test case for get_dataset

    
    """
    params = [('select', 'select_example'),
                    ('pretty', False),
                    ('timezone', 'UTC'),
                    ('include_app_metas', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dataset_attachements(client):
    """Test case for get_dataset_attachements

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/attachments'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dataset_file(client):
    """Test case for get_dataset_file

    
    """
    params = [('thumbnail_size', 'thumbnail_size_example')]
    headers = { 
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/files/{file_id}'.format(source=catalog, dataset_id='dataset_id_example', file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dataset_reuse(client):
    """Test case for get_dataset_reuse

    
    """
    params = [('timezone', 'UTC')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/reuses/{reuse_id}'.format(source=catalog, dataset_id='dataset_id_example', reuse_id='reuse_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dataset_reuses(client):
    """Test case for get_dataset_reuses

    
    """
    params = [('limit', 10),
                    ('offset', 0),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/reuses'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dataset_snapshots(client):
    """Test case for get_dataset_snapshots

    
    """
    params = [('timezone', 'UTC')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/snapshots'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_record(client):
    """Test case for get_record

    
    """
    params = [('select', 'select_example'),
                    ('pretty', False),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/records/{record_id}'.format(source=catalog, dataset_id='dataset_id_example', record_id='record_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_records(client):
    """Test case for get_records

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('group_by', 'group_by_example'),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('pretty', False),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/records'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_records_facets(client):
    """Test case for get_records_facets

    
    """
    params = [('where', ['where_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('search', ['search_example']),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/facets'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_send_dataset_feedback(client):
    """Test case for send_dataset_feedback

    
    """
    feedback = openapi_server.SendDatasetFeedbackRequest()
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/{source}/datasets/{dataset_id}/feedback'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        json=feedback,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

