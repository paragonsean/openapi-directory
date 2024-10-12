from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_dto import AddressDTO
from openapi_server.models.competencies_dto import CompetenciesDTO
from openapi_server.models.contact_dto import ContactDTO
from openapi_server.models.custom_field_dto import CustomFieldDTO
from openapi_server.models.invitation_statistics_dto import InvitationStatisticsDTO
from openapi_server.models.person_contact_dto import PersonContactDTO
from openapi_server.models.provider_dto import ProviderDTO
from openapi_server.models.provider_person_dto import ProviderPersonDTO
from openapi_server import util


async def delete10(request: web.Request, provider_id) -> web.Response:
    """Removes a provider.

    Removes a provider.

    :param provider_id: provider&#39;s internal identifier
    :type provider_id: int

    """
    return web.Response(status=200)


async def delete8(request: web.Request, person_id) -> web.Response:
    """Removes a person.

    Removes a person.

    :param person_id: person&#39;s internal identifier
    :type person_id: int

    """
    return web.Response(status=200)


async def delete9(request: web.Request, price_list_id) -> web.Response:
    """Removes a provider price list.

    Removes a provider price list.

    :param price_list_id: provider price list&#39;s internal identifier
    :type price_list_id: int

    """
    return web.Response(status=200)


async def get_address1(request: web.Request, provider_id) -> web.Response:
    """Returns address of a given provider.

    Returns address of a given provider.

    :param provider_id: provider&#39;s internal identifier
    :type provider_id: int

    """
    return web.Response(status=200)


async def get_all_ids4(request: web.Request, updated_since=None) -> web.Response:
    """Returns persons&#39; internal identifiers.

    Returns persons&#39; internal identifiers.

    :param updated_since: only persons modified since this timestamp
    :type updated_since: int

    """
    return web.Response(status=200)


async def get_all_ids5(request: web.Request, updated_since=None) -> web.Response:
    """Returns providers&#39; internal identifiers.

    Returns providers&#39; internal identifiers.

    :param updated_since: only providers modified since this timestamp
    :type updated_since: int

    """
    return web.Response(status=200)


async def get_by_id4(request: web.Request, person_id) -> web.Response:
    """Returns person details.

    Returns person details.

    :param person_id: person&#39;s internal identifier
    :type person_id: int

    """
    return web.Response(status=200)


async def get_by_id5(request: web.Request, provider_id, embed=None) -> web.Response:
    """Returns provider details.

    Returns provider details.

    :param provider_id: provider&#39;s internal identifier
    :type provider_id: int
    :param embed: list of adittional fields which should be embedded in the response (ie. persons)
    :type embed: str

    """
    return web.Response(status=200)


async def get_competencies(request: web.Request, provider_id) -> web.Response:
    """Returns competencies of a given provider.

    Returns competencies of a given provider.

    :param provider_id: provider&#39;s internal identifier
    :type provider_id: int

    """
    return web.Response(status=200)


async def get_contact2(request: web.Request, person_id) -> web.Response:
    """Returns contact of a given person.

    Returns contact of a given person.

    :param person_id: person&#39;s internal identifier
    :type person_id: int

    """
    return web.Response(status=200)


async def get_contact3(request: web.Request, provider_id) -> web.Response:
    """Returns contact of a given provider.

    Returns contact of a given provider.

    :param provider_id: provider&#39;s internal identifier
    :type provider_id: int

    """
    return web.Response(status=200)


async def get_correspondence_address1(request: web.Request, provider_id) -> web.Response:
    """Returns correspondence address of a given provider.

    Returns correspondence address of a given provider.

    :param provider_id: provider&#39;s internal identifier
    :type provider_id: int

    """
    return web.Response(status=200)


async def get_custom_fields2(request: web.Request, person_id) -> web.Response:
    """Returns custom fields of a given person.

    Returns custom fields of a given person.

    :param person_id: person&#39;s internal identifier
    :type person_id: int

    """
    return web.Response(status=200)


async def get_custom_fields3(request: web.Request, provider_id) -> web.Response:
    """Returns custom fields of a given provider.

    Returns custom fields of a given provider.

    :param provider_id: provider&#39;s internal identifier
    :type provider_id: int

    """
    return web.Response(status=200)


async def send_invitations(request: web.Request, person_id) -> web.Response:
    """Sends invitation to Vendor Portal.

    Sends invitation to Vendor Portal.

    :param person_id: person&#39;s internal identifier
    :type person_id: int

    """
    return web.Response(status=200)


async def send_invitations1(request: web.Request, provider_id) -> web.Response:
    """Sends invitations to Vendor Portal.

    Sends invitations to Vendor Portal.

    :param provider_id: provider&#39;s internal identifier
    :type provider_id: int

    """
    return web.Response(status=200)
