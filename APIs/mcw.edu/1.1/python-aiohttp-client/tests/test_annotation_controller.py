# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.annotation import Annotation
from openapi_server.models.annotation_request import AnnotationRequest
from openapi_server.models.map_pair import MapPair


pytestmark = pytest.mark.asyncio

async def test_get_annotation_count_by_acc_id_and_object_type_using_get(client):
    """Test case for get_annotation_count_by_acc_id_and_object_type_using_get

    Returns annotation count for ontology accession ID and object type
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/annotations/count/{acc_id}/{species_type_key}/{include_children}/{object_type}'.format(acc_id='acc_id_example', species_type_key=56, include_children=True, object_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_annotation_count_by_acc_id_and_species_using_get(client):
    """Test case for get_annotation_count_by_acc_id_and_species_using_get

    Returns annotation count for ontology accession ID and speicies
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/annotations/count/{acc_id}/{species_type_key}/{include_children}'.format(acc_id='acc_id_example', species_type_key=56, include_children=True),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_annotation_count_by_acc_id_using_get(client):
    """Test case for get_annotation_count_by_acc_id_using_get

    Returns annotation count for ontology accession ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/annotations/count/{acc_id}/{include_children}'.format(acc_id='acc_id_example', include_children=True),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_annotations_by_acc_id_and_rgd_id_using_get(client):
    """Test case for get_annotations_by_acc_id_and_rgd_id_using_get

    Returns a list of annotations by RGD ID and ontology term accession ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/annotations/{acc_id}/{rgd_id}'.format(acc_id='acc_id_example', rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_annotations_by_rgd_id_and_ontology_using_get(client):
    """Test case for get_annotations_by_rgd_id_and_ontology_using_get

    Returns a list of annotations by RGD ID and ontology prefix
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/annotations/rgdId/{rgd_id}/{ontology_prefix}'.format(rgd_id=56, ontology_prefix='ontology_prefix_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_annotations_by_rgd_id_using_get(client):
    """Test case for get_annotations_by_rgd_id_using_get

    Returns a list of annotations by RGD ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/annotations/rgdId/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_annotations_using_get(client):
    """Test case for get_annotations_using_get

    Returns a list annotations for an ontology term or a term and it's children
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/annotations/{acc_id}/{species_type_key}/{include_children}'.format(acc_id='acc_id_example', species_type_key=56, include_children=True),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_annotations_using_post(client):
    """Test case for get_annotations_using_post

    Return a list of genes annotated to an ontology term
    """
    body = {"termAcc":"termAcc","speciesTypeKeys":[0,0],"evidenceCodes":["evidenceCodes","evidenceCodes"],"ids":["ids","ids"]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/annotations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_annots_by_refrerence_using_get(client):
    """Test case for get_annots_by_refrerence_using_get

    Returns a list of annotations for a reference
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/annotations/reference/{ref_rgd_id}'.format(ref_rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_term_acc_ids_using_get(client):
    """Test case for get_term_acc_ids_using_get

    Returns a list ontology term accession IDs annotated to an rgd object
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/annotations/accId/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

