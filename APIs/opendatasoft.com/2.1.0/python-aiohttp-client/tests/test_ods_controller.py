# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aggregate_datasets200_response import AggregateDatasets200Response
from openapi_server.models.get_dataset_attachements200_response import GetDatasetAttachements200Response
from openapi_server.models.get_dataset_reuse200_response import GetDatasetReuse200Response
from openapi_server.models.get_dataset_reuses200_response import GetDatasetReuses200Response
from openapi_server.models.get_dataset_snapshots200_response import GetDatasetSnapshots200Response
from openapi_server.models.get_datasets200_response import GetDatasets200Response
from openapi_server.models.get_datasets200_response_datasets_inner import GetDatasets200ResponseDatasetsInner
from openapi_server.models.get_metadata_templates_type200_response import GetMetadataTemplatesType200Response
from openapi_server.models.get_metadata_templates_type200_response_metadata_templates_inner import GetMetadataTemplatesType200ResponseMetadataTemplatesInner
from openapi_server.models.get_pages200_response import GetPages200Response
from openapi_server.models.get_pages200_response_pages_inner import GetPages200ResponsePagesInner
from openapi_server.models.get_records200_response import GetRecords200Response
from openapi_server.models.get_records200_response_records_inner import GetRecords200ResponseRecordsInner
from openapi_server.models.get_records_facets200_response import GetRecordsFacets200Response
from openapi_server.models.get_root200_response import GetRoot200Response
from openapi_server.models.send_dataset_feedback_request import SendDatasetFeedbackRequest


pytestmark = pytest.mark.asyncio

async def test_aggregate_datasets_1(client):
    """Test case for aggregate_datasets_1

    
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
        path='/api/v2/{source}/aggregates'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aggregate_records_1(client):
    """Test case for aggregate_records_1

    
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

async def test_download_dataset_attachement_0(client):
    """Test case for download_dataset_attachement_0

    
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

async def test_download_dataset_snapshot_0(client):
    """Test case for download_dataset_snapshot_0

    
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

async def test_export_datasets_csv_0(client):
    """Test case for export_datasets_csv_0

    
    """
    params = [('where', ['where_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC'),
                    ('include_app_metas', False),
                    ('delimiter', ;)]
    headers = { 
        'Accept': 'text/csv',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/exports/csv'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_datasets_json_0(client):
    """Test case for export_datasets_json_0

    
    """
    params = [('where', ['where_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
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
        path='/api/v2/{source}/exports/json'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_datasets_rdf_0(client):
    """Test case for export_datasets_rdf_0

    
    """
    params = [('where', ['where_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC'),
                    ('include_app_metas', False)]
    headers = { 
        'Accept': 'application/rdf+xml',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/exports/rdf'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_datasets_rss_0(client):
    """Test case for export_datasets_rss_0

    
    """
    params = [('where', ['where_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC'),
                    ('include_app_metas', False)]
    headers = { 
        'Accept': 'text/xml',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/exports/rss'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_datasets_ttl_0(client):
    """Test case for export_datasets_ttl_0

    
    """
    params = [('where', ['where_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC'),
                    ('include_app_metas', False)]
    headers = { 
        'Accept': 'text/turtle',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/exports/ttl'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_datasets_xls_0(client):
    """Test case for export_datasets_xls_0

    
    """
    params = [('where', ['where_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC'),
                    ('include_app_metas', False)]
    headers = { 
        'Accept': 'xls',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/exports/xls'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_records_csv_0(client):
    """Test case for export_records_csv_0

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', -1),
                    ('offset', 0),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC'),
                    ('delimiter', ;)]
    headers = { 
        'Accept': 'text/csv',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/exports/csv'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_records_geojson_0(client):
    """Test case for export_records_geojson_0

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', -1),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC'),
                    ('pretty', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/exports/geojson'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_records_ical_0(client):
    """Test case for export_records_ical_0

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', -1),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/exports/ical'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_records_json_0(client):
    """Test case for export_records_json_0

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', -1),
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
        path='/api/v2/{source}/datasets/{dataset_id}/exports/json'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_records_ov2_0(client):
    """Test case for export_records_ov2_0

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', -1),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'text/plain',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/exports/ov2'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_records_shp_0(client):
    """Test case for export_records_shp_0

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', -1),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'application/zip',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/exports/shp'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_records_xls_0(client):
    """Test case for export_records_xls_0

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', -1),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'xls',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/exports/xls'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dataset_0(client):
    """Test case for get_dataset_0

    
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

async def test_get_dataset_attachements_0(client):
    """Test case for get_dataset_attachements_0

    
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

async def test_get_dataset_file_0(client):
    """Test case for get_dataset_file_0

    
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

async def test_get_dataset_reuse_0(client):
    """Test case for get_dataset_reuse_0

    
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

async def test_get_dataset_reuses_0(client):
    """Test case for get_dataset_reuses_0

    
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

async def test_get_dataset_snapshots_0(client):
    """Test case for get_dataset_snapshots_0

    
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

async def test_get_datasets_0(client):
    """Test case for get_datasets_0

    
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
                    ('timezone', 'UTC'),
                    ('include_app_metas', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_datasets_facets_1(client):
    """Test case for get_datasets_facets_1

    
    """
    params = [('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('where', ['where_example']),
                    ('search', ['search_example']),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/facets'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_metadata_template_0(client):
    """Test case for get_metadata_template_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/metadata_templates/{metadata_template_type}/{metadata_template_name}'.format(source=catalog, metadata_template_type=basic, metadata_template_name='metadata_template_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_metadata_templates_type_0(client):
    """Test case for get_metadata_templates_type_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/metadata_templates/{metadata_template_type}'.format(source=catalog, metadata_template_type=basic),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_metadata_templates_types_0(client):
    """Test case for get_metadata_templates_types_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/metadata_templates'.format(source=catalog),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_page_0(client):
    """Test case for get_page_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/pages/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pages_0(client):
    """Test case for get_pages_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/pages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_record_0(client):
    """Test case for get_record_0

    
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

async def test_get_records_0(client):
    """Test case for get_records_0

    
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

async def test_get_records_facets_1(client):
    """Test case for get_records_facets_1

    
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

async def test_get_root_0(client):
    """Test case for get_root_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_source_0(client):
    """Test case for get_source_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}'.format(source=catalog),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_send_dataset_feedback_0(client):
    """Test case for send_dataset_feedback_0

    
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

