from typing import List, Dict
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
from openapi_server import util


async def app_clients_app_client_id_delete(request: web.Request, app_client_id) -> web.Response:
    """app_clients_app_client_id_delete

    

    :param app_client_id: 
    :type app_client_id: str

    """
    return web.Response(status=200)


async def app_clients_app_client_id_options(request: web.Request, app_client_id, body) -> web.Response:
    """app_clients_app_client_id_options

    

    :param app_client_id: 
    :type app_client_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def app_clients_app_client_id_patch(request: web.Request, app_client_id, content_type, body) -> web.Response:
    """app_clients_app_client_id_patch

    

    :param app_client_id: 
    :type app_client_id: str
    :param content_type: 
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchAppClientId.from_dict(body)
    return web.Response(status=200)


async def app_clients_get(request: web.Request, next_token=None, max_results=None) -> web.Response:
    """app_clients_get

    

    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def app_clients_options(request: web.Request, body) -> web.Response:
    """app_clients_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def app_clients_post(request: web.Request, content_type, body) -> web.Response:
    """app_clients_post

    

    :param content_type: 
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostAppClients.from_dict(body)
    return web.Response(status=200)


async def assets_asset_id_delete(request: web.Request, asset_id) -> web.Response:
    """assets_asset_id_delete

    

    :param asset_id: 
    :type asset_id: str

    """
    return web.Response(status=200)


async def assets_asset_id_get(request: web.Request, asset_id) -> web.Response:
    """assets_asset_id_get

    

    :param asset_id: 
    :type asset_id: str

    """
    return web.Response(status=200)


async def assets_asset_id_options(request: web.Request, asset_id, body) -> web.Response:
    """assets_asset_id_options

    

    :param asset_id: 
    :type asset_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def assets_asset_id_patch(request: web.Request, content_type, asset_id, body) -> web.Response:
    """assets_asset_id_patch

    

    :param content_type: 
    :type content_type: str
    :param asset_id: 
    :type asset_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchAssetId.from_dict(body)
    return web.Response(status=200)


async def assets_get(request: web.Request, next_token=None, max_results=None) -> web.Response:
    """assets_get

    

    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def assets_options(request: web.Request, body) -> web.Response:
    """assets_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def assets_post(request: web.Request, content_type, body) -> web.Response:
    """assets_post

    

    :param content_type: 
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostAssets.from_dict(body)
    return web.Response(status=200)


async def datasets_dataset_id_delete(request: web.Request, dataset_id) -> web.Response:
    """datasets_dataset_id_delete

    

    :param dataset_id: 
    :type dataset_id: str

    """
    return web.Response(status=200)


async def datasets_dataset_id_get(request: web.Request, dataset_id) -> web.Response:
    """datasets_dataset_id_get

    

    :param dataset_id: 
    :type dataset_id: str

    """
    return web.Response(status=200)


async def datasets_dataset_id_options(request: web.Request, dataset_id, body) -> web.Response:
    """datasets_dataset_id_options

    

    :param dataset_id: 
    :type dataset_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def datasets_dataset_id_patch(request: web.Request, content_type, dataset_id, body) -> web.Response:
    """datasets_dataset_id_patch

    

    :param content_type: 
    :type content_type: str
    :param dataset_id: 
    :type dataset_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchDatasetId.from_dict(body)
    return web.Response(status=200)


