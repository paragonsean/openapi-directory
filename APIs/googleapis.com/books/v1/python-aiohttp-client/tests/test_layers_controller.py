# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.annotationsdata import Annotationsdata
from openapi_server.models.dictionary_annotationdata import DictionaryAnnotationdata
from openapi_server.models.layersummaries import Layersummaries
from openapi_server.models.layersummary import Layersummary
from openapi_server.models.volumeannotation import Volumeannotation
from openapi_server.models.volumeannotations import Volumeannotations


pytestmark = pytest.mark.asyncio

async def test_books_layers_annotation_data_get(client):
    """Test case for books_layers_annotation_data_get

    
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
                    ('contentVersion', 'content_version_example'),
                    ('allowWebDefinitions', True),
                    ('h', 56),
                    ('locale', 'locale_example'),
                    ('scale', 56),
                    ('source', 'source_example'),
                    ('w', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/books/v1/volumes/{volume_id}/layers/{layer_id}/data/{annotation_data_id}'.format(volume_id='volume_id_example', layer_id='layer_id_example', annotation_data_id='annotation_data_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_layers_annotation_data_list(client):
    """Test case for books_layers_annotation_data_list

    
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
                    ('contentVersion', 'content_version_example'),
                    ('annotationDataId', ['annotation_data_id_example']),
                    ('h', 56),
                    ('locale', 'locale_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('scale', 56),
                    ('source', 'source_example'),
                    ('updatedMax', 'updated_max_example'),
                    ('updatedMin', 'updated_min_example'),
                    ('w', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/books/v1/volumes/{volume_id}/layers/{layer_id}/data'.format(volume_id='volume_id_example', layer_id='layer_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_layers_get(client):
    """Test case for books_layers_get

    
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
                    ('contentVersion', 'content_version_example'),
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/books/v1/volumes/{volume_id}/layersummary/{summary_id}'.format(volume_id='volume_id_example', summary_id='summary_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_layers_list(client):
    """Test case for books_layers_list

    
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
                    ('contentVersion', 'content_version_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/books/v1/volumes/{volume_id}/layersummary'.format(volume_id='volume_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_layers_volume_annotations_get(client):
    """Test case for books_layers_volume_annotations_get

    
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
                    ('locale', 'locale_example'),
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/books/v1/volumes/{volume_id}/layers/{layer_id}/annotations/{annotation_id}'.format(volume_id='volume_id_example', layer_id='layer_id_example', annotation_id='annotation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_layers_volume_annotations_list(client):
    """Test case for books_layers_volume_annotations_list

    
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
                    ('contentVersion', 'content_version_example'),
                    ('endOffset', 'end_offset_example'),
                    ('endPosition', 'end_position_example'),
                    ('locale', 'locale_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('showDeleted', True),
                    ('source', 'source_example'),
                    ('startOffset', 'start_offset_example'),
                    ('startPosition', 'start_position_example'),
                    ('updatedMax', 'updated_max_example'),
                    ('updatedMin', 'updated_min_example'),
                    ('volumeAnnotationsVersion', 'volume_annotations_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/books/v1/volumes/{volume_id}/layers/{layer_id}'.format(volume_id='volume_id_example', layer_id='layer_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

