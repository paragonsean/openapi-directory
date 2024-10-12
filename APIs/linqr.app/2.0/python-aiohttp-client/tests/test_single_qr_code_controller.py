# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auto_qr_code import AutoQRCode
from openapi_server.models.auto_qr_code_multipart_body import AutoQRCodeMultipartBody
from openapi_server.models.contact_qr_code import ContactQRCode
from openapi_server.models.contact_qr_code_multipart_body import ContactQRCodeMultipartBody
from openapi_server.models.crypto_payment_qr_code import CryptoPaymentQRCode
from openapi_server.models.crypto_payment_qr_code_multipart_body import CryptoPaymentQRCodeMultipartBody
from openapi_server.models.email_qr_code import EmailQRCode
from openapi_server.models.email_qr_code_multipart_body import EmailQRCodeMultipartBody
from openapi_server.models.generic_error import GenericError
from openapi_server.models.geolocation_qr_code import GeolocationQRCode
from openapi_server.models.geolocation_qr_code_multipart_body import GeolocationQRCodeMultipartBody
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.phone_qr_code import PhoneQRCode
from openapi_server.models.phone_qr_code_multipart_body import PhoneQRCodeMultipartBody
from openapi_server.models.smsqr_code import SMSQRCode
from openapi_server.models.smsqr_code_multipart_body import SMSQRCodeMultipartBody
from openapi_server.models.text_qr_code import TextQRCode
from openapi_server.models.text_qr_code_multipart_body import TextQRCodeMultipartBody
from openapi_server.models.wi_fi_qr_code import WiFiQRCode
from openapi_server.models.wi_fi_qr_code_multipart_body import WiFiQRCodeMultipartBody


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_dispatcher_qrcode_contact_post(client):
    """Test case for dispatcher_qrcode_contact_post

    Contact QR Code
    """
    body = {"output":"","image":"","data":"","size":"","style":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Byvalue': 'special-key',
        'RapidAPI': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/qrcode/contact',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_dispatcher_qrcode_crypto_post(client):
    """Test case for dispatcher_qrcode_crypto_post

    Cryptocurrency payment QR Code
    """
    body = {"output":"","image":"","data":"","size":"","style":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Byvalue': 'special-key',
        'RapidAPI': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/qrcode/crypto',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_dispatcher_qrcode_email_post(client):
    """Test case for dispatcher_qrcode_email_post

    Email QR Code
    """
    body = {"output":"","image":"","data":"","size":"","style":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Byvalue': 'special-key',
        'RapidAPI': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/qrcode/email',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_dispatcher_qrcode_geo_post(client):
    """Test case for dispatcher_qrcode_geo_post

    Geolocation QR Code
    """
    body = {"output":"","image":"","data":"","size":"","style":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Byvalue': 'special-key',
        'RapidAPI': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/qrcode/geo',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_dispatcher_qrcode_phone_post(client):
    """Test case for dispatcher_qrcode_phone_post

    Telephone QR Code
    """
    body = {"output":"","image":"","data":"","size":"","style":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Byvalue': 'special-key',
        'RapidAPI': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/qrcode/phone',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_dispatcher_qrcode_post(client):
    """Test case for dispatcher_qrcode_post

    Arbitrary data type QR Code
    """
    body = {"output":"","image":"","data":"https://linqr.app","size":"","style":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Byvalue': 'special-key',
        'RapidAPI': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/qrcode',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_dispatcher_qrcode_sms_post(client):
    """Test case for dispatcher_qrcode_sms_post

    SMS QR Code
    """
    body = {"output":"","image":"","data":"","size":"","style":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Byvalue': 'special-key',
        'RapidAPI': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/qrcode/sms',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_dispatcher_qrcode_text_post(client):
    """Test case for dispatcher_qrcode_text_post

    Text QR Code
    """
    body = {"output":"","image":"","data":"","size":"","style":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Byvalue': 'special-key',
        'RapidAPI': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/qrcode/text',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_dispatcher_qrcode_wifi_post(client):
    """Test case for dispatcher_qrcode_wifi_post

    WiFi QR Code
    """
    body = {"output":"","image":"","data":"","size":"","style":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Byvalue': 'special-key',
        'RapidAPI': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/qrcode/wifi',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

