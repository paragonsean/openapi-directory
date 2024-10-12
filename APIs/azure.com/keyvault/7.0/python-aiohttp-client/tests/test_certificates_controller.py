# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_certificate_result import BackupCertificateResult
from openapi_server.models.certificate_bundle import CertificateBundle
from openapi_server.models.certificate_create_parameters import CertificateCreateParameters
from openapi_server.models.certificate_import_parameters import CertificateImportParameters
from openapi_server.models.certificate_issuer_list_result import CertificateIssuerListResult
from openapi_server.models.certificate_issuer_set_parameters import CertificateIssuerSetParameters
from openapi_server.models.certificate_issuer_update_parameters import CertificateIssuerUpdateParameters
from openapi_server.models.certificate_list_result import CertificateListResult
from openapi_server.models.certificate_merge_parameters import CertificateMergeParameters
from openapi_server.models.certificate_operation import CertificateOperation
from openapi_server.models.certificate_operation_update_parameter import CertificateOperationUpdateParameter
from openapi_server.models.certificate_policy import CertificatePolicy
from openapi_server.models.certificate_restore_parameters import CertificateRestoreParameters
from openapi_server.models.certificate_update_parameters import CertificateUpdateParameters
from openapi_server.models.contacts import Contacts
from openapi_server.models.deleted_certificate_bundle import DeletedCertificateBundle
from openapi_server.models.issuer_bundle import IssuerBundle
from openapi_server.models.key_vault_error import KeyVaultError


pytestmark = pytest.mark.asyncio

