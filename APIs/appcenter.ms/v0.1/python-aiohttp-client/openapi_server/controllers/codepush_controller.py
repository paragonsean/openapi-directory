from typing import List, Dict
from aiohttp import web

from openapi_server.models.branch_configurations_delete200_response import BranchConfigurationsDelete200Response
from openapi_server.models.code_push_acquisition_get_acquisition_status200_response import CodePushAcquisitionGetAcquisitionStatus200Response
from openapi_server.models.code_push_acquisition_update_check200_response import CodePushAcquisitionUpdateCheck200Response
from openapi_server.models.code_push_acquisition_update_deploy_status_request import CodePushAcquisitionUpdateDeployStatusRequest
from openapi_server.models.code_push_deployment_metrics_get200_response_inner import CodePushDeploymentMetricsGet200ResponseInner
from openapi_server.models.code_push_deployment_release_rollback_request import CodePushDeploymentReleaseRollbackRequest
from openapi_server.models.code_push_deployment_releases_create_request import CodePushDeploymentReleasesCreateRequest
from openapi_server.models.code_push_deployment_upload_create200_response import CodePushDeploymentUploadCreate200Response
from openapi_server.models.code_push_deployments_list200_response_inner import CodePushDeploymentsList200ResponseInner
from openapi_server.models.code_push_deployments_list200_response_inner_latest_release import CodePushDeploymentsList200ResponseInnerLatestRelease
from openapi_server.models.code_push_deployments_promote_request import CodePushDeploymentsPromoteRequest
from openapi_server.models.code_push_deployments_update_request import CodePushDeploymentsUpdateRequest
from openapi_server.models.deployment_releases_update_request import DeploymentReleasesUpdateRequest
from openapi_server.models.legacy_code_push_acquisition_update_check200_response import LegacyCodePushAcquisitionUpdateCheck200Response
from openapi_server.models.legacy_code_push_acquisition_update_installs_status_request import LegacyCodePushAcquisitionUpdateInstallsStatusRequest
from openapi_server import util


async def code_push_acquisition_get_acquisition_status(request: web.Request, ) -> web.Response:
    """code_push_acquisition_get_acquisition_status

    Returns the acquisition service status to the caller


    """
    return web.Response(status=200)


async def code_push_acquisition_update_check(request: web.Request, deployment_key, app_version, package_hash=None, label=None, client_unique_id=None, is_companion=None, previous_label_or_app_version=None, previous_deployment_key=None) -> web.Response:
    """code_push_acquisition_update_check

    Check for updates

    :param deployment_key: 
    :type deployment_key: str
    :param app_version: 
    :type app_version: str
    :param package_hash: 
    :type package_hash: str
    :param label: 
    :type label: str
    :param client_unique_id: 
    :type client_unique_id: str
    :param is_companion: 
    :type is_companion: bool
    :param previous_label_or_app_version: 
    :type previous_label_or_app_version: str
    :param previous_deployment_key: 
    :type previous_deployment_key: str

    """
    return web.Response(status=200)


async def code_push_acquisition_update_deploy_status(request: web.Request, body) -> web.Response:
    """code_push_acquisition_update_deploy_status

    Report Deployment status metric

    :param body: Deployment status metric properties
    :type body: dict | bytes

    """
    body = CodePushAcquisitionUpdateDeployStatusRequest.from_dict(body)
    return web.Response(status=200)


async def code_push_acquisition_update_download_status(request: web.Request, body) -> web.Response:
    """code_push_acquisition_update_download_status

    Report download of specified release

    :param body: Deployment status metric properties
    :type body: dict | bytes

    """
    body = CodePushAcquisitionUpdateDeployStatusRequest.from_dict(body)
    return web.Response(status=200)


