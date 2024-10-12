from typing import List, Dict
from aiohttp import web

from openapi_server.models.beanstream_exception import BeanstreamException
from openapi_server.models.create_profile_body import CreateProfileBody
from openapi_server.models.payment_profile import PaymentProfile
from openapi_server.models.profile_card import ProfileCard
from openapi_server.models.profile_get_cards import ProfileGetCards
from openapi_server.models.profile_response import ProfileResponse
from openapi_server.models.update_profile_body import UpdateProfileBody
from openapi_server import util


async def profiles_post(request: web.Request, create_profile_body) -> web.Response:
    """Create Profile

    Create a new Payment Profile using either a card or a Legato token. You must supply one of them.

    :param create_profile_body: 
    :type create_profile_body: dict | bytes

    """
    create_profile_body = CreateProfileBody.from_dict(create_profile_body)
    return web.Response(status=200)


async def profiles_profile_id_cards_card_id_delete(request: web.Request, profile_id, card_id) -> web.Response:
    """Delete card

    Delete a card on the profile.

    :param profile_id: The profile id. (aka CustomerCode)
    :type profile_id: str
    :param card_id: The card id.
    :type card_id: 

    """
    return web.Response(status=200)


async def profiles_profile_id_cards_card_id_put(request: web.Request, profile_id, card_id, card) -> web.Response:
    """Update card

    Update the details of a card on the profile.

    :param profile_id: The profile id. (aka CustomerCode)
    :type profile_id: str
    :param card_id: The card id.
    :type card_id: 
    :param card: The card that will be updated on the profile.
    :type card: dict | bytes

    """
    card = ProfileCard.from_dict(card)
    return web.Response(status=200)


async def profiles_profile_id_cards_get(request: web.Request, profile_id) -> web.Response:
    """Get cards

    Get all of the cards on the profile.

    :param profile_id: The profile id. (aka CustomerCode)
    :type profile_id: str

    """
    return web.Response(status=200)


async def profiles_profile_id_cards_post(request: web.Request, profile_id, card) -> web.Response:
    """Add card

    Add a card to the profile. Note that there is a default limit of 1 card per profile. You can change this in your Profiles settings in the back office.

    :param profile_id: The profile id. (aka CustomerCode)
    :type profile_id: str
    :param card: The card that will be added to the profile.
    :type card: dict | bytes

    """
    card = ProfileCard.from_dict(card)
    return web.Response(status=200)


async def profiles_profile_id_delete(request: web.Request, profile_id) -> web.Response:
    """Delete profile

    Delete a Payment Profile using the profile ID, also known as the Customer Code.

    :param profile_id: The profile id. (aka CustomerCode)
    :type profile_id: str

    """
    return web.Response(status=200)


async def profiles_profile_id_get(request: web.Request, profile_id) -> web.Response:
    """Get profile

    Get a Payment Profile using the profile ID, also known as the Customer Code.

    :param profile_id: The profile id. (aka CustomerCode)
    :type profile_id: str

    """
    return web.Response(status=200)


async def profiles_profile_id_put(request: web.Request, profile_id, update_profile_body) -> web.Response:
    """Update Profile

    Create a new Payment Profile using either a card or a Legato token. You must supply one of them.

    :param profile_id: The profile id. (aka CustomerCode)
    :type profile_id: str
    :param update_profile_body: 
    :type update_profile_body: dict | bytes

    """
    update_profile_body = UpdateProfileBody.from_dict(update_profile_body)
    return web.Response(status=200)
