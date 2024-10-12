# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_add_document(client):
    """Test case for add_document

    Add a new document to your continuous project
    """
    body = {"document":{"data":"data","name":"name"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{project_id}/documents'.format(project_id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collect_analytics(client):
    """Test case for collect_analytics

    Save/collect analytics data from Active widget
    """
    body = {"anonymousId":"anonymousId","sessionId":"sessionId","type":"type","userId":"userId","properties":{"key":"properties"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{id}/collect-analytics'.format(id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete(client):
    """Test case for complete

    Complete continuous project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{id}/complete'.format(id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_continuous_document(client):
    """Test case for complete_continuous_document

    Complete a continuous project document
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{id}/documents/{document_id}/complete'.format(id=74, document_id=179469),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_language(client):
    """Test case for complete_language

    Complete continuous project language
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{id}/languages/{target_language}/complete'.format(id=74, target_language='en-US'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_active_widget(client):
    """Test case for create_active_widget

    Create a new Active widget
    """
    body = {"debug_mode":True,"restricted_domains":"restricted_domains","created_at":"2000-01-23T04:56:07.000+00:00","use_cache":True,"reboot_on_url_change":True,"admin_mode":True,"pages":"pages","query_name":"locale","test_mode":True,"theme":"theme","url_mode":"url_mode","id":0,"url_change_mode":"url_change_mode","live":True,"allow_query_in_url":True,"force_cache_refresh_interval":True,"path_regex":"path_regex","variables":"variables","hit_backend_for_existing":True,"use_dummy_translations":True,"modify_links":True,"sections":"sections","token":"token","language_mappings":"language_mappings","allow_hash_in_url":True,"follow_user":True,"auto_detect_source_language":True,"elements":"elements","name":"name","position":"position","optimize_per_page":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{project_id}/widgets'.format(project_id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_continuous_project(client):
    """Test case for create_continuous_project

    Create a continuous project
    """
    body = {"target_languages":["target_languages","target_languages"],"source_language":"source_language","created_at":"2000-01-23T04:56:07.000+00:00","mt_engine":"mt_engine","subscription":{"period_end":"2000-01-23T04:56:07.000+00:00","subscription_id":"subscription_id","upgrade":["upgrade","upgrade"],"price":"price","withTrial":"","downgrade":["downgrade","downgrade"],"schedule_name":"schedule_name","payment_method":6,"plan_id":"plan_id","plan_name":"plan_name","products":["",""],"schedule_start":"2000-01-23T04:56:07.000+00:00"},"type":"type","auto_start_postedit":True,"postedit_enabled":True,"mt_enabled":True,"is_enabled":True,"word_count":1,"analytics_enabled":True,"last_activity_at":"2000-01-23T04:56:07.000+00:00","name":"name","links":{"self":{"href":"href"},"editors":{"key":{"href":"href"}}},"id":0,"status":"status"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_subscription(client):
    """Test case for create_subscription

    Create subscription for continuous project
    """
    body = {"period_end":"2000-01-23T04:56:07.000+00:00","subscription_id":"subscription_id","upgrade":["upgrade","upgrade"],"price":"price","withTrial":"","downgrade":["downgrade","downgrade"],"schedule_name":"schedule_name","payment_method":6,"plan_id":"plan_id","plan_name":"plan_name","products":["",""],"schedule_start":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{id}/subscription'.format(id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_active_widget(client):
    """Test case for delete_active_widget

    Delete a single widget for this Active project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/continuous_projects/{project_id}/widgets/{widget_id}'.format(project_id=74, widget_id=236),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_continuous_project(client):
    """Test case for delete_continuous_project

    Delete a continuous project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/continuous_projects/{id}'.format(id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_subscription(client):
    """Test case for delete_subscription

    Delete subscription for continuous project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/continuous_projects/{id}/subscription'.format(id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_active_widget(client):
    """Test case for get_active_widget

    View an Active widget
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/continuous_projects/{project_id}/widgets/{widget_id}'.format(project_id=74, widget_id=236),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_active_widgets(client):
    """Test case for get_active_widgets

    View Active widgets
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/continuous_projects/{project_id}/widgets'.format(project_id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_analytics_token(client):
    """Test case for get_analytics_token

    Get JWT token to be used in analytics dashboards
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/continuous_projects/{id}/analytics-token'.format(id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_continuous_project(client):
    """Test case for get_continuous_project

    View a continuous project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/continuous_projects/{id}'.format(id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_continuous_project_document(client):
    """Test case for get_continuous_project_document

    View a continuous document
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/continuous_projects/{project_id}/documents/{document_id}'.format(project_id=74, document_id=179469),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_continuous_project_document_progress(client):
    """Test case for get_continuous_project_document_progress

    Monitor progress of a continuous document
    """
    params = [('filterByLanguage', 'filter_by_language_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/continuous_projects/{project_id}/documents/{document_id}/progress'.format(project_id=74, document_id=179469),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_continuous_project_documents(client):
    """Test case for get_continuous_project_documents

    View continuous documents
    """
    params = [('filterByLanguage', 'filter_by_language_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/continuous_projects/{project_id}/documents'.format(project_id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_continuous_project_invoices(client):
    """Test case for get_continuous_project_invoices

    Invoices of a continuous project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/continuous_projects/{project_id}/invoices'.format(project_id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_continuous_project_progress(client):
    """Test case for get_continuous_project_progress

    Monitor progress and status of a continous project
    """
    params = [('filterByLanguage', 'filter_by_language_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/continuous_projects/{project_id}/progress'.format(project_id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_continuous_projects(client):
    """Test case for get_continuous_projects

    View continuous projects
    """
    params = [('type', active)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/continuous_projects',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_for_document(client):
    """Test case for get_quote_for_document

    Get a quote for a continuous project document
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{id}/documents/{document_id}/quote'.format(id=74, document_id=179469),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_for_documents(client):
    """Test case for get_quote_for_documents

    Get quote for documents
    """
    body = {"files":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{id}/documents/quote'.format(id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_for_language(client):
    """Test case for get_quote_for_language

    Get quote for language
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{id}/languages/{target_language}/quote'.format(id=74, target_language='en-US'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_for_languages(client):
    """Test case for get_quote_for_languages

    Get quote for languages
    """
    body = {"languages":["languages","languages"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{id}/languages/quote'.format(id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription(client):
    """Test case for get_subscription

    Get subscription for continuous project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/continuous_projects/{id}/subscription'.format(id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_continuous_project_document_progress(client):
    """Test case for post_continuous_project_document_progress

    Get continuous project document progress for multiple IDs
    """
    body = {"filterByLanguage":"filterByLanguage","documentName":"documentName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{project_id}/documents/progress'.format(project_id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_active_widget_token(client):
    """Test case for reset_active_widget_token

    Reset Active widget token
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{project_id}/widgets/{widget_id}/reset-token'.format(project_id=74, widget_id=236),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate(client):
    """Test case for translate

    Instantly translate your content
    """
    body = {"contents":["contents","contents"],"documents":[{"data":"data","name":"name"},{"data":"data","name":"name"}],"meta":"{}","filters":{"skipMt":["skipMt","skipMt"],"skipPostEdit":["skipPostEdit","skipPostEdit"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{id}/translate/{target_language}'.format(id=74, target_language='en-US'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_active_widget(client):
    """Test case for update_active_widget

    Update Active widget settings.
    """
    body = {"debug_mode":True,"restricted_domains":"restricted_domains","created_at":"2000-01-23T04:56:07.000+00:00","use_cache":True,"reboot_on_url_change":True,"admin_mode":True,"pages":"pages","query_name":"locale","test_mode":True,"theme":"theme","url_mode":"url_mode","id":0,"url_change_mode":"url_change_mode","live":True,"allow_query_in_url":True,"force_cache_refresh_interval":True,"path_regex":"path_regex","variables":"variables","hit_backend_for_existing":True,"use_dummy_translations":True,"modify_links":True,"sections":"sections","token":"token","language_mappings":"language_mappings","allow_hash_in_url":True,"follow_user":True,"auto_detect_source_language":True,"elements":"elements","name":"name","position":"position","optimize_per_page":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{project_id}/widgets/{widget_id}'.format(project_id=74, widget_id=236),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_continuous_project(client):
    """Test case for update_continuous_project

    Update a continuous project
    """
    body = {"is_enabled":True,"analytics_enabled":True,"languages":[{"is_enabled":True,"code":"code"},{"is_enabled":True,"code":"code"}],"name":"name","auto_start_postedit":True,"postedit_enabled":True,"mt_enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{id}'.format(id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_document(client):
    """Test case for update_document

    Update the document
    """
    body = {"document":{"data":"data","name":"name"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{project_id}/documents/{document_id}'.format(project_id=74, document_id=179469),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_subscription(client):
    """Test case for update_subscription

    Update subscription for continuous project
    """
    body = {"period_end":"2000-01-23T04:56:07.000+00:00","subscription_id":"subscription_id","upgrade":["upgrade","upgrade"],"price":"price","withTrial":"","downgrade":["downgrade","downgrade"],"schedule_name":"schedule_name","payment_method":6,"plan_id":"plan_id","plan_name":"plan_name","products":["",""],"schedule_start":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/continuous_projects/{id}/subscription'.format(id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_subscription_payment_method(client):
    """Test case for update_subscription_payment_method

    Update subscription payment method for continuous project
    """
    body = {"period_end":"2000-01-23T04:56:07.000+00:00","subscription_id":"subscription_id","upgrade":["upgrade","upgrade"],"price":"price","withTrial":"","downgrade":["downgrade","downgrade"],"schedule_name":"schedule_name","payment_method":6,"plan_id":"plan_id","plan_name":"plan_name","products":["",""],"schedule_start":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/continuous_projects/{id}/subscription/payment'.format(id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

