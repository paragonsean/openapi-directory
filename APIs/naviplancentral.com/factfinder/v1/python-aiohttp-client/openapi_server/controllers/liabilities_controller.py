from typing import List, Dict
from aiohttp import web

from openapi_server.models.liabilities_model import LiabilitiesModel
from openapi_server.models.liability_model import LiabilityModel
from openapi_server.models.liability_with_id_model import LiabilityWithIdModel
from openapi_server import util


async def liabilities_delete_by_id(request: web.Request, id) -> web.Response:
    """liabilities_delete_by_id

    Description: The operation removes a Liability tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Liability from a Fact Finder.

    :param id: The Liability ID used to identify which Liability to remove
    :type id: int

    """
    return web.Response(status=200)


async def liabilities_get_by_id(request: web.Request, id) -> web.Response:
    """liabilities_get_by_id

    Description: This operation retrieves a single Liability for the specified Liability ID.&lt;br /&gt;                Purpose: Provides access to the Liability including owner and type.

    :param id: The ID of the Liability used to retreive the Liability
    :type id: int

    """
    return web.Response(status=200)


async def liabilities_get_liabilities_by_fact_finder_id_by_factfinderid_externalsourceid(request: web.Request, fact_finder_id, external_source_id=None) -> web.Response:
    """liabilities_get_liabilities_by_fact_finder_id_by_factfinderid_externalsourceid

    Description: This operation retrieves all Liabilities for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Liabilities including owner and type.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Liabilities
    :type fact_finder_id: int
    :param external_source_id: The external source ID used to filter Liabilities
    :type external_source_id: str

    """
    return web.Response(status=200)


async def liabilities_post_by_model(request: web.Request, model) -> web.Response:
    """liabilities_post_by_model

    Description: The operation creates a Liability.&lt;br /&gt;                Purpose: Allows for creation of Liabilities on a Fact Finder.

    :param model: The Liability to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = LiabilityModel.from_dict(model)
    return web.Response(status=200)


async def liabilities_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """liabilities_put_by_id_model

    Description: The operation updates a Liability.&lt;br /&gt;                Purpose: Allows for complete replacement of a Liability on a Fact Finder.

    :param id: The existing Liability ID used to identify which Liability to update
    :type id: int
    :param model: The Liability to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = LiabilityModel.from_dict(model)
    return web.Response(status=200)
