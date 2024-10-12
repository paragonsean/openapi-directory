from typing import List, Dict
from aiohttp import web

from openapi_server.models.accumulate_loyalty_points_request import AccumulateLoyaltyPointsRequest
from openapi_server.models.accumulate_loyalty_points_response import AccumulateLoyaltyPointsResponse
from openapi_server.models.adjust_loyalty_points_request import AdjustLoyaltyPointsRequest
from openapi_server.models.adjust_loyalty_points_response import AdjustLoyaltyPointsResponse
from openapi_server.models.calculate_loyalty_points_request import CalculateLoyaltyPointsRequest
from openapi_server.models.calculate_loyalty_points_response import CalculateLoyaltyPointsResponse
from openapi_server.models.create_loyalty_account_request import CreateLoyaltyAccountRequest
from openapi_server.models.create_loyalty_account_response import CreateLoyaltyAccountResponse
from openapi_server.models.create_loyalty_reward_request import CreateLoyaltyRewardRequest
from openapi_server.models.create_loyalty_reward_response import CreateLoyaltyRewardResponse
from openapi_server.models.delete_loyalty_reward_response import DeleteLoyaltyRewardResponse
from openapi_server.models.list_loyalty_programs_response import ListLoyaltyProgramsResponse
from openapi_server.models.redeem_loyalty_reward_request import RedeemLoyaltyRewardRequest
from openapi_server.models.redeem_loyalty_reward_response import RedeemLoyaltyRewardResponse
from openapi_server.models.retrieve_loyalty_account_response import RetrieveLoyaltyAccountResponse
from openapi_server.models.retrieve_loyalty_program_response import RetrieveLoyaltyProgramResponse
from openapi_server.models.retrieve_loyalty_reward_response import RetrieveLoyaltyRewardResponse
from openapi_server.models.search_loyalty_accounts_request import SearchLoyaltyAccountsRequest
from openapi_server.models.search_loyalty_accounts_response import SearchLoyaltyAccountsResponse
from openapi_server.models.search_loyalty_events_request import SearchLoyaltyEventsRequest
from openapi_server.models.search_loyalty_events_response import SearchLoyaltyEventsResponse
from openapi_server.models.search_loyalty_rewards_request import SearchLoyaltyRewardsRequest
from openapi_server.models.search_loyalty_rewards_response import SearchLoyaltyRewardsResponse
from openapi_server import util


async def accumulate_loyalty_points(request: web.Request, account_id, body) -> web.Response:
    """AccumulateLoyaltyPoints

    Adds points to a loyalty account.  - If you are using the Orders API to manage orders, you only provide the &#x60;order_id&#x60;.  The endpoint reads the order to compute points to add to the buyer&#39;s account. - If you are not using the Orders API to manage orders,  you first perform a client-side computation to compute the points.   For spend-based and visit-based programs, you can first call  [CalculateLoyaltyPoints](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/calculate-loyalty-points) to compute the points   that you provide to this endpoint.   __Note:__ The country of the seller&#39;s Square account determines whether tax is included in the purchase amount when accruing points for spend-based and visit-based programs.  For more information, see [Availability of Square Loyalty](https://developer.squareup.com/docs/loyalty-api/overview#loyalty-market-availability).

    :param account_id: The [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) ID to which to add the points.
    :type account_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = AccumulateLoyaltyPointsRequest.from_dict(body)
    return web.Response(status=200)


async def adjust_loyalty_points(request: web.Request, account_id, body) -> web.Response:
    """AdjustLoyaltyPoints

    Adds points to or subtracts points from a buyer&#39;s account.   Use this endpoint only when you need to manually adjust points. Otherwise, in your application flow, you call  [AccumulateLoyaltyPoints](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/accumulate-loyalty-points)  to add points when a buyer pays for the purchase.

    :param account_id: The ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) in which to adjust the points.
    :type account_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = AdjustLoyaltyPointsRequest.from_dict(body)
    return web.Response(status=200)


async def calculate_loyalty_points(request: web.Request, program_id, body) -> web.Response:
    """CalculateLoyaltyPoints

    Calculates the points a purchase earns.  - If you are using the Orders API to manage orders, you provide &#x60;order_id&#x60; in the request. The  endpoint calculates the points by reading the order. - If you are not using the Orders API to manage orders, you provide the purchase amount in  the request for the endpoint to calculate the points.  An application might call this endpoint to show the points that a buyer can earn with the  specific purchase.  __Note:__ The country of the seller&#39;s Square account determines whether tax is included in the purchase amount when accruing points for spend-based and visit-based programs.  For more information, see [Availability of Square Loyalty](https://developer.squareup.com/docs/loyalty-api/overview#loyalty-market-availability).

    :param program_id: The [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram) ID, which defines the rules for accruing points.
    :type program_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CalculateLoyaltyPointsRequest.from_dict(body)
    return web.Response(status=200)


async def create_loyalty_account(request: web.Request, body) -> web.Response:
    """CreateLoyaltyAccount

    Creates a loyalty account. To create a loyalty account, you must provide the &#x60;program_id&#x60; and a &#x60;mapping&#x60; with the &#x60;phone_number&#x60; of the buyer.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateLoyaltyAccountRequest.from_dict(body)
    return web.Response(status=200)


