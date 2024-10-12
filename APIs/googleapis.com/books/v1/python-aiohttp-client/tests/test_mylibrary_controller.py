# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.annotation import Annotation
from openapi_server.models.annotations import Annotations
from openapi_server.models.annotations_summary import AnnotationsSummary
from openapi_server.models.bookshelf import Bookshelf
from openapi_server.models.bookshelves import Bookshelves
from openapi_server.models.reading_position import ReadingPosition
from openapi_server.models.volumes import Volumes


pytestmark = pytest.mark.asyncio

async def test_books_mylibrary_annotations_delete(client):
    """Test case for books_mylibrary_annotations_delete

    
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
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/books/v1/mylibrary/annotations/{annotation_id}'.format(annotation_id='annotation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_mylibrary_annotations_insert(client):
    """Test case for books_mylibrary_annotations_insert

    
    """
    body = {"layerSummary":{"allowedCharacterCount":0,"limitType":"limitType","remainingCharacterCount":6},"data":"data","selectedText":"selectedText","created":"created","kind":"kind","beforeSelectedText":"beforeSelectedText","selfLink":"selfLink","deleted":True,"layerId":"layerId","pageIds":["pageIds","pageIds"],"clientVersionRanges":{"gbImageRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"},"cfiRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"},"contentVersion":"contentVersion","gbTextRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"},"imageCfiRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"}},"volumeId":"volumeId","currentVersionRanges":{"gbImageRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"},"cfiRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"},"contentVersion":"contentVersion","gbTextRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"},"imageCfiRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"}},"id":"id","afterSelectedText":"afterSelectedText","updated":"updated","highlightStyle":"highlightStyle"}
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
                    ('annotationId', 'annotation_id_example'),
                    ('country', 'country_example'),
                    ('showOnlySummaryInResponse', True),
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/books/v1/mylibrary/annotations',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_mylibrary_annotations_list(client):
    """Test case for books_mylibrary_annotations_list

    
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
                    ('layerId', 'layer_id_example'),
                    ('layerIds', ['layer_ids_example']),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('showDeleted', True),
                    ('source', 'source_example'),
                    ('updatedMax', 'updated_max_example'),
                    ('updatedMin', 'updated_min_example'),
                    ('volumeId', 'volume_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/books/v1/mylibrary/annotations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_mylibrary_annotations_summary(client):
    """Test case for books_mylibrary_annotations_summary

    
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
                    ('layerIds', ['layer_ids_example']),
                    ('volumeId', 'volume_id_example'),
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/books/v1/mylibrary/annotations/summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_mylibrary_annotations_update(client):
    """Test case for books_mylibrary_annotations_update

    
    """
    body = {"layerSummary":{"allowedCharacterCount":0,"limitType":"limitType","remainingCharacterCount":6},"data":"data","selectedText":"selectedText","created":"created","kind":"kind","beforeSelectedText":"beforeSelectedText","selfLink":"selfLink","deleted":True,"layerId":"layerId","pageIds":["pageIds","pageIds"],"clientVersionRanges":{"gbImageRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"},"cfiRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"},"contentVersion":"contentVersion","gbTextRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"},"imageCfiRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"}},"volumeId":"volumeId","currentVersionRanges":{"gbImageRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"},"cfiRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"},"contentVersion":"contentVersion","gbTextRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"},"imageCfiRange":{"endOffset":"endOffset","startOffset":"startOffset","endPosition":"endPosition","startPosition":"startPosition"}},"id":"id","afterSelectedText":"afterSelectedText","updated":"updated","highlightStyle":"highlightStyle"}
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
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/books/v1/mylibrary/annotations/{annotation_id}'.format(annotation_id='annotation_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_mylibrary_bookshelves_add_volume(client):
    """Test case for books_mylibrary_bookshelves_add_volume

    
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
                    ('volumeId', 'volume_id_example'),
                    ('reason', 'reason_example'),
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/books/v1/mylibrary/bookshelves/{shelf}/addVolume'.format(shelf='shelf_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_mylibrary_bookshelves_clear_volumes(client):
    """Test case for books_mylibrary_bookshelves_clear_volumes

    
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
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/books/v1/mylibrary/bookshelves/{shelf}/clearVolumes'.format(shelf='shelf_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_mylibrary_bookshelves_get(client):
    """Test case for books_mylibrary_bookshelves_get

    
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
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/books/v1/mylibrary/bookshelves/{shelf}'.format(shelf='shelf_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_mylibrary_bookshelves_list(client):
    """Test case for books_mylibrary_bookshelves_list

    
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
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/books/v1/mylibrary/bookshelves',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_mylibrary_bookshelves_move_volume(client):
    """Test case for books_mylibrary_bookshelves_move_volume

    
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
                    ('volumeId', 'volume_id_example'),
                    ('volumePosition', 56),
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/books/v1/mylibrary/bookshelves/{shelf}/moveVolume'.format(shelf='shelf_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_mylibrary_bookshelves_remove_volume(client):
    """Test case for books_mylibrary_bookshelves_remove_volume

    
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
                    ('volumeId', 'volume_id_example'),
                    ('reason', 'reason_example'),
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/books/v1/mylibrary/bookshelves/{shelf}/removeVolume'.format(shelf='shelf_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_mylibrary_bookshelves_volumes_list(client):
    """Test case for books_mylibrary_bookshelves_volumes_list

    
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
                    ('country', 'country_example'),
                    ('maxResults', 56),
                    ('projection', 'projection_example'),
                    ('q', 'q_example'),
                    ('showPreorders', True),
                    ('source', 'source_example'),
                    ('startIndex', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/books/v1/mylibrary/bookshelves/{shelf}/volumes'.format(shelf='shelf_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_mylibrary_readingpositions_get(client):
    """Test case for books_mylibrary_readingpositions_get

    
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
        path='/books/v1/mylibrary/readingpositions/{volume_id}'.format(volume_id='volume_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_mylibrary_readingpositions_set_position(client):
    """Test case for books_mylibrary_readingpositions_set_position

    
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
                    ('position', 'position_example'),
                    ('timestamp', 'timestamp_example'),
                    ('action', 'action_example'),
                    ('contentVersion', 'content_version_example'),
                    ('deviceCookie', 'device_cookie_example'),
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/books/v1/mylibrary/readingpositions/{volume_id}/setPosition'.format(volume_id='volume_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

