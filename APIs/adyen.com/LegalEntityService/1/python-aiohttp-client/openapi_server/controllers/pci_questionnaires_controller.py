from typing import List, Dict
from aiohttp import web

from openapi_server.models.generate_pci_description_request import GeneratePciDescriptionRequest
from openapi_server.models.generate_pci_description_response import GeneratePciDescriptionResponse
from openapi_server.models.get_pci_questionnaire_infos_response import GetPciQuestionnaireInfosResponse
from openapi_server.models.get_pci_questionnaire_response import GetPciQuestionnaireResponse
from openapi_server.models.pci_signing_request import PciSigningRequest
from openapi_server.models.pci_signing_response import PciSigningResponse
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def get_legal_entities_id_pci_questionnaires(request: web.Request, id) -> web.Response:
    """Get PCI questionnaire details

    Get a list of signed PCI questionnaires.

    :param id: The unique identifier of the legal entity to get PCI questionnaire information.
    :type id: str

    """
    return web.Response(status=200)


async def get_legal_entities_id_pci_questionnaires_pciid(request: web.Request, id, pciid) -> web.Response:
    """Get PCI questionnaire

    Returns the signed PCI questionnaire.

    :param id: The legal entity ID of the individual who signed the PCI questionnaire.
    :type id: str
    :param pciid: The unique identifier of the signed PCI questionnaire.
    :type pciid: str

    """
    return web.Response(status=200)


async def post_legal_entities_id_pci_questionnaires_generate_pci_templates(request: web.Request, id, body=None) -> web.Response:
    """Generate PCI questionnaire

    Generates the required PCI questionnaires based on the user&#39;s [salesChannel](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines__reqParam_salesChannels).

    :param id: The unique identifier of the legal entity to get PCI questionnaire information.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GeneratePciDescriptionRequest.from_dict(body)
    return web.Response(status=200)


async def post_legal_entities_id_pci_questionnaires_sign_pci_templates(request: web.Request, id, body=None) -> web.Response:
    """Sign PCI questionnaire

    Signs the required PCI questionnaire.

    :param id: The legal entity ID of the user that has a contractual relationship with your platform.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PciSigningRequest.from_dict(body)
    return web.Response(status=200)
