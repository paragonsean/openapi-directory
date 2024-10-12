# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_client import AppClient
from openapi_server.models.app_clients import AppClients
from openapi_server.models.asset import Asset
from openapi_server.models.assets import Assets
from openapi_server.models.data_bundle import DataBundle
from openapi_server.models.data_bundles import DataBundles
from openapi_server.models.dataset import Dataset
from openapi_server.models.datasets import Datasets
from openapi_server.models.deployment_environment import DeploymentEnvironment
from openapi_server.models.deployment_environments import DeploymentEnvironments
from openapi_server.models.document import Document
from openapi_server.models.documents import Documents
from openapi_server.models.error import Error
from openapi_server.models.log import Log
from openapi_server.models.logs import Logs
from openapi_server.models.model import Model
from openapi_server.models.models import Models
from openapi_server.models.organization import Organization
from openapi_server.models.organizations import Organizations
from openapi_server.models.patch_app_client_id import PatchAppClientId
from openapi_server.models.patch_asset_id import PatchAssetId
from openapi_server.models.patch_data_bundle_id import PatchDataBundleId
from openapi_server.models.patch_dataset_id import PatchDatasetId
from openapi_server.models.patch_document_id import PatchDocumentId
from openapi_server.models.patch_model_id import PatchModelId
from openapi_server.models.patch_organization_id import PatchOrganizationId
from openapi_server.models.patch_payment_method_id import PatchPaymentMethodId
from openapi_server.models.patch_secret_id import PatchSecretId
from openapi_server.models.patch_training_id import PatchTrainingId
from openapi_server.models.patch_transistion_execution_id import PatchTransistionExecutionId
from openapi_server.models.patch_transition_id import PatchTransitionId
from openapi_server.models.patch_user_id import PatchUserId
from openapi_server.models.patch_workflow_execution_id import PatchWorkflowExecutionId
from openapi_server.models.patch_workflow_id import PatchWorkflowId
from openapi_server.models.payment_method import PaymentMethod
from openapi_server.models.payment_methods import PaymentMethods
from openapi_server.models.plan import Plan
from openapi_server.models.plans import Plans
from openapi_server.models.post_app_clients import PostAppClients
from openapi_server.models.post_assets import PostAssets
from openapi_server.models.post_data_bundles import PostDataBundles
from openapi_server.models.post_datasets import PostDatasets
from openapi_server.models.post_documents import PostDocuments
from openapi_server.models.post_models import PostModels
from openapi_server.models.post_organizations import PostOrganizations
from openapi_server.models.post_payment_methods import PostPaymentMethods
from openapi_server.models.post_predictions import PostPredictions
from openapi_server.models.post_secrets import PostSecrets
from openapi_server.models.post_trainings import PostTrainings
from openapi_server.models.post_transitions import PostTransitions
from openapi_server.models.post_users import PostUsers
from openapi_server.models.post_workflow_executions import PostWorkflowExecutions
from openapi_server.models.post_workflows import PostWorkflows
from openapi_server.models.prediction import Prediction
from openapi_server.models.predictions import Predictions
from openapi_server.models.profile import Profile
from openapi_server.models.secret import Secret
from openapi_server.models.secrets import Secrets
from openapi_server.models.training import Training
from openapi_server.models.trainings import Trainings
from openapi_server.models.transition import Transition
from openapi_server.models.transition_execution import TransitionExecution
from openapi_server.models.transition_executions import TransitionExecutions
from openapi_server.models.transitions import Transitions
from openapi_server.models.user import User
from openapi_server.models.users import Users
from openapi_server.models.workflow import Workflow
from openapi_server.models.workflow_execution import WorkflowExecution
from openapi_server.models.workflow_executions import WorkflowExecutions
from openapi_server.models.workflows import Workflows


pytestmark = pytest.mark.asyncio