async def datasets_get(request: web.Request, next_token=None, max_results=None) -> web.Response:
    """datasets_get

    

    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def datasets_options(request: web.Request, body) -> web.Response:
    """datasets_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def datasets_post(request: web.Request, content_type, body) -> web.Response:
    """datasets_post

    

    :param content_type: 
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostDatasets.from_dict(body)
    return web.Response(status=200)


async def deployment_environments_deployment_environment_id_get(request: web.Request, deployment_environment_id) -> web.Response:
    """deployment_environments_deployment_environment_id_get

    

    :param deployment_environment_id: 
    :type deployment_environment_id: str

    """
    return web.Response(status=200)


async def deployment_environments_deployment_environment_id_options(request: web.Request, deployment_environment_id, body) -> web.Response:
    """deployment_environments_deployment_environment_id_options

    

    :param deployment_environment_id: 
    :type deployment_environment_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def deployment_environments_get(request: web.Request, owner=None, next_token=None, max_results=None) -> web.Response:
    """deployment_environments_get

    

    :param owner: 
    :type owner: str
    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def deployment_environments_options(request: web.Request, body) -> web.Response:
    """deployment_environments_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def documents_delete(request: web.Request, consent_id=None, dataset_id=None, next_token=None, max_results=None) -> web.Response:
    """documents_delete

    

    :param consent_id: 
    :type consent_id: str
    :param dataset_id: 
    :type dataset_id: str
    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def documents_document_id_delete(request: web.Request, document_id) -> web.Response:
    """documents_document_id_delete

    

    :param document_id: 
    :type document_id: str

    """
    return web.Response(status=200)


async def documents_document_id_get(request: web.Request, document_id) -> web.Response:
    """documents_document_id_get

    

    :param document_id: 
    :type document_id: str

    """
    return web.Response(status=200)


async def documents_document_id_options(request: web.Request, document_id, body) -> web.Response:
    """documents_document_id_options

    

    :param document_id: 
    :type document_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def documents_document_id_patch(request: web.Request, content_type, document_id, body) -> web.Response:
    """documents_document_id_patch

    

    :param content_type: 
    :type content_type: str
    :param document_id: 
    :type document_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchDocumentId.from_dict(body)
    return web.Response(status=200)


async def documents_get(request: web.Request, dataset_id=None, next_token=None, order=None, document_id=None, consent_id=None, max_results=None, sort_by=None) -> web.Response:
    """documents_get

    

    :param dataset_id: 
    :type dataset_id: str
    :param next_token: 
    :type next_token: str
    :param order: 
    :type order: str
    :param document_id: 
    :type document_id: str
    :param consent_id: 
    :type consent_id: str
    :param max_results: 
    :type max_results: str
    :param sort_by: 
    :type sort_by: str

    """
    return web.Response(status=200)


async def documents_options(request: web.Request, body) -> web.Response:
    """documents_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def documents_post(request: web.Request, content_type, body) -> web.Response:
    """documents_post

    

    :param content_type: 
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostDocuments.from_dict(body)
    return web.Response(status=200)


async def logs_get(request: web.Request, workflow_id=None, next_token=None, order=None, transition_execution_id=None, transition_id=None, max_results=None, workflow_execution_id=None) -> web.Response:
    """logs_get

    

    :param workflow_id: 
    :type workflow_id: str
    :param next_token: 
    :type next_token: str
    :param order: 
    :type order: str
    :param transition_execution_id: 
    :type transition_execution_id: str
    :param transition_id: 
    :type transition_id: str
    :param max_results: 
    :type max_results: str
    :param workflow_execution_id: 
    :type workflow_execution_id: str

    """
    return web.Response(status=200)


async def logs_log_id_get(request: web.Request, log_id) -> web.Response:
    """logs_log_id_get

    

    :param log_id: 
    :type log_id: str

    """
    return web.Response(status=200)


async def logs_log_id_options(request: web.Request, log_id, body) -> web.Response:
    """logs_log_id_options

    

    :param log_id: 
    :type log_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def logs_options(request: web.Request, body) -> web.Response:
    """logs_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def models_get(request: web.Request, owner=None, next_token=None, max_results=None) -> web.Response:
    """models_get

    

    :param owner: 
    :type owner: str
    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def models_model_id_data_bundles_data_bundle_id_delete(request: web.Request, data_bundle_id, model_id) -> web.Response:
    """models_model_id_data_bundles_data_bundle_id_delete

    

    :param data_bundle_id: 
    :type data_bundle_id: str
    :param model_id: 
    :type model_id: str

    """
    return web.Response(status=200)


async def models_model_id_data_bundles_data_bundle_id_options(request: web.Request, data_bundle_id, model_id, body) -> web.Response:
    """models_model_id_data_bundles_data_bundle_id_options

    

    :param data_bundle_id: 
    :type data_bundle_id: str
    :param model_id: 
    :type model_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def models_model_id_data_bundles_data_bundle_id_patch(request: web.Request, data_bundle_id, content_type, model_id, body) -> web.Response:
    """models_model_id_data_bundles_data_bundle_id_patch

    

    :param data_bundle_id: 
    :type data_bundle_id: str
    :param content_type: 
    :type content_type: str
    :param model_id: 
    :type model_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchDataBundleId.from_dict(body)
    return web.Response(status=200)


