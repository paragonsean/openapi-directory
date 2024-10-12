from typing import List, Dict
from aiohttp import web

from openapi_server.models.cm import CM
from openapi_server.models.callback_result import CallbackResult
from openapi_server.models.cancel_project_request import CancelProjectRequest
from openapi_server.models.error import Error
from openapi_server.models.invoice import Invoice
from openapi_server.models.list_order_type import ListOrderType
from openapi_server.models.new_project import NewProject
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.package import Package
from openapi_server.models.package_status import PackageStatus
from openapi_server.models.progress import Progress
from openapi_server.models.project import Project
from openapi_server.models.project_id import ProjectId
from openapi_server.models.project_launch_response import ProjectLaunchResponse
from openapi_server.models.project_list import ProjectList
from openapi_server.models.project_payment import ProjectPayment
from openapi_server.models.project_status import ProjectStatus
from openapi_server.models.project_update import ProjectUpdate
from openapi_server.models.report_content import ReportContent
from openapi_server.models.user_list import UserList
from openapi_server import util


async def assign_cm(request: web.Request, id, body=None) -> web.Response:
    """Assign a CM to the project

    

    :param id: Project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CM.from_dict(body)
    return web.Response(status=200)


async def cancel_project(request: web.Request, id, body=None) -> web.Response:
    """Cancel your translation project

    If you haven&#39;t launched your translation project yet, we will delete it. If MotaWord already started working on your project, we will cancel the project and refund the volume that we haven&#39;t worked on yet.

    :param id: Project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CancelProjectRequest.from_dict(body)
    return web.Response(status=200)


async def create_project(request: web.Request, body=None) -> web.Response:
    """Create a new project

    Create a new translation project. Projects are not launched (you are not charged) until you &#x60;/launch&#x60; the created project.

    :param body: 
    :type body: dict | bytes

    """
    body = NewProject.from_dict(body)
    return web.Response(status=200)


async def delete_project(request: web.Request, id) -> web.Response:
    """Delete your translation project

    If you haven&#39;t launched your translation project yet, we will delete it. If MotaWord already started working on your project, we will cancel the project and refund the volume that we haven&#39;t worked on yet.

    :param id: Project ID
    :type id: int

    """
    return web.Response(status=200)


async def deliver_project(request: web.Request, id) -> web.Response:
    """Deliver project

    Deliver project to the owner of the project. You can also download your translations in &#x60;/package&#x60; and &#x60;/download&#x60; endpoints.

    :param id: Project ID
    :type id: int

    """
    return web.Response(status=200)


async def download(request: web.Request, id) -> web.Response:
    """Download your translated project

    Download the latest translation package. You must have requested a &#x60;/package&#x60; call beforehand and wait until the packaging status is &#39;completed&#39;.

    :param id: Project ID
    :type id: int

    """
    return web.Response(status=200)


async def download_html_invoice(request: web.Request, id) -> web.Response:
    """Download project invoice (HTML)

    Download your project invoice as HTML. This is useful when you want to show your users the invoice in a webpage.

    :param id: Project ID
    :type id: int

    """
    return web.Response(status=200)


async def download_language(request: web.Request, id, language) -> web.Response:
    """Download your translated project language

    Download the latest translation package for your target language. You must have requested a &#x60;/package&#x60; call beforehand and wait until the packaging status is &#39;completed&#39;.

    :param id: Project ID
    :type id: int
    :param language: Language code. You can download the translation of only a specific language.
    :type language: str

    """
    return web.Response(status=200)


async def download_pdf_invoice(request: web.Request, id) -> web.Response:
    """Download project invoice (PDF)

    Download your project invoice as PDF. Your invoice may be in \&quot;unpaid\&quot; status, in which case youn can see the payment instructions in the PDF file.

    :param id: Project ID
    :type id: int

    """
    return web.Response(status=200)


async def get_invoice(request: web.Request, id) -> web.Response:
    """View project invoice

    View your invoice details for your translation project.

    :param id: Project ID
    :type id: int

    """
    return web.Response(status=200)


async def get_progress(request: web.Request, id, raw=None) -> web.Response:
    """View progress of a project

    Monitor the translation progress of an already launched project in real-time.

    :param id: Project ID
    :type id: int
    :param raw: This will return a more raw progress information for translation and proofreading. For instance, when completed, we will return 100% for both tasks by default, whereas their actual progress may be lower than 100%.
    :type raw: bool

    """
    return web.Response(status=200)


async def get_project(request: web.Request, id, _with=None) -> web.Response:
    """View a translation project

    View the details of a translation project in your account.

    :param id: Project ID
    :type id: int
    :param _with: Include detailed information. Possible values &#39;client&#39;, &#39;vendor&#39;, &#39;score&#39;
    :type _with: List[str]

    """
    return web.Response(status=200)


async def get_project_vendors(request: web.Request, project_id) -> web.Response:
    """Get a list of vendors.

    Get a list of vendors.

    :param project_id: Project ID
    :type project_id: int

    """
    return web.Response(status=200)


