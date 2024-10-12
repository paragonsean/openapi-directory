# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.generic_class import GenericClass
from openapi_server.models.generic_class_list_response import GenericClassListResponse


pytestmark = pytest.mark.asyncio

async def test_walletobjects_genericclass_get(client):
    """Test case for walletobjects_genericclass_get

    
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
        path='/walletobjects/v1/genericClass/{resource_id}'.format(resource_id='resource_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_walletobjects_genericclass_insert(client):
    """Test case for walletobjects_genericclass_insert

    
    """
    body = {"linksModuleData":{"uris":[{"kind":"kind","description":"description","id":"id","localizedDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"uri":"uri"},{"kind":"kind","description":"description","id":"id","localizedDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"uri":"uri"}]},"viewUnlockRequirement":"VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED","classTemplateInfo":{"cardTemplateOverride":{"cardRowTemplateInfos":[{"oneItem":{"item":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},"threeItems":{"endItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"middleItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"startItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},"twoItems":{"endItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"startItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}}},{"oneItem":{"item":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},"threeItems":{"endItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"middleItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"startItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},"twoItems":{"endItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"startItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}}}]},"detailsTemplateOverride":{"detailsItemInfos":[{"item":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},{"item":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}}]},"cardBarcodeSectionDetails":{"secondTopDetail":{"fieldSelector":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]}},"firstBottomDetail":{"fieldSelector":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]}},"firstTopDetail":{"fieldSelector":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]}}},"listTemplateOverride":{"secondRowOption":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"firstRowOption":{"fieldOption":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"transitOption":"TRANSIT_OPTION_UNSPECIFIED"},"thirdRowOption":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]}}},"multipleDevicesAndHoldersAllowedStatus":"STATUS_UNSPECIFIED","securityAnimation":{"animationType":"ANIMATION_UNSPECIFIED"},"textModulesData":[{"localizedBody":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"localizedHeader":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"header":"header","id":"id","body":"body"},{"localizedBody":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"localizedHeader":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"header":"header","id":"id","body":"body"}],"callbackOptions":{"updateRequestUrl":"updateRequestUrl","url":"url"},"redemptionIssuers":["redemptionIssuers","redemptionIssuers"],"id":"id","imageModulesData":[{"mainImage":{"contentDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"sourceUri":{"description":"description","localizedDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"uri":"uri"},"kind":"kind"},"id":"id"},{"mainImage":{"contentDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"sourceUri":{"description":"description","localizedDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"uri":"uri"},"kind":"kind"},"id":"id"}],"enableSmartTap":True}
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
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/walletobjects/v1/genericClass',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_walletobjects_genericclass_list(client):
    """Test case for walletobjects_genericclass_list

    
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
                    ('issuerId', 'issuer_id_example'),
                    ('maxResults', 56),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/walletobjects/v1/genericClass',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_walletobjects_genericclass_patch(client):
    """Test case for walletobjects_genericclass_patch

    
    """
    body = {"linksModuleData":{"uris":[{"kind":"kind","description":"description","id":"id","localizedDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"uri":"uri"},{"kind":"kind","description":"description","id":"id","localizedDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"uri":"uri"}]},"viewUnlockRequirement":"VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED","classTemplateInfo":{"cardTemplateOverride":{"cardRowTemplateInfos":[{"oneItem":{"item":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},"threeItems":{"endItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"middleItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"startItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},"twoItems":{"endItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"startItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}}},{"oneItem":{"item":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},"threeItems":{"endItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"middleItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"startItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},"twoItems":{"endItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"startItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}}}]},"detailsTemplateOverride":{"detailsItemInfos":[{"item":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},{"item":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}}]},"cardBarcodeSectionDetails":{"secondTopDetail":{"fieldSelector":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]}},"firstBottomDetail":{"fieldSelector":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]}},"firstTopDetail":{"fieldSelector":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]}}},"listTemplateOverride":{"secondRowOption":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"firstRowOption":{"fieldOption":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"transitOption":"TRANSIT_OPTION_UNSPECIFIED"},"thirdRowOption":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]}}},"multipleDevicesAndHoldersAllowedStatus":"STATUS_UNSPECIFIED","securityAnimation":{"animationType":"ANIMATION_UNSPECIFIED"},"textModulesData":[{"localizedBody":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"localizedHeader":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"header":"header","id":"id","body":"body"},{"localizedBody":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"localizedHeader":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"header":"header","id":"id","body":"body"}],"callbackOptions":{"updateRequestUrl":"updateRequestUrl","url":"url"},"redemptionIssuers":["redemptionIssuers","redemptionIssuers"],"id":"id","imageModulesData":[{"mainImage":{"contentDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"sourceUri":{"description":"description","localizedDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"uri":"uri"},"kind":"kind"},"id":"id"},{"mainImage":{"contentDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"sourceUri":{"description":"description","localizedDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"uri":"uri"},"kind":"kind"},"id":"id"}],"enableSmartTap":True}
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
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/walletobjects/v1/genericClass/{resource_id}'.format(resource_id='resource_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_walletobjects_genericclass_update(client):
    """Test case for walletobjects_genericclass_update

    
    """
    body = {"linksModuleData":{"uris":[{"kind":"kind","description":"description","id":"id","localizedDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"uri":"uri"},{"kind":"kind","description":"description","id":"id","localizedDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"uri":"uri"}]},"viewUnlockRequirement":"VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED","classTemplateInfo":{"cardTemplateOverride":{"cardRowTemplateInfos":[{"oneItem":{"item":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},"threeItems":{"endItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"middleItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"startItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},"twoItems":{"endItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"startItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}}},{"oneItem":{"item":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},"threeItems":{"endItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"middleItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"startItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},"twoItems":{"endItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"},"startItem":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}}}]},"detailsTemplateOverride":{"detailsItemInfos":[{"item":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}},{"item":{"firstValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"secondValue":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"predefinedItem":"PREDEFINED_ITEM_UNSPECIFIED"}}]},"cardBarcodeSectionDetails":{"secondTopDetail":{"fieldSelector":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]}},"firstBottomDetail":{"fieldSelector":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]}},"firstTopDetail":{"fieldSelector":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]}}},"listTemplateOverride":{"secondRowOption":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"firstRowOption":{"fieldOption":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]},"transitOption":"TRANSIT_OPTION_UNSPECIFIED"},"thirdRowOption":{"fields":[{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"},{"dateFormat":"DATE_FORMAT_UNSPECIFIED","fieldPath":"fieldPath"}]}}},"multipleDevicesAndHoldersAllowedStatus":"STATUS_UNSPECIFIED","securityAnimation":{"animationType":"ANIMATION_UNSPECIFIED"},"textModulesData":[{"localizedBody":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"localizedHeader":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"header":"header","id":"id","body":"body"},{"localizedBody":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"localizedHeader":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"header":"header","id":"id","body":"body"}],"callbackOptions":{"updateRequestUrl":"updateRequestUrl","url":"url"},"redemptionIssuers":["redemptionIssuers","redemptionIssuers"],"id":"id","imageModulesData":[{"mainImage":{"contentDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"sourceUri":{"description":"description","localizedDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"uri":"uri"},"kind":"kind"},"id":"id"},{"mainImage":{"contentDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"sourceUri":{"description":"description","localizedDescription":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"uri":"uri"},"kind":"kind"},"id":"id"}],"enableSmartTap":True}
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
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/walletobjects/v1/genericClass/{resource_id}'.format(resource_id='resource_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

