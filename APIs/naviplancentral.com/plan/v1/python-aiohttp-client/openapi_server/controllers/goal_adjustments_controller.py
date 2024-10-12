from typing import List, Dict
from aiohttp import web

from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_coverage_projections_result_model_advicent_domain_logic_goal_what_if_education_goal_adjustments import AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_coverage_projections_result_model_advicent_domain_logic_goal_what_if_major_purchase_goal_adjustments import AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_coverage_projections_result_model_advicent_domain_logic_goal_what_if_retirement_goal_adjustments import AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_education_goal_adjustments_model import AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_goal_adjustments_model_advicent_domain_logic_goal_what_if_education_goal_adjustments import AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_goal_adjustments_model_advicent_domain_logic_goal_what_if_major_purchase_goal_adjustments import AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_goal_adjustments_model_advicent_domain_logic_goal_what_if_retirement_goal_adjustments import AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_goal_success_rate_results_model import AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateResultsModel
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_major_purchase_goal_adjustments_model import AdvicentNaviPlanRestApiGoalAdjustmentsModelsMajorPurchaseGoalAdjustmentsModel
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_restrictions_result_model import AdvicentNaviPlanRestApiGoalAdjustmentsModelsRestrictionsResultModel
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_retirement_goal_adjustments_model import AdvicentNaviPlanRestApiGoalAdjustmentsModelsRetirementGoalAdjustmentsModel
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_what_are_my_options_model import AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel
from openapi_server import util


async def goal_adjustments_get_education_by_id_clientid_planid(request: web.Request, id, plan_id, client_id=None) -> web.Response:
    """Retrieve the adjustments

    This function retrieves a goal and the adjustments made to it

    :param id: The id of the goal to retrieve adjustments for.
    :type id: int
    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)


async def goal_adjustments_get_goal_adjustment_restrictions_by_clientid_planid(request: web.Request, plan_id, client_id=None) -> web.Response:
    """Returns a list of goal adjustment restrictions.

    This function returns a list of adjustment restrictions for all goals.

    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)


async def goal_adjustments_get_goal_success_rates_by_clientid_planid(request: web.Request, plan_id, client_id=None) -> web.Response:
    """Returns a list of goals with their relevant success rates.

    

    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)


async def goal_adjustments_get_major_purchase_by_id_clientid_planid(request: web.Request, id, plan_id, client_id=None) -> web.Response:
    """Retrieve the adjustments

    This function retrieves a goal and the adjustments made to it

    :param id: The id of the goal to retrieve adjustments for.
    :type id: int
    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)


async def goal_adjustments_get_retirement_by_clientid_planid(request: web.Request, plan_id, client_id=None) -> web.Response:
    """Retrieve the adjustments

    This function retrieves a goal and the adjustments made to it for a particular client

    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)


async def goal_adjustments_get_what_are_my_options_by_id_clientid_planid(request: web.Request, id, plan_id, client_id=None) -> web.Response:
    """Returns WAMO values for current goal

    

    :param id: The id of the goal to retrieve WAMO values for.
    :type id: int
    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param client_id: Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    :type client_id: str

    """
    return web.Response(status=200)


async def goal_adjustments_post_education_by_id_goaladjustments_planid(request: web.Request, id, plan_id, goal_adjustments) -> web.Response:
    """Perform calculations

    This function returns the posted object and the adjusted calculation values

    :param id: The id of the goal to retrieve adjustments for.
    :type id: int
    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param goal_adjustments: The adjusted values for this goal
    :type goal_adjustments: dict | bytes

    """
    goal_adjustments = AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments.from_dict(goal_adjustments)
    return web.Response(status=200)


async def goal_adjustments_post_major_purchase_by_id_goaladjustments_planid(request: web.Request, id, plan_id, goal_adjustments) -> web.Response:
    """Perform calculations

    This function returns the posted object and the adjusted calculation values

    :param id: The id of the goal to retrieve adjustments for.
    :type id: int
    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param goal_adjustments: The adjusted values for this goal
    :type goal_adjustments: dict | bytes

    """
    goal_adjustments = AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments.from_dict(goal_adjustments)
    return web.Response(status=200)


async def goal_adjustments_post_retirement_by_goaladjustments_planid(request: web.Request, plan_id, goal_adjustments) -> web.Response:
    """Perform calculations

    This function returns the posted object and the adjusted calculation values

    :param plan_id: Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    :type plan_id: str
    :param goal_adjustments: The adjusted values for this goal
    :type goal_adjustments: dict | bytes

    """
    goal_adjustments = AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments.from_dict(goal_adjustments)
    return web.Response(status=200)
