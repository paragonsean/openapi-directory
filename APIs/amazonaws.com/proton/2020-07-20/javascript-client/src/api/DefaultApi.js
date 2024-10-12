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


import ApiClient from "../ApiClient";
import AcceptEnvironmentAccountConnectionInput from '../model/AcceptEnvironmentAccountConnectionInput';
import AcceptEnvironmentAccountConnectionOutput from '../model/AcceptEnvironmentAccountConnectionOutput';
import CancelComponentDeploymentInput from '../model/CancelComponentDeploymentInput';
import CancelComponentDeploymentOutput from '../model/CancelComponentDeploymentOutput';
import CancelEnvironmentDeploymentInput from '../model/CancelEnvironmentDeploymentInput';
import CancelEnvironmentDeploymentOutput from '../model/CancelEnvironmentDeploymentOutput';
import CancelServiceInstanceDeploymentInput from '../model/CancelServiceInstanceDeploymentInput';
import CancelServiceInstanceDeploymentOutput from '../model/CancelServiceInstanceDeploymentOutput';
import CancelServicePipelineDeploymentInput from '../model/CancelServicePipelineDeploymentInput';
import CancelServicePipelineDeploymentOutput from '../model/CancelServicePipelineDeploymentOutput';
import CreateComponentInput from '../model/CreateComponentInput';
import CreateComponentOutput from '../model/CreateComponentOutput';
import CreateEnvironmentAccountConnectionInput from '../model/CreateEnvironmentAccountConnectionInput';
import CreateEnvironmentAccountConnectionOutput from '../model/CreateEnvironmentAccountConnectionOutput';
import CreateEnvironmentInput from '../model/CreateEnvironmentInput';
import CreateEnvironmentOutput from '../model/CreateEnvironmentOutput';
import CreateEnvironmentTemplateInput from '../model/CreateEnvironmentTemplateInput';
import CreateEnvironmentTemplateOutput from '../model/CreateEnvironmentTemplateOutput';
import CreateEnvironmentTemplateVersionInput from '../model/CreateEnvironmentTemplateVersionInput';
import CreateEnvironmentTemplateVersionOutput from '../model/CreateEnvironmentTemplateVersionOutput';
import CreateRepositoryInput from '../model/CreateRepositoryInput';
import CreateRepositoryOutput from '../model/CreateRepositoryOutput';
import CreateServiceInput from '../model/CreateServiceInput';
import CreateServiceInstanceInput from '../model/CreateServiceInstanceInput';
import CreateServiceInstanceOutput from '../model/CreateServiceInstanceOutput';
import CreateServiceOutput from '../model/CreateServiceOutput';
import CreateServiceSyncConfigInput from '../model/CreateServiceSyncConfigInput';
import CreateServiceSyncConfigOutput from '../model/CreateServiceSyncConfigOutput';
import CreateServiceTemplateInput from '../model/CreateServiceTemplateInput';
import CreateServiceTemplateOutput from '../model/CreateServiceTemplateOutput';
import CreateServiceTemplateVersionInput from '../model/CreateServiceTemplateVersionInput';
import CreateServiceTemplateVersionOutput from '../model/CreateServiceTemplateVersionOutput';
import CreateTemplateSyncConfigInput from '../model/CreateTemplateSyncConfigInput';
import CreateTemplateSyncConfigOutput from '../model/CreateTemplateSyncConfigOutput';
import DeleteComponentInput from '../model/DeleteComponentInput';
import DeleteComponentOutput from '../model/DeleteComponentOutput';
import DeleteDeploymentInput from '../model/DeleteDeploymentInput';
import DeleteDeploymentOutput from '../model/DeleteDeploymentOutput';
import DeleteEnvironmentAccountConnectionInput from '../model/DeleteEnvironmentAccountConnectionInput';
import DeleteEnvironmentAccountConnectionOutput from '../model/DeleteEnvironmentAccountConnectionOutput';
import DeleteEnvironmentInput from '../model/DeleteEnvironmentInput';
import DeleteEnvironmentOutput from '../model/DeleteEnvironmentOutput';
import DeleteEnvironmentTemplateInput from '../model/DeleteEnvironmentTemplateInput';
import DeleteEnvironmentTemplateOutput from '../model/DeleteEnvironmentTemplateOutput';
import DeleteEnvironmentTemplateVersionInput from '../model/DeleteEnvironmentTemplateVersionInput';
import DeleteEnvironmentTemplateVersionOutput from '../model/DeleteEnvironmentTemplateVersionOutput';
import DeleteRepositoryInput from '../model/DeleteRepositoryInput';
import DeleteRepositoryOutput from '../model/DeleteRepositoryOutput';
import DeleteServiceInput from '../model/DeleteServiceInput';
import DeleteServiceOutput from '../model/DeleteServiceOutput';
import DeleteServiceSyncConfigInput from '../model/DeleteServiceSyncConfigInput';
import DeleteServiceSyncConfigOutput from '../model/DeleteServiceSyncConfigOutput';
import DeleteServiceTemplateInput from '../model/DeleteServiceTemplateInput';
import DeleteServiceTemplateOutput from '../model/DeleteServiceTemplateOutput';
import DeleteServiceTemplateVersionInput from '../model/DeleteServiceTemplateVersionInput';
import DeleteServiceTemplateVersionOutput from '../model/DeleteServiceTemplateVersionOutput';
import DeleteTemplateSyncConfigInput from '../model/DeleteTemplateSyncConfigInput';
import DeleteTemplateSyncConfigOutput from '../model/DeleteTemplateSyncConfigOutput';
import GetAccountSettingsOutput from '../model/GetAccountSettingsOutput';
import GetComponentInput from '../model/GetComponentInput';
import GetComponentOutput from '../model/GetComponentOutput';
import GetDeploymentInput from '../model/GetDeploymentInput';
import GetDeploymentOutput from '../model/GetDeploymentOutput';
import GetEnvironmentAccountConnectionInput from '../model/GetEnvironmentAccountConnectionInput';
import GetEnvironmentAccountConnectionOutput from '../model/GetEnvironmentAccountConnectionOutput';
import GetEnvironmentInput from '../model/GetEnvironmentInput';
import GetEnvironmentOutput from '../model/GetEnvironmentOutput';
import GetEnvironmentTemplateInput from '../model/GetEnvironmentTemplateInput';
import GetEnvironmentTemplateOutput from '../model/GetEnvironmentTemplateOutput';
import GetEnvironmentTemplateVersionInput from '../model/GetEnvironmentTemplateVersionInput';
import GetEnvironmentTemplateVersionOutput from '../model/GetEnvironmentTemplateVersionOutput';
import GetRepositoryInput from '../model/GetRepositoryInput';
import GetRepositoryOutput from '../model/GetRepositoryOutput';
import GetRepositorySyncStatusInput from '../model/GetRepositorySyncStatusInput';
import GetRepositorySyncStatusOutput from '../model/GetRepositorySyncStatusOutput';
import GetResourcesSummaryOutput from '../model/GetResourcesSummaryOutput';
import GetServiceInput from '../model/GetServiceInput';
import GetServiceInstanceInput from '../model/GetServiceInstanceInput';
import GetServiceInstanceOutput from '../model/GetServiceInstanceOutput';
import GetServiceInstanceSyncStatusInput from '../model/GetServiceInstanceSyncStatusInput';
import GetServiceInstanceSyncStatusOutput from '../model/GetServiceInstanceSyncStatusOutput';
import GetServiceOutput from '../model/GetServiceOutput';
import GetServiceSyncBlockerSummaryInput from '../model/GetServiceSyncBlockerSummaryInput';
import GetServiceSyncBlockerSummaryOutput from '../model/GetServiceSyncBlockerSummaryOutput';
import GetServiceSyncConfigInput from '../model/GetServiceSyncConfigInput';
import GetServiceSyncConfigOutput from '../model/GetServiceSyncConfigOutput';
import GetServiceTemplateInput from '../model/GetServiceTemplateInput';
import GetServiceTemplateOutput from '../model/GetServiceTemplateOutput';
import GetServiceTemplateVersionInput from '../model/GetServiceTemplateVersionInput';
import GetServiceTemplateVersionOutput from '../model/GetServiceTemplateVersionOutput';
import GetTemplateSyncConfigInput from '../model/GetTemplateSyncConfigInput';
import GetTemplateSyncConfigOutput from '../model/GetTemplateSyncConfigOutput';
import GetTemplateSyncStatusInput from '../model/GetTemplateSyncStatusInput';
import GetTemplateSyncStatusOutput from '../model/GetTemplateSyncStatusOutput';
import ListComponentOutputsInput from '../model/ListComponentOutputsInput';
import ListComponentOutputsOutput from '../model/ListComponentOutputsOutput';
import ListComponentProvisionedResourcesInput from '../model/ListComponentProvisionedResourcesInput';
import ListComponentProvisionedResourcesOutput from '../model/ListComponentProvisionedResourcesOutput';
import ListComponentsInput from '../model/ListComponentsInput';
import ListComponentsOutput from '../model/ListComponentsOutput';
import ListDeploymentsInput from '../model/ListDeploymentsInput';
import ListDeploymentsOutput from '../model/ListDeploymentsOutput';
import ListEnvironmentAccountConnectionsInput from '../model/ListEnvironmentAccountConnectionsInput';
import ListEnvironmentAccountConnectionsOutput from '../model/ListEnvironmentAccountConnectionsOutput';
import ListEnvironmentOutputsInput from '../model/ListEnvironmentOutputsInput';
import ListEnvironmentOutputsOutput from '../model/ListEnvironmentOutputsOutput';
import ListEnvironmentProvisionedResourcesInput from '../model/ListEnvironmentProvisionedResourcesInput';
import ListEnvironmentProvisionedResourcesOutput from '../model/ListEnvironmentProvisionedResourcesOutput';
import ListEnvironmentTemplateVersionsInput from '../model/ListEnvironmentTemplateVersionsInput';
import ListEnvironmentTemplateVersionsOutput from '../model/ListEnvironmentTemplateVersionsOutput';
import ListEnvironmentTemplatesInput from '../model/ListEnvironmentTemplatesInput';
import ListEnvironmentTemplatesOutput from '../model/ListEnvironmentTemplatesOutput';
import ListEnvironmentsInput from '../model/ListEnvironmentsInput';
import ListEnvironmentsOutput from '../model/ListEnvironmentsOutput';
import ListRepositoriesInput from '../model/ListRepositoriesInput';
import ListRepositoriesOutput from '../model/ListRepositoriesOutput';
import ListRepositorySyncDefinitionsInput from '../model/ListRepositorySyncDefinitionsInput';
import ListRepositorySyncDefinitionsOutput from '../model/ListRepositorySyncDefinitionsOutput';
import ListServiceInstanceOutputsInput from '../model/ListServiceInstanceOutputsInput';
import ListServiceInstanceOutputsOutput from '../model/ListServiceInstanceOutputsOutput';
import ListServiceInstanceProvisionedResourcesInput from '../model/ListServiceInstanceProvisionedResourcesInput';
import ListServiceInstanceProvisionedResourcesOutput from '../model/ListServiceInstanceProvisionedResourcesOutput';
import ListServiceInstancesInput from '../model/ListServiceInstancesInput';
import ListServiceInstancesOutput from '../model/ListServiceInstancesOutput';
import ListServicePipelineOutputsInput from '../model/ListServicePipelineOutputsInput';
import ListServicePipelineOutputsOutput from '../model/ListServicePipelineOutputsOutput';
import ListServicePipelineProvisionedResourcesInput from '../model/ListServicePipelineProvisionedResourcesInput';
import ListServicePipelineProvisionedResourcesOutput from '../model/ListServicePipelineProvisionedResourcesOutput';
import ListServiceTemplateVersionsInput from '../model/ListServiceTemplateVersionsInput';
import ListServiceTemplateVersionsOutput from '../model/ListServiceTemplateVersionsOutput';
import ListServiceTemplatesInput from '../model/ListServiceTemplatesInput';
import ListServiceTemplatesOutput from '../model/ListServiceTemplatesOutput';
import ListServicesInput from '../model/ListServicesInput';
import ListServicesOutput from '../model/ListServicesOutput';
import ListTagsForResourceInput from '../model/ListTagsForResourceInput';
import ListTagsForResourceOutput from '../model/ListTagsForResourceOutput';
import NotifyResourceDeploymentStatusChangeInput from '../model/NotifyResourceDeploymentStatusChangeInput';
import RejectEnvironmentAccountConnectionInput from '../model/RejectEnvironmentAccountConnectionInput';
import RejectEnvironmentAccountConnectionOutput from '../model/RejectEnvironmentAccountConnectionOutput';
import TagResourceInput from '../model/TagResourceInput';
import UntagResourceInput from '../model/UntagResourceInput';
import UpdateAccountSettingsInput from '../model/UpdateAccountSettingsInput';
import UpdateAccountSettingsOutput from '../model/UpdateAccountSettingsOutput';
import UpdateComponentInput from '../model/UpdateComponentInput';
import UpdateComponentOutput from '../model/UpdateComponentOutput';
import UpdateEnvironmentAccountConnectionInput from '../model/UpdateEnvironmentAccountConnectionInput';
import UpdateEnvironmentAccountConnectionOutput from '../model/UpdateEnvironmentAccountConnectionOutput';
import UpdateEnvironmentInput from '../model/UpdateEnvironmentInput';
import UpdateEnvironmentOutput from '../model/UpdateEnvironmentOutput';
import UpdateEnvironmentTemplateInput from '../model/UpdateEnvironmentTemplateInput';
import UpdateEnvironmentTemplateOutput from '../model/UpdateEnvironmentTemplateOutput';
import UpdateEnvironmentTemplateVersionInput from '../model/UpdateEnvironmentTemplateVersionInput';
import UpdateEnvironmentTemplateVersionOutput from '../model/UpdateEnvironmentTemplateVersionOutput';
import UpdateServiceInput from '../model/UpdateServiceInput';
import UpdateServiceInstanceInput from '../model/UpdateServiceInstanceInput';
import UpdateServiceInstanceOutput from '../model/UpdateServiceInstanceOutput';
import UpdateServiceOutput from '../model/UpdateServiceOutput';
import UpdateServicePipelineInput from '../model/UpdateServicePipelineInput';
import UpdateServicePipelineOutput from '../model/UpdateServicePipelineOutput';
import UpdateServiceSyncBlockerInput from '../model/UpdateServiceSyncBlockerInput';
import UpdateServiceSyncBlockerOutput from '../model/UpdateServiceSyncBlockerOutput';
import UpdateServiceSyncConfigInput from '../model/UpdateServiceSyncConfigInput';
import UpdateServiceSyncConfigOutput from '../model/UpdateServiceSyncConfigOutput';
import UpdateServiceTemplateInput from '../model/UpdateServiceTemplateInput';
import UpdateServiceTemplateOutput from '../model/UpdateServiceTemplateOutput';
import UpdateServiceTemplateVersionInput from '../model/UpdateServiceTemplateVersionInput';
import UpdateServiceTemplateVersionOutput from '../model/UpdateServiceTemplateVersionOutput';
import UpdateTemplateSyncConfigInput from '../model/UpdateTemplateSyncConfigInput';
import UpdateTemplateSyncConfigOutput from '../model/UpdateTemplateSyncConfigOutput';