async def test_app_clients_app_client_id_delete(client):
    """Test case for app_clients_app_client_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/appClients/{app_client_id}'.format(app_client_id='app_client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_clients_app_client_id_options(client):
    """Test case for app_clients_app_client_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/appClients/{app_client_id}'.format(app_client_id='app_client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_clients_app_client_id_patch(client):
    """Test case for app_clients_app_client_id_patch

    
    """
    body = {"name":"name","description":"description","loginUrls":["loginUrls","loginUrls"],"defaultLoginUrl":"defaultLoginUrl"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/appClients/{app_client_id}'.format(app_client_id='app_client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_clients_get(client):
    """Test case for app_clients_get

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appClients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_clients_options(client):
    """Test case for app_clients_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/appClients',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_clients_post(client):
    """Test case for app_clients_post

    
    """
    body = {"generateSecret":True,"logoutUrls":["logoutUrls","logoutUrls"],"name":"name","callbackUrls":["callbackUrls","callbackUrls"],"description":"description","loginUrls":["loginUrls","loginUrls"],"defaultLoginUrl":"defaultLoginUrl"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/appClients',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_asset_id_delete(client):
    """Test case for assets_asset_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/assets/{asset_id}'.format(asset_id='asset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_asset_id_get(client):
    """Test case for assets_asset_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/assets/{asset_id}'.format(asset_id='asset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_asset_id_options(client):
    """Test case for assets_asset_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/assets/{asset_id}'.format(asset_id='asset_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_asset_id_patch(client):
    """Test case for assets_asset_id_patch

    
    """
    body = {"name":"name","description":"description","content":"content"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/assets/{asset_id}'.format(asset_id='asset_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_get(client):
    """Test case for assets_get

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/assets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_options(client):
    """Test case for assets_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/assets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_post(client):
    """Test case for assets_post

    
    """
    body = {"name":"name","description":"description","content":"content"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/assets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datasets_dataset_id_delete(client):
    """Test case for datasets_dataset_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/datasets/{dataset_id}'.format(dataset_id='dataset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datasets_dataset_id_get(client):
    """Test case for datasets_dataset_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/datasets/{dataset_id}'.format(dataset_id='dataset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datasets_dataset_id_options(client):
    """Test case for datasets_dataset_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/datasets/{dataset_id}'.format(dataset_id='dataset_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datasets_dataset_id_patch(client):
    """Test case for datasets_dataset_id_patch

    
    """
    body = {"metadata":"{}","retentionInDays":1,"name":"name","description":"description","containsPersonallyIdentifiableInformation":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/datasets/{dataset_id}'.format(dataset_id='dataset_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datasets_get(client):
    """Test case for datasets_get

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/datasets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datasets_options(client):
    """Test case for datasets_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/datasets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datasets_post(client):
    """Test case for datasets_post

    
    """
    body = {"metadata":"{}","retentionInDays":1,"name":"name","description":"description","containsPersonallyIdentifiableInformation":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/datasets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_environments_deployment_environment_id_get(client):
    """Test case for deployment_environments_deployment_environment_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/deploymentEnvironments/{deployment_environment_id}'.format(deployment_environment_id='deployment_environment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_environments_deployment_environment_id_options(client):
    """Test case for deployment_environments_deployment_environment_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/deploymentEnvironments/{deployment_environment_id}'.format(deployment_environment_id='deployment_environment_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_environments_get(client):
    """Test case for deployment_environments_get

    
    """
    params = [('owner', 'owner_example'),
                    ('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/deploymentEnvironments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_environments_options(client):
    """Test case for deployment_environments_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/deploymentEnvironments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_delete(client):
    """Test case for documents_delete

    
    """
    params = [('consentId', 'consent_id_example'),
                    ('datasetId', 'dataset_id_example'),
                    ('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_document_id_delete(client):
    """Test case for documents_document_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/documents/{document_id}'.format(document_id='document_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_document_id_get(client):
    """Test case for documents_document_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/documents/{document_id}'.format(document_id='document_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_document_id_options(client):
    """Test case for documents_document_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/documents/{document_id}'.format(document_id='document_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_document_id_patch(client):
    """Test case for documents_document_id_patch

    
    """
    body = {"groundTruth":[{"label":"label","value":"Document_groundTruth_inner_value"},{"label":"label","value":"Document_groundTruth_inner_value"}],"metadata":"{}","retentionInDays":1,"name":"name","datasetId":"datasetId","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/documents/{document_id}'.format(document_id='document_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_get(client):
    """Test case for documents_get

    
    """
    params = [('datasetId', 'dataset_id_example'),
                    ('nextToken', 'next_token_example'),
                    ('order', 'order_example'),
                    ('documentId', 'document_id_example'),
                    ('consentId', 'consent_id_example'),
                    ('maxResults', 'max_results_example'),
                    ('sortBy', 'sort_by_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_options(client):
    """Test case for documents_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/documents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_post(client):
    """Test case for documents_post

    
    """
    body = {"groundTruth":[{"label":"label","value":"Document_groundTruth_inner_value"},{"label":"label","value":"Document_groundTruth_inner_value"}],"consentId":"consentId","metadata":"{}","retentionInDays":1,"name":"name","datasetId":"datasetId","description":"description","contentType":"application/pdf","content":"content"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/documents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_get(client):
    """Test case for logs_get

    
    """
    params = [('workflowId', 'workflow_id_example'),
                    ('nextToken', 'next_token_example'),
                    ('order', 'order_example'),
                    ('transitionExecutionId', 'transition_execution_id_example'),
                    ('transitionId', 'transition_id_example'),
                    ('maxResults', 'max_results_example'),
                    ('workflowExecutionId', 'workflow_execution_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/logs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_log_id_get(client):
    """Test case for logs_log_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/logs/{log_id}'.format(log_id='log_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_log_id_options(client):
    """Test case for logs_log_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/logs/{log_id}'.format(log_id='log_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_options(client):
    """Test case for logs_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/logs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_get(client):
    """Test case for models_get

    
    """
    params = [('owner', 'owner_example'),
                    ('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/models',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_data_bundles_data_bundle_id_delete(client):
    """Test case for models_model_id_data_bundles_data_bundle_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/models/{model_id}/dataBundles/{data_bundle_id}'.format(data_bundle_id='data_bundle_id_example', model_id='model_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_data_bundles_data_bundle_id_options(client):
    """Test case for models_model_id_data_bundles_data_bundle_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/models/{model_id}/dataBundles/{data_bundle_id}'.format(data_bundle_id='data_bundle_id_example', model_id='model_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_data_bundles_data_bundle_id_patch(client):
    """Test case for models_model_id_data_bundles_data_bundle_id_patch

    
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/models/{model_id}/dataBundles/{data_bundle_id}'.format(data_bundle_id='data_bundle_id_example', model_id='model_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_data_bundles_get(client):
    """Test case for models_model_id_data_bundles_get

    
    """
    params = [('status', 'status_example'),
                    ('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/models/{model_id}/dataBundles'.format(model_id='model_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_data_bundles_options(client):
    """Test case for models_model_id_data_bundles_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/models/{model_id}/dataBundles'.format(model_id='model_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_data_bundles_post(client):
    """Test case for models_model_id_data_bundles_post

    
    """
    body = {"datasetIds":["datasetIds","datasetIds"],"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/models/{model_id}/dataBundles'.format(model_id='model_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_delete(client):
    """Test case for models_model_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/models/{model_id}'.format(model_id='model_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_get(client):
    """Test case for models_model_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/models/{model_id}'.format(model_id='model_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_options(client):
    """Test case for models_model_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/models/{model_id}'.format(model_id='model_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_patch(client):
    """Test case for models_model_id_patch

    
    """
    body = {"metadata":"{}","preprocessConfig":{"maxPages":2,"autoRotate":True,"imageQuality":"LOW"},"trainingId":"trainingId","postprocessConfig":{"strategy":"BEST_FIRST"},"name":"name","description":"description","fieldConfig":{"key":{"description":"description","type":"amount","enum":["enum","enum","enum","enum","enum"],"maxLength":41}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/models/{model_id}'.format(model_id='model_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_trainings_get(client):
    """Test case for models_model_id_trainings_get

    
    """
    params = [('status', 'status_example'),
                    ('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/models/{model_id}/trainings'.format(model_id='model_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_trainings_options(client):
    """Test case for models_model_id_trainings_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/models/{model_id}/trainings'.format(model_id='model_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_trainings_post(client):
    """Test case for models_model_id_trainings_post

    
    """
    body = {"dataScientistAssistance":True,"metadata":"{}","warmStartConfig":{"trainingId":"trainingId"},"instanceType":"small-gpu","dataBundleIds":["dataBundleIds","dataBundleIds"],"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/models/{model_id}/trainings'.format(model_id='model_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_trainings_training_id_options(client):
    """Test case for models_model_id_trainings_training_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/models/{model_id}/trainings/{training_id}'.format(model_id='model_id_example', training_id='training_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_model_id_trainings_training_id_patch(client):
    """Test case for models_model_id_trainings_training_id_patch

    
    """
    body = {"deploymentEnvironmentId":"deploymentEnvironmentId","metadata":"{}","name":"name","description":"description","status":"cancelled"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/models/{model_id}/trainings/{training_id}'.format(model_id='model_id_example', training_id='training_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_options(client):
    """Test case for models_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/models',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_models_post(client):
    """Test case for models_post

    
    """
    body = {"metadata":"{}","preprocessConfig":{"maxPages":2,"autoRotate":True,"imageQuality":"LOW"},"postprocessConfig":{"strategy":"BEST_FIRST"},"name":"name","description":"description","fieldConfig":{"key":{"description":"description","type":"amount","enum":["enum","enum","enum","enum","enum"],"maxLength":41}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/models',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizations_get(client):
    """Test case for organizations_get

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/organizations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizations_options(client):
    """Test case for organizations_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/organizations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizations_organization_id_get(client):
    """Test case for organizations_organization_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/organizations/{organization_id}'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizations_organization_id_options(client):
    """Test case for organizations_organization_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/organizations/{organization_id}'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizations_organization_id_patch(client):
    """Test case for organizations_organization_id_patch

    
    """
    body = {"paymentMethodId":"paymentMethodId","name":"name","description":"description","planId":"planId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/organizations/{organization_id}'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizations_post(client):
    """Test case for organizations_post

    
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/organizations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_methods_get(client):
    """Test case for payment_methods_get

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/paymentMethods',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_methods_options(client):
    """Test case for payment_methods_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/paymentMethods',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_methods_payment_method_id_delete(client):
    """Test case for payment_methods_payment_method_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/paymentMethods/{payment_method_id}'.format(payment_method_id='payment_method_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_methods_payment_method_id_get(client):
    """Test case for payment_methods_payment_method_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/paymentMethods/{payment_method_id}'.format(payment_method_id='payment_method_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_methods_payment_method_id_options(client):
    """Test case for payment_methods_payment_method_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/paymentMethods/{payment_method_id}'.format(payment_method_id='payment_method_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_methods_payment_method_id_patch(client):
    """Test case for payment_methods_payment_method_id_patch

    
    """
    body = {"stripeSetupIntentSecret":"stripeSetupIntentSecret","name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/paymentMethods/{payment_method_id}'.format(payment_method_id='payment_method_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_methods_post(client):
    """Test case for payment_methods_post

    
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/paymentMethods',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_plans_get(client):
    """Test case for plans_get

    
    """
    params = [('owner', 'owner_example'),
                    ('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/plans',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_plans_options(client):
    """Test case for plans_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/plans',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_plans_plan_id_get(client):
    """Test case for plans_plan_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/plans/{plan_id}'.format(plan_id='plan_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_plans_plan_id_options(client):
    """Test case for plans_plan_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/plans/{plan_id}'.format(plan_id='plan_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_predictions_get(client):
    """Test case for predictions_get

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example'),
                    ('sortBy', 'sort_by_example'),
                    ('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/predictions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_predictions_options(client):
    """Test case for predictions_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/predictions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_predictions_post(client):
    """Test case for predictions_post

    
    """
    body = {"trainingId":"trainingId","modelId":"modelId","postprocessConfig":{"strategy":"BEST_FIRST"},"maxPages":1,"rotation":6,"documentId":"documentId","autoRotate":True,"imageQuality":"LOW"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/predictions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_profile_id_get(client):
    """Test case for profiles_profile_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/profiles/{profile_id}'.format(profile_id='profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_profile_id_options(client):
    """Test case for profiles_profile_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/profiles/{profile_id}'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_profile_id_patch(client):
    """Test case for profiles_profile_id_patch

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/profiles/{profile_id}'.format(profile_id='profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_get(client):
    """Test case for secrets_get

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/secrets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_options(client):
    """Test case for secrets_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/secrets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_post(client):
    """Test case for secrets_post

    
    """
    body = {"data":"{}","name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/secrets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secret_id_delete(client):
    """Test case for secrets_secret_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/secrets/{secret_id}'.format(secret_id='secret_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secret_id_options(client):
    """Test case for secrets_secret_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/secrets/{secret_id}'.format(secret_id='secret_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secret_id_patch(client):
    """Test case for secrets_secret_id_patch

    
    """
    body = {"data":"{}","name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/secrets/{secret_id}'.format(secret_id='secret_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_get(client):
    """Test case for transitions_get

    
    """
    params = [('transitionType', 'transition_type_example'),
                    ('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/transitions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_options(client):
    """Test case for transitions_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/transitions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_post(client):
    """Test case for transitions_post

    
    """
    body = {"outputJsonSchema":"{}","name":"name","description":"description","inputJsonSchema":"{}","parameters":{"environmentSecrets":["environmentSecrets","environmentSecrets"],"environment":{"key":"environment"},"memory":6,"imageUrl":"imageUrl","cpu":0,"secretId":"secretId"},"transitionType":"docker","timeoutInSeconds":315}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/transitions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_transition_id_delete(client):
    """Test case for transitions_transition_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/transitions/{transition_id}'.format(transition_id='transition_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_transition_id_executions_execution_id_get(client):
    """Test case for transitions_transition_id_executions_execution_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/transitions/{transition_id}/executions/{execution_id}'.format(transition_id='transition_id_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_transition_id_executions_execution_id_heartbeats_options(client):
    """Test case for transitions_transition_id_executions_execution_id_heartbeats_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/transitions/{transition_id}/executions/{execution_id}/heartbeats'.format(transition_id='transition_id_example', execution_id='execution_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_transition_id_executions_execution_id_heartbeats_post(client):
    """Test case for transitions_transition_id_executions_execution_id_heartbeats_post

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/transitions/{transition_id}/executions/{execution_id}/heartbeats'.format(transition_id='transition_id_example', execution_id='execution_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_transition_id_executions_execution_id_options(client):
    """Test case for transitions_transition_id_executions_execution_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/transitions/{transition_id}/executions/{execution_id}'.format(transition_id='transition_id_example', execution_id='execution_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_transition_id_executions_execution_id_patch(client):
    """Test case for transitions_transition_id_executions_execution_id_patch

    
    """
    body = {"output":"{}","startTime":"startTime","error":"{}","status":"status"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/transitions/{transition_id}/executions/{execution_id}'.format(transition_id='transition_id_example', execution_id='execution_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_transition_id_executions_get(client):
    """Test case for transitions_transition_id_executions_get

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('order', 'order_example'),
                    ('executionId', 'execution_id_example'),
                    ('status', 'status_example'),
                    ('maxResults', 'max_results_example'),
                    ('sortBy', 'sort_by_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/transitions/{transition_id}/executions'.format(transition_id='transition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_transition_id_executions_options(client):
    """Test case for transitions_transition_id_executions_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/transitions/{transition_id}/executions'.format(transition_id='transition_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_transition_id_executions_post(client):
    """Test case for transitions_transition_id_executions_post

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/transitions/{transition_id}/executions'.format(transition_id='transition_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_transition_id_get(client):
    """Test case for transitions_transition_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/transitions/{transition_id}'.format(transition_id='transition_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_transition_id_options(client):
    """Test case for transitions_transition_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/transitions/{transition_id}'.format(transition_id='transition_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transitions_transition_id_patch(client):
    """Test case for transitions_transition_id_patch

    
    """
    body = {"environmentSecrets":["environmentSecrets","environmentSecrets"],"environment":{"key":"environment"},"assets":{"jsRemoteComponent":"jsRemoteComponent"},"outputJsonSchema":"{}","name":"name","description":"description","inputJsonSchema":"{}","parameters":{"environmentSecrets":["environmentSecrets","environmentSecrets"],"environment":{"key":"environment"},"memory":6,"imageUrl":"imageUrl","cpu":0,"secretId":"secretId"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/transitions/{transition_id}'.format(transition_id='transition_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_options(client):
    """Test case for users_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_post(client):
    """Test case for users_post

    
    """
    body = {"metadata":"{}","name":"name","avatar":"avatar","appClientId":"appClientId","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_delete(client):
    """Test case for users_user_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_get(client):
    """Test case for users_user_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_options(client):
    """Test case for users_user_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_patch(client):
    """Test case for users_user_id_patch

    
    """
    body = {"metadata":"{}","name":"name","avatar":"avatar"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_get(client):
    """Test case for workflows_get

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('maxResults', 'max_results_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/workflows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_options(client):
    """Test case for workflows_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/workflows',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_post(client):
    """Test case for workflows_post

    
    """
    body = {"completedConfig":{"environmentSecrets":["environmentSecrets","environmentSecrets"],"environment":{"key":"environment"},"imageUrl":"imageUrl","secretId":"secretId"},"name":"name","description":"description","specification":{"definition":"{}","language":"ASL","version":"1.0.0"},"errorConfig":{"manualRetry":True,"email":"email"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/workflows',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_workflow_id_delete(client):
    """Test case for workflows_workflow_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/workflows/{workflow_id}'.format(workflow_id='workflow_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_workflow_id_executions_execution_id_delete(client):
    """Test case for workflows_workflow_id_executions_execution_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/workflows/{workflow_id}/executions/{execution_id}'.format(execution_id='execution_id_example', workflow_id='workflow_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_workflow_id_executions_execution_id_get(client):
    """Test case for workflows_workflow_id_executions_execution_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/workflows/{workflow_id}/executions/{execution_id}'.format(execution_id='execution_id_example', workflow_id='workflow_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_workflow_id_executions_execution_id_options(client):
    """Test case for workflows_workflow_id_executions_execution_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/workflows/{workflow_id}/executions/{execution_id}'.format(execution_id='execution_id_example', workflow_id='workflow_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_workflow_id_executions_execution_id_patch(client):
    """Test case for workflows_workflow_id_executions_execution_id_patch

    
    """
    body = {"nextTransitionId":"Logs_transitionId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/workflows/{workflow_id}/executions/{execution_id}'.format(execution_id='execution_id_example', workflow_id='workflow_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_workflow_id_executions_get(client):
    """Test case for workflows_workflow_id_executions_get

    
    """
    params = [('fromStartTime', 'from_start_time_example'),
                    ('toStartTime', 'to_start_time_example'),
                    ('nextToken', 'next_token_example'),
                    ('order', 'order_example'),
                    ('status', 'status_example'),
                    ('maxResults', 'max_results_example'),
                    ('sortBy', 'sort_by_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/workflows/{workflow_id}/executions'.format(workflow_id='workflow_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_workflow_id_executions_options(client):
    """Test case for workflows_workflow_id_executions_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/workflows/{workflow_id}/executions'.format(workflow_id='workflow_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_workflow_id_executions_post(client):
    """Test case for workflows_workflow_id_executions_post

    
    """
    body = {"input":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/workflows/{workflow_id}/executions'.format(workflow_id='workflow_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_workflow_id_get(client):
    """Test case for workflows_workflow_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/workflows/{workflow_id}'.format(workflow_id='workflow_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_workflow_id_options(client):
    """Test case for workflows_workflow_id_options

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/v1/workflows/{workflow_id}'.format(workflow_id='workflow_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_workflow_id_patch(client):
    """Test case for workflows_workflow_id_patch

    
    """
    body = {"completedConfig":{"environmentSecrets":["environmentSecrets","environmentSecrets"],"environment":{"key":"environment"},"imageUrl":"imageUrl","secretId":"secretId"},"name":"name","description":"description","errorConfig":{"manualRetry":True,"email":"email"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/workflows/{workflow_id}'.format(workflow_id='workflow_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

