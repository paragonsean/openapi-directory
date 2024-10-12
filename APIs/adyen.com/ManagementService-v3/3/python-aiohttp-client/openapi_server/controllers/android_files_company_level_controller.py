from typing import List, Dict
from aiohttp import web

from openapi_server.models.android_app import AndroidApp
from openapi_server.models.android_apps_response import AndroidAppsResponse
from openapi_server.models.android_certificates_response import AndroidCertificatesResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.upload_android_app_response import UploadAndroidAppResponse
from openapi_server import util


async def get_companies_company_id_android_apps(request: web.Request, company_id, page_number=None, page_size=None, package_name=None, version_code=None) -> web.Response:
    """Get a list of Android apps

    Returns a list of the Android apps that are available for the company identified in the path.  These apps have been uploaded to Adyen and can be installed or uninstalled on Android payment terminals through [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Android files read * Management API—Android files read and write * Management API—Terminal actions read * Management API—Terminal actions read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param page_number: The number of the page to fetch.
    :type page_number: int
    :param page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
    :type page_size: int
    :param package_name: The package name that uniquely identifies the Android app.
    :type package_name: str
    :param version_code: The version number of the app.
    :type version_code: int

    """
    return web.Response(status=200)


async def get_companies_company_id_android_apps_id(request: web.Request, company_id, id) -> web.Response:
    """Get Android app

    Returns the details of the Android app identified in the path.  These apps have been uploaded to Adyen and can be installed or uninstalled on Android payment terminals through [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Android files read * Management API—Android files read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param id: The unique identifier of the app.
    :type id: str

    """
    return web.Response(status=200)


async def get_companies_company_id_android_certificates(request: web.Request, company_id, page_number=None, page_size=None, certificate_name=None) -> web.Response:
    """Get a list of Android certificates

    Returns a list of the Android certificates that are available for the company identified in the path. Typically, these certificates enable running apps on Android payment terminals. The certifcates in the list have been uploaded to Adyen and can be installed or uninstalled on Android terminals through [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Android files read * Management API—Android files read and write * Management API—Terminal actions read * Management API—Terminal actions read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param page_number: The number of the page to fetch.
    :type page_number: int
    :param page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
    :type page_size: int
    :param certificate_name: The name of the certificate.
    :type certificate_name: str

    """
    return web.Response(status=200)


async def post_companies_company_id_android_apps(request: web.Request, company_id) -> web.Response:
    """Upload Android App

    Uploads an Android APK file to Adyen. The maximum APK file size is 200 MB. To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Android files read and write  &gt;By choosing to upload, install, or run any third-party applications on an Adyen payment terminal, you accept full responsibility and liability for any consequences of uploading, installing, or running any such applications.

    :param company_id: The unique identifier of the company account.
    :type company_id: str

    """
    return web.Response(status=200)
