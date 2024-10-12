from typing import List, Dict
from aiohttp import web

from openapi_server.models.active_widget import ActiveWidget
from openapi_server.models.active_widget_list import ActiveWidgetList
from openapi_server.models.add_or_update_document_request import AddOrUpdateDocumentRequest
from openapi_server.models.analytics_collection import AnalyticsCollection
from openapi_server.models.analytics_token import AnalyticsToken
from openapi_server.models.continuous_project import ContinuousProject
from openapi_server.models.continuous_project_document import ContinuousProjectDocument
from openapi_server.models.continuous_project_document_list import ContinuousProjectDocumentList
from openapi_server.models.continuous_project_document_progress_body import ContinuousProjectDocumentProgressBody
from openapi_server.models.continuous_project_invoices import ContinuousProjectInvoices
from openapi_server.models.continuous_project_progress import ContinuousProjectProgress
from openapi_server.models.continuous_project_update_content import ContinuousProjectUpdateContent
from openapi_server.models.continuous_projects_list import ContinuousProjectsList
from openapi_server.models.error import Error
from openapi_server.models.get_quotes_for_documents_body import GetQuotesForDocumentsBody
from openapi_server.models.get_quotes_for_languages_body import GetQuotesForLanguagesBody
from openapi_server.models.instant_translation_request import InstantTranslationRequest
from openapi_server.models.instant_translation_result import InstantTranslationResult
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.progress import Progress
from openapi_server.models.project_list import ProjectList
from openapi_server.models.subscription import Subscription
from openapi_server import util


async def add_document(request: web.Request, project_id, body=None) -> web.Response:
    """Add a new document to your continuous project

    Add a new document to your continuous project. If the name already exists, it will update the existing document. In most scenarios, this operation will also trigger auto-translation of your document, via MT and/or TM.

    :param project_id: Continuous project ID
    :type project_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AddOrUpdateDocumentRequest.from_dict(body)
    return web.Response(status=200)


async def collect_analytics(request: web.Request, id, body=None) -> web.Response:
    """Save/collect analytics data from Active widget

    Save/collect analytics data from Active widget

    :param id: Continuous project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AnalyticsCollection.from_dict(body)
    return web.Response(status=200)


async def complete(request: web.Request, id) -> web.Response:
    """Complete continuous project

    Complete continuous project

    :param id: Continuous project ID
    :type id: int

    """
    return web.Response(status=200)


async def complete_continuous_document(request: web.Request, id, document_id) -> web.Response:
    """Complete a continuous project document

    Complete a continuous project document. Per your project settings, a continuous project document can be target language-specific or project-wide for all target languages of the project.

    :param id: Continuous project ID
    :type id: int
    :param document_id: Document ID
    :type document_id: int

    """
    return web.Response(status=200)


async def complete_language(request: web.Request, id, target_language) -> web.Response:
    """Complete continuous project language

    Complete continuous project language

    :param id: Continuous project ID
    :type id: int
    :param target_language: Target language that you want to complete
    :type target_language: str

    """
    return web.Response(status=200)


async def create_active_widget(request: web.Request, project_id, body=None) -> web.Response:
    """Create a new Active widget

    Create a new widget for your Active project to be used in your website. Most website-specific configuration is provided via widgets. This does not create a new Active project, just a separate widget.

    :param project_id: Continuous project ID
    :type project_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ActiveWidget.from_dict(body)
    return web.Response(status=200)


async def create_continuous_project(request: web.Request, body=None) -> web.Response:
    """Create a continuous project

    Create a new continuous project for your software, website, CI/CD translation needs.

    :param body: 
    :type body: dict | bytes

    """
    body = ContinuousProject.from_dict(body)
    return web.Response(status=200)


async def create_subscription(request: web.Request, id, body) -> web.Response:
    """Create subscription for continuous project

    Create subscription for continuous project

    :param id: Continuous project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Subscription.from_dict(body)
    return web.Response(status=200)


async def delete_active_widget(request: web.Request, project_id, widget_id) -> web.Response:
    """Delete a single widget for this Active project

    Delete a single widget for this Active project

    :param project_id: Continuous Project ID
    :type project_id: int
    :param widget_id: Active widget ID belonging to this Continuous Project
    :type widget_id: int

    """
    return web.Response(status=200)


