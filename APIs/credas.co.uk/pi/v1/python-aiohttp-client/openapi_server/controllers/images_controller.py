from typing import List, Dict
from aiohttp import web

from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server.models.credas_api_models_images_add_id_document_image_request import CredasApiModelsImagesAddIdDocumentImageRequest
from openapi_server.models.credas_api_models_images_add_id_document_image_response import CredasApiModelsImagesAddIdDocumentImageResponse
from openapi_server.models.credas_api_models_images_add_liveness_image_request import CredasApiModelsImagesAddLivenessImageRequest
from openapi_server.models.credas_api_models_images_add_selfie_image_request import CredasApiModelsImagesAddSelfieImageRequest
from openapi_server.models.credas_api_models_images_add_selfie_image_response import CredasApiModelsImagesAddSelfieImageResponse
from openapi_server.models.credas_api_models_images_get_id_document_image_response import CredasApiModelsImagesGetIdDocumentImageResponse
from openapi_server.models.credas_api_models_images_get_liveness_image_response import CredasApiModelsImagesGetLivenessImageResponse
from openapi_server.models.credas_api_models_images_get_liveness_performed_image_response import CredasApiModelsImagesGetLivenessPerformedImageResponse
from openapi_server.models.credas_api_models_images_get_selfie_image_response import CredasApiModelsImagesGetSelfieImageResponse
from openapi_server import util


async def add_id_document_image(request: web.Request, apikey, body=None) -> web.Response:
    """Add an id document image to the specified registration.

    

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: Object containing the id document image and registration id.
    :type body: dict | bytes

    """
    body = CredasApiModelsImagesAddIdDocumentImageRequest.from_dict(body)
    return web.Response(status=200)


async def add_liveness_image(request: web.Request, apikey, body=None) -> web.Response:
    """Add a liveness image (UAP) to the specified registration.

    

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: Object containing the liveness image and registration id.
    :type body: dict | bytes

    """
    body = CredasApiModelsImagesAddLivenessImageRequest.from_dict(body)
    return web.Response(status=200)


async def add_selfie_image(request: web.Request, apikey, body=None) -> web.Response:
    """Add a selfie image to the registration.

    

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: Object containing the selfie image and registration id.
    :type body: dict | bytes

    """
    body = CredasApiModelsImagesAddSelfieImageRequest.from_dict(body)
    return web.Response(status=200)


async def get_id_document_images(request: web.Request, registration_id, apikey) -> web.Response:
    """Get all id document images associated with a registration.

    

    :param registration_id: The id of the registration.
    :type registration_id: str
    :type registration_id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)


async def get_liveness_image(request: web.Request, registration_id, apikey) -> web.Response:
    """Retrieve the liveness action image (UAP) associated with a registration.

    

    :param registration_id: The id of the registration.
    :type registration_id: str
    :type registration_id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)


async def get_liveness_performed_image(request: web.Request, registration_id, apikey) -> web.Response:
    """Retrieve the liveness performed image associated with a registration.

    

    :param registration_id: The id of the registration.
    :type registration_id: str
    :type registration_id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)


async def get_scan_report_pdf(request: web.Request, scan_id, apikey) -> web.Response:
    """Returns a detailed report on the analysis that has taken place of a scanned document

    

    :param scan_id: Id of the individual scanned document
    :type scan_id: str
    :type scan_id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)


async def get_selfie_image(request: web.Request, registration_id, apikey) -> web.Response:
    """Retrieve the selfie image associated with a registration.

    

    :param registration_id: The id of the registration.
    :type registration_id: str
    :type registration_id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)
