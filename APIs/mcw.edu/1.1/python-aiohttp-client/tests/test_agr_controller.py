# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_affected_genomic_models_using_get(client):
    """Test case for get_affected_genomic_models_using_get

    Get affected genomic models (rat strains with gene alleles) submitted by RGD to AGR by taxonId
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/agr/affectedGenomicModels/{taxon_id}'.format(taxon_id='taxon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_alleles_for_taxon_using_get(client):
    """Test case for get_alleles_for_taxon_using_get

    Get gene allele records submitted by RGD to AGR by taxonId
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/agr/alleles/{taxon_id}'.format(taxon_id='taxon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_expression_for_taxon_using_get(client):
    """Test case for get_expression_for_taxon_using_get

    Get expression annotations submitted by RGD to AGR by taxonId
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/agr/expression/{taxon_id}'.format(taxon_id='taxon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genes_for_latest_assembly_using_get(client):
    """Test case for get_genes_for_latest_assembly_using_get

    Get gene records submitted by RGD to AGR by taxonId
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/agr/{taxon_id}'.format(taxon_id='taxon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_phenotypes_for_taxon_using_get(client):
    """Test case for get_phenotypes_for_taxon_using_get

    Get phenotype annotations submitted by RGD to AGR by taxonId
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/agr/phenotypes/{taxon_id}'.format(taxon_id='taxon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variants_for_taxon_using_get(client):
    """Test case for get_variants_for_taxon_using_get

    Get basic variant records submitted by RGD to AGR by taxonId
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/agr/variants/{taxon_id}'.format(taxon_id='taxon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

