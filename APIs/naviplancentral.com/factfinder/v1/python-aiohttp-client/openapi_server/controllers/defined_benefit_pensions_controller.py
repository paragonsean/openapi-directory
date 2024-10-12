from typing import List, Dict
from aiohttp import web

from openapi_server.models.defined_benefit_pension_model import DefinedBenefitPensionModel
from openapi_server.models.defined_benefit_pension_with_id_model import DefinedBenefitPensionWithIdModel
from openapi_server.models.defined_benefit_pensions_model import DefinedBenefitPensionsModel
from openapi_server import util


async def defined_benefit_pensions_delete_defined_benefit_pension_by_id(request: web.Request, id) -> web.Response:
    """defined_benefit_pensions_delete_defined_benefit_pension_by_id

    Description: The operation removes a Defined Benefit Pension tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Defined Benefit Pension from a Fact Finder.

    :param id: The Defined Benefit Pension ID used to identify which Defined Benefit Pension to remove
    :type id: int

    """
    return web.Response(status=200)


async def defined_benefit_pensions_get_by_id(request: web.Request, id) -> web.Response:
    """defined_benefit_pensions_get_by_id

    Description: This operation retrieves a single Defined Benefit Pension for the specified Defined Benefit Pension ID.&lt;br /&gt;                Purpose: Provides access to the Defined Benefit Pension including description and start date.

    :param id: The ID of the Defined Benefit Pension used to retreive the Defined Benefit Pension
    :type id: int

    """
    return web.Response(status=200)


async def defined_benefit_pensions_get_defined_benefit_pensions_by_fact_finder_id_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """defined_benefit_pensions_get_defined_benefit_pensions_by_fact_finder_id_by_factfinderid

    Description: This operation retrieves all Defined Benefit Pensions for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Defined Benefit Pensions including description and start date.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Defined Benefit Pensions
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def defined_benefit_pensions_post_by_model(request: web.Request, model) -> web.Response:
    """defined_benefit_pensions_post_by_model

    Description: The operation creates a Defined Benefit Pension.&lt;br /&gt;                Purpose: Allows for creation of Defined Benefit Pensions on a Fact Finder.

    :param model: The Defined Benefit Pension to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = DefinedBenefitPensionModel.from_dict(model)
    return web.Response(status=200)


async def defined_benefit_pensions_put_defined_benefit_pension_by_id_model(request: web.Request, id, model) -> web.Response:
    """defined_benefit_pensions_put_defined_benefit_pension_by_id_model

    Description: The operation updates a Defined Benefit Pension.&lt;br /&gt;                Purpose: Allows for complete replacement of a Defined Benefit Pension on a Fact Finder.

    :param id: The existing Defined Benefit Pension ID used to identify which Defined Benefit Pension to update
    :type id: int
    :param model: The Defined Benefit Pension to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = DefinedBenefitPensionModel.from_dict(model)
    return web.Response(status=200)
