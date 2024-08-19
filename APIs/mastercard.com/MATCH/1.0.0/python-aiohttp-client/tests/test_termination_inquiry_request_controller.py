# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.termination_inquiry_request_schema import TerminationInquiryRequestSchema
from openapi_server.models.termination_inquiry_schema import TerminationInquirySchema


pytestmark = pytest.mark.asyncio

async def test_fraud_merchant_v3_termination_inquiry_post(client):
    """Test case for fraud_merchant_v3_termination_inquiry_post

    Returns information on merchants that have been terminated and merchants that have inquired upon. Provides the acquiring bank with information, such as, if a Merchant or individual has been terminated by another acquirer already, the reason for termination, the history of fraudulent or risky business practices that led to that termination and the inquiry that was made already on the Merchant or individual by own or another acquiring bank (if opted).
    """
    termination_inquiry_request = {"TerminationInquiryRequest":{"Merchant":{"DoingBusinessAsName":"BAIT R US","UrlGroup":[{"CloseMatchUrls":[{"Url":["WWW.SHOESHOP.COM","WWW.SHOESHOP.COM"]},{"Url":["WWW.SHOESHOP.COM","WWW.SHOESHOP.COM"]}],"NoMatchUrls":{"Url":["WWW.SHOESHOP.COM","WWW.SHOESHOP.COM"]},"ExactMatchUrls":[{"Url":["WWW.SHOESHOP.COM","WWW.SHOESHOP.COM"]},{"Url":["WWW.SHOESHOP.COM","WWW.SHOESHOP.COM"]}]},{"CloseMatchUrls":[{"Url":["WWW.SHOESHOP.COM","WWW.SHOESHOP.COM"]},{"Url":["WWW.SHOESHOP.COM","WWW.SHOESHOP.COM"]}],"NoMatchUrls":{"Url":["WWW.SHOESHOP.COM","WWW.SHOESHOP.COM"]},"ExactMatchUrls":[{"Url":["WWW.SHOESHOP.COM","WWW.SHOESHOP.COM"]},{"Url":["WWW.SHOESHOP.COM","WWW.SHOESHOP.COM"]}]}],"Address":{"Country":"USA","PostalCode":"66579","CountrySubdivision":"IL","City":"DALLAS","Line1":"42 ELM AVENUE","Line2":"SUITE 201","Province":""},"AltPhoneNumber":"3165557625","NationalTaxId":"888596927","AddedByAcquirerID":"1234","AddedOnDate":"10/13/2015","SearchCriteria":{"MinPossibleMatchCount":"3","SearchAll":"N","Country":["USA","USA"],"Region":["A","A"]},"Url":"WWW.TESTMERCHANT.COM","Name":"THE BAIT SHOP","CountrySubdivisionTaxId":"492321030","PhoneNumber":"3165557625","ServiceProvLegal":"XYZ FINANCIAL SERVICE INCORPORATED","TerminationReasonCode":"13","Principal":[{"Address":{"Country":"USA","PostalCode":"66579","CountrySubdivision":"IL","City":"DALLAS","Line1":"42 ELM AVENUE","Line2":"SUITE 201","Province":""},"MiddleInitial":"P","FirstName":"DAVID","NationalId":"541022104","PhoneNumber":"3165557625","AltPhoneNumber":"3165557625","DriversLicense":{"Number":"M15698025","Country":"USA","CountrySubdivision":"IL"},"LastName":"SMITH","SearchCriteria":{"MinPossibleMatchCount":"3","SearchAll":"N","Country":["USA","USA"],"Region":["A","A"]}},{"Address":{"Country":"USA","PostalCode":"66579","CountrySubdivision":"IL","City":"DALLAS","Line1":"42 ELM AVENUE","Line2":"SUITE 201","Province":""},"MiddleInitial":"P","FirstName":"DAVID","NationalId":"541022104","PhoneNumber":"3165557625","AltPhoneNumber":"3165557625","DriversLicense":{"Number":"M15698025","Country":"USA","CountrySubdivision":"IL"},"LastName":"SMITH","SearchCriteria":{"MinPossibleMatchCount":"3","SearchAll":"N","Country":["USA","USA"],"Region":["A","A"]}}],"ServiceProvDBA":"XYZ FINANCIAL SERVICE"},"AcquirerId":"1996","TransactionReferenceNumber":"12345"}}
    params = [('PageOffset', 0),
                    ('PageLength', 10)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/fraud/merchant/v3/termination-inquiry',
        headers=headers,
        json=termination_inquiry_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