async def models_model_id_data_bundles_get(request: web.Request, model_id, status=None, next_token=None, max_results=None) -> web.Response:
    """models_model_id_data_bundles_get

    

    :param model_id: 
    :type model_id: str
    :param status: 
    :type status: str
    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def models_model_id_data_bundles_options(request: web.Request, model_id, body) -> web.Response:
    """models_model_id_data_bundles_options

    

    :param model_id: 
    :type model_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def models_model_id_data_bundles_post(request: web.Request, content_type, model_id, body) -> web.Response:
    """models_model_id_data_bundles_post

    

    :param content_type: 
    :type content_type: str
    :param model_id: 
    :type model_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostDataBundles.from_dict(body)
    return web.Response(status=200)


async def models_model_id_delete(request: web.Request, model_id) -> web.Response:
    """models_model_id_delete

    

    :param model_id: 
    :type model_id: str

    """
    return web.Response(status=200)


async def models_model_id_get(request: web.Request, model_id) -> web.Response:
    """models_model_id_get

    

    :param model_id: 
    :type model_id: str

    """
    return web.Response(status=200)


async def models_model_id_options(request: web.Request, model_id, body) -> web.Response:
    """models_model_id_options

    

    :param model_id: 
    :type model_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def models_model_id_patch(request: web.Request, content_type, model_id, body) -> web.Response:
    """models_model_id_patch

    

    :param content_type: 
    :type content_type: str
    :param model_id: 
    :type model_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchModelId.from_dict(body)
    return web.Response(status=200)


async def models_model_id_trainings_get(request: web.Request, model_id, status=None, next_token=None, max_results=None) -> web.Response:
    """models_model_id_trainings_get

    

    :param model_id: 
    :type model_id: str
    :param status: 
    :type status: str
    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def models_model_id_trainings_options(request: web.Request, model_id, body) -> web.Response:
    """models_model_id_trainings_options

    

    :param model_id: 
    :type model_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def models_model_id_trainings_post(request: web.Request, content_type, model_id, body) -> web.Response:
    """models_model_id_trainings_post

    

    :param content_type: 
    :type content_type: str
    :param model_id: 
    :type model_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostTrainings.from_dict(body)
    return web.Response(status=200)


async def models_model_id_trainings_training_id_options(request: web.Request, model_id, training_id, body) -> web.Response:
    """models_model_id_trainings_training_id_options

    

    :param model_id: 
    :type model_id: str
    :param training_id: 
    :type training_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def models_model_id_trainings_training_id_patch(request: web.Request, content_type, model_id, training_id, body) -> web.Response:
    """models_model_id_trainings_training_id_patch

    

    :param content_type: 
    :type content_type: str
    :param model_id: 
    :type model_id: str
    :param training_id: 
    :type training_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchTrainingId.from_dict(body)
    return web.Response(status=200)


async def models_options(request: web.Request, body) -> web.Response:
    """models_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def models_post(request: web.Request, content_type, body) -> web.Response:
    """models_post

    

    :param content_type: 
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostModels.from_dict(body)
    return web.Response(status=200)


async def organizations_get(request: web.Request, next_token=None, max_results=None) -> web.Response:
    """organizations_get

    

    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def organizations_options(request: web.Request, body) -> web.Response:
    """organizations_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def organizations_organization_id_get(request: web.Request, organization_id) -> web.Response:
    """organizations_organization_id_get

    

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def organizations_organization_id_options(request: web.Request, organization_id, body) -> web.Response:
    """organizations_organization_id_options

    

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def organizations_organization_id_patch(request: web.Request, content_type, organization_id, body) -> web.Response:
    """organizations_organization_id_patch

    

    :param content_type: 
    :type content_type: str
    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchOrganizationId.from_dict(body)
    return web.Response(status=200)


async def organizations_post(request: web.Request, content_type, body) -> web.Response:
    """organizations_post

    

    :param content_type: 
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostOrganizations.from_dict(body)
    return web.Response(status=200)


