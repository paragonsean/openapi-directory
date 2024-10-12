from typing import List, Dict
from aiohttp import web

from openapi_server.models.group_v2_get_user_clan_invite_setting200_response import GroupV2GetUserClanInviteSetting200Response
from openapi_server.models.tokens_get_bungie_rewards_list200_response import TokensGetBungieRewardsList200Response
from openapi_server.models.tokens_get_partner_offer_sku_history200_response import TokensGetPartnerOfferSkuHistory200Response
from openapi_server.models.tokens_get_partner_reward_history200_response import TokensGetPartnerRewardHistory200Response
from openapi_server import util


async def tokens_apply_missing_partner_offers_without_claim(request: web.Request, partner_application_id, target_bnet_membership_id) -> web.Response:
    """tokens_apply_missing_partner_offers_without_claim

    Apply a partner offer to the targeted user. This endpoint does not claim a new offer, but any already claimed offers will be applied to the game if not already.

    :param partner_application_id: The partner application identifier.
    :type partner_application_id: int
    :param target_bnet_membership_id: The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
    :type target_bnet_membership_id: int

    """
    return web.Response(status=200)


async def tokens_claim_partner_offer(request: web.Request, ) -> web.Response:
    """tokens_claim_partner_offer

    Claim a partner offer as the authenticated user.


    """
    return web.Response(status=200)


async def tokens_force_drops_repair(request: web.Request, ) -> web.Response:
    """tokens_force_drops_repair

    Twitch Drops self-repair function - scans twitch for drops not marked as fulfilled and resyncs them.


    """
    return web.Response(status=200)


async def tokens_get_bungie_rewards_for_platform_user(request: web.Request, membership_id, membership_type) -> web.Response:
    """tokens_get_bungie_rewards_for_platform_user

    Returns the bungie rewards for the targeted user when a platform membership Id and Type are used.

    :param membership_id: users platform membershipId for requested user rewards. If not self, elevated permissions are required.
    :type membership_id: int
    :param membership_type: The target Destiny 2 membership type.
    :type membership_type: int

    """
    return web.Response(status=200)


async def tokens_get_bungie_rewards_for_user(request: web.Request, membership_id) -> web.Response:
    """tokens_get_bungie_rewards_for_user

    Returns the bungie rewards for the targeted user.

    :param membership_id: bungie.net user membershipId for requested user rewards. If not self, elevated permissions are required.
    :type membership_id: int

    """
    return web.Response(status=200)


async def tokens_get_bungie_rewards_list(request: web.Request, ) -> web.Response:
    """tokens_get_bungie_rewards_list

    Returns a list of the current bungie rewards


    """
    return web.Response(status=200)


async def tokens_get_partner_offer_sku_history(request: web.Request, partner_application_id, target_bnet_membership_id) -> web.Response:
    """tokens_get_partner_offer_sku_history

    Returns the partner sku and offer history of the targeted user. Elevated permissions are required to see users that are not yourself.

    :param partner_application_id: The partner application identifier.
    :type partner_application_id: int
    :param target_bnet_membership_id: The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
    :type target_bnet_membership_id: int

    """
    return web.Response(status=200)


async def tokens_get_partner_reward_history(request: web.Request, partner_application_id, target_bnet_membership_id) -> web.Response:
    """tokens_get_partner_reward_history

    Returns the partner rewards history of the targeted user, both partner offers and Twitch drops.

    :param partner_application_id: The partner application identifier.
    :type partner_application_id: int
    :param target_bnet_membership_id: The bungie.net user to return reward history for.
    :type target_bnet_membership_id: int

    """
    return web.Response(status=200)
