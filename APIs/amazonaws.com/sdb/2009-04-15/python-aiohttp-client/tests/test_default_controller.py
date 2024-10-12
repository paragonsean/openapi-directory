# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attribute_does_not_exist import AttributeDoesNotExist
from openapi_server.models.batch_delete_attributes_request import BatchDeleteAttributesRequest
from openapi_server.models.batch_put_attributes_request import BatchPutAttributesRequest
from openapi_server.models.create_domain_request import CreateDomainRequest
from openapi_server.models.delete_attributes_request import DeleteAttributesRequest
from openapi_server.models.delete_domain_request import DeleteDomainRequest
from openapi_server.models.domain_metadata_request import DomainMetadataRequest
from openapi_server.models.domain_metadata_result import DomainMetadataResult
from openapi_server.models.get_batch_delete_attributes_items_parameter_inner import GETBatchDeleteAttributesItemsParameterInner
from openapi_server.models.get_batch_put_attributes_items_parameter_inner import GETBatchPutAttributesItemsParameterInner
from openapi_server.models.get_delete_attributes_attributes_parameter_inner import GETDeleteAttributesAttributesParameterInner
from openapi_server.models.get_delete_attributes_expected_parameter import GETDeleteAttributesExpectedParameter
from openapi_server.models.get_put_attributes_attributes_parameter_inner import GETPutAttributesAttributesParameterInner
from openapi_server.models.get_attributes_request import GetAttributesRequest
from openapi_server.models.get_attributes_result import GetAttributesResult
from openapi_server.models.invalid_next_token import InvalidNextToken
from openapi_server.models.list_domains_request import ListDomainsRequest
from openapi_server.models.list_domains_result import ListDomainsResult
from openapi_server.models.missing_parameter import MissingParameter
from openapi_server.models.no_such_domain import NoSuchDomain
from openapi_server.models.number_domains_exceeded import NumberDomainsExceeded
from openapi_server.models.number_item_attributes_exceeded import NumberItemAttributesExceeded
from openapi_server.models.number_submitted_attributes_exceeded import NumberSubmittedAttributesExceeded
from openapi_server.models.put_attributes_request import PutAttributesRequest
from openapi_server.models.request_timeout import RequestTimeout
from openapi_server.models.select_request import SelectRequest
from openapi_server.models.select_result import SelectResult
from openapi_server.models.too_many_requested_attributes import TooManyRequestedAttributes


pytestmark = pytest.mark.asyncio

async def test_g_et_batch_delete_attributes(client):
    """Test case for g_et_batch_delete_attributes

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('DomainName', 'domain_name_example'),
                    ('Items', [openapi_server.GETBatchDeleteAttributesItemsParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=BatchDeleteAttributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_batch_put_attributes(client):
    """Test case for g_et_batch_put_attributes

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('DomainName', 'domain_name_example'),
                    ('Items', [openapi_server.GETBatchPutAttributesItemsParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=BatchPutAttributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_domain(client):
    """Test case for g_et_create_domain

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('DomainName', 'domain_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=CreateDomain',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_attributes(client):
    """Test case for g_et_delete_attributes

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('DomainName', 'domain_name_example'),
                    ('ItemName', 'item_name_example'),
                    ('Attributes', [openapi_server.GETDeleteAttributesAttributesParameterInner()]),
                    ('Expected', openapi_server.GETDeleteAttributesExpectedParameter()),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DeleteAttributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_domain(client):
    """Test case for g_et_delete_domain

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('DomainName', 'domain_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DeleteDomain',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_domain_metadata(client):
    """Test case for g_et_domain_metadata

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('DomainName', 'domain_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DomainMetadata',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_get_attributes(client):
    """Test case for g_et_get_attributes

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('DomainName', 'domain_name_example'),
                    ('ItemName', 'item_name_example'),
                    ('AttributeNames', ['attribute_names_example']),
                    ('ConsistentRead', True),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=GetAttributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_list_domains(client):
    """Test case for g_et_list_domains

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('MaxNumberOfDomains', 56),
                    ('NextToken', 'next_token_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=ListDomains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_put_attributes(client):
    """Test case for g_et_put_attributes

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('DomainName', 'domain_name_example'),
                    ('ItemName', 'item_name_example'),
                    ('Attributes', [openapi_server.GETPutAttributesAttributesParameterInner()]),
                    ('Expected', openapi_server.GETDeleteAttributesExpectedParameter()),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=PutAttributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_select(client):
    """Test case for g_et_select

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('SelectExpression', 'select_expression_example'),
                    ('NextToken', 'next_token_example'),
                    ('ConsistentRead', True),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=Select',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_batch_delete_attributes(client):
    """Test case for p_ost_batch_delete_attributes

    
    """
    body = openapi_server.BatchDeleteAttributesRequest()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=BatchDeleteAttributes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_batch_put_attributes(client):
    """Test case for p_ost_batch_put_attributes

    
    """
    body = openapi_server.BatchPutAttributesRequest()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=BatchPutAttributes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_domain(client):
    """Test case for p_ost_create_domain

    
    """
    body = openapi_server.CreateDomainRequest()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=CreateDomain',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_attributes(client):
    """Test case for p_ost_delete_attributes

    
    """
    body = openapi_server.DeleteAttributesRequest()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DeleteAttributes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_domain(client):
    """Test case for p_ost_delete_domain

    
    """
    body = openapi_server.DeleteDomainRequest()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DeleteDomain',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_domain_metadata(client):
    """Test case for p_ost_domain_metadata

    
    """
    body = openapi_server.DomainMetadataRequest()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DomainMetadata',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_get_attributes(client):
    """Test case for p_ost_get_attributes

    
    """
    body = openapi_server.GetAttributesRequest()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=GetAttributes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_list_domains(client):
    """Test case for p_ost_list_domains

    
    """
    body = openapi_server.ListDomainsRequest()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('MaxNumberOfDomains', 'max_number_of_domains_example'),
                    ('NextToken', 'next_token_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=ListDomains',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_put_attributes(client):
    """Test case for p_ost_put_attributes

    
    """
    body = openapi_server.PutAttributesRequest()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=PutAttributes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_select(client):
    """Test case for p_ost_select

    
    """
    body = openapi_server.SelectRequest()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('NextToken', 'next_token_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=Select',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