async def payment_methods_get(request: web.Request, next_token=None, max_results=None) -> web.Response:
    """payment_methods_get

    

    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def payment_methods_options(request: web.Request, body) -> web.Response:
    """payment_methods_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def payment_methods_payment_method_id_delete(request: web.Request, payment_method_id) -> web.Response:
    """payment_methods_payment_method_id_delete

    

    :param payment_method_id: 
    :type payment_method_id: str

    """
    return web.Response(status=200)


async def payment_methods_payment_method_id_get(request: web.Request, payment_method_id) -> web.Response:
    """payment_methods_payment_method_id_get

    

    :param payment_method_id: 
    :type payment_method_id: str

    """
    return web.Response(status=200)


async def payment_methods_payment_method_id_options(request: web.Request, payment_method_id, body) -> web.Response:
    """payment_methods_payment_method_id_options

    

    :param payment_method_id: 
    :type payment_method_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def payment_methods_payment_method_id_patch(request: web.Request, content_type, payment_method_id, body) -> web.Response:
    """payment_methods_payment_method_id_patch

    

    :param content_type: 
    :type content_type: str
    :param payment_method_id: 
    :type payment_method_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchPaymentMethodId.from_dict(body)
    return web.Response(status=200)


async def payment_methods_post(request: web.Request, content_type, body) -> web.Response:
    """payment_methods_post

    

    :param content_type: 
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostPaymentMethods.from_dict(body)
    return web.Response(status=200)


async def plans_get(request: web.Request, owner=None, next_token=None, max_results=None) -> web.Response:
    """plans_get

    

    :param owner: 
    :type owner: str
    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def plans_options(request: web.Request, body) -> web.Response:
    """plans_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def plans_plan_id_get(request: web.Request, plan_id) -> web.Response:
    """plans_plan_id_get

    

    :param plan_id: 
    :type plan_id: str

    """
    return web.Response(status=200)


async def plans_plan_id_options(request: web.Request, plan_id, body) -> web.Response:
    """plans_plan_id_options

    

    :param plan_id: 
    :type plan_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def predictions_get(request: web.Request, next_token=None, max_results=None, sort_by=None, order=None) -> web.Response:
    """predictions_get

    

    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str
    :param sort_by: 
    :type sort_by: str
    :param order: 
    :type order: str

    """
    return web.Response(status=200)


async def predictions_options(request: web.Request, body) -> web.Response:
    """predictions_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def predictions_post(request: web.Request, content_type, body) -> web.Response:
    """predictions_post

    

    :param content_type: 
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostPredictions.from_dict(body)
    return web.Response(status=200)


async def profiles_profile_id_get(request: web.Request, profile_id) -> web.Response:
    """profiles_profile_id_get

    

    :param profile_id: 
    :type profile_id: str

    """
    return web.Response(status=200)


async def profiles_profile_id_options(request: web.Request, profile_id, body) -> web.Response:
    """profiles_profile_id_options

    

    :param profile_id: 
    :type profile_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def profiles_profile_id_patch(request: web.Request, profile_id) -> web.Response:
    """profiles_profile_id_patch

    

    :param profile_id: 
    :type profile_id: str

    """
    return web.Response(status=200)


async def secrets_get(request: web.Request, next_token=None, max_results=None) -> web.Response:
    """secrets_get

    

    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def secrets_options(request: web.Request, body) -> web.Response:
    """secrets_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def secrets_post(request: web.Request, content_type, body) -> web.Response:
    """secrets_post

    

    :param content_type: 
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostSecrets.from_dict(body)
    return web.Response(status=200)


async def secrets_secret_id_delete(request: web.Request, secret_id) -> web.Response:
    """secrets_secret_id_delete

    

    :param secret_id: 
    :type secret_id: str

    """
    return web.Response(status=200)


async def secrets_secret_id_options(request: web.Request, secret_id, body) -> web.Response:
    """secrets_secret_id_options

    

    :param secret_id: 
    :type secret_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def secrets_secret_id_patch(request: web.Request, content_type, secret_id, body) -> web.Response:
    """secrets_secret_id_patch

    

    :param content_type: 
    :type content_type: str
    :param secret_id: 
    :type secret_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchSecretId.from_dict(body)
    return web.Response(status=200)


