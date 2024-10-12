# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authorisations import Authorisations
from openapi_server.models.error400_ngpis import Error400NGPIS
from openapi_server.models.error400_pis import Error400PIS
from openapi_server.models.error401_ngpis import Error401NGPIS
from openapi_server.models.error401_pis import Error401PIS
from openapi_server.models.error403_ngpis import Error403NGPIS
from openapi_server.models.error403_pis import Error403PIS
from openapi_server.models.error404_ngpis import Error404NGPIS
from openapi_server.models.error404_pis import Error404PIS
from openapi_server.models.error405_ngpis import Error405NGPIS
from openapi_server.models.error405_ngpiscanc import Error405NGPISCANC
from openapi_server.models.error405_pis import Error405PIS
from openapi_server.models.error405_piscanc import Error405PISCANC
from openapi_server.models.error409_ngpis import Error409NGPIS
from openapi_server.models.error409_pis import Error409PIS
from openapi_server.models.get_payment_information200_response import GetPaymentInformation200Response
from openapi_server.models.initiate_payment_request import InitiatePaymentRequest
from openapi_server.models.initiate_payment_request1 import InitiatePaymentRequest1
from openapi_server.models.payment_initation_request_response201 import PaymentInitationRequestResponse201
from openapi_server.models.payment_initiation_cancel_response202 import PaymentInitiationCancelResponse202
from openapi_server.models.payment_initiation_status_response200_json import PaymentInitiationStatusResponse200Json
from openapi_server.models.periodic_payment_initiation_multipart_body import PeriodicPaymentInitiationMultipartBody
from openapi_server.models.sca_status_response import ScaStatusResponse
from openapi_server.models.start_consent_authorisation_request import StartConsentAuthorisationRequest
from openapi_server.models.start_scaprocess_response import StartScaprocessResponse
from openapi_server.models.update_consents_psu_data200_response import UpdateConsentsPsuData200Response
from openapi_server.models.update_consents_psu_data_request import UpdateConsentsPsuDataRequest


pytestmark = pytest.mark.asyncio