async def delete_continuous_project(request: web.Request, id) -> web.Response:
    """Delete a continuous project

    Delete an existing continuous project. Your project will be cancelled, and you will still be charged for the amount of translations we have done for you so far.

    :param id: Continuous project ID
    :type id: int

    """
    return web.Response(status=200)


async def delete_subscription(request: web.Request, id) -> web.Response:
    """Delete subscription for continuous project

    Delete subscription for continuous project

    :param id: Continuous project ID
    :type id: int

    """
    return web.Response(status=200)


async def get_active_widget(request: web.Request, project_id, widget_id) -> web.Response:
    """View an Active widget

    View the details of an Active widget to be used in your website. Most website-specific configuration is provided via widgets.

    :param project_id: Continuous Project ID
    :type project_id: int
    :param widget_id: Active widget ID belonging to this Continuous Project
    :type widget_id: int

    """
    return web.Response(status=200)


async def get_active_widgets(request: web.Request, project_id) -> web.Response:
    """View Active widgets

    View a list of widgets in your Active project to be used in your website. Most website-specific configuration is provided via widgets.

    :param project_id: Continuous Project ID
    :type project_id: int

    """
    return web.Response(status=200)


async def get_analytics_token(request: web.Request, id) -> web.Response:
    """Get JWT token to be used in analytics dashboards

    Get JWT token to be used in analytics dashboards

    :param id: Continuous project ID
    :type id: int

    """
    return web.Response(status=200)


async def get_continuous_project(request: web.Request, id) -> web.Response:
    """View a continuous project

    View the details of a continuous project.

    :param id: Continuous Project ID
    :type id: int

    """
    return web.Response(status=200)


async def get_continuous_project_document(request: web.Request, project_id, document_id) -> web.Response:
    """View a continuous document

    View the details of a source document in continuous translation project.

    :param project_id: Continuous project ID
    :type project_id: int
    :param document_id: Document ID/Name
    :type document_id: int

    """
    return web.Response(status=200)


async def get_continuous_project_document_progress(request: web.Request, project_id, document_id, filter_by_language=None) -> web.Response:
    """Monitor progress of a continuous document

    Monitor the translation progress of a document in a continuous project in real-time.

    :param project_id: Continuous project ID
    :type project_id: int
    :param document_id: Document ID/Name
    :type document_id: int
    :param filter_by_language: 
    :type filter_by_language: str

    """
    return web.Response(status=200)


async def get_continuous_project_documents(request: web.Request, project_id, filter_by_language=None) -> web.Response:
    """View continuous documents

    View the documents under this continuous project

    :param project_id: Continuous Project ID
    :type project_id: int
    :param filter_by_language: 
    :type filter_by_language: str

    """
    return web.Response(status=200)


async def get_continuous_project_invoices(request: web.Request, project_id) -> web.Response:
    """Invoices of a continuous project

    Get real-time access to a continuous project&#39;s invoices.

    :param project_id: Project ID
    :type project_id: int

    """
    return web.Response(status=200)


async def get_continuous_project_progress(request: web.Request, project_id, filter_by_language=None) -> web.Response:
    """Monitor progress and status of a continous project

    Monitor the translation progress of an ongoing continuous project in real-time.

    :param project_id: Project ID
    :type project_id: int
    :param filter_by_language: 
    :type filter_by_language: str

    """
    return web.Response(status=200)


async def get_continuous_projects(request: web.Request, type=None) -> web.Response:
    """View continuous projects

    View a list of continuous projects under your account. Continuous projects are those that are constantly updated, such as a CI/CD project, software project, website translation and such.

    :param type: Type of continuous project.
    :type type: str

    """
    return web.Response(status=200)


async def get_quote_for_document(request: web.Request, id, document_id) -> web.Response:
    """Get a quote for a continuous project document

    Get a new quote for provided document in continuous project. Per your project settings, a continuous project document can be target language-specific or project-wide for all target languages of the project.

    :param id: Continuous project ID
    :type id: int
    :param document_id: Document ID
    :type document_id: int

    """
    return web.Response(status=200)


