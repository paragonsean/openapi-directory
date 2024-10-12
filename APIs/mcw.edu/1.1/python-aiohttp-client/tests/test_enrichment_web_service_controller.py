# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.enrichment_gene_request import EnrichmentGeneRequest
from openapi_server.models.enrichment_request import EnrichmentRequest


pytestmark = pytest.mark.asyncio

async def test_get_enrichment_data_using_post(client):
    """Test case for get_enrichment_data_using_post

    Return a list of genes annotated to the term.Genes are rgdids separated by comma.Species type is an integer value.term is the ontology
    """
    body = {"species":"species","accId":"accId","geneSymbols":["geneSymbols","geneSymbols"]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/enrichment/annotatedGenes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_enrichment_data_using_post1(client):
    """Test case for get_enrichment_data_using_post1

    Return a chart of ontology terms annotated to the genes.Genes are rgdids separated by comma.Species type is an integer value.Aspect is the Ontology group
    """
    body = {"genes":["genes","genes"],"species":"species","aspect":"aspect"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rgdws/enrichment/data',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

