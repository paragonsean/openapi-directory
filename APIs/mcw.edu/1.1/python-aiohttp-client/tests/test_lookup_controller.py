# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.map import Map
from openapi_server.models.rgdid_list_request import RGDIDListRequest


pytestmark = pytest.mark.asyncio

async def test_get_ensembl_gene_mapping_using_get(client):
    """Test case for get_ensembl_gene_mapping_using_get

    Translate an RGD ID to an Ensembl Gene  ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/lookup/id/map/EnsemblGene/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ensembl_gene_mapping_using_post(client):
    """Test case for get_ensembl_gene_mapping_using_post

    Translate RGD IDs to Ensembl Gene IDs
    """
    body = {"rgdIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/lookup/id/map/EnsemblGene',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ensembl_protein_mapping_using_get(client):
    """Test case for get_ensembl_protein_mapping_using_get

    Translate an RGD ID to an Ensembl Protein ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/lookup/id/map/EnsemblProtein/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ensembl_protein_mapping_using_post(client):
    """Test case for get_ensembl_protein_mapping_using_post

    Translate RGD IDs to Ensembl Protein IDs
    """
    body = {"rgdIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/lookup/id/map/EnsemblProtein',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ensembl_transcript_mapping_using_get(client):
    """Test case for get_ensembl_transcript_mapping_using_get

    Translate an RGD ID to an Ensembl Transcript ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/lookup/id/map/EnsemblTranscript/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ensembl_transcript_mapping_using_post(client):
    """Test case for get_ensembl_transcript_mapping_using_post

    Translate RGD IDs to Ensembl Transcript IDs
    """
    body = {"rgdIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/lookup/id/map/EnsemblTranscript',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gen_bank_nucleotide_mapping_using_get(client):
    """Test case for get_gen_bank_nucleotide_mapping_using_get

    Translate an RGD ID to a GenBank Nucleotide ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/lookup/id/map/GenBankNucleotide/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gen_bank_nucleotide_mapping_using_post(client):
    """Test case for get_gen_bank_nucleotide_mapping_using_post

    Translate RGD IDs to GenBank Nucleotide IDs
    """
    body = {"rgdIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/lookup/id/map/GenBankNucleotide',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gen_bank_protein_mapping_using_get(client):
    """Test case for get_gen_bank_protein_mapping_using_get

    Translate an RGD ID to a GenBank Protein ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/lookup/id/map/GenBankProtein/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gen_bank_protein_mapping_using_post(client):
    """Test case for get_gen_bank_protein_mapping_using_post

    Translate RGD IDs to GenBank Protein IDs
    """
    body = {"rgdIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/lookup/id/map/GenBankProtein',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_types_using_get(client):
    """Test case for get_gene_types_using_get

    Returns a list of gene types avialable in RGD
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/lookup/geneTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gtex_mapping_using_get(client):
    """Test case for get_gtex_mapping_using_get

    Translate an RGD ID to an GTEx ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/lookup/id/map/GTEx/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gtex_mapping_using_post(client):
    """Test case for get_gtex_mapping_using_post

    Translate RGD IDs to GTEx IDs
    """
    body = {"rgdIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/lookup/id/map/GTEx',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hgnc_mapping_using_get(client):
    """Test case for get_hgnc_mapping_using_get

    Translate an RGD ID to an HGNC ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/lookup/id/map/HGNC/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hgnc_mapping_using_post(client):
    """Test case for get_hgnc_mapping_using_post

    Translate RGD IDs to HGNC IDs
    """
    body = {"rgdIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/lookup/id/map/HGNC',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_maps_using_get(client):
    """Test case for get_maps_using_get

    Return a list assembly maps for a species
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/lookup/maps/{species_type_key}'.format(species_type_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_maps_using_get1(client):
    """Test case for get_maps_using_get1

    Return a standardUnit for an ontology if it exists
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/lookup/standardUnit/{acc_id}'.format(acc_id='acc_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mgi_mapping_using_get(client):
    """Test case for get_mgi_mapping_using_get

    Translate an RGD ID to an MGI ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/lookup/id/map/MGI/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mgi_mapping_using_post(client):
    """Test case for get_mgi_mapping_using_post

    Translate RGD IDs to MGI IDs
    """
    body = {"rgdIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/lookup/id/map/MGI',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ncbi_gene_mapping_using_get(client):
    """Test case for get_ncbi_gene_mapping_using_get

    Translate an RGD ID to an NCBI Gene ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/lookup/id/map/NCBIGene/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ncbi_gene_mapping_using_post(client):
    """Test case for get_ncbi_gene_mapping_using_post

    Translate RGD IDs to NCBI Gene IDs
    """
    body = {"rgdIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/lookup/id/map/NCBIGene',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_species_types_using_get(client):
    """Test case for get_species_types_using_get

    Return a Map of species type keys available in RGD
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/lookup/speciesTypeKeys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_uni_prot_mapping_using_get(client):
    """Test case for get_uni_prot_mapping_using_get

    Translate an RGD ID to a UniProt ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/lookup/id/map/UniProt/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_uni_prot_mapping_using_post(client):
    """Test case for get_uni_prot_mapping_using_post

    Translate RGD IDs to UniProt IDs
    """
    body = {"rgdIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/lookup/id/map/UniProt',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