async def get_quote_for_documents(request: web.Request, id, body=None) -> web.Response:
    """Get quote for documents

    Get a new quote for provided documents in continuous project

    :param id: Continuous project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = GetQuotesForDocumentsBody.from_dict(body)
    return web.Response(status=200)


async def get_quote_for_language(request: web.Request, id, target_language) -> web.Response:
    """Get quote for language

    Get a new quote for provided target language in continuous project

    :param id: Continuous project ID
    :type id: int
    :param target_language: Target language that you want to complete
    :type target_language: str

    """
    return web.Response(status=200)


async def get_quote_for_languages(request: web.Request, id, body=None) -> web.Response:
    """Get quote for languages

    Get a new quote for provided target languages in continuous project

    :param id: Continuous project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = GetQuotesForLanguagesBody.from_dict(body)
    return web.Response(status=200)


async def get_subscription(request: web.Request, id) -> web.Response:
    """Get subscription for continuous project

    Get subscription for continuous project

    :param id: Continuous project ID
    :type id: int

    """
    return web.Response(status=200)


async def post_continuous_project_document_progress(request: web.Request, project_id, body=None) -> web.Response:
    """Get continuous project document progress for multiple IDs

    Get continuous project document progress for multiple IDs

    :param project_id: Continuous project ID
    :type project_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ContinuousProjectDocumentProgressBody.from_dict(body)
    return web.Response(status=200)


async def reset_active_widget_token(request: web.Request, project_id, widget_id) -> web.Response:
    """Reset Active widget token

    Reset the public token used with your Active widget. This token is used when communicating from your environment to MotaWord systems for translation, analytics and meta.

    :param project_id: Continuous Project ID
    :type project_id: int
    :param widget_id: Active widget ID belonging to this Continuous Project
    :type widget_id: int

    """
    return web.Response(status=200)


async def translate(request: web.Request, id, target_language, body=None) -> web.Response:
    """Instantly translate your content

    Instantly translate your content with your existing TM and MT resources. This is the primary endpoint to translate your files and content on the fly, especially in CI/CD environments. This is a complex endpoint that is configured in your Active or Continuous Project dashboards. For instance, you can configure whether to use your TM, or translate missing strings via MT and then post-edit those new translations. There are various scenarios you can establish via a set of configurations.

    :param id: Continuous project ID
    :type id: int
    :param target_language: Target language that you want to instantly translate your file into.
    :type target_language: str
    :param body: 
    :type body: dict | bytes

    """
    body = InstantTranslationRequest.from_dict(body)
    return web.Response(status=200)


async def update_active_widget(request: web.Request, project_id, widget_id, body=None) -> web.Response:
    """Update Active widget settings.

    Update Active widget settings.

    :param project_id: Continuous Project ID
    :type project_id: int
    :param widget_id: Active widget ID belonging to this Continuous Project
    :type widget_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ActiveWidget.from_dict(body)
    return web.Response(status=200)


async def update_continuous_project(request: web.Request, id, body=None) -> web.Response:
    """Update a continuous project

    Update the details and settings of continuous project.

    :param id: Continuous project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ContinuousProjectUpdateContent.from_dict(body)
    return web.Response(status=200)


async def update_document(request: web.Request, project_id, document_id, body=None) -> web.Response:
    """Update the document

    Update source document in your continuous project. In most scenarios, this operation will also trigger auto-translation of your document, via MT and/or TM.

    :param project_id: Continuous project ID
    :type project_id: int
    :param document_id: Continuous project document ID
    :type document_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AddOrUpdateDocumentRequest.from_dict(body)
    return web.Response(status=200)


async def update_subscription(request: web.Request, id, body) -> web.Response:
    """Update subscription for continuous project

    Update subscription for continuous project

    :param id: Continuous project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Subscription.from_dict(body)
    return web.Response(status=200)


async def update_subscription_payment_method(request: web.Request, id, body) -> web.Response:
    """Update subscription payment method for continuous project

    Update subscription payment method for continuous project

    :param id: Continuous project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Subscription.from_dict(body)
    return web.Response(status=200)
