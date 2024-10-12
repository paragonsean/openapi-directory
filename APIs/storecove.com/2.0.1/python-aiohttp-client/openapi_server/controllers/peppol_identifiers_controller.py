from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.peppol_identifier import PeppolIdentifier
from openapi_server.models.peppol_identifier_create import PeppolIdentifierCreate
from openapi_server import util


async def create_peppol_identifier(request: web.Request, legal_entity_id, body) -> web.Response:
    """Create a new PeppolIdentifier

    Create a brand new new PeppolIdentifier. For &lt;&lt;_sg_singapore&gt;&gt;, special rules apply.

    :param legal_entity_id: The id of the LegalEntity for which to create the PeppolIdentifier
    :type legal_entity_id: int
    :param body: PeppolIdentifier to create
    :type body: dict | bytes

    """
    body = PeppolIdentifierCreate.from_dict(body)
    return web.Response(status=200)


async def delete_peppol_identifier(request: web.Request, legal_entity_id, superscheme, scheme, identifier) -> web.Response:
    """Delete PeppolIdentifier

    Delete a PeppolIdentifier.

    :param legal_entity_id: The id of the LegalEntity this PeppolIdentifier belongs to
    :type legal_entity_id: int
    :param superscheme: The superscheme of the identifier. Should always be \&quot;iso6523-actorid-upis\&quot;.
    :type superscheme: str
    :param scheme: PEPPOL identifier scheme id, e.g. \&quot;DE:VAT\&quot;. For a full list see &lt;&lt;_receiver_identifiers_list&gt;&gt;.
    :type scheme: str
    :param identifier: PEPPOL identifier
    :type identifier: str

    """
    return web.Response(status=200)
