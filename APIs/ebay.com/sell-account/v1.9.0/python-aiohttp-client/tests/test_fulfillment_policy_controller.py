# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fulfillment_policy import FulfillmentPolicy
from openapi_server.models.fulfillment_policy_request import FulfillmentPolicyRequest
from openapi_server.models.fulfillment_policy_response import FulfillmentPolicyResponse
from openapi_server.models.set_fulfillment_policy_response import SetFulfillmentPolicyResponse


pytestmark = pytest.mark.asyncio

async def test_create_fulfillment_policy(client):
    """Test case for create_fulfillment_policy

    
    """
    body = {"handlingTime":{"unit":"unit","value":0},"localPickup":True,"marketplaceId":"marketplaceId","categoryTypes":[{"default":True,"name":"name"},{"default":True,"name":"name"}],"name":"name","description":"description","pickupDropOff":True,"globalShipping":True,"freightShipping":True,"shipToLocations":{"regionIncluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}],"regionExcluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}]},"shippingOptions":[{"optionType":"optionType","insuranceFee":{"currency":"currency","value":"value"},"rateTableId":"rateTableId","shippingPromotionOffered":True,"costType":"costType","insuranceOffered":True,"packageHandlingCost":{"currency":"currency","value":"value"},"shippingDiscountProfileId":"shippingDiscountProfileId","shippingServices":[{"surcharge":{"currency":"currency","value":"value"},"buyerResponsibleForPickup":True,"buyerResponsibleForShipping":True,"shippingCost":{"currency":"currency","value":"value"},"additionalShippingCost":{"currency":"currency","value":"value"},"freeShipping":True,"shippingCarrierCode":"shippingCarrierCode","sortOrder":6,"shippingServiceCode":"shippingServiceCode","shipToLocations":{"regionIncluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}],"regionExcluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}]},"cashOnDeliveryFee":{"currency":"currency","value":"value"}},{"surcharge":{"currency":"currency","value":"value"},"buyerResponsibleForPickup":True,"buyerResponsibleForShipping":True,"shippingCost":{"currency":"currency","value":"value"},"additionalShippingCost":{"currency":"currency","value":"value"},"freeShipping":True,"shippingCarrierCode":"shippingCarrierCode","sortOrder":6,"shippingServiceCode":"shippingServiceCode","shipToLocations":{"regionIncluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}],"regionExcluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}]},"cashOnDeliveryFee":{"currency":"currency","value":"value"}}]},{"optionType":"optionType","insuranceFee":{"currency":"currency","value":"value"},"rateTableId":"rateTableId","shippingPromotionOffered":True,"costType":"costType","insuranceOffered":True,"packageHandlingCost":{"currency":"currency","value":"value"},"shippingDiscountProfileId":"shippingDiscountProfileId","shippingServices":[{"surcharge":{"currency":"currency","value":"value"},"buyerResponsibleForPickup":True,"buyerResponsibleForShipping":True,"shippingCost":{"currency":"currency","value":"value"},"additionalShippingCost":{"currency":"currency","value":"value"},"freeShipping":True,"shippingCarrierCode":"shippingCarrierCode","sortOrder":6,"shippingServiceCode":"shippingServiceCode","shipToLocations":{"regionIncluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}],"regionExcluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}]},"cashOnDeliveryFee":{"currency":"currency","value":"value"}},{"surcharge":{"currency":"currency","value":"value"},"buyerResponsibleForPickup":True,"buyerResponsibleForShipping":True,"shippingCost":{"currency":"currency","value":"value"},"additionalShippingCost":{"currency":"currency","value":"value"},"freeShipping":True,"shippingCarrierCode":"shippingCarrierCode","sortOrder":6,"shippingServiceCode":"shippingServiceCode","shipToLocations":{"regionIncluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}],"regionExcluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}]},"cashOnDeliveryFee":{"currency":"currency","value":"value"}}]}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/account/v1/fulfillment_policy/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_fulfillment_policy(client):
    """Test case for delete_fulfillment_policy

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}'.format(fulfillment_policy_id='fulfillment_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fulfillment_policies(client):
    """Test case for get_fulfillment_policies

    
    """
    params = [('marketplace_id', 'marketplace_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/fulfillment_policy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fulfillment_policy(client):
    """Test case for get_fulfillment_policy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}'.format(fulfillment_policy_id='fulfillment_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fulfillment_policy_by_name(client):
    """Test case for get_fulfillment_policy_by_name

    
    """
    params = [('marketplace_id', 'marketplace_id_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/fulfillment_policy/get_by_policy_name',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_fulfillment_policy(client):
    """Test case for update_fulfillment_policy

    
    """
    body = {"handlingTime":{"unit":"unit","value":0},"localPickup":True,"marketplaceId":"marketplaceId","categoryTypes":[{"default":True,"name":"name"},{"default":True,"name":"name"}],"name":"name","description":"description","pickupDropOff":True,"globalShipping":True,"freightShipping":True,"shipToLocations":{"regionIncluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}],"regionExcluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}]},"shippingOptions":[{"optionType":"optionType","insuranceFee":{"currency":"currency","value":"value"},"rateTableId":"rateTableId","shippingPromotionOffered":True,"costType":"costType","insuranceOffered":True,"packageHandlingCost":{"currency":"currency","value":"value"},"shippingDiscountProfileId":"shippingDiscountProfileId","shippingServices":[{"surcharge":{"currency":"currency","value":"value"},"buyerResponsibleForPickup":True,"buyerResponsibleForShipping":True,"shippingCost":{"currency":"currency","value":"value"},"additionalShippingCost":{"currency":"currency","value":"value"},"freeShipping":True,"shippingCarrierCode":"shippingCarrierCode","sortOrder":6,"shippingServiceCode":"shippingServiceCode","shipToLocations":{"regionIncluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}],"regionExcluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}]},"cashOnDeliveryFee":{"currency":"currency","value":"value"}},{"surcharge":{"currency":"currency","value":"value"},"buyerResponsibleForPickup":True,"buyerResponsibleForShipping":True,"shippingCost":{"currency":"currency","value":"value"},"additionalShippingCost":{"currency":"currency","value":"value"},"freeShipping":True,"shippingCarrierCode":"shippingCarrierCode","sortOrder":6,"shippingServiceCode":"shippingServiceCode","shipToLocations":{"regionIncluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}],"regionExcluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}]},"cashOnDeliveryFee":{"currency":"currency","value":"value"}}]},{"optionType":"optionType","insuranceFee":{"currency":"currency","value":"value"},"rateTableId":"rateTableId","shippingPromotionOffered":True,"costType":"costType","insuranceOffered":True,"packageHandlingCost":{"currency":"currency","value":"value"},"shippingDiscountProfileId":"shippingDiscountProfileId","shippingServices":[{"surcharge":{"currency":"currency","value":"value"},"buyerResponsibleForPickup":True,"buyerResponsibleForShipping":True,"shippingCost":{"currency":"currency","value":"value"},"additionalShippingCost":{"currency":"currency","value":"value"},"freeShipping":True,"shippingCarrierCode":"shippingCarrierCode","sortOrder":6,"shippingServiceCode":"shippingServiceCode","shipToLocations":{"regionIncluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}],"regionExcluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}]},"cashOnDeliveryFee":{"currency":"currency","value":"value"}},{"surcharge":{"currency":"currency","value":"value"},"buyerResponsibleForPickup":True,"buyerResponsibleForShipping":True,"shippingCost":{"currency":"currency","value":"value"},"additionalShippingCost":{"currency":"currency","value":"value"},"freeShipping":True,"shippingCarrierCode":"shippingCarrierCode","sortOrder":6,"shippingServiceCode":"shippingServiceCode","shipToLocations":{"regionIncluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}],"regionExcluded":[{"regionType":"regionType","regionName":"regionName"},{"regionType":"regionType","regionName":"regionName"}]},"cashOnDeliveryFee":{"currency":"currency","value":"value"}}]}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}'.format(fulfillment_policy_id='fulfillment_policy_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

