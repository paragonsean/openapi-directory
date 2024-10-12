# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.association import Association
from openapi_server.models.association_results import AssociationResults
from openapi_server.models.bio_object import BioObject
from openapi_server.models.d2_p_association_results import D2PAssociationResults
from openapi_server.models.named_object import NamedObject


pytestmark = pytest.mark.asyncio

async def test_get_anatomy_gene_associations(client):
    """Test case for get_anatomy_gene_associations

    Returns genes associated with a given anatomy
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/anatomy/{id}/genes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_anatomy_gene_by_taxon_associations(client):
    """Test case for get_anatomy_gene_by_taxon_associations

    Returns gene IDs for all genes associated with a given anatomy, filtered by taxon
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/anatomy/{id}/genes/{taxid}'.format(taxid='taxid_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_case_disease_associations(client):
    """Test case for get_case_disease_associations

    Returns diseases associated with a case
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/case/{id}/diseases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_case_genotype_associations(client):
    """Test case for get_case_genotype_associations

    Returns genotypes associated with a case
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/case/{id}/genotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_case_model_associations(client):
    """Test case for get_case_model_associations

    Returns models associated with a case
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/case/{id}/models'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_case_phenotype_associations(client):
    """Test case for get_case_phenotype_associations

    Returns phenotypes associated with a case
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/case/{id}/phenotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_case_variant_associations(client):
    """Test case for get_case_variant_associations

    Returns variants associated with a case
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/case/{id}/variants'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_disease_case_associations(client):
    """Test case for get_disease_case_associations

    Returns cases associated with a disease
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/disease/{id}/cases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_disease_gene_associations(client):
    """Test case for get_disease_gene_associations

    Returns genes associated with a disease
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example'),
                    ('association_type', both)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/disease/{id}/genes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_disease_genotype_associations(client):
    """Test case for get_disease_genotype_associations

    Returns genotypes associated with a disease
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/disease/{id}/genotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_disease_model_associations(client):
    """Test case for get_disease_model_associations

    Returns associations to models of the disease
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/disease/{id}/models'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_disease_model_taxon_associations(client):
    """Test case for get_disease_model_taxon_associations

    Returns associations to models of the disease constrained by taxon
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/disease/{id}/models/{taxon}'.format(taxon='taxon_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_disease_pathway_associations(client):
    """Test case for get_disease_pathway_associations

    Returns pathways associated with a disease
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/disease/{id}/pathways'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_disease_phenotype_associations(client):
    """Test case for get_disease_phenotype_associations

    Returns phenotypes associated with disease
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/disease/{id}/phenotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_disease_publication_associations(client):
    """Test case for get_disease_publication_associations

    Returns publications associated with a disease
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/disease/{id}/publications'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_disease_substance_associations(client):
    """Test case for get_disease_substance_associations

    Returns substances associated with a disease
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/disease/{id}/treatment'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_disease_variant_associations(client):
    """Test case for get_disease_variant_associations

    Returns variants associated with a disease
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/disease/{id}/variants'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_function_associations(client):
    """Test case for get_function_associations

    Returns annotations associated to a function term
    """
    params = [('start', 0),
                    ('rows', 100),
                    ('evidence', ['evidence_example'])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/function/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_function_gene_associations(client):
    """Test case for get_function_gene_associations

    Returns genes associated to a GO term
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example'),
                    ('relationship_type', involved_in)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/function/{id}/genes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_function_publication_associations(client):
    """Test case for get_function_publication_associations

    Returns publications associated to a GO term
    """
    params = [('start', 0),
                    ('rows', 100),
                    ('evidence', ['evidence_example'])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/function/{id}/publications'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_function_taxon_associations(client):
    """Test case for get_function_taxon_associations

    Returns taxons associated to a GO term
    """
    params = [('start', 0),
                    ('rows', 100),
                    ('evidence', ['evidence_example'])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/function/{id}/taxons'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_anatomy_associations(client):
    """Test case for get_gene_anatomy_associations

    Returns anatomical entities associated with a gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/anatomy'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_case_associations(client):
    """Test case for get_gene_case_associations

    Returns cases associated with a gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/cases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_disease_associations(client):
    """Test case for get_gene_disease_associations

    Returns diseases associated with gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example'),
                    ('association_type', both)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/diseases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_expression_associations(client):
    """Test case for get_gene_expression_associations

    Returns expression events for a gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/expression/anatomy'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_function_associations(client):
    """Test case for get_gene_function_associations

    Returns function associations for a gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/function'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_genotype_associations(client):
    """Test case for get_gene_genotype_associations

    Returns genotypes associated with a gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/genotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_homolog_associations(client):
    """Test case for get_gene_homolog_associations

    Returns homologs for a gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('homology_type', 'homology_type_example'),
                    ('direct_taxon', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/homologs'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_interactions(client):
    """Test case for get_gene_interactions

    Returns interactions for a gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/interactions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_model_associations(client):
    """Test case for get_gene_model_associations

    Returns models associated with a gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/models'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_ortholog_disease_associations(client):
    """Test case for get_gene_ortholog_disease_associations

    Return diseases associated with orthologs of a gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/ortholog/diseases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_ortholog_phenotype_associations(client):
    """Test case for get_gene_ortholog_phenotype_associations

    Return phenotypes associated with orthologs for a gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/ortholog/phenotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_pathway_associations(client):
    """Test case for get_gene_pathway_associations

    Returns pathways associated with gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/pathways'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_phenotype_associations(client):
    """Test case for get_gene_phenotype_associations

    Returns phenotypes associated with gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/phenotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_publication_associations(client):
    """Test case for get_gene_publication_associations

    Returns publications associated with a gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/publications'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_variant_associations(client):
    """Test case for get_gene_variant_associations

    Returns variants associated with a gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/gene/{id}/variants'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_generic_associations(client):
    """Test case for get_generic_associations

    Returns associations for an entity regardless of the type
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/{id}/associations'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_generic_object(client):
    """Test case for get_generic_object

    Returns basic info on object of any type
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_generic_object_by_type(client):
    """Test case for get_generic_object_by_type

    Return basic info on an object for a given type
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('get_association_counts', False),
                    ('distinct_counts', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/{type}/{id}'.format(type='type_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genotype_case_associations(client):
    """Test case for get_genotype_case_associations

    Returns cases associated with a genotype
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/genotype/{id}/cases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genotype_disease_associations(client):
    """Test case for get_genotype_disease_associations

    Returns diseases associated with a genotype
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/genotype/{id}/diseases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genotype_gene_associations(client):
    """Test case for get_genotype_gene_associations

    Returns genes associated with a genotype
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/genotype/{id}/genes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genotype_genotype_associations(client):
    """Test case for get_genotype_genotype_associations

    Returns genotypes-genotype associations
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/genotype/{id}/genotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genotype_model_associations(client):
    """Test case for get_genotype_model_associations

    Returns models associated with a genotype
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/genotype/{id}/models'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genotype_phenotype_associations(client):
    """Test case for get_genotype_phenotype_associations

    Returns phenotypes associated with a genotype
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/genotype/{id}/phenotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genotype_publication_associations(client):
    """Test case for get_genotype_publication_associations

    Returns publications associated with a genotype
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/genotype/{id}/publications'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genotype_variant_associations(client):
    """Test case for get_genotype_variant_associations

    Returns genotypes-variant associations
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/genotype/{id}/variants'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_goterm_gene_associations(client):
    """Test case for get_goterm_gene_associations

    Returns associations to GO terms for a gene
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('relationship_type', involved_in)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/goterm/{id}/genes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_model_case_associations(client):
    """Test case for get_model_case_associations

    Returns cases associated with a model
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/model/{id}/cases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_model_disease_associations(client):
    """Test case for get_model_disease_associations

    Returns diseases associated with a model
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/model/{id}/diseases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_model_gene_associations(client):
    """Test case for get_model_gene_associations

    Returns genes associated with a model
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/model/{id}/genes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_model_genotype_associations(client):
    """Test case for get_model_genotype_associations

    Returns genotypes associated with a model
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/model/{id}/genotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_model_phenotype_associations(client):
    """Test case for get_model_phenotype_associations

    Returns phenotypes associated with a model
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/model/{id}/phenotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_model_publication_associations(client):
    """Test case for get_model_publication_associations

    Returns publications associated with a model
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/model/{id}/publications'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_model_variant_associations(client):
    """Test case for get_model_variant_associations

    Returns variants associated with a model
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/model/{id}/variants'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pathway_disease_associations(client):
    """Test case for get_pathway_disease_associations

    Returns diseases associated with a pathway
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/pathway/{id}/diseases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pathway_gene_associations(client):
    """Test case for get_pathway_gene_associations

    Returns genes associated with a pathway
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/pathway/{id}/genes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pathway_phenotype_associations(client):
    """Test case for get_pathway_phenotype_associations

    Returns phenotypes associated with a pathway
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/pathway/{id}/phenotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_phenotype_anatomy_associations(client):
    """Test case for get_phenotype_anatomy_associations

    Returns anatomical entities associated with a phenotype
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/phenotype/{id}/anatomy'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_phenotype_case_associations(client):
    """Test case for get_phenotype_case_associations

    Returns cases associated with a phenotype
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/phenotype/{id}/cases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_phenotype_disease_associations(client):
    """Test case for get_phenotype_disease_associations

    Returns diseases associated with a phenotype
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/phenotype/{id}/diseases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_phenotype_gene_associations(client):
    """Test case for get_phenotype_gene_associations

    Returns genes associated with a phenotype
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/phenotype/{id}/genes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_phenotype_gene_by_taxon_associations(client):
    """Test case for get_phenotype_gene_by_taxon_associations

    Returns gene IDs for all genes associated with a given phenotype, filtered by taxon
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/phenotype/{id}/gene/{taxid}/ids'.format(taxid='taxid_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_phenotype_genotype_associations(client):
    """Test case for get_phenotype_genotype_associations

    Returns genotypes associated with a phenotype
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/phenotype/{id}/genotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_phenotype_pathway_associations(client):
    """Test case for get_phenotype_pathway_associations

    Returns pathways associated with a phenotype
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/phenotype/{id}/pathways'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_phenotype_publication_associations(client):
    """Test case for get_phenotype_publication_associations

    Returns publications associated with a phenotype
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/phenotype/{id}/publications'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_phenotype_variant_associations(client):
    """Test case for get_phenotype_variant_associations

    Returns variants associated with a phenotype
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/phenotype/{id}/variants'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_publication_disease_associations(client):
    """Test case for get_publication_disease_associations

    Returns diseases associated with a publication
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/publication/{id}/diseases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_publication_gene_associations(client):
    """Test case for get_publication_gene_associations

    Returns genes associated with a publication
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/publication/{id}/genes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_publication_genotype_associations(client):
    """Test case for get_publication_genotype_associations

    Returns genotypes associated with a publication
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/publication/{id}/genotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_publication_model_associations(client):
    """Test case for get_publication_model_associations

    Returns models associated with a publication
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/publication/{id}/models'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_publication_phenotype_associations(client):
    """Test case for get_publication_phenotype_associations

    Returns phenotypes associated with a publication
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/publication/{id}/phenotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_publication_variant_associations(client):
    """Test case for get_publication_variant_associations

    Returns variants associated with a publication
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/publication/{id}/variants'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_substance_participant_in_associations(client):
    """Test case for get_substance_participant_in_associations

    Returns associations between an activity and process and the specified substance
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/substance/{id}/participant_in'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_substance_role_associations(client):
    """Test case for get_substance_role_associations

    Returns associations between given drug and roles
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/substance/{id}/roles'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_substance_treats_associations(client):
    """Test case for get_substance_treats_associations

    Returns substances associated with a disease
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/substance/{id}/treats'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variant_case_associations(client):
    """Test case for get_variant_case_associations

    Returns cases associated with a variant
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/variant/{id}/cases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variant_disease_associations(client):
    """Test case for get_variant_disease_associations

    Returns diseases associated with a variant
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/variant/{id}/diseases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variant_gene_associations(client):
    """Test case for get_variant_gene_associations

    Returns genes associated with a variant
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/variant/{id}/genes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variant_genotype_associations(client):
    """Test case for get_variant_genotype_associations

    Returns genotypes associated with a variant
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/variant/{id}/genotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variant_model_associations(client):
    """Test case for get_variant_model_associations

    Returns models associated with a variant
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/variant/{id}/models'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variant_phenotype_associations(client):
    """Test case for get_variant_phenotype_associations

    Returns phenotypes associated with a variant
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/variant/{id}/phenotypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variant_publication_associations(client):
    """Test case for get_variant_publication_associations

    Returns publications associated with a variant
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('facet', False),
                    ('facet_fields', ['facet_fields_example']),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('fetch_objects', False),
                    ('use_compact_associations', False),
                    ('slim', ['slim_example']),
                    ('evidence', 'evidence_example'),
                    ('direct', False),
                    ('taxon', ['taxon_example']),
                    ('direct_taxon', False),
                    ('relation', 'relation_example'),
                    ('sort', 'sort_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentity/variant/{id}/publications'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

