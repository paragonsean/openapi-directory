from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.dealer_db_models_edt_lite_registration import DealerDBModelsEDTLiteRegistration
from openapi_server.models.dealer_db_models_license_activation import DealerDBModelsLicenseActivation
from openapi_server.models.dealer_db_models_license_activation_confirm import DealerDBModelsLicenseActivationConfirm
from openapi_server.models.dealer_db_models_license_activation_create import DealerDBModelsLicenseActivationCreate
from openapi_server.models.dealer_db_models_license_activation_update import DealerDBModelsLicenseActivationUpdate
from openapi_server import util


async def license_activations_post(request: web.Request, body) -> web.Response:
    """Create a license activation.

    No Documentation Found.

    :param body: The data required for creating the license.
    :type body: dict | bytes

    """
    body = DealerDBModelsLicenseActivationCreate.from_dict(body)
    return web.Response(status=200)


async def license_activations_post_register_edt_lite(request: web.Request, body) -> web.Response:
    """Register an EDT Lite with the Server

    No Documentation Found.

    :param body: The information required for registration.
    :type body: dict | bytes

    """
    body = DealerDBModelsEDTLiteRegistration.from_dict(body)
    return web.Response(status=200)


async def license_activations_put(request: web.Request, id, body) -> web.Response:
    """Update a license activiation.

    No Documentation Found.

    :param id: The ID of the license.
    :type id: str
    :param body: The data required for updating the license.
    :type body: dict | bytes

    """
    body = DealerDBModelsLicenseActivationUpdate.from_dict(body)
    return web.Response(status=200)


async def license_activations_put_confirm(request: web.Request, id, body) -> web.Response:
    """Confirm that the client has applied the updated license.

    No Documentation Found.

    :param id: The ID of the license
    :type id: str
    :param body: The license data.
    :type body: dict | bytes

    """
    body = DealerDBModelsLicenseActivationConfirm.from_dict(body)
    return web.Response(status=200)
