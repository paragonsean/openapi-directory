# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.transfer_billing_subscription_request_properties import TransferBillingSubscriptionRequestProperties
from openapi_server.models.transfer_billing_subscription_result import TransferBillingSubscriptionResult
from openapi_server.models.transfer_product_request_properties import TransferProductRequestProperties
from openapi_server.models.validate_product_transfer_eligibility_result import ValidateProductTransferEligibilityResult
from openapi_server.models.validate_subscription_transfer_eligibility_result import ValidateSubscriptionTransferEligibilityResult


pytestmark = pytest.mark.asyncio

async def test_billing_subscriptions_transfer(client):
    """Test case for billing_subscriptions_transfer

    
    """
    parameters = {"destinationInvoiceSectionId":"destinationInvoiceSectionId","destinationBillingProfileId":"destinationBillingProfileId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/invoiceSections/{invoice_section_name}/billingSubscriptions/{billing_subscription_name}/transfer'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', invoice_section_name='invoice_section_name_example', billing_subscription_name='billing_subscription_name_example'),
        headers=headers,
        json=parameters,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_subscriptions_validate_transfer(client):
    """Test case for billing_subscriptions_validate_transfer

    
    """
    parameters = {"destinationInvoiceSectionId":"destinationInvoiceSectionId","destinationBillingProfileId":"destinationBillingProfileId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/invoiceSections/{invoice_section_name}/billingSubscriptions/{billing_subscription_name}/validateTransferEligibility'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', invoice_section_name='invoice_section_name_example', billing_subscription_name='billing_subscription_name_example'),
        headers=headers,
        json=parameters,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_validate_transfer(client):
    """Test case for products_validate_transfer

    
    """
    parameters = {"destinationInvoiceSectionId":"destinationInvoiceSectionId","destinationBillingProfileId":"destinationBillingProfileId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/invoiceSections/{invoice_section_name}/products/{product_name}/validateTransferEligibility'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', invoice_section_name='invoice_section_name_example', product_name='product_name_example'),
        headers=headers,
        json=parameters,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

