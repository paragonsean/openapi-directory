# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.orderinvoices_create_charge_invoice_request import OrderinvoicesCreateChargeInvoiceRequest
from openapi_server.models.orderinvoices_create_charge_invoice_response import OrderinvoicesCreateChargeInvoiceResponse
from openapi_server.models.orderinvoices_create_refund_invoice_request import OrderinvoicesCreateRefundInvoiceRequest
from openapi_server.models.orderinvoices_create_refund_invoice_response import OrderinvoicesCreateRefundInvoiceResponse


pytestmark = pytest.mark.asyncio

async def test_content_orderinvoices_createchargeinvoice(client):
    """Test case for content_orderinvoices_createchargeinvoice

    
    """
    body = {"shipmentGroupId":"shipmentGroupId","invoiceSummary":{"additionalChargeSummaries":[{"totalAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"},{"totalAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"}],"productTotal":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}}},"lineItemInvoices":[{"productId":"productId","shipmentUnitIds":["shipmentUnitIds","shipmentUnitIds"],"unitInvoice":{"unitPrice":{"currency":"currency","value":"value"},"additionalCharges":[{"additionalChargeAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"},{"additionalChargeAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"}],"unitPriceTaxes":[{"taxAmount":{"currency":"currency","value":"value"},"taxName":"taxName","taxType":"taxType"},{"taxAmount":{"currency":"currency","value":"value"},"taxName":"taxName","taxType":"taxType"}]},"lineItemId":"lineItemId"},{"productId":"productId","shipmentUnitIds":["shipmentUnitIds","shipmentUnitIds"],"unitInvoice":{"unitPrice":{"currency":"currency","value":"value"},"additionalCharges":[{"additionalChargeAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"},{"additionalChargeAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"}],"unitPriceTaxes":[{"taxAmount":{"currency":"currency","value":"value"},"taxName":"taxName","taxType":"taxType"},{"taxAmount":{"currency":"currency","value":"value"},"taxName":"taxName","taxType":"taxType"}]},"lineItemId":"lineItemId"}],"operationId":"operationId","invoiceId":"invoiceId"}
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
        method='POST',
        path='/content/v2.1/{merchant_id}/orderinvoices/{order_id}/createChargeInvoice'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orderinvoices_createrefundinvoice(client):
    """Test case for content_orderinvoices_createrefundinvoice

    
    """
    body = {"returnOption":{"reason":"reason","description":"description"},"operationId":"operationId","invoiceId":"invoiceId","refundOnlyOption":{"reason":"reason","description":"description"},"shipmentInvoices":[{"shipmentGroupId":"shipmentGroupId","invoiceSummary":{"additionalChargeSummaries":[{"totalAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"},{"totalAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"}],"productTotal":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}}},"lineItemInvoices":[{"productId":"productId","shipmentUnitIds":["shipmentUnitIds","shipmentUnitIds"],"unitInvoice":{"unitPrice":{"currency":"currency","value":"value"},"additionalCharges":[{"additionalChargeAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"},{"additionalChargeAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"}],"unitPriceTaxes":[{"taxAmount":{"currency":"currency","value":"value"},"taxName":"taxName","taxType":"taxType"},{"taxAmount":{"currency":"currency","value":"value"},"taxName":"taxName","taxType":"taxType"}]},"lineItemId":"lineItemId"},{"productId":"productId","shipmentUnitIds":["shipmentUnitIds","shipmentUnitIds"],"unitInvoice":{"unitPrice":{"currency":"currency","value":"value"},"additionalCharges":[{"additionalChargeAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"},{"additionalChargeAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"}],"unitPriceTaxes":[{"taxAmount":{"currency":"currency","value":"value"},"taxName":"taxName","taxType":"taxType"},{"taxAmount":{"currency":"currency","value":"value"},"taxName":"taxName","taxType":"taxType"}]},"lineItemId":"lineItemId"}]},{"shipmentGroupId":"shipmentGroupId","invoiceSummary":{"additionalChargeSummaries":[{"totalAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"},{"totalAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"}],"productTotal":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}}},"lineItemInvoices":[{"productId":"productId","shipmentUnitIds":["shipmentUnitIds","shipmentUnitIds"],"unitInvoice":{"unitPrice":{"currency":"currency","value":"value"},"additionalCharges":[{"additionalChargeAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"},{"additionalChargeAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"}],"unitPriceTaxes":[{"taxAmount":{"currency":"currency","value":"value"},"taxName":"taxName","taxType":"taxType"},{"taxAmount":{"currency":"currency","value":"value"},"taxName":"taxName","taxType":"taxType"}]},"lineItemId":"lineItemId"},{"productId":"productId","shipmentUnitIds":["shipmentUnitIds","shipmentUnitIds"],"unitInvoice":{"unitPrice":{"currency":"currency","value":"value"},"additionalCharges":[{"additionalChargeAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"},{"additionalChargeAmount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"type":"type"}],"unitPriceTaxes":[{"taxAmount":{"currency":"currency","value":"value"},"taxName":"taxName","taxType":"taxType"},{"taxAmount":{"currency":"currency","value":"value"},"taxName":"taxName","taxType":"taxType"}]},"lineItemId":"lineItemId"}]}]}
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
        method='POST',
        path='/content/v2.1/{merchant_id}/orderinvoices/{order_id}/createRefundInvoice'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