async def test_cancel_payment(client):
    """Test case for cancel_payment

    Payment cancellation request
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'tpp_redirect_preferred': True,
        'tpp_nok_redirect_uri': 'tpp_nok_redirect_uri_example',
        'tpp_redirect_uri': 'tpp_redirect_uri_example',
        'tpp_explicit_authorisation_preferred': True,
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{payment_service}/{payment_product}/{payment_id}'.format(payment_service='payment_service_example', payment_product='payment_product_example', payment_id='payment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_cancellation_sca_status(client):
    """Test case for get_payment_cancellation_sca_status

    Read the SCA status of the payment cancellation's authorisation
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{payment_service}/{payment_product}/{payment_id}/cancellation-authorisations/{authorisation_id}'.format(payment_service='payment_service_example', payment_product='payment_product_example', payment_id='payment_id_example', authorisation_id='authorisation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_information(client):
    """Test case for get_payment_information

    Get payment information
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{payment_service}/{payment_product}/{payment_id}'.format(payment_service='payment_service_example', payment_product='payment_product_example', payment_id='payment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_initiation_authorisation(client):
    """Test case for get_payment_initiation_authorisation

    Get payment initiation authorisation sub-resources request
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{payment_service}/{payment_product}/{payment_id}/authorisations'.format(payment_service='payment_service_example', payment_product='payment_product_example', payment_id='payment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_initiation_cancellation_authorisation_information(client):
    """Test case for get_payment_initiation_cancellation_authorisation_information

    Will deliver an array of resource identifications to all generated cancellation authorisation sub-resources
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{payment_service}/{payment_product}/{payment_id}/cancellation-authorisations'.format(payment_service='payment_service_example', payment_product='payment_product_example', payment_id='payment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_initiation_sca_status(client):
    """Test case for get_payment_initiation_sca_status

    Read the SCA status of the payment authorisation
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{payment_service}/{payment_product}/{payment_id}/authorisations/{authorisation_id}'.format(payment_service='payment_service_example', payment_product='payment_product_example', payment_id='payment_id_example', authorisation_id='authorisation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_initiation_status(client):
    """Test case for get_payment_initiation_status

    Payment initiation status request
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{payment_service}/{payment_product}/{payment_id}/status'.format(payment_service='payment_service_example', payment_product='payment_product_example', payment_id='payment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_initiate_payment(client):
    """Test case for initiate_payment

    Payment initiation request
    """
    body = openapi_server.InitiatePaymentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_id': 'PSU-1234',
        'psu_id_type': 'psu_id_type_example',
        'psu_corporate_id': 'psu_corporate_id_example',
        'psu_corporate_id_type': 'psu_corporate_id_type_example',
        'consent_id': 'consent_id_example',
        'psu_ip_address': '192.168.8.78',
        'tpp_redirect_preferred': True,
        'tpp_redirect_uri': 'tpp_redirect_uri_example',
        'tpp_nok_redirect_uri': 'tpp_nok_redirect_uri_example',
        'tpp_explicit_authorisation_preferred': True,
        'tpp_rejection_no_funds_preferred': True,
        'tpp_brand_logging_information': 'tpp_brand_logging_information_example',
        'tpp_notification_uri': 'tpp_notification_uri_example',
        'tpp_notification_content_preferred': 'tpp_notification_content_preferred_example',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{payment_service}/{payment_product}'.format(payment_service='payment_service_example', payment_product='payment_product_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_payment_authorisation(client):
    """Test case for start_payment_authorisation

    Start the authorisation process for a payment initiation
    """
    body = openapi_server.StartConsentAuthorisationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'psu_id': 'PSU-1234',
        'psu_id_type': 'psu_id_type_example',
        'psu_corporate_id': 'psu_corporate_id_example',
        'psu_corporate_id_type': 'psu_corporate_id_type_example',
        'tpp_redirect_preferred': True,
        'tpp_redirect_uri': 'tpp_redirect_uri_example',
        'tpp_nok_redirect_uri': 'tpp_nok_redirect_uri_example',
        'tpp_notification_uri': 'tpp_notification_uri_example',
        'tpp_notification_content_preferred': 'tpp_notification_content_preferred_example',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{payment_service}/{payment_product}/{payment_id}/authorisations'.format(payment_service='payment_service_example', payment_product='payment_product_example', payment_id='payment_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_payment_initiation_cancellation_authorisation(client):
    """Test case for start_payment_initiation_cancellation_authorisation

    Start the authorisation process for the cancellation of the addressed payment
    """
    body = openapi_server.StartConsentAuthorisationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_id': 'PSU-1234',
        'psu_id_type': 'psu_id_type_example',
        'psu_corporate_id': 'psu_corporate_id_example',
        'psu_corporate_id_type': 'psu_corporate_id_type_example',
        'tpp_redirect_preferred': True,
        'tpp_redirect_uri': 'tpp_redirect_uri_example',
        'tpp_nok_redirect_uri': 'tpp_nok_redirect_uri_example',
        'tpp_notification_uri': 'tpp_notification_uri_example',
        'tpp_notification_content_preferred': 'tpp_notification_content_preferred_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{payment_service}/{payment_product}/{payment_id}/cancellation-authorisations'.format(payment_service='payment_service_example', payment_product='payment_product_example', payment_id='payment_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_payment_cancellation_psu_data(client):
    """Test case for update_payment_cancellation_psu_data

    Update PSU data for payment initiation cancellation
    """
    body = openapi_server.UpdateConsentsPsuDataRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_id': 'PSU-1234',
        'psu_id_type': 'psu_id_type_example',
        'psu_corporate_id': 'psu_corporate_id_example',
        'psu_corporate_id_type': 'psu_corporate_id_type_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/{payment_service}/{payment_product}/{payment_id}/cancellation-authorisations/{authorisation_id}'.format(payment_service='payment_service_example', payment_product='payment_product_example', payment_id='payment_id_example', authorisation_id='authorisation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_payment_psu_data(client):
    """Test case for update_payment_psu_data

    Update PSU data for payment initiation
    """
    body = openapi_server.UpdateConsentsPsuDataRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_id': 'PSU-1234',
        'psu_id_type': 'psu_id_type_example',
        'psu_corporate_id': 'psu_corporate_id_example',
        'psu_corporate_id_type': 'psu_corporate_id_type_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/{payment_service}/{payment_product}/{payment_id}/authorisations/{authorisation_id}'.format(payment_service='payment_service_example', payment_product='payment_product_example', payment_id='payment_id_example', authorisation_id='authorisation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

