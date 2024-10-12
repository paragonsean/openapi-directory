# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flat_series import FlatSeries
from openapi_server.models.idsquery import Idsquery
from openapi_server.models.image import Image
from openapi_server.models.patient import Patient
from openapi_server.models.query import Query
from openapi_server.models.series import Series
from openapi_server.models.seriesidseriestypesresult import Seriesidseriestypesresult
from openapi_server.models.seriestag import Seriestag
from openapi_server.models.seriestype import Seriestype
from openapi_server.models.source import Source
from openapi_server.models.study import Study


pytestmark = pytest.mark.asyncio

async def test_metadata_flatseries_get(client):
    """Test case for metadata_flatseries_get

    
    """
    params = [('startindex', 0),
                    ('count', 20),
                    ('orderby', 'orderby_example'),
                    ('orderascending', True),
                    ('filter', 'filter_example'),
                    ('sources', 'sources_example'),
                    ('seriestypes', 'seriestypes_example'),
                    ('seriestags', 'seriestags_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/flatseries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_flatseries_id_get(client):
    """Test case for metadata_flatseries_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/flatseries/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_metadata_flatseries_query_post(client):
    """Test case for metadata_flatseries_query_post

    
    """
    query = openapi_server.Query()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/metadata/flatseries/query',
        headers=headers,
        json=query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_images_get(client):
    """Test case for metadata_images_get

    
    """
    params = [('startindex', 0),
                    ('count', 20),
                    ('seriesid', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/images',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_images_id_get(client):
    """Test case for metadata_images_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/images/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_metadata_images_query_post(client):
    """Test case for metadata_images_query_post

    
    """
    query = openapi_server.Query()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/metadata/images/query',
        headers=headers,
        json=query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_patients_get(client):
    """Test case for metadata_patients_get

    
    """
    params = [('startindex', 0),
                    ('count', 20),
                    ('orderby', 'orderby_example'),
                    ('orderascending', True),
                    ('filter', 'filter_example'),
                    ('sources', 'sources_example'),
                    ('seriestypes', 'seriestypes_example'),
                    ('seriestags', 'seriestags_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/patients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_patients_id_get(client):
    """Test case for metadata_patients_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/patients/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_patients_id_images_get(client):
    """Test case for metadata_patients_id_images_get

    
    """
    params = [('sources', 'sources_example'),
                    ('seriestypes', 'seriestypes_example'),
                    ('seriestags', 'seriestags_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/patients/{id}/images'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_metadata_patients_query_post(client):
    """Test case for metadata_patients_query_post

    
    """
    query = openapi_server.Query()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/metadata/patients/query',
        headers=headers,
        json=query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_series_get(client):
    """Test case for metadata_series_get

    
    """
    params = [('startindex', 0),
                    ('count', 20),
                    ('studyid', 56),
                    ('sources', 'sources_example'),
                    ('seriestypes', 'seriestypes_example'),
                    ('seriestags', 'seriestags_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_series_id_get(client):
    """Test case for metadata_series_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/series/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_series_id_seriestags_get(client):
    """Test case for metadata_series_id_seriestags_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/series/{id}/seriestags'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_metadata_series_id_seriestags_post(client):
    """Test case for metadata_series_id_seriestags_post

    
    """
    query = openapi_server.Seriestag()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/metadata/series/{id}/seriestags'.format(id=56),
        headers=headers,
        json=query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_series_id_seriestypes_delete(client):
    """Test case for metadata_series_id_seriestypes_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/metadata/series/{id}/seriestypes'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_series_id_seriestypes_get(client):
    """Test case for metadata_series_id_seriestypes_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/series/{id}/seriestypes'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_series_id_source_get(client):
    """Test case for metadata_series_id_source_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/series/{id}/source'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_metadata_series_query_post(client):
    """Test case for metadata_series_query_post

    
    """
    query = openapi_server.Query()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/metadata/series/query',
        headers=headers,
        json=query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_series_series_id_seriestags_series_tag_id_delete(client):
    """Test case for metadata_series_series_id_seriestags_series_tag_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/metadata/series/{series_id}/seriestags/{series_tag_id}'.format(series_id=56, series_tag_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_series_series_id_seriestypes_series_type_id_delete(client):
    """Test case for metadata_series_series_id_seriestypes_series_type_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/metadata/series/{series_id}/seriestypes/{series_type_id}'.format(series_id=56, series_type_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_series_series_id_seriestypes_series_type_id_put(client):
    """Test case for metadata_series_series_id_seriestypes_series_type_id_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/api/metadata/series/{series_id}/seriestypes/{series_type_id}'.format(series_id=56, series_type_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_seriestags_get(client):
    """Test case for metadata_seriestags_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/seriestags',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_studies_get(client):
    """Test case for metadata_studies_get

    
    """
    params = [('startindex', 0),
                    ('count', 20),
                    ('patientid', 56),
                    ('sources', 'sources_example'),
                    ('seriestypes', 'seriestypes_example'),
                    ('seriestags', 'seriestags_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/studies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_studies_id_get(client):
    """Test case for metadata_studies_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/studies/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metadata_studies_id_images_get(client):
    """Test case for metadata_studies_id_images_get

    
    """
    params = [('sources', 'sources_example'),
                    ('seriestypes', 'seriestypes_example'),
                    ('seriestags', 'seriestags_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/studies/{id}/images'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_metadata_studies_query_post(client):
    """Test case for metadata_studies_query_post

    
    """
    query = openapi_server.Query()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/metadata/studies/query',
        headers=headers,
        json=query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_seriestypes_series_query_post(client):
    """Test case for seriestypes_series_query_post

    
    """
    query = openapi_server.Idsquery()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/seriestypes/series/query',
        headers=headers,
        json=query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

