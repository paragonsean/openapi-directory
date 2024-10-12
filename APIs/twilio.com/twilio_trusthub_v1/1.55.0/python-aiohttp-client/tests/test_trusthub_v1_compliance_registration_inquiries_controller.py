# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.compliance_registration_enum_business_identity_type import ComplianceRegistrationEnumBusinessIdentityType
from openapi_server.models.compliance_registration_enum_business_registration_authority import ComplianceRegistrationEnumBusinessRegistrationAuthority
from openapi_server.models.compliance_registration_enum_end_user_type import ComplianceRegistrationEnumEndUserType
from openapi_server.models.compliance_registration_enum_phone_number_type import ComplianceRegistrationEnumPhoneNumberType
from openapi_server.models.trusthub_v1_compliance_registration import TrusthubV1ComplianceRegistration


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_compliance_registration(client):
    """Test case for create_compliance_registration

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'accepted_notification_receipt': True,
        'address_city': 'address_city_example',
        'address_country_code': 'address_country_code_example',
        'address_postal_code': 'address_postal_code_example',
        'address_street': 'address_street_example',
        'address_street_secondary': 'address_street_secondary_example',
        'address_subdivision': 'address_subdivision_example',
        'authorized_representative1_date_of_birth': 'authorized_representative1_date_of_birth_example',
        'authorized_representative1_email': 'authorized_representative1_email_example',
        'authorized_representative1_first_name': 'authorized_representative1_first_name_example',
        'authorized_representative1_last_name': 'authorized_representative1_last_name_example',
        'authorized_representative1_phone': 'authorized_representative1_phone_example',
        'business_identity_type': openapi_server.ComplianceRegistrationEnumBusinessIdentityType(),
        'business_legal_name': 'business_legal_name_example',
        'business_registration_authority': openapi_server.ComplianceRegistrationEnumBusinessRegistrationAuthority(),
        'business_registration_number': 'business_registration_number_example',
        'business_website_url': 'business_website_url_example',
        'date_of_birth': 'date_of_birth_example',
        'emergency_address_city': 'emergency_address_city_example',
        'emergency_address_country_code': 'emergency_address_country_code_example',
        'emergency_address_postal_code': 'emergency_address_postal_code_example',
        'emergency_address_street': 'emergency_address_street_example',
        'emergency_address_street_secondary': 'emergency_address_street_secondary_example',
        'emergency_address_subdivision': 'emergency_address_subdivision_example',
        'end_user_type': openapi_server.ComplianceRegistrationEnumEndUserType(),
        'file': 'file_example',
        'file_name': 'file_name_example',
        'first_name': 'first_name_example',
        'friendly_name': 'friendly_name_example',
        'individual_email': 'individual_email_example',
        'individual_phone': 'individual_phone_example',
        'is_isv_embed': True,
        'last_name': 'last_name_example',
        'notification_email': 'notification_email_example',
        'phone_number_type': openapi_server.ComplianceRegistrationEnumPhoneNumberType(),
        'use_address_as_emergency_address': True
        }
    response = await client.request(
        method='POST',
        path='/v1/ComplianceInquiries/Registration/RegulatoryCompliance/GB/Initialize',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

