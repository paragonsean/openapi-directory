# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.logo import Logo
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.terminal_settings import TerminalSettings


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_stores_reference_terminal_logos(client):
    """Test case for get_merchants_merchant_id_stores_reference_terminal_logos

    Get the terminal logo
    """
    params = [('model', 'model_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/stores/{reference}/terminalLogos'.format(merchant_id='merchant_id_example', reference='reference_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_stores_reference_terminal_settings(client):
    """Test case for get_merchants_merchant_id_stores_reference_terminal_settings

    Get terminal settings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/stores/{reference}/terminalSettings'.format(merchant_id='merchant_id_example', reference='reference_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stores_store_id_terminal_logos(client):
    """Test case for get_stores_store_id_terminal_logos

    Get the terminal logo
    """
    params = [('model', 'model_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/stores/{store_id}/terminalLogos'.format(store_id='store_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stores_store_id_terminal_settings(client):
    """Test case for get_stores_store_id_terminal_settings

    Get terminal settings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/stores/{store_id}/terminalSettings'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_merchants_merchant_id_stores_reference_terminal_logos(client):
    """Test case for patch_merchants_merchant_id_stores_reference_terminal_logos

    Update the terminal logo
    """
    body = {"data":"data"}
    params = [('model', 'model_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/merchants/{merchant_id}/stores/{reference}/terminalLogos'.format(merchant_id='merchant_id_example', reference='reference_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_merchants_merchant_id_stores_reference_terminal_settings(client):
    """Test case for patch_merchants_merchant_id_stores_reference_terminal_settings

    Update terminal settings
    """
    body = {"localization":{"timezone":"timezone","language":"language","secondaryLanguage":"secondaryLanguage"},"surcharge":{"configurations":[{"country":["country","country"],"sources":["sources","sources"],"brand":"brand","currencies":[{"amount":7,"percentage":9.301444243932576,"currencyCode":"currencyCode"},{"amount":7,"percentage":9.301444243932576,"currencyCode":"currencyCode"}]},{"country":["country","country"],"sources":["sources","sources"],"brand":"brand","currencies":[{"amount":7,"percentage":9.301444243932576,"currencyCode":"currencyCode"},{"amount":7,"percentage":9.301444243932576,"currencyCode":"currencyCode"}]}],"askConfirmation":True},"payAtTable":{"enablePayAtTable":True,"authenticationMethod":"MAGSWIPE","paymentInstrument":"Cash"},"signature":{"skipSignature":True,"deviceSlogan":"deviceSlogan","deviceName":"deviceName","askSignatureOnScreen":True},"passcodes":{"refundPin":"refundPin","screenLockPin":"screenLockPin","adminMenuPin":"adminMenuPin","txMenuPin":"txMenuPin"},"cardholderReceipt":{"headerForAuthorizedReceipt":"headerForAuthorizedReceipt"},"standalone":{"enableStandalone":True,"currencyCode":"currencyCode"},"timeouts":{"fromActiveToSleep":3},"opi":{"enablePayAtTable":True,"payAtTableURL":"payAtTableURL","payAtTableStoreNumber":"payAtTableStoreNumber"},"wifiProfiles":{"settings":{"roaming":True,"band":"band","timeout":4},"profiles":[{"bssType":"bssType","eapCaCert":{"data":"data","name":"name"},"autoWifi":True,"channel":2,"psk":"psk","defaultProfile":True,"eapClientCert":{"data":"data","name":"name"},"eapClientPwd":"eapClientPwd","eapPwd":"eapPwd","ssid":"ssid","wsec":"wsec","eapClientKey":{"data":"data","name":"name"},"eapIdentity":"eapIdentity","eap":"eap","name":"name","eapIntermediateCert":{"data":"data","name":"name"},"authType":"authType","hiddenSsid":True},{"bssType":"bssType","eapCaCert":{"data":"data","name":"name"},"autoWifi":True,"channel":2,"psk":"psk","defaultProfile":True,"eapClientCert":{"data":"data","name":"name"},"eapClientPwd":"eapClientPwd","eapPwd":"eapPwd","ssid":"ssid","wsec":"wsec","eapClientKey":{"data":"data","name":"name"},"eapIdentity":"eapIdentity","eap":"eap","name":"name","eapIntermediateCert":{"data":"data","name":"name"},"authType":"authType","hiddenSsid":True}]},"refunds":{"referenced":{"enableStandaloneRefunds":True}},"terminalInstructions":{"adyenAppRestart":True},"receiptPrinting":{"merchantApproved":True,"merchantCancelled":True,"shopperCancelled":True,"shopperCaptureRefused":True,"merchantCaptureRefused":True,"merchantRefundRefused":True,"shopperRefused":True,"shopperApproved":True,"shopperCaptureApproved":True,"merchantRefused":True,"shopperRefundApproved":True,"shopperRefundRefused":True,"merchantRefundApproved":True,"merchantVoid":True,"merchantCaptureApproved":True,"shopperVoid":True},"connectivity":{"simcardStatus":"ACTIVATED"},"gratuities":[{"predefinedTipEntries":["predefinedTipEntries","predefinedTipEntries"],"allowCustomAmount":True,"usePredefinedTipEntries":True,"currency":"currency"},{"predefinedTipEntries":["predefinedTipEntries","predefinedTipEntries"],"allowCustomAmount":True,"usePredefinedTipEntries":True,"currency":"currency"}],"offlineProcessing":{"chipFloorLimit":5,"offlineSwipeLimits":[{"amount":2,"currencyCode":"currencyCode"},{"amount":2,"currencyCode":"currencyCode"}]},"payment":{"contactlessCurrency":"contactlessCurrency","hideMinorUnitsInCurrencies":["hideMinorUnitsInCurrencies","hideMinorUnitsInCurrencies"]},"receiptOptions":{"promptBeforePrinting":True,"qrCodeData":"qrCodeData","logo":"logo"},"tapToPay":{"merchantDisplayName":"merchantDisplayName"},"nexo":{"nexoEventUrls":["nexoEventUrls","nexoEventUrls"],"eventUrls":{"eventLocalUrls":[{"password":"password","encrypted":True,"url":"url","username":"username"},{"password":"password","encrypted":True,"url":"url","username":"username"}],"eventPublicUrls":[{"password":"password","encrypted":True,"url":"url","username":"username"},{"password":"password","encrypted":True,"url":"url","username":"username"}]},"notification":{"showButton":True,"details":"details","category":"SaleWakeUp","title":"title","enabled":True},"displayUrls":{"localUrls":[{"password":"password","encrypted":True,"url":"url","username":"username"},{"password":"password","encrypted":True,"url":"url","username":"username"}],"publicUrls":[{"password":"password","encrypted":True,"url":"url","username":"username"},{"password":"password","encrypted":True,"url":"url","username":"username"}]},"encryptionKey":{"identifier":"identifier","passphrase":"passphrase","version":5}},"hardware":{"restartHour":1,"resetTotalsHour":6,"displayMaximumBackLight":0}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/merchants/{merchant_id}/stores/{reference}/terminalSettings'.format(merchant_id='merchant_id_example', reference='reference_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_stores_store_id_terminal_logos(client):
    """Test case for patch_stores_store_id_terminal_logos

    Update the terminal logo
    """
    body = {"data":"data"}
    params = [('model', 'model_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/stores/{store_id}/terminalLogos'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_stores_store_id_terminal_settings(client):
    """Test case for patch_stores_store_id_terminal_settings

    Update terminal settings
    """
    body = {"localization":{"timezone":"timezone","language":"language","secondaryLanguage":"secondaryLanguage"},"surcharge":{"configurations":[{"country":["country","country"],"sources":["sources","sources"],"brand":"brand","currencies":[{"amount":7,"percentage":9.301444243932576,"currencyCode":"currencyCode"},{"amount":7,"percentage":9.301444243932576,"currencyCode":"currencyCode"}]},{"country":["country","country"],"sources":["sources","sources"],"brand":"brand","currencies":[{"amount":7,"percentage":9.301444243932576,"currencyCode":"currencyCode"},{"amount":7,"percentage":9.301444243932576,"currencyCode":"currencyCode"}]}],"askConfirmation":True},"payAtTable":{"enablePayAtTable":True,"authenticationMethod":"MAGSWIPE","paymentInstrument":"Cash"},"signature":{"skipSignature":True,"deviceSlogan":"deviceSlogan","deviceName":"deviceName","askSignatureOnScreen":True},"passcodes":{"refundPin":"refundPin","screenLockPin":"screenLockPin","adminMenuPin":"adminMenuPin","txMenuPin":"txMenuPin"},"cardholderReceipt":{"headerForAuthorizedReceipt":"headerForAuthorizedReceipt"},"standalone":{"enableStandalone":True,"currencyCode":"currencyCode"},"timeouts":{"fromActiveToSleep":3},"opi":{"enablePayAtTable":True,"payAtTableURL":"payAtTableURL","payAtTableStoreNumber":"payAtTableStoreNumber"},"wifiProfiles":{"settings":{"roaming":True,"band":"band","timeout":4},"profiles":[{"bssType":"bssType","eapCaCert":{"data":"data","name":"name"},"autoWifi":True,"channel":2,"psk":"psk","defaultProfile":True,"eapClientCert":{"data":"data","name":"name"},"eapClientPwd":"eapClientPwd","eapPwd":"eapPwd","ssid":"ssid","wsec":"wsec","eapClientKey":{"data":"data","name":"name"},"eapIdentity":"eapIdentity","eap":"eap","name":"name","eapIntermediateCert":{"data":"data","name":"name"},"authType":"authType","hiddenSsid":True},{"bssType":"bssType","eapCaCert":{"data":"data","name":"name"},"autoWifi":True,"channel":2,"psk":"psk","defaultProfile":True,"eapClientCert":{"data":"data","name":"name"},"eapClientPwd":"eapClientPwd","eapPwd":"eapPwd","ssid":"ssid","wsec":"wsec","eapClientKey":{"data":"data","name":"name"},"eapIdentity":"eapIdentity","eap":"eap","name":"name","eapIntermediateCert":{"data":"data","name":"name"},"authType":"authType","hiddenSsid":True}]},"refunds":{"referenced":{"enableStandaloneRefunds":True}},"terminalInstructions":{"adyenAppRestart":True},"receiptPrinting":{"merchantApproved":True,"merchantCancelled":True,"shopperCancelled":True,"shopperCaptureRefused":True,"merchantCaptureRefused":True,"merchantRefundRefused":True,"shopperRefused":True,"shopperApproved":True,"shopperCaptureApproved":True,"merchantRefused":True,"shopperRefundApproved":True,"shopperRefundRefused":True,"merchantRefundApproved":True,"merchantVoid":True,"merchantCaptureApproved":True,"shopperVoid":True},"connectivity":{"simcardStatus":"ACTIVATED"},"gratuities":[{"predefinedTipEntries":["predefinedTipEntries","predefinedTipEntries"],"allowCustomAmount":True,"usePredefinedTipEntries":True,"currency":"currency"},{"predefinedTipEntries":["predefinedTipEntries","predefinedTipEntries"],"allowCustomAmount":True,"usePredefinedTipEntries":True,"currency":"currency"}],"offlineProcessing":{"chipFloorLimit":5,"offlineSwipeLimits":[{"amount":2,"currencyCode":"currencyCode"},{"amount":2,"currencyCode":"currencyCode"}]},"payment":{"contactlessCurrency":"contactlessCurrency","hideMinorUnitsInCurrencies":["hideMinorUnitsInCurrencies","hideMinorUnitsInCurrencies"]},"receiptOptions":{"promptBeforePrinting":True,"qrCodeData":"qrCodeData","logo":"logo"},"tapToPay":{"merchantDisplayName":"merchantDisplayName"},"nexo":{"nexoEventUrls":["nexoEventUrls","nexoEventUrls"],"eventUrls":{"eventLocalUrls":[{"password":"password","encrypted":True,"url":"url","username":"username"},{"password":"password","encrypted":True,"url":"url","username":"username"}],"eventPublicUrls":[{"password":"password","encrypted":True,"url":"url","username":"username"},{"password":"password","encrypted":True,"url":"url","username":"username"}]},"notification":{"showButton":True,"details":"details","category":"SaleWakeUp","title":"title","enabled":True},"displayUrls":{"localUrls":[{"password":"password","encrypted":True,"url":"url","username":"username"},{"password":"password","encrypted":True,"url":"url","username":"username"}],"publicUrls":[{"password":"password","encrypted":True,"url":"url","username":"username"},{"password":"password","encrypted":True,"url":"url","username":"username"}]},"encryptionKey":{"identifier":"identifier","passphrase":"passphrase","version":5}},"hardware":{"restartHour":1,"resetTotalsHour":6,"displayMaximumBackLight":0}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/stores/{store_id}/terminalSettings'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

