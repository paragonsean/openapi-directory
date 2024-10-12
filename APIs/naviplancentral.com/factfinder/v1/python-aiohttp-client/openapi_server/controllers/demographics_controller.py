from typing import List, Dict
from aiohttp import web

from openapi_server.models.demographics_dependent_model import DemographicsDependentModel
from openapi_server.models.demographics_dependent_with_id_model import DemographicsDependentWithIdModel
from openapi_server.models.demographics_dependents_model import DemographicsDependentsModel
from openapi_server.models.demographics_model import DemographicsModel
from openapi_server.models.demographics_with_id_model import DemographicsWithIdModel
from openapi_server import util


async def demographics_delete_dependent_by_demographicid_id(request: web.Request, demographic_id, id) -> web.Response:
    """demographics_delete_dependent_by_demographicid_id

    Description: The operation removes a Dependent tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Dependent from a Fact Finder.

    :param demographic_id: The ID of the Demographic information used to identify which Dependent to remove
    :type demographic_id: int
    :param id: The Dependent ID used to identify which Dependent to remove
    :type id: int

    """
    return web.Response(status=200)


async def demographics_get_by_id(request: web.Request, id) -> web.Response:
    """demographics_get_by_id

    Description: This operation retrieves Demographic information for the specified Demographic information ID.&lt;br /&gt;                Purpose: Provides access to the Demographic information including city and state.

    :param id: The ID of the Demographic information used to retreive the Demographic information
    :type id: int

    """
    return web.Response(status=200)


async def demographics_get_demographics_by_fact_finder_id_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """demographics_get_demographics_by_fact_finder_id_by_factfinderid

    Description: This operation retrieves all Demographic information for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Demographic information including city and state.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Demographic information
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def demographics_get_dependent_by_demographicid_id(request: web.Request, demographic_id, id) -> web.Response:
    """demographics_get_dependent_by_demographicid_id

    Description: This operation retrieves a single Dependent for the specified Dependent ID.&lt;br /&gt;                Purpose: Provides access to the Dependent including first and last name.

    :param demographic_id: The ID of the Demographic information used to retrieve Dependents
    :type demographic_id: int
    :param id: The ID of the Dependent used to retreive the Dependent
    :type id: int

    """
    return web.Response(status=200)


async def demographics_get_dependents_by_demographicid(request: web.Request, demographic_id) -> web.Response:
    """demographics_get_dependents_by_demographicid

    Description: This operation retrieves all Dependents for the specified Demographic information ID.&lt;br /&gt;                Purpose: Provides access to the Dependents including first and last name.

    :param demographic_id: The ID of the Demographic information used to retrieve Dependents
    :type demographic_id: int

    """
    return web.Response(status=200)


async def demographics_post_by_demographicid_model(request: web.Request, demographic_id, model) -> web.Response:
    """demographics_post_by_demographicid_model

    Description: The operation creates a Dependent.&lt;br /&gt;                Purpose: Allows for creation of Dependents on a Fact Finder.

    :param demographic_id: The ID of the Demographic information to add the Dependent to
    :type demographic_id: int
    :param model: The Dependent to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = DemographicsDependentModel.from_dict(model)
    return web.Response(status=200)


async def demographics_post_by_model(request: web.Request, model) -> web.Response:
    """demographics_post_by_model

    Description: The operation creates Demographic information.&lt;br /&gt;                Purpose: Allows for creation of Demographic information on a Fact Finder.

    :param model: The Demographic information to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = DemographicsModel.from_dict(model)
    return web.Response(status=200)


async def demographics_put_by_demographicid_id_model(request: web.Request, demographic_id, id, model) -> web.Response:
    """demographics_put_by_demographicid_id_model

    Description: The operation updates a Dependent.&lt;br /&gt;                Purpose: Allows for complete replacement of a Dependent on a Fact Finder.

    :param demographic_id: The ID of the Demographic information used to identify which Dependent to update
    :type demographic_id: int
    :param id: The existing Dependent ID used to identify which Dependent to update
    :type id: int
    :param model: The Dependent to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = DemographicsDependentModel.from_dict(model)
    return web.Response(status=200)


async def demographics_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """demographics_put_by_id_model

    Description: The operation updates Demographic information.&lt;br /&gt;                Purpose: Allows for complete replacement of Demographic information on a Fact Finder.

    :param id: The existing Demographic information ID used to identify which Demographic information to update
    :type id: int
    :param model: The Demographic information to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = DemographicsModel.from_dict(model)
    return web.Response(status=200)
