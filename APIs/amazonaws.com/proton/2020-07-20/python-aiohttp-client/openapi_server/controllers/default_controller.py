from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_environment_account_connection_input import AcceptEnvironmentAccountConnectionInput
from openapi_server.models.accept_environment_account_connection_output import AcceptEnvironmentAccountConnectionOutput
from openapi_server.models.cancel_component_deployment_input import CancelComponentDeploymentInput
from openapi_server.models.cancel_component_deployment_output import CancelComponentDeploymentOutput
from openapi_server.models.cancel_environment_deployment_input import CancelEnvironmentDeploymentInput
from openapi_server.models.cancel_environment_deployment_output import CancelEnvironmentDeploymentOutput
from openapi_server.models.cancel_service_instance_deployment_input import CancelServiceInstanceDeploymentInput
from openapi_server.models.cancel_service_instance_deployment_output import CancelServiceInstanceDeploymentOutput
from openapi_server.models.cancel_service_pipeline_deployment_input import CancelServicePipelineDeploymentInput
from openapi_server.models.cancel_service_pipeline_deployment_output import CancelServicePipelineDeploymentOutput
from openapi_server.models.create_component_input import CreateComponentInput
from openapi_server.models.create_component_output import CreateComponentOutput
from openapi_server.models.create_environment_account_connection_input import CreateEnvironmentAccountConnectionInput
from openapi_server.models.create_environment_account_connection_output import CreateEnvironmentAccountConnectionOutput
from openapi_server.models.create_environment_input import CreateEnvironmentInput
from openapi_server.models.create_environment_output import CreateEnvironmentOutput
from openapi_server.models.create_environment_template_input import CreateEnvironmentTemplateInput
from openapi_server.models.create_environment_template_output import CreateEnvironmentTemplateOutput
from openapi_server.models.create_environment_template_version_input import CreateEnvironmentTemplateVersionInput
from openapi_server.models.create_environment_template_version_output import CreateEnvironmentTemplateVersionOutput
from openapi_server.models.create_repository_input import CreateRepositoryInput
from openapi_server.models.create_repository_output import CreateRepositoryOutput
from openapi_server.models.create_service_input import CreateServiceInput
from openapi_server.models.create_service_instance_input import CreateServiceInstanceInput
from openapi_server.models.create_service_instance_output import CreateServiceInstanceOutput
from openapi_server.models.create_service_output import CreateServiceOutput
from openapi_server.models.create_service_sync_config_input import CreateServiceSyncConfigInput
from openapi_server.models.create_service_sync_config_output import CreateServiceSyncConfigOutput
from openapi_server.models.create_service_template_input import CreateServiceTemplateInput
from openapi_server.models.create_service_template_output import CreateServiceTemplateOutput
from openapi_server.models.create_service_template_version_input import CreateServiceTemplateVersionInput
from openapi_server.models.create_service_template_version_output import CreateServiceTemplateVersionOutput
from openapi_server.models.create_template_sync_config_input import CreateTemplateSyncConfigInput
from openapi_server.models.create_template_sync_config_output import CreateTemplateSyncConfigOutput
from openapi_server.models.delete_component_input import DeleteComponentInput
from openapi_server.models.delete_component_output import DeleteComponentOutput
from openapi_server.models.delete_deployment_input import DeleteDeploymentInput
from openapi_server.models.delete_deployment_output import DeleteDeploymentOutput
from openapi_server.models.delete_environment_account_connection_input import DeleteEnvironmentAccountConnectionInput
from openapi_server.models.delete_environment_account_connection_output import DeleteEnvironmentAccountConnectionOutput
from openapi_server.models.delete_environment_input import DeleteEnvironmentInput
from openapi_server.models.delete_environment_output import DeleteEnvironmentOutput
from openapi_server.models.delete_environment_template_input import DeleteEnvironmentTemplateInput
from openapi_server.models.delete_environment_template_output import DeleteEnvironmentTemplateOutput
from openapi_server.models.delete_environment_template_version_input import DeleteEnvironmentTemplateVersionInput
from openapi_server.models.delete_environment_template_version_output import DeleteEnvironmentTemplateVersionOutput
from openapi_server.models.delete_repository_input import DeleteRepositoryInput
from openapi_server.models.delete_repository_output import DeleteRepositoryOutput
from openapi_server.models.delete_service_input import DeleteServiceInput
from openapi_server.models.delete_service_output import DeleteServiceOutput
from openapi_server.models.delete_service_sync_config_input import DeleteServiceSyncConfigInput
from openapi_server.models.delete_service_sync_config_output import DeleteServiceSyncConfigOutput
from openapi_server.models.delete_service_template_input import DeleteServiceTemplateInput
from openapi_server.models.delete_service_template_output import DeleteServiceTemplateOutput
from openapi_server.models.delete_service_template_version_input import DeleteServiceTemplateVersionInput
from openapi_server.models.delete_service_template_version_output import DeleteServiceTemplateVersionOutput
from openapi_server.models.delete_template_sync_config_input import DeleteTemplateSyncConfigInput
from openapi_server.models.delete_template_sync_config_output import DeleteTemplateSyncConfigOutput
from openapi_server.models.get_account_settings_output import GetAccountSettingsOutput
from openapi_server.models.get_component_input import GetComponentInput
from openapi_server.models.get_component_output import GetComponentOutput
from openapi_server.models.get_deployment_input import GetDeploymentInput
from openapi_server.models.get_deployment_output import GetDeploymentOutput
from openapi_server.models.get_environment_account_connection_input import GetEnvironmentAccountConnectionInput
from openapi_server.models.get_environment_account_connection_output import GetEnvironmentAccountConnectionOutput
from openapi_server.models.get_environment_input import GetEnvironmentInput
from openapi_server.models.get_environment_output import GetEnvironmentOutput
from openapi_server.models.get_environment_template_input import GetEnvironmentTemplateInput
from openapi_server.models.get_environment_template_output import GetEnvironmentTemplateOutput
from openapi_server.models.get_environment_template_version_input import GetEnvironmentTemplateVersionInput
from openapi_server.models.get_environment_template_version_output import GetEnvironmentTemplateVersionOutput
from openapi_server.models.get_repository_input import GetRepositoryInput
from openapi_server.models.get_repository_output import GetRepositoryOutput
from openapi_server.models.get_repository_sync_status_input import GetRepositorySyncStatusInput
from openapi_server.models.get_repository_sync_status_output import GetRepositorySyncStatusOutput
from openapi_server.models.get_resources_summary_output import GetResourcesSummaryOutput
from openapi_server.models.get_service_input import GetServiceInput
from openapi_server.models.get_service_instance_input import GetServiceInstanceInput
from openapi_server.models.get_service_instance_output import GetServiceInstanceOutput
from openapi_server.models.get_service_instance_sync_status_input import GetServiceInstanceSyncStatusInput
from openapi_server.models.get_service_instance_sync_status_output import GetServiceInstanceSyncStatusOutput
from openapi_server.models.get_service_output import GetServiceOutput
from openapi_server.models.get_service_sync_blocker_summary_input import GetServiceSyncBlockerSummaryInput
from openapi_server.models.get_service_sync_blocker_summary_output import GetServiceSyncBlockerSummaryOutput
from openapi_server.models.get_service_sync_config_input import GetServiceSyncConfigInput
from openapi_server.models.get_service_sync_config_output import GetServiceSyncConfigOutput
from openapi_server.models.get_service_template_input import GetServiceTemplateInput
from openapi_server.models.get_service_template_output import GetServiceTemplateOutput
from openapi_server.models.get_service_template_version_input import GetServiceTemplateVersionInput
from openapi_server.models.get_service_template_version_output import GetServiceTemplateVersionOutput
from openapi_server.models.get_template_sync_config_input import GetTemplateSyncConfigInput
from openapi_server.models.get_template_sync_config_output import GetTemplateSyncConfigOutput
from openapi_server.models.get_template_sync_status_input import GetTemplateSyncStatusInput
from openapi_server.models.get_template_sync_status_output import GetTemplateSyncStatusOutput
from openapi_server.models.list_component_outputs_input import ListComponentOutputsInput
from openapi_server.models.list_component_outputs_output import ListComponentOutputsOutput
from openapi_server.models.list_component_provisioned_resources_input import ListComponentProvisionedResourcesInput
from openapi_server.models.list_component_provisioned_resources_output import ListComponentProvisionedResourcesOutput
from openapi_server.models.list_components_input import ListComponentsInput
from openapi_server.models.list_components_output import ListComponentsOutput
from openapi_server.models.list_deployments_input import ListDeploymentsInput
from openapi_server.models.list_deployments_output import ListDeploymentsOutput
from openapi_server.models.list_environment_account_connections_input import ListEnvironmentAccountConnectionsInput
from openapi_server.models.list_environment_account_connections_output import ListEnvironmentAccountConnectionsOutput
from openapi_server.models.list_environment_outputs_input import ListEnvironmentOutputsInput
from openapi_server.models.list_environment_outputs_output import ListEnvironmentOutputsOutput
from openapi_server.models.list_environment_provisioned_resources_input import ListEnvironmentProvisionedResourcesInput
from openapi_server.models.list_environment_provisioned_resources_output import ListEnvironmentProvisionedResourcesOutput
from openapi_server.models.list_environment_template_versions_input import ListEnvironmentTemplateVersionsInput
from openapi_server.models.list_environment_template_versions_output import ListEnvironmentTemplateVersionsOutput
from openapi_server.models.list_environment_templates_input import ListEnvironmentTemplatesInput
from openapi_server.models.list_environment_templates_output import ListEnvironmentTemplatesOutput
from openapi_server.models.list_environments_input import ListEnvironmentsInput
from openapi_server.models.list_environments_output import ListEnvironmentsOutput
from openapi_server.models.list_repositories_input import ListRepositoriesInput
from openapi_server.models.list_repositories_output import ListRepositoriesOutput
from openapi_server.models.list_repository_sync_definitions_input import ListRepositorySyncDefinitionsInput
from openapi_server.models.list_repository_sync_definitions_output import ListRepositorySyncDefinitionsOutput
from openapi_server.models.list_service_instance_outputs_input import ListServiceInstanceOutputsInput
from openapi_server.models.list_service_instance_outputs_output import ListServiceInstanceOutputsOutput
from openapi_server.models.list_service_instance_provisioned_resources_input import ListServiceInstanceProvisionedResourcesInput
from openapi_server.models.list_service_instance_provisioned_resources_output import ListServiceInstanceProvisionedResourcesOutput
from openapi_server.models.list_service_instances_input import ListServiceInstancesInput
from openapi_server.models.list_service_instances_output import ListServiceInstancesOutput
from openapi_server.models.list_service_pipeline_outputs_input import ListServicePipelineOutputsInput
from openapi_server.models.list_service_pipeline_outputs_output import ListServicePipelineOutputsOutput
from openapi_server.models.list_service_pipeline_provisioned_resources_input import ListServicePipelineProvisionedResourcesInput
from openapi_server.models.list_service_pipeline_provisioned_resources_output import ListServicePipelineProvisionedResourcesOutput
from openapi_server.models.list_service_template_versions_input import ListServiceTemplateVersionsInput
from openapi_server.models.list_service_template_versions_output import ListServiceTemplateVersionsOutput
from openapi_server.models.list_service_templates_input import ListServiceTemplatesInput
from openapi_server.models.list_service_templates_output import ListServiceTemplatesOutput
from openapi_server.models.list_services_input import ListServicesInput
from openapi_server.models.list_services_output import ListServicesOutput
from openapi_server.models.list_tags_for_resource_input import ListTagsForResourceInput
from openapi_server.models.list_tags_for_resource_output import ListTagsForResourceOutput
from openapi_server.models.notify_resource_deployment_status_change_input import NotifyResourceDeploymentStatusChangeInput
from openapi_server.models.reject_environment_account_connection_input import RejectEnvironmentAccountConnectionInput
from openapi_server.models.reject_environment_account_connection_output import RejectEnvironmentAccountConnectionOutput
from openapi_server.models.tag_resource_input import TagResourceInput
from openapi_server.models.untag_resource_input import UntagResourceInput
from openapi_server.models.update_account_settings_input import UpdateAccountSettingsInput
from openapi_server.models.update_account_settings_output import UpdateAccountSettingsOutput
from openapi_server.models.update_component_input import UpdateComponentInput
from openapi_server.models.update_component_output import UpdateComponentOutput
from openapi_server.models.update_environment_account_connection_input import UpdateEnvironmentAccountConnectionInput
from openapi_server.models.update_environment_account_connection_output import UpdateEnvironmentAccountConnectionOutput
from openapi_server.models.update_environment_input import UpdateEnvironmentInput
from openapi_server.models.update_environment_output import UpdateEnvironmentOutput
from openapi_server.models.update_environment_template_input import UpdateEnvironmentTemplateInput
from openapi_server.models.update_environment_template_output import UpdateEnvironmentTemplateOutput
from openapi_server.models.update_environment_template_version_input import UpdateEnvironmentTemplateVersionInput
from openapi_server.models.update_environment_template_version_output import UpdateEnvironmentTemplateVersionOutput
from openapi_server.models.update_service_input import UpdateServiceInput
from openapi_server.models.update_service_instance_input import UpdateServiceInstanceInput
from openapi_server.models.update_service_instance_output import UpdateServiceInstanceOutput
from openapi_server.models.update_service_output import UpdateServiceOutput
from openapi_server.models.update_service_pipeline_input import UpdateServicePipelineInput
from openapi_server.models.update_service_pipeline_output import UpdateServicePipelineOutput
from openapi_server.models.update_service_sync_blocker_input import UpdateServiceSyncBlockerInput
from openapi_server.models.update_service_sync_blocker_output import UpdateServiceSyncBlockerOutput
from openapi_server.models.update_service_sync_config_input import UpdateServiceSyncConfigInput
from openapi_server.models.update_service_sync_config_output import UpdateServiceSyncConfigOutput
from openapi_server.models.update_service_template_input import UpdateServiceTemplateInput
from openapi_server.models.update_service_template_output import UpdateServiceTemplateOutput
from openapi_server.models.update_service_template_version_input import UpdateServiceTemplateVersionInput
from openapi_server.models.update_service_template_version_output import UpdateServiceTemplateVersionOutput
from openapi_server.models.update_template_sync_config_input import UpdateTemplateSyncConfigInput
from openapi_server.models.update_template_sync_config_output import UpdateTemplateSyncConfigOutput
from openapi_server import util


