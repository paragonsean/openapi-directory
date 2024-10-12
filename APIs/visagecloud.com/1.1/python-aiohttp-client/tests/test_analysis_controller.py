# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.rest_response import RestResponse


pytestmark = pytest.mark.asyncio

async def test_compare_faces_using_get(client):
    """Test case for compare_faces_using_get

    Compare several faces identified by faceHash, without depending on mapping faces to profiles
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('faceHashes', ['face_hashes_example']),
                    ('showDetails', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/analysis/compare',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_perform_analysis_using_post(client):
    """Test case for perform_analysis_using_post

    Perform detection on a given picture or picture URL
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('storeAnalysisPicture', True),
                    ('storeFacePictures', True),
                    ('storeResult', True),
                    ('retentionTime', 56),
                    ('pictureURL', 'picture_url_example'),
                    ('algorithmVersion', V2),
                    ('autoRotate', False),
                    ('skipEXIF', False),
                    ('waitForPictureUpload', False),
                    ('filters', ['filters_example']),
                    ('options', 'options_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('picture', 'picture_example')
    response = await client.request(
        method='POST',
        path='/rest/v1.1/analysis/detection',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_perform_recognition_using_post(client):
    """Test case for perform_recognition_using_post

    Perform labeled recognition on a given picture or picture URL
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('storeAnalysisPicture', True),
                    ('storeFacePictures', True),
                    ('storeResult', True),
                    ('retentionTime', 56),
                    ('collectionId', 'collection_id_example'),
                    ('labels', ['labels_example']),
                    ('attributeFilters', ['attribute_filters_example']),
                    ('pictureURL', 'picture_url_example'),
                    ('algorithmVersion', V2),
                    ('autoRotate', False),
                    ('skipEXIF rotation processing', False),
                    ('waitForPictureUpload', False),
                    ('filters', ['filters_example']),
                    ('options', 'options_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('picture', 'picture_example')
    response = await client.request(
        method='POST',
        path='/rest/v1.1/analysis/recognition',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_analysis_using_get(client):
    """Test case for retrieve_analysis_using_get

    Retrieve a complete analysis object including both detection and recognition information
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('analysisId', 'analysis_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/analysis/retrieve',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrive_latest_using_get(client):
    """Test case for retrive_latest_using_get

    Retrieve the last *count* operations per current account
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('count', 100)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/analysis/listLatest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

