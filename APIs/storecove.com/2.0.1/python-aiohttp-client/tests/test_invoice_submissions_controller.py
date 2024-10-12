# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.invoice_recipient_preflight import InvoiceRecipientPreflight
from openapi_server.models.invoice_submission import InvoiceSubmission
from openapi_server.models.invoice_submission_evidence import InvoiceSubmissionEvidence
from openapi_server.models.invoice_submission_result import InvoiceSubmissionResult
from openapi_server.models.preflight_invoice_recipient_result import PreflightInvoiceRecipientResult


pytestmark = pytest.mark.asyncio

async def test_create_invoice_submission(client):
    """Test case for create_invoice_submission

    Submit a new invoice
    """
    body = {"invoiceData":{"conversionStrategy":"ubl","document":"document"},"attachments":[{"filename":"filename","primaryImage":False,"document":"document","description":"description","documentId":"documentId","mimeType":"application/pdf"},{"filename":"filename","primaryImage":False,"document":"document","description":"description","documentId":"documentId","mimeType":"application/pdf"},{"filename":"filename","primaryImage":False,"document":"document","description":"description","documentId":"documentId","mimeType":"application/pdf"},{"filename":"filename","primaryImage":False,"document":"document","description":"description","documentId":"documentId","mimeType":"application/pdf"},{"filename":"filename","primaryImage":False,"document":"document","description":"description","documentId":"documentId","mimeType":"application/pdf"}],"supplierId":1,"document":"document","documentUrl":"https://openapi-generator.tech","idempotencyGuid":"idempotencyGuid","legalSupplierId":6,"createPrimaryImage":True,"invoiceRecipient":{"emails":["emails","emails"],"publicIdentifiers":[{"scheme":"scheme","id":"id"},{"scheme":"scheme","id":"id"}]},"mode":"direct","routing":{"emails":["emails","emails"],"eIdentifiers":[{"scheme":"scheme","id":"id"},{"scheme":"scheme","id":"id"}],"clearWithoutSending":False},"legalEntityId":0,"invoice":{"salesOrderId":"salesOrderId","contractDocumentReference":"contractDocumentReference","note":"note","accountingCost":"accountingCost","attachments":[{"filename":"filename","primaryImage":False,"document":"document","description":"description","documentId":"documentId","mimeType":"application/pdf"},{"filename":"filename","primaryImage":False,"document":"document","description":"description","documentId":"documentId","mimeType":"application/pdf"},{"filename":"filename","primaryImage":False,"document":"document","description":"description","documentId":"documentId","mimeType":"application/pdf"},{"filename":"filename","primaryImage":False,"document":"document","description":"description","documentId":"documentId","mimeType":"application/pdf"},{"filename":"filename","primaryImage":False,"document":"document","description":"description","documentId":"documentId","mimeType":"application/pdf"}],"priceMode":"price_mode_net","references":[{"documentType":"purchase_order","lineId":"lineId","documentId":"documentId","issueDate":"issueDate"},{"documentType":"purchase_order","lineId":"lineId","documentId":"documentId","issueDate":"issueDate"}],"prepaidAmount":5.025004791520295,"dueDate":"dueDate","paymentMeansIban":"paymentMeansIban","preferredInvoiceType":"prefer_autodetect","paymentMeansBic":"paymentMeansBic","taxPointDate":"taxPointDate","vatReverseCharge":False,"issueReasons":["issueReasons","issueReasons"],"taxSubtotals":[{"taxableAmount":6.683562403749608,"percentage":9.965781217890562,"category":"standard","taxAmount":9.369310271410669},{"taxableAmount":6.683562403749608,"percentage":9.965781217890562,"category":"standard","taxAmount":9.369310271410669}],"accountingCurrencyTaxAmountCurrency":"AED","accountingCurrencyTaxAmount":0.8008281904610115,"allowanceCharges":[{"amountExcludingVat":1.4658129805029452,"reason":"Agreed settlement","amountExcludingTax":6.027456183070403,"baseAmountIncludingTax":2.3021358869347655,"tax":{"amount":7.061401241503109,"percentage":9.301444243932576,"category":"standard"},"reasonCode":"reasonCode","taxesDutiesFees":[{"amount":7.061401241503109,"percentage":9.301444243932576,"category":"standard"},{"amount":7.061401241503109,"percentage":9.301444243932576,"category":"standard"}],"amountIncludingTax":5.962133916683182,"baseAmountExcludingTax":5.637376656633329},{"amountExcludingVat":1.4658129805029452,"reason":"Agreed settlement","amountExcludingTax":6.027456183070403,"baseAmountIncludingTax":2.3021358869347655,"tax":{"amount":7.061401241503109,"percentage":9.301444243932576,"category":"standard"},"reasonCode":"reasonCode","taxesDutiesFees":[{"amount":7.061401241503109,"percentage":9.301444243932576,"category":"standard"},{"amount":7.061401241503109,"percentage":9.301444243932576,"category":"standard"}],"amountIncludingTax":5.962133916683182,"baseAmountExcludingTax":5.637376656633329}],"invoiceLines":[{"amountExcludingVat":1.4894159098541704,"note":"note","additionalItemProperties":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"accountingCost":"accountingCost","quantity":1.1730742509559433,"references":[{"documentType":"purchase_order","lineId":"lineId","documentId":"documentId","issueDate":"issueDate"},{"documentType":"purchase_order","lineId":"lineId","documentId":"documentId","issueDate":"issueDate"}],"amountExcludingTax":1.0246457001441578,"description":"description","lineId":"lineId","standardItemIdentificationSchemeId":"GTIN","tax":{"amount":7.061401241503109,"percentage":9.301444243932576,"category":"standard"},"quantityUnitCode":"C62","allowanceCharges":[{"reason":"reason","amountExcludingTax":7.386281948385884,"reasonCode":"reasonCode","baseAmountExcludingTax":1.2315135367772556},{"reason":"reason","amountExcludingTax":7.386281948385884,"reasonCode":"reasonCode","baseAmountExcludingTax":1.2315135367772556}],"standardItemIdentification":"standardItemIdentification","standardItemIdentificationSchemeAgencyId":"9","invoicePeriod":"invoicePeriod","name":"name","orderLineReferenceLineId":"orderLineReferenceLineId","itemPrice":7.457744773683766,"taxesDutiesFees":[{"amount":7.061401241503109,"percentage":9.301444243932576,"category":"standard"},{"amount":7.061401241503109,"percentage":9.301444243932576,"category":"standard"}],"amountIncludingTax":6.84685269835264,"buyersItemIdentification":"buyersItemIdentification","allowanceCharge":4.145608029883936,"sellersItemIdentification":"sellersItemIdentification"},{"amountExcludingVat":1.4894159098541704,"note":"note","additionalItemProperties":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"accountingCost":"accountingCost","quantity":1.1730742509559433,"references":[{"documentType":"purchase_order","lineId":"lineId","documentId":"documentId","issueDate":"issueDate"},{"documentType":"purchase_order","lineId":"lineId","documentId":"documentId","issueDate":"issueDate"}],"amountExcludingTax":1.0246457001441578,"description":"description","lineId":"lineId","standardItemIdentificationSchemeId":"GTIN","tax":{"amount":7.061401241503109,"percentage":9.301444243932576,"category":"standard"},"quantityUnitCode":"C62","allowanceCharges":[{"reason":"reason","amountExcludingTax":7.386281948385884,"reasonCode":"reasonCode","baseAmountExcludingTax":1.2315135367772556},{"reason":"reason","amountExcludingTax":7.386281948385884,"reasonCode":"reasonCode","baseAmountExcludingTax":1.2315135367772556}],"standardItemIdentification":"standardItemIdentification","standardItemIdentificationSchemeAgencyId":"9","invoicePeriod":"invoicePeriod","name":"name","orderLineReferenceLineId":"orderLineReferenceLineId","itemPrice":7.457744773683766,"taxesDutiesFees":[{"amount":7.061401241503109,"percentage":9.301444243932576,"category":"standard"},{"amount":7.061401241503109,"percentage":9.301444243932576,"category":"standard"}],"amountIncludingTax":6.84685269835264,"buyersItemIdentification":"buyersItemIdentification","allowanceCharge":4.145608029883936,"sellersItemIdentification":"sellersItemIdentification"}],"selfBillingMode":False,"invoicePeriod":"invoicePeriod","consumerTaxMode":False,"invoiceNumber":"invoiceNumber","invoiceType":"380","issueDate":"issueDate","taxExemptReason":"export","accountingSupplierParty":{"party":{"contact":{"firstName":"firstName","lastName":"lastName","phone":"phone","id":"id","email":"email"}}},"paymentTerms":{"note":"note"},"delivery":{"quantity":2.027123023002322,"deliveryLocation":{"address":{"zip":"zip","country":"AD","city":"city","county":"county","street1":"street1","street2":"street2"},"locationName":"locationName","schemeAgencyId":"schemeAgencyId","schemeId":"schemeId","id":"id"},"deliveryParty":{"party":{"address":{"zip":"zip","country":"AD","city":"city","county":"county","street1":"street1","street2":"street2"},"companyName":"companyName","contact":{"firstName":"firstName","lastName":"lastName","phone":"phone","id":"id","email":"email"}}},"shippingMarks":"shippingMarks","requestedDeliveryPeriod":"requestedDeliveryPeriod","actualDate":"actualDate","deliveryPartyName":"deliveryPartyName"},"accountingCustomerParty":{"publicIdentifiers":[{"scheme":"scheme","id":"id"},{"scheme":"scheme","id":"id"}],"party":{"address":{"zip":"zip","country":"AD","city":"city","county":"county","street1":"street1","street2":"street2"},"companyName":"companyName","contact":{"firstName":"firstName","lastName":"lastName","phone":"phone","id":"id","email":"email"}}},"buyerReference":"buyerReference","ublExtensions":["ublExtensions","ublExtensions"],"paymentMeansArray":[{"amount":4.965218492984954,"mandate":"mandate","code":"credit_transfer","paymentId":"paymentId","branche_code":"branche_code","holder":"holder","account":"account","network":"network"},{"amount":4.965218492984954,"mandate":"mandate","code":"credit_transfer","paymentId":"paymentId","branche_code":"branche_code","holder":"holder","account":"account","network":"network"}],"transactionType":"b2b","paymentMeansCode":"online_payment_service","billingReference":"billingReference","orderReference":"orderReference","taxSystem":"tax_line_amounts","taxesDutiesFees":[{"amount":7.061401241503109,"percentage":9.301444243932576,"category":"standard"}],"paymentMeansPaymentId":"paymentMeansPaymentId","amountIncludingVat":3.616076749251911,"x2y":"b2b","projectReference":"projectReference"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/invoice_submissions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preflight_invoice_recipient(client):
    """Test case for preflight_invoice_recipient

    DEPRECATED. Preflight an invoice recipient
    """
    body = {"publicIdentifiers":[{"scheme":"scheme","id":"id"},{"scheme":"scheme","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/invoice_submissions/preflight',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_invoice_submission_evidence(client):
    """Test case for show_invoice_submission_evidence

    DEPRECATED. Get InvoiceSubmission Evidence
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/invoice_submissions/{guid}/evidence'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

