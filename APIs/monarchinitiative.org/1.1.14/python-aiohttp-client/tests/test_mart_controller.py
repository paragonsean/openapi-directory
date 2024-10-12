# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_mart_case_associations_resource(client):
    """Test case for get_mart_case_associations_resource

    Bulk download of case associations
    """
    params = [('slim', ['slim_example'])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/mart/case/{object_category}/{taxon}'.format(taxon='taxon_example', object_category='object_category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mart_disease_associations_resource(client):
    """Test case for get_mart_disease_associations_resource

    Bulk download of disease associations
    """
    params = [('slim', ['slim_example'])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/mart/disease/{object_category}/{taxon}'.format(taxon='taxon_example', object_category='object_category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mart_gene_associations_resource(client):
    """Test case for get_mart_gene_associations_resource

    Bulk download of gene associations
    """
    params = [('slim', ['slim_example'])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/mart/gene/{object_category}/{taxon}'.format(taxon='taxon_example', object_category='object_category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mart_ortholog_associations_resource(client):
    """Test case for get_mart_ortholog_associations_resource

    Bulk download of orthologs
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/mart/ortholog/{taxon1}/{taxon2}'.format(taxon2='taxon2_example', taxon1='taxon1_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mart_paralog_associations_resource(client):
    """Test case for get_mart_paralog_associations_resource

    Bulk download of paralogs
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/mart/paralog/{taxon1}/{taxon2}'.format(taxon2='taxon2_example', taxon1='taxon1_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