async def transitions_get(request: web.Request, transition_type=None, next_token=None, max_results=None) -> web.Response:
    """transitions_get

    

    :param transition_type: 
    :type transition_type: str
    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def transitions_options(request: web.Request, body) -> web.Response:
    """transitions_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def transitions_post(request: web.Request, content_type, body) -> web.Response:
    """transitions_post

    

    :param content_type: 
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostTransitions.from_dict(body)
    return web.Response(status=200)


async def transitions_transition_id_delete(request: web.Request, transition_id) -> web.Response:
    """transitions_transition_id_delete

    

    :param transition_id: 
    :type transition_id: str

    """
    return web.Response(status=200)


async def transitions_transition_id_executions_execution_id_get(request: web.Request, transition_id, execution_id) -> web.Response:
    """transitions_transition_id_executions_execution_id_get

    

    :param transition_id: 
    :type transition_id: str
    :param execution_id: 
    :type execution_id: str

    """
    return web.Response(status=200)


async def transitions_transition_id_executions_execution_id_heartbeats_options(request: web.Request, transition_id, execution_id, body) -> web.Response:
    """transitions_transition_id_executions_execution_id_heartbeats_options

    

    :param transition_id: 
    :type transition_id: str
    :param execution_id: 
    :type execution_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def transitions_transition_id_executions_execution_id_heartbeats_post(request: web.Request, content_type, transition_id, execution_id, body) -> web.Response:
    """transitions_transition_id_executions_execution_id_heartbeats_post

    

    :param content_type: 
    :type content_type: str
    :param transition_id: 
    :type transition_id: str
    :param execution_id: 
    :type execution_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def transitions_transition_id_executions_execution_id_options(request: web.Request, transition_id, execution_id, body) -> web.Response:
    """transitions_transition_id_executions_execution_id_options

    

    :param transition_id: 
    :type transition_id: str
    :param execution_id: 
    :type execution_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def transitions_transition_id_executions_execution_id_patch(request: web.Request, content_type, transition_id, execution_id, body) -> web.Response:
    """transitions_transition_id_executions_execution_id_patch

    

    :param content_type: 
    :type content_type: str
    :param transition_id: 
    :type transition_id: str
    :param execution_id: 
    :type execution_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchTransistionExecutionId.from_dict(body)
    return web.Response(status=200)


async def transitions_transition_id_executions_get(request: web.Request, transition_id, next_token=None, order=None, execution_id=None, status=None, max_results=None, sort_by=None) -> web.Response:
    """transitions_transition_id_executions_get

    

    :param transition_id: 
    :type transition_id: str
    :param next_token: 
    :type next_token: str
    :param order: 
    :type order: str
    :param execution_id: 
    :type execution_id: str
    :param status: 
    :type status: str
    :param max_results: 
    :type max_results: str
    :param sort_by: 
    :type sort_by: str

    """
    return web.Response(status=200)


async def transitions_transition_id_executions_options(request: web.Request, transition_id, body) -> web.Response:
    """transitions_transition_id_executions_options

    

    :param transition_id: 
    :type transition_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def transitions_transition_id_executions_post(request: web.Request, content_type, transition_id, body) -> web.Response:
    """transitions_transition_id_executions_post

    

    :param content_type: 
    :type content_type: str
    :param transition_id: 
    :type transition_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def transitions_transition_id_get(request: web.Request, transition_id) -> web.Response:
    """transitions_transition_id_get

    

    :param transition_id: 
    :type transition_id: str

    """
    return web.Response(status=200)


async def transitions_transition_id_options(request: web.Request, transition_id, body) -> web.Response:
    """transitions_transition_id_options

    

    :param transition_id: 
    :type transition_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def transitions_transition_id_patch(request: web.Request, content_type, transition_id, body) -> web.Response:
    """transitions_transition_id_patch

    

    :param content_type: 
    :type content_type: str
    :param transition_id: 
    :type transition_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchTransitionId.from_dict(body)
    return web.Response(status=200)


async def users_get(request: web.Request, next_token=None, max_results=None) -> web.Response:
    """users_get

    

    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def users_options(request: web.Request, body) -> web.Response:
    """users_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def users_post(request: web.Request, content_type, body) -> web.Response:
    """users_post

    

    :param content_type: 
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostUsers.from_dict(body)
    return web.Response(status=200)


