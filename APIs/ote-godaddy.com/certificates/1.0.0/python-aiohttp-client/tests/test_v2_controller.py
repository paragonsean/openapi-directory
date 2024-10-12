# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate_detail_v2 import CertificateDetailV2
from openapi_server.models.certificate_summaries_v2 import CertificateSummariesV2
from openapi_server.models.domain_verification_detail import DomainVerificationDetail
from openapi_server.models.domain_verification_summary import DomainVerificationSummary
from openapi_server.models.error import Error
from openapi_server.models.error_limit import ErrorLimit
from openapi_server.models.external_account_binding import ExternalAccountBinding


pytestmark = pytest.mark.asyncio

async def test_get_acme_external_account_binding(client):
    """Test case for get_acme_external_account_binding

    Retrieves the external account binding for the specified customer
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customers/{customer_id}/certificates/acme/externalAccountBinding'.format(customer_id='customer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_certificate_detail_by_cert_identifier(client):
    """Test case for get_certificate_detail_by_cert_identifier

    Retrieve individual certificate details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customers/{customer_id}/certificates/{certificate_id}'.format(customer_id='customer_id_example', certificate_id='certificate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customer_certificates_by_customer_id(client):
    """Test case for get_customer_certificates_by_customer_id

    Retrieve customer's certificates
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customers/{customer_id}/certificates'.format(customer_id='customer_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domain_details_by_domain(client):
    """Test case for get_domain_details_by_domain

    Retrieve detailed information for supplied domain
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customers/{customer_id}/certificates/{certificate_id}/domainVerifications/{domain}'.format(customer_id='customer_id_example', certificate_id='certificate_id_example', domain='domain_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domain_information_by_certificate_id(client):
    """Test case for get_domain_information_by_certificate_id

    Retrieve domain verification status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customers/{customer_id}/certificates/{certificate_id}/domainVerifications'.format(customer_id='customer_id_example', certificate_id='certificate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