async def test_backup_certificate(client):
    """Test case for backup_certificate

    Backs up the specified certificate.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/certificates/{certificate_name}/backup'.format(certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_certificate(client):
    """Test case for create_certificate

    Creates a new certificate.
    """
    parameters = {"attributes":{"recoveryLevel":"Purgeable"},"policy":{"x509_props":{"key_usage":["digitalSignature","digitalSignature"],"validity_months":0,"sans":{"emails":["emails","emails"],"dns_names":["dns_names","dns_names"],"upns":["upns","upns"]},"subject":"subject","ekus":["ekus","ekus"]},"attributes":{"recoveryLevel":"Purgeable"},"id":"id","secret_props":{"contentType":"contentType"},"issuer":{"cert_transparency":True,"name":"name","cty":"cty"},"lifetime_actions":[{"action":{"action_type":"EmailContacts"},"trigger":{"lifetime_percentage":15,"days_before_expiry":6}},{"action":{"action_type":"EmailContacts"},"trigger":{"lifetime_percentage":15,"days_before_expiry":6}}],"key_props":{"kty":"EC","exportable":True,"crv":"P-256","reuse_key":True,"key_size":0}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/certificates/{certificate_name}/create'.format(certificate_name='certificate_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_certificate(client):
    """Test case for delete_certificate

    Deletes a certificate from a specified key vault.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/certificates/{certificate_name}'.format(certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_certificate_contacts(client):
    """Test case for delete_certificate_contacts

    Deletes the certificate contacts for a specified key vault.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/certificates/contacts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_certificate_issuer(client):
    """Test case for delete_certificate_issuer

    Deletes the specified certificate issuer.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/certificates/issuers/{issuer_name}'.format(issuer_name='issuer_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_certificate_operation(client):
    """Test case for delete_certificate_operation

    Deletes the creation operation for a specific certificate.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/certificates/{certificate_name}/pending'.format(certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_certificate(client):
    """Test case for get_certificate

    Gets information about a certificate.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/certificates/{certificate_name}/{certificate_version}'.format(certificate_name='certificate_name_example', certificate_version='certificate_version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_certificate_contacts(client):
    """Test case for get_certificate_contacts

    Lists the certificate contacts for a specified key vault.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/certificates/contacts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_certificate_issuer(client):
    """Test case for get_certificate_issuer

    Lists the specified certificate issuer.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/certificates/issuers/{issuer_name}'.format(issuer_name='issuer_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_certificate_issuers(client):
    """Test case for get_certificate_issuers

    List certificate issuers for a specified key vault.
    """
    params = [('maxresults', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/certificates/issuers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_certificate_operation(client):
    """Test case for get_certificate_operation

    Gets the creation operation of a certificate.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/certificates/{certificate_name}/pending'.format(certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_certificate_policy(client):
    """Test case for get_certificate_policy

    Lists the policy for a certificate.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/certificates/{certificate_name}/policy'.format(certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_certificate_versions(client):
    """Test case for get_certificate_versions

    List the versions of a certificate.
    """
    params = [('maxresults', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/certificates/{certificate_name}/versions'.format(certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_certificates(client):
    """Test case for get_certificates

    List certificates in a specified key vault
    """
    params = [('maxresults', 56),
                    ('includePending', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/certificates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_import_certificate(client):
    """Test case for import_certificate

    Imports a certificate into a specified key vault.
    """
    parameters = {"attributes":{"recoveryLevel":"Purgeable"},"pwd":"pwd","value":"value","policy":{"x509_props":{"key_usage":["digitalSignature","digitalSignature"],"validity_months":0,"sans":{"emails":["emails","emails"],"dns_names":["dns_names","dns_names"],"upns":["upns","upns"]},"subject":"subject","ekus":["ekus","ekus"]},"attributes":{"recoveryLevel":"Purgeable"},"id":"id","secret_props":{"contentType":"contentType"},"issuer":{"cert_transparency":True,"name":"name","cty":"cty"},"lifetime_actions":[{"action":{"action_type":"EmailContacts"},"trigger":{"lifetime_percentage":15,"days_before_expiry":6}},{"action":{"action_type":"EmailContacts"},"trigger":{"lifetime_percentage":15,"days_before_expiry":6}}],"key_props":{"kty":"EC","exportable":True,"crv":"P-256","reuse_key":True,"key_size":0}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/certificates/{certificate_name}/import'.format(certificate_name='certificate_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_merge_certificate(client):
    """Test case for merge_certificate

    Merges a certificate or a certificate chain with a key pair existing on the server.
    """
    parameters = {"x5c":["x5c","x5c"],"attributes":{"recoveryLevel":"Purgeable"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/certificates/{certificate_name}/pending/merge'.format(certificate_name='certificate_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restore_certificate(client):
    """Test case for restore_certificate

    Restores a backed up certificate to a vault.
    """
    parameters = {"value":"value"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/certificates/restore',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_certificate_contacts(client):
    """Test case for set_certificate_contacts

    Sets the certificate contacts for the specified key vault.
    """
    contacts = {"id":"id","contacts":[{"phone":"phone","name":"name","email":"email"},{"phone":"phone","name":"name","email":"email"}]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/certificates/contacts',
        headers=headers,
        json=contacts,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_certificate_issuer(client):
    """Test case for set_certificate_issuer

    Sets the specified certificate issuer.
    """
    parameter = {"credentials":{"account_id":"account_id","pwd":"pwd"},"provider":"provider","org_details":{"admin_details":[{"phone":"phone","last_name":"last_name","first_name":"first_name","email":"email"},{"phone":"phone","last_name":"last_name","first_name":"first_name","email":"email"}],"id":"id"},"attributes":{"created":0,"updated":6,"enabled":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/certificates/issuers/{issuer_name}'.format(issuer_name='issuer_name_example'),
        headers=headers,
        json=parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_certificate(client):
    """Test case for update_certificate

    Updates the specified attributes associated with the given certificate.
    """
    parameters = {"attributes":{"recoveryLevel":"Purgeable"},"policy":{"x509_props":{"key_usage":["digitalSignature","digitalSignature"],"validity_months":0,"sans":{"emails":["emails","emails"],"dns_names":["dns_names","dns_names"],"upns":["upns","upns"]},"subject":"subject","ekus":["ekus","ekus"]},"attributes":{"recoveryLevel":"Purgeable"},"id":"id","secret_props":{"contentType":"contentType"},"issuer":{"cert_transparency":True,"name":"name","cty":"cty"},"lifetime_actions":[{"action":{"action_type":"EmailContacts"},"trigger":{"lifetime_percentage":15,"days_before_expiry":6}},{"action":{"action_type":"EmailContacts"},"trigger":{"lifetime_percentage":15,"days_before_expiry":6}}],"key_props":{"kty":"EC","exportable":True,"crv":"P-256","reuse_key":True,"key_size":0}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/certificates/{certificate_name}/{certificate_version}'.format(certificate_name='certificate_name_example', certificate_version='certificate_version_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_certificate_issuer(client):
    """Test case for update_certificate_issuer

    Updates the specified certificate issuer.
    """
    parameter = {"credentials":{"account_id":"account_id","pwd":"pwd"},"provider":"provider","org_details":{"admin_details":[{"phone":"phone","last_name":"last_name","first_name":"first_name","email":"email"},{"phone":"phone","last_name":"last_name","first_name":"first_name","email":"email"}],"id":"id"},"attributes":{"created":0,"updated":6,"enabled":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/certificates/issuers/{issuer_name}'.format(issuer_name='issuer_name_example'),
        headers=headers,
        json=parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_certificate_operation(client):
    """Test case for update_certificate_operation

    Updates a certificate operation.
    """
    certificate_operation = {"cancellation_requested":True}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/certificates/{certificate_name}/pending'.format(certificate_name='certificate_name_example'),
        headers=headers,
        json=certificate_operation,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_certificate_policy(client):
    """Test case for update_certificate_policy

    Updates the policy for a certificate.
    """
    certificate_policy = {"x509_props":{"key_usage":["digitalSignature","digitalSignature"],"validity_months":0,"sans":{"emails":["emails","emails"],"dns_names":["dns_names","dns_names"],"upns":["upns","upns"]},"subject":"subject","ekus":["ekus","ekus"]},"attributes":{"recoveryLevel":"Purgeable"},"id":"id","secret_props":{"contentType":"contentType"},"issuer":{"cert_transparency":True,"name":"name","cty":"cty"},"lifetime_actions":[{"action":{"action_type":"EmailContacts"},"trigger":{"lifetime_percentage":15,"days_before_expiry":6}},{"action":{"action_type":"EmailContacts"},"trigger":{"lifetime_percentage":15,"days_before_expiry":6}}],"key_props":{"kty":"EC","exportable":True,"crv":"P-256","reuse_key":True,"key_size":0}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/certificates/{certificate_name}/policy'.format(certificate_name='certificate_name_example'),
        headers=headers,
        json=certificate_policy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