async def users_user_id_delete(request: web.Request, user_id) -> web.Response:
    """users_user_id_delete

    

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_get(request: web.Request, user_id) -> web.Response:
    """users_user_id_get

    

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_options(request: web.Request, user_id, body) -> web.Response:
    """users_user_id_options

    

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def users_user_id_patch(request: web.Request, content_type, user_id, body) -> web.Response:
    """users_user_id_patch

    

    :param content_type: 
    :type content_type: str
    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchUserId.from_dict(body)
    return web.Response(status=200)


async def workflows_get(request: web.Request, next_token=None, max_results=None) -> web.Response:
    """workflows_get

    

    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: str

    """
    return web.Response(status=200)


async def workflows_options(request: web.Request, body) -> web.Response:
    """workflows_options

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def workflows_post(request: web.Request, content_type, body) -> web.Response:
    """workflows_post

    

    :param content_type: 
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostWorkflows.from_dict(body)
    return web.Response(status=200)


async def workflows_workflow_id_delete(request: web.Request, workflow_id) -> web.Response:
    """workflows_workflow_id_delete

    

    :param workflow_id: 
    :type workflow_id: str

    """
    return web.Response(status=200)


async def workflows_workflow_id_executions_execution_id_delete(request: web.Request, execution_id, workflow_id) -> web.Response:
    """workflows_workflow_id_executions_execution_id_delete

    

    :param execution_id: 
    :type execution_id: str
    :param workflow_id: 
    :type workflow_id: str

    """
    return web.Response(status=200)


async def workflows_workflow_id_executions_execution_id_get(request: web.Request, execution_id, workflow_id) -> web.Response:
    """workflows_workflow_id_executions_execution_id_get

    

    :param execution_id: 
    :type execution_id: str
    :param workflow_id: 
    :type workflow_id: str

    """
    return web.Response(status=200)


async def workflows_workflow_id_executions_execution_id_options(request: web.Request, execution_id, workflow_id, body) -> web.Response:
    """workflows_workflow_id_executions_execution_id_options

    

    :param execution_id: 
    :type execution_id: str
    :param workflow_id: 
    :type workflow_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def workflows_workflow_id_executions_execution_id_patch(request: web.Request, content_type, execution_id, workflow_id, body) -> web.Response:
    """workflows_workflow_id_executions_execution_id_patch

    

    :param content_type: 
    :type content_type: str
    :param execution_id: 
    :type execution_id: str
    :param workflow_id: 
    :type workflow_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchWorkflowExecutionId.from_dict(body)
    return web.Response(status=200)


async def workflows_workflow_id_executions_get(request: web.Request, workflow_id, from_start_time=None, to_start_time=None, next_token=None, order=None, status=None, max_results=None, sort_by=None) -> web.Response:
    """workflows_workflow_id_executions_get

    

    :param workflow_id: 
    :type workflow_id: str
    :param from_start_time: 
    :type from_start_time: str
    :param to_start_time: 
    :type to_start_time: str
    :param next_token: 
    :type next_token: str
    :param order: 
    :type order: str
    :param status: 
    :type status: str
    :param max_results: 
    :type max_results: str
    :param sort_by: 
    :type sort_by: str

    """
    return web.Response(status=200)


async def workflows_workflow_id_executions_options(request: web.Request, workflow_id, body) -> web.Response:
    """workflows_workflow_id_executions_options

    

    :param workflow_id: 
    :type workflow_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def workflows_workflow_id_executions_post(request: web.Request, content_type, workflow_id, body) -> web.Response:
    """workflows_workflow_id_executions_post

    

    :param content_type: 
    :type content_type: str
    :param workflow_id: 
    :type workflow_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostWorkflowExecutions.from_dict(body)
    return web.Response(status=200)


async def workflows_workflow_id_get(request: web.Request, workflow_id) -> web.Response:
    """workflows_workflow_id_get

    

    :param workflow_id: 
    :type workflow_id: str

    """
    return web.Response(status=200)


async def workflows_workflow_id_options(request: web.Request, workflow_id, body) -> web.Response:
    """workflows_workflow_id_options

    

    :param workflow_id: 
    :type workflow_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def workflows_workflow_id_patch(request: web.Request, content_type, workflow_id, body) -> web.Response:
    """workflows_workflow_id_patch

    

    :param content_type: 
    :type content_type: str
    :param workflow_id: 
    :type workflow_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchWorkflowId.from_dict(body)
    return web.Response(status=200)
