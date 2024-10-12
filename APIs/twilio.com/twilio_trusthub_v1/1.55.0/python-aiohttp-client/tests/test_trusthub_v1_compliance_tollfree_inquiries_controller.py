# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.compliance_tollfree_inquiry_enum_opt_in_type import ComplianceTollfreeInquiryEnumOptInType
from openapi_server.models.trusthub_v1_compliance_tollfree_inquiry import TrusthubV1ComplianceTollfreeInquiry


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_compliance_tollfree_inquiry(client):
    """Test case for create_compliance_tollfree_inquiry

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'additional_information': 'additional_information_example',
        'business_city': 'business_city_example',
        'business_contact_email': 'business_contact_email_example',
        'business_contact_first_name': 'business_contact_first_name_example',
        'business_contact_last_name': 'business_contact_last_name_example',
        'business_contact_phone': 'business_contact_phone_example',
        'business_country': 'business_country_example',
        'business_name': 'business_name_example',
        'business_postal_code': 'business_postal_code_example',
        'business_state_province_region': 'business_state_province_region_example',
        'business_street_address': 'business_street_address_example',
        'business_street_address2': 'business_street_address2_example',
        'business_website': 'business_website_example',
        'message_volume': 'message_volume_example',
        'notification_email': 'notification_email_example',
        'opt_in_image_urls': ['opt_in_image_urls_example'],
        'opt_in_type': openapi_server.ComplianceTollfreeInquiryEnumOptInType(),
        'production_message_sample': 'production_message_sample_example',
        'tollfree_phone_number': 'tollfree_phone_number_example',
        'use_case_categories': ['use_case_categories_example'],
        'use_case_summary': 'use_case_summary_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/ComplianceInquiries/Tollfree/Initialize',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

