from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_with_sub_entities_model import AccountsWithSubEntitiesModel
from openapi_server.models.defined_benefit_pensions_model import DefinedBenefitPensionsModel
from openapi_server.models.incomes_model import IncomesModel
from openapi_server.models.liabilities_model import LiabilitiesModel
from openapi_server.models.life_insurance_policies_with_sub_entities_model import LifeInsurancePoliciesWithSubEntitiesModel
from openapi_server.models.owners_model import OwnersModel
from openapi_server.models.relationship_types_model import RelationshipTypesModel
from openapi_server import util


async def presentation_get_accounts_by_factfinderid_externalsourceid(request: web.Request, fact_finder_id, external_source_id=None) -> web.Response:
    """presentation_get_accounts_by_factfinderid_externalsourceid

    Description: This operation retrieves all current Accounts for the specified Fact Finder ID, as well as                             all of the holdings and savings strategies belonging to those accounts.&lt;br /&gt;                Purpose: Provides access to the Accounts in a Fact Finder as well as any sub-entities belonging to them.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Accounts
    :type fact_finder_id: int
    :param external_source_id: The external ID used to filter Accounts
    :type external_source_id: str

    """
    return web.Response(status=200)


async def presentation_get_demographic_owners_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """presentation_get_demographic_owners_by_factfinderid

    Description: This operation retrieves owner values for the fact finder based on demographics data                Purpose: Provides the list of valid options for owner, student, beneficiary, etc.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve owners.
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def presentation_get_demographic_relationships(request: web.Request, ) -> web.Response:
    """presentation_get_demographic_relationships

    Description: This operation retrieves all relationship types relevant to demographics.&lt;br /&gt;                Purpose: Provides a list of relationship types organized by whether or not they can be defined as children.


    """
    return web.Response(status=200)


async def presentation_get_incomes_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """presentation_get_incomes_by_factfinderid

    Description: This operation retrieves all current Incomes for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Incomes in a Fact Finder, filtered by Incomes that are current.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Incomes
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def presentation_get_liabilities_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """presentation_get_liabilities_by_factfinderid

    Description: This operation retrieves all current Liabilities for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Liabilities in a Fact Finder, filtered by Liabilities that are current.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Liabilities
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def presentation_get_life_insurance_policies_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """presentation_get_life_insurance_policies_by_factfinderid

    Description: This operation retrieves all life insurance policies, including subaccounts if available, for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policies in a Fact Finder.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Life Insurance Policies.
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def presentation_get_pensions_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """presentation_get_pensions_by_factfinderid

    Description: This operation retrieves all future Defined Benefit Pensions for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Pensions in a Fact Finder, filtered by Pensions that are in the future.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Pensions.
    :type fact_finder_id: int

    """
    return web.Response(status=200)
