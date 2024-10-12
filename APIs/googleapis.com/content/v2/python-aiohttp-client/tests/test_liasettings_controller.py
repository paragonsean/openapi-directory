# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.lia_settings import LiaSettings
from openapi_server.models.liasettings_custom_batch_request import LiasettingsCustomBatchRequest
from openapi_server.models.liasettings_custom_batch_response import LiasettingsCustomBatchResponse
from openapi_server.models.liasettings_get_accessible_gmb_accounts_response import LiasettingsGetAccessibleGmbAccountsResponse
from openapi_server.models.liasettings_list_pos_data_providers_response import LiasettingsListPosDataProvidersResponse
from openapi_server.models.liasettings_list_response import LiasettingsListResponse
from openapi_server.models.liasettings_request_gmb_access_response import LiasettingsRequestGmbAccessResponse
from openapi_server.models.liasettings_request_inventory_verification_response import LiasettingsRequestInventoryVerificationResponse
from openapi_server.models.liasettings_set_inventory_verification_contact_response import LiasettingsSetInventoryVerificationContactResponse
from openapi_server.models.liasettings_set_pos_data_provider_response import LiasettingsSetPosDataProviderResponse


pytestmark = pytest.mark.asyncio

async def test_content_liasettings_custombatch(client):
    """Test case for content_liasettings_custombatch

    
    """
    body = {"entries":[{"posExternalAccountId":"posExternalAccountId","accountId":"accountId","country":"country","liaSettings":{"accountId":"accountId","kind":"kind","countrySettings":[{"country":"country","hostedLocalStorefrontActive":True,"onDisplayToOrder":{"shippingCostPolicyUrl":"shippingCostPolicyUrl","status":"status"},"about":{"url":"url","status":"status"},"storePickupActive":True,"inventory":{"inventoryVerificationContactStatus":"inventoryVerificationContactStatus","inventoryVerificationContactEmail":"inventoryVerificationContactEmail","inventoryVerificationContactName":"inventoryVerificationContactName","status":"status"},"posDataProvider":{"posExternalAccountId":"posExternalAccountId","posDataProviderId":"posDataProviderId"}},{"country":"country","hostedLocalStorefrontActive":True,"onDisplayToOrder":{"shippingCostPolicyUrl":"shippingCostPolicyUrl","status":"status"},"about":{"url":"url","status":"status"},"storePickupActive":True,"inventory":{"inventoryVerificationContactStatus":"inventoryVerificationContactStatus","inventoryVerificationContactEmail":"inventoryVerificationContactEmail","inventoryVerificationContactName":"inventoryVerificationContactName","status":"status"},"posDataProvider":{"posExternalAccountId":"posExternalAccountId","posDataProviderId":"posDataProviderId"}}]},"method":"method","contactEmail":"contactEmail","merchantId":"merchantId","contactName":"contactName","posDataProviderId":"posDataProviderId","gmbEmail":"gmbEmail","batchId":0},{"posExternalAccountId":"posExternalAccountId","accountId":"accountId","country":"country","liaSettings":{"accountId":"accountId","kind":"kind","countrySettings":[{"country":"country","hostedLocalStorefrontActive":True,"onDisplayToOrder":{"shippingCostPolicyUrl":"shippingCostPolicyUrl","status":"status"},"about":{"url":"url","status":"status"},"storePickupActive":True,"inventory":{"inventoryVerificationContactStatus":"inventoryVerificationContactStatus","inventoryVerificationContactEmail":"inventoryVerificationContactEmail","inventoryVerificationContactName":"inventoryVerificationContactName","status":"status"},"posDataProvider":{"posExternalAccountId":"posExternalAccountId","posDataProviderId":"posDataProviderId"}},{"country":"country","hostedLocalStorefrontActive":True,"onDisplayToOrder":{"shippingCostPolicyUrl":"shippingCostPolicyUrl","status":"status"},"about":{"url":"url","status":"status"},"storePickupActive":True,"inventory":{"inventoryVerificationContactStatus":"inventoryVerificationContactStatus","inventoryVerificationContactEmail":"inventoryVerificationContactEmail","inventoryVerificationContactName":"inventoryVerificationContactName","status":"status"},"posDataProvider":{"posExternalAccountId":"posExternalAccountId","posDataProviderId":"posDataProviderId"}}]},"method":"method","contactEmail":"contactEmail","merchantId":"merchantId","contactName":"contactName","posDataProviderId":"posDataProviderId","gmbEmail":"gmbEmail","batchId":0}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('dryRun', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2/liasettings/batch',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_liasettings_get(client):
    """Test case for content_liasettings_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2/{merchant_id}/liasettings/{account_id}'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_liasettings_getaccessiblegmbaccounts(client):
    """Test case for content_liasettings_getaccessiblegmbaccounts

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2/{merchant_id}/liasettings/{account_id}/accessiblegmbaccounts'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_liasettings_list(client):
    """Test case for content_liasettings_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2/{merchant_id}/liasettings'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_liasettings_listposdataproviders(client):
    """Test case for content_liasettings_listposdataproviders

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2/liasettings/posdataproviders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_liasettings_requestgmbaccess(client):
    """Test case for content_liasettings_requestgmbaccess

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('gmbEmail', 'gmb_email_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2/{merchant_id}/liasettings/{account_id}/requestgmbaccess'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_liasettings_requestinventoryverification(client):
    """Test case for content_liasettings_requestinventoryverification

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2/{merchant_id}/liasettings/{account_id}/requestinventoryverification/{country}'.format(merchant_id='merchant_id_example', account_id='account_id_example', country='country_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_liasettings_setinventoryverificationcontact(client):
    """Test case for content_liasettings_setinventoryverificationcontact

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('country', 'country_example'),
                    ('language', 'language_example'),
                    ('contactName', 'contact_name_example'),
                    ('contactEmail', 'contact_email_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2/{merchant_id}/liasettings/{account_id}/setinventoryverificationcontact'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_liasettings_setposdataprovider(client):
    """Test case for content_liasettings_setposdataprovider

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('country', 'country_example'),
                    ('posDataProviderId', 'pos_data_provider_id_example'),
                    ('posExternalAccountId', 'pos_external_account_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2/{merchant_id}/liasettings/{account_id}/setposdataprovider'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_liasettings_update(client):
    """Test case for content_liasettings_update

    
    """
    body = {"accountId":"accountId","kind":"kind","countrySettings":[{"country":"country","hostedLocalStorefrontActive":True,"onDisplayToOrder":{"shippingCostPolicyUrl":"shippingCostPolicyUrl","status":"status"},"about":{"url":"url","status":"status"},"storePickupActive":True,"inventory":{"inventoryVerificationContactStatus":"inventoryVerificationContactStatus","inventoryVerificationContactEmail":"inventoryVerificationContactEmail","inventoryVerificationContactName":"inventoryVerificationContactName","status":"status"},"posDataProvider":{"posExternalAccountId":"posExternalAccountId","posDataProviderId":"posDataProviderId"}},{"country":"country","hostedLocalStorefrontActive":True,"onDisplayToOrder":{"shippingCostPolicyUrl":"shippingCostPolicyUrl","status":"status"},"about":{"url":"url","status":"status"},"storePickupActive":True,"inventory":{"inventoryVerificationContactStatus":"inventoryVerificationContactStatus","inventoryVerificationContactEmail":"inventoryVerificationContactEmail","inventoryVerificationContactName":"inventoryVerificationContactName","status":"status"},"posDataProvider":{"posExternalAccountId":"posExternalAccountId","posDataProviderId":"posDataProviderId"}}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('dryRun', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/content/v2/{merchant_id}/liasettings/{account_id}'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

