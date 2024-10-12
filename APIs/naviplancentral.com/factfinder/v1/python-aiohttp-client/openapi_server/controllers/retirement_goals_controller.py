from typing import List, Dict
from aiohttp import web

from openapi_server.models.retirement_expense_model import RetirementExpenseModel
from openapi_server.models.retirement_expense_with_id_model import RetirementExpenseWithIdModel
from openapi_server.models.retirement_expenses_model import RetirementExpensesModel
from openapi_server.models.retirement_goal_model import RetirementGoalModel
from openapi_server.models.retirement_goal_with_id_model import RetirementGoalWithIdModel
from openapi_server.models.retirement_goals_model import RetirementGoalsModel
from openapi_server import util


async def retirement_goals_delete_by_id(request: web.Request, id) -> web.Response:
    """retirement_goals_delete_by_id

    Description: The operation removes a Retirement Goal tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Retirement Goal from a Fact Finder.

    :param id: The Retirement Goal ID used to identify which Retirement Goal to remove
    :type id: int

    """
    return web.Response(status=200)


async def retirement_goals_delete_by_retirementgoalid_id(request: web.Request, retirement_goal_id, id) -> web.Response:
    """retirement_goals_delete_by_retirementgoalid_id

    Description: The operation removes a Retirement Goal Expense tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Retirement Goal Expense from a Fact Finder.

    :param retirement_goal_id: The Retirement Goal ID used to locate the Goal to delete the Retirement Goal Expense under
    :type retirement_goal_id: int
    :param id: The Retirement Goal Expense ID used to identify which Retirement Goal Expense to remove
    :type id: int

    """
    return web.Response(status=200)


async def retirement_goals_get_by_id(request: web.Request, id) -> web.Response:
    """retirement_goals_get_by_id

    Description: This operation retrieves a single Retirement Goal for the specified Retirement Goal ID.&lt;br /&gt;                Purpose: Provides access to the Retirement Goal including retirement date.

    :param id: The ID of the Retirement Goal used to retreive the Retirement Goal
    :type id: int

    """
    return web.Response(status=200)


async def retirement_goals_get_retirement_expense_by_retirementgoalid_id(request: web.Request, retirement_goal_id, id) -> web.Response:
    """retirement_goals_get_retirement_expense_by_retirementgoalid_id

    Description: This operation retrieves a single Retirement Goal Expense for the specified Retirement Goal Expense ID.&lt;br /&gt;                Purpose: Provides access to the Retirement Goal Expense including description and amount.

    :param retirement_goal_id: The ID of the Retirement Goal used to retrieve the Retirement Goal Expense
    :type retirement_goal_id: int
    :param id: The ID of the Retirement Goal Expense used to retreive the Retirement Goal Expense
    :type id: int

    """
    return web.Response(status=200)


async def retirement_goals_get_retirement_expenses_by_retirement_goal_id_by_retirementgoalid(request: web.Request, retirement_goal_id) -> web.Response:
    """retirement_goals_get_retirement_expenses_by_retirement_goal_id_by_retirementgoalid

    Description: This operation retrieves all Retirement Goal Expenses for the specified Retirement Goal ID.&lt;br /&gt;                Purpose: Provides access to the Retirement Goal Expenses including description and amount.

    :param retirement_goal_id: The ID of the Retirement Goal used to retrieve Retirement Goal Expenses
    :type retirement_goal_id: int

    """
    return web.Response(status=200)


async def retirement_goals_get_retirement_goals_by_fact_finder_id_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """retirement_goals_get_retirement_goals_by_fact_finder_id_by_factfinderid

    Description: This operation retrieves all Retirement Goals for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Retirement Goals including retirement date.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Retirement Goals
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def retirement_goals_post_by_model(request: web.Request, model) -> web.Response:
    """retirement_goals_post_by_model

    Description: The operation creates a Retirement Goal.&lt;br /&gt;                Purpose: Allows for creation of Retirement Goals on a Fact Finder.

    :param model: The Retirement Goal to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = RetirementGoalModel.from_dict(model)
    return web.Response(status=200)


async def retirement_goals_post_by_retirementgoalid_model(request: web.Request, retirement_goal_id, model) -> web.Response:
    """retirement_goals_post_by_retirementgoalid_model

    Description: The operation creates a Retirement Goal Expense.&lt;br /&gt;                Purpose: Allows for creation of Retirement Goal Expenses on a Fact Finder.

    :param retirement_goal_id: The ID of the Retirement Goal to add the Retirement Goal Expense to
    :type retirement_goal_id: int
    :param model: The Retirement Goal Expense to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = RetirementExpenseModel.from_dict(model)
    return web.Response(status=200)


async def retirement_goals_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """retirement_goals_put_by_id_model

    Description: The operation updates a Retirement Goal.&lt;br /&gt;                Purpose: Allows for complete replacement of a Retirement Goal on a Fact Finder.

    :param id: The existing Retirement Goal ID used to identify which Retirement Goal to update
    :type id: int
    :param model: The Retirement Goal to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = RetirementGoalModel.from_dict(model)
    return web.Response(status=200)


async def retirement_goals_put_by_retirementgoalid_id_model(request: web.Request, retirement_goal_id, id, model) -> web.Response:
    """retirement_goals_put_by_retirementgoalid_id_model

    Description: The operation updates a Retirement Goal Expense.&lt;br /&gt;                Purpose: Allows for complete replacement of a Retirement Goal Expense on a Fact Finder.

    :param retirement_goal_id: The Retirement Goal ID used to locate the Goal to update the Retirement Goal Expense under
    :type retirement_goal_id: int
    :param id: The existing Retirement Goal Expense ID used to identify which Retirement Goal Expense to update
    :type id: int
    :param model: The Retirement Goal Expense to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = RetirementExpenseModel.from_dict(model)
    return web.Response(status=200)