async def accept_environment_account_connection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """accept_environment_account_connection

    &lt;p&gt;In a management account, an environment account connection request is accepted. When the environment account connection request is accepted, Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\&quot;&gt;Environment account connections&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AcceptEnvironmentAccountConnectionInput.from_dict(body)
    return web.Response(status=200)


async def cancel_component_deployment(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_component_deployment

    &lt;p&gt;Attempts to cancel a component deployment (for a component that is in the &lt;code&gt;IN_PROGRESS&lt;/code&gt; deployment status).&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CancelComponentDeploymentInput.from_dict(body)
    return web.Response(status=200)


async def cancel_environment_deployment(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_environment_deployment

    &lt;p&gt;Attempts to cancel an environment deployment on an &lt;a&gt;UpdateEnvironment&lt;/a&gt; action, if the deployment is &lt;code&gt;IN_PROGRESS&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-update.html\&quot;&gt;Update an environment&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following list includes potential cancellation scenarios.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the cancellation attempt succeeds, the resulting deployment state is &lt;code&gt;CANCELLED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the cancellation attempt fails, the resulting deployment state is &lt;code&gt;FAILED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the current &lt;a&gt;UpdateEnvironment&lt;/a&gt; action succeeds before the cancellation attempt starts, the resulting deployment state is &lt;code&gt;SUCCEEDED&lt;/code&gt; and the cancellation attempt has no effect.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CancelEnvironmentDeploymentInput.from_dict(body)
    return web.Response(status=200)


async def cancel_service_instance_deployment(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_service_instance_deployment

    &lt;p&gt;Attempts to cancel a service instance deployment on an &lt;a&gt;UpdateServiceInstance&lt;/a&gt; action, if the deployment is &lt;code&gt;IN_PROGRESS&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-instance-update.html\&quot;&gt;Update a service instance&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following list includes potential cancellation scenarios.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the cancellation attempt succeeds, the resulting deployment state is &lt;code&gt;CANCELLED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the cancellation attempt fails, the resulting deployment state is &lt;code&gt;FAILED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the current &lt;a&gt;UpdateServiceInstance&lt;/a&gt; action succeeds before the cancellation attempt starts, the resulting deployment state is &lt;code&gt;SUCCEEDED&lt;/code&gt; and the cancellation attempt has no effect.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CancelServiceInstanceDeploymentInput.from_dict(body)
    return web.Response(status=200)


async def cancel_service_pipeline_deployment(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_service_pipeline_deployment

    &lt;p&gt;Attempts to cancel a service pipeline deployment on an &lt;a&gt;UpdateServicePipeline&lt;/a&gt; action, if the deployment is &lt;code&gt;IN_PROGRESS&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-pipeline-update.html\&quot;&gt;Update a service pipeline&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following list includes potential cancellation scenarios.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the cancellation attempt succeeds, the resulting deployment state is &lt;code&gt;CANCELLED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the cancellation attempt fails, the resulting deployment state is &lt;code&gt;FAILED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the current &lt;a&gt;UpdateServicePipeline&lt;/a&gt; action succeeds before the cancellation attempt starts, the resulting deployment state is &lt;code&gt;SUCCEEDED&lt;/code&gt; and the cancellation attempt has no effect.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CancelServicePipelineDeploymentInput.from_dict(body)
    return web.Response(status=200)


async def create_component(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_component

    &lt;p&gt;Create an Proton component. A component is an infrastructure extension for a service instance.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateComponentInput.from_dict(body)
    return web.Response(status=200)


async def create_environment(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_environment

    &lt;p&gt;Deploy a new environment. An Proton environment is created from an environment template that defines infrastructure and resources that can be shared across services.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;You can provision environments using the following methods:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Amazon Web Services-managed provisioning: Proton makes direct calls to provision your resources.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Self-managed provisioning: Proton makes pull requests on your repository to provide compiled infrastructure as code (IaC) files that your IaC engine uses to provision resources.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html\&quot;&gt;Environments&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html\&quot;&gt;Provisioning methods&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateEnvironmentInput.from_dict(body)
    return web.Response(status=200)


async def create_environment_account_connection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_environment_account_connection

    &lt;p&gt;Create an environment account connection in an environment account so that environment infrastructure resources can be provisioned in the environment account from a management account.&lt;/p&gt; &lt;p&gt;An environment account connection is a secure bi-directional connection between a &lt;i&gt;management account&lt;/i&gt; and an &lt;i&gt;environment account&lt;/i&gt; that maintains authorization and permissions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\&quot;&gt;Environment account connections&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateEnvironmentAccountConnectionInput.from_dict(body)
    return web.Response(status=200)


async def create_environment_template(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_environment_template

    &lt;p&gt;Create an environment template for Proton. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html\&quot;&gt;Environment Templates&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can create an environment template in one of the two following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Register and publish a &lt;i&gt;standard&lt;/i&gt; environment template that instructs Proton to deploy and manage environment infrastructure.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Register and publish a &lt;i&gt;customer managed&lt;/i&gt; environment template that connects Proton to your existing provisioned infrastructure that you manage. Proton &lt;i&gt;doesn&#39;t&lt;/i&gt; manage your existing provisioned infrastructure. To create an environment template for customer provisioned and managed infrastructure, include the &lt;code&gt;provisioning&lt;/code&gt; parameter and set the value to &lt;code&gt;CUSTOMER_MANAGED&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/template-create.html\&quot;&gt;Register and publish an environment template&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateEnvironmentTemplateInput.from_dict(body)
    return web.Response(status=200)


async def create_environment_template_version(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_environment_template_version

    Create a new major or minor version of an environment template. A major version of an environment template is a version that &lt;i&gt;isn&#39;t&lt;/i&gt; backwards compatible. A minor version of an environment template is a version that&#39;s backwards compatible within its major version.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateEnvironmentTemplateVersionInput.from_dict(body)
    return web.Response(status=200)


async def create_repository(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_repository

    &lt;p&gt;Create and register a link to a repository. Proton uses the link to repeatedly access the repository, to either push to it (self-managed provisioning) or pull from it (template sync). You can share a linked repository across multiple resources (like environments using self-managed provisioning, or synced templates). When you create a repository link, Proton creates a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/using-service-linked-roles.html\&quot;&gt;service-linked role&lt;/a&gt; for you.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self\&quot;&gt;Self-managed provisioning&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html#ag-template-bundles\&quot;&gt;Template bundles&lt;/a&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html\&quot;&gt;Template sync configurations&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateRepositoryInput.from_dict(body)
    return web.Response(status=200)


async def create_service(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_service

    Create an Proton service. An Proton service is an instantiation of a service template and often includes several service instances and pipeline. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-services.html\&quot;&gt;Services&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateServiceInput.from_dict(body)
    return web.Response(status=200)


async def create_service_instance(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_service_instance

    Create a service instance.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateServiceInstanceInput.from_dict(body)
    return web.Response(status=200)


async def create_service_sync_config(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_service_sync_config

    Create the Proton Ops configuration file.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateServiceSyncConfigInput.from_dict(body)
    return web.Response(status=200)


async def create_service_template(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_service_template

    Create a service template. The administrator creates a service template to define standardized infrastructure and an optional CI/CD service pipeline. Developers, in turn, select the service template from Proton. If the selected service template includes a service pipeline definition, they provide a link to their source code repository. Proton then deploys and manages the infrastructure defined by the selected service template. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html\&quot;&gt;Proton templates&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateServiceTemplateInput.from_dict(body)
    return web.Response(status=200)


async def create_service_template_version(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_service_template_version

    Create a new major or minor version of a service template. A major version of a service template is a version that &lt;i&gt;isn&#39;t&lt;/i&gt; backward compatible. A minor version of a service template is a version that&#39;s backward compatible within its major version.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateServiceTemplateVersionInput.from_dict(body)
    return web.Response(status=200)


async def create_template_sync_config(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_template_sync_config

    &lt;p&gt;Set up a template to create new template versions automatically by tracking a linked repository. A linked repository is a repository that has been registered with Proton. For more information, see &lt;a&gt;CreateRepository&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;When a commit is pushed to your linked repository, Proton checks for changes to your repository template bundles. If it detects a template bundle change, a new major or minor version of its template is created, if the version doesn’t already exist. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html\&quot;&gt;Template sync configurations&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateTemplateSyncConfigInput.from_dict(body)
    return web.Response(status=200)


async def delete_component(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_component

    &lt;p&gt;Delete an Proton component resource.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteComponentInput.from_dict(body)
    return web.Response(status=200)


async def delete_deployment(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_deployment

    Delete the deployment.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteDeploymentInput.from_dict(body)
    return web.Response(status=200)


async def delete_environment(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_environment

    Delete an environment.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteEnvironmentInput.from_dict(body)
    return web.Response(status=200)


async def delete_environment_account_connection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_environment_account_connection

    &lt;p&gt;In an environment account, delete an environment account connection.&lt;/p&gt; &lt;p&gt;After you delete an environment account connection that’s in use by an Proton environment, Proton &lt;i&gt;can’t&lt;/i&gt; manage the environment infrastructure resources until a new environment account connection is accepted for the environment account and associated environment. You&#39;re responsible for cleaning up provisioned resources that remain without an environment connection.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\&quot;&gt;Environment account connections&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteEnvironmentAccountConnectionInput.from_dict(body)
    return web.Response(status=200)


async def delete_environment_template(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_environment_template

    If no other major or minor versions of an environment template exist, delete the environment template.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteEnvironmentTemplateInput.from_dict(body)
    return web.Response(status=200)


async def delete_environment_template_version(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_environment_template_version

    &lt;p&gt;If no other minor versions of an environment template exist, delete a major version of the environment template if it&#39;s not the &lt;code&gt;Recommended&lt;/code&gt; version. Delete the &lt;code&gt;Recommended&lt;/code&gt; version of the environment template if no other major versions or minor versions of the environment template exist. A major version of an environment template is a version that&#39;s not backward compatible.&lt;/p&gt; &lt;p&gt;Delete a minor version of an environment template if it &lt;i&gt;isn&#39;t&lt;/i&gt; the &lt;code&gt;Recommended&lt;/code&gt; version. Delete a &lt;code&gt;Recommended&lt;/code&gt; minor version of the environment template if no other minor versions of the environment template exist. A minor version of an environment template is a version that&#39;s backward compatible.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteEnvironmentTemplateVersionInput.from_dict(body)
    return web.Response(status=200)


async def delete_repository(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_repository

    De-register and unlink your repository.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteRepositoryInput.from_dict(body)
    return web.Response(status=200)


async def delete_service(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_service

    &lt;p&gt;Delete a service, with its instances and pipeline.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t delete a service if it has any service instances that have components attached to them.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteServiceInput.from_dict(body)
    return web.Response(status=200)


async def delete_service_sync_config(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_service_sync_config

    Delete the Proton Ops file.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteServiceSyncConfigInput.from_dict(body)
    return web.Response(status=200)


async def delete_service_template(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_service_template

    If no other major or minor versions of the service template exist, delete the service template.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteServiceTemplateInput.from_dict(body)
    return web.Response(status=200)


async def delete_service_template_version(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_service_template_version

    &lt;p&gt;If no other minor versions of a service template exist, delete a major version of the service template if it&#39;s not the &lt;code&gt;Recommended&lt;/code&gt; version. Delete the &lt;code&gt;Recommended&lt;/code&gt; version of the service template if no other major versions or minor versions of the service template exist. A major version of a service template is a version that &lt;i&gt;isn&#39;t&lt;/i&gt; backwards compatible.&lt;/p&gt; &lt;p&gt;Delete a minor version of a service template if it&#39;s not the &lt;code&gt;Recommended&lt;/code&gt; version. Delete a &lt;code&gt;Recommended&lt;/code&gt; minor version of the service template if no other minor versions of the service template exist. A minor version of a service template is a version that&#39;s backwards compatible.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteServiceTemplateVersionInput.from_dict(body)
    return web.Response(status=200)


async def delete_template_sync_config(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_template_sync_config

    Delete a template sync configuration.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteTemplateSyncConfigInput.from_dict(body)
    return web.Response(status=200)


async def get_account_settings(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_account_settings

    Get detail data for Proton account-wide settings.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_component(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_component

    &lt;p&gt;Get detailed data for a component.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetComponentInput.from_dict(body)
    return web.Response(status=200)


async def get_deployment(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_deployment

    Get detailed data for a deployment.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetDeploymentInput.from_dict(body)
    return web.Response(status=200)


async def get_environment(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_environment

    Get detailed data for an environment.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetEnvironmentInput.from_dict(body)
    return web.Response(status=200)


async def get_environment_account_connection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_environment_account_connection

    &lt;p&gt;In an environment account, get the detailed data for an environment account connection.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\&quot;&gt;Environment account connections&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetEnvironmentAccountConnectionInput.from_dict(body)
    return web.Response(status=200)


async def get_environment_template(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_environment_template

    Get detailed data for an environment template.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetEnvironmentTemplateInput.from_dict(body)
    return web.Response(status=200)


async def get_environment_template_version(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_environment_template_version

    Get detailed data for a major or minor version of an environment template.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetEnvironmentTemplateVersionInput.from_dict(body)
    return web.Response(status=200)


async def get_repository(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_repository

    Get detail data for a linked repository.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetRepositoryInput.from_dict(body)
    return web.Response(status=200)


async def get_repository_sync_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_repository_sync_status

    &lt;p&gt;Get the sync status of a repository used for Proton template sync. For more information about template sync, see .&lt;/p&gt; &lt;note&gt; &lt;p&gt;A repository sync status isn&#39;t tied to the Proton Repository resource (or any other Proton resource). Therefore, tags on an Proton Repository resource have no effect on this action. Specifically, you can&#39;t use these tags to control access to this action using Attribute-based access control (ABAC).&lt;/p&gt; &lt;p&gt;For more information about ABAC, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags\&quot;&gt;ABAC&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetRepositorySyncStatusInput.from_dict(body)
    return web.Response(status=200)


async def get_resources_summary(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_resources_summary

    &lt;p&gt;Get counts of Proton resources.&lt;/p&gt; &lt;p&gt;For infrastructure-provisioning resources (environments, services, service instances, pipelines), the action returns staleness counts. A resource is stale when it&#39;s behind the recommended version of the Proton template that it uses and it needs an update to become current.&lt;/p&gt; &lt;p&gt;The action returns staleness counts (counts of resources that are up-to-date, behind a template major version, or behind a template minor version), the total number of resources, and the number of resources that are in a failed state, grouped by resource type. Components, environments, and service templates return less information - see the &lt;code&gt;components&lt;/code&gt;, &lt;code&gt;environments&lt;/code&gt;, and &lt;code&gt;serviceTemplates&lt;/code&gt; field descriptions.&lt;/p&gt; &lt;p&gt;For context, the action also returns the total number of each type of Proton template in the Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/monitoring-dashboard.html\&quot;&gt;Proton dashboard&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_service(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service

    Get detailed data for a service.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetServiceInput.from_dict(body)
    return web.Response(status=200)


async def get_service_instance(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service_instance

    Get detailed data for a service instance. A service instance is an instantiation of service template and it runs in a specific environment.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetServiceInstanceInput.from_dict(body)
    return web.Response(status=200)


async def get_service_instance_sync_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service_instance_sync_status

    Get the status of the synced service instance.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetServiceInstanceSyncStatusInput.from_dict(body)
    return web.Response(status=200)


async def get_service_sync_blocker_summary(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service_sync_blocker_summary

    Get detailed data for the service sync blocker summary.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetServiceSyncBlockerSummaryInput.from_dict(body)
    return web.Response(status=200)


async def get_service_sync_config(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service_sync_config

    Get detailed information for the service sync configuration.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetServiceSyncConfigInput.from_dict(body)
    return web.Response(status=200)


async def get_service_template(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service_template

    Get detailed data for a service template.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetServiceTemplateInput.from_dict(body)
    return web.Response(status=200)


async def get_service_template_version(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service_template_version

    Get detailed data for a major or minor version of a service template.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetServiceTemplateVersionInput.from_dict(body)
    return web.Response(status=200)


async def get_template_sync_config(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_template_sync_config

    Get detail data for a template sync configuration.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetTemplateSyncConfigInput.from_dict(body)
    return web.Response(status=200)


async def get_template_sync_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_template_sync_status

    Get the status of a template sync.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetTemplateSyncStatusInput.from_dict(body)
    return web.Response(status=200)


async def list_component_outputs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_component_outputs

    &lt;p&gt;Get a list of component Infrastructure as Code (IaC) outputs.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListComponentOutputsInput.from_dict(body)
    return web.Response(status=200)


async def list_component_provisioned_resources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_component_provisioned_resources

    &lt;p&gt;List provisioned resources for a component with details.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListComponentProvisionedResourcesInput.from_dict(body)
    return web.Response(status=200)


async def list_components(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_components

    &lt;p&gt;List components with summary data. You can filter the result list by environment, service, or a single service instance.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListComponentsInput.from_dict(body)
    return web.Response(status=200)


async def list_deployments(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_deployments

    List deployments. You can filter the result list by environment, service, or a single service instance.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListDeploymentsInput.from_dict(body)
    return web.Response(status=200)


async def list_environment_account_connections(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_environment_account_connections

    &lt;p&gt;View a list of environment account connections.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\&quot;&gt;Environment account connections&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListEnvironmentAccountConnectionsInput.from_dict(body)
    return web.Response(status=200)


async def list_environment_outputs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_environment_outputs

    List the infrastructure as code outputs for your environment.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListEnvironmentOutputsInput.from_dict(body)
    return web.Response(status=200)


async def list_environment_provisioned_resources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_environment_provisioned_resources

    List the provisioned resources for your environment.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListEnvironmentProvisionedResourcesInput.from_dict(body)
    return web.Response(status=200)


async def list_environment_template_versions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_environment_template_versions

    List major or minor versions of an environment template with detail data.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListEnvironmentTemplateVersionsInput.from_dict(body)
    return web.Response(status=200)


async def list_environment_templates(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_environment_templates

    List environment templates.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListEnvironmentTemplatesInput.from_dict(body)
    return web.Response(status=200)


async def list_environments(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_environments

    List environments with detail data summaries.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListEnvironmentsInput.from_dict(body)
    return web.Response(status=200)


async def list_repositories(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_repositories

    List linked repositories with detail data.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListRepositoriesInput.from_dict(body)
    return web.Response(status=200)


async def list_repository_sync_definitions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_repository_sync_definitions

    List repository sync definitions with detail data.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListRepositorySyncDefinitionsInput.from_dict(body)
    return web.Response(status=200)


async def list_service_instance_outputs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_service_instance_outputs

    Get a list service of instance Infrastructure as Code (IaC) outputs.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListServiceInstanceOutputsInput.from_dict(body)
    return web.Response(status=200)


async def list_service_instance_provisioned_resources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_service_instance_provisioned_resources

    List provisioned resources for a service instance with details.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListServiceInstanceProvisionedResourcesInput.from_dict(body)
    return web.Response(status=200)


async def list_service_instances(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_service_instances

    List service instances with summary data. This action lists service instances of all services in the Amazon Web Services account.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListServiceInstancesInput.from_dict(body)
    return web.Response(status=200)


async def list_service_pipeline_outputs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_service_pipeline_outputs

    Get a list of service pipeline Infrastructure as Code (IaC) outputs.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListServicePipelineOutputsInput.from_dict(body)
    return web.Response(status=200)


async def list_service_pipeline_provisioned_resources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_service_pipeline_provisioned_resources

    List provisioned resources for a service and pipeline with details.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListServicePipelineProvisionedResourcesInput.from_dict(body)
    return web.Response(status=200)


async def list_service_template_versions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_service_template_versions

    List major or minor versions of a service template with detail data.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListServiceTemplateVersionsInput.from_dict(body)
    return web.Response(status=200)


async def list_service_templates(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_service_templates

    List service templates with detail data.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListServiceTemplatesInput.from_dict(body)
    return web.Response(status=200)


async def list_services(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_services

    List services with summaries of detail data.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListServicesInput.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_tags_for_resource

    List tags for a resource. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/resources.html\&quot;&gt;Proton resources and tagging&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTagsForResourceInput.from_dict(body)
    return web.Response(status=200)


async def notify_resource_deployment_status_change(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """notify_resource_deployment_status_change

    &lt;p&gt;Notify Proton of status changes to a provisioned resource when you use self-managed provisioning.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self\&quot;&gt;Self-managed provisioning&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = NotifyResourceDeploymentStatusChangeInput.from_dict(body)
    return web.Response(status=200)


