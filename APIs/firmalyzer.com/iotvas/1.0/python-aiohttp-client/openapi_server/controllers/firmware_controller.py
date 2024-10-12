from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_issue import ConfigIssue
from openapi_server.models.crypto_key import CryptoKey
from openapi_server.models.default_account import DefaultAccount
from openapi_server.models.expired_cert import ExpiredCert
from openapi_server.models.firmware_risk import FirmwareRisk
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.weak_cert import WeakCert
from openapi_server import util


async def get_accounts(request: web.Request, firmware_hash) -> web.Response:
    """Get default accounts and password hashes of a firmware

    

    :param firmware_hash: SHA2 hash of device firmware
    :type firmware_hash: str

    """
    return web.Response(status=200)


async def get_config_issues(request: web.Request, firmware_hash) -> web.Response:
    """Get default OS configuration issues of a device firmware

    

    :param firmware_hash: SHA2 hash of device firmware
    :type firmware_hash: str

    """
    return web.Response(status=200)


async def get_expired_certs(request: web.Request, firmware_hash) -> web.Response:
    """Get expired digital certificates embedded in a device firmware

    

    :param firmware_hash: SHA2 hash of device firmware
    :type firmware_hash: str

    """
    return web.Response(status=200)


async def get_private_keys(request: web.Request, firmware_hash) -> web.Response:
    """Get private crypto keys embedded in a device firmware

    

    :param firmware_hash: SHA2 hash of device firmware
    :type firmware_hash: str

    """
    return web.Response(status=200)


async def get_risk(request: web.Request, firmware_hash) -> web.Response:
    """Get iot device firmware risk analysis

    

    :param firmware_hash: SHA2 hash of device firmware
    :type firmware_hash: str

    """
    return web.Response(status=200)


async def get_weak_certs(request: web.Request, firmware_hash) -> web.Response:
    """Get certificates with weak fingerprinting algorithms that are mebedded in a device firmware

    

    :param firmware_hash: SHA2 hash of device firmware
    :type firmware_hash: str

    """
    return web.Response(status=200)


async def get_weak_keys(request: web.Request, firmware_hash) -> web.Response:
    """Get weak crypto keys with short length

    

    :param firmware_hash: SHA2 hash of device firmware
    :type firmware_hash: str

    """
    return web.Response(status=200)
