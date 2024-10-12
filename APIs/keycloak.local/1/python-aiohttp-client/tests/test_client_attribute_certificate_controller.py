# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate_representation import CertificateRepresentation
from openapi_server.models.key_store_config import KeyStoreConfig


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_certificates_attr_download_post(client):
    """Test case for realm_clients_id_certificates_attr_download_post

    Get a keystore file for the client, containing private key and public certificate
    """
    body = {"storePassword":"storePassword","keyAlias":"keyAlias","keyPassword":"keyPassword","format":"format","realmCertificate":True,"realmAlias":"realmAlias"}
    headers = { 
        'Accept': 'application/octet-stream',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/certificates/{attr}/download'.format(realm='realm_example', id='id_example', attr='attr_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_certificates_attr_generate_and_download_post(client):
    """Test case for realm_clients_id_certificates_attr_generate_and_download_post

    Generate a new keypair and certificate, and get the private key file   Generates a keypair and certificate and serves the private key in a specified keystore format.
    """
    body = {"storePassword":"storePassword","keyAlias":"keyAlias","keyPassword":"keyPassword","format":"format","realmCertificate":True,"realmAlias":"realmAlias"}
    headers = { 
        'Accept': 'application/octet-stream',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/certificates/{attr}/generate-and-download'.format(realm='realm_example', id='id_example', attr='attr_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_certificates_attr_generate_post(client):
    """Test case for realm_clients_id_certificates_attr_generate_post

    Generate a new certificate with new key pair
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/certificates/{attr}/generate'.format(realm='realm_example', id='id_example', attr='attr_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_certificates_attr_get(client):
    """Test case for realm_clients_id_certificates_attr_get

    Get key info
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/certificates/{attr}'.format(realm='realm_example', id='id_example', attr='attr_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_certificates_attr_upload_certificate_post(client):
    """Test case for realm_clients_id_certificates_attr_upload_certificate_post

    Upload only certificate, not private key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/certificates/{attr}/upload-certificate'.format(realm='realm_example', id='id_example', attr='attr_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_certificates_attr_upload_post(client):
    """Test case for realm_clients_id_certificates_attr_upload_post

    Upload certificate and eventually private key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/certificates/{attr}/upload'.format(realm='realm_example', id='id_example', attr='attr_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

