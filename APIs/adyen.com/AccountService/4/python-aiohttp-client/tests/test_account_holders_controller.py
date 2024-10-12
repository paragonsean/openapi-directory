# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.close_account_holder_request import CloseAccountHolderRequest
from openapi_server.models.close_account_holder_response import CloseAccountHolderResponse
from openapi_server.models.create_account_holder_request import CreateAccountHolderRequest
from openapi_server.models.create_account_holder_response import CreateAccountHolderResponse
from openapi_server.models.get_account_holder_request import GetAccountHolderRequest
from openapi_server.models.get_account_holder_response import GetAccountHolderResponse
from openapi_server.models.get_account_holder_status_response import GetAccountHolderStatusResponse
from openapi_server.models.get_tax_form_request import GetTaxFormRequest
from openapi_server.models.get_tax_form_response import GetTaxFormResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.suspend_account_holder_request import SuspendAccountHolderRequest
from openapi_server.models.suspend_account_holder_response import SuspendAccountHolderResponse
from openapi_server.models.un_suspend_account_holder_request import UnSuspendAccountHolderRequest
from openapi_server.models.un_suspend_account_holder_response import UnSuspendAccountHolderResponse
from openapi_server.models.update_account_holder_request import UpdateAccountHolderRequest
from openapi_server.models.update_account_holder_response import UpdateAccountHolderResponse
from openapi_server.models.update_account_holder_state_request import UpdateAccountHolderStateRequest


pytestmark = pytest.mark.asyncio

