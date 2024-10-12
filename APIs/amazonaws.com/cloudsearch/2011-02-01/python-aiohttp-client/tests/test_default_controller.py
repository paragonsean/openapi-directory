# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_exception import BaseException
from openapi_server.models.create_domain_request import CreateDomainRequest
from openapi_server.models.create_domain_response import CreateDomainResponse
from openapi_server.models.define_index_field_request import DefineIndexFieldRequest
from openapi_server.models.define_index_field_response import DefineIndexFieldResponse
from openapi_server.models.define_rank_expression_request import DefineRankExpressionRequest
from openapi_server.models.define_rank_expression_response import DefineRankExpressionResponse
from openapi_server.models.delete_domain_request import DeleteDomainRequest
from openapi_server.models.delete_domain_response import DeleteDomainResponse
from openapi_server.models.delete_index_field_request import DeleteIndexFieldRequest
from openapi_server.models.delete_index_field_response import DeleteIndexFieldResponse
from openapi_server.models.delete_rank_expression_request import DeleteRankExpressionRequest
from openapi_server.models.delete_rank_expression_response import DeleteRankExpressionResponse
from openapi_server.models.describe_availability_options_request import DescribeAvailabilityOptionsRequest
from openapi_server.models.describe_availability_options_response import DescribeAvailabilityOptionsResponse
from openapi_server.models.describe_default_search_field_request import DescribeDefaultSearchFieldRequest
from openapi_server.models.describe_default_search_field_response import DescribeDefaultSearchFieldResponse
from openapi_server.models.describe_domains_request import DescribeDomainsRequest
from openapi_server.models.describe_domains_response import DescribeDomainsResponse
from openapi_server.models.describe_index_fields_request import DescribeIndexFieldsRequest
from openapi_server.models.describe_index_fields_response import DescribeIndexFieldsResponse
from openapi_server.models.describe_rank_expressions_request import DescribeRankExpressionsRequest
from openapi_server.models.describe_rank_expressions_response import DescribeRankExpressionsResponse
from openapi_server.models.describe_service_access_policies_request import DescribeServiceAccessPoliciesRequest
from openapi_server.models.describe_service_access_policies_response import DescribeServiceAccessPoliciesResponse
from openapi_server.models.describe_stemming_options_request import DescribeStemmingOptionsRequest
from openapi_server.models.describe_stemming_options_response import DescribeStemmingOptionsResponse
from openapi_server.models.describe_stopword_options_request import DescribeStopwordOptionsRequest
from openapi_server.models.describe_stopword_options_response import DescribeStopwordOptionsResponse
from openapi_server.models.describe_synonym_options_request import DescribeSynonymOptionsRequest
from openapi_server.models.describe_synonym_options_response import DescribeSynonymOptionsResponse
from openapi_server.models.get_define_index_field_index_field_parameter import GETDefineIndexFieldIndexFieldParameter
from openapi_server.models.get_define_rank_expression_rank_expression_parameter import GETDefineRankExpressionRankExpressionParameter
from openapi_server.models.index_documents_request import IndexDocumentsRequest
from openapi_server.models.index_documents_response import IndexDocumentsResponse
from openapi_server.models.update_availability_options_request import UpdateAvailabilityOptionsRequest
from openapi_server.models.update_availability_options_response import UpdateAvailabilityOptionsResponse
from openapi_server.models.update_default_search_field_request import UpdateDefaultSearchFieldRequest
from openapi_server.models.update_default_search_field_response import UpdateDefaultSearchFieldResponse
from openapi_server.models.update_service_access_policies_request import UpdateServiceAccessPoliciesRequest
from openapi_server.models.update_service_access_policies_response import UpdateServiceAccessPoliciesResponse
from openapi_server.models.update_stemming_options_request import UpdateStemmingOptionsRequest
from openapi_server.models.update_stemming_options_response import UpdateStemmingOptionsResponse
from openapi_server.models.update_stopword_options_request import UpdateStopwordOptionsRequest
from openapi_server.models.update_stopword_options_response import UpdateStopwordOptionsResponse
from openapi_server.models.update_synonym_options_request import UpdateSynonymOptionsRequest
from openapi_server.models.update_synonym_options_response import UpdateSynonymOptionsResponse


pytestmark = pytest.mark.asyncio

async def test_g_et_create_domain(client):
    """Test case for g_et_create_domain

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
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

async def test_g_et_define_index_field(client):
    """Test case for g_et_define_index_field

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('IndexField', openapi_server.GETDefineIndexFieldIndexFieldParameter()),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DefineIndexField',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_define_rank_expression(client):
    """Test case for g_et_define_rank_expression

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('RankExpression', openapi_server.GETDefineRankExpressionRankExpressionParameter()),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DefineRankExpression',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_domain(client):
    """Test case for g_et_delete_domain

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
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

