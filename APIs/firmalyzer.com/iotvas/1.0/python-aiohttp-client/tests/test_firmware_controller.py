# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.config_issue import ConfigIssue
from openapi_server.models.crypto_key import CryptoKey
from openapi_server.models.default_account import DefaultAccount
from openapi_server.models.expired_cert import ExpiredCert
from openapi_server.models.firmware_risk import FirmwareRisk
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.weak_cert import WeakCert


pytestmark = pytest.mark.asyncio

async def test_get_accounts(client):
    """Test case for get_accounts

    Get default accounts and password hashes of a firmware
    """
    headers = { 
        'Accept': 'application/json',
        'api-key-header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/firmware/{firmware_hash}/accounts'.format(firmware_hash='af88b1aaac0b222df8539f3ae1479b5c8eaeae41f1776b5dd2fa805cb33a1175'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_config_issues(client):
    """Test case for get_config_issues

    Get default OS configuration issues of a device firmware
    """
    headers = { 
        'Accept': 'application/json',
        'api-key-header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/firmware/{firmware_hash}/config-issues'.format(firmware_hash='aa96e4d41a4b0ceb3f1ae4d94f3cb445621b9501e3a9c69e6b9eb37c5888a03c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_expired_certs(client):
    """Test case for get_expired_certs

    Get expired digital certificates embedded in a device firmware
    """
    headers = { 
        'Accept': 'application/json',
        'api-key-header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/firmware/{firmware_hash}/expired-certs'.format(firmware_hash='ac7c090c34338ea6a3b335004755e24578e7e4eee739c5c33736f0822b64907e'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_private_keys(client):
    """Test case for get_private_keys

    Get private crypto keys embedded in a device firmware
    """
    headers = { 
        'Accept': 'application/json',
        'api-key-header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/firmware/{firmware_hash}/private-keys'.format(firmware_hash='90e3e68e1c61850f20c50e551816d47d484d7feb46890f5bc0a0e0dab3e3ba0b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_risk(client):
    """Test case for get_risk

    Get iot device firmware risk analysis
    """
    headers = { 
        'Accept': 'application/json',
        'api-key-header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/firmware/{firmware_hash}/risk'.format(firmware_hash='af88b1aaac0b222df8539f3ae1479b5c8eaeae41f1776b5dd2fa805cb33a1175'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_weak_certs(client):
    """Test case for get_weak_certs

    Get certificates with weak fingerprinting algorithms that are mebedded in a device firmware
    """
    headers = { 
        'Accept': 'application/json',
        'api-key-header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/firmware/{firmware_hash}/weak-certs'.format(firmware_hash='52841661d61e00649451cc471e9b56d169df8041926b1252bb3fd0710c27b12c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_weak_keys(client):
    """Test case for get_weak_keys

    Get weak crypto keys with short length
    """
    headers = { 
        'Accept': 'application/json',
        'api-key-header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/firmware/{firmware_hash}/weak-keys'.format(firmware_hash='852031776c09f8152c90496f2c3fac85b46a938d20612d7fc03eea8aab46f23e'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