async def test_post_close_account_holder(client):
    """Test case for post_close_account_holder

    Close an account holder
    """
    body = {"accountHolderCode":"accountHolderCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v4/closeAccountHolder',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_create_account_holder(client):
    """Test case for post_create_account_holder

    Create an account holder
    """
    body = {"createDefaultAccount":True,"accountHolderCode":"accountHolderCode","accountHolderDetails":{"metadata":{"key":"metadata"},"principalBusinessAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"bankAccountDetails":[{"BankAccountDetail":{"ownerNationality":"ownerNationality","ownerPostalCode":"ownerPostalCode","ownerCountryCode":"ownerCountryCode","bankName":"bankName","ownerState":"ownerState","bankAccountUUID":"bankAccountUUID","ownerName":"ownerName","bankBicSwift":"bankBicSwift","countryCode":"countryCode","ownerDateOfBirth":"ownerDateOfBirth","ownerStreet":"ownerStreet","bankAccountName":"bankAccountName","ownerHouseNumberOrName":"ownerHouseNumberOrName","bankCode":"bankCode","accountType":"accountType","accountNumber":"accountNumber","primaryAccount":True,"bankCity":"bankCity","checkCode":"checkCode","branchCode":"branchCode","taxId":"taxId","iban":"iban","ownerCity":"ownerCity","urlForVerification":"urlForVerification","currencyCode":"currencyCode"}},{"BankAccountDetail":{"ownerNationality":"ownerNationality","ownerPostalCode":"ownerPostalCode","ownerCountryCode":"ownerCountryCode","bankName":"bankName","ownerState":"ownerState","bankAccountUUID":"bankAccountUUID","ownerName":"ownerName","bankBicSwift":"bankBicSwift","countryCode":"countryCode","ownerDateOfBirth":"ownerDateOfBirth","ownerStreet":"ownerStreet","bankAccountName":"bankAccountName","ownerHouseNumberOrName":"ownerHouseNumberOrName","bankCode":"bankCode","accountType":"accountType","accountNumber":"accountNumber","primaryAccount":True,"bankCity":"bankCity","checkCode":"checkCode","branchCode":"branchCode","taxId":"taxId","iban":"iban","ownerCity":"ownerCity","urlForVerification":"urlForVerification","currencyCode":"currencyCode"}}],"individualDetails":{"personalData":{"nationality":"nationality","dateOfBirth":"dateOfBirth","documentData":[{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}},{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}}],"idNumber":"idNumber"},"name":{"firstName":"firstName","lastName":"lastName","gender":"MALE","infix":"infix"}},"lastReviewDate":"lastReviewDate","webAddress":"webAddress","merchantCategoryCode":"merchantCategoryCode","fullPhoneNumber":"fullPhoneNumber","businessDetails":{"signatories":[{"SignatoryContact":{"signatoryReference":"signatoryReference","address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"phoneNumber":{"phoneType":"Fax","phoneNumber":"phoneNumber","phoneCountryCode":"phoneCountryCode"},"signatoryCode":"signatoryCode","webAddress":"webAddress","jobTitle":"jobTitle","personalData":{"nationality":"nationality","dateOfBirth":"dateOfBirth","documentData":[{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}},{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}}],"idNumber":"idNumber"},"fullPhoneNumber":"fullPhoneNumber","name":{"firstName":"firstName","lastName":"lastName","gender":"MALE","infix":"infix"},"email":"email"}},{"SignatoryContact":{"signatoryReference":"signatoryReference","address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"phoneNumber":{"phoneType":"Fax","phoneNumber":"phoneNumber","phoneCountryCode":"phoneCountryCode"},"signatoryCode":"signatoryCode","webAddress":"webAddress","jobTitle":"jobTitle","personalData":{"nationality":"nationality","dateOfBirth":"dateOfBirth","documentData":[{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}},{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}}],"idNumber":"idNumber"},"fullPhoneNumber":"fullPhoneNumber","name":{"firstName":"firstName","lastName":"lastName","gender":"MALE","infix":"infix"},"email":"email"}}],"shareholders":[{"ShareholderContact":{"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"phoneNumber":{"phoneType":"Fax","phoneNumber":"phoneNumber","phoneCountryCode":"phoneCountryCode"},"webAddress":"webAddress","jobTitle":"jobTitle","personalData":{"nationality":"nationality","dateOfBirth":"dateOfBirth","documentData":[{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}},{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}}],"idNumber":"idNumber"},"fullPhoneNumber":"fullPhoneNumber","name":{"firstName":"firstName","lastName":"lastName","gender":"MALE","infix":"infix"},"shareholderType":"Controller","email":"email","shareholderCode":"shareholderCode"}},{"ShareholderContact":{"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"phoneNumber":{"phoneType":"Fax","phoneNumber":"phoneNumber","phoneCountryCode":"phoneCountryCode"},"webAddress":"webAddress","jobTitle":"jobTitle","personalData":{"nationality":"nationality","dateOfBirth":"dateOfBirth","documentData":[{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}},{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}}],"idNumber":"idNumber"},"fullPhoneNumber":"fullPhoneNumber","name":{"firstName":"firstName","lastName":"lastName","gender":"MALE","infix":"infix"},"shareholderType":"Controller","email":"email","shareholderCode":"shareholderCode"}}],"doingBusinessAs":"doingBusinessAs","registrationNumber":"registrationNumber","taxId":"taxId","listedUltimateParentCompany":[{"UltimateParentCompany":{"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"businessDetails":{"stockExchange":"stockExchange","stockNumber":"stockNumber","registrationNumber":"registrationNumber","legalBusinessName":"legalBusinessName","stockTicker":"stockTicker"},"ultimateParentCompanyCode":"ultimateParentCompanyCode"}},{"UltimateParentCompany":{"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"businessDetails":{"stockExchange":"stockExchange","stockNumber":"stockNumber","registrationNumber":"registrationNumber","legalBusinessName":"legalBusinessName","stockTicker":"stockTicker"},"ultimateParentCompanyCode":"ultimateParentCompanyCode"}}],"legalBusinessName":"legalBusinessName"},"email":"email"},"description":"description","processingTier":0,"primaryCurrency":"primaryCurrency","legalEntity":"Business"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v4/createAccountHolder',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_get_account_holder(client):
    """Test case for post_get_account_holder

    Get an account holder
    """
    body = {"accountCode":"accountCode","accountHolderCode":"accountHolderCode","showDetails":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v4/getAccountHolder',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_get_tax_form(client):
    """Test case for post_get_tax_form

    Get a tax form
    """
    body = {"accountHolderCode":"accountHolderCode","formType":"formType","year":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v4/getTaxForm',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_suspend_account_holder(client):
    """Test case for post_suspend_account_holder

    Suspend an account holder
    """
    body = {"accountHolderCode":"accountHolderCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v4/suspendAccountHolder',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_un_suspend_account_holder(client):
    """Test case for post_un_suspend_account_holder

    Unsuspend an account holder
    """
    body = {"accountHolderCode":"accountHolderCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v4/unSuspendAccountHolder',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_update_account_holder(client):
    """Test case for post_update_account_holder

    Update an account holder
    """
    body = {"accountHolderCode":"accountHolderCode","accountHolderDetails":{"metadata":{"key":"metadata"},"principalBusinessAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"bankAccountDetails":[{"BankAccountDetail":{"ownerNationality":"ownerNationality","ownerPostalCode":"ownerPostalCode","ownerCountryCode":"ownerCountryCode","bankName":"bankName","ownerState":"ownerState","bankAccountUUID":"bankAccountUUID","ownerName":"ownerName","bankBicSwift":"bankBicSwift","countryCode":"countryCode","ownerDateOfBirth":"ownerDateOfBirth","ownerStreet":"ownerStreet","bankAccountName":"bankAccountName","ownerHouseNumberOrName":"ownerHouseNumberOrName","bankCode":"bankCode","accountType":"accountType","accountNumber":"accountNumber","primaryAccount":True,"bankCity":"bankCity","checkCode":"checkCode","branchCode":"branchCode","taxId":"taxId","iban":"iban","ownerCity":"ownerCity","urlForVerification":"urlForVerification","currencyCode":"currencyCode"}},{"BankAccountDetail":{"ownerNationality":"ownerNationality","ownerPostalCode":"ownerPostalCode","ownerCountryCode":"ownerCountryCode","bankName":"bankName","ownerState":"ownerState","bankAccountUUID":"bankAccountUUID","ownerName":"ownerName","bankBicSwift":"bankBicSwift","countryCode":"countryCode","ownerDateOfBirth":"ownerDateOfBirth","ownerStreet":"ownerStreet","bankAccountName":"bankAccountName","ownerHouseNumberOrName":"ownerHouseNumberOrName","bankCode":"bankCode","accountType":"accountType","accountNumber":"accountNumber","primaryAccount":True,"bankCity":"bankCity","checkCode":"checkCode","branchCode":"branchCode","taxId":"taxId","iban":"iban","ownerCity":"ownerCity","urlForVerification":"urlForVerification","currencyCode":"currencyCode"}}],"individualDetails":{"personalData":{"nationality":"nationality","dateOfBirth":"dateOfBirth","documentData":[{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}},{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}}],"idNumber":"idNumber"},"name":{"firstName":"firstName","lastName":"lastName","gender":"MALE","infix":"infix"}},"lastReviewDate":"lastReviewDate","webAddress":"webAddress","merchantCategoryCode":"merchantCategoryCode","fullPhoneNumber":"fullPhoneNumber","businessDetails":{"signatories":[{"SignatoryContact":{"signatoryReference":"signatoryReference","address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"phoneNumber":{"phoneType":"Fax","phoneNumber":"phoneNumber","phoneCountryCode":"phoneCountryCode"},"signatoryCode":"signatoryCode","webAddress":"webAddress","jobTitle":"jobTitle","personalData":{"nationality":"nationality","dateOfBirth":"dateOfBirth","documentData":[{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}},{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}}],"idNumber":"idNumber"},"fullPhoneNumber":"fullPhoneNumber","name":{"firstName":"firstName","lastName":"lastName","gender":"MALE","infix":"infix"},"email":"email"}},{"SignatoryContact":{"signatoryReference":"signatoryReference","address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"phoneNumber":{"phoneType":"Fax","phoneNumber":"phoneNumber","phoneCountryCode":"phoneCountryCode"},"signatoryCode":"signatoryCode","webAddress":"webAddress","jobTitle":"jobTitle","personalData":{"nationality":"nationality","dateOfBirth":"dateOfBirth","documentData":[{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}},{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}}],"idNumber":"idNumber"},"fullPhoneNumber":"fullPhoneNumber","name":{"firstName":"firstName","lastName":"lastName","gender":"MALE","infix":"infix"},"email":"email"}}],"shareholders":[{"ShareholderContact":{"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"phoneNumber":{"phoneType":"Fax","phoneNumber":"phoneNumber","phoneCountryCode":"phoneCountryCode"},"webAddress":"webAddress","jobTitle":"jobTitle","personalData":{"nationality":"nationality","dateOfBirth":"dateOfBirth","documentData":[{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}},{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}}],"idNumber":"idNumber"},"fullPhoneNumber":"fullPhoneNumber","name":{"firstName":"firstName","lastName":"lastName","gender":"MALE","infix":"infix"},"shareholderType":"Controller","email":"email","shareholderCode":"shareholderCode"}},{"ShareholderContact":{"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"phoneNumber":{"phoneType":"Fax","phoneNumber":"phoneNumber","phoneCountryCode":"phoneCountryCode"},"webAddress":"webAddress","jobTitle":"jobTitle","personalData":{"nationality":"nationality","dateOfBirth":"dateOfBirth","documentData":[{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}},{"PersonalDocumentData":{"issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","type":"DRIVINGLICENSE","expirationDate":"expirationDate"}}],"idNumber":"idNumber"},"fullPhoneNumber":"fullPhoneNumber","name":{"firstName":"firstName","lastName":"lastName","gender":"MALE","infix":"infix"},"shareholderType":"Controller","email":"email","shareholderCode":"shareholderCode"}}],"doingBusinessAs":"doingBusinessAs","registrationNumber":"registrationNumber","taxId":"taxId","listedUltimateParentCompany":[{"UltimateParentCompany":{"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"businessDetails":{"stockExchange":"stockExchange","stockNumber":"stockNumber","registrationNumber":"registrationNumber","legalBusinessName":"legalBusinessName","stockTicker":"stockTicker"},"ultimateParentCompanyCode":"ultimateParentCompanyCode"}},{"UltimateParentCompany":{"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"businessDetails":{"stockExchange":"stockExchange","stockNumber":"stockNumber","registrationNumber":"registrationNumber","legalBusinessName":"legalBusinessName","stockTicker":"stockTicker"},"ultimateParentCompanyCode":"ultimateParentCompanyCode"}}],"legalBusinessName":"legalBusinessName"},"email":"email"},"description":"description","processingTier":0,"primaryCurrency":"primaryCurrency"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v4/updateAccountHolder',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_update_account_holder_state(client):
    """Test case for post_update_account_holder_state

    Update payout or processing state
    """
    body = {"reason":"reason","accountHolderCode":"accountHolderCode","disable":True,"stateType":"LimitedPayout"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v4/updateAccountHolderState',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

