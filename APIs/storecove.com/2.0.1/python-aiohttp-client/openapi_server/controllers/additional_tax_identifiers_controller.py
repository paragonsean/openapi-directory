from typing import List, Dict
from aiohttp import web

from openapi_server.models.additional_tax_identifier import AdditionalTaxIdentifier
from openapi_server.models.additional_tax_identifier_create import AdditionalTaxIdentifierCreate
from openapi_server.models.additional_tax_identifier_update import AdditionalTaxIdentifierUpdate
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def create_additional_tax_identifier(request: web.Request, legal_entity_id, body) -> web.Response:
    """Create a new AdditionalTaxIdentifier

    Create a new AdditionalTaxIdentifier. An AdditionalTaxIdentifier is a seconday tax identifier that is used inside the EU when sending invoices to consumers. In that case, the VAT of the receiving country is used and if the sender has a local VAT identifier, that is used to identifiy the sender, instead of the sender&#39;s origin country VAT number. To use these identifiers, use the invoice.consumerTaxMode &#x3D; true property.

    :param legal_entity_id: The id of the LegalEntity for which to create the AdditionalTaxIdentifier
    :type legal_entity_id: int
    :param body: AdditionalTaxIdentifier to create
    :type body: dict | bytes

    """
    body = AdditionalTaxIdentifierCreate.from_dict(body)
    return web.Response(status=200)


async def delete_additional_tax_identifier(request: web.Request, legal_entity_id, id) -> web.Response:
    """Delete AdditionalTaxIdentifier

    Delete an AdditionalTaxIdentifier

    :param legal_entity_id: The id of the LegalEntity the AdditionalTaxIdentifier belongs to
    :type legal_entity_id: int
    :param id: The id of the AdditionalTaxIdentifier
    :type id: int

    """
    return web.Response(status=200)


async def get_additional_tax_identifier(request: web.Request, legal_entity_id, id) -> web.Response:
    """Get AdditionalTaxIdentifier

    Get an AdditionalTaxIdentifier

    :param legal_entity_id: The id of the LegalEntity the AdditionalTaxIdentifier belongs to
    :type legal_entity_id: int
    :param id: The id of the AdditionalTaxIdentifier
    :type id: int

    """
    return web.Response(status=200)


async def update_additional_tax_identifier(request: web.Request, legal_entity_id, id, body) -> web.Response:
    """Update AdditionalTaxIdentifier

    Update an AdditionalTaxIdentifier

    :param legal_entity_id: The id of the LegalEntity the AdditionalTaxIdentifier belongs to
    :type legal_entity_id: int
    :param id: The id of the AdditionalTaxIdentifier to be updated
    :type id: int
    :param body: AdditionalTaxIdentifier to update
    :type body: dict | bytes

    """
    body = AdditionalTaxIdentifierUpdate.from_dict(body)
    return web.Response(status=200)