/**
* Default service.
* @module api/DefaultApi
* @version 2020-07-20
*/
export default class DefaultApi {

    /**
    * Constructs a new DefaultApi. 
    * @alias module:api/DefaultApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the acceptEnvironmentAccountConnection operation.
     * @callback module:api/DefaultApi~acceptEnvironmentAccountConnectionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AcceptEnvironmentAccountConnectionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>In a management account, an environment account connection request is accepted. When the environment account connection request is accepted, Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/AcceptEnvironmentAccountConnectionInput} acceptEnvironmentAccountConnectionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~acceptEnvironmentAccountConnectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AcceptEnvironmentAccountConnectionOutput}
     */
    acceptEnvironmentAccountConnection(xAmzTarget, acceptEnvironmentAccountConnectionInput, opts, callback) {
      opts = opts || {};
      let postBody = acceptEnvironmentAccountConnectionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling acceptEnvironmentAccountConnection");
      }
      // verify the required parameter 'acceptEnvironmentAccountConnectionInput' is set
      if (acceptEnvironmentAccountConnectionInput === undefined || acceptEnvironmentAccountConnectionInput === null) {
        throw new Error("Missing the required parameter 'acceptEnvironmentAccountConnectionInput' when calling acceptEnvironmentAccountConnection");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = AcceptEnvironmentAccountConnectionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.AcceptEnvironmentAccountConnection', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cancelComponentDeployment operation.
     * @callback module:api/DefaultApi~cancelComponentDeploymentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CancelComponentDeploymentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Attempts to cancel a component deployment (for a component that is in the <code>IN_PROGRESS</code> deployment status).</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CancelComponentDeploymentInput} cancelComponentDeploymentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~cancelComponentDeploymentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CancelComponentDeploymentOutput}
     */
    cancelComponentDeployment(xAmzTarget, cancelComponentDeploymentInput, opts, callback) {
      opts = opts || {};
      let postBody = cancelComponentDeploymentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling cancelComponentDeployment");
      }
      // verify the required parameter 'cancelComponentDeploymentInput' is set
      if (cancelComponentDeploymentInput === undefined || cancelComponentDeploymentInput === null) {
        throw new Error("Missing the required parameter 'cancelComponentDeploymentInput' when calling cancelComponentDeployment");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CancelComponentDeploymentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CancelComponentDeployment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cancelEnvironmentDeployment operation.
     * @callback module:api/DefaultApi~cancelEnvironmentDeploymentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CancelEnvironmentDeploymentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Attempts to cancel an environment deployment on an <a>UpdateEnvironment</a> action, if the deployment is <code>IN_PROGRESS</code>. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-update.html\">Update an environment</a> in the <i>Proton User guide</i>.</p> <p>The following list includes potential cancellation scenarios.</p> <ul> <li> <p>If the cancellation attempt succeeds, the resulting deployment state is <code>CANCELLED</code>.</p> </li> <li> <p>If the cancellation attempt fails, the resulting deployment state is <code>FAILED</code>.</p> </li> <li> <p>If the current <a>UpdateEnvironment</a> action succeeds before the cancellation attempt starts, the resulting deployment state is <code>SUCCEEDED</code> and the cancellation attempt has no effect.</p> </li> </ul>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CancelEnvironmentDeploymentInput} cancelEnvironmentDeploymentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~cancelEnvironmentDeploymentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CancelEnvironmentDeploymentOutput}
     */
    cancelEnvironmentDeployment(xAmzTarget, cancelEnvironmentDeploymentInput, opts, callback) {
      opts = opts || {};
      let postBody = cancelEnvironmentDeploymentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling cancelEnvironmentDeployment");
      }
      // verify the required parameter 'cancelEnvironmentDeploymentInput' is set
      if (cancelEnvironmentDeploymentInput === undefined || cancelEnvironmentDeploymentInput === null) {
        throw new Error("Missing the required parameter 'cancelEnvironmentDeploymentInput' when calling cancelEnvironmentDeployment");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CancelEnvironmentDeploymentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CancelEnvironmentDeployment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cancelServiceInstanceDeployment operation.
     * @callback module:api/DefaultApi~cancelServiceInstanceDeploymentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CancelServiceInstanceDeploymentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Attempts to cancel a service instance deployment on an <a>UpdateServiceInstance</a> action, if the deployment is <code>IN_PROGRESS</code>. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-instance-update.html\">Update a service instance</a> in the <i>Proton User guide</i>.</p> <p>The following list includes potential cancellation scenarios.</p> <ul> <li> <p>If the cancellation attempt succeeds, the resulting deployment state is <code>CANCELLED</code>.</p> </li> <li> <p>If the cancellation attempt fails, the resulting deployment state is <code>FAILED</code>.</p> </li> <li> <p>If the current <a>UpdateServiceInstance</a> action succeeds before the cancellation attempt starts, the resulting deployment state is <code>SUCCEEDED</code> and the cancellation attempt has no effect.</p> </li> </ul>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CancelServiceInstanceDeploymentInput} cancelServiceInstanceDeploymentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~cancelServiceInstanceDeploymentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CancelServiceInstanceDeploymentOutput}
     */
    cancelServiceInstanceDeployment(xAmzTarget, cancelServiceInstanceDeploymentInput, opts, callback) {
      opts = opts || {};
      let postBody = cancelServiceInstanceDeploymentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling cancelServiceInstanceDeployment");
      }
      // verify the required parameter 'cancelServiceInstanceDeploymentInput' is set
      if (cancelServiceInstanceDeploymentInput === undefined || cancelServiceInstanceDeploymentInput === null) {
        throw new Error("Missing the required parameter 'cancelServiceInstanceDeploymentInput' when calling cancelServiceInstanceDeployment");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CancelServiceInstanceDeploymentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CancelServiceInstanceDeployment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cancelServicePipelineDeployment operation.
     * @callback module:api/DefaultApi~cancelServicePipelineDeploymentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CancelServicePipelineDeploymentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Attempts to cancel a service pipeline deployment on an <a>UpdateServicePipeline</a> action, if the deployment is <code>IN_PROGRESS</code>. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-pipeline-update.html\">Update a service pipeline</a> in the <i>Proton User guide</i>.</p> <p>The following list includes potential cancellation scenarios.</p> <ul> <li> <p>If the cancellation attempt succeeds, the resulting deployment state is <code>CANCELLED</code>.</p> </li> <li> <p>If the cancellation attempt fails, the resulting deployment state is <code>FAILED</code>.</p> </li> <li> <p>If the current <a>UpdateServicePipeline</a> action succeeds before the cancellation attempt starts, the resulting deployment state is <code>SUCCEEDED</code> and the cancellation attempt has no effect.</p> </li> </ul>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CancelServicePipelineDeploymentInput} cancelServicePipelineDeploymentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~cancelServicePipelineDeploymentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CancelServicePipelineDeploymentOutput}
     */
    cancelServicePipelineDeployment(xAmzTarget, cancelServicePipelineDeploymentInput, opts, callback) {
      opts = opts || {};
      let postBody = cancelServicePipelineDeploymentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling cancelServicePipelineDeployment");
      }
      // verify the required parameter 'cancelServicePipelineDeploymentInput' is set
      if (cancelServicePipelineDeploymentInput === undefined || cancelServicePipelineDeploymentInput === null) {
        throw new Error("Missing the required parameter 'cancelServicePipelineDeploymentInput' when calling cancelServicePipelineDeployment");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CancelServicePipelineDeploymentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CancelServicePipelineDeployment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createComponent operation.
     * @callback module:api/DefaultApi~createComponentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateComponentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Create an Proton component. A component is an infrastructure extension for a service instance.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateComponentInput} createComponentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createComponentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateComponentOutput}
     */
    createComponent(xAmzTarget, createComponentInput, opts, callback) {
      opts = opts || {};
      let postBody = createComponentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createComponent");
      }
      // verify the required parameter 'createComponentInput' is set
      if (createComponentInput === undefined || createComponentInput === null) {
        throw new Error("Missing the required parameter 'createComponentInput' when calling createComponent");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateComponentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CreateComponent', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createEnvironment operation.
     * @callback module:api/DefaultApi~createEnvironmentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateEnvironmentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Deploy a new environment. An Proton environment is created from an environment template that defines infrastructure and resources that can be shared across services.</p> <p class=\"title\"> <b>You can provision environments using the following methods:</b> </p> <ul> <li> <p>Amazon Web Services-managed provisioning: Proton makes direct calls to provision your resources.</p> </li> <li> <p>Self-managed provisioning: Proton makes pull requests on your repository to provide compiled infrastructure as code (IaC) files that your IaC engine uses to provision resources.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html\">Environments</a> and <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html\">Provisioning methods</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateEnvironmentInput} createEnvironmentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createEnvironmentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateEnvironmentOutput}
     */
    createEnvironment(xAmzTarget, createEnvironmentInput, opts, callback) {
      opts = opts || {};
      let postBody = createEnvironmentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createEnvironment");
      }
      // verify the required parameter 'createEnvironmentInput' is set
      if (createEnvironmentInput === undefined || createEnvironmentInput === null) {
        throw new Error("Missing the required parameter 'createEnvironmentInput' when calling createEnvironment");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateEnvironmentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CreateEnvironment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createEnvironmentAccountConnection operation.
     * @callback module:api/DefaultApi~createEnvironmentAccountConnectionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateEnvironmentAccountConnectionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Create an environment account connection in an environment account so that environment infrastructure resources can be provisioned in the environment account from a management account.</p> <p>An environment account connection is a secure bi-directional connection between a <i>management account</i> and an <i>environment account</i> that maintains authorization and permissions. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateEnvironmentAccountConnectionInput} createEnvironmentAccountConnectionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createEnvironmentAccountConnectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateEnvironmentAccountConnectionOutput}
     */
    createEnvironmentAccountConnection(xAmzTarget, createEnvironmentAccountConnectionInput, opts, callback) {
      opts = opts || {};
      let postBody = createEnvironmentAccountConnectionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createEnvironmentAccountConnection");
      }
      // verify the required parameter 'createEnvironmentAccountConnectionInput' is set
      if (createEnvironmentAccountConnectionInput === undefined || createEnvironmentAccountConnectionInput === null) {
        throw new Error("Missing the required parameter 'createEnvironmentAccountConnectionInput' when calling createEnvironmentAccountConnection");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateEnvironmentAccountConnectionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CreateEnvironmentAccountConnection', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createEnvironmentTemplate operation.
     * @callback module:api/DefaultApi~createEnvironmentTemplateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateEnvironmentTemplateOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Create an environment template for Proton. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html\">Environment Templates</a> in the <i>Proton User Guide</i>.</p> <p>You can create an environment template in one of the two following ways:</p> <ul> <li> <p>Register and publish a <i>standard</i> environment template that instructs Proton to deploy and manage environment infrastructure.</p> </li> <li> <p>Register and publish a <i>customer managed</i> environment template that connects Proton to your existing provisioned infrastructure that you manage. Proton <i>doesn't</i> manage your existing provisioned infrastructure. To create an environment template for customer provisioned and managed infrastructure, include the <code>provisioning</code> parameter and set the value to <code>CUSTOMER_MANAGED</code>. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/template-create.html\">Register and publish an environment template</a> in the <i>Proton User Guide</i>.</p> </li> </ul>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateEnvironmentTemplateInput} createEnvironmentTemplateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createEnvironmentTemplateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateEnvironmentTemplateOutput}
     */
    createEnvironmentTemplate(xAmzTarget, createEnvironmentTemplateInput, opts, callback) {
      opts = opts || {};
      let postBody = createEnvironmentTemplateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createEnvironmentTemplate");
      }
      // verify the required parameter 'createEnvironmentTemplateInput' is set
      if (createEnvironmentTemplateInput === undefined || createEnvironmentTemplateInput === null) {
        throw new Error("Missing the required parameter 'createEnvironmentTemplateInput' when calling createEnvironmentTemplate");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateEnvironmentTemplateOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CreateEnvironmentTemplate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createEnvironmentTemplateVersion operation.
     * @callback module:api/DefaultApi~createEnvironmentTemplateVersionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateEnvironmentTemplateVersionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new major or minor version of an environment template. A major version of an environment template is a version that <i>isn't</i> backwards compatible. A minor version of an environment template is a version that's backwards compatible within its major version.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateEnvironmentTemplateVersionInput} createEnvironmentTemplateVersionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createEnvironmentTemplateVersionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateEnvironmentTemplateVersionOutput}
     */
    createEnvironmentTemplateVersion(xAmzTarget, createEnvironmentTemplateVersionInput, opts, callback) {
      opts = opts || {};
      let postBody = createEnvironmentTemplateVersionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createEnvironmentTemplateVersion");
      }
      // verify the required parameter 'createEnvironmentTemplateVersionInput' is set
      if (createEnvironmentTemplateVersionInput === undefined || createEnvironmentTemplateVersionInput === null) {
        throw new Error("Missing the required parameter 'createEnvironmentTemplateVersionInput' when calling createEnvironmentTemplateVersion");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateEnvironmentTemplateVersionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CreateEnvironmentTemplateVersion', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createRepository operation.
     * @callback module:api/DefaultApi~createRepositoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateRepositoryOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Create and register a link to a repository. Proton uses the link to repeatedly access the repository, to either push to it (self-managed provisioning) or pull from it (template sync). You can share a linked repository across multiple resources (like environments using self-managed provisioning, or synced templates). When you create a repository link, Proton creates a <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/using-service-linked-roles.html\">service-linked role</a> for you.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self\">Self-managed provisioning</a>, <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html#ag-template-bundles\">Template bundles</a>, and <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html\">Template sync configurations</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateRepositoryInput} createRepositoryInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createRepositoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateRepositoryOutput}
     */
    createRepository(xAmzTarget, createRepositoryInput, opts, callback) {
      opts = opts || {};
      let postBody = createRepositoryInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createRepository");
      }
      // verify the required parameter 'createRepositoryInput' is set
      if (createRepositoryInput === undefined || createRepositoryInput === null) {
        throw new Error("Missing the required parameter 'createRepositoryInput' when calling createRepository");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateRepositoryOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CreateRepository', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createService operation.
     * @callback module:api/DefaultApi~createServiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateServiceOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create an Proton service. An Proton service is an instantiation of a service template and often includes several service instances and pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-services.html\">Services</a> in the <i>Proton User Guide</i>.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateServiceInput} createServiceInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createServiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateServiceOutput}
     */
    createService(xAmzTarget, createServiceInput, opts, callback) {
      opts = opts || {};
      let postBody = createServiceInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createService");
      }
      // verify the required parameter 'createServiceInput' is set
      if (createServiceInput === undefined || createServiceInput === null) {
        throw new Error("Missing the required parameter 'createServiceInput' when calling createService");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateServiceOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CreateService', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createServiceInstance operation.
     * @callback module:api/DefaultApi~createServiceInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateServiceInstanceOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a service instance.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateServiceInstanceInput} createServiceInstanceInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createServiceInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateServiceInstanceOutput}
     */
    createServiceInstance(xAmzTarget, createServiceInstanceInput, opts, callback) {
      opts = opts || {};
      let postBody = createServiceInstanceInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createServiceInstance");
      }
      // verify the required parameter 'createServiceInstanceInput' is set
      if (createServiceInstanceInput === undefined || createServiceInstanceInput === null) {
        throw new Error("Missing the required parameter 'createServiceInstanceInput' when calling createServiceInstance");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateServiceInstanceOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CreateServiceInstance', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createServiceSyncConfig operation.
     * @callback module:api/DefaultApi~createServiceSyncConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateServiceSyncConfigOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create the Proton Ops configuration file.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateServiceSyncConfigInput} createServiceSyncConfigInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createServiceSyncConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateServiceSyncConfigOutput}
     */
    createServiceSyncConfig(xAmzTarget, createServiceSyncConfigInput, opts, callback) {
      opts = opts || {};
      let postBody = createServiceSyncConfigInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createServiceSyncConfig");
      }
      // verify the required parameter 'createServiceSyncConfigInput' is set
      if (createServiceSyncConfigInput === undefined || createServiceSyncConfigInput === null) {
        throw new Error("Missing the required parameter 'createServiceSyncConfigInput' when calling createServiceSyncConfig");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateServiceSyncConfigOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CreateServiceSyncConfig', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createServiceTemplate operation.
     * @callback module:api/DefaultApi~createServiceTemplateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateServiceTemplateOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a service template. The administrator creates a service template to define standardized infrastructure and an optional CI/CD service pipeline. Developers, in turn, select the service template from Proton. If the selected service template includes a service pipeline definition, they provide a link to their source code repository. Proton then deploys and manages the infrastructure defined by the selected service template. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html\">Proton templates</a> in the <i>Proton User Guide</i>.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateServiceTemplateInput} createServiceTemplateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createServiceTemplateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateServiceTemplateOutput}
     */
    createServiceTemplate(xAmzTarget, createServiceTemplateInput, opts, callback) {
      opts = opts || {};
      let postBody = createServiceTemplateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createServiceTemplate");
      }
      // verify the required parameter 'createServiceTemplateInput' is set
      if (createServiceTemplateInput === undefined || createServiceTemplateInput === null) {
        throw new Error("Missing the required parameter 'createServiceTemplateInput' when calling createServiceTemplate");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateServiceTemplateOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CreateServiceTemplate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createServiceTemplateVersion operation.
     * @callback module:api/DefaultApi~createServiceTemplateVersionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateServiceTemplateVersionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new major or minor version of a service template. A major version of a service template is a version that <i>isn't</i> backward compatible. A minor version of a service template is a version that's backward compatible within its major version.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateServiceTemplateVersionInput} createServiceTemplateVersionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createServiceTemplateVersionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateServiceTemplateVersionOutput}
     */
    createServiceTemplateVersion(xAmzTarget, createServiceTemplateVersionInput, opts, callback) {
      opts = opts || {};
      let postBody = createServiceTemplateVersionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createServiceTemplateVersion");
      }
      // verify the required parameter 'createServiceTemplateVersionInput' is set
      if (createServiceTemplateVersionInput === undefined || createServiceTemplateVersionInput === null) {
        throw new Error("Missing the required parameter 'createServiceTemplateVersionInput' when calling createServiceTemplateVersion");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateServiceTemplateVersionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CreateServiceTemplateVersion', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createTemplateSyncConfig operation.
     * @callback module:api/DefaultApi~createTemplateSyncConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateTemplateSyncConfigOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Set up a template to create new template versions automatically by tracking a linked repository. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p> <p>When a commit is pushed to your linked repository, Proton checks for changes to your repository template bundles. If it detects a template bundle change, a new major or minor version of its template is created, if the version doesn’t already exist. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html\">Template sync configurations</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateTemplateSyncConfigInput} createTemplateSyncConfigInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createTemplateSyncConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateTemplateSyncConfigOutput}
     */
    createTemplateSyncConfig(xAmzTarget, createTemplateSyncConfigInput, opts, callback) {
      opts = opts || {};
      let postBody = createTemplateSyncConfigInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createTemplateSyncConfig");
      }
      // verify the required parameter 'createTemplateSyncConfigInput' is set
      if (createTemplateSyncConfigInput === undefined || createTemplateSyncConfigInput === null) {
        throw new Error("Missing the required parameter 'createTemplateSyncConfigInput' when calling createTemplateSyncConfig");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateTemplateSyncConfigOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.CreateTemplateSyncConfig', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteComponent operation.
     * @callback module:api/DefaultApi~deleteComponentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteComponentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Delete an Proton component resource.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteComponentInput} deleteComponentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteComponentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteComponentOutput}
     */
    deleteComponent(xAmzTarget, deleteComponentInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteComponentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteComponent");
      }
      // verify the required parameter 'deleteComponentInput' is set
      if (deleteComponentInput === undefined || deleteComponentInput === null) {
        throw new Error("Missing the required parameter 'deleteComponentInput' when calling deleteComponent");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteComponentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.DeleteComponent', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteDeployment operation.
     * @callback module:api/DefaultApi~deleteDeploymentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteDeploymentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete the deployment.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteDeploymentInput} deleteDeploymentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteDeploymentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteDeploymentOutput}
     */
    deleteDeployment(xAmzTarget, deleteDeploymentInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteDeploymentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteDeployment");
      }
      // verify the required parameter 'deleteDeploymentInput' is set
      if (deleteDeploymentInput === undefined || deleteDeploymentInput === null) {
        throw new Error("Missing the required parameter 'deleteDeploymentInput' when calling deleteDeployment");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteDeploymentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.DeleteDeployment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteEnvironment operation.
     * @callback module:api/DefaultApi~deleteEnvironmentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteEnvironmentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an environment.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteEnvironmentInput} deleteEnvironmentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteEnvironmentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteEnvironmentOutput}
     */
    deleteEnvironment(xAmzTarget, deleteEnvironmentInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteEnvironmentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteEnvironment");
      }
      // verify the required parameter 'deleteEnvironmentInput' is set
      if (deleteEnvironmentInput === undefined || deleteEnvironmentInput === null) {
        throw new Error("Missing the required parameter 'deleteEnvironmentInput' when calling deleteEnvironment");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteEnvironmentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.DeleteEnvironment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteEnvironmentAccountConnection operation.
     * @callback module:api/DefaultApi~deleteEnvironmentAccountConnectionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteEnvironmentAccountConnectionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>In an environment account, delete an environment account connection.</p> <p>After you delete an environment account connection that’s in use by an Proton environment, Proton <i>can’t</i> manage the environment infrastructure resources until a new environment account connection is accepted for the environment account and associated environment. You're responsible for cleaning up provisioned resources that remain without an environment connection.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteEnvironmentAccountConnectionInput} deleteEnvironmentAccountConnectionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteEnvironmentAccountConnectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteEnvironmentAccountConnectionOutput}
     */
    deleteEnvironmentAccountConnection(xAmzTarget, deleteEnvironmentAccountConnectionInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteEnvironmentAccountConnectionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteEnvironmentAccountConnection");
      }
      // verify the required parameter 'deleteEnvironmentAccountConnectionInput' is set
      if (deleteEnvironmentAccountConnectionInput === undefined || deleteEnvironmentAccountConnectionInput === null) {
        throw new Error("Missing the required parameter 'deleteEnvironmentAccountConnectionInput' when calling deleteEnvironmentAccountConnection");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteEnvironmentAccountConnectionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.DeleteEnvironmentAccountConnection', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteEnvironmentTemplate operation.
     * @callback module:api/DefaultApi~deleteEnvironmentTemplateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteEnvironmentTemplateOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * If no other major or minor versions of an environment template exist, delete the environment template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteEnvironmentTemplateInput} deleteEnvironmentTemplateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteEnvironmentTemplateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteEnvironmentTemplateOutput}
     */
    deleteEnvironmentTemplate(xAmzTarget, deleteEnvironmentTemplateInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteEnvironmentTemplateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteEnvironmentTemplate");
      }
      // verify the required parameter 'deleteEnvironmentTemplateInput' is set
      if (deleteEnvironmentTemplateInput === undefined || deleteEnvironmentTemplateInput === null) {
        throw new Error("Missing the required parameter 'deleteEnvironmentTemplateInput' when calling deleteEnvironmentTemplate");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteEnvironmentTemplateOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.DeleteEnvironmentTemplate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteEnvironmentTemplateVersion operation.
     * @callback module:api/DefaultApi~deleteEnvironmentTemplateVersionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteEnvironmentTemplateVersionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>If no other minor versions of an environment template exist, delete a major version of the environment template if it's not the <code>Recommended</code> version. Delete the <code>Recommended</code> version of the environment template if no other major versions or minor versions of the environment template exist. A major version of an environment template is a version that's not backward compatible.</p> <p>Delete a minor version of an environment template if it <i>isn't</i> the <code>Recommended</code> version. Delete a <code>Recommended</code> minor version of the environment template if no other minor versions of the environment template exist. A minor version of an environment template is a version that's backward compatible.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteEnvironmentTemplateVersionInput} deleteEnvironmentTemplateVersionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteEnvironmentTemplateVersionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteEnvironmentTemplateVersionOutput}
     */
    deleteEnvironmentTemplateVersion(xAmzTarget, deleteEnvironmentTemplateVersionInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteEnvironmentTemplateVersionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteEnvironmentTemplateVersion");
      }
      // verify the required parameter 'deleteEnvironmentTemplateVersionInput' is set
      if (deleteEnvironmentTemplateVersionInput === undefined || deleteEnvironmentTemplateVersionInput === null) {
        throw new Error("Missing the required parameter 'deleteEnvironmentTemplateVersionInput' when calling deleteEnvironmentTemplateVersion");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteEnvironmentTemplateVersionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.DeleteEnvironmentTemplateVersion', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteRepository operation.
     * @callback module:api/DefaultApi~deleteRepositoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteRepositoryOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * De-register and unlink your repository.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteRepositoryInput} deleteRepositoryInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteRepositoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteRepositoryOutput}
     */
    deleteRepository(xAmzTarget, deleteRepositoryInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteRepositoryInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteRepository");
      }
      // verify the required parameter 'deleteRepositoryInput' is set
      if (deleteRepositoryInput === undefined || deleteRepositoryInput === null) {
        throw new Error("Missing the required parameter 'deleteRepositoryInput' when calling deleteRepository");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteRepositoryOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.DeleteRepository', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteService operation.
     * @callback module:api/DefaultApi~deleteServiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteServiceOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Delete a service, with its instances and pipeline.</p> <note> <p>You can't delete a service if it has any service instances that have components attached to them.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteServiceInput} deleteServiceInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteServiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteServiceOutput}
     */
    deleteService(xAmzTarget, deleteServiceInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteServiceInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteService");
      }
      // verify the required parameter 'deleteServiceInput' is set
      if (deleteServiceInput === undefined || deleteServiceInput === null) {
        throw new Error("Missing the required parameter 'deleteServiceInput' when calling deleteService");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteServiceOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.DeleteService', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteServiceSyncConfig operation.
     * @callback module:api/DefaultApi~deleteServiceSyncConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteServiceSyncConfigOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete the Proton Ops file.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteServiceSyncConfigInput} deleteServiceSyncConfigInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteServiceSyncConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteServiceSyncConfigOutput}
     */
    deleteServiceSyncConfig(xAmzTarget, deleteServiceSyncConfigInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteServiceSyncConfigInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteServiceSyncConfig");
      }
      // verify the required parameter 'deleteServiceSyncConfigInput' is set
      if (deleteServiceSyncConfigInput === undefined || deleteServiceSyncConfigInput === null) {
        throw new Error("Missing the required parameter 'deleteServiceSyncConfigInput' when calling deleteServiceSyncConfig");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteServiceSyncConfigOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.DeleteServiceSyncConfig', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteServiceTemplate operation.
     * @callback module:api/DefaultApi~deleteServiceTemplateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteServiceTemplateOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * If no other major or minor versions of the service template exist, delete the service template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteServiceTemplateInput} deleteServiceTemplateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteServiceTemplateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteServiceTemplateOutput}
     */
    deleteServiceTemplate(xAmzTarget, deleteServiceTemplateInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteServiceTemplateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteServiceTemplate");
      }
      // verify the required parameter 'deleteServiceTemplateInput' is set
      if (deleteServiceTemplateInput === undefined || deleteServiceTemplateInput === null) {
        throw new Error("Missing the required parameter 'deleteServiceTemplateInput' when calling deleteServiceTemplate");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteServiceTemplateOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.DeleteServiceTemplate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteServiceTemplateVersion operation.
     * @callback module:api/DefaultApi~deleteServiceTemplateVersionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteServiceTemplateVersionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>If no other minor versions of a service template exist, delete a major version of the service template if it's not the <code>Recommended</code> version. Delete the <code>Recommended</code> version of the service template if no other major versions or minor versions of the service template exist. A major version of a service template is a version that <i>isn't</i> backwards compatible.</p> <p>Delete a minor version of a service template if it's not the <code>Recommended</code> version. Delete a <code>Recommended</code> minor version of the service template if no other minor versions of the service template exist. A minor version of a service template is a version that's backwards compatible.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteServiceTemplateVersionInput} deleteServiceTemplateVersionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteServiceTemplateVersionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteServiceTemplateVersionOutput}
     */
    deleteServiceTemplateVersion(xAmzTarget, deleteServiceTemplateVersionInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteServiceTemplateVersionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteServiceTemplateVersion");
      }
      // verify the required parameter 'deleteServiceTemplateVersionInput' is set
      if (deleteServiceTemplateVersionInput === undefined || deleteServiceTemplateVersionInput === null) {
        throw new Error("Missing the required parameter 'deleteServiceTemplateVersionInput' when calling deleteServiceTemplateVersion");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteServiceTemplateVersionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.DeleteServiceTemplateVersion', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteTemplateSyncConfig operation.
     * @callback module:api/DefaultApi~deleteTemplateSyncConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteTemplateSyncConfigOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a template sync configuration.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteTemplateSyncConfigInput} deleteTemplateSyncConfigInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteTemplateSyncConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteTemplateSyncConfigOutput}
     */
    deleteTemplateSyncConfig(xAmzTarget, deleteTemplateSyncConfigInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteTemplateSyncConfigInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteTemplateSyncConfig");
      }
      // verify the required parameter 'deleteTemplateSyncConfigInput' is set
      if (deleteTemplateSyncConfigInput === undefined || deleteTemplateSyncConfigInput === null) {
        throw new Error("Missing the required parameter 'deleteTemplateSyncConfigInput' when calling deleteTemplateSyncConfig");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteTemplateSyncConfigOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.DeleteTemplateSyncConfig', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAccountSettings operation.
     * @callback module:api/DefaultApi~getAccountSettingsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetAccountSettingsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get detail data for Proton account-wide settings.
     * @param {module:model/String} xAmzTarget 
     * @param {Object.<String, Object>} body 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getAccountSettingsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetAccountSettingsOutput}
     */
    getAccountSettings(xAmzTarget, body, opts, callback) {
      opts = opts || {};
      let postBody = body;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getAccountSettings");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling getAccountSettings");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetAccountSettingsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetAccountSettings', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getComponent operation.
     * @callback module:api/DefaultApi~getComponentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetComponentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Get detailed data for a component.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetComponentInput} getComponentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getComponentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetComponentOutput}
     */
    getComponent(xAmzTarget, getComponentInput, opts, callback) {
      opts = opts || {};
      let postBody = getComponentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getComponent");
      }
      // verify the required parameter 'getComponentInput' is set
      if (getComponentInput === undefined || getComponentInput === null) {
        throw new Error("Missing the required parameter 'getComponentInput' when calling getComponent");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetComponentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetComponent', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDeployment operation.
     * @callback module:api/DefaultApi~getDeploymentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDeploymentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get detailed data for a deployment.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetDeploymentInput} getDeploymentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getDeploymentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDeploymentOutput}
     */
    getDeployment(xAmzTarget, getDeploymentInput, opts, callback) {
      opts = opts || {};
      let postBody = getDeploymentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getDeployment");
      }
      // verify the required parameter 'getDeploymentInput' is set
      if (getDeploymentInput === undefined || getDeploymentInput === null) {
        throw new Error("Missing the required parameter 'getDeploymentInput' when calling getDeployment");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetDeploymentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetDeployment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getEnvironment operation.
     * @callback module:api/DefaultApi~getEnvironmentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetEnvironmentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get detailed data for an environment.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetEnvironmentInput} getEnvironmentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getEnvironmentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetEnvironmentOutput}
     */
    getEnvironment(xAmzTarget, getEnvironmentInput, opts, callback) {
      opts = opts || {};
      let postBody = getEnvironmentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getEnvironment");
      }
      // verify the required parameter 'getEnvironmentInput' is set
      if (getEnvironmentInput === undefined || getEnvironmentInput === null) {
        throw new Error("Missing the required parameter 'getEnvironmentInput' when calling getEnvironment");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetEnvironmentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetEnvironment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getEnvironmentAccountConnection operation.
     * @callback module:api/DefaultApi~getEnvironmentAccountConnectionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetEnvironmentAccountConnectionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>In an environment account, get the detailed data for an environment account connection.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetEnvironmentAccountConnectionInput} getEnvironmentAccountConnectionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getEnvironmentAccountConnectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetEnvironmentAccountConnectionOutput}
     */
    getEnvironmentAccountConnection(xAmzTarget, getEnvironmentAccountConnectionInput, opts, callback) {
      opts = opts || {};
      let postBody = getEnvironmentAccountConnectionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getEnvironmentAccountConnection");
      }
      // verify the required parameter 'getEnvironmentAccountConnectionInput' is set
      if (getEnvironmentAccountConnectionInput === undefined || getEnvironmentAccountConnectionInput === null) {
        throw new Error("Missing the required parameter 'getEnvironmentAccountConnectionInput' when calling getEnvironmentAccountConnection");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetEnvironmentAccountConnectionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetEnvironmentAccountConnection', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getEnvironmentTemplate operation.
     * @callback module:api/DefaultApi~getEnvironmentTemplateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetEnvironmentTemplateOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get detailed data for an environment template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetEnvironmentTemplateInput} getEnvironmentTemplateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getEnvironmentTemplateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetEnvironmentTemplateOutput}
     */
    getEnvironmentTemplate(xAmzTarget, getEnvironmentTemplateInput, opts, callback) {
      opts = opts || {};
      let postBody = getEnvironmentTemplateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getEnvironmentTemplate");
      }
      // verify the required parameter 'getEnvironmentTemplateInput' is set
      if (getEnvironmentTemplateInput === undefined || getEnvironmentTemplateInput === null) {
        throw new Error("Missing the required parameter 'getEnvironmentTemplateInput' when calling getEnvironmentTemplate");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetEnvironmentTemplateOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetEnvironmentTemplate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getEnvironmentTemplateVersion operation.
     * @callback module:api/DefaultApi~getEnvironmentTemplateVersionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetEnvironmentTemplateVersionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get detailed data for a major or minor version of an environment template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetEnvironmentTemplateVersionInput} getEnvironmentTemplateVersionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getEnvironmentTemplateVersionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetEnvironmentTemplateVersionOutput}
     */
    getEnvironmentTemplateVersion(xAmzTarget, getEnvironmentTemplateVersionInput, opts, callback) {
      opts = opts || {};
      let postBody = getEnvironmentTemplateVersionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getEnvironmentTemplateVersion");
      }
      // verify the required parameter 'getEnvironmentTemplateVersionInput' is set
      if (getEnvironmentTemplateVersionInput === undefined || getEnvironmentTemplateVersionInput === null) {
        throw new Error("Missing the required parameter 'getEnvironmentTemplateVersionInput' when calling getEnvironmentTemplateVersion");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetEnvironmentTemplateVersionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetEnvironmentTemplateVersion', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRepository operation.
     * @callback module:api/DefaultApi~getRepositoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetRepositoryOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get detail data for a linked repository.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetRepositoryInput} getRepositoryInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getRepositoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetRepositoryOutput}
     */
    getRepository(xAmzTarget, getRepositoryInput, opts, callback) {
      opts = opts || {};
      let postBody = getRepositoryInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getRepository");
      }
      // verify the required parameter 'getRepositoryInput' is set
      if (getRepositoryInput === undefined || getRepositoryInput === null) {
        throw new Error("Missing the required parameter 'getRepositoryInput' when calling getRepository");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetRepositoryOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetRepository', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRepositorySyncStatus operation.
     * @callback module:api/DefaultApi~getRepositorySyncStatusCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetRepositorySyncStatusOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Get the sync status of a repository used for Proton template sync. For more information about template sync, see .</p> <note> <p>A repository sync status isn't tied to the Proton Repository resource (or any other Proton resource). Therefore, tags on an Proton Repository resource have no effect on this action. Specifically, you can't use these tags to control access to this action using Attribute-based access control (ABAC).</p> <p>For more information about ABAC, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags\">ABAC</a> in the <i>Proton User Guide</i>.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetRepositorySyncStatusInput} getRepositorySyncStatusInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getRepositorySyncStatusCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetRepositorySyncStatusOutput}
     */
    getRepositorySyncStatus(xAmzTarget, getRepositorySyncStatusInput, opts, callback) {
      opts = opts || {};
      let postBody = getRepositorySyncStatusInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getRepositorySyncStatus");
      }
      // verify the required parameter 'getRepositorySyncStatusInput' is set
      if (getRepositorySyncStatusInput === undefined || getRepositorySyncStatusInput === null) {
        throw new Error("Missing the required parameter 'getRepositorySyncStatusInput' when calling getRepositorySyncStatus");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetRepositorySyncStatusOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetRepositorySyncStatus', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getResourcesSummary operation.
     * @callback module:api/DefaultApi~getResourcesSummaryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetResourcesSummaryOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Get counts of Proton resources.</p> <p>For infrastructure-provisioning resources (environments, services, service instances, pipelines), the action returns staleness counts. A resource is stale when it's behind the recommended version of the Proton template that it uses and it needs an update to become current.</p> <p>The action returns staleness counts (counts of resources that are up-to-date, behind a template major version, or behind a template minor version), the total number of resources, and the number of resources that are in a failed state, grouped by resource type. Components, environments, and service templates return less information - see the <code>components</code>, <code>environments</code>, and <code>serviceTemplates</code> field descriptions.</p> <p>For context, the action also returns the total number of each type of Proton template in the Amazon Web Services account.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/monitoring-dashboard.html\">Proton dashboard</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {Object.<String, Object>} body 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getResourcesSummaryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetResourcesSummaryOutput}
     */
    getResourcesSummary(xAmzTarget, body, opts, callback) {
      opts = opts || {};
      let postBody = body;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getResourcesSummary");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling getResourcesSummary");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetResourcesSummaryOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetResourcesSummary', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getService operation.
     * @callback module:api/DefaultApi~getServiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetServiceOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get detailed data for a service.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetServiceInput} getServiceInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getServiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetServiceOutput}
     */
    getService(xAmzTarget, getServiceInput, opts, callback) {
      opts = opts || {};
      let postBody = getServiceInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getService");
      }
      // verify the required parameter 'getServiceInput' is set
      if (getServiceInput === undefined || getServiceInput === null) {
        throw new Error("Missing the required parameter 'getServiceInput' when calling getService");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetServiceOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetService', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getServiceInstance operation.
     * @callback module:api/DefaultApi~getServiceInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetServiceInstanceOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get detailed data for a service instance. A service instance is an instantiation of service template and it runs in a specific environment.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetServiceInstanceInput} getServiceInstanceInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getServiceInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetServiceInstanceOutput}
     */
    getServiceInstance(xAmzTarget, getServiceInstanceInput, opts, callback) {
      opts = opts || {};
      let postBody = getServiceInstanceInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getServiceInstance");
      }
      // verify the required parameter 'getServiceInstanceInput' is set
      if (getServiceInstanceInput === undefined || getServiceInstanceInput === null) {
        throw new Error("Missing the required parameter 'getServiceInstanceInput' when calling getServiceInstance");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetServiceInstanceOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetServiceInstance', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getServiceInstanceSyncStatus operation.
     * @callback module:api/DefaultApi~getServiceInstanceSyncStatusCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetServiceInstanceSyncStatusOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the status of the synced service instance.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetServiceInstanceSyncStatusInput} getServiceInstanceSyncStatusInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getServiceInstanceSyncStatusCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetServiceInstanceSyncStatusOutput}
     */
    getServiceInstanceSyncStatus(xAmzTarget, getServiceInstanceSyncStatusInput, opts, callback) {
      opts = opts || {};
      let postBody = getServiceInstanceSyncStatusInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getServiceInstanceSyncStatus");
      }
      // verify the required parameter 'getServiceInstanceSyncStatusInput' is set
      if (getServiceInstanceSyncStatusInput === undefined || getServiceInstanceSyncStatusInput === null) {
        throw new Error("Missing the required parameter 'getServiceInstanceSyncStatusInput' when calling getServiceInstanceSyncStatus");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetServiceInstanceSyncStatusOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetServiceInstanceSyncStatus', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getServiceSyncBlockerSummary operation.
     * @callback module:api/DefaultApi~getServiceSyncBlockerSummaryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetServiceSyncBlockerSummaryOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get detailed data for the service sync blocker summary.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetServiceSyncBlockerSummaryInput} getServiceSyncBlockerSummaryInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getServiceSyncBlockerSummaryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetServiceSyncBlockerSummaryOutput}
     */
    getServiceSyncBlockerSummary(xAmzTarget, getServiceSyncBlockerSummaryInput, opts, callback) {
      opts = opts || {};
      let postBody = getServiceSyncBlockerSummaryInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getServiceSyncBlockerSummary");
      }
      // verify the required parameter 'getServiceSyncBlockerSummaryInput' is set
      if (getServiceSyncBlockerSummaryInput === undefined || getServiceSyncBlockerSummaryInput === null) {
        throw new Error("Missing the required parameter 'getServiceSyncBlockerSummaryInput' when calling getServiceSyncBlockerSummary");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetServiceSyncBlockerSummaryOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetServiceSyncBlockerSummary', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getServiceSyncConfig operation.
     * @callback module:api/DefaultApi~getServiceSyncConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetServiceSyncConfigOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get detailed information for the service sync configuration.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetServiceSyncConfigInput} getServiceSyncConfigInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getServiceSyncConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetServiceSyncConfigOutput}
     */
    getServiceSyncConfig(xAmzTarget, getServiceSyncConfigInput, opts, callback) {
      opts = opts || {};
      let postBody = getServiceSyncConfigInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getServiceSyncConfig");
      }
      // verify the required parameter 'getServiceSyncConfigInput' is set
      if (getServiceSyncConfigInput === undefined || getServiceSyncConfigInput === null) {
        throw new Error("Missing the required parameter 'getServiceSyncConfigInput' when calling getServiceSyncConfig");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetServiceSyncConfigOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetServiceSyncConfig', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getServiceTemplate operation.
     * @callback module:api/DefaultApi~getServiceTemplateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetServiceTemplateOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get detailed data for a service template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetServiceTemplateInput} getServiceTemplateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getServiceTemplateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetServiceTemplateOutput}
     */
    getServiceTemplate(xAmzTarget, getServiceTemplateInput, opts, callback) {
      opts = opts || {};
      let postBody = getServiceTemplateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getServiceTemplate");
      }
      // verify the required parameter 'getServiceTemplateInput' is set
      if (getServiceTemplateInput === undefined || getServiceTemplateInput === null) {
        throw new Error("Missing the required parameter 'getServiceTemplateInput' when calling getServiceTemplate");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetServiceTemplateOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetServiceTemplate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getServiceTemplateVersion operation.
     * @callback module:api/DefaultApi~getServiceTemplateVersionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetServiceTemplateVersionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get detailed data for a major or minor version of a service template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetServiceTemplateVersionInput} getServiceTemplateVersionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getServiceTemplateVersionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetServiceTemplateVersionOutput}
     */
    getServiceTemplateVersion(xAmzTarget, getServiceTemplateVersionInput, opts, callback) {
      opts = opts || {};
      let postBody = getServiceTemplateVersionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getServiceTemplateVersion");
      }
      // verify the required parameter 'getServiceTemplateVersionInput' is set
      if (getServiceTemplateVersionInput === undefined || getServiceTemplateVersionInput === null) {
        throw new Error("Missing the required parameter 'getServiceTemplateVersionInput' when calling getServiceTemplateVersion");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetServiceTemplateVersionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetServiceTemplateVersion', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTemplateSyncConfig operation.
     * @callback module:api/DefaultApi~getTemplateSyncConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetTemplateSyncConfigOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get detail data for a template sync configuration.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetTemplateSyncConfigInput} getTemplateSyncConfigInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getTemplateSyncConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetTemplateSyncConfigOutput}
     */
    getTemplateSyncConfig(xAmzTarget, getTemplateSyncConfigInput, opts, callback) {
      opts = opts || {};
      let postBody = getTemplateSyncConfigInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getTemplateSyncConfig");
      }
      // verify the required parameter 'getTemplateSyncConfigInput' is set
      if (getTemplateSyncConfigInput === undefined || getTemplateSyncConfigInput === null) {
        throw new Error("Missing the required parameter 'getTemplateSyncConfigInput' when calling getTemplateSyncConfig");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetTemplateSyncConfigOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetTemplateSyncConfig', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTemplateSyncStatus operation.
     * @callback module:api/DefaultApi~getTemplateSyncStatusCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetTemplateSyncStatusOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the status of a template sync.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetTemplateSyncStatusInput} getTemplateSyncStatusInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getTemplateSyncStatusCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetTemplateSyncStatusOutput}
     */
    getTemplateSyncStatus(xAmzTarget, getTemplateSyncStatusInput, opts, callback) {
      opts = opts || {};
      let postBody = getTemplateSyncStatusInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getTemplateSyncStatus");
      }
      // verify the required parameter 'getTemplateSyncStatusInput' is set
      if (getTemplateSyncStatusInput === undefined || getTemplateSyncStatusInput === null) {
        throw new Error("Missing the required parameter 'getTemplateSyncStatusInput' when calling getTemplateSyncStatus");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetTemplateSyncStatusOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.GetTemplateSyncStatus', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listComponentOutputs operation.
     * @callback module:api/DefaultApi~listComponentOutputsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListComponentOutputsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Get a list of component Infrastructure as Code (IaC) outputs.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListComponentOutputsInput} listComponentOutputsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listComponentOutputsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListComponentOutputsOutput}
     */
    listComponentOutputs(xAmzTarget, listComponentOutputsInput, opts, callback) {
      opts = opts || {};
      let postBody = listComponentOutputsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listComponentOutputs");
      }
      // verify the required parameter 'listComponentOutputsInput' is set
      if (listComponentOutputsInput === undefined || listComponentOutputsInput === null) {
        throw new Error("Missing the required parameter 'listComponentOutputsInput' when calling listComponentOutputs");
      }

      let pathParams = {
      };
      let queryParams = {
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListComponentOutputsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListComponentOutputs', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listComponentProvisionedResources operation.
     * @callback module:api/DefaultApi~listComponentProvisionedResourcesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListComponentProvisionedResourcesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>List provisioned resources for a component with details.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListComponentProvisionedResourcesInput} listComponentProvisionedResourcesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listComponentProvisionedResourcesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListComponentProvisionedResourcesOutput}
     */
    listComponentProvisionedResources(xAmzTarget, listComponentProvisionedResourcesInput, opts, callback) {
      opts = opts || {};
      let postBody = listComponentProvisionedResourcesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listComponentProvisionedResources");
      }
      // verify the required parameter 'listComponentProvisionedResourcesInput' is set
      if (listComponentProvisionedResourcesInput === undefined || listComponentProvisionedResourcesInput === null) {
        throw new Error("Missing the required parameter 'listComponentProvisionedResourcesInput' when calling listComponentProvisionedResources");
      }

      let pathParams = {
      };
      let queryParams = {
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListComponentProvisionedResourcesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListComponentProvisionedResources', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listComponents operation.
     * @callback module:api/DefaultApi~listComponentsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListComponentsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>List components with summary data. You can filter the result list by environment, service, or a single service instance.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListComponentsInput} listComponentsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listComponentsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListComponentsOutput}
     */
    listComponents(xAmzTarget, listComponentsInput, opts, callback) {
      opts = opts || {};
      let postBody = listComponentsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listComponents");
      }
      // verify the required parameter 'listComponentsInput' is set
      if (listComponentsInput === undefined || listComponentsInput === null) {
        throw new Error("Missing the required parameter 'listComponentsInput' when calling listComponents");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListComponentsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListComponents', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listDeployments operation.
     * @callback module:api/DefaultApi~listDeploymentsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListDeploymentsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List deployments. You can filter the result list by environment, service, or a single service instance.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListDeploymentsInput} listDeploymentsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listDeploymentsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListDeploymentsOutput}
     */
    listDeployments(xAmzTarget, listDeploymentsInput, opts, callback) {
      opts = opts || {};
      let postBody = listDeploymentsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listDeployments");
      }
      // verify the required parameter 'listDeploymentsInput' is set
      if (listDeploymentsInput === undefined || listDeploymentsInput === null) {
        throw new Error("Missing the required parameter 'listDeploymentsInput' when calling listDeployments");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListDeploymentsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListDeployments', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listEnvironmentAccountConnections operation.
     * @callback module:api/DefaultApi~listEnvironmentAccountConnectionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListEnvironmentAccountConnectionsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>View a list of environment account connections.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListEnvironmentAccountConnectionsInput} listEnvironmentAccountConnectionsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listEnvironmentAccountConnectionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListEnvironmentAccountConnectionsOutput}
     */
    listEnvironmentAccountConnections(xAmzTarget, listEnvironmentAccountConnectionsInput, opts, callback) {
      opts = opts || {};
      let postBody = listEnvironmentAccountConnectionsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listEnvironmentAccountConnections");
      }
      // verify the required parameter 'listEnvironmentAccountConnectionsInput' is set
      if (listEnvironmentAccountConnectionsInput === undefined || listEnvironmentAccountConnectionsInput === null) {
        throw new Error("Missing the required parameter 'listEnvironmentAccountConnectionsInput' when calling listEnvironmentAccountConnections");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListEnvironmentAccountConnectionsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListEnvironmentAccountConnections', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listEnvironmentOutputs operation.
     * @callback module:api/DefaultApi~listEnvironmentOutputsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListEnvironmentOutputsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the infrastructure as code outputs for your environment.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListEnvironmentOutputsInput} listEnvironmentOutputsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listEnvironmentOutputsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListEnvironmentOutputsOutput}
     */
    listEnvironmentOutputs(xAmzTarget, listEnvironmentOutputsInput, opts, callback) {
      opts = opts || {};
      let postBody = listEnvironmentOutputsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listEnvironmentOutputs");
      }
      // verify the required parameter 'listEnvironmentOutputsInput' is set
      if (listEnvironmentOutputsInput === undefined || listEnvironmentOutputsInput === null) {
        throw new Error("Missing the required parameter 'listEnvironmentOutputsInput' when calling listEnvironmentOutputs");
      }

      let pathParams = {
      };
      let queryParams = {
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListEnvironmentOutputsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListEnvironmentOutputs', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listEnvironmentProvisionedResources operation.
     * @callback module:api/DefaultApi~listEnvironmentProvisionedResourcesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListEnvironmentProvisionedResourcesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the provisioned resources for your environment.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListEnvironmentProvisionedResourcesInput} listEnvironmentProvisionedResourcesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listEnvironmentProvisionedResourcesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListEnvironmentProvisionedResourcesOutput}
     */
    listEnvironmentProvisionedResources(xAmzTarget, listEnvironmentProvisionedResourcesInput, opts, callback) {
      opts = opts || {};
      let postBody = listEnvironmentProvisionedResourcesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listEnvironmentProvisionedResources");
      }
      // verify the required parameter 'listEnvironmentProvisionedResourcesInput' is set
      if (listEnvironmentProvisionedResourcesInput === undefined || listEnvironmentProvisionedResourcesInput === null) {
        throw new Error("Missing the required parameter 'listEnvironmentProvisionedResourcesInput' when calling listEnvironmentProvisionedResources");
      }

      let pathParams = {
      };
      let queryParams = {
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListEnvironmentProvisionedResourcesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListEnvironmentProvisionedResources', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listEnvironmentTemplateVersions operation.
     * @callback module:api/DefaultApi~listEnvironmentTemplateVersionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListEnvironmentTemplateVersionsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List major or minor versions of an environment template with detail data.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListEnvironmentTemplateVersionsInput} listEnvironmentTemplateVersionsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listEnvironmentTemplateVersionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListEnvironmentTemplateVersionsOutput}
     */
    listEnvironmentTemplateVersions(xAmzTarget, listEnvironmentTemplateVersionsInput, opts, callback) {
      opts = opts || {};
      let postBody = listEnvironmentTemplateVersionsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listEnvironmentTemplateVersions");
      }
      // verify the required parameter 'listEnvironmentTemplateVersionsInput' is set
      if (listEnvironmentTemplateVersionsInput === undefined || listEnvironmentTemplateVersionsInput === null) {
        throw new Error("Missing the required parameter 'listEnvironmentTemplateVersionsInput' when calling listEnvironmentTemplateVersions");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListEnvironmentTemplateVersionsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListEnvironmentTemplateVersions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listEnvironmentTemplates operation.
     * @callback module:api/DefaultApi~listEnvironmentTemplatesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListEnvironmentTemplatesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List environment templates.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListEnvironmentTemplatesInput} listEnvironmentTemplatesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listEnvironmentTemplatesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListEnvironmentTemplatesOutput}
     */
    listEnvironmentTemplates(xAmzTarget, listEnvironmentTemplatesInput, opts, callback) {
      opts = opts || {};
      let postBody = listEnvironmentTemplatesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listEnvironmentTemplates");
      }
      // verify the required parameter 'listEnvironmentTemplatesInput' is set
      if (listEnvironmentTemplatesInput === undefined || listEnvironmentTemplatesInput === null) {
        throw new Error("Missing the required parameter 'listEnvironmentTemplatesInput' when calling listEnvironmentTemplates");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListEnvironmentTemplatesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListEnvironmentTemplates', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listEnvironments operation.
     * @callback module:api/DefaultApi~listEnvironmentsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListEnvironmentsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List environments with detail data summaries.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListEnvironmentsInput} listEnvironmentsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listEnvironmentsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListEnvironmentsOutput}
     */
    listEnvironments(xAmzTarget, listEnvironmentsInput, opts, callback) {
      opts = opts || {};
      let postBody = listEnvironmentsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listEnvironments");
      }
      // verify the required parameter 'listEnvironmentsInput' is set
      if (listEnvironmentsInput === undefined || listEnvironmentsInput === null) {
        throw new Error("Missing the required parameter 'listEnvironmentsInput' when calling listEnvironments");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListEnvironmentsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListEnvironments', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listRepositories operation.
     * @callback module:api/DefaultApi~listRepositoriesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListRepositoriesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List linked repositories with detail data.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListRepositoriesInput} listRepositoriesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listRepositoriesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListRepositoriesOutput}
     */
    listRepositories(xAmzTarget, listRepositoriesInput, opts, callback) {
      opts = opts || {};
      let postBody = listRepositoriesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listRepositories");
      }
      // verify the required parameter 'listRepositoriesInput' is set
      if (listRepositoriesInput === undefined || listRepositoriesInput === null) {
        throw new Error("Missing the required parameter 'listRepositoriesInput' when calling listRepositories");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListRepositoriesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListRepositories', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listRepositorySyncDefinitions operation.
     * @callback module:api/DefaultApi~listRepositorySyncDefinitionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListRepositorySyncDefinitionsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List repository sync definitions with detail data.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListRepositorySyncDefinitionsInput} listRepositorySyncDefinitionsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listRepositorySyncDefinitionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListRepositorySyncDefinitionsOutput}
     */
    listRepositorySyncDefinitions(xAmzTarget, listRepositorySyncDefinitionsInput, opts, callback) {
      opts = opts || {};
      let postBody = listRepositorySyncDefinitionsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listRepositorySyncDefinitions");
      }
      // verify the required parameter 'listRepositorySyncDefinitionsInput' is set
      if (listRepositorySyncDefinitionsInput === undefined || listRepositorySyncDefinitionsInput === null) {
        throw new Error("Missing the required parameter 'listRepositorySyncDefinitionsInput' when calling listRepositorySyncDefinitions");
      }

      let pathParams = {
      };
      let queryParams = {
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListRepositorySyncDefinitionsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListRepositorySyncDefinitions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listServiceInstanceOutputs operation.
     * @callback module:api/DefaultApi~listServiceInstanceOutputsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListServiceInstanceOutputsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a list service of instance Infrastructure as Code (IaC) outputs.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListServiceInstanceOutputsInput} listServiceInstanceOutputsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listServiceInstanceOutputsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListServiceInstanceOutputsOutput}
     */
    listServiceInstanceOutputs(xAmzTarget, listServiceInstanceOutputsInput, opts, callback) {
      opts = opts || {};
      let postBody = listServiceInstanceOutputsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listServiceInstanceOutputs");
      }
      // verify the required parameter 'listServiceInstanceOutputsInput' is set
      if (listServiceInstanceOutputsInput === undefined || listServiceInstanceOutputsInput === null) {
        throw new Error("Missing the required parameter 'listServiceInstanceOutputsInput' when calling listServiceInstanceOutputs");
      }

      let pathParams = {
      };
      let queryParams = {
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListServiceInstanceOutputsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListServiceInstanceOutputs', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listServiceInstanceProvisionedResources operation.
     * @callback module:api/DefaultApi~listServiceInstanceProvisionedResourcesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListServiceInstanceProvisionedResourcesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List provisioned resources for a service instance with details.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListServiceInstanceProvisionedResourcesInput} listServiceInstanceProvisionedResourcesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listServiceInstanceProvisionedResourcesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListServiceInstanceProvisionedResourcesOutput}
     */
    listServiceInstanceProvisionedResources(xAmzTarget, listServiceInstanceProvisionedResourcesInput, opts, callback) {
      opts = opts || {};
      let postBody = listServiceInstanceProvisionedResourcesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listServiceInstanceProvisionedResources");
      }
      // verify the required parameter 'listServiceInstanceProvisionedResourcesInput' is set
      if (listServiceInstanceProvisionedResourcesInput === undefined || listServiceInstanceProvisionedResourcesInput === null) {
        throw new Error("Missing the required parameter 'listServiceInstanceProvisionedResourcesInput' when calling listServiceInstanceProvisionedResources");
      }

      let pathParams = {
      };
      let queryParams = {
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListServiceInstanceProvisionedResourcesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListServiceInstanceProvisionedResources', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listServiceInstances operation.
     * @callback module:api/DefaultApi~listServiceInstancesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListServiceInstancesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List service instances with summary data. This action lists service instances of all services in the Amazon Web Services account.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListServiceInstancesInput} listServiceInstancesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listServiceInstancesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListServiceInstancesOutput}
     */
    listServiceInstances(xAmzTarget, listServiceInstancesInput, opts, callback) {
      opts = opts || {};
      let postBody = listServiceInstancesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listServiceInstances");
      }
      // verify the required parameter 'listServiceInstancesInput' is set
      if (listServiceInstancesInput === undefined || listServiceInstancesInput === null) {
        throw new Error("Missing the required parameter 'listServiceInstancesInput' when calling listServiceInstances");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListServiceInstancesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListServiceInstances', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listServicePipelineOutputs operation.
     * @callback module:api/DefaultApi~listServicePipelineOutputsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListServicePipelineOutputsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a list of service pipeline Infrastructure as Code (IaC) outputs.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListServicePipelineOutputsInput} listServicePipelineOutputsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listServicePipelineOutputsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListServicePipelineOutputsOutput}
     */
    listServicePipelineOutputs(xAmzTarget, listServicePipelineOutputsInput, opts, callback) {
      opts = opts || {};
      let postBody = listServicePipelineOutputsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listServicePipelineOutputs");
      }
      // verify the required parameter 'listServicePipelineOutputsInput' is set
      if (listServicePipelineOutputsInput === undefined || listServicePipelineOutputsInput === null) {
        throw new Error("Missing the required parameter 'listServicePipelineOutputsInput' when calling listServicePipelineOutputs");
      }

      let pathParams = {
      };
      let queryParams = {
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListServicePipelineOutputsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListServicePipelineOutputs', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listServicePipelineProvisionedResources operation.
     * @callback module:api/DefaultApi~listServicePipelineProvisionedResourcesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListServicePipelineProvisionedResourcesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List provisioned resources for a service and pipeline with details.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListServicePipelineProvisionedResourcesInput} listServicePipelineProvisionedResourcesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listServicePipelineProvisionedResourcesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListServicePipelineProvisionedResourcesOutput}
     */
    listServicePipelineProvisionedResources(xAmzTarget, listServicePipelineProvisionedResourcesInput, opts, callback) {
      opts = opts || {};
      let postBody = listServicePipelineProvisionedResourcesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listServicePipelineProvisionedResources");
      }
      // verify the required parameter 'listServicePipelineProvisionedResourcesInput' is set
      if (listServicePipelineProvisionedResourcesInput === undefined || listServicePipelineProvisionedResourcesInput === null) {
        throw new Error("Missing the required parameter 'listServicePipelineProvisionedResourcesInput' when calling listServicePipelineProvisionedResources");
      }

      let pathParams = {
      };
      let queryParams = {
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListServicePipelineProvisionedResourcesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListServicePipelineProvisionedResources', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listServiceTemplateVersions operation.
     * @callback module:api/DefaultApi~listServiceTemplateVersionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListServiceTemplateVersionsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List major or minor versions of a service template with detail data.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListServiceTemplateVersionsInput} listServiceTemplateVersionsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listServiceTemplateVersionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListServiceTemplateVersionsOutput}
     */
    listServiceTemplateVersions(xAmzTarget, listServiceTemplateVersionsInput, opts, callback) {
      opts = opts || {};
      let postBody = listServiceTemplateVersionsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listServiceTemplateVersions");
      }
      // verify the required parameter 'listServiceTemplateVersionsInput' is set
      if (listServiceTemplateVersionsInput === undefined || listServiceTemplateVersionsInput === null) {
        throw new Error("Missing the required parameter 'listServiceTemplateVersionsInput' when calling listServiceTemplateVersions");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListServiceTemplateVersionsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListServiceTemplateVersions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listServiceTemplates operation.
     * @callback module:api/DefaultApi~listServiceTemplatesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListServiceTemplatesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List service templates with detail data.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListServiceTemplatesInput} listServiceTemplatesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listServiceTemplatesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListServiceTemplatesOutput}
     */
    listServiceTemplates(xAmzTarget, listServiceTemplatesInput, opts, callback) {
      opts = opts || {};
      let postBody = listServiceTemplatesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listServiceTemplates");
      }
      // verify the required parameter 'listServiceTemplatesInput' is set
      if (listServiceTemplatesInput === undefined || listServiceTemplatesInput === null) {
        throw new Error("Missing the required parameter 'listServiceTemplatesInput' when calling listServiceTemplates");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListServiceTemplatesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListServiceTemplates', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listServices operation.
     * @callback module:api/DefaultApi~listServicesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListServicesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List services with summaries of detail data.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListServicesInput} listServicesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listServicesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListServicesOutput}
     */
    listServices(xAmzTarget, listServicesInput, opts, callback) {
      opts = opts || {};
      let postBody = listServicesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listServices");
      }
      // verify the required parameter 'listServicesInput' is set
      if (listServicesInput === undefined || listServicesInput === null) {
        throw new Error("Missing the required parameter 'listServicesInput' when calling listServices");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListServicesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListServices', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listTagsForResource operation.
     * @callback module:api/DefaultApi~listTagsForResourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListTagsForResourceOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List tags for a resource. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListTagsForResourceInput} listTagsForResourceInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listTagsForResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListTagsForResourceOutput}
     */
    listTagsForResource(xAmzTarget, listTagsForResourceInput, opts, callback) {
      opts = opts || {};
      let postBody = listTagsForResourceInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listTagsForResource");
      }
      // verify the required parameter 'listTagsForResourceInput' is set
      if (listTagsForResourceInput === undefined || listTagsForResourceInput === null) {
        throw new Error("Missing the required parameter 'listTagsForResourceInput' when calling listTagsForResource");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListTagsForResourceOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.ListTagsForResource', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the notifyResourceDeploymentStatusChange operation.
     * @callback module:api/DefaultApi~notifyResourceDeploymentStatusChangeCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Notify Proton of status changes to a provisioned resource when you use self-managed provisioning.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self\">Self-managed provisioning</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/NotifyResourceDeploymentStatusChangeInput} notifyResourceDeploymentStatusChangeInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~notifyResourceDeploymentStatusChangeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    notifyResourceDeploymentStatusChange(xAmzTarget, notifyResourceDeploymentStatusChangeInput, opts, callback) {
      opts = opts || {};
      let postBody = notifyResourceDeploymentStatusChangeInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling notifyResourceDeploymentStatusChange");
      }
      // verify the required parameter 'notifyResourceDeploymentStatusChangeInput' is set
      if (notifyResourceDeploymentStatusChangeInput === undefined || notifyResourceDeploymentStatusChangeInput === null) {
        throw new Error("Missing the required parameter 'notifyResourceDeploymentStatusChangeInput' when calling notifyResourceDeploymentStatusChange");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.NotifyResourceDeploymentStatusChange', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the rejectEnvironmentAccountConnection operation.
     * @callback module:api/DefaultApi~rejectEnvironmentAccountConnectionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RejectEnvironmentAccountConnectionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>In a management account, reject an environment account connection from another environment account.</p> <p>After you reject an environment account connection request, you <i>can't</i> accept or use the rejected environment account connection.</p> <p>You <i>can’t</i> reject an environment account connection that's connected to an environment.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/RejectEnvironmentAccountConnectionInput} rejectEnvironmentAccountConnectionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~rejectEnvironmentAccountConnectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RejectEnvironmentAccountConnectionOutput}
     */
    rejectEnvironmentAccountConnection(xAmzTarget, rejectEnvironmentAccountConnectionInput, opts, callback) {
      opts = opts || {};
      let postBody = rejectEnvironmentAccountConnectionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling rejectEnvironmentAccountConnection");
      }
      // verify the required parameter 'rejectEnvironmentAccountConnectionInput' is set
      if (rejectEnvironmentAccountConnectionInput === undefined || rejectEnvironmentAccountConnectionInput === null) {
        throw new Error("Missing the required parameter 'rejectEnvironmentAccountConnectionInput' when calling rejectEnvironmentAccountConnection");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = RejectEnvironmentAccountConnectionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.RejectEnvironmentAccountConnection', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the tagResource operation.
     * @callback module:api/DefaultApi~tagResourceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Tag a resource. A tag is a key-value pair of metadata that you associate with an Proton resource.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/TagResourceInput} tagResourceInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~tagResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    tagResource(xAmzTarget, tagResourceInput, opts, callback) {
      opts = opts || {};
      let postBody = tagResourceInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling tagResource");
      }
      // verify the required parameter 'tagResourceInput' is set
      if (tagResourceInput === undefined || tagResourceInput === null) {
        throw new Error("Missing the required parameter 'tagResourceInput' when calling tagResource");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.TagResource', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the untagResource operation.
     * @callback module:api/DefaultApi~untagResourceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Remove a customer tag from a resource. A tag is a key-value pair of metadata associated with an Proton resource.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UntagResourceInput} untagResourceInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~untagResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    untagResource(xAmzTarget, untagResourceInput, opts, callback) {
      opts = opts || {};
      let postBody = untagResourceInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling untagResource");
      }
      // verify the required parameter 'untagResourceInput' is set
      if (untagResourceInput === undefined || untagResourceInput === null) {
        throw new Error("Missing the required parameter 'untagResourceInput' when calling untagResource");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UntagResource', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateAccountSettings operation.
     * @callback module:api/DefaultApi~updateAccountSettingsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateAccountSettingsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update Proton settings that are used for multiple services in the Amazon Web Services account.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateAccountSettingsInput} updateAccountSettingsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateAccountSettingsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateAccountSettingsOutput}
     */
    updateAccountSettings(xAmzTarget, updateAccountSettingsInput, opts, callback) {
      opts = opts || {};
      let postBody = updateAccountSettingsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateAccountSettings");
      }
      // verify the required parameter 'updateAccountSettingsInput' is set
      if (updateAccountSettingsInput === undefined || updateAccountSettingsInput === null) {
        throw new Error("Missing the required parameter 'updateAccountSettingsInput' when calling updateAccountSettings");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateAccountSettingsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UpdateAccountSettings', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateComponent operation.
     * @callback module:api/DefaultApi~updateComponentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateComponentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Update a component.</p> <p>There are a few modes for updating a component. The <code>deploymentType</code> field defines the mode.</p> <note> <p>You can't update a component while its deployment status, or the deployment status of a service instance attached to it, is <code>IN_PROGRESS</code>.</p> </note> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateComponentInput} updateComponentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateComponentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateComponentOutput}
     */
    updateComponent(xAmzTarget, updateComponentInput, opts, callback) {
      opts = opts || {};
      let postBody = updateComponentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateComponent");
      }
      // verify the required parameter 'updateComponentInput' is set
      if (updateComponentInput === undefined || updateComponentInput === null) {
        throw new Error("Missing the required parameter 'updateComponentInput' when calling updateComponent");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateComponentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UpdateComponent', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateEnvironment operation.
     * @callback module:api/DefaultApi~updateEnvironmentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateEnvironmentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Update an environment.</p> <p>If the environment is associated with an environment account connection, <i>don't</i> update or include the <code>protonServiceRoleArn</code> and <code>provisioningRepository</code> parameter to update or connect to an environment account connection.</p> <p>You can only update to a new environment account connection if that connection was created in the same environment account that the current environment account connection was created in. The account connection must also be associated with the current environment.</p> <p>If the environment <i>isn't</i> associated with an environment account connection, <i>don't</i> update or include the <code>environmentAccountConnectionId</code> parameter. You <i>can't</i> update or connect the environment to an environment account connection if it <i>isn't</i> already associated with an environment connection.</p> <p>You can update either the <code>environmentAccountConnectionId</code> or <code>protonServiceRoleArn</code> parameter and value. You can’t update both.</p> <p>If the environment was configured for Amazon Web Services-managed provisioning, omit the <code>provisioningRepository</code> parameter.</p> <p>If the environment was configured for self-managed provisioning, specify the <code>provisioningRepository</code> parameter and omit the <code>protonServiceRoleArn</code> and <code>environmentAccountConnectionId</code> parameters.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html\">Environments</a> and <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html\">Provisioning methods</a> in the <i>Proton User Guide</i>.</p> <p>There are four modes for updating an environment. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include minor or major version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can also specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateEnvironmentInput} updateEnvironmentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateEnvironmentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateEnvironmentOutput}
     */
    updateEnvironment(xAmzTarget, updateEnvironmentInput, opts, callback) {
      opts = opts || {};
      let postBody = updateEnvironmentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateEnvironment");
      }
      // verify the required parameter 'updateEnvironmentInput' is set
      if (updateEnvironmentInput === undefined || updateEnvironmentInput === null) {
        throw new Error("Missing the required parameter 'updateEnvironmentInput' when calling updateEnvironment");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateEnvironmentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UpdateEnvironment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateEnvironmentAccountConnection operation.
     * @callback module:api/DefaultApi~updateEnvironmentAccountConnectionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateEnvironmentAccountConnectionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>In an environment account, update an environment account connection to use a new IAM role.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateEnvironmentAccountConnectionInput} updateEnvironmentAccountConnectionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateEnvironmentAccountConnectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateEnvironmentAccountConnectionOutput}
     */
    updateEnvironmentAccountConnection(xAmzTarget, updateEnvironmentAccountConnectionInput, opts, callback) {
      opts = opts || {};
      let postBody = updateEnvironmentAccountConnectionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateEnvironmentAccountConnection");
      }
      // verify the required parameter 'updateEnvironmentAccountConnectionInput' is set
      if (updateEnvironmentAccountConnectionInput === undefined || updateEnvironmentAccountConnectionInput === null) {
        throw new Error("Missing the required parameter 'updateEnvironmentAccountConnectionInput' when calling updateEnvironmentAccountConnection");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateEnvironmentAccountConnectionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UpdateEnvironmentAccountConnection', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateEnvironmentTemplate operation.
     * @callback module:api/DefaultApi~updateEnvironmentTemplateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateEnvironmentTemplateOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an environment template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateEnvironmentTemplateInput} updateEnvironmentTemplateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateEnvironmentTemplateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateEnvironmentTemplateOutput}
     */
    updateEnvironmentTemplate(xAmzTarget, updateEnvironmentTemplateInput, opts, callback) {
      opts = opts || {};
      let postBody = updateEnvironmentTemplateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateEnvironmentTemplate");
      }
      // verify the required parameter 'updateEnvironmentTemplateInput' is set
      if (updateEnvironmentTemplateInput === undefined || updateEnvironmentTemplateInput === null) {
        throw new Error("Missing the required parameter 'updateEnvironmentTemplateInput' when calling updateEnvironmentTemplate");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateEnvironmentTemplateOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UpdateEnvironmentTemplate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateEnvironmentTemplateVersion operation.
     * @callback module:api/DefaultApi~updateEnvironmentTemplateVersionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateEnvironmentTemplateVersionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a major or minor version of an environment template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateEnvironmentTemplateVersionInput} updateEnvironmentTemplateVersionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateEnvironmentTemplateVersionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateEnvironmentTemplateVersionOutput}
     */
    updateEnvironmentTemplateVersion(xAmzTarget, updateEnvironmentTemplateVersionInput, opts, callback) {
      opts = opts || {};
      let postBody = updateEnvironmentTemplateVersionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateEnvironmentTemplateVersion");
      }
      // verify the required parameter 'updateEnvironmentTemplateVersionInput' is set
      if (updateEnvironmentTemplateVersionInput === undefined || updateEnvironmentTemplateVersionInput === null) {
        throw new Error("Missing the required parameter 'updateEnvironmentTemplateVersionInput' when calling updateEnvironmentTemplateVersion");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateEnvironmentTemplateVersionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UpdateEnvironmentTemplateVersion', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateService operation.
     * @callback module:api/DefaultApi~updateServiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateServiceOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Edit a service description or use a spec to add and delete service instances.</p> <note> <p>Existing service instances and the service pipeline <i>can't</i> be edited using this API. They can only be deleted.</p> </note> <p>Use the <code>description</code> parameter to modify the description.</p> <p>Edit the <code>spec</code> parameter to add or delete instances.</p> <note> <p>You can't delete a service instance (remove it from the spec) if it has an attached component.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateServiceInput} updateServiceInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateServiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateServiceOutput}
     */
    updateService(xAmzTarget, updateServiceInput, opts, callback) {
      opts = opts || {};
      let postBody = updateServiceInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateService");
      }
      // verify the required parameter 'updateServiceInput' is set
      if (updateServiceInput === undefined || updateServiceInput === null) {
        throw new Error("Missing the required parameter 'updateServiceInput' when calling updateService");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateServiceOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UpdateService', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateServiceInstance operation.
     * @callback module:api/DefaultApi~updateServiceInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateServiceInstanceOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Update a service instance.</p> <p>There are a few modes for updating a service instance. The <code>deploymentType</code> field defines the mode.</p> <note> <p>You can't update a service instance while its deployment status, or the deployment status of a component attached to it, is <code>IN_PROGRESS</code>.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateServiceInstanceInput} updateServiceInstanceInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateServiceInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateServiceInstanceOutput}
     */
    updateServiceInstance(xAmzTarget, updateServiceInstanceInput, opts, callback) {
      opts = opts || {};
      let postBody = updateServiceInstanceInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateServiceInstance");
      }
      // verify the required parameter 'updateServiceInstanceInput' is set
      if (updateServiceInstanceInput === undefined || updateServiceInstanceInput === null) {
        throw new Error("Missing the required parameter 'updateServiceInstanceInput' when calling updateServiceInstance");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateServiceInstanceOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UpdateServiceInstance', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateServicePipeline operation.
     * @callback module:api/DefaultApi~updateServicePipelineCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateServicePipelineOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Update the service pipeline.</p> <p>There are four modes for updating a service pipeline. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateServicePipelineInput} updateServicePipelineInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateServicePipelineCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateServicePipelineOutput}
     */
    updateServicePipeline(xAmzTarget, updateServicePipelineInput, opts, callback) {
      opts = opts || {};
      let postBody = updateServicePipelineInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateServicePipeline");
      }
      // verify the required parameter 'updateServicePipelineInput' is set
      if (updateServicePipelineInput === undefined || updateServicePipelineInput === null) {
        throw new Error("Missing the required parameter 'updateServicePipelineInput' when calling updateServicePipeline");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateServicePipelineOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UpdateServicePipeline', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateServiceSyncBlocker operation.
     * @callback module:api/DefaultApi~updateServiceSyncBlockerCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateServiceSyncBlockerOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the service sync blocker by resolving it.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateServiceSyncBlockerInput} updateServiceSyncBlockerInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateServiceSyncBlockerCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateServiceSyncBlockerOutput}
     */
    updateServiceSyncBlocker(xAmzTarget, updateServiceSyncBlockerInput, opts, callback) {
      opts = opts || {};
      let postBody = updateServiceSyncBlockerInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateServiceSyncBlocker");
      }
      // verify the required parameter 'updateServiceSyncBlockerInput' is set
      if (updateServiceSyncBlockerInput === undefined || updateServiceSyncBlockerInput === null) {
        throw new Error("Missing the required parameter 'updateServiceSyncBlockerInput' when calling updateServiceSyncBlocker");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateServiceSyncBlockerOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UpdateServiceSyncBlocker', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateServiceSyncConfig operation.
     * @callback module:api/DefaultApi~updateServiceSyncConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateServiceSyncConfigOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the Proton Ops config file.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateServiceSyncConfigInput} updateServiceSyncConfigInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateServiceSyncConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateServiceSyncConfigOutput}
     */
    updateServiceSyncConfig(xAmzTarget, updateServiceSyncConfigInput, opts, callback) {
      opts = opts || {};
      let postBody = updateServiceSyncConfigInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateServiceSyncConfig");
      }
      // verify the required parameter 'updateServiceSyncConfigInput' is set
      if (updateServiceSyncConfigInput === undefined || updateServiceSyncConfigInput === null) {
        throw new Error("Missing the required parameter 'updateServiceSyncConfigInput' when calling updateServiceSyncConfig");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateServiceSyncConfigOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UpdateServiceSyncConfig', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateServiceTemplate operation.
     * @callback module:api/DefaultApi~updateServiceTemplateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateServiceTemplateOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a service template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateServiceTemplateInput} updateServiceTemplateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateServiceTemplateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateServiceTemplateOutput}
     */
    updateServiceTemplate(xAmzTarget, updateServiceTemplateInput, opts, callback) {
      opts = opts || {};
      let postBody = updateServiceTemplateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateServiceTemplate");
      }
      // verify the required parameter 'updateServiceTemplateInput' is set
      if (updateServiceTemplateInput === undefined || updateServiceTemplateInput === null) {
        throw new Error("Missing the required parameter 'updateServiceTemplateInput' when calling updateServiceTemplate");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateServiceTemplateOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UpdateServiceTemplate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateServiceTemplateVersion operation.
     * @callback module:api/DefaultApi~updateServiceTemplateVersionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateServiceTemplateVersionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a major or minor version of a service template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateServiceTemplateVersionInput} updateServiceTemplateVersionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateServiceTemplateVersionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateServiceTemplateVersionOutput}
     */
    updateServiceTemplateVersion(xAmzTarget, updateServiceTemplateVersionInput, opts, callback) {
      opts = opts || {};
      let postBody = updateServiceTemplateVersionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateServiceTemplateVersion");
      }
      // verify the required parameter 'updateServiceTemplateVersionInput' is set
      if (updateServiceTemplateVersionInput === undefined || updateServiceTemplateVersionInput === null) {
        throw new Error("Missing the required parameter 'updateServiceTemplateVersionInput' when calling updateServiceTemplateVersion");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateServiceTemplateVersionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UpdateServiceTemplateVersion', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateTemplateSyncConfig operation.
     * @callback module:api/DefaultApi~updateTemplateSyncConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateTemplateSyncConfigOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update template sync configuration parameters, except for the <code>templateName</code> and <code>templateType</code>. Repository details (branch, name, and provider) should be of a linked repository. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateTemplateSyncConfigInput} updateTemplateSyncConfigInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateTemplateSyncConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateTemplateSyncConfigOutput}
     */
    updateTemplateSyncConfig(xAmzTarget, updateTemplateSyncConfigInput, opts, callback) {
      opts = opts || {};
      let postBody = updateTemplateSyncConfigInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateTemplateSyncConfig");
      }
      // verify the required parameter 'updateTemplateSyncConfigInput' is set
      if (updateTemplateSyncConfigInput === undefined || updateTemplateSyncConfigInput === null) {
        throw new Error("Missing the required parameter 'updateTemplateSyncConfigInput' when calling updateTemplateSyncConfig");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateTemplateSyncConfigOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=AwsProton20200720.UpdateTemplateSyncConfig', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
