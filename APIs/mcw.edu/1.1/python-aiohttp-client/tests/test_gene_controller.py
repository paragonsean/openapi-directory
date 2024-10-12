# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.annotated_gene_request import AnnotatedGeneRequest
from openapi_server.models.gene import Gene
from openapi_server.models.mapped_gene import MappedGene
from openapi_server.models.mapped_gene_position import MappedGenePosition
from openapi_server.models.ortholog_request import OrthologRequest


pytestmark = pytest.mark.asyncio

async def test_get_all_annotated_genes_using_get(client):
    """Test case for get_all_annotated_genes_using_get

    Return a list of genes annotated to an ontology term
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/genes/annotation/{acc_id}'.format(acc_id='acc_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_annotated_genes_using_post(client):
    """Test case for get_annotated_genes_using_post

    Return a list of genes annotated to an ontology term
    """
    body = {"speciesTypeKeys":[0,0],"evidenceCodes":["evidenceCodes","evidenceCodes"],"accId":"accId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/genes/annotation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_alleles_using_get(client):
    """Test case for get_gene_alleles_using_get

    Return a list of gene alleles
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/genes/allele/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_by_map_key_using_get(client):
    """Test case for get_gene_by_map_key_using_get

    Return a list of all genes with position information for an assembly
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/genes/map/{map_key}'.format(map_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_by_rgd_id_using_get(client):
    """Test case for get_gene_by_rgd_id_using_get

    Get a gene record by RGD ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/genes/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_by_symbol_using_get(client):
    """Test case for get_gene_by_symbol_using_get

    Get a gene record by symbol and species type key
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/genes/{symbol}/{species_type_key}'.format(symbol='symbol_example', species_type_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_orthologs_using_get(client):
    """Test case for get_gene_orthologs_using_get

    Return a list of gene orthologs
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/genes/orthologs/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genes_annotated_using_get(client):
    """Test case for get_genes_annotated_using_get

    Return a list of genes annotated to an ontology term
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/genes/annotation/{acc_id}/{species_type_key}'.format(acc_id='acc_id_example', species_type_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genes_by_affy_id_using_get(client):
    """Test case for get_genes_by_affy_id_using_get

    Return a list of genes for an affymetrix ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/genes/affyId/{affy_id}/{species_type_key}'.format(affy_id='affy_id_example', species_type_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genes_by_alias_symbol_using_get(client):
    """Test case for get_genes_by_alias_symbol_using_get

    Return a list of genes for an alias and species
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/genes/alias/{alias_symbol}/{species_type_key}'.format(alias_symbol='alias_symbol_example', species_type_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genes_by_keyword_using_get(client):
    """Test case for get_genes_by_keyword_using_get

    Return a list of genes by keyword and species type key
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/genes/keyword/{keyword}/{species_type_key}'.format(keyword='keyword_example', species_type_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genes_by_position_using_get(client):
    """Test case for get_genes_by_position_using_get

    Return a list of genes position and map key
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/genes/{chr}/{start}/{stop}/{map_key}'.format(chr='chr_example', start=56, stop=56, map_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genes_by_species_using_get(client):
    """Test case for get_genes_by_species_using_get

    Return a list of all genes for a species in RGD
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/genes/species/{species_type_key}'.format(species_type_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genes_in_region_using_get(client):
    """Test case for get_genes_in_region_using_get

    Return a list of genes in region
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/genes/region/{chr}/{start}/{stop}/{map_key}'.format(chr='chr_example', start=56, stop=56, map_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mapped_genes_by_position_using_get(client):
    """Test case for get_mapped_genes_by_position_using_get

    Return a list of genes position and map key
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/genes/mapped/{chr}/{start}/{stop}/{map_key}'.format(chr='chr_example', start=56, stop=56, map_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_orthologs_by_list_using_post(client):
    """Test case for get_orthologs_by_list_using_post

    Return a list of gene orthologs
    """
    body = {"speciesTypeKeys":[6,6],"rgdIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/genes/orthologs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

