# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.authorization import Authorization
from openapi_server.models.client_gene import ClientGene
from openapi_server.models.client_snp import ClientSNP
from openapi_server.models.javascript_web_token import JavascriptWebToken
from openapi_server.models.product import Product
from openapi_server.models.public_gene import PublicGene
from openapi_server.models.public_snp import PublicSNP
from openapi_server.models.reference_chromosome_overview import ReferenceChromosomeOverview
from openapi_server.models.reference_genome_overview import ReferenceGenomeOverview
from openapi_server.models.reference_sequence import ReferenceSequence
from openapi_server.models.report_credentials import ReportCredentials
from openapi_server.models.report_file import ReportFile


pytestmark = pytest.mark.asyncio

async def test_get_authorizations_queue(client):
    """Test case for get_authorizations_queue

    
    """
    params = [('seq_num_start', 'seq_num_start_example')]
    headers = { 
        'Accept': 'application/json',
        'x_fields': 'x_fields_example',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{product_id}/authorizations'.format(product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_client_gene(client):
    """Test case for get_client_gene

    Get gene by symbol
    """
    headers = { 
        'Accept': 'application/json',
        'x_fields': 'x_fields_example',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/clients/{client_id}/datasets/{dataset_id}/genes/{gene_symbol}'.format(client_id='client_id_example', dataset_id='dataset_id_example', gene_symbol='gene_symbol_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_client_snp(client):
    """Test case for get_client_snp

    Get SNP information
    """
    headers = { 
        'Accept': 'application/json',
        'x_fields': 'x_fields_example',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/clients/{client_id}/datasets/{dataset_id}/snps/{snp_id}'.format(client_id='client_id_example', dataset_id='dataset_id_example', snp_id='snp_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_client_snp_group(client):
    """Test case for get_client_snp_group

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_fields': 'x_fields_example',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/clients/{client_id}/datasets/{dataset_id}/snps'.format(client_id='client_id_example', dataset_id='dataset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene(client):
    """Test case for get_gene

    Generic gene information
    """
    params = [('dbsnp_build', 149),
                    ('reference_genome', 'GRCH37P13')]
    headers = { 
        'Accept': 'application/json',
        'x_fields': 'x_fields_example',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/reference/genes/databases/{database_name}/accessions/{accession}'.format(database_name='database_name_example', accession='accession_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product(client):
    """Test case for get_product

    Get product details
    """
    headers = { 
        'Accept': 'application/json',
        'x_fields': 'x_fields_example',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{product_id}'.format(product_id='product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_authorization(client):
    """Test case for get_product_authorization

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_fields': 'x_fields_example',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{product_id}/authorizations/{authorization_id}'.format(product_id='product_id_example', authorization_id='authorization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reference_chromosome(client):
    """Test case for get_reference_chromosome

    Sequence for a region of the reference genome
    """
    params = [('range_start', 56),
                    ('range_stop', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_fields': 'x_fields_example',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/reference/genomes/{genome_build_accession}/chromosomes/{chromosome_accession}'.format(genome_build_accession='genome_build_accession_example', chromosome_accession='chromosome_accession_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reference_genome(client):
    """Test case for get_reference_genome

    Reference genome metadata
    """
    headers = { 
        'Accept': 'application/json',
        'x_fields': 'x_fields_example',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/reference/genomes/{genome_build_accession}/chromosomes'.format(genome_build_accession='genome_build_accession_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reference_genomes_group(client):
    """Test case for get_reference_genomes_group

    Reference genome builds
    """
    headers = { 
        'Accept': 'application/json',
        'x_fields': 'x_fields_example',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/reference/genomes/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reference_snp(client):
    """Test case for get_reference_snp

    Reference SNP data
    """
    params = [('dbsnp_version', 149),
                    ('grch_version', 'GRCH37P13')]
    headers = { 
        'Accept': 'application/json',
        'x_fields': 'x_fields_example',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/reference/snps/{snp_accession}'.format(snp_accession='snp_accession_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_authorization_result_credentials(client):
    """Test case for post_authorization_result_credentials

    Provide a result for the authorization
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_fields': 'x_fields_example',
        'Bearer': 'special-key',
    }
    data = {
        'credentials_username': 'credentials_username_example',
        'credentials_password': 'credentials_password_example',
        'report_url': 'report_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/products/{product_id}/authorizations/{authorization_id}/credentials'.format(product_id='product_id_example', authorization_id='authorization_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_authorization_result_file(client):
    """Test case for post_authorization_result_file

    Provide a file result to the authorization, e
    """
    params = [('original_filename', 'original_filename_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'x_fields': 'x_fields_example',
        'Bearer': 'special-key',
    }
    data = FormData()
    data.add_field('file_report', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v1/products/{product_id}/authorizations/{authorization_id}/file'.format(product_id='product_id_example', authorization_id='authorization_id_example'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_client_snp_group(client):
    """Test case for post_client_snp_group

    Get a large group of SNPs
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_fields': 'x_fields_example',
        'Bearer': 'special-key',
    }
    data = {
        'snps': 'snps_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/clients/{client_id}/datasets/{dataset_id}/snps'.format(client_id='client_id_example', dataset_id='dataset_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_jwt_auth(client):
    """Test case for post_jwt_auth

    General-purpose authentication
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_fields': 'x_fields_example',
    }
    data = {
        'username': 'username_example',
        'password': 'password_example',
        'role': 'role_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/auth/jwt',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_product_authorization(client):
    """Test case for post_product_authorization

    Signal that processing is complete, without uploading any result
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/products/{product_id}/authorizations/{authorization_id}'.format(product_id='product_id_example', authorization_id='authorization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_product_authorization_unfulfillable(client):
    """Test case for post_product_authorization_unfulfillable

    Catch-all Authorization state, for authorizations that passed all verifications and should reach the partner Product, but cannot be fulfilled for various reasons
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/products/{product_id}/authorizations/{authorization_id}/unfulfillable'.format(product_id='product_id_example', authorization_id='authorization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

