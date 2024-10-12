# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_response import RestResponse


pytestmark = pytest.mark.asyncio

async def test_add_svm_classifier_using_post(client):
    """Test case for add_svm_classifier_using_post

    Create new SVM classifier with given name
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('name', 'name_example'),
                    ('collectionIds', ['collection_ids_example']),
                    ('preprocessor', 'FeaturePreprocessor'),
                    ('classificationAttributeName', 'classification_attribute_name_example'),
                    ('considerViewPoints', False),
                    ('seed', 179425537),
                    ('trainingRatio', 0.8),
                    ('probabilityParameter', 1),
                    ('gammaParameter', 0.5),
                    ('nuParameter', 0.25),
                    ('cParameter', 1.0),
                    ('svmTypeParameter', 0),
                    ('kernelTypeParameter', 0),
                    ('cacheSizeParameter', 500.0),
                    ('epsParameter', 0.001)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/v1.1/classifier/svm',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_classifer_full_using_get(client):
    """Test case for get_classifer_full_using_get

    Get classifier full
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/classifier/svm',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_classifer_status_using_get(client):
    """Test case for get_classifer_status_using_get

    Get classifer status
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/classifier/svm/status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_classifer_using_delete(client):
    """Test case for remove_classifer_using_delete

    Delete existing classifier
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v1.1/classifier/svm',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

