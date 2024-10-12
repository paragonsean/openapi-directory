from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_contact_in_mailing_list import CreateContactInMailingList
from openapi_server.models.create_distribution_links import CreateDistributionLinks
from openapi_server.models.distributions_response import DistributionsResponse
from openapi_server.models.event_subscriptions_response import EventSubscriptionsResponse
from openapi_server.models.retrieve_distribution_links_response import RetrieveDistributionLinksResponse
from openapi_server.models.subscribe_to_event_body import SubscribeToEventBody
from openapi_server import util


async def create_contact_in_mailinglist(request: web.Request, directory_id, mailing_list_id, body) -> web.Response:
    """Create contact in mailing list

    Creates a contact in a given mailing list

    :param directory_id: ID of the qualtrics directory to create the contact to
    :type directory_id: str
    :param mailing_list_id: ID of the mailing list
    :type mailing_list_id: str
    :param body: Contact data
    :type body: dict | bytes

    """
    body = CreateContactInMailingList.from_dict(body)
    return web.Response(status=200)


async def generate_distribution_links(request: web.Request, body) -> web.Response:
    """Generate distribution links

    Geneates links for individual distribution

    :param body: Parameters for the link generation
    :type body: dict | bytes

    """
    body = CreateDistributionLinks.from_dict(body)
    return web.Response(status=200)


async def get_distributions(request: web.Request, survey_id) -> web.Response:
    """Get distributions for survey

    Gets all distributions for a given survey

    :param survey_id: The survey for which to load the distributions
    :type survey_id: str

    """
    return web.Response(status=200)


async def get_event_subscriptions(request: web.Request, subscription_id) -> web.Response:
    """Get event subscriptions

    Get event subscriptions

    :param subscription_id: ID of event subscription - can be obtained from web hook response
    :type subscription_id: str

    """
    return web.Response(status=200)


async def get_survey(request: web.Request, survey_id) -> web.Response:
    """Get survey

    Gets a single Qualtrics survey speficied by its ID

    :param survey_id: ID of survey (eg. SV_123)
    :type survey_id: str

    """
    return web.Response(status=200)


async def retrievedistributionlinks(request: web.Request, survey_id, distribution_id) -> web.Response:
    """Retrieve distribution links

    Retrieves all the individual links for a given distribution

    :param survey_id: ID of the survey (eg: SV_123)
    :type survey_id: str
    :param distribution_id: ID of the distribution list
    :type distribution_id: str

    """
    return web.Response(status=200)


async def webhook_delete(request: web.Request, body) -> web.Response:
    """Remove subscription to response event

    Remove event subscription

    :param body: This is the request body of the webhook
    :type body: dict | bytes

    """
    body = SubscribeToEventBody.from_dict(body)
    return web.Response(status=200)


async def when_a_response_is_received(request: web.Request, body) -> web.Response:
    """Triggers when a response is submitted to a qualtrics survey

    Subscribe to response event

    :param body: This is the request body of the webhook
    :type body: dict | bytes

    """
    body = SubscribeToEventBody.from_dict(body)
    return web.Response(status=200)
