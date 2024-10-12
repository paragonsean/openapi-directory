# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate import Certificate
from openapi_server.models.certificate_action import CertificateAction
from openapi_server.models.certificate_bundle import CertificateBundle
from openapi_server.models.certificate_callback import CertificateCallback
from openapi_server.models.certificate_create import CertificateCreate
from openapi_server.models.certificate_email_history import CertificateEmailHistory
from openapi_server.models.certificate_identifier import CertificateIdentifier
from openapi_server.models.certificate_reissue import CertificateReissue
from openapi_server.models.certificate_renew import CertificateRenew
from openapi_server.models.certificate_revoke import CertificateRevoke
from openapi_server.models.certificate_site_seal import CertificateSiteSeal
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_certificate_action_retrieve(client):
    """Test case for certificate_action_retrieve

    Retrieve all certificate actions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/certificates/{certificate_id}/actions'.format(certificate_id='certificate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_alternate_email_address(client):
    """Test case for certificate_alternate_email_address

    Add alternate email address
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/certificates/{certificate_id}/email/resend/{email_address}'.format(certificate_id='certificate_id_example', email_address='email_address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_callback_delete(client):
    """Test case for certificate_callback_delete

    Unregister system callback
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/certificates/{certificate_id}/callback'.format(certificate_id='certificate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_callback_get(client):
    """Test case for certificate_callback_get

    Retrieve system stateful action callback url
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/certificates/{certificate_id}/callback'.format(certificate_id='certificate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_callback_replace(client):
    """Test case for certificate_callback_replace

    Register of certificate action callback
    """
    params = [('callbackUrl', 'callback_url_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/certificates/{certificate_id}/callback'.format(certificate_id='certificate_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_cancel(client):
    """Test case for certificate_cancel

    Cancel a pending certificate
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/certificates/{certificate_id}/cancel'.format(certificate_id='certificate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_create(client):
    """Test case for certificate_create

    Create a pending order for certificate
    """
    body = {"commonName":"commonName","period":0,"rootType":"STARFIELD_SHA_2","csr":"csr","slotSize":"FIVE","intelVPro":False,"subjectAlternativeNames":["subjectAlternativeNames","subjectAlternativeNames"],"contact":{"nameLast":"nameLast","nameFirst":"nameFirst","phone":"phone","jobTitle":"jobTitle","suffix":"suffix","nameMiddle":"nameMiddle","email":"email"},"organization":{"assumedName":"assumedName","address":{"country":"AC","address2":"address2","city":"city","address1":"address1","postalCode":"postalCode","state":"state"},"phone":"phone","registrationNumber":"registrationNumber","name":"name","registrationAgent":"registrationAgent"},"callbackUrl":"callbackUrl","productType":"DV_SSL"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_market_id': 'Default locale for shopper account',
    }
    response = await client.request(
        method='POST',
        path='/v1/certificates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_download(client):
    """Test case for certificate_download

    Download certificate
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/certificates/{certificate_id}/download'.format(certificate_id='certificate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_download_entitlement(client):
    """Test case for certificate_download_entitlement

    Download certificate by entitlement
    """
    params = [('entitlementId', 'entitlement_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/certificates/download',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_email_history(client):
    """Test case for certificate_email_history

    Retrieve email history
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/certificates/{certificate_id}/email/history'.format(certificate_id='certificate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_get(client):
    """Test case for certificate_get

    Retrieve certificate details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/certificates/{certificate_id}'.format(certificate_id='certificate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_get_entitlement(client):
    """Test case for certificate_get_entitlement

    Search for certificate details by entitlement
    """
    params = [('entitlementId', 'entitlement_id_example'),
                    ('latest', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/certificates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_reissue(client):
    """Test case for certificate_reissue

    Reissue active certificate
    """
    body = {"commonName":"Existing common name","rootType":"GODADDY_SHA_1","csr":"Existing CSR","subjectAlternativeNames":["subjectAlternativeNames","subjectAlternativeNames"],"callbackUrl":"callbackUrl","forceDomainRevetting":["forceDomainRevetting","forceDomainRevetting"],"delayExistingRevoke":13}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/certificates/{certificate_id}/reissue'.format(certificate_id='certificate_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_renew(client):
    """Test case for certificate_renew

    Renew active certificate
    """
    body = {"commonName":"Existing common name","period":0,"rootType":"GODADDY_SHA_1","csr":"Existing CSR","subjectAlternativeNames":["subjectAlternativeNames","subjectAlternativeNames"],"callbackUrl":"callbackUrl"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/certificates/{certificate_id}/renew'.format(certificate_id='certificate_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_resend_email(client):
    """Test case for certificate_resend_email

    Resend an email
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/certificates/{certificate_id}/email/{email_id}/resend'.format(certificate_id='certificate_id_example', email_id='email_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_resend_email_address(client):
    """Test case for certificate_resend_email_address

    Resend email to email address
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/certificates/{certificate_id}/email/{email_id}/resend/{email_address}'.format(certificate_id='certificate_id_example', email_id='email_id_example', email_address='email_address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_revoke(client):
    """Test case for certificate_revoke

    Revoke active certificate
    """
    body = {"reason":"AFFILIATION_CHANGED"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/certificates/{certificate_id}/revoke'.format(certificate_id='certificate_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_siteseal_get(client):
    """Test case for certificate_siteseal_get

    Get Site seal
    """
    params = [('theme', LIGHT),
                    ('locale', 'en')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/certificates/{certificate_id}/siteSeal'.format(certificate_id='certificate_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_validate(client):
    """Test case for certificate_validate

    Validate a pending order for certificate
    """
    body = {"commonName":"commonName","period":0,"rootType":"STARFIELD_SHA_2","csr":"csr","slotSize":"FIVE","intelVPro":False,"subjectAlternativeNames":["subjectAlternativeNames","subjectAlternativeNames"],"contact":{"nameLast":"nameLast","nameFirst":"nameFirst","phone":"phone","jobTitle":"jobTitle","suffix":"suffix","nameMiddle":"nameMiddle","email":"email"},"organization":{"assumedName":"assumedName","address":{"country":"AC","address2":"address2","city":"city","address1":"address1","postalCode":"postalCode","state":"state"},"phone":"phone","registrationNumber":"registrationNumber","name":"name","registrationAgent":"registrationAgent"},"callbackUrl":"callbackUrl","productType":"DV_SSL"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_market_id': 'Default locale for shopper account',
    }
    response = await client.request(
        method='POST',
        path='/v1/certificates/validate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_verifydomaincontrol(client):
    """Test case for certificate_verifydomaincontrol

    Check Domain Control
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/certificates/{certificate_id}/verifyDomainControl'.format(certificate_id='certificate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

