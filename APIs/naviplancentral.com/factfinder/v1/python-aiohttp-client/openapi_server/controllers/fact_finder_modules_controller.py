from typing import List, Dict
from aiohttp import web

from openapi_server.models.fact_finder_module_model import FactFinderModuleModel
from openapi_server.models.fact_finder_module_with_id_model import FactFinderModuleWithIdModel
from openapi_server.models.fact_finder_modules_model import FactFinderModulesModel
from openapi_server import util


async def fact_finder_modules_get_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """fact_finder_modules_get_by_factfinderid

    Description: This operation retrieves all Fact Finder Modules for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Fact Finder Modules including description and policy type.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Fact Finder Modules
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def fact_finder_modules_get_by_factfinderid_id(request: web.Request, fact_finder_id, id) -> web.Response:
    """fact_finder_modules_get_by_factfinderid_id

    Description: This operation retrieves a single Fact Finder Module for the specified Fact Finder Module ID.&lt;br /&gt;                Purpose: Provides access to the Fact Finder Module including description and policy type.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Fact Finder Module
    :type fact_finder_id: int
    :param id: The ID of the Fact Finder Module used to retreive the Fact Finder Module
    :type id: int

    """
    return web.Response(status=200)


async def fact_finder_modules_put_by_model_factfinderid_id(request: web.Request, fact_finder_id, id, model) -> web.Response:
    """fact_finder_modules_put_by_model_factfinderid_id

    Description: The operation updates a Fact Finder Module.&lt;br /&gt;                Purpose: Allows for complete replacement of a Fact Finder Module on a Fact Finder.

    :param fact_finder_id: The ID of the Fact Finder used to identify the Fact Finder Module to update
    :type fact_finder_id: int
    :param id: The existing Fact Finder Module ID used to identify which Fact Finder Module to update
    :type id: int
    :param model: The Fact Finder Module to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = FactFinderModuleModel.from_dict(model)
    return web.Response(status=200)
