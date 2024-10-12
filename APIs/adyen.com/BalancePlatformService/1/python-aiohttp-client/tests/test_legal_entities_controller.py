# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.legal_entity import LegalEntity
from openapi_server.models.legal_entity_info import LegalEntityInfo
from openapi_server.models.legal_entity_info_required_type import LegalEntityInfoRequiredType
from openapi_server.models.service_error import ServiceError


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
        path='/bcl/v1/legalEntities/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_legal_entities_id(client):
    """Test case for patch_legal_entities_id

    Update a legal entity
    """
    body = {"reference":"reference","capabilities":{"key":{"requested":True,"verificationStatus":"verificationStatus","allowed":True,"allowedSettings":{"authorizedCardUsers":True,"interval":"daily","fundingSource":["credit","credit"],"maxAmount":{"currency":"currency","value":5},"amountPerIndustry":{"key":{"currency":"currency","value":5}}},"allowedLevel":"high","requestedLevel":"high","requestedSettings":{"authorizedCardUsers":True,"interval":"daily","fundingSource":["credit","credit"],"maxAmount":{"currency":"currency","value":5},"amountPerIndustry":{"key":{"currency":"currency","value":5}}},"transferInstruments":[{"requested":True,"verificationStatus":"verificationStatus","allowed":True,"id":"id"},{"requested":True,"verificationStatus":"verificationStatus","allowed":True,"id":"id"}],"problems":[null,null]}},"individual":{"identificationData":{"expiryDate":"expiryDate","issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","nationalIdExempt":True,"type":"bankStatement","cardNumber":"cardNumber"},"nationality":"nationality","phone":{"number":"number","countryCode":"countryCode","type":"type"},"residentialAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"name":{"firstName":"firstName","lastName":"lastName","infix":"infix"},"birthData":{"dateOfBirth":"dateOfBirth"},"webData":{"webAddressId":"webAddressId","webAddress":"webAddress"},"email":"email"},"organization":{"taxExempt":True,"description":"description","type":"associationIncorporated","stockData":{"stockNumber":"stockNumber","tickerSymbol":"tickerSymbol","marketIdentifier":"marketIdentifier"},"legalName":"legalName","registeredAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"doingBusinessAs":"doingBusinessAs","phone":{"number":"number","countryCode":"countryCode","type":"type"},"registrationNumber":"registrationNumber","taxId":"taxId","taxIdAbsenceReason":"industryExemption","webData":{"webAddressId":"webAddressId","webAddress":"webAddress"},"principalPlaceOfBusiness":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"email":"email"},"entityAssociations":[{"associatorId":"associatorId","legalEntityId":"legalEntityId","entityType":"entityType","jobTitle":"jobTitle","name":"name","type":"signatory"},{"associatorId":"associatorId","legalEntityId":"legalEntityId","entityType":"entityType","jobTitle":"jobTitle","name":"name","type":"signatory"}],"type":"individual"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/bcl/v1/legalEntities/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_legal_entities(client):
    """Test case for post_legal_entities

    Create a legal entity
    """
    body = {"reference":"reference","capabilities":{"key":{"requested":True,"verificationStatus":"verificationStatus","allowed":True,"allowedSettings":{"authorizedCardUsers":True,"interval":"daily","fundingSource":["credit","credit"],"maxAmount":{"currency":"currency","value":5},"amountPerIndustry":{"key":{"currency":"currency","value":5}}},"allowedLevel":"high","requestedLevel":"high","requestedSettings":{"authorizedCardUsers":True,"interval":"daily","fundingSource":["credit","credit"],"maxAmount":{"currency":"currency","value":5},"amountPerIndustry":{"key":{"currency":"currency","value":5}}},"transferInstruments":[{"requested":True,"verificationStatus":"verificationStatus","allowed":True,"id":"id"},{"requested":True,"verificationStatus":"verificationStatus","allowed":True,"id":"id"}],"problems":[null,null]}},"individual":{"identificationData":{"expiryDate":"expiryDate","issuerCountry":"issuerCountry","issuerState":"issuerState","number":"number","nationalIdExempt":True,"type":"bankStatement","cardNumber":"cardNumber"},"nationality":"nationality","phone":{"number":"number","countryCode":"countryCode","type":"type"},"residentialAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"name":{"firstName":"firstName","lastName":"lastName","infix":"infix"},"birthData":{"dateOfBirth":"dateOfBirth"},"webData":{"webAddressId":"webAddressId","webAddress":"webAddress"},"email":"email"},"organization":{"taxExempt":True,"description":"description","type":"associationIncorporated","stockData":{"stockNumber":"stockNumber","tickerSymbol":"tickerSymbol","marketIdentifier":"marketIdentifier"},"legalName":"legalName","registeredAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"doingBusinessAs":"doingBusinessAs","phone":{"number":"number","countryCode":"countryCode","type":"type"},"registrationNumber":"registrationNumber","taxId":"taxId","taxIdAbsenceReason":"industryExemption","webData":{"webAddressId":"webAddressId","webAddress":"webAddress"},"principalPlaceOfBusiness":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","street":"street","postalCode":"postalCode","street2":"street2"},"email":"email"},"entityAssociations":[{"associatorId":"associatorId","legalEntityId":"legalEntityId","entityType":"entityType","jobTitle":"jobTitle","name":"name","type":"signatory"},{"associatorId":"associatorId","legalEntityId":"legalEntityId","entityType":"entityType","jobTitle":"jobTitle","name":"name","type":"signatory"}],"type":"individual"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bcl/v1/legalEntities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