async def create_loyalty_reward(request: web.Request, body) -> web.Response:
    """CreateLoyaltyReward

    Creates a loyalty reward. In the process, the endpoint does following:  - Uses the &#x60;reward_tier_id&#x60; in the request to determine the number of points  to lock for this reward.  - If the request includes &#x60;order_id&#x60;, it adds the reward and related discount to the order.   After a reward is created, the points are locked and  not available for the buyer to redeem another reward.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateLoyaltyRewardRequest.from_dict(body)
    return web.Response(status=200)


async def delete_loyalty_reward(request: web.Request, reward_id) -> web.Response:
    """DeleteLoyaltyReward

    Deletes a loyalty reward by doing the following:  - Returns the loyalty points back to the loyalty account. - If an order ID was specified when the reward was created  (see [CreateLoyaltyReward](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/create-loyalty-reward)),  it updates the order by removing the reward and related  discounts.  You cannot delete a reward that has reached the terminal state (REDEEMED).

    :param reward_id: The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to delete.
    :type reward_id: str

    """
    return web.Response(status=200)


async def list_loyalty_programs(request: web.Request, ) -> web.Response:
    """ListLoyaltyPrograms

    Returns a list of loyalty programs in the seller&#39;s account. Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).   Replaced with [RetrieveLoyaltyProgram](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/retrieve-loyalty-program) when used with the keyword &#x60;main&#x60;.


    """
    return web.Response(status=200)


async def redeem_loyalty_reward(request: web.Request, reward_id, body) -> web.Response:
    """RedeemLoyaltyReward

    Redeems a loyalty reward.  The endpoint sets the reward to the &#x60;REDEEMED&#x60; terminal state.   If you are using your own order processing system (not using the  Orders API), you call this endpoint after the buyer paid for the  purchase.  After the reward reaches the terminal state, it cannot be deleted.  In other words, points used for the reward cannot be returned  to the account.

    :param reward_id: The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to redeem.
    :type reward_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = RedeemLoyaltyRewardRequest.from_dict(body)
    return web.Response(status=200)


async def retrieve_loyalty_account(request: web.Request, account_id) -> web.Response:
    """RetrieveLoyaltyAccount

    Retrieves a loyalty account.

    :param account_id: The ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) to retrieve.
    :type account_id: str

    """
    return web.Response(status=200)


async def retrieve_loyalty_program(request: web.Request, program_id) -> web.Response:
    """RetrieveLoyaltyProgram

    Retrieves the loyalty program in a seller&#39;s account, specified by the program ID or the keyword &#x60;main&#x60;.   Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).

    :param program_id: The ID of the loyalty program or the keyword &#x60;main&#x60;. Either value can be used to retrieve the single loyalty program that belongs to the seller.
    :type program_id: str

    """
    return web.Response(status=200)


async def retrieve_loyalty_reward(request: web.Request, reward_id) -> web.Response:
    """RetrieveLoyaltyReward

    Retrieves a loyalty reward.

    :param reward_id: The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to retrieve.
    :type reward_id: str

    """
    return web.Response(status=200)


async def search_loyalty_accounts(request: web.Request, body) -> web.Response:
    """SearchLoyaltyAccounts

    Searches for loyalty accounts in a loyalty program.    You can search for a loyalty account using the phone number or customer ID associated with the account. To return all loyalty accounts, specify an empty &#x60;query&#x60; object or omit it entirely.    Search results are sorted by &#x60;created_at&#x60; in ascending order.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = SearchLoyaltyAccountsRequest.from_dict(body)
    return web.Response(status=200)


async def search_loyalty_events(request: web.Request, body) -> web.Response:
    """SearchLoyaltyEvents

    Searches for loyalty events.  A Square loyalty program maintains a ledger of events that occur during the lifetime of a  buyer&#39;s loyalty account. Each change in the point balance  (for example, points earned, points redeemed, and points expired) is  recorded in the ledger. Using this endpoint, you can search the ledger for events.  Search results are sorted by &#x60;created_at&#x60; in descending order.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = SearchLoyaltyEventsRequest.from_dict(body)
    return web.Response(status=200)


async def search_loyalty_rewards(request: web.Request, body) -> web.Response:
    """SearchLoyaltyRewards

    Searches for loyalty rewards in a loyalty account.   In the current implementation, the endpoint supports search by the reward &#x60;status&#x60;.  If you know a reward ID, use the  [RetrieveLoyaltyReward](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/retrieve-loyalty-reward) endpoint.  Search results are sorted by &#x60;updated_at&#x60; in descending order.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = SearchLoyaltyRewardsRequest.from_dict(body)
    return web.Response(status=200)