async def reject_environment_account_connection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reject_environment_account_connection

    &lt;p&gt;In a management account, reject an environment account connection from another environment account.&lt;/p&gt; &lt;p&gt;After you reject an environment account connection request, you &lt;i&gt;can&#39;t&lt;/i&gt; accept or use the rejected environment account connection.&lt;/p&gt; &lt;p&gt;You &lt;i&gt;can’t&lt;/i&gt; reject an environment account connection that&#39;s connected to an environment.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\&quot;&gt;Environment account connections&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RejectEnvironmentAccountConnectionInput.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Tag a resource. A tag is a key-value pair of metadata that you associate with an Proton resource.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/resources.html\&quot;&gt;Proton resources and tagging&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceInput.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    &lt;p&gt;Remove a customer tag from a resource. A tag is a key-value pair of metadata associated with an Proton resource.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/resources.html\&quot;&gt;Proton resources and tagging&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UntagResourceInput.from_dict(body)
    return web.Response(status=200)


async def update_account_settings(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_account_settings

    Update Proton settings that are used for multiple services in the Amazon Web Services account.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateAccountSettingsInput.from_dict(body)
    return web.Response(status=200)


async def update_component(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_component

    &lt;p&gt;Update a component.&lt;/p&gt; &lt;p&gt;There are a few modes for updating a component. The &lt;code&gt;deploymentType&lt;/code&gt; field defines the mode.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t update a component while its deployment status, or the deployment status of a service instance attached to it, is &lt;code&gt;IN_PROGRESS&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateComponentInput.from_dict(body)
    return web.Response(status=200)


async def update_environment(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_environment

    &lt;p&gt;Update an environment.&lt;/p&gt; &lt;p&gt;If the environment is associated with an environment account connection, &lt;i&gt;don&#39;t&lt;/i&gt; update or include the &lt;code&gt;protonServiceRoleArn&lt;/code&gt; and &lt;code&gt;provisioningRepository&lt;/code&gt; parameter to update or connect to an environment account connection.&lt;/p&gt; &lt;p&gt;You can only update to a new environment account connection if that connection was created in the same environment account that the current environment account connection was created in. The account connection must also be associated with the current environment.&lt;/p&gt; &lt;p&gt;If the environment &lt;i&gt;isn&#39;t&lt;/i&gt; associated with an environment account connection, &lt;i&gt;don&#39;t&lt;/i&gt; update or include the &lt;code&gt;environmentAccountConnectionId&lt;/code&gt; parameter. You &lt;i&gt;can&#39;t&lt;/i&gt; update or connect the environment to an environment account connection if it &lt;i&gt;isn&#39;t&lt;/i&gt; already associated with an environment connection.&lt;/p&gt; &lt;p&gt;You can update either the &lt;code&gt;environmentAccountConnectionId&lt;/code&gt; or &lt;code&gt;protonServiceRoleArn&lt;/code&gt; parameter and value. You can’t update both.&lt;/p&gt; &lt;p&gt;If the environment was configured for Amazon Web Services-managed provisioning, omit the &lt;code&gt;provisioningRepository&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;If the environment was configured for self-managed provisioning, specify the &lt;code&gt;provisioningRepository&lt;/code&gt; parameter and omit the &lt;code&gt;protonServiceRoleArn&lt;/code&gt; and &lt;code&gt;environmentAccountConnectionId&lt;/code&gt; parameters.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html\&quot;&gt;Environments&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html\&quot;&gt;Provisioning methods&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;There are four modes for updating an environment. The &lt;code&gt;deploymentType&lt;/code&gt; field defines the mode.&lt;/p&gt; &lt;dl&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;NONE&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, a deployment &lt;i&gt;doesn&#39;t&lt;/i&gt; occur. Only the requested metadata parameters are updated.&lt;/p&gt; &lt;/dd&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;CURRENT_VERSION&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, the environment is deployed and updated with the new spec that you provide. Only requested parameters are updated. &lt;i&gt;Don’t&lt;/i&gt; include minor or major version parameters when you use this &lt;code&gt;deployment-type&lt;/code&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;MINOR_VERSION&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, the environment is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.&lt;/p&gt; &lt;/dd&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;MAJOR_VERSION&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, the environment is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can also specify a different major version that&#39;s higher than the major version in use and a minor version.&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateEnvironmentInput.from_dict(body)
    return web.Response(status=200)


async def update_environment_account_connection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_environment_account_connection

    &lt;p&gt;In an environment account, update an environment account connection to use a new IAM role.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\&quot;&gt;Environment account connections&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateEnvironmentAccountConnectionInput.from_dict(body)
    return web.Response(status=200)


async def update_environment_template(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_environment_template

    Update an environment template.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateEnvironmentTemplateInput.from_dict(body)
    return web.Response(status=200)


async def update_environment_template_version(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_environment_template_version

    Update a major or minor version of an environment template.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateEnvironmentTemplateVersionInput.from_dict(body)
    return web.Response(status=200)


async def update_service(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service

    &lt;p&gt;Edit a service description or use a spec to add and delete service instances.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Existing service instances and the service pipeline &lt;i&gt;can&#39;t&lt;/i&gt; be edited using this API. They can only be deleted.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Use the &lt;code&gt;description&lt;/code&gt; parameter to modify the description.&lt;/p&gt; &lt;p&gt;Edit the &lt;code&gt;spec&lt;/code&gt; parameter to add or delete instances.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t delete a service instance (remove it from the spec) if it has an attached component.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateServiceInput.from_dict(body)
    return web.Response(status=200)


async def update_service_instance(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service_instance

    &lt;p&gt;Update a service instance.&lt;/p&gt; &lt;p&gt;There are a few modes for updating a service instance. The &lt;code&gt;deploymentType&lt;/code&gt; field defines the mode.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t update a service instance while its deployment status, or the deployment status of a component attached to it, is &lt;code&gt;IN_PROGRESS&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateServiceInstanceInput.from_dict(body)
    return web.Response(status=200)


async def update_service_pipeline(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service_pipeline

    &lt;p&gt;Update the service pipeline.&lt;/p&gt; &lt;p&gt;There are four modes for updating a service pipeline. The &lt;code&gt;deploymentType&lt;/code&gt; field defines the mode.&lt;/p&gt; &lt;dl&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;NONE&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, a deployment &lt;i&gt;doesn&#39;t&lt;/i&gt; occur. Only the requested metadata parameters are updated.&lt;/p&gt; &lt;/dd&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;CURRENT_VERSION&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. &lt;i&gt;Don’t&lt;/i&gt; include major or minor version parameters when you use this &lt;code&gt;deployment-type&lt;/code&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;MINOR_VERSION&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.&lt;/p&gt; &lt;/dd&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;MAJOR_VERSION&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template by default. You can specify a different major version that&#39;s higher than the major version in use and a minor version.&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateServicePipelineInput.from_dict(body)
    return web.Response(status=200)


async def update_service_sync_blocker(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service_sync_blocker

    Update the service sync blocker by resolving it.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateServiceSyncBlockerInput.from_dict(body)
    return web.Response(status=200)


async def update_service_sync_config(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service_sync_config

    Update the Proton Ops config file.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateServiceSyncConfigInput.from_dict(body)
    return web.Response(status=200)


async def update_service_template(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service_template

    Update a service template.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateServiceTemplateInput.from_dict(body)
    return web.Response(status=200)


async def update_service_template_version(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service_template_version

    Update a major or minor version of a service template.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateServiceTemplateVersionInput.from_dict(body)
    return web.Response(status=200)


async def update_template_sync_config(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_template_sync_config

    Update template sync configuration parameters, except for the &lt;code&gt;templateName&lt;/code&gt; and &lt;code&gt;templateType&lt;/code&gt;. Repository details (branch, name, and provider) should be of a linked repository. A linked repository is a repository that has been registered with Proton. For more information, see &lt;a&gt;CreateRepository&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateTemplateSyncConfigInput.from_dict(body)
    return web.Response(status=200)
