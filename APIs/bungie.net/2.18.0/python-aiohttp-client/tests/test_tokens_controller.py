# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.group_v2_get_user_clan_invite_setting200_response import GroupV2GetUserClanInviteSetting200Response
from openapi_server.models.tokens_get_bungie_rewards_list200_response import TokensGetBungieRewardsList200Response
from openapi_server.models.tokens_get_partner_offer_sku_history200_response import TokensGetPartnerOfferSkuHistory200Response
from openapi_server.models.tokens_get_partner_reward_history200_response import TokensGetPartnerRewardHistory200Response


pytestmark = pytest.mark.asyncio

async def test_tokens_apply_missing_partner_offers_without_claim(client):
    """Test case for tokens_apply_missing_partner_offers_without_claim

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Tokens/Partner/ApplyMissingOffers/{partner_application_id}/{target_bnet_membership_id}'.format(partner_application_id=56, target_bnet_membership_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tokens_claim_partner_offer(client):
    """Test case for tokens_claim_partner_offer

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Tokens/Partner/ClaimOffer/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tokens_force_drops_repair(client):
    """Test case for tokens_force_drops_repair

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Tokens/Partner/ForceDropsRepair/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tokens_get_bungie_rewards_for_platform_user(client):
    """Test case for tokens_get_bungie_rewards_for_platform_user

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Tokens/Rewards/GetRewardsForPlatformUser/{membership_id}/{membership_type}'.format(membership_id=56, membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tokens_get_bungie_rewards_for_user(client):
    """Test case for tokens_get_bungie_rewards_for_user

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Tokens/Rewards/GetRewardsForUser/{membership_id}'.format(membership_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tokens_get_bungie_rewards_list(client):
    """Test case for tokens_get_bungie_rewards_list

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Tokens/Rewards/BungieRewards/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tokens_get_partner_offer_sku_history(client):
    """Test case for tokens_get_partner_offer_sku_history

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Tokens/Partner/History/{partner_application_id}/{target_bnet_membership_id}'.format(partner_application_id=56, target_bnet_membership_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tokens_get_partner_reward_history(client):
    """Test case for tokens_get_partner_reward_history

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Tokens/Partner/History/{target_bnet_membership_id}/Application/{partner_application_id}'.format(partner_application_id=56, target_bnet_membership_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

