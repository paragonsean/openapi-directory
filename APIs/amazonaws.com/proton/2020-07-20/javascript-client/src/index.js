/**
 * AWS Proton
 * <p>This is the Proton Service API Reference. It provides descriptions, syntax and usage examples for each of the <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Operations.html\">actions</a> and <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Types.html\">data types</a> for the Proton service.</p> <p>The documentation for each action shows the Query API request parameters and the XML response.</p> <p>Alternatively, you can use the Amazon Web Services CLI to access an API. For more information, see the <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html\">Amazon Web Services Command Line Interface User Guide</a>.</p> <p>The Proton service is a two-pronged automation framework. Administrators create service templates to provide standardized infrastructure and deployment tooling for serverless and container based applications. Developers, in turn, select from the available service templates to automate their application or service deployments.</p> <p>Because administrators define the infrastructure and tooling that Proton deploys and manages, they need permissions to use all of the listed API operations.</p> <p>When developers select a specific infrastructure and tooling set, Proton deploys their applications. To monitor their applications that are running on Proton, developers need permissions to the service <i>create</i>, <i>list</i>, <i>update</i> and <i>delete</i> API operations and the service instance <i>list</i> and <i>update</i> API operations.</p> <p>To learn more about Proton, see the <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html\">Proton User Guide</a>.</p> <p> <b>Ensuring Idempotency</b> </p> <p>When you make a mutating API request, the request typically returns a result before the asynchronous workflows of the operation are complete. Operations might also time out or encounter other server issues before they're complete, even if the request already returned a result. This might make it difficult to determine whether the request succeeded. Moreover, you might need to retry the request multiple times to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation occurs multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request action completes no more than one time. With an idempotent request, if the original request action completes successfully, any subsequent retries complete successfully without performing any further actions. However, the result might contain updated information, such as the current creation status.</p> <p>The following lists of APIs are grouped according to methods that ensure idempotency.</p> <p> <b>Idempotent create APIs with a client token</b> </p> <p>The API actions in this list support idempotency with the use of a <i>client token</i>. The corresponding Amazon Web Services CLI commands also support idempotency using a client token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request. We recommend that you <i>don't</i> reuse the same client token for other API requests. If you don’t provide a client token for these APIs, a default client token is automatically provided by SDKs.</p> <p>Given a request action that has succeeded:</p> <p>If you retry the request using the same client token and the same parameters, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If you retry the request using the same client token, but one or more of the parameters are different, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Client tokens expire eight hours after a request is made. If you retry the request with the expired token, a new resource is created.</p> <p>If the original resource is deleted and you retry the request, a new resource is created.</p> <p>Idempotent create APIs with a client token:</p> <ul> <li> <p>CreateEnvironmentTemplateVersion</p> </li> <li> <p>CreateServiceTemplateVersion</p> </li> <li> <p>CreateEnvironmentAccountConnection</p> </li> </ul> <p> <b>Idempotent create APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, and the original resource <i>hasn't</i> been modified, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If the original resource has been modified, the retry throws a <code>ConflictException</code>.</p> <p>If you retry with different input parameters, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Idempotent create APIs:</p> <ul> <li> <p>CreateEnvironmentTemplate</p> </li> <li> <p>CreateServiceTemplate</p> </li> <li> <p>CreateEnvironment</p> </li> <li> <p>CreateService</p> </li> </ul> <p> <b>Idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>When you retry the request with an API from this group and the resource was deleted, its metadata is returned in the response.</p> <p>If you retry and the resource doesn't exist, the response is empty.</p> <p>In both cases, the retry succeeds.</p> <p>Idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironmentTemplate</p> </li> <li> <p>DeleteEnvironmentTemplateVersion</p> </li> <li> <p>DeleteServiceTemplate</p> </li> <li> <p>DeleteServiceTemplateVersion</p> </li> <li> <p>DeleteEnvironmentAccountConnection</p> </li> </ul> <p> <b>Asynchronous idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, if the original request delete operation status is <code>DELETE_IN_PROGRESS</code>, the retry returns the resource detail data in the response without performing any further actions.</p> <p>If the original request delete operation is complete, a retry returns an empty response.</p> <p>Asynchronous idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironment</p> </li> <li> <p>DeleteService</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2020-07-20
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import AcceptEnvironmentAccountConnectionInput from './model/AcceptEnvironmentAccountConnectionInput';
import AcceptEnvironmentAccountConnectionOutput from './model/AcceptEnvironmentAccountConnectionOutput';
import AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection from './model/AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection';
import AccountSettings from './model/AccountSettings';
import AccountSettingsPipelineProvisioningRepository from './model/AccountSettingsPipelineProvisioningRepository';
import BlockerStatus from './model/BlockerStatus';
import BlockerType from './model/BlockerType';
import CancelComponentDeploymentInput from './model/CancelComponentDeploymentInput';
import CancelComponentDeploymentOutput from './model/CancelComponentDeploymentOutput';
import CancelComponentDeploymentOutputComponent from './model/CancelComponentDeploymentOutputComponent';
import CancelEnvironmentDeploymentInput from './model/CancelEnvironmentDeploymentInput';
import CancelEnvironmentDeploymentOutput from './model/CancelEnvironmentDeploymentOutput';
import CancelEnvironmentDeploymentOutputEnvironment from './model/CancelEnvironmentDeploymentOutputEnvironment';
import CancelServiceInstanceDeploymentInput from './model/CancelServiceInstanceDeploymentInput';
import CancelServiceInstanceDeploymentOutput from './model/CancelServiceInstanceDeploymentOutput';
import CancelServiceInstanceDeploymentOutputServiceInstance from './model/CancelServiceInstanceDeploymentOutputServiceInstance';
import CancelServicePipelineDeploymentInput from './model/CancelServicePipelineDeploymentInput';
import CancelServicePipelineDeploymentOutput from './model/CancelServicePipelineDeploymentOutput';
import CancelServicePipelineDeploymentOutputPipeline from './model/CancelServicePipelineDeploymentOutputPipeline';
import CompatibleEnvironmentTemplate from './model/CompatibleEnvironmentTemplate';
import CompatibleEnvironmentTemplateInput from './model/CompatibleEnvironmentTemplateInput';
import Component from './model/Component';
import ComponentDeploymentUpdateType from './model/ComponentDeploymentUpdateType';
import ComponentState from './model/ComponentState';
import ComponentSummary from './model/ComponentSummary';
import CountsSummary from './model/CountsSummary';
import CountsSummaryComponents from './model/CountsSummaryComponents';
import CountsSummaryEnvironmentTemplates from './model/CountsSummaryEnvironmentTemplates';
import CountsSummaryEnvironments from './model/CountsSummaryEnvironments';
import CountsSummaryPipelines from './model/CountsSummaryPipelines';
import CountsSummaryServiceInstances from './model/CountsSummaryServiceInstances';
import CountsSummaryServiceTemplates from './model/CountsSummaryServiceTemplates';
import CountsSummaryServices from './model/CountsSummaryServices';
import CreateComponentInput from './model/CreateComponentInput';
import CreateComponentOutput from './model/CreateComponentOutput';
import CreateComponentOutputComponent from './model/CreateComponentOutputComponent';
import CreateEnvironmentAccountConnectionInput from './model/CreateEnvironmentAccountConnectionInput';
import CreateEnvironmentAccountConnectionOutput from './model/CreateEnvironmentAccountConnectionOutput';
import CreateEnvironmentAccountConnectionOutputEnvironmentAccountConnection from './model/CreateEnvironmentAccountConnectionOutputEnvironmentAccountConnection';
import CreateEnvironmentInput from './model/CreateEnvironmentInput';
import CreateEnvironmentInputProvisioningRepository from './model/CreateEnvironmentInputProvisioningRepository';
import CreateEnvironmentOutput from './model/CreateEnvironmentOutput';
import CreateEnvironmentOutputEnvironment from './model/CreateEnvironmentOutputEnvironment';
import CreateEnvironmentTemplateInput from './model/CreateEnvironmentTemplateInput';
import CreateEnvironmentTemplateOutput from './model/CreateEnvironmentTemplateOutput';
import CreateEnvironmentTemplateOutputEnvironmentTemplate from './model/CreateEnvironmentTemplateOutputEnvironmentTemplate';
import CreateEnvironmentTemplateVersionInput from './model/CreateEnvironmentTemplateVersionInput';
import CreateEnvironmentTemplateVersionInputSource from './model/CreateEnvironmentTemplateVersionInputSource';
import CreateEnvironmentTemplateVersionOutput from './model/CreateEnvironmentTemplateVersionOutput';
import CreateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion from './model/CreateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion';
import CreateRepositoryInput from './model/CreateRepositoryInput';
import CreateRepositoryOutput from './model/CreateRepositoryOutput';
import CreateRepositoryOutputRepository from './model/CreateRepositoryOutputRepository';
import CreateServiceInput from './model/CreateServiceInput';
import CreateServiceInstanceInput from './model/CreateServiceInstanceInput';
import CreateServiceInstanceOutput from './model/CreateServiceInstanceOutput';
import CreateServiceInstanceOutputServiceInstance from './model/CreateServiceInstanceOutputServiceInstance';
import CreateServiceOutput from './model/CreateServiceOutput';
import CreateServiceOutputService from './model/CreateServiceOutputService';
import CreateServiceSyncConfigInput from './model/CreateServiceSyncConfigInput';
import CreateServiceSyncConfigOutput from './model/CreateServiceSyncConfigOutput';
import CreateServiceSyncConfigOutputServiceSyncConfig from './model/CreateServiceSyncConfigOutputServiceSyncConfig';
import CreateServiceTemplateInput from './model/CreateServiceTemplateInput';
import CreateServiceTemplateOutput from './model/CreateServiceTemplateOutput';
import CreateServiceTemplateOutputServiceTemplate from './model/CreateServiceTemplateOutputServiceTemplate';
import CreateServiceTemplateVersionInput from './model/CreateServiceTemplateVersionInput';
import CreateServiceTemplateVersionInputSource from './model/CreateServiceTemplateVersionInputSource';
import CreateServiceTemplateVersionOutput from './model/CreateServiceTemplateVersionOutput';
import CreateServiceTemplateVersionOutputServiceTemplateVersion from './model/CreateServiceTemplateVersionOutputServiceTemplateVersion';
import CreateTemplateSyncConfigInput from './model/CreateTemplateSyncConfigInput';
import CreateTemplateSyncConfigOutput from './model/CreateTemplateSyncConfigOutput';
import CreateTemplateSyncConfigOutputTemplateSyncConfig from './model/CreateTemplateSyncConfigOutputTemplateSyncConfig';
import DeleteComponentInput from './model/DeleteComponentInput';
import DeleteComponentOutput from './model/DeleteComponentOutput';
import DeleteComponentOutputComponent from './model/DeleteComponentOutputComponent';
import DeleteDeploymentInput from './model/DeleteDeploymentInput';
import DeleteDeploymentOutput from './model/DeleteDeploymentOutput';
import DeleteDeploymentOutputDeployment from './model/DeleteDeploymentOutputDeployment';
import DeleteEnvironmentAccountConnectionInput from './model/DeleteEnvironmentAccountConnectionInput';
import DeleteEnvironmentAccountConnectionOutput from './model/DeleteEnvironmentAccountConnectionOutput';
import DeleteEnvironmentAccountConnectionOutputEnvironmentAccountConnection from './model/DeleteEnvironmentAccountConnectionOutputEnvironmentAccountConnection';
import DeleteEnvironmentInput from './model/DeleteEnvironmentInput';
import DeleteEnvironmentOutput from './model/DeleteEnvironmentOutput';
import DeleteEnvironmentOutputEnvironment from './model/DeleteEnvironmentOutputEnvironment';
import DeleteEnvironmentTemplateInput from './model/DeleteEnvironmentTemplateInput';
import DeleteEnvironmentTemplateOutput from './model/DeleteEnvironmentTemplateOutput';
import DeleteEnvironmentTemplateOutputEnvironmentTemplate from './model/DeleteEnvironmentTemplateOutputEnvironmentTemplate';
import DeleteEnvironmentTemplateVersionInput from './model/DeleteEnvironmentTemplateVersionInput';
import DeleteEnvironmentTemplateVersionOutput from './model/DeleteEnvironmentTemplateVersionOutput';
import DeleteEnvironmentTemplateVersionOutputEnvironmentTemplateVersion from './model/DeleteEnvironmentTemplateVersionOutputEnvironmentTemplateVersion';
import DeleteRepositoryInput from './model/DeleteRepositoryInput';
import DeleteRepositoryOutput from './model/DeleteRepositoryOutput';
import DeleteRepositoryOutputRepository from './model/DeleteRepositoryOutputRepository';
import DeleteServiceInput from './model/DeleteServiceInput';
import DeleteServiceOutput from './model/DeleteServiceOutput';
import DeleteServiceOutputService from './model/DeleteServiceOutputService';
import DeleteServiceSyncConfigInput from './model/DeleteServiceSyncConfigInput';
import DeleteServiceSyncConfigOutput from './model/DeleteServiceSyncConfigOutput';
import DeleteServiceSyncConfigOutputServiceSyncConfig from './model/DeleteServiceSyncConfigOutputServiceSyncConfig';
import DeleteServiceTemplateInput from './model/DeleteServiceTemplateInput';
import DeleteServiceTemplateOutput from './model/DeleteServiceTemplateOutput';
import DeleteServiceTemplateOutputServiceTemplate from './model/DeleteServiceTemplateOutputServiceTemplate';
import DeleteServiceTemplateVersionInput from './model/DeleteServiceTemplateVersionInput';
import DeleteServiceTemplateVersionOutput from './model/DeleteServiceTemplateVersionOutput';
import DeleteServiceTemplateVersionOutputServiceTemplateVersion from './model/DeleteServiceTemplateVersionOutputServiceTemplateVersion';
import DeleteTemplateSyncConfigInput from './model/DeleteTemplateSyncConfigInput';
import DeleteTemplateSyncConfigOutput from './model/DeleteTemplateSyncConfigOutput';
import Deployment from './model/Deployment';
import DeploymentInitialState from './model/DeploymentInitialState';
import DeploymentState from './model/DeploymentState';
import DeploymentStateComponent from './model/DeploymentStateComponent';
import DeploymentStateEnvironment from './model/DeploymentStateEnvironment';
import DeploymentStateServiceInstance from './model/DeploymentStateServiceInstance';
import DeploymentStateServicePipeline from './model/DeploymentStateServicePipeline';
import DeploymentStatus from './model/DeploymentStatus';
import DeploymentSummary from './model/DeploymentSummary';
import DeploymentTargetResourceType from './model/DeploymentTargetResourceType';
import DeploymentTargetState from './model/DeploymentTargetState';
import DeploymentUpdateType from './model/DeploymentUpdateType';
import Environment from './model/Environment';
import EnvironmentAccountConnection from './model/EnvironmentAccountConnection';
import EnvironmentAccountConnectionRequesterAccountType from './model/EnvironmentAccountConnectionRequesterAccountType';
import EnvironmentAccountConnectionStatus from './model/EnvironmentAccountConnectionStatus';
import EnvironmentAccountConnectionSummary from './model/EnvironmentAccountConnectionSummary';
import EnvironmentProvisioningRepository from './model/EnvironmentProvisioningRepository';
import EnvironmentState from './model/EnvironmentState';
import EnvironmentSummary from './model/EnvironmentSummary';
import EnvironmentTemplate from './model/EnvironmentTemplate';
import EnvironmentTemplateFilter from './model/EnvironmentTemplateFilter';
import EnvironmentTemplateSummary from './model/EnvironmentTemplateSummary';
import EnvironmentTemplateVersion from './model/EnvironmentTemplateVersion';
import EnvironmentTemplateVersionSummary from './model/EnvironmentTemplateVersionSummary';
import GetAccountSettingsOutput from './model/GetAccountSettingsOutput';
import GetAccountSettingsOutputAccountSettings from './model/GetAccountSettingsOutputAccountSettings';
import GetComponentInput from './model/GetComponentInput';
import GetComponentOutput from './model/GetComponentOutput';
import GetComponentOutputComponent from './model/GetComponentOutputComponent';
import GetDeploymentInput from './model/GetDeploymentInput';
import GetDeploymentOutput from './model/GetDeploymentOutput';
import GetDeploymentOutputDeployment from './model/GetDeploymentOutputDeployment';
import GetEnvironmentAccountConnectionInput from './model/GetEnvironmentAccountConnectionInput';
import GetEnvironmentAccountConnectionOutput from './model/GetEnvironmentAccountConnectionOutput';
import GetEnvironmentAccountConnectionOutputEnvironmentAccountConnection from './model/GetEnvironmentAccountConnectionOutputEnvironmentAccountConnection';
import GetEnvironmentInput from './model/GetEnvironmentInput';
import GetEnvironmentOutput from './model/GetEnvironmentOutput';
import GetEnvironmentOutputEnvironment from './model/GetEnvironmentOutputEnvironment';
import GetEnvironmentTemplateInput from './model/GetEnvironmentTemplateInput';
import GetEnvironmentTemplateOutput from './model/GetEnvironmentTemplateOutput';
import GetEnvironmentTemplateOutputEnvironmentTemplate from './model/GetEnvironmentTemplateOutputEnvironmentTemplate';
import GetEnvironmentTemplateVersionInput from './model/GetEnvironmentTemplateVersionInput';
import GetEnvironmentTemplateVersionOutput from './model/GetEnvironmentTemplateVersionOutput';
import GetEnvironmentTemplateVersionOutputEnvironmentTemplateVersion from './model/GetEnvironmentTemplateVersionOutputEnvironmentTemplateVersion';
import GetRepositoryInput from './model/GetRepositoryInput';
import GetRepositoryOutput from './model/GetRepositoryOutput';
import GetRepositorySyncStatusInput from './model/GetRepositorySyncStatusInput';
import GetRepositorySyncStatusOutput from './model/GetRepositorySyncStatusOutput';
import GetRepositorySyncStatusOutputLatestSync from './model/GetRepositorySyncStatusOutputLatestSync';
import GetResourcesSummaryOutput from './model/GetResourcesSummaryOutput';
import GetResourcesSummaryOutputCounts from './model/GetResourcesSummaryOutputCounts';
import GetServiceInput from './model/GetServiceInput';
import GetServiceInstanceInput from './model/GetServiceInstanceInput';
import GetServiceInstanceOutput from './model/GetServiceInstanceOutput';
import GetServiceInstanceOutputServiceInstance from './model/GetServiceInstanceOutputServiceInstance';
import GetServiceInstanceSyncStatusInput from './model/GetServiceInstanceSyncStatusInput';
import GetServiceInstanceSyncStatusOutput from './model/GetServiceInstanceSyncStatusOutput';
import GetServiceInstanceSyncStatusOutputDesiredState from './model/GetServiceInstanceSyncStatusOutputDesiredState';
import GetServiceInstanceSyncStatusOutputLatestSuccessfulSync from './model/GetServiceInstanceSyncStatusOutputLatestSuccessfulSync';
import GetServiceInstanceSyncStatusOutputLatestSync from './model/GetServiceInstanceSyncStatusOutputLatestSync';
import GetServiceOutput from './model/GetServiceOutput';
import GetServiceOutputService from './model/GetServiceOutputService';
import GetServiceSyncBlockerSummaryInput from './model/GetServiceSyncBlockerSummaryInput';
import GetServiceSyncBlockerSummaryOutput from './model/GetServiceSyncBlockerSummaryOutput';
import GetServiceSyncBlockerSummaryOutputServiceSyncBlockerSummary from './model/GetServiceSyncBlockerSummaryOutputServiceSyncBlockerSummary';
import GetServiceSyncConfigInput from './model/GetServiceSyncConfigInput';
import GetServiceSyncConfigOutput from './model/GetServiceSyncConfigOutput';
import GetServiceSyncConfigOutputServiceSyncConfig from './model/GetServiceSyncConfigOutputServiceSyncConfig';
import GetServiceTemplateInput from './model/GetServiceTemplateInput';
import GetServiceTemplateOutput from './model/GetServiceTemplateOutput';
import GetServiceTemplateOutputServiceTemplate from './model/GetServiceTemplateOutputServiceTemplate';
import GetServiceTemplateVersionInput from './model/GetServiceTemplateVersionInput';
import GetServiceTemplateVersionOutput from './model/GetServiceTemplateVersionOutput';
import GetServiceTemplateVersionOutputServiceTemplateVersion from './model/GetServiceTemplateVersionOutputServiceTemplateVersion';
import GetTemplateSyncConfigInput from './model/GetTemplateSyncConfigInput';
import GetTemplateSyncConfigOutput from './model/GetTemplateSyncConfigOutput';
import GetTemplateSyncStatusInput from './model/GetTemplateSyncStatusInput';
import GetTemplateSyncStatusOutput from './model/GetTemplateSyncStatusOutput';
import GetTemplateSyncStatusOutputDesiredState from './model/GetTemplateSyncStatusOutputDesiredState';
import GetTemplateSyncStatusOutputLatestSuccessfulSync from './model/GetTemplateSyncStatusOutputLatestSuccessfulSync';
import GetTemplateSyncStatusOutputLatestSync from './model/GetTemplateSyncStatusOutputLatestSync';
import ListComponentOutputsInput from './model/ListComponentOutputsInput';
import ListComponentOutputsOutput from './model/ListComponentOutputsOutput';
import ListComponentProvisionedResourcesInput from './model/ListComponentProvisionedResourcesInput';
import ListComponentProvisionedResourcesOutput from './model/ListComponentProvisionedResourcesOutput';
import ListComponentsInput from './model/ListComponentsInput';
import ListComponentsOutput from './model/ListComponentsOutput';
import ListDeploymentsInput from './model/ListDeploymentsInput';
import ListDeploymentsOutput from './model/ListDeploymentsOutput';
import ListEnvironmentAccountConnectionsInput from './model/ListEnvironmentAccountConnectionsInput';
import ListEnvironmentAccountConnectionsOutput from './model/ListEnvironmentAccountConnectionsOutput';
import ListEnvironmentOutputsInput from './model/ListEnvironmentOutputsInput';
import ListEnvironmentOutputsOutput from './model/ListEnvironmentOutputsOutput';
import ListEnvironmentProvisionedResourcesInput from './model/ListEnvironmentProvisionedResourcesInput';
import ListEnvironmentProvisionedResourcesOutput from './model/ListEnvironmentProvisionedResourcesOutput';
import ListEnvironmentTemplateVersionsInput from './model/ListEnvironmentTemplateVersionsInput';
import ListEnvironmentTemplateVersionsOutput from './model/ListEnvironmentTemplateVersionsOutput';
import ListEnvironmentTemplatesInput from './model/ListEnvironmentTemplatesInput';
import ListEnvironmentTemplatesOutput from './model/ListEnvironmentTemplatesOutput';
import ListEnvironmentsInput from './model/ListEnvironmentsInput';
import ListEnvironmentsOutput from './model/ListEnvironmentsOutput';
import ListRepositoriesInput from './model/ListRepositoriesInput';
import ListRepositoriesOutput from './model/ListRepositoriesOutput';
import ListRepositorySyncDefinitionsInput from './model/ListRepositorySyncDefinitionsInput';
import ListRepositorySyncDefinitionsOutput from './model/ListRepositorySyncDefinitionsOutput';
import ListServiceInstanceOutputsInput from './model/ListServiceInstanceOutputsInput';
import ListServiceInstanceOutputsOutput from './model/ListServiceInstanceOutputsOutput';
import ListServiceInstanceProvisionedResourcesInput from './model/ListServiceInstanceProvisionedResourcesInput';
import ListServiceInstanceProvisionedResourcesOutput from './model/ListServiceInstanceProvisionedResourcesOutput';
import ListServiceInstancesFilter from './model/ListServiceInstancesFilter';
import ListServiceInstancesFilterBy from './model/ListServiceInstancesFilterBy';
import ListServiceInstancesInput from './model/ListServiceInstancesInput';
import ListServiceInstancesOutput from './model/ListServiceInstancesOutput';
import ListServiceInstancesSortBy from './model/ListServiceInstancesSortBy';
import ListServicePipelineOutputsInput from './model/ListServicePipelineOutputsInput';
import ListServicePipelineOutputsOutput from './model/ListServicePipelineOutputsOutput';
import ListServicePipelineProvisionedResourcesInput from './model/ListServicePipelineProvisionedResourcesInput';
import ListServicePipelineProvisionedResourcesOutput from './model/ListServicePipelineProvisionedResourcesOutput';
import ListServiceTemplateVersionsInput from './model/ListServiceTemplateVersionsInput';
import ListServiceTemplateVersionsOutput from './model/ListServiceTemplateVersionsOutput';
import ListServiceTemplatesInput from './model/ListServiceTemplatesInput';
import ListServiceTemplatesOutput from './model/ListServiceTemplatesOutput';
import ListServicesInput from './model/ListServicesInput';
import ListServicesOutput from './model/ListServicesOutput';
import ListTagsForResourceInput from './model/ListTagsForResourceInput';
import ListTagsForResourceOutput from './model/ListTagsForResourceOutput';
import NotifyResourceDeploymentStatusChangeInput from './model/NotifyResourceDeploymentStatusChangeInput';
import Output from './model/Output';
import ProvisionedResource from './model/ProvisionedResource';
import ProvisionedResourceEngine from './model/ProvisionedResourceEngine';
import Provisioning from './model/Provisioning';
import RejectEnvironmentAccountConnectionInput from './model/RejectEnvironmentAccountConnectionInput';
import RejectEnvironmentAccountConnectionOutput from './model/RejectEnvironmentAccountConnectionOutput';
import RejectEnvironmentAccountConnectionOutputEnvironmentAccountConnection from './model/RejectEnvironmentAccountConnectionOutputEnvironmentAccountConnection';
import Repository from './model/Repository';
import RepositoryBranch from './model/RepositoryBranch';
import RepositoryBranchInput from './model/RepositoryBranchInput';
import RepositoryProvider from './model/RepositoryProvider';
import RepositorySummary from './model/RepositorySummary';
import RepositorySyncAttempt from './model/RepositorySyncAttempt';
import RepositorySyncDefinition from './model/RepositorySyncDefinition';
import RepositorySyncEvent from './model/RepositorySyncEvent';
import RepositorySyncStatus from './model/RepositorySyncStatus';
import ResourceCountsSummary from './model/ResourceCountsSummary';
import ResourceDeploymentStatus from './model/ResourceDeploymentStatus';
import ResourceSyncAttempt from './model/ResourceSyncAttempt';
import ResourceSyncAttemptInitialRevision from './model/ResourceSyncAttemptInitialRevision';
import ResourceSyncAttemptTargetRevision from './model/ResourceSyncAttemptTargetRevision';
import ResourceSyncEvent from './model/ResourceSyncEvent';
import ResourceSyncStatus from './model/ResourceSyncStatus';
import Revision from './model/Revision';
import S3ObjectSource from './model/S3ObjectSource';
import Service from './model/Service';
import ServiceInstance from './model/ServiceInstance';
import ServiceInstanceState from './model/ServiceInstanceState';
import ServiceInstanceSummary from './model/ServiceInstanceSummary';
import ServicePipeline from './model/ServicePipeline';
import ServicePipelineState from './model/ServicePipelineState';
import ServiceStatus from './model/ServiceStatus';
import ServiceSummary from './model/ServiceSummary';
import ServiceSyncBlockerSummary from './model/ServiceSyncBlockerSummary';
import ServiceSyncConfig from './model/ServiceSyncConfig';
import ServiceTemplate from './model/ServiceTemplate';
import ServiceTemplateSummary from './model/ServiceTemplateSummary';
import ServiceTemplateSupportedComponentSourceType from './model/ServiceTemplateSupportedComponentSourceType';
import ServiceTemplateVersion from './model/ServiceTemplateVersion';
import ServiceTemplateVersionSummary from './model/ServiceTemplateVersionSummary';
import SortOrder from './model/SortOrder';
import SyncBlocker from './model/SyncBlocker';
import SyncBlockerContext from './model/SyncBlockerContext';
import SyncType from './model/SyncType';
import Tag from './model/Tag';
import TagResourceInput from './model/TagResourceInput';
import TemplateSyncConfig from './model/TemplateSyncConfig';
import TemplateType from './model/TemplateType';
import TemplateVersionSourceInput from './model/TemplateVersionSourceInput';
import TemplateVersionSourceInputS3 from './model/TemplateVersionSourceInputS3';
import TemplateVersionStatus from './model/TemplateVersionStatus';
import UntagResourceInput from './model/UntagResourceInput';
import UpdateAccountSettingsInput from './model/UpdateAccountSettingsInput';
import UpdateAccountSettingsInputPipelineProvisioningRepository from './model/UpdateAccountSettingsInputPipelineProvisioningRepository';
import UpdateAccountSettingsOutput from './model/UpdateAccountSettingsOutput';
import UpdateAccountSettingsOutputAccountSettings from './model/UpdateAccountSettingsOutputAccountSettings';
import UpdateComponentInput from './model/UpdateComponentInput';
import UpdateComponentOutput from './model/UpdateComponentOutput';
import UpdateComponentOutputComponent from './model/UpdateComponentOutputComponent';
import UpdateEnvironmentAccountConnectionInput from './model/UpdateEnvironmentAccountConnectionInput';
import UpdateEnvironmentAccountConnectionOutput from './model/UpdateEnvironmentAccountConnectionOutput';
import UpdateEnvironmentInput from './model/UpdateEnvironmentInput';
import UpdateEnvironmentInputProvisioningRepository from './model/UpdateEnvironmentInputProvisioningRepository';
import UpdateEnvironmentOutput from './model/UpdateEnvironmentOutput';
import UpdateEnvironmentTemplateInput from './model/UpdateEnvironmentTemplateInput';
import UpdateEnvironmentTemplateOutput from './model/UpdateEnvironmentTemplateOutput';
import UpdateEnvironmentTemplateVersionInput from './model/UpdateEnvironmentTemplateVersionInput';
import UpdateEnvironmentTemplateVersionOutput from './model/UpdateEnvironmentTemplateVersionOutput';
import UpdateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion from './model/UpdateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion';
import UpdateServiceInput from './model/UpdateServiceInput';
import UpdateServiceInstanceInput from './model/UpdateServiceInstanceInput';
import UpdateServiceInstanceOutput from './model/UpdateServiceInstanceOutput';
import UpdateServiceOutput from './model/UpdateServiceOutput';
import UpdateServicePipelineInput from './model/UpdateServicePipelineInput';
import UpdateServicePipelineOutput from './model/UpdateServicePipelineOutput';
import UpdateServicePipelineOutputPipeline from './model/UpdateServicePipelineOutputPipeline';
import UpdateServiceSyncBlockerInput from './model/UpdateServiceSyncBlockerInput';
import UpdateServiceSyncBlockerOutput from './model/UpdateServiceSyncBlockerOutput';
import UpdateServiceSyncBlockerOutputServiceSyncBlocker from './model/UpdateServiceSyncBlockerOutputServiceSyncBlocker';
import UpdateServiceSyncConfigInput from './model/UpdateServiceSyncConfigInput';
import UpdateServiceSyncConfigOutput from './model/UpdateServiceSyncConfigOutput';
import UpdateServiceTemplateInput from './model/UpdateServiceTemplateInput';
import UpdateServiceTemplateOutput from './model/UpdateServiceTemplateOutput';
import UpdateServiceTemplateVersionInput from './model/UpdateServiceTemplateVersionInput';
import UpdateServiceTemplateVersionOutput from './model/UpdateServiceTemplateVersionOutput';
import UpdateServiceTemplateVersionOutputServiceTemplateVersion from './model/UpdateServiceTemplateVersionOutputServiceTemplateVersion';
import UpdateTemplateSyncConfigInput from './model/UpdateTemplateSyncConfigInput';
import UpdateTemplateSyncConfigOutput from './model/UpdateTemplateSyncConfigOutput';
import DefaultApi from './api/DefaultApi';


/**
* &lt;p&gt;This is the Proton Service API Reference. It provides descriptions, syntax and usage examples for each of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/APIReference/API_Operations.html\&quot;&gt;actions&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/APIReference/API_Types.html\&quot;&gt;data types&lt;/a&gt; for the Proton service.&lt;/p&gt; &lt;p&gt;The documentation for each action shows the Query API request parameters and the XML response.&lt;/p&gt; &lt;p&gt;Alternatively, you can use the Amazon Web Services CLI to access an API. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html\&quot;&gt;Amazon Web Services Command Line Interface User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The Proton service is a two-pronged automation framework. Administrators create service templates to provide standardized infrastructure and deployment tooling for serverless and container based applications. Developers, in turn, select from the available service templates to automate their application or service deployments.&lt;/p&gt; &lt;p&gt;Because administrators define the infrastructure and tooling that Proton deploys and manages, they need permissions to use all of the listed API operations.&lt;/p&gt; &lt;p&gt;When developers select a specific infrastructure and tooling set, Proton deploys their applications. To monitor their applications that are running on Proton, developers need permissions to the service &lt;i&gt;create&lt;/i&gt;, &lt;i&gt;list&lt;/i&gt;, &lt;i&gt;update&lt;/i&gt; and &lt;i&gt;delete&lt;/i&gt; API operations and the service instance &lt;i&gt;list&lt;/i&gt; and &lt;i&gt;update&lt;/i&gt; API operations.&lt;/p&gt; &lt;p&gt;To learn more about Proton, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html\&quot;&gt;Proton User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Ensuring Idempotency&lt;/b&gt; &lt;/p&gt; &lt;p&gt;When you make a mutating API request, the request typically returns a result before the asynchronous workflows of the operation are complete. Operations might also time out or encounter other server issues before they&#39;re complete, even if the request already returned a result. This might make it difficult to determine whether the request succeeded. Moreover, you might need to retry the request multiple times to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation occurs multiple times. This means that you might create more resources than you intended.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Idempotency&lt;/i&gt; ensures that an API request action completes no more than one time. With an idempotent request, if the original request action completes successfully, any subsequent retries complete successfully without performing any further actions. However, the result might contain updated information, such as the current creation status.&lt;/p&gt; &lt;p&gt;The following lists of APIs are grouped according to methods that ensure idempotency.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Idempotent create APIs with a client token&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The API actions in this list support idempotency with the use of a &lt;i&gt;client token&lt;/i&gt;. The corresponding Amazon Web Services CLI commands also support idempotency using a client token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request. We recommend that you &lt;i&gt;don&#39;t&lt;/i&gt; reuse the same client token for other API requests. If you don’t provide a client token for these APIs, a default client token is automatically provided by SDKs.&lt;/p&gt; &lt;p&gt;Given a request action that has succeeded:&lt;/p&gt; &lt;p&gt;If you retry the request using the same client token and the same parameters, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.&lt;/p&gt; &lt;p&gt;If you retry the request using the same client token, but one or more of the parameters are different, the retry throws a &lt;code&gt;ValidationException&lt;/code&gt; with an &lt;code&gt;IdempotentParameterMismatch&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;Client tokens expire eight hours after a request is made. If you retry the request with the expired token, a new resource is created.&lt;/p&gt; &lt;p&gt;If the original resource is deleted and you retry the request, a new resource is created.&lt;/p&gt; &lt;p&gt;Idempotent create APIs with a client token:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;CreateEnvironmentTemplateVersion&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CreateServiceTemplateVersion&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CreateEnvironmentAccountConnection&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Idempotent create APIs&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Given a request action that has succeeded:&lt;/p&gt; &lt;p&gt;If you retry the request with an API from this group, and the original resource &lt;i&gt;hasn&#39;t&lt;/i&gt; been modified, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.&lt;/p&gt; &lt;p&gt;If the original resource has been modified, the retry throws a &lt;code&gt;ConflictException&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you retry with different input parameters, the retry throws a &lt;code&gt;ValidationException&lt;/code&gt; with an &lt;code&gt;IdempotentParameterMismatch&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;Idempotent create APIs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;CreateEnvironmentTemplate&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CreateServiceTemplate&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CreateEnvironment&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CreateService&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Idempotent delete APIs&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Given a request action that has succeeded:&lt;/p&gt; &lt;p&gt;When you retry the request with an API from this group and the resource was deleted, its metadata is returned in the response.&lt;/p&gt; &lt;p&gt;If you retry and the resource doesn&#39;t exist, the response is empty.&lt;/p&gt; &lt;p&gt;In both cases, the retry succeeds.&lt;/p&gt; &lt;p&gt;Idempotent delete APIs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;DeleteEnvironmentTemplate&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;DeleteEnvironmentTemplateVersion&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;DeleteServiceTemplate&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;DeleteServiceTemplateVersion&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;DeleteEnvironmentAccountConnection&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Asynchronous idempotent delete APIs&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Given a request action that has succeeded:&lt;/p&gt; &lt;p&gt;If you retry the request with an API from this group, if the original request delete operation status is &lt;code&gt;DELETE_IN_PROGRESS&lt;/code&gt;, the retry returns the resource detail data in the response without performing any further actions.&lt;/p&gt; &lt;p&gt;If the original request delete operation is complete, a retry returns an empty response.&lt;/p&gt; &lt;p&gt;Asynchronous idempotent delete APIs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;DeleteEnvironment&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;DeleteService&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var AwsProton = require('index'); // See note below*.
* var xxxSvc = new AwsProton.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new AwsProton.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new AwsProton.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new AwsProton.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2020-07-20
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AcceptEnvironmentAccountConnectionInput model constructor.
     * @property {module:model/AcceptEnvironmentAccountConnectionInput}
     */
    AcceptEnvironmentAccountConnectionInput,

    /**
     * The AcceptEnvironmentAccountConnectionOutput model constructor.
     * @property {module:model/AcceptEnvironmentAccountConnectionOutput}
     */
    AcceptEnvironmentAccountConnectionOutput,

    /**
     * The AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection model constructor.
     * @property {module:model/AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection}
     */
    AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection,

    /**
     * The AccountSettings model constructor.
     * @property {module:model/AccountSettings}
     */
    AccountSettings,

    /**
     * The AccountSettingsPipelineProvisioningRepository model constructor.
     * @property {module:model/AccountSettingsPipelineProvisioningRepository}
     */
    AccountSettingsPipelineProvisioningRepository,

    /**
     * The BlockerStatus model constructor.
     * @property {module:model/BlockerStatus}
     */
    BlockerStatus,

    /**
     * The BlockerType model constructor.
     * @property {module:model/BlockerType}
     */
    BlockerType,

    /**
     * The CancelComponentDeploymentInput model constructor.
     * @property {module:model/CancelComponentDeploymentInput}
     */
    CancelComponentDeploymentInput,

    /**
     * The CancelComponentDeploymentOutput model constructor.
     * @property {module:model/CancelComponentDeploymentOutput}
     */
    CancelComponentDeploymentOutput,

    /**
     * The CancelComponentDeploymentOutputComponent model constructor.
     * @property {module:model/CancelComponentDeploymentOutputComponent}
     */
    CancelComponentDeploymentOutputComponent,

    /**
     * The CancelEnvironmentDeploymentInput model constructor.
     * @property {module:model/CancelEnvironmentDeploymentInput}
     */
    CancelEnvironmentDeploymentInput,

    /**
     * The CancelEnvironmentDeploymentOutput model constructor.
     * @property {module:model/CancelEnvironmentDeploymentOutput}
     */
    CancelEnvironmentDeploymentOutput,

    /**
     * The CancelEnvironmentDeploymentOutputEnvironment model constructor.
     * @property {module:model/CancelEnvironmentDeploymentOutputEnvironment}
     */
    CancelEnvironmentDeploymentOutputEnvironment,

    /**
     * The CancelServiceInstanceDeploymentInput model constructor.
     * @property {module:model/CancelServiceInstanceDeploymentInput}
     */
    CancelServiceInstanceDeploymentInput,

    /**
     * The CancelServiceInstanceDeploymentOutput model constructor.
     * @property {module:model/CancelServiceInstanceDeploymentOutput}
     */
    CancelServiceInstanceDeploymentOutput,

    /**
     * The CancelServiceInstanceDeploymentOutputServiceInstance model constructor.
     * @property {module:model/CancelServiceInstanceDeploymentOutputServiceInstance}
     */
    CancelServiceInstanceDeploymentOutputServiceInstance,

    /**
     * The CancelServicePipelineDeploymentInput model constructor.
     * @property {module:model/CancelServicePipelineDeploymentInput}
     */
    CancelServicePipelineDeploymentInput,

    /**
     * The CancelServicePipelineDeploymentOutput model constructor.
     * @property {module:model/CancelServicePipelineDeploymentOutput}
     */
    CancelServicePipelineDeploymentOutput,

    /**
     * The CancelServicePipelineDeploymentOutputPipeline model constructor.
     * @property {module:model/CancelServicePipelineDeploymentOutputPipeline}
     */
    CancelServicePipelineDeploymentOutputPipeline,

    /**
     * The CompatibleEnvironmentTemplate model constructor.
     * @property {module:model/CompatibleEnvironmentTemplate}
     */
    CompatibleEnvironmentTemplate,

    /**
     * The CompatibleEnvironmentTemplateInput model constructor.
     * @property {module:model/CompatibleEnvironmentTemplateInput}
     */
    CompatibleEnvironmentTemplateInput,

    /**
     * The Component model constructor.
     * @property {module:model/Component}
     */
    Component,

    /**
     * The ComponentDeploymentUpdateType model constructor.
     * @property {module:model/ComponentDeploymentUpdateType}
     */
    ComponentDeploymentUpdateType,

    /**
     * The ComponentState model constructor.
     * @property {module:model/ComponentState}
     */
    ComponentState,

    /**
     * The ComponentSummary model constructor.
     * @property {module:model/ComponentSummary}
     */
    ComponentSummary,

    /**
     * The CountsSummary model constructor.
     * @property {module:model/CountsSummary}
     */
    CountsSummary,

    /**
     * The CountsSummaryComponents model constructor.
     * @property {module:model/CountsSummaryComponents}
     */
    CountsSummaryComponents,

    /**
     * The CountsSummaryEnvironmentTemplates model constructor.
     * @property {module:model/CountsSummaryEnvironmentTemplates}
     */
    CountsSummaryEnvironmentTemplates,

    /**
     * The CountsSummaryEnvironments model constructor.
     * @property {module:model/CountsSummaryEnvironments}
     */
    CountsSummaryEnvironments,

    /**
     * The CountsSummaryPipelines model constructor.
     * @property {module:model/CountsSummaryPipelines}
     */
    CountsSummaryPipelines,

    /**
     * The CountsSummaryServiceInstances model constructor.
     * @property {module:model/CountsSummaryServiceInstances}
     */
    CountsSummaryServiceInstances,

    /**
     * The CountsSummaryServiceTemplates model constructor.
     * @property {module:model/CountsSummaryServiceTemplates}
     */
    CountsSummaryServiceTemplates,

    /**
     * The CountsSummaryServices model constructor.
     * @property {module:model/CountsSummaryServices}
     */
    CountsSummaryServices,

    /**
     * The CreateComponentInput model constructor.
     * @property {module:model/CreateComponentInput}
     */
    CreateComponentInput,

    /**
     * The CreateComponentOutput model constructor.
     * @property {module:model/CreateComponentOutput}
     */
    CreateComponentOutput,

    /**
     * The CreateComponentOutputComponent model constructor.
     * @property {module:model/CreateComponentOutputComponent}
     */
    CreateComponentOutputComponent,

    /**
     * The CreateEnvironmentAccountConnectionInput model constructor.
     * @property {module:model/CreateEnvironmentAccountConnectionInput}
     */
    CreateEnvironmentAccountConnectionInput,

    /**
     * The CreateEnvironmentAccountConnectionOutput model constructor.
     * @property {module:model/CreateEnvironmentAccountConnectionOutput}
     */
    CreateEnvironmentAccountConnectionOutput,

    /**
     * The CreateEnvironmentAccountConnectionOutputEnvironmentAccountConnection model constructor.
     * @property {module:model/CreateEnvironmentAccountConnectionOutputEnvironmentAccountConnection}
     */
    CreateEnvironmentAccountConnectionOutputEnvironmentAccountConnection,

    /**
     * The CreateEnvironmentInput model constructor.
     * @property {module:model/CreateEnvironmentInput}
     */
    CreateEnvironmentInput,

    /**
     * The CreateEnvironmentInputProvisioningRepository model constructor.
     * @property {module:model/CreateEnvironmentInputProvisioningRepository}
     */
    CreateEnvironmentInputProvisioningRepository,

    /**
     * The CreateEnvironmentOutput model constructor.
     * @property {module:model/CreateEnvironmentOutput}
     */
    CreateEnvironmentOutput,

    /**
     * The CreateEnvironmentOutputEnvironment model constructor.
     * @property {module:model/CreateEnvironmentOutputEnvironment}
     */
    CreateEnvironmentOutputEnvironment,

    /**
     * The CreateEnvironmentTemplateInput model constructor.
     * @property {module:model/CreateEnvironmentTemplateInput}
     */
    CreateEnvironmentTemplateInput,

    /**
     * The CreateEnvironmentTemplateOutput model constructor.
     * @property {module:model/CreateEnvironmentTemplateOutput}
     */
    CreateEnvironmentTemplateOutput,

    /**
     * The CreateEnvironmentTemplateOutputEnvironmentTemplate model constructor.
     * @property {module:model/CreateEnvironmentTemplateOutputEnvironmentTemplate}
     */
    CreateEnvironmentTemplateOutputEnvironmentTemplate,

    /**
     * The CreateEnvironmentTemplateVersionInput model constructor.
     * @property {module:model/CreateEnvironmentTemplateVersionInput}
     */
    CreateEnvironmentTemplateVersionInput,

    /**
     * The CreateEnvironmentTemplateVersionInputSource model constructor.
     * @property {module:model/CreateEnvironmentTemplateVersionInputSource}
     */
    CreateEnvironmentTemplateVersionInputSource,

    /**
     * The CreateEnvironmentTemplateVersionOutput model constructor.
     * @property {module:model/CreateEnvironmentTemplateVersionOutput}
     */
    CreateEnvironmentTemplateVersionOutput,

    /**
     * The CreateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion model constructor.
     * @property {module:model/CreateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion}
     */
    CreateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion,

    /**
     * The CreateRepositoryInput model constructor.
     * @property {module:model/CreateRepositoryInput}
     */
    CreateRepositoryInput,

    /**
     * The CreateRepositoryOutput model constructor.
     * @property {module:model/CreateRepositoryOutput}
     */
    CreateRepositoryOutput,

    /**
     * The CreateRepositoryOutputRepository model constructor.
     * @property {module:model/CreateRepositoryOutputRepository}
     */
    CreateRepositoryOutputRepository,

    /**
     * The CreateServiceInput model constructor.
     * @property {module:model/CreateServiceInput}
     */
    CreateServiceInput,

    /**
     * The CreateServiceInstanceInput model constructor.
     * @property {module:model/CreateServiceInstanceInput}
     */
    CreateServiceInstanceInput,

    /**
     * The CreateServiceInstanceOutput model constructor.
     * @property {module:model/CreateServiceInstanceOutput}
     */
    CreateServiceInstanceOutput,

    /**
     * The CreateServiceInstanceOutputServiceInstance model constructor.
     * @property {module:model/CreateServiceInstanceOutputServiceInstance}
     */
    CreateServiceInstanceOutputServiceInstance,

    /**
     * The CreateServiceOutput model constructor.
     * @property {module:model/CreateServiceOutput}
     */
    CreateServiceOutput,

    /**
     * The CreateServiceOutputService model constructor.
     * @property {module:model/CreateServiceOutputService}
     */
    CreateServiceOutputService,

    /**
     * The CreateServiceSyncConfigInput model constructor.
     * @property {module:model/CreateServiceSyncConfigInput}
     */
    CreateServiceSyncConfigInput,

    /**
     * The CreateServiceSyncConfigOutput model constructor.
     * @property {module:model/CreateServiceSyncConfigOutput}
     */
    CreateServiceSyncConfigOutput,

    /**
     * The CreateServiceSyncConfigOutputServiceSyncConfig model constructor.
     * @property {module:model/CreateServiceSyncConfigOutputServiceSyncConfig}
     */
    CreateServiceSyncConfigOutputServiceSyncConfig,

    /**
     * The CreateServiceTemplateInput model constructor.
     * @property {module:model/CreateServiceTemplateInput}
     */
    CreateServiceTemplateInput,

    /**
     * The CreateServiceTemplateOutput model constructor.
     * @property {module:model/CreateServiceTemplateOutput}
     */
    CreateServiceTemplateOutput,

    /**
     * The CreateServiceTemplateOutputServiceTemplate model constructor.
     * @property {module:model/CreateServiceTemplateOutputServiceTemplate}
     */
    CreateServiceTemplateOutputServiceTemplate,

    /**
     * The CreateServiceTemplateVersionInput model constructor.
     * @property {module:model/CreateServiceTemplateVersionInput}
     */
    CreateServiceTemplateVersionInput,

    /**
     * The CreateServiceTemplateVersionInputSource model constructor.
     * @property {module:model/CreateServiceTemplateVersionInputSource}
     */
    CreateServiceTemplateVersionInputSource,

    /**
     * The CreateServiceTemplateVersionOutput model constructor.
     * @property {module:model/CreateServiceTemplateVersionOutput}
     */
    CreateServiceTemplateVersionOutput,

    /**
     * The CreateServiceTemplateVersionOutputServiceTemplateVersion model constructor.
     * @property {module:model/CreateServiceTemplateVersionOutputServiceTemplateVersion}
     */
    CreateServiceTemplateVersionOutputServiceTemplateVersion,

    /**
     * The CreateTemplateSyncConfigInput model constructor.
     * @property {module:model/CreateTemplateSyncConfigInput}
     */
    CreateTemplateSyncConfigInput,

    /**
     * The CreateTemplateSyncConfigOutput model constructor.
     * @property {module:model/CreateTemplateSyncConfigOutput}
     */
    CreateTemplateSyncConfigOutput,

    /**
     * The CreateTemplateSyncConfigOutputTemplateSyncConfig model constructor.
     * @property {module:model/CreateTemplateSyncConfigOutputTemplateSyncConfig}
     */
    CreateTemplateSyncConfigOutputTemplateSyncConfig,

    /**
     * The DeleteComponentInput model constructor.
     * @property {module:model/DeleteComponentInput}
     */
    DeleteComponentInput,

    /**
     * The DeleteComponentOutput model constructor.
     * @property {module:model/DeleteComponentOutput}
     */
    DeleteComponentOutput,

    /**
     * The DeleteComponentOutputComponent model constructor.
     * @property {module:model/DeleteComponentOutputComponent}
     */
    DeleteComponentOutputComponent,

    /**
     * The DeleteDeploymentInput model constructor.
     * @property {module:model/DeleteDeploymentInput}
     */
    DeleteDeploymentInput,

    /**
     * The DeleteDeploymentOutput model constructor.
     * @property {module:model/DeleteDeploymentOutput}
     */
    DeleteDeploymentOutput,

    /**
     * The DeleteDeploymentOutputDeployment model constructor.
     * @property {module:model/DeleteDeploymentOutputDeployment}
     */
    DeleteDeploymentOutputDeployment,

    /**
     * The DeleteEnvironmentAccountConnectionInput model constructor.
     * @property {module:model/DeleteEnvironmentAccountConnectionInput}
     */
    DeleteEnvironmentAccountConnectionInput,

    /**
     * The DeleteEnvironmentAccountConnectionOutput model constructor.
     * @property {module:model/DeleteEnvironmentAccountConnectionOutput}
     */
    DeleteEnvironmentAccountConnectionOutput,

    /**
     * The DeleteEnvironmentAccountConnectionOutputEnvironmentAccountConnection model constructor.
     * @property {module:model/DeleteEnvironmentAccountConnectionOutputEnvironmentAccountConnection}
     */
    DeleteEnvironmentAccountConnectionOutputEnvironmentAccountConnection,

    /**
     * The DeleteEnvironmentInput model constructor.
     * @property {module:model/DeleteEnvironmentInput}
     */
    DeleteEnvironmentInput,

    /**
     * The DeleteEnvironmentOutput model constructor.
     * @property {module:model/DeleteEnvironmentOutput}
     */
    DeleteEnvironmentOutput,

    /**
     * The DeleteEnvironmentOutputEnvironment model constructor.
     * @property {module:model/DeleteEnvironmentOutputEnvironment}
     */
    DeleteEnvironmentOutputEnvironment,

    /**
     * The DeleteEnvironmentTemplateInput model constructor.
     * @property {module:model/DeleteEnvironmentTemplateInput}
     */
    DeleteEnvironmentTemplateInput,

    /**
     * The DeleteEnvironmentTemplateOutput model constructor.
     * @property {module:model/DeleteEnvironmentTemplateOutput}
     */
    DeleteEnvironmentTemplateOutput,

    /**
     * The DeleteEnvironmentTemplateOutputEnvironmentTemplate model constructor.
     * @property {module:model/DeleteEnvironmentTemplateOutputEnvironmentTemplate}
     */
    DeleteEnvironmentTemplateOutputEnvironmentTemplate,

    /**
     * The DeleteEnvironmentTemplateVersionInput model constructor.
     * @property {module:model/DeleteEnvironmentTemplateVersionInput}
     */
    DeleteEnvironmentTemplateVersionInput,

    /**
     * The DeleteEnvironmentTemplateVersionOutput model constructor.
     * @property {module:model/DeleteEnvironmentTemplateVersionOutput}
     */
    DeleteEnvironmentTemplateVersionOutput,

    /**
     * The DeleteEnvironmentTemplateVersionOutputEnvironmentTemplateVersion model constructor.
     * @property {module:model/DeleteEnvironmentTemplateVersionOutputEnvironmentTemplateVersion}
     */
    DeleteEnvironmentTemplateVersionOutputEnvironmentTemplateVersion,

    /**
     * The DeleteRepositoryInput model constructor.
     * @property {module:model/DeleteRepositoryInput}
     */
    DeleteRepositoryInput,

    /**
     * The DeleteRepositoryOutput model constructor.
     * @property {module:model/DeleteRepositoryOutput}
     */
    DeleteRepositoryOutput,

    /**
     * The DeleteRepositoryOutputRepository model constructor.
     * @property {module:model/DeleteRepositoryOutputRepository}
     */
    DeleteRepositoryOutputRepository,

    /**
     * The DeleteServiceInput model constructor.
     * @property {module:model/DeleteServiceInput}
     */
    DeleteServiceInput,

    /**
     * The DeleteServiceOutput model constructor.
     * @property {module:model/DeleteServiceOutput}
     */
    DeleteServiceOutput,

    /**
     * The DeleteServiceOutputService model constructor.
     * @property {module:model/DeleteServiceOutputService}
     */
    DeleteServiceOutputService,

    /**
     * The DeleteServiceSyncConfigInput model constructor.
     * @property {module:model/DeleteServiceSyncConfigInput}
     */
    DeleteServiceSyncConfigInput,

    /**
     * The DeleteServiceSyncConfigOutput model constructor.
     * @property {module:model/DeleteServiceSyncConfigOutput}
     */
    DeleteServiceSyncConfigOutput,

    /**
     * The DeleteServiceSyncConfigOutputServiceSyncConfig model constructor.
     * @property {module:model/DeleteServiceSyncConfigOutputServiceSyncConfig}
     */
    DeleteServiceSyncConfigOutputServiceSyncConfig,

    /**
     * The DeleteServiceTemplateInput model constructor.
     * @property {module:model/DeleteServiceTemplateInput}
     */
    DeleteServiceTemplateInput,

    /**
     * The DeleteServiceTemplateOutput model constructor.
     * @property {module:model/DeleteServiceTemplateOutput}
     */
    DeleteServiceTemplateOutput,

    /**
     * The DeleteServiceTemplateOutputServiceTemplate model constructor.
     * @property {module:model/DeleteServiceTemplateOutputServiceTemplate}
     */
    DeleteServiceTemplateOutputServiceTemplate,

    /**
     * The DeleteServiceTemplateVersionInput model constructor.
     * @property {module:model/DeleteServiceTemplateVersionInput}
     */
    DeleteServiceTemplateVersionInput,

    /**
     * The DeleteServiceTemplateVersionOutput model constructor.
     * @property {module:model/DeleteServiceTemplateVersionOutput}
     */
    DeleteServiceTemplateVersionOutput,

    /**
     * The DeleteServiceTemplateVersionOutputServiceTemplateVersion model constructor.
     * @property {module:model/DeleteServiceTemplateVersionOutputServiceTemplateVersion}
     */
    DeleteServiceTemplateVersionOutputServiceTemplateVersion,

    /**
     * The DeleteTemplateSyncConfigInput model constructor.
     * @property {module:model/DeleteTemplateSyncConfigInput}
     */
    DeleteTemplateSyncConfigInput,

    /**
     * The DeleteTemplateSyncConfigOutput model constructor.
     * @property {module:model/DeleteTemplateSyncConfigOutput}
     */
    DeleteTemplateSyncConfigOutput,

    /**
     * The Deployment model constructor.
     * @property {module:model/Deployment}
     */
    Deployment,

    /**
     * The DeploymentInitialState model constructor.
     * @property {module:model/DeploymentInitialState}
     */
    DeploymentInitialState,

    /**
     * The DeploymentState model constructor.
     * @property {module:model/DeploymentState}
     */
    DeploymentState,

    /**
     * The DeploymentStateComponent model constructor.
     * @property {module:model/DeploymentStateComponent}
     */
    DeploymentStateComponent,

    /**
     * The DeploymentStateEnvironment model constructor.
     * @property {module:model/DeploymentStateEnvironment}
     */
    DeploymentStateEnvironment,

    /**
     * The DeploymentStateServiceInstance model constructor.
     * @property {module:model/DeploymentStateServiceInstance}
     */
    DeploymentStateServiceInstance,

    /**
     * The DeploymentStateServicePipeline model constructor.
     * @property {module:model/DeploymentStateServicePipeline}
     */
    DeploymentStateServicePipeline,

    /**
     * The DeploymentStatus model constructor.
     * @property {module:model/DeploymentStatus}
     */
    DeploymentStatus,

    /**
     * The DeploymentSummary model constructor.
     * @property {module:model/DeploymentSummary}
     */
    DeploymentSummary,

    /**
     * The DeploymentTargetResourceType model constructor.
     * @property {module:model/DeploymentTargetResourceType}
     */
    DeploymentTargetResourceType,

    /**
     * The DeploymentTargetState model constructor.
     * @property {module:model/DeploymentTargetState}
     */
    DeploymentTargetState,

    /**
     * The DeploymentUpdateType model constructor.
     * @property {module:model/DeploymentUpdateType}
     */
    DeploymentUpdateType,

    /**
     * The Environment model constructor.
     * @property {module:model/Environment}
     */
    Environment,

    /**
     * The EnvironmentAccountConnection model constructor.
     * @property {module:model/EnvironmentAccountConnection}
     */
    EnvironmentAccountConnection,

    /**
     * The EnvironmentAccountConnectionRequesterAccountType model constructor.
     * @property {module:model/EnvironmentAccountConnectionRequesterAccountType}
     */
    EnvironmentAccountConnectionRequesterAccountType,

    /**
     * The EnvironmentAccountConnectionStatus model constructor.
     * @property {module:model/EnvironmentAccountConnectionStatus}
     */
    EnvironmentAccountConnectionStatus,

    /**
     * The EnvironmentAccountConnectionSummary model constructor.
     * @property {module:model/EnvironmentAccountConnectionSummary}
     */
    EnvironmentAccountConnectionSummary,

    /**
     * The EnvironmentProvisioningRepository model constructor.
     * @property {module:model/EnvironmentProvisioningRepository}
     */
    EnvironmentProvisioningRepository,

    /**
     * The EnvironmentState model constructor.
     * @property {module:model/EnvironmentState}
     */
    EnvironmentState,

    /**
     * The EnvironmentSummary model constructor.
     * @property {module:model/EnvironmentSummary}
     */
    EnvironmentSummary,

    /**
     * The EnvironmentTemplate model constructor.
     * @property {module:model/EnvironmentTemplate}
     */
    EnvironmentTemplate,

    /**
     * The EnvironmentTemplateFilter model constructor.
     * @property {module:model/EnvironmentTemplateFilter}
     */
    EnvironmentTemplateFilter,

    /**
     * The EnvironmentTemplateSummary model constructor.
     * @property {module:model/EnvironmentTemplateSummary}
     */
    EnvironmentTemplateSummary,

    /**
     * The EnvironmentTemplateVersion model constructor.
     * @property {module:model/EnvironmentTemplateVersion}
     */
    EnvironmentTemplateVersion,

    /**
     * The EnvironmentTemplateVersionSummary model constructor.
     * @property {module:model/EnvironmentTemplateVersionSummary}
     */
    EnvironmentTemplateVersionSummary,

    /**
     * The GetAccountSettingsOutput model constructor.
     * @property {module:model/GetAccountSettingsOutput}
     */
    GetAccountSettingsOutput,

    /**
     * The GetAccountSettingsOutputAccountSettings model constructor.
     * @property {module:model/GetAccountSettingsOutputAccountSettings}
     */
    GetAccountSettingsOutputAccountSettings,

    /**
     * The GetComponentInput model constructor.
     * @property {module:model/GetComponentInput}
     */
    GetComponentInput,

    /**
     * The GetComponentOutput model constructor.
     * @property {module:model/GetComponentOutput}
     */
    GetComponentOutput,

    /**
     * The GetComponentOutputComponent model constructor.
     * @property {module:model/GetComponentOutputComponent}
     */
    GetComponentOutputComponent,

    /**
     * The GetDeploymentInput model constructor.
     * @property {module:model/GetDeploymentInput}
     */
    GetDeploymentInput,

    /**
     * The GetDeploymentOutput model constructor.
     * @property {module:model/GetDeploymentOutput}
     */
    GetDeploymentOutput,

    /**
     * The GetDeploymentOutputDeployment model constructor.
     * @property {module:model/GetDeploymentOutputDeployment}
     */
    GetDeploymentOutputDeployment,

    /**
     * The GetEnvironmentAccountConnectionInput model constructor.
     * @property {module:model/GetEnvironmentAccountConnectionInput}
     */
    GetEnvironmentAccountConnectionInput,

    /**
     * The GetEnvironmentAccountConnectionOutput model constructor.
     * @property {module:model/GetEnvironmentAccountConnectionOutput}
     */
    GetEnvironmentAccountConnectionOutput,

    /**
     * The GetEnvironmentAccountConnectionOutputEnvironmentAccountConnection model constructor.
     * @property {module:model/GetEnvironmentAccountConnectionOutputEnvironmentAccountConnection}
     */
    GetEnvironmentAccountConnectionOutputEnvironmentAccountConnection,

    /**
     * The GetEnvironmentInput model constructor.
     * @property {module:model/GetEnvironmentInput}
     */
    GetEnvironmentInput,

    /**
     * The GetEnvironmentOutput model constructor.
     * @property {module:model/GetEnvironmentOutput}
     */
    GetEnvironmentOutput,

    /**
     * The GetEnvironmentOutputEnvironment model constructor.
     * @property {module:model/GetEnvironmentOutputEnvironment}
     */
    GetEnvironmentOutputEnvironment,

    /**
     * The GetEnvironmentTemplateInput model constructor.
     * @property {module:model/GetEnvironmentTemplateInput}
     */
    GetEnvironmentTemplateInput,

    /**
     * The GetEnvironmentTemplateOutput model constructor.
     * @property {module:model/GetEnvironmentTemplateOutput}
     */
    GetEnvironmentTemplateOutput,

    /**
     * The GetEnvironmentTemplateOutputEnvironmentTemplate model constructor.
     * @property {module:model/GetEnvironmentTemplateOutputEnvironmentTemplate}
     */
    GetEnvironmentTemplateOutputEnvironmentTemplate,

    /**
     * The GetEnvironmentTemplateVersionInput model constructor.
     * @property {module:model/GetEnvironmentTemplateVersionInput}
     */
    GetEnvironmentTemplateVersionInput,

    /**
     * The GetEnvironmentTemplateVersionOutput model constructor.
     * @property {module:model/GetEnvironmentTemplateVersionOutput}
     */
    GetEnvironmentTemplateVersionOutput,

    /**
     * The GetEnvironmentTemplateVersionOutputEnvironmentTemplateVersion model constructor.
     * @property {module:model/GetEnvironmentTemplateVersionOutputEnvironmentTemplateVersion}
     */
    GetEnvironmentTemplateVersionOutputEnvironmentTemplateVersion,

    /**
     * The GetRepositoryInput model constructor.
     * @property {module:model/GetRepositoryInput}
     */
    GetRepositoryInput,

    /**
     * The GetRepositoryOutput model constructor.
     * @property {module:model/GetRepositoryOutput}
     */
    GetRepositoryOutput,

    /**
     * The GetRepositorySyncStatusInput model constructor.
     * @property {module:model/GetRepositorySyncStatusInput}
     */
    GetRepositorySyncStatusInput,

    /**
     * The GetRepositorySyncStatusOutput model constructor.
     * @property {module:model/GetRepositorySyncStatusOutput}
     */
    GetRepositorySyncStatusOutput,

    /**
     * The GetRepositorySyncStatusOutputLatestSync model constructor.
     * @property {module:model/GetRepositorySyncStatusOutputLatestSync}
     */
    GetRepositorySyncStatusOutputLatestSync,

    /**
     * The GetResourcesSummaryOutput model constructor.
     * @property {module:model/GetResourcesSummaryOutput}
     */
    GetResourcesSummaryOutput,

    /**
     * The GetResourcesSummaryOutputCounts model constructor.
     * @property {module:model/GetResourcesSummaryOutputCounts}
     */
    GetResourcesSummaryOutputCounts,

    /**
     * The GetServiceInput model constructor.
     * @property {module:model/GetServiceInput}
     */
    GetServiceInput,

    /**
     * The GetServiceInstanceInput model constructor.
     * @property {module:model/GetServiceInstanceInput}
     */
    GetServiceInstanceInput,

    /**
     * The GetServiceInstanceOutput model constructor.
     * @property {module:model/GetServiceInstanceOutput}
     */
    GetServiceInstanceOutput,

    /**
     * The GetServiceInstanceOutputServiceInstance model constructor.
     * @property {module:model/GetServiceInstanceOutputServiceInstance}
     */
    GetServiceInstanceOutputServiceInstance,

    /**
     * The GetServiceInstanceSyncStatusInput model constructor.
     * @property {module:model/GetServiceInstanceSyncStatusInput}
     */
    GetServiceInstanceSyncStatusInput,

    /**
     * The GetServiceInstanceSyncStatusOutput model constructor.
     * @property {module:model/GetServiceInstanceSyncStatusOutput}
     */
    GetServiceInstanceSyncStatusOutput,

    /**
     * The GetServiceInstanceSyncStatusOutputDesiredState model constructor.
     * @property {module:model/GetServiceInstanceSyncStatusOutputDesiredState}
     */
    GetServiceInstanceSyncStatusOutputDesiredState,

    /**
     * The GetServiceInstanceSyncStatusOutputLatestSuccessfulSync model constructor.
     * @property {module:model/GetServiceInstanceSyncStatusOutputLatestSuccessfulSync}
     */
    GetServiceInstanceSyncStatusOutputLatestSuccessfulSync,

    /**
     * The GetServiceInstanceSyncStatusOutputLatestSync model constructor.
     * @property {module:model/GetServiceInstanceSyncStatusOutputLatestSync}
     */
    GetServiceInstanceSyncStatusOutputLatestSync,

    /**
     * The GetServiceOutput model constructor.
     * @property {module:model/GetServiceOutput}
     */
    GetServiceOutput,

    /**
     * The GetServiceOutputService model constructor.
     * @property {module:model/GetServiceOutputService}
     */
    GetServiceOutputService,

    /**
     * The GetServiceSyncBlockerSummaryInput model constructor.
     * @property {module:model/GetServiceSyncBlockerSummaryInput}
     */
    GetServiceSyncBlockerSummaryInput,

    /**
     * The GetServiceSyncBlockerSummaryOutput model constructor.
     * @property {module:model/GetServiceSyncBlockerSummaryOutput}
     */
    GetServiceSyncBlockerSummaryOutput,

    /**
     * The GetServiceSyncBlockerSummaryOutputServiceSyncBlockerSummary model constructor.
     * @property {module:model/GetServiceSyncBlockerSummaryOutputServiceSyncBlockerSummary}
     */
    GetServiceSyncBlockerSummaryOutputServiceSyncBlockerSummary,

    /**
     * The GetServiceSyncConfigInput model constructor.
     * @property {module:model/GetServiceSyncConfigInput}
     */
    GetServiceSyncConfigInput,

    /**
     * The GetServiceSyncConfigOutput model constructor.
     * @property {module:model/GetServiceSyncConfigOutput}
     */
    GetServiceSyncConfigOutput,

    /**
     * The GetServiceSyncConfigOutputServiceSyncConfig model constructor.
     * @property {module:model/GetServiceSyncConfigOutputServiceSyncConfig}
     */
    GetServiceSyncConfigOutputServiceSyncConfig,

    /**
     * The GetServiceTemplateInput model constructor.
     * @property {module:model/GetServiceTemplateInput}
     */
    GetServiceTemplateInput,

    /**
     * The GetServiceTemplateOutput model constructor.
     * @property {module:model/GetServiceTemplateOutput}
     */
    GetServiceTemplateOutput,

    /**
     * The GetServiceTemplateOutputServiceTemplate model constructor.
     * @property {module:model/GetServiceTemplateOutputServiceTemplate}
     */
    GetServiceTemplateOutputServiceTemplate,

    /**
     * The GetServiceTemplateVersionInput model constructor.
     * @property {module:model/GetServiceTemplateVersionInput}
     */
    GetServiceTemplateVersionInput,

    /**
     * The GetServiceTemplateVersionOutput model constructor.
     * @property {module:model/GetServiceTemplateVersionOutput}
     */
    GetServiceTemplateVersionOutput,

    /**
     * The GetServiceTemplateVersionOutputServiceTemplateVersion model constructor.
     * @property {module:model/GetServiceTemplateVersionOutputServiceTemplateVersion}
     */
    GetServiceTemplateVersionOutputServiceTemplateVersion,

    /**
     * The GetTemplateSyncConfigInput model constructor.
     * @property {module:model/GetTemplateSyncConfigInput}
     */
    GetTemplateSyncConfigInput,

    /**
     * The GetTemplateSyncConfigOutput model constructor.
     * @property {module:model/GetTemplateSyncConfigOutput}
     */
    GetTemplateSyncConfigOutput,

    /**
     * The GetTemplateSyncStatusInput model constructor.
     * @property {module:model/GetTemplateSyncStatusInput}
     */
    GetTemplateSyncStatusInput,

    /**
     * The GetTemplateSyncStatusOutput model constructor.
     * @property {module:model/GetTemplateSyncStatusOutput}
     */
    GetTemplateSyncStatusOutput,

    /**
     * The GetTemplateSyncStatusOutputDesiredState model constructor.
     * @property {module:model/GetTemplateSyncStatusOutputDesiredState}
     */
    GetTemplateSyncStatusOutputDesiredState,

    /**
     * The GetTemplateSyncStatusOutputLatestSuccessfulSync model constructor.
     * @property {module:model/GetTemplateSyncStatusOutputLatestSuccessfulSync}
     */
    GetTemplateSyncStatusOutputLatestSuccessfulSync,

    /**
     * The GetTemplateSyncStatusOutputLatestSync model constructor.
     * @property {module:model/GetTemplateSyncStatusOutputLatestSync}
     */
    GetTemplateSyncStatusOutputLatestSync,

    /**
     * The ListComponentOutputsInput model constructor.
     * @property {module:model/ListComponentOutputsInput}
     */
    ListComponentOutputsInput,

    /**
     * The ListComponentOutputsOutput model constructor.
     * @property {module:model/ListComponentOutputsOutput}
     */
    ListComponentOutputsOutput,

    /**
     * The ListComponentProvisionedResourcesInput model constructor.
     * @property {module:model/ListComponentProvisionedResourcesInput}
     */
    ListComponentProvisionedResourcesInput,

    /**
     * The ListComponentProvisionedResourcesOutput model constructor.
     * @property {module:model/ListComponentProvisionedResourcesOutput}
     */
    ListComponentProvisionedResourcesOutput,

    /**
     * The ListComponentsInput model constructor.
     * @property {module:model/ListComponentsInput}
     */
    ListComponentsInput,

    /**
     * The ListComponentsOutput model constructor.
     * @property {module:model/ListComponentsOutput}
     */
    ListComponentsOutput,

    /**
     * The ListDeploymentsInput model constructor.
     * @property {module:model/ListDeploymentsInput}
     */
    ListDeploymentsInput,

    /**
     * The ListDeploymentsOutput model constructor.
     * @property {module:model/ListDeploymentsOutput}
     */
    ListDeploymentsOutput,

    /**
     * The ListEnvironmentAccountConnectionsInput model constructor.
     * @property {module:model/ListEnvironmentAccountConnectionsInput}
     */
    ListEnvironmentAccountConnectionsInput,

    /**
     * The ListEnvironmentAccountConnectionsOutput model constructor.
     * @property {module:model/ListEnvironmentAccountConnectionsOutput}
     */
    ListEnvironmentAccountConnectionsOutput,

    /**
     * The ListEnvironmentOutputsInput model constructor.
     * @property {module:model/ListEnvironmentOutputsInput}
     */
    ListEnvironmentOutputsInput,

    /**
     * The ListEnvironmentOutputsOutput model constructor.
     * @property {module:model/ListEnvironmentOutputsOutput}
     */
    ListEnvironmentOutputsOutput,

    /**
     * The ListEnvironmentProvisionedResourcesInput model constructor.
     * @property {module:model/ListEnvironmentProvisionedResourcesInput}
     */
    ListEnvironmentProvisionedResourcesInput,

    /**
     * The ListEnvironmentProvisionedResourcesOutput model constructor.
     * @property {module:model/ListEnvironmentProvisionedResourcesOutput}
     */
    ListEnvironmentProvisionedResourcesOutput,

    /**
     * The ListEnvironmentTemplateVersionsInput model constructor.
     * @property {module:model/ListEnvironmentTemplateVersionsInput}
     */
    ListEnvironmentTemplateVersionsInput,

    /**
     * The ListEnvironmentTemplateVersionsOutput model constructor.
     * @property {module:model/ListEnvironmentTemplateVersionsOutput}
     */
    ListEnvironmentTemplateVersionsOutput,

    /**
     * The ListEnvironmentTemplatesInput model constructor.
     * @property {module:model/ListEnvironmentTemplatesInput}
     */
    ListEnvironmentTemplatesInput,

    /**
     * The ListEnvironmentTemplatesOutput model constructor.
     * @property {module:model/ListEnvironmentTemplatesOutput}
     */
    ListEnvironmentTemplatesOutput,

    /**
     * The ListEnvironmentsInput model constructor.
     * @property {module:model/ListEnvironmentsInput}
     */
    ListEnvironmentsInput,

    /**
     * The ListEnvironmentsOutput model constructor.
     * @property {module:model/ListEnvironmentsOutput}
     */
    ListEnvironmentsOutput,

    /**
     * The ListRepositoriesInput model constructor.
     * @property {module:model/ListRepositoriesInput}
     */
    ListRepositoriesInput,

    /**
     * The ListRepositoriesOutput model constructor.
     * @property {module:model/ListRepositoriesOutput}
     */
    ListRepositoriesOutput,

    /**
     * The ListRepositorySyncDefinitionsInput model constructor.
     * @property {module:model/ListRepositorySyncDefinitionsInput}
     */
    ListRepositorySyncDefinitionsInput,

    /**
     * The ListRepositorySyncDefinitionsOutput model constructor.
     * @property {module:model/ListRepositorySyncDefinitionsOutput}
     */
    ListRepositorySyncDefinitionsOutput,

    /**
     * The ListServiceInstanceOutputsInput model constructor.
     * @property {module:model/ListServiceInstanceOutputsInput}
     */
    ListServiceInstanceOutputsInput,

    /**
     * The ListServiceInstanceOutputsOutput model constructor.
     * @property {module:model/ListServiceInstanceOutputsOutput}
     */
    ListServiceInstanceOutputsOutput,

    /**
     * The ListServiceInstanceProvisionedResourcesInput model constructor.
     * @property {module:model/ListServiceInstanceProvisionedResourcesInput}
     */
    ListServiceInstanceProvisionedResourcesInput,

    /**
     * The ListServiceInstanceProvisionedResourcesOutput model constructor.
     * @property {module:model/ListServiceInstanceProvisionedResourcesOutput}
     */
    ListServiceInstanceProvisionedResourcesOutput,

    /**
     * The ListServiceInstancesFilter model constructor.
     * @property {module:model/ListServiceInstancesFilter}
     */
    ListServiceInstancesFilter,

    /**
     * The ListServiceInstancesFilterBy model constructor.
     * @property {module:model/ListServiceInstancesFilterBy}
     */
    ListServiceInstancesFilterBy,

    /**
     * The ListServiceInstancesInput model constructor.
     * @property {module:model/ListServiceInstancesInput}
     */
    ListServiceInstancesInput,

    /**
     * The ListServiceInstancesOutput model constructor.
     * @property {module:model/ListServiceInstancesOutput}
     */
    ListServiceInstancesOutput,

    /**
     * The ListServiceInstancesSortBy model constructor.
     * @property {module:model/ListServiceInstancesSortBy}
     */
    ListServiceInstancesSortBy,

    /**
     * The ListServicePipelineOutputsInput model constructor.
     * @property {module:model/ListServicePipelineOutputsInput}
     */
    ListServicePipelineOutputsInput,

    /**
     * The ListServicePipelineOutputsOutput model constructor.
     * @property {module:model/ListServicePipelineOutputsOutput}
     */
    ListServicePipelineOutputsOutput,

    /**
     * The ListServicePipelineProvisionedResourcesInput model constructor.
     * @property {module:model/ListServicePipelineProvisionedResourcesInput}
     */
    ListServicePipelineProvisionedResourcesInput,

    /**
     * The ListServicePipelineProvisionedResourcesOutput model constructor.
     * @property {module:model/ListServicePipelineProvisionedResourcesOutput}
     */
    ListServicePipelineProvisionedResourcesOutput,

    /**
     * The ListServiceTemplateVersionsInput model constructor.
     * @property {module:model/ListServiceTemplateVersionsInput}
     */
    ListServiceTemplateVersionsInput,

    /**
     * The ListServiceTemplateVersionsOutput model constructor.
     * @property {module:model/ListServiceTemplateVersionsOutput}
     */
    ListServiceTemplateVersionsOutput,

    /**
     * The ListServiceTemplatesInput model constructor.
     * @property {module:model/ListServiceTemplatesInput}
     */
    ListServiceTemplatesInput,

    /**
     * The ListServiceTemplatesOutput model constructor.
     * @property {module:model/ListServiceTemplatesOutput}
     */
    ListServiceTemplatesOutput,

    /**
     * The ListServicesInput model constructor.
     * @property {module:model/ListServicesInput}
     */
    ListServicesInput,

    /**
     * The ListServicesOutput model constructor.
     * @property {module:model/ListServicesOutput}
     */
    ListServicesOutput,

    /**
     * The ListTagsForResourceInput model constructor.
     * @property {module:model/ListTagsForResourceInput}
     */
    ListTagsForResourceInput,

    /**
     * The ListTagsForResourceOutput model constructor.
     * @property {module:model/ListTagsForResourceOutput}
     */
    ListTagsForResourceOutput,

    /**
     * The NotifyResourceDeploymentStatusChangeInput model constructor.
     * @property {module:model/NotifyResourceDeploymentStatusChangeInput}
     */
    NotifyResourceDeploymentStatusChangeInput,

    /**
     * The Output model constructor.
     * @property {module:model/Output}
     */
    Output,

    /**
     * The ProvisionedResource model constructor.
     * @property {module:model/ProvisionedResource}
     */
    ProvisionedResource,

    /**
     * The ProvisionedResourceEngine model constructor.
     * @property {module:model/ProvisionedResourceEngine}
     */
    ProvisionedResourceEngine,

    /**
     * The Provisioning model constructor.
     * @property {module:model/Provisioning}
     */
    Provisioning,

    /**
     * The RejectEnvironmentAccountConnectionInput model constructor.
     * @property {module:model/RejectEnvironmentAccountConnectionInput}
     */
    RejectEnvironmentAccountConnectionInput,

    /**
     * The RejectEnvironmentAccountConnectionOutput model constructor.
     * @property {module:model/RejectEnvironmentAccountConnectionOutput}
     */
    RejectEnvironmentAccountConnectionOutput,

    /**
     * The RejectEnvironmentAccountConnectionOutputEnvironmentAccountConnection model constructor.
     * @property {module:model/RejectEnvironmentAccountConnectionOutputEnvironmentAccountConnection}
     */
    RejectEnvironmentAccountConnectionOutputEnvironmentAccountConnection,

    /**
     * The Repository model constructor.
     * @property {module:model/Repository}
     */
    Repository,

    /**
     * The RepositoryBranch model constructor.
     * @property {module:model/RepositoryBranch}
     */
    RepositoryBranch,

    /**
     * The RepositoryBranchInput model constructor.
     * @property {module:model/RepositoryBranchInput}
     */
    RepositoryBranchInput,

    /**
     * The RepositoryProvider model constructor.
     * @property {module:model/RepositoryProvider}
     */
    RepositoryProvider,

    /**
     * The RepositorySummary model constructor.
     * @property {module:model/RepositorySummary}
     */
    RepositorySummary,

    /**
     * The RepositorySyncAttempt model constructor.
     * @property {module:model/RepositorySyncAttempt}
     */
    RepositorySyncAttempt,

    /**
     * The RepositorySyncDefinition model constructor.
     * @property {module:model/RepositorySyncDefinition}
     */
    RepositorySyncDefinition,

    /**
     * The RepositorySyncEvent model constructor.
     * @property {module:model/RepositorySyncEvent}
     */
    RepositorySyncEvent,

    /**
     * The RepositorySyncStatus model constructor.
     * @property {module:model/RepositorySyncStatus}
     */
    RepositorySyncStatus,

    /**
     * The ResourceCountsSummary model constructor.
     * @property {module:model/ResourceCountsSummary}
     */
    ResourceCountsSummary,

    /**
     * The ResourceDeploymentStatus model constructor.
     * @property {module:model/ResourceDeploymentStatus}
     */
    ResourceDeploymentStatus,

    /**
     * The ResourceSyncAttempt model constructor.
     * @property {module:model/ResourceSyncAttempt}
     */
    ResourceSyncAttempt,

    /**
     * The ResourceSyncAttemptInitialRevision model constructor.
     * @property {module:model/ResourceSyncAttemptInitialRevision}
     */
    ResourceSyncAttemptInitialRevision,

    /**
     * The ResourceSyncAttemptTargetRevision model constructor.
     * @property {module:model/ResourceSyncAttemptTargetRevision}
     */
    ResourceSyncAttemptTargetRevision,

    /**
     * The ResourceSyncEvent model constructor.
     * @property {module:model/ResourceSyncEvent}
     */
    ResourceSyncEvent,

    /**
     * The ResourceSyncStatus model constructor.
     * @property {module:model/ResourceSyncStatus}
     */
    ResourceSyncStatus,

    /**
     * The Revision model constructor.
     * @property {module:model/Revision}
     */
    Revision,

    /**
     * The S3ObjectSource model constructor.
     * @property {module:model/S3ObjectSource}
     */
    S3ObjectSource,

    /**
     * The Service model constructor.
     * @property {module:model/Service}
     */
    Service,

    /**
     * The ServiceInstance model constructor.
     * @property {module:model/ServiceInstance}
     */
    ServiceInstance,

    /**
     * The ServiceInstanceState model constructor.
     * @property {module:model/ServiceInstanceState}
     */
    ServiceInstanceState,

    /**
     * The ServiceInstanceSummary model constructor.
     * @property {module:model/ServiceInstanceSummary}
     */
    ServiceInstanceSummary,

    /**
     * The ServicePipeline model constructor.
     * @property {module:model/ServicePipeline}
     */
    ServicePipeline,

    /**
     * The ServicePipelineState model constructor.
     * @property {module:model/ServicePipelineState}
     */
    ServicePipelineState,

    /**
     * The ServiceStatus model constructor.
     * @property {module:model/ServiceStatus}
     */
    ServiceStatus,

    /**
     * The ServiceSummary model constructor.
     * @property {module:model/ServiceSummary}
     */
    ServiceSummary,

    /**
     * The ServiceSyncBlockerSummary model constructor.
     * @property {module:model/ServiceSyncBlockerSummary}
     */
    ServiceSyncBlockerSummary,

    /**
     * The ServiceSyncConfig model constructor.
     * @property {module:model/ServiceSyncConfig}
     */
    ServiceSyncConfig,

    /**
     * The ServiceTemplate model constructor.
     * @property {module:model/ServiceTemplate}
     */
    ServiceTemplate,

    /**
     * The ServiceTemplateSummary model constructor.
     * @property {module:model/ServiceTemplateSummary}
     */
    ServiceTemplateSummary,

    /**
     * The ServiceTemplateSupportedComponentSourceType model constructor.
     * @property {module:model/ServiceTemplateSupportedComponentSourceType}
     */
    ServiceTemplateSupportedComponentSourceType,

    /**
     * The ServiceTemplateVersion model constructor.
     * @property {module:model/ServiceTemplateVersion}
     */
    ServiceTemplateVersion,

    /**
     * The ServiceTemplateVersionSummary model constructor.
     * @property {module:model/ServiceTemplateVersionSummary}
     */
    ServiceTemplateVersionSummary,

    /**
     * The SortOrder model constructor.
     * @property {module:model/SortOrder}
     */
    SortOrder,

    /**
     * The SyncBlocker model constructor.
     * @property {module:model/SyncBlocker}
     */
    SyncBlocker,

    /**
     * The SyncBlockerContext model constructor.
     * @property {module:model/SyncBlockerContext}
     */
    SyncBlockerContext,

    /**
     * The SyncType model constructor.
     * @property {module:model/SyncType}
     */
    SyncType,

    /**
     * The Tag model constructor.
     * @property {module:model/Tag}
     */
    Tag,

    /**
     * The TagResourceInput model constructor.
     * @property {module:model/TagResourceInput}
     */
    TagResourceInput,

    /**
     * The TemplateSyncConfig model constructor.
     * @property {module:model/TemplateSyncConfig}
     */
    TemplateSyncConfig,

    /**
     * The TemplateType model constructor.
     * @property {module:model/TemplateType}
     */
    TemplateType,

    /**
     * The TemplateVersionSourceInput model constructor.
     * @property {module:model/TemplateVersionSourceInput}
     */
    TemplateVersionSourceInput,

    /**
     * The TemplateVersionSourceInputS3 model constructor.
     * @property {module:model/TemplateVersionSourceInputS3}
     */
    TemplateVersionSourceInputS3,

    /**
     * The TemplateVersionStatus model constructor.
     * @property {module:model/TemplateVersionStatus}
     */
    TemplateVersionStatus,

    /**
     * The UntagResourceInput model constructor.
     * @property {module:model/UntagResourceInput}
     */
    UntagResourceInput,

    /**
     * The UpdateAccountSettingsInput model constructor.
     * @property {module:model/UpdateAccountSettingsInput}
     */
    UpdateAccountSettingsInput,

    /**
     * The UpdateAccountSettingsInputPipelineProvisioningRepository model constructor.
     * @property {module:model/UpdateAccountSettingsInputPipelineProvisioningRepository}
     */
    UpdateAccountSettingsInputPipelineProvisioningRepository,

    /**
     * The UpdateAccountSettingsOutput model constructor.
     * @property {module:model/UpdateAccountSettingsOutput}
     */
    UpdateAccountSettingsOutput,

    /**
     * The UpdateAccountSettingsOutputAccountSettings model constructor.
     * @property {module:model/UpdateAccountSettingsOutputAccountSettings}
     */
    UpdateAccountSettingsOutputAccountSettings,

    /**
     * The UpdateComponentInput model constructor.
     * @property {module:model/UpdateComponentInput}
     */
    UpdateComponentInput,

    /**
     * The UpdateComponentOutput model constructor.
     * @property {module:model/UpdateComponentOutput}
     */
    UpdateComponentOutput,

    /**
     * The UpdateComponentOutputComponent model constructor.
     * @property {module:model/UpdateComponentOutputComponent}
     */
    UpdateComponentOutputComponent,

    /**
     * The UpdateEnvironmentAccountConnectionInput model constructor.
     * @property {module:model/UpdateEnvironmentAccountConnectionInput}
     */
    UpdateEnvironmentAccountConnectionInput,

    /**
     * The UpdateEnvironmentAccountConnectionOutput model constructor.
     * @property {module:model/UpdateEnvironmentAccountConnectionOutput}
     */
    UpdateEnvironmentAccountConnectionOutput,

    /**
     * The UpdateEnvironmentInput model constructor.
     * @property {module:model/UpdateEnvironmentInput}
     */
    UpdateEnvironmentInput,

    /**
     * The UpdateEnvironmentInputProvisioningRepository model constructor.
     * @property {module:model/UpdateEnvironmentInputProvisioningRepository}
     */
    UpdateEnvironmentInputProvisioningRepository,

    /**
     * The UpdateEnvironmentOutput model constructor.
     * @property {module:model/UpdateEnvironmentOutput}
     */
    UpdateEnvironmentOutput,

    /**
     * The UpdateEnvironmentTemplateInput model constructor.
     * @property {module:model/UpdateEnvironmentTemplateInput}
     */
    UpdateEnvironmentTemplateInput,

    /**
     * The UpdateEnvironmentTemplateOutput model constructor.
     * @property {module:model/UpdateEnvironmentTemplateOutput}
     */
    UpdateEnvironmentTemplateOutput,

    /**
     * The UpdateEnvironmentTemplateVersionInput model constructor.
     * @property {module:model/UpdateEnvironmentTemplateVersionInput}
     */
    UpdateEnvironmentTemplateVersionInput,

    /**
     * The UpdateEnvironmentTemplateVersionOutput model constructor.
     * @property {module:model/UpdateEnvironmentTemplateVersionOutput}
     */
    UpdateEnvironmentTemplateVersionOutput,

    /**
     * The UpdateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion model constructor.
     * @property {module:model/UpdateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion}
     */
    UpdateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion,

    /**
     * The UpdateServiceInput model constructor.
     * @property {module:model/UpdateServiceInput}
     */
    UpdateServiceInput,

    /**
     * The UpdateServiceInstanceInput model constructor.
     * @property {module:model/UpdateServiceInstanceInput}
     */
    UpdateServiceInstanceInput,

    /**
     * The UpdateServiceInstanceOutput model constructor.
     * @property {module:model/UpdateServiceInstanceOutput}
     */
    UpdateServiceInstanceOutput,

    /**
     * The UpdateServiceOutput model constructor.
     * @property {module:model/UpdateServiceOutput}
     */
    UpdateServiceOutput,

    /**
     * The UpdateServicePipelineInput model constructor.
     * @property {module:model/UpdateServicePipelineInput}
     */
    UpdateServicePipelineInput,

    /**
     * The UpdateServicePipelineOutput model constructor.
     * @property {module:model/UpdateServicePipelineOutput}
     */
    UpdateServicePipelineOutput,

    /**
     * The UpdateServicePipelineOutputPipeline model constructor.
     * @property {module:model/UpdateServicePipelineOutputPipeline}
     */
    UpdateServicePipelineOutputPipeline,

    /**
     * The UpdateServiceSyncBlockerInput model constructor.
     * @property {module:model/UpdateServiceSyncBlockerInput}
     */
    UpdateServiceSyncBlockerInput,

    /**
     * The UpdateServiceSyncBlockerOutput model constructor.
     * @property {module:model/UpdateServiceSyncBlockerOutput}
     */
    UpdateServiceSyncBlockerOutput,

    /**
     * The UpdateServiceSyncBlockerOutputServiceSyncBlocker model constructor.
     * @property {module:model/UpdateServiceSyncBlockerOutputServiceSyncBlocker}
     */
    UpdateServiceSyncBlockerOutputServiceSyncBlocker,

    /**
     * The UpdateServiceSyncConfigInput model constructor.
     * @property {module:model/UpdateServiceSyncConfigInput}
     */
    UpdateServiceSyncConfigInput,

    /**
     * The UpdateServiceSyncConfigOutput model constructor.
     * @property {module:model/UpdateServiceSyncConfigOutput}
     */
    UpdateServiceSyncConfigOutput,

    /**
     * The UpdateServiceTemplateInput model constructor.
     * @property {module:model/UpdateServiceTemplateInput}
     */
    UpdateServiceTemplateInput,

    /**
     * The UpdateServiceTemplateOutput model constructor.
     * @property {module:model/UpdateServiceTemplateOutput}
     */
    UpdateServiceTemplateOutput,

    /**
     * The UpdateServiceTemplateVersionInput model constructor.
     * @property {module:model/UpdateServiceTemplateVersionInput}
     */
    UpdateServiceTemplateVersionInput,

    /**
     * The UpdateServiceTemplateVersionOutput model constructor.
     * @property {module:model/UpdateServiceTemplateVersionOutput}
     */
    UpdateServiceTemplateVersionOutput,

    /**
     * The UpdateServiceTemplateVersionOutputServiceTemplateVersion model constructor.
     * @property {module:model/UpdateServiceTemplateVersionOutputServiceTemplateVersion}
     */
    UpdateServiceTemplateVersionOutputServiceTemplateVersion,

    /**
     * The UpdateTemplateSyncConfigInput model constructor.
     * @property {module:model/UpdateTemplateSyncConfigInput}
     */
    UpdateTemplateSyncConfigInput,

    /**
     * The UpdateTemplateSyncConfigOutput model constructor.
     * @property {module:model/UpdateTemplateSyncConfigOutput}
     */
    UpdateTemplateSyncConfigOutput,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
