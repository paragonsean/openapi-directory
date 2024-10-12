from typing import List, Dict
from aiohttp import web

from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_what_are_my_options_model import AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel
from openapi_server.models.advicent_navi_plan_rest_api_goals_models_goal_funding_list_model import AdvicentNaviPlanRestApiGoalsModelsGoalFundingListModel
from openapi_server.models.advicent_navi_plan_rest_api_goals_models_live_goal_base_model import AdvicentNaviPlanRestApiGoalsModelsLiveGoalBaseModel
from openapi_server.models.advicent_navi_plan_rest_api_net_worth_models_account_base_model import AdvicentNaviPlanRestApiNetWorthModelsAccountBaseModel
from openapi_server.models.advicent_navi_plan_rest_api_net_worth_models_liability_base_model import AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel
from openapi_server.models.advicent_navi_plan_rest_api_net_worth_models_lifestyle_asset_base_model import AdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel
from openapi_server.models.advicent_navi_plan_rest_api_net_worth_models_real_estate_base_model import AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel
from openapi_server.models.advicent_navi_plan_rest_api_projections_models_needs_vs_abilities_projections_model import AdvicentNaviPlanRestApiProjectionsModelsNeedsVsAbilitiesProjectionsModel
from openapi_server.models.advicent_navi_plan_rest_api_projections_models_net_worth_projections_model import AdvicentNaviPlanRestApiProjectionsModelsNetWorthProjectionsModel
from openapi_server import util


async def live_plan_get_accounts_by_clientid_planid(request: web.Request, plan_id, client_id=None) -> web.Response:
    """Retrieves accounts for a given plan

    

    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)


async def live_plan_get_goal_funding_list_by_clientid_planid(request: web.Request, plan_id, client_id=None) -> web.Response:
    """Retrieve a list of funding accounts

    This function retrieves a list of funding accounts for the goals in the plan

    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)


async def live_plan_get_goals_by_clientid_planid(request: web.Request, plan_id, client_id=None) -> web.Response:
    """Retrieves all goals from the live plan

    

    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)


async def live_plan_get_liabilities_by_clientid_planid(request: web.Request, plan_id, client_id=None) -> web.Response:
    """Retrieves liabilities for a given plan

    

    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)


async def live_plan_get_lifestyle_assets_by_clientid_planid(request: web.Request, plan_id, client_id=None) -> web.Response:
    """Retrieves lifestyle assets for a given plan

    

    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)


async def live_plan_get_projected_needs_vs_abilities_by_id_clientid_planid(request: web.Request, id, plan_id, client_id=None) -> web.Response:
    """Retrieves needs vs abilities projections

    

    :param id: 
    :type id: int
    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)


async def live_plan_get_projected_net_worth_by_clientid_planid(request: web.Request, plan_id, client_id=None) -> web.Response:
    """Retrieves net worth projections

    

    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)


async def live_plan_get_real_estate_assets_by_clientid_planid(request: web.Request, plan_id, client_id=None) -> web.Response:
    """Retrieves real estate accounts for a given plan

    

    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)


async def live_plan_get_what_are_my_options_by_id_clientid_planid(request: web.Request, id, plan_id, client_id=None) -> web.Response:
    """Retrieve WAMO values for a given goal

    This function retrieves the WAMO values for the specified goal

    :param id: The id of the goal
    :type id: int
    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)
