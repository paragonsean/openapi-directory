/**
 * AWS CodePipeline
 * <fullname>CodePipeline</fullname> <p> <b>Overview</b> </p> <p>This is the CodePipeline API Reference. This guide provides descriptions of the actions and data types for CodePipeline. Some functionality for your pipeline can only be configured through the API. For more information, see the <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html\">CodePipeline User Guide</a>.</p> <p>You can use the CodePipeline API to work with pipelines, stages, actions, and transitions.</p> <p> <i>Pipelines</i> are models of automated release processes. Each pipeline is uniquely named, and consists of stages, actions, and transitions. </p> <p>You can work with pipelines by calling:</p> <ul> <li> <p> <a>CreatePipeline</a>, which creates a uniquely named pipeline.</p> </li> <li> <p> <a>DeletePipeline</a>, which deletes the specified pipeline.</p> </li> <li> <p> <a>GetPipeline</a>, which returns information about the pipeline structure and pipeline metadata, including the pipeline Amazon Resource Name (ARN).</p> </li> <li> <p> <a>GetPipelineExecution</a>, which returns information about a specific execution of a pipeline.</p> </li> <li> <p> <a>GetPipelineState</a>, which returns information about the current state of the stages and actions of a pipeline.</p> </li> <li> <p> <a>ListActionExecutions</a>, which returns action-level details for past executions. The details include full stage and action-level details, including individual action duration, status, any errors that occurred during the execution, and input and output artifact location details.</p> </li> <li> <p> <a>ListPipelines</a>, which gets a summary of all of the pipelines associated with your account.</p> </li> <li> <p> <a>ListPipelineExecutions</a>, which gets a summary of the most recent executions for a pipeline.</p> </li> <li> <p> <a>StartPipelineExecution</a>, which runs the most recent revision of an artifact through the pipeline.</p> </li> <li> <p> <a>StopPipelineExecution</a>, which stops the specified pipeline execution from continuing through the pipeline.</p> </li> <li> <p> <a>UpdatePipeline</a>, which updates a pipeline with edits or changes to the structure of the pipeline.</p> </li> </ul> <p>Pipelines include <i>stages</i>. Each stage contains one or more actions that must complete before the next stage begins. A stage results in success or failure. If a stage fails, the pipeline stops at that stage and remains stopped until either a new version of an artifact appears in the source location, or a user takes action to rerun the most recent artifact through the pipeline. You can call <a>GetPipelineState</a>, which displays the status of a pipeline, including the status of stages in the pipeline, or <a>GetPipeline</a>, which returns the entire structure of the pipeline, including the stages of that pipeline. For more information about the structure of stages and actions, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-structure.html\">CodePipeline Pipeline Structure Reference</a>.</p> <p>Pipeline stages include <i>actions</i> that are categorized into categories such as source or build actions performed in a stage of a pipeline. For example, you can use a source action to import artifacts into a pipeline from a source such as Amazon S3. Like stages, you do not work with actions directly in most cases, but you do define and interact with actions when working with pipeline operations such as <a>CreatePipeline</a> and <a>GetPipelineState</a>. Valid action categories are:</p> <ul> <li> <p>Source</p> </li> <li> <p>Build</p> </li> <li> <p>Test</p> </li> <li> <p>Deploy</p> </li> <li> <p>Approval</p> </li> <li> <p>Invoke</p> </li> </ul> <p>Pipelines also include <i>transitions</i>, which allow the transition of artifacts from one stage to the next in a pipeline after the actions in one stage complete.</p> <p>You can work with transitions by calling:</p> <ul> <li> <p> <a>DisableStageTransition</a>, which prevents artifacts from transitioning to the next stage in a pipeline.</p> </li> <li> <p> <a>EnableStageTransition</a>, which enables transition of artifacts between stages in a pipeline. </p> </li> </ul> <p> <b>Using the API to integrate with CodePipeline</b> </p> <p>For third-party integrators or developers who want to create their own integrations with CodePipeline, the expected sequence varies from the standard API user. To integrate with CodePipeline, developers need to work with the following items:</p> <p> <b>Jobs</b>, which are instances of an action. For example, a job for a source action might import a revision of an artifact from a source. </p> <p>You can work with jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetJobDetails</a>, which returns the details of a job.</p> </li> <li> <p> <a>PollForJobs</a>, which determines whether there are any jobs to act on.</p> </li> <li> <p> <a>PutJobFailureResult</a>, which provides details of a job failure. </p> </li> <li> <p> <a>PutJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul> <p> <b>Third party jobs</b>, which are instances of an action created by a partner action and integrated into CodePipeline. Partner actions are created by members of the Amazon Web Services Partner Network.</p> <p>You can work with third party jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeThirdPartyJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetThirdPartyJobDetails</a>, which requests the details of a job for a partner action.</p> </li> <li> <p> <a>PollForThirdPartyJobs</a>, which determines whether there are any jobs to act on. </p> </li> <li> <p> <a>PutThirdPartyJobFailureResult</a>, which provides details of a job failure.</p> </li> <li> <p> <a>PutThirdPartyJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2015-07-09
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AcknowledgeJobInput from '../model/AcknowledgeJobInput';
import AcknowledgeJobOutput from '../model/AcknowledgeJobOutput';
import AcknowledgeThirdPartyJobInput from '../model/AcknowledgeThirdPartyJobInput';
import AcknowledgeThirdPartyJobOutput from '../model/AcknowledgeThirdPartyJobOutput';
import CreateCustomActionTypeInput from '../model/CreateCustomActionTypeInput';
import CreateCustomActionTypeOutput from '../model/CreateCustomActionTypeOutput';
import CreatePipelineInput from '../model/CreatePipelineInput';
import CreatePipelineOutput from '../model/CreatePipelineOutput';
import DeleteCustomActionTypeInput from '../model/DeleteCustomActionTypeInput';
import DeletePipelineInput from '../model/DeletePipelineInput';
import DeleteWebhookInput from '../model/DeleteWebhookInput';
import DeregisterWebhookWithThirdPartyInput from '../model/DeregisterWebhookWithThirdPartyInput';
import DisableStageTransitionInput from '../model/DisableStageTransitionInput';
import EnableStageTransitionInput from '../model/EnableStageTransitionInput';
import GetActionTypeInput from '../model/GetActionTypeInput';
import GetActionTypeOutput from '../model/GetActionTypeOutput';
import GetJobDetailsInput from '../model/GetJobDetailsInput';
import GetJobDetailsOutput from '../model/GetJobDetailsOutput';
import GetPipelineExecutionInput from '../model/GetPipelineExecutionInput';
import GetPipelineExecutionOutput from '../model/GetPipelineExecutionOutput';
import GetPipelineInput from '../model/GetPipelineInput';
import GetPipelineOutput from '../model/GetPipelineOutput';
import GetPipelineStateInput from '../model/GetPipelineStateInput';
import GetPipelineStateOutput from '../model/GetPipelineStateOutput';
import GetThirdPartyJobDetailsInput from '../model/GetThirdPartyJobDetailsInput';
import GetThirdPartyJobDetailsOutput from '../model/GetThirdPartyJobDetailsOutput';
import ListActionExecutionsInput from '../model/ListActionExecutionsInput';
import ListActionExecutionsOutput from '../model/ListActionExecutionsOutput';
import ListActionTypesInput from '../model/ListActionTypesInput';
import ListActionTypesOutput from '../model/ListActionTypesOutput';
import ListPipelineExecutionsInput from '../model/ListPipelineExecutionsInput';
import ListPipelineExecutionsOutput from '../model/ListPipelineExecutionsOutput';
import ListPipelinesInput from '../model/ListPipelinesInput';
import ListPipelinesOutput from '../model/ListPipelinesOutput';
import ListTagsForResourceInput from '../model/ListTagsForResourceInput';
import ListTagsForResourceOutput from '../model/ListTagsForResourceOutput';
import ListWebhooksInput from '../model/ListWebhooksInput';
import ListWebhooksOutput from '../model/ListWebhooksOutput';
import PollForJobsInput from '../model/PollForJobsInput';
import PollForJobsOutput from '../model/PollForJobsOutput';
import PollForThirdPartyJobsInput from '../model/PollForThirdPartyJobsInput';
import PollForThirdPartyJobsOutput from '../model/PollForThirdPartyJobsOutput';
import PutActionRevisionInput from '../model/PutActionRevisionInput';
import PutActionRevisionOutput from '../model/PutActionRevisionOutput';
import PutApprovalResultInput from '../model/PutApprovalResultInput';
import PutApprovalResultOutput from '../model/PutApprovalResultOutput';
import PutJobFailureResultInput from '../model/PutJobFailureResultInput';
import PutJobSuccessResultInput from '../model/PutJobSuccessResultInput';
import PutThirdPartyJobFailureResultInput from '../model/PutThirdPartyJobFailureResultInput';
import PutThirdPartyJobSuccessResultInput from '../model/PutThirdPartyJobSuccessResultInput';
import PutWebhookInput from '../model/PutWebhookInput';
import PutWebhookOutput from '../model/PutWebhookOutput';
import RegisterWebhookWithThirdPartyInput from '../model/RegisterWebhookWithThirdPartyInput';
import RetryStageExecutionInput from '../model/RetryStageExecutionInput';
import RetryStageExecutionOutput from '../model/RetryStageExecutionOutput';
import StartPipelineExecutionInput from '../model/StartPipelineExecutionInput';
import StartPipelineExecutionOutput from '../model/StartPipelineExecutionOutput';
import StopPipelineExecutionInput from '../model/StopPipelineExecutionInput';
import StopPipelineExecutionOutput from '../model/StopPipelineExecutionOutput';
import TagResourceInput from '../model/TagResourceInput';
import UntagResourceInput from '../model/UntagResourceInput';
import UpdateActionTypeInput from '../model/UpdateActionTypeInput';
import UpdatePipelineInput from '../model/UpdatePipelineInput';
import UpdatePipelineOutput from '../model/UpdatePipelineOutput';

/**
* Default service.
* @module api/DefaultApi
* @version 2015-07-09
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
     * Callback function to receive the result of the acknowledgeJob operation.
     * @callback module:api/DefaultApi~acknowledgeJobCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AcknowledgeJobOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about a specified job and whether that job has been received by the job worker. Used for custom actions only.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/AcknowledgeJobInput} acknowledgeJobInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~acknowledgeJobCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AcknowledgeJobOutput}
     */
    acknowledgeJob(xAmzTarget, acknowledgeJobInput, opts, callback) {
      opts = opts || {};
      let postBody = acknowledgeJobInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling acknowledgeJob");
      }
      // verify the required parameter 'acknowledgeJobInput' is set
      if (acknowledgeJobInput === undefined || acknowledgeJobInput === null) {
        throw new Error("Missing the required parameter 'acknowledgeJobInput' when calling acknowledgeJob");
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
      let returnType = AcknowledgeJobOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.AcknowledgeJob', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the acknowledgeThirdPartyJob operation.
     * @callback module:api/DefaultApi~acknowledgeThirdPartyJobCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AcknowledgeThirdPartyJobOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Confirms a job worker has received the specified job. Used for partner actions only.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/AcknowledgeThirdPartyJobInput} acknowledgeThirdPartyJobInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~acknowledgeThirdPartyJobCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AcknowledgeThirdPartyJobOutput}
     */
    acknowledgeThirdPartyJob(xAmzTarget, acknowledgeThirdPartyJobInput, opts, callback) {
      opts = opts || {};
      let postBody = acknowledgeThirdPartyJobInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling acknowledgeThirdPartyJob");
      }
      // verify the required parameter 'acknowledgeThirdPartyJobInput' is set
      if (acknowledgeThirdPartyJobInput === undefined || acknowledgeThirdPartyJobInput === null) {
        throw new Error("Missing the required parameter 'acknowledgeThirdPartyJobInput' when calling acknowledgeThirdPartyJob");
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
      let returnType = AcknowledgeThirdPartyJobOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.AcknowledgeThirdPartyJob', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createCustomActionType operation.
     * @callback module:api/DefaultApi~createCustomActionTypeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateCustomActionTypeOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a new custom action that can be used in all pipelines associated with the Amazon Web Services account. Only used for custom actions.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateCustomActionTypeInput} createCustomActionTypeInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createCustomActionTypeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateCustomActionTypeOutput}
     */
    createCustomActionType(xAmzTarget, createCustomActionTypeInput, opts, callback) {
      opts = opts || {};
      let postBody = createCustomActionTypeInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createCustomActionType");
      }
      // verify the required parameter 'createCustomActionTypeInput' is set
      if (createCustomActionTypeInput === undefined || createCustomActionTypeInput === null) {
        throw new Error("Missing the required parameter 'createCustomActionTypeInput' when calling createCustomActionType");
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
      let returnType = CreateCustomActionTypeOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.CreateCustomActionType', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createPipeline operation.
     * @callback module:api/DefaultApi~createPipelineCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreatePipelineOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Creates a pipeline.</p> <note> <p>In the pipeline structure, you must include either <code>artifactStore</code> or <code>artifactStores</code> in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use <code>artifactStores</code>.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreatePipelineInput} createPipelineInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createPipelineCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreatePipelineOutput}
     */
    createPipeline(xAmzTarget, createPipelineInput, opts, callback) {
      opts = opts || {};
      let postBody = createPipelineInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createPipeline");
      }
      // verify the required parameter 'createPipelineInput' is set
      if (createPipelineInput === undefined || createPipelineInput === null) {
        throw new Error("Missing the required parameter 'createPipelineInput' when calling createPipeline");
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
      let returnType = CreatePipelineOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.CreatePipeline', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteCustomActionType operation.
     * @callback module:api/DefaultApi~deleteCustomActionTypeCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Marks a custom action as deleted. <code>PollForJobs</code> for the custom action fails after the action is marked for deletion. Used for custom actions only.</p> <important> <p>To re-create a custom action after it has been deleted you must use a string in the version field that has never been used before. This string can be an incremented version number, for example. To restore a deleted custom action, use a JSON file that is identical to the deleted action, including the original string in the version field.</p> </important>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteCustomActionTypeInput} deleteCustomActionTypeInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteCustomActionTypeCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteCustomActionType(xAmzTarget, deleteCustomActionTypeInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteCustomActionTypeInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteCustomActionType");
      }
      // verify the required parameter 'deleteCustomActionTypeInput' is set
      if (deleteCustomActionTypeInput === undefined || deleteCustomActionTypeInput === null) {
        throw new Error("Missing the required parameter 'deleteCustomActionTypeInput' when calling deleteCustomActionType");
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
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.DeleteCustomActionType', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deletePipeline operation.
     * @callback module:api/DefaultApi~deletePipelineCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes the specified pipeline.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeletePipelineInput} deletePipelineInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deletePipelineCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deletePipeline(xAmzTarget, deletePipelineInput, opts, callback) {
      opts = opts || {};
      let postBody = deletePipelineInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deletePipeline");
      }
      // verify the required parameter 'deletePipelineInput' is set
      if (deletePipelineInput === undefined || deletePipelineInput === null) {
        throw new Error("Missing the required parameter 'deletePipelineInput' when calling deletePipeline");
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
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.DeletePipeline', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteWebhook operation.
     * @callback module:api/DefaultApi~deleteWebhookCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes a previously created webhook by name. Deleting the webhook stops CodePipeline from starting a pipeline every time an external event occurs. The API returns successfully when trying to delete a webhook that is already deleted. If a deleted webhook is re-created by calling PutWebhook with the same name, it will have a different URL.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteWebhookInput} deleteWebhookInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteWebhookCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteWebhook(xAmzTarget, deleteWebhookInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteWebhookInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteWebhook");
      }
      // verify the required parameter 'deleteWebhookInput' is set
      if (deleteWebhookInput === undefined || deleteWebhookInput === null) {
        throw new Error("Missing the required parameter 'deleteWebhookInput' when calling deleteWebhook");
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
        '/#X-Amz-Target=CodePipeline_20150709.DeleteWebhook', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deregisterWebhookWithThirdParty operation.
     * @callback module:api/DefaultApi~deregisterWebhookWithThirdPartyCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Removes the connection between the webhook that was created by CodePipeline and the external tool with events to be detected. Currently supported only for webhooks that target an action type of GitHub.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeregisterWebhookWithThirdPartyInput} deregisterWebhookWithThirdPartyInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deregisterWebhookWithThirdPartyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deregisterWebhookWithThirdParty(xAmzTarget, deregisterWebhookWithThirdPartyInput, opts, callback) {
      opts = opts || {};
      let postBody = deregisterWebhookWithThirdPartyInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deregisterWebhookWithThirdParty");
      }
      // verify the required parameter 'deregisterWebhookWithThirdPartyInput' is set
      if (deregisterWebhookWithThirdPartyInput === undefined || deregisterWebhookWithThirdPartyInput === null) {
        throw new Error("Missing the required parameter 'deregisterWebhookWithThirdPartyInput' when calling deregisterWebhookWithThirdParty");
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
        '/#X-Amz-Target=CodePipeline_20150709.DeregisterWebhookWithThirdParty', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the disableStageTransition operation.
     * @callback module:api/DefaultApi~disableStageTransitionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Prevents artifacts in a pipeline from transitioning to the next stage in the pipeline.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DisableStageTransitionInput} disableStageTransitionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~disableStageTransitionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    disableStageTransition(xAmzTarget, disableStageTransitionInput, opts, callback) {
      opts = opts || {};
      let postBody = disableStageTransitionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling disableStageTransition");
      }
      // verify the required parameter 'disableStageTransitionInput' is set
      if (disableStageTransitionInput === undefined || disableStageTransitionInput === null) {
        throw new Error("Missing the required parameter 'disableStageTransitionInput' when calling disableStageTransition");
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
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.DisableStageTransition', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the enableStageTransition operation.
     * @callback module:api/DefaultApi~enableStageTransitionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Enables artifacts in a pipeline to transition to a stage in a pipeline.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/EnableStageTransitionInput} enableStageTransitionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~enableStageTransitionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    enableStageTransition(xAmzTarget, enableStageTransitionInput, opts, callback) {
      opts = opts || {};
      let postBody = enableStageTransitionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling enableStageTransition");
      }
      // verify the required parameter 'enableStageTransitionInput' is set
      if (enableStageTransitionInput === undefined || enableStageTransitionInput === null) {
        throw new Error("Missing the required parameter 'enableStageTransitionInput' when calling enableStageTransition");
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
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.EnableStageTransition', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getActionType operation.
     * @callback module:api/DefaultApi~getActionTypeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetActionTypeOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about an action type created for an external provider, where the action is to be used by customers of the external provider. The action can be created with any supported integration model.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetActionTypeInput} getActionTypeInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getActionTypeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetActionTypeOutput}
     */
    getActionType(xAmzTarget, getActionTypeInput, opts, callback) {
      opts = opts || {};
      let postBody = getActionTypeInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getActionType");
      }
      // verify the required parameter 'getActionTypeInput' is set
      if (getActionTypeInput === undefined || getActionTypeInput === null) {
        throw new Error("Missing the required parameter 'getActionTypeInput' when calling getActionType");
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
      let returnType = GetActionTypeOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.GetActionType', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getJobDetails operation.
     * @callback module:api/DefaultApi~getJobDetailsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetJobDetailsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Returns information about a job. Used for custom actions only.</p> <important> <p>When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.</p> </important>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetJobDetailsInput} getJobDetailsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getJobDetailsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetJobDetailsOutput}
     */
    getJobDetails(xAmzTarget, getJobDetailsInput, opts, callback) {
      opts = opts || {};
      let postBody = getJobDetailsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getJobDetails");
      }
      // verify the required parameter 'getJobDetailsInput' is set
      if (getJobDetailsInput === undefined || getJobDetailsInput === null) {
        throw new Error("Missing the required parameter 'getJobDetailsInput' when calling getJobDetails");
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
      let returnType = GetJobDetailsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.GetJobDetails', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPipeline operation.
     * @callback module:api/DefaultApi~getPipelineCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetPipelineOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns the metadata, structure, stages, and actions of a pipeline. Can be used to return the entire structure of a pipeline in JSON format, which can then be modified and used to update the pipeline structure with <a>UpdatePipeline</a>.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetPipelineInput} getPipelineInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getPipelineCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetPipelineOutput}
     */
    getPipeline(xAmzTarget, getPipelineInput, opts, callback) {
      opts = opts || {};
      let postBody = getPipelineInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getPipeline");
      }
      // verify the required parameter 'getPipelineInput' is set
      if (getPipelineInput === undefined || getPipelineInput === null) {
        throw new Error("Missing the required parameter 'getPipelineInput' when calling getPipeline");
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
      let returnType = GetPipelineOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.GetPipeline', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPipelineExecution operation.
     * @callback module:api/DefaultApi~getPipelineExecutionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetPipelineExecutionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about an execution of a pipeline, including details about artifacts, the pipeline execution ID, and the name, version, and status of the pipeline.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetPipelineExecutionInput} getPipelineExecutionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getPipelineExecutionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetPipelineExecutionOutput}
     */
    getPipelineExecution(xAmzTarget, getPipelineExecutionInput, opts, callback) {
      opts = opts || {};
      let postBody = getPipelineExecutionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getPipelineExecution");
      }
      // verify the required parameter 'getPipelineExecutionInput' is set
      if (getPipelineExecutionInput === undefined || getPipelineExecutionInput === null) {
        throw new Error("Missing the required parameter 'getPipelineExecutionInput' when calling getPipelineExecution");
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
      let returnType = GetPipelineExecutionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.GetPipelineExecution', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPipelineState operation.
     * @callback module:api/DefaultApi~getPipelineStateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetPipelineStateOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Returns information about the state of a pipeline, including the stages and actions.</p> <note> <p>Values returned in the <code>revisionId</code> and <code>revisionUrl</code> fields indicate the source revision information, such as the commit ID, for the current state.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetPipelineStateInput} getPipelineStateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getPipelineStateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetPipelineStateOutput}
     */
    getPipelineState(xAmzTarget, getPipelineStateInput, opts, callback) {
      opts = opts || {};
      let postBody = getPipelineStateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getPipelineState");
      }
      // verify the required parameter 'getPipelineStateInput' is set
      if (getPipelineStateInput === undefined || getPipelineStateInput === null) {
        throw new Error("Missing the required parameter 'getPipelineStateInput' when calling getPipelineState");
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
      let returnType = GetPipelineStateOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.GetPipelineState', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getThirdPartyJobDetails operation.
     * @callback module:api/DefaultApi~getThirdPartyJobDetailsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetThirdPartyJobDetailsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Requests the details of a job for a third party action. Used for partner actions only.</p> <important> <p>When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.</p> </important>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetThirdPartyJobDetailsInput} getThirdPartyJobDetailsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getThirdPartyJobDetailsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetThirdPartyJobDetailsOutput}
     */
    getThirdPartyJobDetails(xAmzTarget, getThirdPartyJobDetailsInput, opts, callback) {
      opts = opts || {};
      let postBody = getThirdPartyJobDetailsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getThirdPartyJobDetails");
      }
      // verify the required parameter 'getThirdPartyJobDetailsInput' is set
      if (getThirdPartyJobDetailsInput === undefined || getThirdPartyJobDetailsInput === null) {
        throw new Error("Missing the required parameter 'getThirdPartyJobDetailsInput' when calling getThirdPartyJobDetails");
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
      let returnType = GetThirdPartyJobDetailsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.GetThirdPartyJobDetails', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listActionExecutions operation.
     * @callback module:api/DefaultApi~listActionExecutionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListActionExecutionsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists the action executions that have occurred in a pipeline.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListActionExecutionsInput} listActionExecutionsInput 
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
     * @param {module:api/DefaultApi~listActionExecutionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListActionExecutionsOutput}
     */
    listActionExecutions(xAmzTarget, listActionExecutionsInput, opts, callback) {
      opts = opts || {};
      let postBody = listActionExecutionsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listActionExecutions");
      }
      // verify the required parameter 'listActionExecutionsInput' is set
      if (listActionExecutionsInput === undefined || listActionExecutionsInput === null) {
        throw new Error("Missing the required parameter 'listActionExecutionsInput' when calling listActionExecutions");
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
      let returnType = ListActionExecutionsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.ListActionExecutions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listActionTypes operation.
     * @callback module:api/DefaultApi~listActionTypesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListActionTypesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets a summary of all CodePipeline action types associated with your account.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListActionTypesInput} listActionTypesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listActionTypesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListActionTypesOutput}
     */
    listActionTypes(xAmzTarget, listActionTypesInput, opts, callback) {
      opts = opts || {};
      let postBody = listActionTypesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listActionTypes");
      }
      // verify the required parameter 'listActionTypesInput' is set
      if (listActionTypesInput === undefined || listActionTypesInput === null) {
        throw new Error("Missing the required parameter 'listActionTypesInput' when calling listActionTypes");
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
      let returnType = ListActionTypesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.ListActionTypes', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listPipelineExecutions operation.
     * @callback module:api/DefaultApi~listPipelineExecutionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListPipelineExecutionsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets a summary of the most recent executions for a pipeline.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListPipelineExecutionsInput} listPipelineExecutionsInput 
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
     * @param {module:api/DefaultApi~listPipelineExecutionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListPipelineExecutionsOutput}
     */
    listPipelineExecutions(xAmzTarget, listPipelineExecutionsInput, opts, callback) {
      opts = opts || {};
      let postBody = listPipelineExecutionsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listPipelineExecutions");
      }
      // verify the required parameter 'listPipelineExecutionsInput' is set
      if (listPipelineExecutionsInput === undefined || listPipelineExecutionsInput === null) {
        throw new Error("Missing the required parameter 'listPipelineExecutionsInput' when calling listPipelineExecutions");
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
      let returnType = ListPipelineExecutionsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.ListPipelineExecutions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listPipelines operation.
     * @callback module:api/DefaultApi~listPipelinesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListPipelinesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets a summary of all of the pipelines associated with your account.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListPipelinesInput} listPipelinesInput 
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
     * @param {module:api/DefaultApi~listPipelinesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListPipelinesOutput}
     */
    listPipelines(xAmzTarget, listPipelinesInput, opts, callback) {
      opts = opts || {};
      let postBody = listPipelinesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listPipelines");
      }
      // verify the required parameter 'listPipelinesInput' is set
      if (listPipelinesInput === undefined || listPipelinesInput === null) {
        throw new Error("Missing the required parameter 'listPipelinesInput' when calling listPipelines");
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
      let returnType = ListPipelinesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.ListPipelines', 'POST',
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
     * Gets the set of key-value pairs (metadata) that are used to manage the resource.
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
        '/#X-Amz-Target=CodePipeline_20150709.ListTagsForResource', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listWebhooks operation.
     * @callback module:api/DefaultApi~listWebhooksCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListWebhooksOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets a listing of all the webhooks in this Amazon Web Services Region for this account. The output lists all webhooks and includes the webhook URL and ARN and the configuration for each webhook.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListWebhooksInput} listWebhooksInput 
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
     * @param {module:api/DefaultApi~listWebhooksCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListWebhooksOutput}
     */
    listWebhooks(xAmzTarget, listWebhooksInput, opts, callback) {
      opts = opts || {};
      let postBody = listWebhooksInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listWebhooks");
      }
      // verify the required parameter 'listWebhooksInput' is set
      if (listWebhooksInput === undefined || listWebhooksInput === null) {
        throw new Error("Missing the required parameter 'listWebhooksInput' when calling listWebhooks");
      }

      let pathParams = {
      };
      let queryParams = {
        'MaxResults': opts['maxResults'],
        'NextToken': opts['nextToken']
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
      let returnType = ListWebhooksOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.ListWebhooks', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the pollForJobs operation.
     * @callback module:api/DefaultApi~pollForJobsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PollForJobsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Returns information about any jobs for CodePipeline to act on. <code>PollForJobs</code> is valid only for action types with \"Custom\" in the owner field. If the action type contains <code>AWS</code> or <code>ThirdParty</code> in the owner field, the <code>PollForJobs</code> action returns an error.</p> <important> <p>When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.</p> </important>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PollForJobsInput} pollForJobsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~pollForJobsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PollForJobsOutput}
     */
    pollForJobs(xAmzTarget, pollForJobsInput, opts, callback) {
      opts = opts || {};
      let postBody = pollForJobsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling pollForJobs");
      }
      // verify the required parameter 'pollForJobsInput' is set
      if (pollForJobsInput === undefined || pollForJobsInput === null) {
        throw new Error("Missing the required parameter 'pollForJobsInput' when calling pollForJobs");
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
      let returnType = PollForJobsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.PollForJobs', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the pollForThirdPartyJobs operation.
     * @callback module:api/DefaultApi~pollForThirdPartyJobsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PollForThirdPartyJobsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Determines whether there are any third party jobs for a job worker to act on. Used for partner actions only.</p> <important> <p>When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts.</p> </important>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PollForThirdPartyJobsInput} pollForThirdPartyJobsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~pollForThirdPartyJobsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PollForThirdPartyJobsOutput}
     */
    pollForThirdPartyJobs(xAmzTarget, pollForThirdPartyJobsInput, opts, callback) {
      opts = opts || {};
      let postBody = pollForThirdPartyJobsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling pollForThirdPartyJobs");
      }
      // verify the required parameter 'pollForThirdPartyJobsInput' is set
      if (pollForThirdPartyJobsInput === undefined || pollForThirdPartyJobsInput === null) {
        throw new Error("Missing the required parameter 'pollForThirdPartyJobsInput' when calling pollForThirdPartyJobs");
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
      let returnType = PollForThirdPartyJobsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.PollForThirdPartyJobs', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putActionRevision operation.
     * @callback module:api/DefaultApi~putActionRevisionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PutActionRevisionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Provides information to CodePipeline about new revisions to a source.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PutActionRevisionInput} putActionRevisionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~putActionRevisionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PutActionRevisionOutput}
     */
    putActionRevision(xAmzTarget, putActionRevisionInput, opts, callback) {
      opts = opts || {};
      let postBody = putActionRevisionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling putActionRevision");
      }
      // verify the required parameter 'putActionRevisionInput' is set
      if (putActionRevisionInput === undefined || putActionRevisionInput === null) {
        throw new Error("Missing the required parameter 'putActionRevisionInput' when calling putActionRevision");
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
      let returnType = PutActionRevisionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.PutActionRevision', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putApprovalResult operation.
     * @callback module:api/DefaultApi~putApprovalResultCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PutApprovalResultOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Provides the response to a manual approval request to CodePipeline. Valid responses include Approved and Rejected.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PutApprovalResultInput} putApprovalResultInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~putApprovalResultCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PutApprovalResultOutput}
     */
    putApprovalResult(xAmzTarget, putApprovalResultInput, opts, callback) {
      opts = opts || {};
      let postBody = putApprovalResultInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling putApprovalResult");
      }
      // verify the required parameter 'putApprovalResultInput' is set
      if (putApprovalResultInput === undefined || putApprovalResultInput === null) {
        throw new Error("Missing the required parameter 'putApprovalResultInput' when calling putApprovalResult");
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
      let returnType = PutApprovalResultOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.PutApprovalResult', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putJobFailureResult operation.
     * @callback module:api/DefaultApi~putJobFailureResultCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Represents the failure of a job as returned to the pipeline by a job worker. Used for custom actions only.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PutJobFailureResultInput} putJobFailureResultInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~putJobFailureResultCallback} callback The callback function, accepting three arguments: error, data, response
     */
    putJobFailureResult(xAmzTarget, putJobFailureResultInput, opts, callback) {
      opts = opts || {};
      let postBody = putJobFailureResultInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling putJobFailureResult");
      }
      // verify the required parameter 'putJobFailureResultInput' is set
      if (putJobFailureResultInput === undefined || putJobFailureResultInput === null) {
        throw new Error("Missing the required parameter 'putJobFailureResultInput' when calling putJobFailureResult");
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
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.PutJobFailureResult', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putJobSuccessResult operation.
     * @callback module:api/DefaultApi~putJobSuccessResultCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Represents the success of a job as returned to the pipeline by a job worker. Used for custom actions only.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PutJobSuccessResultInput} putJobSuccessResultInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~putJobSuccessResultCallback} callback The callback function, accepting three arguments: error, data, response
     */
    putJobSuccessResult(xAmzTarget, putJobSuccessResultInput, opts, callback) {
      opts = opts || {};
      let postBody = putJobSuccessResultInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling putJobSuccessResult");
      }
      // verify the required parameter 'putJobSuccessResultInput' is set
      if (putJobSuccessResultInput === undefined || putJobSuccessResultInput === null) {
        throw new Error("Missing the required parameter 'putJobSuccessResultInput' when calling putJobSuccessResult");
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
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.PutJobSuccessResult', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putThirdPartyJobFailureResult operation.
     * @callback module:api/DefaultApi~putThirdPartyJobFailureResultCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Represents the failure of a third party job as returned to the pipeline by a job worker. Used for partner actions only.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PutThirdPartyJobFailureResultInput} putThirdPartyJobFailureResultInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~putThirdPartyJobFailureResultCallback} callback The callback function, accepting three arguments: error, data, response
     */
    putThirdPartyJobFailureResult(xAmzTarget, putThirdPartyJobFailureResultInput, opts, callback) {
      opts = opts || {};
      let postBody = putThirdPartyJobFailureResultInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling putThirdPartyJobFailureResult");
      }
      // verify the required parameter 'putThirdPartyJobFailureResultInput' is set
      if (putThirdPartyJobFailureResultInput === undefined || putThirdPartyJobFailureResultInput === null) {
        throw new Error("Missing the required parameter 'putThirdPartyJobFailureResultInput' when calling putThirdPartyJobFailureResult");
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
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.PutThirdPartyJobFailureResult', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putThirdPartyJobSuccessResult operation.
     * @callback module:api/DefaultApi~putThirdPartyJobSuccessResultCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Represents the success of a third party job as returned to the pipeline by a job worker. Used for partner actions only.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PutThirdPartyJobSuccessResultInput} putThirdPartyJobSuccessResultInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~putThirdPartyJobSuccessResultCallback} callback The callback function, accepting three arguments: error, data, response
     */
    putThirdPartyJobSuccessResult(xAmzTarget, putThirdPartyJobSuccessResultInput, opts, callback) {
      opts = opts || {};
      let postBody = putThirdPartyJobSuccessResultInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling putThirdPartyJobSuccessResult");
      }
      // verify the required parameter 'putThirdPartyJobSuccessResultInput' is set
      if (putThirdPartyJobSuccessResultInput === undefined || putThirdPartyJobSuccessResultInput === null) {
        throw new Error("Missing the required parameter 'putThirdPartyJobSuccessResultInput' when calling putThirdPartyJobSuccessResult");
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
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.PutThirdPartyJobSuccessResult', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putWebhook operation.
     * @callback module:api/DefaultApi~putWebhookCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PutWebhookOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Defines a webhook and returns a unique webhook URL generated by CodePipeline. This URL can be supplied to third party source hosting providers to call every time there's a code change. When CodePipeline receives a POST request on this URL, the pipeline defined in the webhook is started as long as the POST request satisfied the authentication and filtering requirements supplied when defining the webhook. RegisterWebhookWithThirdParty and DeregisterWebhookWithThirdParty APIs can be used to automatically configure supported third parties to call the generated webhook URL.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PutWebhookInput} putWebhookInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~putWebhookCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PutWebhookOutput}
     */
    putWebhook(xAmzTarget, putWebhookInput, opts, callback) {
      opts = opts || {};
      let postBody = putWebhookInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling putWebhook");
      }
      // verify the required parameter 'putWebhookInput' is set
      if (putWebhookInput === undefined || putWebhookInput === null) {
        throw new Error("Missing the required parameter 'putWebhookInput' when calling putWebhook");
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
      let returnType = PutWebhookOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.PutWebhook', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the registerWebhookWithThirdParty operation.
     * @callback module:api/DefaultApi~registerWebhookWithThirdPartyCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configures a connection between the webhook that was created and the external tool with events to be detected.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/RegisterWebhookWithThirdPartyInput} registerWebhookWithThirdPartyInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~registerWebhookWithThirdPartyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    registerWebhookWithThirdParty(xAmzTarget, registerWebhookWithThirdPartyInput, opts, callback) {
      opts = opts || {};
      let postBody = registerWebhookWithThirdPartyInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling registerWebhookWithThirdParty");
      }
      // verify the required parameter 'registerWebhookWithThirdPartyInput' is set
      if (registerWebhookWithThirdPartyInput === undefined || registerWebhookWithThirdPartyInput === null) {
        throw new Error("Missing the required parameter 'registerWebhookWithThirdPartyInput' when calling registerWebhookWithThirdParty");
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
        '/#X-Amz-Target=CodePipeline_20150709.RegisterWebhookWithThirdParty', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the retryStageExecution operation.
     * @callback module:api/DefaultApi~retryStageExecutionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RetryStageExecutionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Resumes the pipeline execution by retrying the last failed actions in a stage. You can retry a stage immediately if any of the actions in the stage fail. When you retry, all actions that are still in progress continue working, and failed actions are triggered again.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/RetryStageExecutionInput} retryStageExecutionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~retryStageExecutionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RetryStageExecutionOutput}
     */
    retryStageExecution(xAmzTarget, retryStageExecutionInput, opts, callback) {
      opts = opts || {};
      let postBody = retryStageExecutionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling retryStageExecution");
      }
      // verify the required parameter 'retryStageExecutionInput' is set
      if (retryStageExecutionInput === undefined || retryStageExecutionInput === null) {
        throw new Error("Missing the required parameter 'retryStageExecutionInput' when calling retryStageExecution");
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
      let returnType = RetryStageExecutionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.RetryStageExecution', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the startPipelineExecution operation.
     * @callback module:api/DefaultApi~startPipelineExecutionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/StartPipelineExecutionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Starts the specified pipeline. Specifically, it begins processing the latest commit to the source location specified as part of the pipeline.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/StartPipelineExecutionInput} startPipelineExecutionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~startPipelineExecutionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/StartPipelineExecutionOutput}
     */
    startPipelineExecution(xAmzTarget, startPipelineExecutionInput, opts, callback) {
      opts = opts || {};
      let postBody = startPipelineExecutionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling startPipelineExecution");
      }
      // verify the required parameter 'startPipelineExecutionInput' is set
      if (startPipelineExecutionInput === undefined || startPipelineExecutionInput === null) {
        throw new Error("Missing the required parameter 'startPipelineExecutionInput' when calling startPipelineExecution");
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
      let returnType = StartPipelineExecutionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.StartPipelineExecution', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the stopPipelineExecution operation.
     * @callback module:api/DefaultApi~stopPipelineExecutionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/StopPipelineExecutionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Stops the specified pipeline execution. You choose to either stop the pipeline execution by completing in-progress actions without starting subsequent actions, or by abandoning in-progress actions. While completing or abandoning in-progress actions, the pipeline execution is in a <code>Stopping</code> state. After all in-progress actions are completed or abandoned, the pipeline execution is in a <code>Stopped</code> state.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/StopPipelineExecutionInput} stopPipelineExecutionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~stopPipelineExecutionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/StopPipelineExecutionOutput}
     */
    stopPipelineExecution(xAmzTarget, stopPipelineExecutionInput, opts, callback) {
      opts = opts || {};
      let postBody = stopPipelineExecutionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling stopPipelineExecution");
      }
      // verify the required parameter 'stopPipelineExecutionInput' is set
      if (stopPipelineExecutionInput === undefined || stopPipelineExecutionInput === null) {
        throw new Error("Missing the required parameter 'stopPipelineExecutionInput' when calling stopPipelineExecution");
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
      let returnType = StopPipelineExecutionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.StopPipelineExecution', 'POST',
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
     * Adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a resource. 
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
        '/#X-Amz-Target=CodePipeline_20150709.TagResource', 'POST',
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
     * Removes tags from an Amazon Web Services resource.
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
        '/#X-Amz-Target=CodePipeline_20150709.UntagResource', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateActionType operation.
     * @callback module:api/DefaultApi~updateActionTypeCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates an action type that was created with any supported integration model, where the action type is to be used by customers of the action type provider. Use a JSON file with the action definition and <code>UpdateActionType</code> to provide the full structure.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateActionTypeInput} updateActionTypeInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateActionTypeCallback} callback The callback function, accepting three arguments: error, data, response
     */
    updateActionType(xAmzTarget, updateActionTypeInput, opts, callback) {
      opts = opts || {};
      let postBody = updateActionTypeInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateActionType");
      }
      // verify the required parameter 'updateActionTypeInput' is set
      if (updateActionTypeInput === undefined || updateActionTypeInput === null) {
        throw new Error("Missing the required parameter 'updateActionTypeInput' when calling updateActionType");
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
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.UpdateActionType', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updatePipeline operation.
     * @callback module:api/DefaultApi~updatePipelineCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdatePipelineOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates a specified pipeline with edits or changes to its structure. Use a JSON file with the pipeline structure and <code>UpdatePipeline</code> to provide the full structure of the pipeline. Updating the pipeline increases the version number of the pipeline by 1.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdatePipelineInput} updatePipelineInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updatePipelineCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdatePipelineOutput}
     */
    updatePipeline(xAmzTarget, updatePipelineInput, opts, callback) {
      opts = opts || {};
      let postBody = updatePipelineInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updatePipeline");
      }
      // verify the required parameter 'updatePipelineInput' is set
      if (updatePipelineInput === undefined || updatePipelineInput === null) {
        throw new Error("Missing the required parameter 'updatePipelineInput' when calling updatePipeline");
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
      let returnType = UpdatePipelineOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodePipeline_20150709.UpdatePipeline', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
