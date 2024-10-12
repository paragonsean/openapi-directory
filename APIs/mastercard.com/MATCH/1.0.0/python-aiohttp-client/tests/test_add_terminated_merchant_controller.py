# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_terminated_merchant_request_schema import AddTerminatedMerchantRequestSchema
from openapi_server.models.add_terminated_merchant_response_schema import AddTerminatedMerchantResponseSchema
from openapi_server.models.errors_response import ErrorsResponse


pytestmark = pytest.mark.asyncio

async def test_fraud_merchant_v3_add_merchant_post(client):
    """Test case for fraud_merchant_v3_add_merchant_post

    Used by Acquirers to add a terminated a merchant in the MATCH system. Merchant information, and up to five principal owners per merchant, can be provided by an acquiring bank as part of the listing.
    """
    add_terminated_merchant_request_schema = {"AddMerchantRequest":{"Merchant":{"DateOpened":"12/31/2013","DoingBusinessAsName":"BAIT R US","Address":{"Country":"USA","PostalCode":"66579","CountrySubdivision":"IL","City":"DALLAS","Line1":"42 ELM AVENUE","Line2":"SUITE 201","Province":""},"Comments":"Added for reasons of fraud","MerchantCategory":"0742","AltPhoneNumber":"6367558968","NationalTaxId":"*****","MerchantId":"@random-string[14]@","ReasonCode":"13","Url":["www.testmerchant.com ","www.testmerchant.com "],"CATFlag":"Y","Name":"THE BAIT SHOP","DateClosed":"10/12/2014","CountrySubdivisionTaxId":"*****","PhoneNumber":"6367558963","ServiceProvLegal":"XYZ FINANCIAL SERVICE INCORPORATED","Principal":{"Address":{"Country":"USA","PostalCode":"66579","CountrySubdivision":"IL","City":"DALLAS","Line1":"42 ELM AVENUE","Line2":"SUITE 201","Province":""},"MiddleInitial":"P","FirstName":"DAVID","NationalId":"541022104","PhoneNumber":"3165557625","AltPhoneNumber":"3165557625","DriversLicense":{"Number":"M15698025","Country":"USA","CountrySubdivision":"IL"},"LastName":"SMITH","SearchCriteria":{"MinPossibleMatchCount":"3","SearchAll":"N","Country":["USA","USA"],"Region":["A","A"]}},"ServiceProvDBA":"XYZ FINANCIAL SERVICE"},"AcquirerId":"1996"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/fraud/merchant/v3/add-merchant',
        headers=headers,
        json=add_terminated_merchant_request_schema,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