async def code_push_deployment_metrics_get(request: web.Request, deployment_name, owner_name, app_name) -> web.Response:
    """code_push_deployment_metrics_get

    Gets all releases metrics for specified Deployment

    :param deployment_name: deployment name
    :type deployment_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def code_push_deployment_release_rollback(request: web.Request, deployment_name, owner_name, app_name, body=None) -> web.Response:
    """code_push_deployment_release_rollback

    Rollback the latest or a specific release for an app deployment

    :param deployment_name: deployment name
    :type deployment_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The specific release label that you want to rollback to
    :type body: dict | bytes

    """
    body = CodePushDeploymentReleaseRollbackRequest.from_dict(body)
    return web.Response(status=200)


async def code_push_deployment_releases_create(request: web.Request, deployment_name, owner_name, app_name, body) -> web.Response:
    """code_push_deployment_releases_create

    Create a new CodePush release for the specified deployment

    :param deployment_name: deployment name
    :type deployment_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The necessary information required to download the bundle and being the release process.
    :type body: dict | bytes

    """
    body = CodePushDeploymentReleasesCreateRequest.from_dict(body)
    return web.Response(status=200)


async def code_push_deployment_releases_delete(request: web.Request, deployment_name, owner_name, app_name) -> web.Response:
    """code_push_deployment_releases_delete

    Clears a Deployment of releases

    :param deployment_name: deployment name
    :type deployment_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def code_push_deployment_releases_get(request: web.Request, deployment_name, owner_name, app_name) -> web.Response:
    """code_push_deployment_releases_get

    Gets the history of releases on a Deployment

    :param deployment_name: deployment name
    :type deployment_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def code_push_deployment_upload_create(request: web.Request, deployment_name, owner_name, app_name) -> web.Response:
    """code_push_deployment_upload_create

    Create a new CodePush release upload for the specified deployment

    :param deployment_name: deployment name
    :type deployment_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def code_push_deployments_create(request: web.Request, owner_name, app_name, body) -> web.Response:
    """code_push_deployments_create

    Creates a CodePush Deployment for the given app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Deployment to be created
    :type body: dict | bytes

    """
    body = CodePushDeploymentsList200ResponseInner.from_dict(body)
    return web.Response(status=200)


async def code_push_deployments_delete(request: web.Request, deployment_name, owner_name, app_name, body=None) -> web.Response:
    """code_push_deployments_delete

    Deletes a CodePush Deployment for the given app

    :param deployment_name: deployment name
    :type deployment_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def code_push_deployments_get(request: web.Request, deployment_name, owner_name, app_name) -> web.Response:
    """code_push_deployments_get

    Gets a CodePush Deployment for the given app

    :param deployment_name: deployment name
    :type deployment_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def code_push_deployments_list(request: web.Request, owner_name, app_name) -> web.Response:
    """code_push_deployments_list

    Gets a list of CodePush deployments for the given app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def code_push_deployments_promote(request: web.Request, deployment_name, promote_deployment_name, owner_name, app_name, body=None) -> web.Response:
    """code_push_deployments_promote

    Promote one release (default latest one) from one deployment to another

    :param deployment_name: deployment name
    :type deployment_name: str
    :param promote_deployment_name: deployment name
    :type promote_deployment_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Release to be promoted, only needs to provide optional fields, description, label, disabled, mandatory, rollout, targetBinaryVersion
    :type body: dict | bytes

    """
    body = CodePushDeploymentsPromoteRequest.from_dict(body)
    return web.Response(status=200)


async def code_push_deployments_update(request: web.Request, deployment_name, owner_name, app_name, body) -> web.Response:
    """code_push_deployments_update

    Modifies a CodePush Deployment for the given app

    :param deployment_name: deployment name
    :type deployment_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Deployment modification. All fields are optional and only provided fields will get updated.
    :type body: dict | bytes

    """
    body = CodePushDeploymentsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def deployment_releases_update(request: web.Request, deployment_name, release_label, owner_name, app_name, body) -> web.Response:
    """deployment_releases_update

    Modifies a CodePush release metadata under the given Deployment

    :param deployment_name: deployment name
    :type deployment_name: str
    :param release_label: release label
    :type release_label: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Release modification. All fields are optional and only provided fields will get updated.
    :type body: dict | bytes

    """
    body = DeploymentReleasesUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def legacy_code_push_acquisition_update_check(request: web.Request, deployment_key=None, app_version=None, package_hash=None, label=None, client_unique_id=None, is_companion=None) -> web.Response:
    """legacy_code_push_acquisition_update_check

    Check for updates

    :param deployment_key: 
    :type deployment_key: str
    :param app_version: 
    :type app_version: str
    :param package_hash: 
    :type package_hash: str
    :param label: 
    :type label: str
    :param client_unique_id: 
    :type client_unique_id: str
    :param is_companion: 
    :type is_companion: str

    """
    return web.Response(status=200)


async def legacy_code_push_acquisition_update_download_status(request: web.Request, body) -> web.Response:
    """legacy_code_push_acquisition_update_download_status

    Report download of specified release

    :param body: Deployment status metric properties
    :type body: dict | bytes

    """
    body = LegacyCodePushAcquisitionUpdateInstallsStatusRequest.from_dict(body)
    return web.Response(status=200)


async def legacy_code_push_acquisition_update_installs_status(request: web.Request, body) -> web.Response:
    """legacy_code_push_acquisition_update_installs_status

    Report deploy of specified release

    :param body: Deployment status metric properties
    :type body: dict | bytes

    """
    body = LegacyCodePushAcquisitionUpdateInstallsStatusRequest.from_dict(body)
    return web.Response(status=200)
