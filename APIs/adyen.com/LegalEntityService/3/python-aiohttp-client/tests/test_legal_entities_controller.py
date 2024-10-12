# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.business_lines import BusinessLines
from openapi_server.models.data_review_confirmation_response import DataReviewConfirmationResponse
from openapi_server.models.legal_entity import LegalEntity
from openapi_server.models.legal_entity_info import LegalEntityInfo
from openapi_server.models.legal_entity_info_required_type import LegalEntityInfoRequiredType
from openapi_server.models.service_error import ServiceError
from openapi_server.models.verification_errors import VerificationErrors


pytestmark = pytest.mark.asyncio

async def test_get_legal_entities_id(client):
    """Test case for get_legal_entities_id

    Get a legal entity
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/lem/v3/legalEntities/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_legal_entities_id_business_lines(client):
    """Test case for get_legal_entities_id_business_lines

    Get all business lines under a legal entity
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/lem/v3/legalEntities/{id}/businessLines'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_legal_entities_id(client):
    """Test case for patch_legal_entities_id

    Update a legal entity
    """
    body = {"reference":"reference","trust":{"description":"description","taxInformation":[{"country":"country","number":"number","type":"type"},{"country":"country","number":"number","type":"type"}],"type":"cashManagementTrust","vatAbsenceReason":"industryExemption","countryOfGoverningLaw":"countryOfGoverningLaw","dateOfIncorporation":"dateOfIncorporation","registeredAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"doingBusinessAs":"doingBusinessAs","registrationNumber":"registrationNumber","name":"name","principalPlaceOfBusiness":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"undefinedBeneficiaryInfo":[{"reference":"reference","description":"description"},{"reference":"reference","description":"description"}],"vatNumber":"vatNumber"},"unincorporatedPartnership":{"dateOfIncorporation":"dateOfIncorporation","registeredAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"doingBusinessAs":"doingBusinessAs","registrationNumber":"registrationNumber","name":"name","description":"description","principalPlaceOfBusiness":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"taxInformation":[{"country":"country","number":"number","type":"type"},{"country":"country","number":"number","type":"type"}],"type":"limitedPartnership","vatAbsenceReason":"industryExemption","countryOfGoverningLaw":"countryOfGoverningLaw","vatNumber":"vatNumber"},"soleProprietorship":{"dateOfIncorporation":"dateOfIncorporation","registeredAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"doingBusinessAs":"doingBusinessAs","registrationNumber":"registrationNumber","name":"name","description":"description","principalPlaceOfBusiness":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"taxInformation":[{"country":"country","number":"number","type":"type"},{"country":"country","number":"number","type":"type"}],"vatAbsenceReason":"industryExemption","countryOfGoverningLaw":"countryOfGoverningLaw","vatNumber":"vatNumber"},"capabilities":{"key":{"requested":True,"verificationStatus":"verificationStatus","allowed":True,"allowedSettings":{"authorizedCardUsers":True,"interval":"daily","fundingSource":["credit","credit"],"maxAmount":{"currency":"currency","value":0},"amountPerIndustry":{"key":{"currency":"currency","value":0}}},"allowedLevel":"high","requestedLevel":"high","requestedSettings":{"authorizedCardUsers":True,"interval":"daily","fundingSource":["credit","credit"],"maxAmount":{"currency":"currency","value":0},"amountPerIndustry":{"key":{"currency":"currency","value":0}}},"transferInstruments":[{"requested":True,"verificationStatus":"verificationStatus","allowed":True,"id":"id"},{"requested":True,"verificationStatus":"verificationStatus","allowed":True,"id":"id"}]}},"individual":{"identificationData":{"expiryDate":"expiryDate","issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","nationalIdExempt":True,"type":"nationalIdNumber","cardNumber":"cardNumber"},"nationality":"nationality","phone":{"number":"number","type":"type"},"residentialAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"name":{"firstName":"firstName","lastName":"lastName","infix":"infix"},"birthData":{"dateOfBirth":"dateOfBirth"},"webData":{"webAddressId":"webAddressId","webAddress":"webAddress"},"taxInformation":[{"country":"country","number":"number","type":"type"},{"country":"country","number":"number","type":"type"}],"email":"email"},"organization":{"taxReportingClassification":{"financialInstitutionNumber":"financialInstitutionNumber","mainSourceOfIncome":"businessOperation","businessType":"other","type":"nonFinancialNonReportable"},"description":"description","taxInformation":[{"country":"country","number":"number","type":"type"},{"country":"country","number":"number","type":"type"}],"type":"associationIncorporated","stockData":{"stockNumber":"stockNumber","tickerSymbol":"tickerSymbol","marketIdentifier":"marketIdentifier"},"vatAbsenceReason":"industryExemption","legalName":"legalName","dateOfIncorporation":"dateOfIncorporation","registeredAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"doingBusinessAs":"doingBusinessAs","phone":{"number":"number","type":"type"},"registrationNumber":"registrationNumber","webData":{"webAddressId":"webAddressId","webAddress":"webAddress"},"principalPlaceOfBusiness":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"email":"email","vatNumber":"vatNumber"},"verificationPlan":"verificationPlan","entityAssociations":[{"associatorId":"associatorId","legalEntityId":"legalEntityId","entityType":"entityType","jobTitle":"jobTitle","name":"name","type":"definedBeneficiary","settlorExemptionReason":["settlorExemptionReason","settlorExemptionReason"]},{"associatorId":"associatorId","legalEntityId":"legalEntityId","entityType":"entityType","jobTitle":"jobTitle","name":"name","type":"definedBeneficiary","settlorExemptionReason":["settlorExemptionReason","settlorExemptionReason"]}],"type":"individual"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_requested_verification_code': '1',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/lem/v3/legalEntities/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_legal_entities(client):
    """Test case for post_legal_entities

    Create a legal entity
    """
    body = {"reference":"reference","trust":{"description":"description","taxInformation":[{"country":"country","number":"number","type":"type"},{"country":"country","number":"number","type":"type"}],"type":"cashManagementTrust","vatAbsenceReason":"industryExemption","countryOfGoverningLaw":"countryOfGoverningLaw","dateOfIncorporation":"dateOfIncorporation","registeredAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"doingBusinessAs":"doingBusinessAs","registrationNumber":"registrationNumber","name":"name","principalPlaceOfBusiness":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"undefinedBeneficiaryInfo":[{"reference":"reference","description":"description"},{"reference":"reference","description":"description"}],"vatNumber":"vatNumber"},"unincorporatedPartnership":{"dateOfIncorporation":"dateOfIncorporation","registeredAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"doingBusinessAs":"doingBusinessAs","registrationNumber":"registrationNumber","name":"name","description":"description","principalPlaceOfBusiness":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"taxInformation":[{"country":"country","number":"number","type":"type"},{"country":"country","number":"number","type":"type"}],"type":"limitedPartnership","vatAbsenceReason":"industryExemption","countryOfGoverningLaw":"countryOfGoverningLaw","vatNumber":"vatNumber"},"soleProprietorship":{"dateOfIncorporation":"dateOfIncorporation","registeredAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"doingBusinessAs":"doingBusinessAs","registrationNumber":"registrationNumber","name":"name","description":"description","principalPlaceOfBusiness":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"taxInformation":[{"country":"country","number":"number","type":"type"},{"country":"country","number":"number","type":"type"}],"vatAbsenceReason":"industryExemption","countryOfGoverningLaw":"countryOfGoverningLaw","vatNumber":"vatNumber"},"capabilities":{"key":{"requested":True,"verificationStatus":"verificationStatus","allowed":True,"allowedSettings":{"authorizedCardUsers":True,"interval":"daily","fundingSource":["credit","credit"],"maxAmount":{"currency":"currency","value":0},"amountPerIndustry":{"key":{"currency":"currency","value":0}}},"allowedLevel":"high","requestedLevel":"high","requestedSettings":{"authorizedCardUsers":True,"interval":"daily","fundingSource":["credit","credit"],"maxAmount":{"currency":"currency","value":0},"amountPerIndustry":{"key":{"currency":"currency","value":0}}},"transferInstruments":[{"requested":True,"verificationStatus":"verificationStatus","allowed":True,"id":"id"},{"requested":True,"verificationStatus":"verificationStatus","allowed":True,"id":"id"}]}},"individual":{"identificationData":{"expiryDate":"expiryDate","issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","nationalIdExempt":True,"type":"nationalIdNumber","cardNumber":"cardNumber"},"nationality":"nationality","phone":{"number":"number","type":"type"},"residentialAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"name":{"firstName":"firstName","lastName":"lastName","infix":"infix"},"birthData":{"dateOfBirth":"dateOfBirth"},"webData":{"webAddressId":"webAddressId","webAddress":"webAddress"},"taxInformation":[{"country":"country","number":"number","type":"type"},{"country":"country","number":"number","type":"type"}],"email":"email"},"organization":{"taxReportingClassification":{"financialInstitutionNumber":"financialInstitutionNumber","mainSourceOfIncome":"businessOperation","businessType":"other","type":"nonFinancialNonReportable"},"description":"description","taxInformation":[{"country":"country","number":"number","type":"type"},{"country":"country","number":"number","type":"type"}],"type":"associationIncorporated","stockData":{"stockNumber":"stockNumber","tickerSymbol":"tickerSymbol","marketIdentifier":"marketIdentifier"},"vatAbsenceReason":"industryExemption","legalName":"legalName","dateOfIncorporation":"dateOfIncorporation","registeredAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"doingBusinessAs":"doingBusinessAs","phone":{"number":"number","type":"type"},"registrationNumber":"registrationNumber","webData":{"webAddressId":"webAddressId","webAddress":"webAddress"},"principalPlaceOfBusiness":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"email":"email","vatNumber":"vatNumber"},"verificationPlan":"verificationPlan","entityAssociations":[{"associatorId":"associatorId","legalEntityId":"legalEntityId","entityType":"entityType","jobTitle":"jobTitle","name":"name","type":"definedBeneficiary","settlorExemptionReason":["settlorExemptionReason","settlorExemptionReason"]},{"associatorId":"associatorId","legalEntityId":"legalEntityId","entityType":"entityType","jobTitle":"jobTitle","name":"name","type":"definedBeneficiary","settlorExemptionReason":["settlorExemptionReason","settlorExemptionReason"]}],"type":"individual"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_requested_verification_code': '13004',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/lem/v3/legalEntities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_legal_entities_id_check_verification_errors(client):
    """Test case for post_legal_entities_id_check_verification_errors

    Check a legal entity's verification errors
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/lem/v3/legalEntities/{id}/checkVerificationErrors'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_legal_entities_id_confirm_data_review(client):
    """Test case for post_legal_entities_id_confirm_data_review

    Confirm data review
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/lem/v3/legalEntities/{id}/confirmDataReview'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

