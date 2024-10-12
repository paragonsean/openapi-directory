from typing import List, Dict
from aiohttp import web

from openapi_server.models.major_purchase_goal_model import MajorPurchaseGoalModel
from openapi_server.models.major_purchase_goal_with_id_model import MajorPurchaseGoalWithIdModel
from openapi_server.models.major_purchase_goals_model import MajorPurchaseGoalsModel
from openapi_server import util


async def major_purchase_goals_delete_by_id(request: web.Request, id) -> web.Response:
    """major_purchase_goals_delete_by_id

    Description: The operation removes a Major Purchase tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Major Purchase from a Fact Finder.

    :param id: The Major Purchase ID used to identify which Major Purchase to remove
    :type id: int

    """
    return web.Response(status=200)


async def major_purchase_goals_get_by_id(request: web.Request, id) -> web.Response:
    """major_purchase_goals_get_by_id

    Description: This operation retrieves a single Major Purchase for the specified Major Purchase ID.&lt;br /&gt;                Purpose: Provides access to the Major Purchase including description and amount.

    :param id: The ID of the Major Purchase used to retreive the Major Purchase
    :type id: int

    """
    return web.Response(status=200)


async def major_purchase_goals_get_major_purchase_goals_by_fact_finder_id_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """major_purchase_goals_get_major_purchase_goals_by_fact_finder_id_by_factfinderid

    Description: This operation retrieves all Major Purchases for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Major Purchases including description and amount.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Major Purchases
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def major_purchase_goals_post_by_model(request: web.Request, model) -> web.Response:
    """major_purchase_goals_post_by_model

    Description: The operation creates a Major Purchase.&lt;br /&gt;                Purpose: Allows for creation of Major Purchases on a Fact Finder.

    :param model: The Major Purchase to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = MajorPurchaseGoalModel.from_dict(model)
    return web.Response(status=200)


async def major_purchase_goals_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """major_purchase_goals_put_by_id_model

    Description: The operation updates a Major Purchase.&lt;br /&gt;                Purpose: Allows for complete replacement of a Major Purchase on a Fact Finder.

    :param id: The existing Major Purchase ID used to identify which Major Purchase to update
    :type id: int
    :param model: The Major Purchase to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = MajorPurchaseGoalModel.from_dict(model)
    return web.Response(status=200)
