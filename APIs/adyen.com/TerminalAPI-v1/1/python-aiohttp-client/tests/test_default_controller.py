# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.admin_request import AdminRequest
from openapi_server.models.admin_response import AdminResponse
from openapi_server.models.balance_inquiry_request import BalanceInquiryRequest
from openapi_server.models.balance_inquiry_response import BalanceInquiryResponse
from openapi_server.models.card_acquisition_request import CardAcquisitionRequest
from openapi_server.models.card_acquisition_response import CardAcquisitionResponse
from openapi_server.models.card_reader_apdu_request import CardReaderAPDURequest
from openapi_server.models.card_reader_apdu_response import CardReaderAPDUResponse
from openapi_server.models.diagnosis_request import DiagnosisRequest
from openapi_server.models.diagnosis_response import DiagnosisResponse
from openapi_server.models.display_request import DisplayRequest
from openapi_server.models.display_response import DisplayResponse
from openapi_server.models.enable_service_request import EnableServiceRequest
from openapi_server.models.enable_service_response import EnableServiceResponse
from openapi_server.models.get_totals_request import GetTotalsRequest
from openapi_server.models.get_totals_response import GetTotalsResponse
from openapi_server.models.input_request import InputRequest
from openapi_server.models.input_response import InputResponse
from openapi_server.models.login_request import LoginRequest
from openapi_server.models.login_response import LoginResponse
from openapi_server.models.logout_request import LogoutRequest
from openapi_server.models.logout_response import LogoutResponse
from openapi_server.models.loyalty_request import LoyaltyRequest
from openapi_server.models.loyalty_response import LoyaltyResponse
from openapi_server.models.payment_request import PaymentRequest
from openapi_server.models.payment_response import PaymentResponse
from openapi_server.models.print_request import PrintRequest
from openapi_server.models.print_response import PrintResponse
from openapi_server.models.reconciliation_request import ReconciliationRequest
from openapi_server.models.reconciliation_response import ReconciliationResponse
from openapi_server.models.reversal_request import ReversalRequest
from openapi_server.models.reversal_response import ReversalResponse
from openapi_server.models.stored_value_request import StoredValueRequest
from openapi_server.models.stored_value_response import StoredValueResponse
from openapi_server.models.transaction_status_request import TransactionStatusRequest
from openapi_server.models.transaction_status_response import TransactionStatusResponse


pytestmark = pytest.mark.asyncio

