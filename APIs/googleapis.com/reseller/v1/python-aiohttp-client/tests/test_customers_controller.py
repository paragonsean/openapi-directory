# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer import Customer


pytestmark = pytest.mark.asyncio

async def test_reseller_customers_get(client):
    """Test case for reseller_customers_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/reseller/v1/customers/{customer_id}'.format(customer_id='customer_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reseller_customers_insert(client):
    """Test case for reseller_customers_insert

    
    """
    body = {"alternateEmail":"alternateEmail","customerType":"customerTypeUnspecified","phoneNumber":"phoneNumber","postalAddress":{"organizationName":"organizationName","contactName":"contactName","countryCode":"countryCode","kind":"customers#address","postalCode":"postalCode","locality":"locality","addressLine1":"addressLine1","addressLine2":"addressLine2","addressLine3":"addressLine3","region":"region"},"customerDomain":"customerDomain","primaryAdmin":{"primaryEmail":"primaryEmail"},"kind":"reseller#customer","customerId":"customerId","customerDomainVerified":True,"resourceUiUrl":"resourceUiUrl"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('customerAuthToken', 'customer_auth_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/reseller/v1/customers',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reseller_customers_patch(client):
    """Test case for reseller_customers_patch

    
    """
    body = {"alternateEmail":"alternateEmail","customerType":"customerTypeUnspecified","phoneNumber":"phoneNumber","postalAddress":{"organizationName":"organizationName","contactName":"contactName","countryCode":"countryCode","kind":"customers#address","postalCode":"postalCode","locality":"locality","addressLine1":"addressLine1","addressLine2":"addressLine2","addressLine3":"addressLine3","region":"region"},"customerDomain":"customerDomain","primaryAdmin":{"primaryEmail":"primaryEmail"},"kind":"reseller#customer","customerId":"customerId","customerDomainVerified":True,"resourceUiUrl":"resourceUiUrl"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/apps/reseller/v1/customers/{customer_id}'.format(customer_id='customer_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reseller_customers_update(client):
    """Test case for reseller_customers_update

    
    """
    body = {"alternateEmail":"alternateEmail","customerType":"customerTypeUnspecified","phoneNumber":"phoneNumber","postalAddress":{"organizationName":"organizationName","contactName":"contactName","countryCode":"countryCode","kind":"customers#address","postalCode":"postalCode","locality":"locality","addressLine1":"addressLine1","addressLine2":"addressLine2","addressLine3":"addressLine3","region":"region"},"customerDomain":"customerDomain","primaryAdmin":{"primaryEmail":"primaryEmail"},"kind":"reseller#customer","customerId":"customerId","customerDomainVerified":True,"resourceUiUrl":"resourceUiUrl"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apps/reseller/v1/customers/{customer_id}'.format(customer_id='customer_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

