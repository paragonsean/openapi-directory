# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.flat_rate_input_model import FlatRateInputModel
from openapi_server.models.flat_rate_output_model import FlatRateOutputModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server.models.project_fee_input_model import ProjectFeeInputModel
from openapi_server.models.project_fee_output_model import ProjectFeeOutputModel
from openapi_server.models.project_recurring_fee_rule_input_model import ProjectRecurringFeeRuleInputModel
from openapi_server.models.project_recurring_fee_rule_output_model import ProjectRecurringFeeRuleOutputModel


pytestmark = pytest.mark.asyncio

async def test_flat_rates_patch_flat_rate(client):
    """Test case for flat_rates_patch_flat_rate

    Update (Patch) a flat rate or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/flatrates/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flat_rates_post_flat_rate(client):
    """Test case for flat_rates_post_flat_rate

    Insert a flat rate.
    """
    body = {"phase":{"guid":"guid"},"pricePerAdditionalHour":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"billAdditionalHours":True,"billingSchedule":"Immediately","price":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"plannedBillingDate":"2000-01-23","includesHours":0.8008281904610115}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/flatrates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_fees_patch_project_fee(client):
    """Test case for project_fees_patch_project_fee

    Update (Patch) a projectFee or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projectfees/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_fees_post_project_fee(client):
    """Test case for project_fees_post_project_fee

    Insert a project fee.
    """
    body = {"vatRate":1.4658129805029452,"description":"description","project":{"guid":"guid"},"invoiceRowDescription":"invoiceRowDescription","hasVolumePricing":True,"productType":"FixedFees","phase":{"guid":"guid"},"unitPrice":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"product":{"guid":"guid"},"salesAccount":{"guid":"guid"},"quantity":6.027456183070403,"billingSchedule":"Immediately","costCenter":{"guid":"guid"},"billingDependencyPhase":{"guid":"guid"},"plannedBillingDate":"2000-01-23","measurementUnit":"measurementUnit","isBillable":True,"invoiceQuantity":0.8008281904610115,"unitCost":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"name":"name","invoice":{"guid":"guid"},"invoiceRowComment":"invoiceRowComment","user":{"guid":"guid"},"displayPeriodStartDate":"2000-01-23","eventDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projectfees',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_recurring_fee_rules_patch_project_recurring_fee_rule(client):
    """Test case for project_recurring_fee_rules_patch_project_recurring_fee_rule

    Update (Patch) a projectRecurringFeeRule or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projectrecurringfeerules/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_recurring_fee_rules_post_project_recurring_fee_rule(client):
    """Test case for project_recurring_fee_rules_post_project_recurring_fee_rule

    Insert a projectRecurringFeeRule.
    """
    body = {"phase":{"guid":"guid"},"unitPrice":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"recurrenceEndDate":"2000-01-23","product":{"guid":"guid"},"salesAccount":{"guid":"guid"},"quantity":6.027456183070403,"recurrenceTimes":1,"recurrenceEndType":"Never","costCenter":{"guid":"guid"},"vatRate":5.962133916683182,"description":"description","project":{"guid":"guid"},"isActive":True,"recurringSalesAccount":{"guid":"guid"},"measurementUnit":"measurementUnit","frequency":0,"recurrenceStartDate":"2000-01-23","unitCost":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"hasVolumePricing":True,"user":{"guid":"guid"},"displayPeriodStartDate":"2000-01-23","productType":"FixedFees"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projectrecurringfeerules',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

