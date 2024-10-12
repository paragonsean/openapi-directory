from typing import List, Dict
from aiohttp import web

from openapi_server.models.fact_finder_entity_model import FactFinderEntityModel
from openapi_server.models.fact_finder_model import FactFinderModel
from openapi_server.models.fact_finder_populatable_entity_model import FactFinderPopulatableEntityModel
from openapi_server.models.fact_finder_population_model import FactFinderPopulationModel
from openapi_server.models.fact_finder_snapshot_with_id_model import FactFinderSnapshotWithIdModel
from openapi_server.models.fact_finder_snapshots_model import FactFinderSnapshotsModel
from openapi_server.models.fact_finder_with_id_model import FactFinderWithIdModel
from openapi_server import util


async def fact_finders_delete_by_id(request: web.Request, id) -> web.Response:
    """fact_finders_delete_by_id

    Description: This operation deletes a single Fact Finder for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Deletes the fact finder.

    :param id: The ID of the Fact Finder to be deleted
    :type id: int

    """
    return web.Response(status=200)


async def fact_finders_get_by_household_id_by_householdid(request: web.Request, household_id=None) -> web.Response:
    """fact_finders_get_by_household_id_by_householdid

    Description: This operation retrieves all Fact Finders for the specified householdId,                 or if null, all households associated with the user.&lt;br /&gt;                Purpose: Provides access to the Fact Finder including status.

    :param household_id: The ID of the household used to retrieve the fact finders. If not set, uses all households associated with the user
    :type household_id: int

    """
    return web.Response(status=200)


async def fact_finders_get_by_id(request: web.Request, id) -> web.Response:
    """fact_finders_get_by_id

    Description: This operation retrieves a single Fact Finder for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Fact Finder including status.

    :param id: The ID of the Fact Finder used to retrieve the Fact Finder
    :type id: int

    """
    return web.Response(status=200)


async def fact_finders_get_snapshots_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """fact_finders_get_snapshots_by_factfinderid

    Description: The operation retrieves Snapshots of a Fact Finder.&lt;br /&gt;                Purpose: Allows for advisors to view all Snapshots taken of a Fact Finder.

    :param fact_finder_id: The ID of the Fact Finder to retrieve Snapshots for
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def fact_finders_post_by_model(request: web.Request, model) -> web.Response:
    """fact_finders_post_by_model

    Description: The operation creates a completely empty draft Fact Finder.&lt;br /&gt;                Requirements: A householdId and list of modules must be provided.&lt;br /&gt;                Purpose: Stages a Fact Finder for population.

    :param model: The Household the Fact Finder will belong to and the modules that are available.
    :type model: dict | bytes

    """
    model = FactFinderEntityModel.from_dict(model)
    return web.Response(status=200)


async def fact_finders_post_populate_by_model(request: web.Request, model) -> web.Response:
    """fact_finders_post_populate_by_model

    Description: The operation creates a new Populated Fact Finder.&lt;br /&gt;                Requirements: A householdId and list of modules must be provided.&lt;br /&gt;                Purpose: Creation of a Fact Finder.

    :param model: The Household the Fact Finder will belong to and the modules that are available.               Optional PlanId to populate from
    :type model: dict | bytes

    """
    model = FactFinderPopulatableEntityModel.from_dict(model)
    return web.Response(status=200)


async def fact_finders_post_snapshots_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """fact_finders_post_snapshots_by_factfinderid

    Description: The operation creates a Snapshot of a Fact Finder.&lt;br /&gt;                Purpose: Allows for advisors to compare the current fact finder to a snapshot prior to acceptance.

    :param fact_finder_id: The ID of the Fact Finder used to create the Fact Finder Snapshot
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def fact_finders_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """fact_finders_put_by_id_model

    Description: The operation updates a Fact Finder.&lt;br /&gt;                Purpose: Allows for the updating of a Fact Finder.

    :param id: The existing Fact Finder ID used to identify which Fact Finder to update
    :type id: int
    :param model: The Fact Finder to be updated
    :type model: dict | bytes

    """
    model = FactFinderModel.from_dict(model)
    return web.Response(status=200)


async def fact_finders_put_populate_fact_finder_by_id_model(request: web.Request, id, model) -> web.Response:
    """fact_finders_put_populate_fact_finder_by_id_model

    Description: The operation populates a fact finder.&lt;br /&gt;                Purpose: Allows for the population of a Fact Finder based on a NaviPlan plan or client. This                         operation cannot be performed on a Fact Finder more than once.

    :param id: The existing Fact Finder ID used to identify which Fact Finder to populate.
    :type id: int
    :param model: The plan to populate a fact finder from. If not provided, the client id will be inferred.
    :type model: dict | bytes

    """
    model = FactFinderPopulationModel.from_dict(model)
    return web.Response(status=200)