async def test_admin_post(client):
    """Test case for admin_post

    Admin Request
    """
    body = {"ServiceIdentification":"ServiceIdentification"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/admin',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_balanceinquiry_post(client):
    """Test case for balanceinquiry_post

    BalanceInquiry Request
    """
    body = {"PaymentAccountReq":{"PaymentInstrumentData":{"StoredValueAccountID":{"ExpiryDate":4,"OwnerName":"OwnerName","EntryMode":["Contactless","Contactless"],"StoredValueProvider":"StoredValueProvider","StoredValueID":"StoredValueID","StoredValueAccountType":"GiftCard"},"MobileData":{"Geolocation":{"UTMCoordinates":{"UTMNorthward":"UTMNorthward","UTMEastward":"UTMEastward","UTMZone":"UTMZone"},"GeographicCoordinates":{"Latitude":"Latitude","Longitude":"Longitude"}},"MaskedMSISDN":1,"MobileCountryCode":3,"MobileNetworkCode":2,"SensitiveMobileData":{"MSISDN":4,"ISMI":1,"IMEI":7},"ProtectedMobileData":"ProtectedMobileData"},"ProtectedCardData":"ProtectedCardData","PaymentInstrumentType":"Card","CheckData":{"TypeCode":"Company","Country":"Country","CheckCardNumber":"CheckCardNumber","CheckNumber":"CheckNumber","BankID":"BankID","AccountNumber":"AccountNumber","TrackData":{"TrackFormat":"AAMVA","TrackNumb":1,"TrackValue":"TrackValue"}},"CardData":{"CardCountryCode":3,"SensitiveCardData":{"CardSeqNumb":2,"ExpiryDate":4,"PAN":22,"TrackData":[{"TrackFormat":"AAMVA","TrackNumb":1,"TrackValue":"TrackValue"},{"TrackFormat":"AAMVA","TrackNumb":1,"TrackValue":"TrackValue"}]},"PaymentBrand":"PaymentBrand","ProtectedCardData":"ProtectedCardData","AllowedProduct":[{"ProductCode":11,"AdditionalProductInfo":"AdditionalProductInfo","ProductLabel":"ProductLabel","EanUpc":5},{"ProductCode":11,"AdditionalProductInfo":"AdditionalProductInfo","ProductLabel":"ProductLabel","EanUpc":5}],"CustomerOrder":[{"AdditionalInformation":"AdditionalInformation","OpenOrderState":True,"StartDate":"2000-01-23T04:56:07.000+00:00","SaleReferenceID":"SaleReferenceID","CustomerOrderID":"CustomerOrderID","Currency":"Currency","ForecastedAmount":3.6160767492518745E7,"CurrentAmount":9.301444243932483E7,"AccessedBy":"AccessedBy","EndDate":"2000-01-23T04:56:07.000+00:00"},{"AdditionalInformation":"AdditionalInformation","OpenOrderState":True,"StartDate":"2000-01-23T04:56:07.000+00:00","SaleReferenceID":"SaleReferenceID","CustomerOrderID":"CustomerOrderID","Currency":"Currency","ForecastedAmount":3.6160767492518745E7,"CurrentAmount":9.301444243932483E7,"AccessedBy":"AccessedBy","EndDate":"2000-01-23T04:56:07.000+00:00"}],"EntryMode":["Contactless","Contactless"],"PaymentAccountRef":"PaymentAccountRef","MaskedPan":"MaskedPan","PaymentToken":{"ExpiryDateTime":"2000-01-23T04:56:07.000+00:00","TokenRequestedType":"Customer","TokenValue":"TokenValue"},"AllowedProductCode":[5,5]}},"AccountType":"CardTotals","CardAcquisitionReference":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"}},"LoyaltyAccountReq":{"LoyaltyAccountID":{"LoyaltyID":"LoyaltyID","IdentificationSupport":"HybridCard","EntryMode":["Contactless","Contactless"],"IdentificationType":"AccountNumber"},"CardAcquisitionReference":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/balanceinquiry',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cardacquisition_post(client):
    """Test case for cardacquisition_post

    CardAcquisition Request
    """
    body = {"CardAcquisitionTransaction":{"ForceCustomerSelectionFlag":True,"CashBackFlag":True,"PaymentType":"CashAdvance","AllowedLoyaltyBrand":["AllowedLoyaltyBrand","AllowedLoyaltyBrand"],"LoyaltyHandling":"Allowed","TotalAmount":8008281.904610035,"CustomerLanguage":"CustomerLanguage","ForceEntryMode":["CheckReader","CheckReader"],"AllowedPaymentBrand":["AllowedPaymentBrand","AllowedPaymentBrand"]},"SaleData":{"SaleToAcquirerData":"SaleToAcquirerData","SaleToIssuerData":{"StatementReference":"StatementReference"},"SaleTransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"},"SaleReferenceID":"SaleReferenceID","SaleTerminalData":{"TotalsGroupID":"TotalsGroupID"},"CustomerOrderID":"CustomerOrderID","CustomerOrderReq":["Both","Both"],"OperatorLanguage":"OperatorLanguage","TokenRequestedType":"Customer","OperatorID":"OperatorID","ShiftNumber":"ShiftNumber","SaleToPOIData":"SaleToPOIData"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/cardacquisition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cardreaderapdu_post(client):
    """Test case for cardreaderapdu_post

    CardReaderAPDU Request
    """
    body = {"APDUClass":"APDUClass","APDUData":"APDUData","APDUPar1":"APDUPar1","APDUPar2":"APDUPar2","APDUExpectedLength":"APDUExpectedLength","APDUInstruction":"APDUInstruction"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/cardreaderapdu',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnosis_post(client):
    """Test case for diagnosis_post

    Diagnosis Request
    """
    body = {"POIID":"POIID","AcquirerID":[0,0],"HostDiagnosisFlag":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/diagnosis',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_display_post(client):
    """Test case for display_post

    Display Request
    """
    body = {"DisplayOutput":[{"OutputSignature":"OutputSignature","MenuEntry":[{"DefaultSelectedFlag":False,"OutputFormat":"BarCode","MenuEntryTag":"NonSelectable","OutputText":[{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468},{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468}],"PredefinedContent":{"Language":"Language","ReferenceID":"ReferenceID"},"OutputXHTML":"OutputXHTML"},{"DefaultSelectedFlag":False,"OutputFormat":"BarCode","MenuEntryTag":"NonSelectable","OutputText":[{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468},{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468}],"PredefinedContent":{"Language":"Language","ReferenceID":"ReferenceID"},"OutputXHTML":"OutputXHTML"}],"MinimumDisplayTime":80,"Device":"CashierDisplay","OutputContent":{"OutputBarcode":{"BarcodeValue":"BarcodeValue","BarcodeType":"Code128"},"OutputFormat":"BarCode","OutputText":[{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468},{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468}],"PredefinedContent":{"Language":"Language","ReferenceID":"ReferenceID"},"OutputXHTML":"OutputXHTML"},"InfoQualify":"CustomerAssistance","ResponseRequiredFlag":True},{"OutputSignature":"OutputSignature","MenuEntry":[{"DefaultSelectedFlag":False,"OutputFormat":"BarCode","MenuEntryTag":"NonSelectable","OutputText":[{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468},{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468}],"PredefinedContent":{"Language":"Language","ReferenceID":"ReferenceID"},"OutputXHTML":"OutputXHTML"},{"DefaultSelectedFlag":False,"OutputFormat":"BarCode","MenuEntryTag":"NonSelectable","OutputText":[{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468},{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468}],"PredefinedContent":{"Language":"Language","ReferenceID":"ReferenceID"},"OutputXHTML":"OutputXHTML"}],"MinimumDisplayTime":80,"Device":"CashierDisplay","OutputContent":{"OutputBarcode":{"BarcodeValue":"BarcodeValue","BarcodeType":"Code128"},"OutputFormat":"BarCode","OutputText":[{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468},{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468}],"PredefinedContent":{"Language":"Language","ReferenceID":"ReferenceID"},"OutputXHTML":"OutputXHTML"},"InfoQualify":"CustomerAssistance","ResponseRequiredFlag":True}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/display',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enableservice_post(client):
    """Test case for enableservice_post

    EnableService Request
    """
    body = {"ServicesEnabled":["CardAcquisition","CardAcquisition"],"DisplayOutput":{"OutputSignature":"OutputSignature","MenuEntry":[{"DefaultSelectedFlag":False,"OutputFormat":"BarCode","MenuEntryTag":"NonSelectable","OutputText":[{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468},{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468}],"PredefinedContent":{"Language":"Language","ReferenceID":"ReferenceID"},"OutputXHTML":"OutputXHTML"},{"DefaultSelectedFlag":False,"OutputFormat":"BarCode","MenuEntryTag":"NonSelectable","OutputText":[{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468},{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468}],"PredefinedContent":{"Language":"Language","ReferenceID":"ReferenceID"},"OutputXHTML":"OutputXHTML"}],"MinimumDisplayTime":80,"Device":"CashierDisplay","OutputContent":{"OutputBarcode":{"BarcodeValue":"BarcodeValue","BarcodeType":"Code128"},"OutputFormat":"BarCode","OutputText":[{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468},{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468}],"PredefinedContent":{"Language":"Language","ReferenceID":"ReferenceID"},"OutputXHTML":"OutputXHTML"},"InfoQualify":"CustomerAssistance","ResponseRequiredFlag":True},"TransactionAction":"AbortTransaction"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/enableservice',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gettotals_post(client):
    """Test case for gettotals_post

    GetTotals Request
    """
    body = {"TotalDetails":["OperatorID","OperatorID"],"TotalFilter":{"POIID":"POIID","SaleID":"SaleID","OperatorID":"OperatorID","ShiftNumber":"ShiftNumber","TotalsGroupID":"TotalsGroupID"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/gettotals',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_input_post(client):
    """Test case for input_post

    Input Request
    """
    body = {"DisplayOutput":{"OutputSignature":"OutputSignature","MenuEntry":[{"DefaultSelectedFlag":False,"OutputFormat":"BarCode","MenuEntryTag":"NonSelectable","OutputText":[{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468},{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468}],"PredefinedContent":{"Language":"Language","ReferenceID":"ReferenceID"},"OutputXHTML":"OutputXHTML"},{"DefaultSelectedFlag":False,"OutputFormat":"BarCode","MenuEntryTag":"NonSelectable","OutputText":[{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468},{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468}],"PredefinedContent":{"Language":"Language","ReferenceID":"ReferenceID"},"OutputXHTML":"OutputXHTML"}],"MinimumDisplayTime":80,"Device":"CashierDisplay","OutputContent":{"OutputBarcode":{"BarcodeValue":"BarcodeValue","BarcodeType":"Code128"},"OutputFormat":"BarCode","OutputText":[{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468},{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468}],"PredefinedContent":{"Language":"Language","ReferenceID":"ReferenceID"},"OutputXHTML":"OutputXHTML"},"InfoQualify":"CustomerAssistance","ResponseRequiredFlag":True},"InputData":{"MaxInputTime":6,"MaxDecimalLength":0,"DefaultLayoutString":"DefaultLayoutString","Device":"CashierDisplay","MinLength":5,"InfoQualify":"CustomerAssistance","MaskCharactersFlag":False,"MaxLength":1,"ImmediateResponseFlag":False,"DefaultInputString":"DefaultInputString","MenuBackFlag":False,"DisableCancelFlag":False,"WaitUserValidationFlag":True,"StringMask":"StringMask","BeepKeyFlag":False,"NotifyCardInputFlag":False,"DisableValidFlag":False,"FromRightToLeftFlag":False,"InputCommand":"DecimalString","DisableCorrectFlag":False,"GlobalCorrectionFlag":False}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/input',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_login_post(client):
    """Test case for login_post

    Login Request
    """
    body = {"SaleTerminalData":{"TotalsGroupID":"TotalsGroupID"},"CustomerOrderReq":["Both","Both"],"OperatorLanguage":"OperatorLanguage","TokenRequestedType":"Customer","SaleSoftware":{"ApplicationName":"ApplicationName","SoftwareVersion":"SoftwareVersion","ManufacturerID":"ManufacturerID","CertificationCode":"CertificationCode"},"OperatorID":"OperatorID","DateTime":"2000-01-23T04:56:07.000+00:00","POISerialNumber":"POISerialNumber","ShiftNumber":"ShiftNumber","TrainingModeFlag":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logout_post(client):
    """Test case for logout_post

    Logout Request
    """
    body = {"MaintenanceAllowed":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/logout',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_loyalty_post(client):
    """Test case for loyalty_post

    Loyalty Request
    """
    body = {"LoyaltyData":{"LoyaltyAccountID":{"LoyaltyID":"LoyaltyID","IdentificationSupport":"HybridCard","EntryMode":["Contactless","Contactless"],"IdentificationType":"AccountNumber"},"CardAcquisitionReference":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"},"LoyaltyAmount":{"LoyaltyUnit":"Monetary","Currency":"Currency","AmountValue":6.027456183070343E7}},"LoyaltyTransaction":{"SaleItem":[{"UnitPrice":3.6160767492518745E7,"TaxCode":9,"UnitOfMeasure":"Case","ProductCode":5,"AdditionalProductInfo":"AdditionalProductInfo","Quantity":"Quantity","ProductLabel":"ProductLabel","ItemAmount":5.9621339166831225E7,"ItemID":5,"EanUpc":1,"SaleChannel":7},{"UnitPrice":3.6160767492518745E7,"TaxCode":9,"UnitOfMeasure":"Case","ProductCode":5,"AdditionalProductInfo":"AdditionalProductInfo","Quantity":"Quantity","ProductLabel":"ProductLabel","ItemAmount":5.9621339166831225E7,"ItemID":5,"EanUpc":1,"SaleChannel":7}],"LoyaltyTransactionType":"Award","Currency":"Currency","TransactionConditions":{"MerchantCategoryCode":"MerchantCategoryCode","AcquirerID":[4,4],"AllowedLoyaltyBrand":["AllowedLoyaltyBrand","AllowedLoyaltyBrand"],"LoyaltyHandling":"Allowed","DebitPreferredFlag":True,"CustomerLanguage":"CustomerLanguage","ForceEntryMode":["CheckReader","CheckReader"],"AllowedPaymentBrand":["AllowedPaymentBrand","AllowedPaymentBrand"],"ForceOnlineFlag":False},"TotalAmount":2.0271230230023015E7,"OriginalPOITransaction":{"ReuseCardDataFlag":True,"POIID":"POIID","SaleID":"SaleID","AcquirerID":0,"AmountValue":6.027456183070343E7,"CustomerLanguage":"CustomerLanguage","HostTransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"},"ApprovalCode":"ApprovalCode","POITransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"}}},"SaleData":{"SaleToAcquirerData":"SaleToAcquirerData","SaleToIssuerData":{"StatementReference":"StatementReference"},"SaleTransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"},"SaleReferenceID":"SaleReferenceID","SaleTerminalData":{"TotalsGroupID":"TotalsGroupID"},"CustomerOrderID":"CustomerOrderID","CustomerOrderReq":["Both","Both"],"OperatorLanguage":"OperatorLanguage","TokenRequestedType":"Customer","OperatorID":"OperatorID","ShiftNumber":"ShiftNumber","SaleToPOIData":"SaleToPOIData"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/loyalty',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_post(client):
    """Test case for payment_post

    Payment Request
    """
    body = {"PaymentTransaction":{"SaleItem":[{"UnitPrice":3.6160767492518745E7,"TaxCode":9,"UnitOfMeasure":"Case","ProductCode":5,"AdditionalProductInfo":"AdditionalProductInfo","Quantity":"Quantity","ProductLabel":"ProductLabel","ItemAmount":5.9621339166831225E7,"ItemID":5,"EanUpc":1,"SaleChannel":7},{"UnitPrice":3.6160767492518745E7,"TaxCode":9,"UnitOfMeasure":"Case","ProductCode":5,"AdditionalProductInfo":"AdditionalProductInfo","Quantity":"Quantity","ProductLabel":"ProductLabel","ItemAmount":5.9621339166831225E7,"ItemID":5,"EanUpc":1,"SaleChannel":7}],"AmountsReq":{"CashBackAmount":8008281.904610035,"MinimumSplitAmount":5.9621339166831225E7,"MaximumCashBackAmount":6.027456183070343E7,"Currency":"Currency","RequestedAmount":2.3021358869347423E7,"TipAmount":7.061401241503039E7,"MinimumAmountToDeliver":1.4658129805029305E7,"PaidAmount":5.637376656633272E7},"TransactionConditions":{"MerchantCategoryCode":"MerchantCategoryCode","AcquirerID":[4,4],"AllowedLoyaltyBrand":["AllowedLoyaltyBrand","AllowedLoyaltyBrand"],"LoyaltyHandling":"Allowed","DebitPreferredFlag":True,"CustomerLanguage":"CustomerLanguage","ForceEntryMode":["CheckReader","CheckReader"],"AllowedPaymentBrand":["AllowedPaymentBrand","AllowedPaymentBrand"],"ForceOnlineFlag":False},"OriginalPOITransaction":{"ReuseCardDataFlag":True,"POIID":"POIID","SaleID":"SaleID","AcquirerID":0,"AmountValue":6.027456183070343E7,"CustomerLanguage":"CustomerLanguage","HostTransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"},"ApprovalCode":"ApprovalCode","POITransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"}}},"PaymentData":{"Instalment":{"FirstAmount":2.0271230230023015E7,"FirstPaymentDate":"2000-01-23","PlanID":"PlanID","InstalmentType":"DeferredInstalments","SequenceNumber":7,"Period":4,"Charges":9.301444243932483E7,"TotalNbOfPayments":1,"CumulativeAmount":3.6160767492518745E7,"PeriodUnit":"Annual"},"SplitPaymentFlag":False,"PaymentInstrumentData":{"StoredValueAccountID":{"ExpiryDate":4,"OwnerName":"OwnerName","EntryMode":["Contactless","Contactless"],"StoredValueProvider":"StoredValueProvider","StoredValueID":"StoredValueID","StoredValueAccountType":"GiftCard"},"MobileData":{"Geolocation":{"UTMCoordinates":{"UTMNorthward":"UTMNorthward","UTMEastward":"UTMEastward","UTMZone":"UTMZone"},"GeographicCoordinates":{"Latitude":"Latitude","Longitude":"Longitude"}},"MaskedMSISDN":1,"MobileCountryCode":3,"MobileNetworkCode":2,"SensitiveMobileData":{"MSISDN":4,"ISMI":1,"IMEI":7},"ProtectedMobileData":"ProtectedMobileData"},"ProtectedCardData":"ProtectedCardData","PaymentInstrumentType":"Card","CheckData":{"TypeCode":"Company","Country":"Country","CheckCardNumber":"CheckCardNumber","CheckNumber":"CheckNumber","BankID":"BankID","AccountNumber":"AccountNumber","TrackData":{"TrackFormat":"AAMVA","TrackNumb":1,"TrackValue":"TrackValue"}},"CardData":{"CardCountryCode":3,"SensitiveCardData":{"CardSeqNumb":2,"ExpiryDate":4,"PAN":22,"TrackData":[{"TrackFormat":"AAMVA","TrackNumb":1,"TrackValue":"TrackValue"},{"TrackFormat":"AAMVA","TrackNumb":1,"TrackValue":"TrackValue"}]},"PaymentBrand":"PaymentBrand","ProtectedCardData":"ProtectedCardData","AllowedProduct":[{"ProductCode":11,"AdditionalProductInfo":"AdditionalProductInfo","ProductLabel":"ProductLabel","EanUpc":5},{"ProductCode":11,"AdditionalProductInfo":"AdditionalProductInfo","ProductLabel":"ProductLabel","EanUpc":5}],"CustomerOrder":[{"AdditionalInformation":"AdditionalInformation","OpenOrderState":True,"StartDate":"2000-01-23T04:56:07.000+00:00","SaleReferenceID":"SaleReferenceID","CustomerOrderID":"CustomerOrderID","Currency":"Currency","ForecastedAmount":3.6160767492518745E7,"CurrentAmount":9.301444243932483E7,"AccessedBy":"AccessedBy","EndDate":"2000-01-23T04:56:07.000+00:00"},{"AdditionalInformation":"AdditionalInformation","OpenOrderState":True,"StartDate":"2000-01-23T04:56:07.000+00:00","SaleReferenceID":"SaleReferenceID","CustomerOrderID":"CustomerOrderID","Currency":"Currency","ForecastedAmount":3.6160767492518745E7,"CurrentAmount":9.301444243932483E7,"AccessedBy":"AccessedBy","EndDate":"2000-01-23T04:56:07.000+00:00"}],"EntryMode":["Contactless","Contactless"],"PaymentAccountRef":"PaymentAccountRef","MaskedPan":"MaskedPan","PaymentToken":{"ExpiryDateTime":"2000-01-23T04:56:07.000+00:00","TokenRequestedType":"Customer","TokenValue":"TokenValue"},"AllowedProductCode":[5,5]}},"CustomerOrder":{"AdditionalInformation":"AdditionalInformation","OpenOrderState":True,"StartDate":"2000-01-23T04:56:07.000+00:00","SaleReferenceID":"SaleReferenceID","CustomerOrderID":"CustomerOrderID","Currency":"Currency","ForecastedAmount":3.6160767492518745E7,"CurrentAmount":9.301444243932483E7,"AccessedBy":"AccessedBy","EndDate":"2000-01-23T04:56:07.000+00:00"},"PaymentType":"CashAdvance","RequestedValidityDate":"2000-01-23","CardAcquisitionReference":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"}},"LoyaltyData":[{"LoyaltyAccountID":{"LoyaltyID":"LoyaltyID","IdentificationSupport":"HybridCard","EntryMode":["Contactless","Contactless"],"IdentificationType":"AccountNumber"},"CardAcquisitionReference":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"},"LoyaltyAmount":{"LoyaltyUnit":"Monetary","Currency":"Currency","AmountValue":6.027456183070343E7}},{"LoyaltyAccountID":{"LoyaltyID":"LoyaltyID","IdentificationSupport":"HybridCard","EntryMode":["Contactless","Contactless"],"IdentificationType":"AccountNumber"},"CardAcquisitionReference":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"},"LoyaltyAmount":{"LoyaltyUnit":"Monetary","Currency":"Currency","AmountValue":6.027456183070343E7}}],"SaleData":{"SaleToAcquirerData":"SaleToAcquirerData","SaleToIssuerData":{"StatementReference":"StatementReference"},"SaleTransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"},"SaleReferenceID":"SaleReferenceID","SaleTerminalData":{"TotalsGroupID":"TotalsGroupID"},"CustomerOrderID":"CustomerOrderID","CustomerOrderReq":["Both","Both"],"OperatorLanguage":"OperatorLanguage","TokenRequestedType":"Customer","OperatorID":"OperatorID","ShiftNumber":"ShiftNumber","SaleToPOIData":"SaleToPOIData"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/payment',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_print_post(client):
    """Test case for print_post

    Print Request
    """
    body = {"PrintOutput":{"IntegratedPrintFlag":False,"RequiredSignatureFlag":False,"ResponseMode":"Immediate","OutputContent":{"OutputBarcode":{"BarcodeValue":"BarcodeValue","BarcodeType":"Code128"},"OutputFormat":"BarCode","OutputText":[{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468},{"Alignment":"Centred","CharacterHeight":"DoubleHeight","CharacterWidth":"DoubleWidth","EndOfLineFlag":True,"Color":"Black","Text":"Text","CharacterSet":9,"CharacterStyle":"Bold","Font":"Font","StartRow":334,"StartColumn":468}],"PredefinedContent":{"Language":"Language","ReferenceID":"ReferenceID"},"OutputXHTML":"OutputXHTML"},"DocumentQualifier":"CashierReceipt"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/print',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reconciliation_post(client):
    """Test case for reconciliation_post

    Reconciliation Request
    """
    body = {"ReconciliationType":"AcquirerReconciliation","POIReconciliationID":6,"AcquirerID":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/reconciliation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reversal_post(client):
    """Test case for reversal_post

    Reversal Request
    """
    body = {"CustomerOrder":{"AdditionalInformation":"AdditionalInformation","OpenOrderState":True,"StartDate":"2000-01-23T04:56:07.000+00:00","SaleReferenceID":"SaleReferenceID","CustomerOrderID":"CustomerOrderID","Currency":"Currency","ForecastedAmount":3.6160767492518745E7,"CurrentAmount":9.301444243932483E7,"AccessedBy":"AccessedBy","EndDate":"2000-01-23T04:56:07.000+00:00"},"SaleData":{"SaleToAcquirerData":"SaleToAcquirerData","SaleToIssuerData":{"StatementReference":"StatementReference"},"SaleTransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"},"SaleReferenceID":"SaleReferenceID","SaleTerminalData":{"TotalsGroupID":"TotalsGroupID"},"CustomerOrderID":"CustomerOrderID","CustomerOrderReq":["Both","Both"],"OperatorLanguage":"OperatorLanguage","TokenRequestedType":"Customer","OperatorID":"OperatorID","ShiftNumber":"ShiftNumber","SaleToPOIData":"SaleToPOIData"},"ReversalReason":"CustCancel","ReversedAmount":8008281.904610035,"OriginalPOITransaction":{"ReuseCardDataFlag":True,"POIID":"POIID","SaleID":"SaleID","AcquirerID":0,"AmountValue":6.027456183070343E7,"CustomerLanguage":"CustomerLanguage","HostTransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"},"ApprovalCode":"ApprovalCode","POITransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/reversal',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storedvalue_post(client):
    """Test case for storedvalue_post

    StoredValue Request
    """
    body = {"StoredValueData":[{"StoredValueAccountID":{"ExpiryDate":4,"OwnerName":"OwnerName","EntryMode":["Contactless","Contactless"],"StoredValueProvider":"StoredValueProvider","StoredValueID":"StoredValueID","StoredValueAccountType":"GiftCard"},"ProductCode":3,"Currency":"Currency","StoredValueProvider":"StoredValueProvider","StoredValueTransactionType":"Activate","ItemAmount":6.027456183070343E7,"OriginalPOITransaction":{"ReuseCardDataFlag":True,"POIID":"POIID","SaleID":"SaleID","AcquirerID":0,"AmountValue":6.027456183070343E7,"CustomerLanguage":"CustomerLanguage","HostTransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"},"ApprovalCode":"ApprovalCode","POITransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"}},"EanUpc":0},{"StoredValueAccountID":{"ExpiryDate":4,"OwnerName":"OwnerName","EntryMode":["Contactless","Contactless"],"StoredValueProvider":"StoredValueProvider","StoredValueID":"StoredValueID","StoredValueAccountType":"GiftCard"},"ProductCode":3,"Currency":"Currency","StoredValueProvider":"StoredValueProvider","StoredValueTransactionType":"Activate","ItemAmount":6.027456183070343E7,"OriginalPOITransaction":{"ReuseCardDataFlag":True,"POIID":"POIID","SaleID":"SaleID","AcquirerID":0,"AmountValue":6.027456183070343E7,"CustomerLanguage":"CustomerLanguage","HostTransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"},"ApprovalCode":"ApprovalCode","POITransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"}},"EanUpc":0}],"SaleData":{"SaleToAcquirerData":"SaleToAcquirerData","SaleToIssuerData":{"StatementReference":"StatementReference"},"SaleTransactionID":{"TimeStamp":"2000-01-23T04:56:07.000+00:00","TransactionID":"TransactionID"},"SaleReferenceID":"SaleReferenceID","SaleTerminalData":{"TotalsGroupID":"TotalsGroupID"},"CustomerOrderID":"CustomerOrderID","CustomerOrderReq":["Both","Both"],"OperatorLanguage":"OperatorLanguage","TokenRequestedType":"Customer","OperatorID":"OperatorID","ShiftNumber":"ShiftNumber","SaleToPOIData":"SaleToPOIData"},"CustomerLanguage":"CustomerLanguage"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/storedvalue',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactionstatus_post(client):
    """Test case for transactionstatus_post

    TransactionStatus Request
    """
    body = {"ReceiptReprintFlag":False,"MessageReference":{"DeviceID":"DeviceID","POIID":"POIID","SaleID":"SaleID","MessageCategory":"Abort","ServiceID":"ServiceID"},"DocumentQualifier":["CashierReceipt","CashierReceipt"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/transactionstatus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