async def test_g_et_delete_index_field(client):
    """Test case for g_et_delete_index_field

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('IndexFieldName', 'index_field_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DeleteIndexField',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_rank_expression(client):
    """Test case for g_et_delete_rank_expression

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('RankName', 'rank_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DeleteRankExpression',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_availability_options(client):
    """Test case for g_et_describe_availability_options

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeAvailabilityOptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_default_search_field(client):
    """Test case for g_et_describe_default_search_field

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeDefaultSearchField',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_domains(client):
    """Test case for g_et_describe_domains

    
    """
    params = [('DomainNames', ['domain_names_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeDomains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_index_fields(client):
    """Test case for g_et_describe_index_fields

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('FieldNames', ['field_names_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeIndexFields',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_rank_expressions(client):
    """Test case for g_et_describe_rank_expressions

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('RankNames', ['rank_names_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeRankExpressions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_service_access_policies(client):
    """Test case for g_et_describe_service_access_policies

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeServiceAccessPolicies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_stemming_options(client):
    """Test case for g_et_describe_stemming_options

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeStemmingOptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_stopword_options(client):
    """Test case for g_et_describe_stopword_options

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeStopwordOptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_synonym_options(client):
    """Test case for g_et_describe_synonym_options

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeSynonymOptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_index_documents(client):
    """Test case for g_et_index_documents

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=IndexDocuments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_update_availability_options(client):
    """Test case for g_et_update_availability_options

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('MultiAZ', True),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=UpdateAvailabilityOptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_update_default_search_field(client):
    """Test case for g_et_update_default_search_field

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('DefaultSearchField', 'default_search_field_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=UpdateDefaultSearchField',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_update_service_access_policies(client):
    """Test case for g_et_update_service_access_policies

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('AccessPolicies', 'access_policies_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=UpdateServiceAccessPolicies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_update_stemming_options(client):
    """Test case for g_et_update_stemming_options

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('Stems', 'stems_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=UpdateStemmingOptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_update_stopword_options(client):
    """Test case for g_et_update_stopword_options

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('Stopwords', 'stopwords_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=UpdateStopwordOptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_update_synonym_options(client):
    """Test case for g_et_update_synonym_options

    
    """
    params = [('DomainName', 'domain_name_example'),
                    ('Synonyms', 'synonyms_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=UpdateSynonymOptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_domain(client):
    """Test case for p_ost_create_domain

    
    """
    body = openapi_server.CreateDomainRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
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
async def test_p_ost_define_index_field(client):
    """Test case for p_ost_define_index_field

    
    """
    body = openapi_server.DefineIndexFieldRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DefineIndexField',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_define_rank_expression(client):
    """Test case for p_ost_define_rank_expression

    
    """
    body = openapi_server.DefineRankExpressionRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DefineRankExpression',
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
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
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
async def test_p_ost_delete_index_field(client):
    """Test case for p_ost_delete_index_field

    
    """
    body = openapi_server.DeleteIndexFieldRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DeleteIndexField',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_rank_expression(client):
    """Test case for p_ost_delete_rank_expression

    
    """
    body = openapi_server.DeleteRankExpressionRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DeleteRankExpression',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_availability_options(client):
    """Test case for p_ost_describe_availability_options

    
    """
    body = openapi_server.DescribeAvailabilityOptionsRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeAvailabilityOptions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_default_search_field(client):
    """Test case for p_ost_describe_default_search_field

    
    """
    body = openapi_server.DescribeDefaultSearchFieldRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeDefaultSearchField',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_domains(client):
    """Test case for p_ost_describe_domains

    
    """
    body = openapi_server.DescribeDomainsRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeDomains',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_index_fields(client):
    """Test case for p_ost_describe_index_fields

    
    """
    body = openapi_server.DescribeIndexFieldsRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeIndexFields',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_rank_expressions(client):
    """Test case for p_ost_describe_rank_expressions

    
    """
    body = openapi_server.DescribeRankExpressionsRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeRankExpressions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_service_access_policies(client):
    """Test case for p_ost_describe_service_access_policies

    
    """
    body = openapi_server.DescribeServiceAccessPoliciesRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeServiceAccessPolicies',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_stemming_options(client):
    """Test case for p_ost_describe_stemming_options

    
    """
    body = openapi_server.DescribeStemmingOptionsRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeStemmingOptions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_stopword_options(client):
    """Test case for p_ost_describe_stopword_options

    
    """
    body = openapi_server.DescribeStopwordOptionsRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeStopwordOptions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_synonym_options(client):
    """Test case for p_ost_describe_synonym_options

    
    """
    body = openapi_server.DescribeSynonymOptionsRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeSynonymOptions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_index_documents(client):
    """Test case for p_ost_index_documents

    
    """
    body = openapi_server.IndexDocumentsRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=IndexDocuments',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_update_availability_options(client):
    """Test case for p_ost_update_availability_options

    
    """
    body = openapi_server.UpdateAvailabilityOptionsRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=UpdateAvailabilityOptions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_update_default_search_field(client):
    """Test case for p_ost_update_default_search_field

    
    """
    body = openapi_server.UpdateDefaultSearchFieldRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=UpdateDefaultSearchField',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_update_service_access_policies(client):
    """Test case for p_ost_update_service_access_policies

    
    """
    body = openapi_server.UpdateServiceAccessPoliciesRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=UpdateServiceAccessPolicies',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_update_stemming_options(client):
    """Test case for p_ost_update_stemming_options

    
    """
    body = openapi_server.UpdateStemmingOptionsRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=UpdateStemmingOptions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_update_stopword_options(client):
    """Test case for p_ost_update_stopword_options

    
    """
    body = openapi_server.UpdateStopwordOptionsRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=UpdateStopwordOptions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_update_synonym_options(client):
    """Test case for p_ost_update_synonym_options

    
    """
    body = openapi_server.UpdateSynonymOptionsRequest()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=UpdateSynonymOptions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

