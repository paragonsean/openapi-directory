from typing import List, Dict
from aiohttp import web

from openapi_server.models.education_expense_model import EducationExpenseModel
from openapi_server.models.education_expense_with_id_model import EducationExpenseWithIdModel
from openapi_server.models.education_expenses_model import EducationExpensesModel
from openapi_server.models.education_goal_model import EducationGoalModel
from openapi_server.models.education_goal_with_id_model import EducationGoalWithIdModel
from openapi_server.models.education_goals_model import EducationGoalsModel
from openapi_server import util


async def education_goals_delete_by_educationgoalid_id(request: web.Request, education_goal_id, id) -> web.Response:
    """education_goals_delete_by_educationgoalid_id

    Description: The operation removes an Education Goal Expense tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Education Goal Expense from a Fact Finder.

    :param education_goal_id: The Education Goal ID used to locate the Goal to delete the Expense under
    :type education_goal_id: int
    :param id: The Education Goal Expense ID used to identify which Education Goal Expense to remove
    :type id: int

    """
    return web.Response(status=200)


async def education_goals_delete_by_id(request: web.Request, id) -> web.Response:
    """education_goals_delete_by_id

    Description: The operation removes an Education Goal tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Education Goal from a Fact Finder.

    :param id: The Education Goal ID used to identify which Education Goal to remove
    :type id: int

    """
    return web.Response(status=200)


async def education_goals_get_by_id(request: web.Request, id) -> web.Response:
    """education_goals_get_by_id

    Description: This operation retrieves a single Education Goal for the specified Education Goal ID.&lt;br /&gt;                Purpose: Provides access to the Education Goal including description and projected cost.

    :param id: The ID of the Education Goal used to retreive the Education Goal
    :type id: int

    """
    return web.Response(status=200)


async def education_goals_get_education_expense_by_educationgoalid_id(request: web.Request, education_goal_id, id) -> web.Response:
    """education_goals_get_education_expense_by_educationgoalid_id

    Description: This operation retrieves a single Education Goal Expense for the specified Education Goal Expense ID.&lt;br /&gt;                Purpose: Provides access to the Education Goal Expense including description and annual cost.

    :param education_goal_id: The ID of the Education Goal used to retrieve Education Goal Expenses
    :type education_goal_id: int
    :param id: The ID of the Education Goal Expense used to retreive the Education Goal Expense
    :type id: int

    """
    return web.Response(status=200)


async def education_goals_get_education_expenses_by_education_goal_id_by_educationgoalid(request: web.Request, education_goal_id) -> web.Response:
    """education_goals_get_education_expenses_by_education_goal_id_by_educationgoalid

    Description: This operation retrieves all Education Goal Expenses for the specified Education Goal ID.&lt;br /&gt;                Purpose: Provides access to the Education Goal Expenses including description and annual cost.

    :param education_goal_id: The ID of the Education Goal used to retrieve Education Goal Expenses
    :type education_goal_id: int

    """
    return web.Response(status=200)


async def education_goals_get_education_goals_by_fact_finder_id_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """education_goals_get_education_goals_by_fact_finder_id_by_factfinderid

    Description: This operation retrieves all Education Goals for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Education Goals including description and projected cost.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Education Goals
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def education_goals_post_by_educationgoalid_model(request: web.Request, education_goal_id, model) -> web.Response:
    """education_goals_post_by_educationgoalid_model

    Description: The operation creates an Education Goal Expense.&lt;br /&gt;                Purpose: Allows for creation of Education Goal Expenses on a Fact Finder.

    :param education_goal_id: The Education Goal ID used to locate the Goal to add the expense to
    :type education_goal_id: int
    :param model: The Education Goal Expense to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = EducationExpenseModel.from_dict(model)
    return web.Response(status=200)


async def education_goals_post_by_model(request: web.Request, model) -> web.Response:
    """education_goals_post_by_model

    Description: The operation creates an Education Goal.&lt;br /&gt;                Purpose: Allows for creation of Education Goals on a Fact Finder.

    :param model: The Education Goal to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = EducationGoalModel.from_dict(model)
    return web.Response(status=200)


async def education_goals_put_by_educationgoalid_id_model(request: web.Request, education_goal_id, id, model) -> web.Response:
    """education_goals_put_by_educationgoalid_id_model

    Description: The operation updates an Education Goal Expense.&lt;br /&gt;                Purpose: Allows for complete replacement of an Education Goal Expense on a Fact Finder.

    :param education_goal_id: The Education Goal ID used to locate the Goal to update the Expense under
    :type education_goal_id: int
    :param id: The existing Education Goal Expense ID used to identify which Education Goal Expense to update
    :type id: int
    :param model: The Education Goal Expense to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = EducationExpenseModel.from_dict(model)
    return web.Response(status=200)


async def education_goals_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """education_goals_put_by_id_model

    Description: The operation creates an Education Goal Expense.&lt;br /&gt;                Purpose: Allows for creation of Education Goal Expenses on a Fact Finder.

    :param id: The Education Goal ID used to locate the Goal to add the Expense to
    :type id: int
    :param model: The Education Goal Expense to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = EducationGoalModel.from_dict(model)
    return web.Response(status=200)