async def get_projects(request: web.Request, page=None, per_page=None, status=None, with_pending=None, with_started=None, with_completed=None, order_by=None, order_type=None, _with=None) -> web.Response:
    """View your translation projects

    View the translation projects ordered in your account. If you have the related permission (configured by your account administrator), you can view the projects of your colleagues under the same company account.

    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param status: Filter projects by status. Accepts multiple statuses. Possible values &#39;pending&#39;, &#39;started&#39;, &#39;completed&#39;
    :type status: list | bytes
    :param with_pending: deprecated. use &#x60;status[]&#x60; param.
    :type with_pending: bool
    :param with_started: deprecated. use &#x60;status[]&#x60; param.
    :type with_started: bool
    :param with_completed: deprecated. use &#x60;status[]&#x60; param.
    :type with_completed: bool
    :param order_by: 
    :type order_by: str
    :param order_type: 
    :type order_type: dict | bytes
    :param _with: Include detailed information. Possible values &#39;client&#39;, &#39;vendor&#39;
    :type _with: List[str]

    """
    status = [ProjectStatus.from_dict(d) for d in status]
    order_type = .from_dict(order_type)
    return web.Response(status=200)


async def get_quote_id_from_internal_id(request: web.Request, project_id) -> web.Response:
    """Get Quote Id

    Get Quote Id

    :param project_id: Project ID
    :type project_id: int

    """
    return web.Response(status=200)


async def get_vendor_projects(request: web.Request, joined=None, completed=None, page=None, per_page=None) -> web.Response:
    """List projects as a vendor

    Get a list of projects that are available to you to work on as a vendor. This is not a list of projects that you ordered as a customer.

    :param joined: Return only projects that this user has already joined
    :type joined: bool
    :param completed: Return only projects that have been completed. When &#x60;true&#x60;, this makes &#x60;joined&#x60; true as well.
    :type completed: bool
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)


async def get_vendor_projects_by_user_id(request: web.Request, user_id, joined=None, completed=None, page=None, per_page=None) -> web.Response:
    """Get a list of user/vendor projects

    Get a list of user/vendor projects

    :param user_id: User ID
    :type user_id: int
    :param joined: Return only projects that this user has already joined
    :type joined: bool
    :param completed: Return only projects that have been completed. When &#x60;true&#x60;, this makes &#x60;joined&#x60; true as well.
    :type completed: bool
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)


async def launch_project(request: web.Request, id, body=None) -> web.Response:
    """Launch your translation project

    Launch your translation project so MotaWord can actually start working on your translation.

    :param id: Project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectPayment.from_dict(body)
    return web.Response(status=200)


async def package(request: web.Request, id, _async=None) -> web.Response:
    """Package your translated project

    Package the translations in your project, prepare translated documents and make it ready to be downloaded. Once packaged, you can download your translated project.

    :param id: Project ID
    :type id: int
    :param _async: If you want to package and download the translation synchronously, mark this parameter as &#39;0&#39;. It will package the translation and then return the packaged file in the response, identical to /download call after an asynchronous /package call.
    :type _async: int

    """
    return web.Response(status=200)


async def package_language(request: web.Request, id, language, _async=None) -> web.Response:
    """Package your translated project language

    Package the translations in your project for a specific target language, prepare translated documents and make it ready to be downloaded. Once packaged, you can download your translated project in this target language.

    :param id: Project ID
    :type id: int
    :param language: Language code. You can package the translation of only a specific language.
    :type language: str
    :param _async: If you want to package and download the translation synchronously, mark this parameter as &#39;0&#39;. It will package the translation and then return the packaged file in the response, identical to /download call after an asynchronous /package call.
    :type _async: int

    """
    return web.Response(status=200)


async def recreate_project(request: web.Request, id) -> web.Response:
    """Recreate your translation project from scratch. This is a risky action, you will lose current translations.

    

    :param id: Project ID
    :type id: int

    """
    return web.Response(status=200)


async def send_quote_email(request: web.Request, id) -> web.Response:
    """Send a quote email

    Send a quote email

    :param id: Project ID
    :type id: int

    """
    return web.Response(status=200)


async def submit_project_reports(request: web.Request, id, body=None) -> web.Response:
    """Submit feedback report for a project

    

    :param id: Project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReportContent.from_dict(body)
    return web.Response(status=200)


async def track_package(request: web.Request, id, key=None) -> web.Response:
    """Track translation packaging status

    Track the packaging status of your translations, by using the &#x60;key&#x60; from packaging request. Once packaging is completed, you can download your translations via &#x60;/download&#x60; endpoints.

    :param id: Project ID
    :type id: int
    :param key: This is the package tracking key provided in the response of a /package call.
    :type key: str

    """
    return web.Response(status=200)


async def trigger_callback(request: web.Request, id, action_type) -> web.Response:
    """Trigger a call to your callback URL related to this project.

    Trigger a call to your callback URL related to this project.

    :param id: Project ID
    :type id: int
    :param action_type: Callback type
    :type action_type: str

    """
    return web.Response(status=200)


async def update_project(request: web.Request, id, body=None) -> web.Response:
    """Update project info and settings

    

    :param id: Project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectUpdate.from_dict(body)
    return web.Response(status=200)
