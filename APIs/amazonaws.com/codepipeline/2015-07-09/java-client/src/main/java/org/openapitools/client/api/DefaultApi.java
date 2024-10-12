/*
 * AWS CodePipeline
 * <fullname>CodePipeline</fullname> <p> <b>Overview</b> </p> <p>This is the CodePipeline API Reference. This guide provides descriptions of the actions and data types for CodePipeline. Some functionality for your pipeline can only be configured through the API. For more information, see the <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html\">CodePipeline User Guide</a>.</p> <p>You can use the CodePipeline API to work with pipelines, stages, actions, and transitions.</p> <p> <i>Pipelines</i> are models of automated release processes. Each pipeline is uniquely named, and consists of stages, actions, and transitions. </p> <p>You can work with pipelines by calling:</p> <ul> <li> <p> <a>CreatePipeline</a>, which creates a uniquely named pipeline.</p> </li> <li> <p> <a>DeletePipeline</a>, which deletes the specified pipeline.</p> </li> <li> <p> <a>GetPipeline</a>, which returns information about the pipeline structure and pipeline metadata, including the pipeline Amazon Resource Name (ARN).</p> </li> <li> <p> <a>GetPipelineExecution</a>, which returns information about a specific execution of a pipeline.</p> </li> <li> <p> <a>GetPipelineState</a>, which returns information about the current state of the stages and actions of a pipeline.</p> </li> <li> <p> <a>ListActionExecutions</a>, which returns action-level details for past executions. The details include full stage and action-level details, including individual action duration, status, any errors that occurred during the execution, and input and output artifact location details.</p> </li> <li> <p> <a>ListPipelines</a>, which gets a summary of all of the pipelines associated with your account.</p> </li> <li> <p> <a>ListPipelineExecutions</a>, which gets a summary of the most recent executions for a pipeline.</p> </li> <li> <p> <a>StartPipelineExecution</a>, which runs the most recent revision of an artifact through the pipeline.</p> </li> <li> <p> <a>StopPipelineExecution</a>, which stops the specified pipeline execution from continuing through the pipeline.</p> </li> <li> <p> <a>UpdatePipeline</a>, which updates a pipeline with edits or changes to the structure of the pipeline.</p> </li> </ul> <p>Pipelines include <i>stages</i>. Each stage contains one or more actions that must complete before the next stage begins. A stage results in success or failure. If a stage fails, the pipeline stops at that stage and remains stopped until either a new version of an artifact appears in the source location, or a user takes action to rerun the most recent artifact through the pipeline. You can call <a>GetPipelineState</a>, which displays the status of a pipeline, including the status of stages in the pipeline, or <a>GetPipeline</a>, which returns the entire structure of the pipeline, including the stages of that pipeline. For more information about the structure of stages and actions, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-structure.html\">CodePipeline Pipeline Structure Reference</a>.</p> <p>Pipeline stages include <i>actions</i> that are categorized into categories such as source or build actions performed in a stage of a pipeline. For example, you can use a source action to import artifacts into a pipeline from a source such as Amazon S3. Like stages, you do not work with actions directly in most cases, but you do define and interact with actions when working with pipeline operations such as <a>CreatePipeline</a> and <a>GetPipelineState</a>. Valid action categories are:</p> <ul> <li> <p>Source</p> </li> <li> <p>Build</p> </li> <li> <p>Test</p> </li> <li> <p>Deploy</p> </li> <li> <p>Approval</p> </li> <li> <p>Invoke</p> </li> </ul> <p>Pipelines also include <i>transitions</i>, which allow the transition of artifacts from one stage to the next in a pipeline after the actions in one stage complete.</p> <p>You can work with transitions by calling:</p> <ul> <li> <p> <a>DisableStageTransition</a>, which prevents artifacts from transitioning to the next stage in a pipeline.</p> </li> <li> <p> <a>EnableStageTransition</a>, which enables transition of artifacts between stages in a pipeline. </p> </li> </ul> <p> <b>Using the API to integrate with CodePipeline</b> </p> <p>For third-party integrators or developers who want to create their own integrations with CodePipeline, the expected sequence varies from the standard API user. To integrate with CodePipeline, developers need to work with the following items:</p> <p> <b>Jobs</b>, which are instances of an action. For example, a job for a source action might import a revision of an artifact from a source. </p> <p>You can work with jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetJobDetails</a>, which returns the details of a job.</p> </li> <li> <p> <a>PollForJobs</a>, which determines whether there are any jobs to act on.</p> </li> <li> <p> <a>PutJobFailureResult</a>, which provides details of a job failure. </p> </li> <li> <p> <a>PutJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul> <p> <b>Third party jobs</b>, which are instances of an action created by a partner action and integrated into CodePipeline. Partner actions are created by members of the Amazon Web Services Partner Network.</p> <p>You can work with third party jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeThirdPartyJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetThirdPartyJobDetails</a>, which requests the details of a job for a partner action.</p> </li> <li> <p> <a>PollForThirdPartyJobs</a>, which determines whether there are any jobs to act on. </p> </li> <li> <p> <a>PutThirdPartyJobFailureResult</a>, which provides details of a job failure.</p> </li> <li> <p> <a>PutThirdPartyJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2015-07-09
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import org.openapitools.client.model.AcknowledgeJobInput;
import org.openapitools.client.model.AcknowledgeJobOutput;
import org.openapitools.client.model.AcknowledgeThirdPartyJobInput;
import org.openapitools.client.model.AcknowledgeThirdPartyJobOutput;
import org.openapitools.client.model.CreateCustomActionTypeInput;
import org.openapitools.client.model.CreateCustomActionTypeOutput;
import org.openapitools.client.model.CreatePipelineInput;
import org.openapitools.client.model.CreatePipelineOutput;
import org.openapitools.client.model.DeleteCustomActionTypeInput;
import org.openapitools.client.model.DeletePipelineInput;
import org.openapitools.client.model.DeleteWebhookInput;
import org.openapitools.client.model.DeregisterWebhookWithThirdPartyInput;
import org.openapitools.client.model.DisableStageTransitionInput;
import org.openapitools.client.model.EnableStageTransitionInput;
import org.openapitools.client.model.GetActionTypeInput;
import org.openapitools.client.model.GetActionTypeOutput;
import org.openapitools.client.model.GetJobDetailsInput;
import org.openapitools.client.model.GetJobDetailsOutput;
import org.openapitools.client.model.GetPipelineExecutionInput;
import org.openapitools.client.model.GetPipelineExecutionOutput;
import org.openapitools.client.model.GetPipelineInput;
import org.openapitools.client.model.GetPipelineOutput;
import org.openapitools.client.model.GetPipelineStateInput;
import org.openapitools.client.model.GetPipelineStateOutput;
import org.openapitools.client.model.GetThirdPartyJobDetailsInput;
import org.openapitools.client.model.GetThirdPartyJobDetailsOutput;
import org.openapitools.client.model.ListActionExecutionsInput;
import org.openapitools.client.model.ListActionExecutionsOutput;
import org.openapitools.client.model.ListActionTypesInput;
import org.openapitools.client.model.ListActionTypesOutput;
import org.openapitools.client.model.ListPipelineExecutionsInput;
import org.openapitools.client.model.ListPipelineExecutionsOutput;
import org.openapitools.client.model.ListPipelinesInput;
import org.openapitools.client.model.ListPipelinesOutput;
import org.openapitools.client.model.ListTagsForResourceInput;
import org.openapitools.client.model.ListTagsForResourceOutput;
import org.openapitools.client.model.ListWebhooksInput;
import org.openapitools.client.model.ListWebhooksOutput;
import org.openapitools.client.model.PollForJobsInput;
import org.openapitools.client.model.PollForJobsOutput;
import org.openapitools.client.model.PollForThirdPartyJobsInput;
import org.openapitools.client.model.PollForThirdPartyJobsOutput;
import org.openapitools.client.model.PutActionRevisionInput;
import org.openapitools.client.model.PutActionRevisionOutput;
import org.openapitools.client.model.PutApprovalResultInput;
import org.openapitools.client.model.PutApprovalResultOutput;
import org.openapitools.client.model.PutJobFailureResultInput;
import org.openapitools.client.model.PutJobSuccessResultInput;
import org.openapitools.client.model.PutThirdPartyJobFailureResultInput;
import org.openapitools.client.model.PutThirdPartyJobSuccessResultInput;
import org.openapitools.client.model.PutWebhookInput;
import org.openapitools.client.model.PutWebhookOutput;
import org.openapitools.client.model.RegisterWebhookWithThirdPartyInput;
import org.openapitools.client.model.RetryStageExecutionInput;
import org.openapitools.client.model.RetryStageExecutionOutput;
import org.openapitools.client.model.StartPipelineExecutionInput;
import org.openapitools.client.model.StartPipelineExecutionOutput;
import org.openapitools.client.model.StopPipelineExecutionInput;
import org.openapitools.client.model.StopPipelineExecutionOutput;
import org.openapitools.client.model.TagResourceInput;
import org.openapitools.client.model.UntagResourceInput;
import org.openapitools.client.model.UpdateActionTypeInput;
import org.openapitools.client.model.UpdatePipelineInput;
import org.openapitools.client.model.UpdatePipelineOutput;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DefaultApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DefaultApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DefaultApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for acknowledgeJob
     * @param xAmzTarget  (required)
     * @param acknowledgeJobInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNonceException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> JobNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call acknowledgeJobCall(String xAmzTarget, AcknowledgeJobInput acknowledgeJobInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = acknowledgeJobInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.AcknowledgeJob";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call acknowledgeJobValidateBeforeCall(String xAmzTarget, AcknowledgeJobInput acknowledgeJobInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling acknowledgeJob(Async)");
        }

        // verify the required parameter 'acknowledgeJobInput' is set
        if (acknowledgeJobInput == null) {
            throw new ApiException("Missing the required parameter 'acknowledgeJobInput' when calling acknowledgeJob(Async)");
        }

        return acknowledgeJobCall(xAmzTarget, acknowledgeJobInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Returns information about a specified job and whether that job has been received by the job worker. Used for custom actions only.
     * @param xAmzTarget  (required)
     * @param acknowledgeJobInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return AcknowledgeJobOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNonceException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> JobNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public AcknowledgeJobOutput acknowledgeJob(String xAmzTarget, AcknowledgeJobInput acknowledgeJobInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<AcknowledgeJobOutput> localVarResp = acknowledgeJobWithHttpInfo(xAmzTarget, acknowledgeJobInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Returns information about a specified job and whether that job has been received by the job worker. Used for custom actions only.
     * @param xAmzTarget  (required)
     * @param acknowledgeJobInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;AcknowledgeJobOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNonceException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> JobNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AcknowledgeJobOutput> acknowledgeJobWithHttpInfo(String xAmzTarget, AcknowledgeJobInput acknowledgeJobInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = acknowledgeJobValidateBeforeCall(xAmzTarget, acknowledgeJobInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<AcknowledgeJobOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Returns information about a specified job and whether that job has been received by the job worker. Used for custom actions only.
     * @param xAmzTarget  (required)
     * @param acknowledgeJobInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNonceException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> JobNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call acknowledgeJobAsync(String xAmzTarget, AcknowledgeJobInput acknowledgeJobInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<AcknowledgeJobOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = acknowledgeJobValidateBeforeCall(xAmzTarget, acknowledgeJobInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<AcknowledgeJobOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for acknowledgeThirdPartyJob
     * @param xAmzTarget  (required)
     * @param acknowledgeThirdPartyJobInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNonceException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call acknowledgeThirdPartyJobCall(String xAmzTarget, AcknowledgeThirdPartyJobInput acknowledgeThirdPartyJobInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = acknowledgeThirdPartyJobInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.AcknowledgeThirdPartyJob";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call acknowledgeThirdPartyJobValidateBeforeCall(String xAmzTarget, AcknowledgeThirdPartyJobInput acknowledgeThirdPartyJobInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling acknowledgeThirdPartyJob(Async)");
        }

        // verify the required parameter 'acknowledgeThirdPartyJobInput' is set
        if (acknowledgeThirdPartyJobInput == null) {
            throw new ApiException("Missing the required parameter 'acknowledgeThirdPartyJobInput' when calling acknowledgeThirdPartyJob(Async)");
        }

        return acknowledgeThirdPartyJobCall(xAmzTarget, acknowledgeThirdPartyJobInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Confirms a job worker has received the specified job. Used for partner actions only.
     * @param xAmzTarget  (required)
     * @param acknowledgeThirdPartyJobInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return AcknowledgeThirdPartyJobOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNonceException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
     </table>
     */
    public AcknowledgeThirdPartyJobOutput acknowledgeThirdPartyJob(String xAmzTarget, AcknowledgeThirdPartyJobInput acknowledgeThirdPartyJobInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<AcknowledgeThirdPartyJobOutput> localVarResp = acknowledgeThirdPartyJobWithHttpInfo(xAmzTarget, acknowledgeThirdPartyJobInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Confirms a job worker has received the specified job. Used for partner actions only.
     * @param xAmzTarget  (required)
     * @param acknowledgeThirdPartyJobInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;AcknowledgeThirdPartyJobOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNonceException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AcknowledgeThirdPartyJobOutput> acknowledgeThirdPartyJobWithHttpInfo(String xAmzTarget, AcknowledgeThirdPartyJobInput acknowledgeThirdPartyJobInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = acknowledgeThirdPartyJobValidateBeforeCall(xAmzTarget, acknowledgeThirdPartyJobInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<AcknowledgeThirdPartyJobOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Confirms a job worker has received the specified job. Used for partner actions only.
     * @param xAmzTarget  (required)
     * @param acknowledgeThirdPartyJobInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNonceException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call acknowledgeThirdPartyJobAsync(String xAmzTarget, AcknowledgeThirdPartyJobInput acknowledgeThirdPartyJobInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<AcknowledgeThirdPartyJobOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = acknowledgeThirdPartyJobValidateBeforeCall(xAmzTarget, acknowledgeThirdPartyJobInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<AcknowledgeThirdPartyJobOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createCustomActionType
     * @param xAmzTarget  (required)
     * @param createCustomActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> LimitExceededException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createCustomActionTypeCall(String xAmzTarget, CreateCustomActionTypeInput createCustomActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = createCustomActionTypeInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.CreateCustomActionType";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createCustomActionTypeValidateBeforeCall(String xAmzTarget, CreateCustomActionTypeInput createCustomActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling createCustomActionType(Async)");
        }

        // verify the required parameter 'createCustomActionTypeInput' is set
        if (createCustomActionTypeInput == null) {
            throw new ApiException("Missing the required parameter 'createCustomActionTypeInput' when calling createCustomActionType(Async)");
        }

        return createCustomActionTypeCall(xAmzTarget, createCustomActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Creates a new custom action that can be used in all pipelines associated with the Amazon Web Services account. Only used for custom actions.
     * @param xAmzTarget  (required)
     * @param createCustomActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return CreateCustomActionTypeOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> LimitExceededException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public CreateCustomActionTypeOutput createCustomActionType(String xAmzTarget, CreateCustomActionTypeInput createCustomActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<CreateCustomActionTypeOutput> localVarResp = createCustomActionTypeWithHttpInfo(xAmzTarget, createCustomActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Creates a new custom action that can be used in all pipelines associated with the Amazon Web Services account. Only used for custom actions.
     * @param xAmzTarget  (required)
     * @param createCustomActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;CreateCustomActionTypeOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> LimitExceededException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateCustomActionTypeOutput> createCustomActionTypeWithHttpInfo(String xAmzTarget, CreateCustomActionTypeInput createCustomActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = createCustomActionTypeValidateBeforeCall(xAmzTarget, createCustomActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<CreateCustomActionTypeOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Creates a new custom action that can be used in all pipelines associated with the Amazon Web Services account. Only used for custom actions.
     * @param xAmzTarget  (required)
     * @param createCustomActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> LimitExceededException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createCustomActionTypeAsync(String xAmzTarget, CreateCustomActionTypeInput createCustomActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<CreateCustomActionTypeOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = createCustomActionTypeValidateBeforeCall(xAmzTarget, createCustomActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<CreateCustomActionTypeOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createPipeline
     * @param xAmzTarget  (required)
     * @param createPipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNameInUseException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidStageDeclarationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidActionDeclarationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InvalidBlockerDeclarationException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> InvalidStructureException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> LimitExceededException </td><td>  -  </td></tr>
        <tr><td> 487 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 488 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 489 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createPipelineCall(String xAmzTarget, CreatePipelineInput createPipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = createPipelineInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.CreatePipeline";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createPipelineValidateBeforeCall(String xAmzTarget, CreatePipelineInput createPipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling createPipeline(Async)");
        }

        // verify the required parameter 'createPipelineInput' is set
        if (createPipelineInput == null) {
            throw new ApiException("Missing the required parameter 'createPipelineInput' when calling createPipeline(Async)");
        }

        return createPipelineCall(xAmzTarget, createPipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt;Creates a pipeline.&lt;/p&gt; &lt;note&gt; &lt;p&gt;In the pipeline structure, you must include either &lt;code&gt;artifactStore&lt;/code&gt; or &lt;code&gt;artifactStores&lt;/code&gt; in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use &lt;code&gt;artifactStores&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;
     * @param xAmzTarget  (required)
     * @param createPipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return CreatePipelineOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNameInUseException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidStageDeclarationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidActionDeclarationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InvalidBlockerDeclarationException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> InvalidStructureException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> LimitExceededException </td><td>  -  </td></tr>
        <tr><td> 487 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 488 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 489 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public CreatePipelineOutput createPipeline(String xAmzTarget, CreatePipelineInput createPipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<CreatePipelineOutput> localVarResp = createPipelineWithHttpInfo(xAmzTarget, createPipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt;Creates a pipeline.&lt;/p&gt; &lt;note&gt; &lt;p&gt;In the pipeline structure, you must include either &lt;code&gt;artifactStore&lt;/code&gt; or &lt;code&gt;artifactStores&lt;/code&gt; in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use &lt;code&gt;artifactStores&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;
     * @param xAmzTarget  (required)
     * @param createPipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;CreatePipelineOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNameInUseException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidStageDeclarationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidActionDeclarationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InvalidBlockerDeclarationException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> InvalidStructureException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> LimitExceededException </td><td>  -  </td></tr>
        <tr><td> 487 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 488 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 489 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreatePipelineOutput> createPipelineWithHttpInfo(String xAmzTarget, CreatePipelineInput createPipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = createPipelineValidateBeforeCall(xAmzTarget, createPipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<CreatePipelineOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Creates a pipeline.&lt;/p&gt; &lt;note&gt; &lt;p&gt;In the pipeline structure, you must include either &lt;code&gt;artifactStore&lt;/code&gt; or &lt;code&gt;artifactStores&lt;/code&gt; in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use &lt;code&gt;artifactStores&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;
     * @param xAmzTarget  (required)
     * @param createPipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNameInUseException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidStageDeclarationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidActionDeclarationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InvalidBlockerDeclarationException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> InvalidStructureException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> LimitExceededException </td><td>  -  </td></tr>
        <tr><td> 487 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 488 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 489 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createPipelineAsync(String xAmzTarget, CreatePipelineInput createPipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<CreatePipelineOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = createPipelineValidateBeforeCall(xAmzTarget, createPipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<CreatePipelineOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteCustomActionType
     * @param xAmzTarget  (required)
     * @param deleteCustomActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteCustomActionTypeCall(String xAmzTarget, DeleteCustomActionTypeInput deleteCustomActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = deleteCustomActionTypeInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.DeleteCustomActionType";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteCustomActionTypeValidateBeforeCall(String xAmzTarget, DeleteCustomActionTypeInput deleteCustomActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling deleteCustomActionType(Async)");
        }

        // verify the required parameter 'deleteCustomActionTypeInput' is set
        if (deleteCustomActionTypeInput == null) {
            throw new ApiException("Missing the required parameter 'deleteCustomActionTypeInput' when calling deleteCustomActionType(Async)");
        }

        return deleteCustomActionTypeCall(xAmzTarget, deleteCustomActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt;Marks a custom action as deleted. &lt;code&gt;PollForJobs&lt;/code&gt; for the custom action fails after the action is marked for deletion. Used for custom actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;To re-create a custom action after it has been deleted you must use a string in the version field that has never been used before. This string can be an incremented version number, for example. To restore a deleted custom action, use a JSON file that is identical to the deleted action, including the original string in the version field.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param deleteCustomActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public void deleteCustomActionType(String xAmzTarget, DeleteCustomActionTypeInput deleteCustomActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        deleteCustomActionTypeWithHttpInfo(xAmzTarget, deleteCustomActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * &lt;p&gt;Marks a custom action as deleted. &lt;code&gt;PollForJobs&lt;/code&gt; for the custom action fails after the action is marked for deletion. Used for custom actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;To re-create a custom action after it has been deleted you must use a string in the version field that has never been used before. This string can be an incremented version number, for example. To restore a deleted custom action, use a JSON file that is identical to the deleted action, including the original string in the version field.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param deleteCustomActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteCustomActionTypeWithHttpInfo(String xAmzTarget, DeleteCustomActionTypeInput deleteCustomActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = deleteCustomActionTypeValidateBeforeCall(xAmzTarget, deleteCustomActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Marks a custom action as deleted. &lt;code&gt;PollForJobs&lt;/code&gt; for the custom action fails after the action is marked for deletion. Used for custom actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;To re-create a custom action after it has been deleted you must use a string in the version field that has never been used before. This string can be an incremented version number, for example. To restore a deleted custom action, use a JSON file that is identical to the deleted action, including the original string in the version field.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param deleteCustomActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteCustomActionTypeAsync(String xAmzTarget, DeleteCustomActionTypeInput deleteCustomActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteCustomActionTypeValidateBeforeCall(xAmzTarget, deleteCustomActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deletePipeline
     * @param xAmzTarget  (required)
     * @param deletePipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deletePipelineCall(String xAmzTarget, DeletePipelineInput deletePipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = deletePipelineInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.DeletePipeline";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deletePipelineValidateBeforeCall(String xAmzTarget, DeletePipelineInput deletePipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling deletePipeline(Async)");
        }

        // verify the required parameter 'deletePipelineInput' is set
        if (deletePipelineInput == null) {
            throw new ApiException("Missing the required parameter 'deletePipelineInput' when calling deletePipeline(Async)");
        }

        return deletePipelineCall(xAmzTarget, deletePipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Deletes the specified pipeline.
     * @param xAmzTarget  (required)
     * @param deletePipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public void deletePipeline(String xAmzTarget, DeletePipelineInput deletePipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        deletePipelineWithHttpInfo(xAmzTarget, deletePipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * Deletes the specified pipeline.
     * @param xAmzTarget  (required)
     * @param deletePipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deletePipelineWithHttpInfo(String xAmzTarget, DeletePipelineInput deletePipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = deletePipelineValidateBeforeCall(xAmzTarget, deletePipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Deletes the specified pipeline.
     * @param xAmzTarget  (required)
     * @param deletePipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deletePipelineAsync(String xAmzTarget, DeletePipelineInput deletePipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deletePipelineValidateBeforeCall(xAmzTarget, deletePipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteWebhook
     * @param xAmzTarget  (required)
     * @param deleteWebhookInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteWebhookCall(String xAmzTarget, DeleteWebhookInput deleteWebhookInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = deleteWebhookInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.DeleteWebhook";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteWebhookValidateBeforeCall(String xAmzTarget, DeleteWebhookInput deleteWebhookInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling deleteWebhook(Async)");
        }

        // verify the required parameter 'deleteWebhookInput' is set
        if (deleteWebhookInput == null) {
            throw new ApiException("Missing the required parameter 'deleteWebhookInput' when calling deleteWebhook(Async)");
        }

        return deleteWebhookCall(xAmzTarget, deleteWebhookInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Deletes a previously created webhook by name. Deleting the webhook stops CodePipeline from starting a pipeline every time an external event occurs. The API returns successfully when trying to delete a webhook that is already deleted. If a deleted webhook is re-created by calling PutWebhook with the same name, it will have a different URL.
     * @param xAmzTarget  (required)
     * @param deleteWebhookInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteWebhook(String xAmzTarget, DeleteWebhookInput deleteWebhookInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = deleteWebhookWithHttpInfo(xAmzTarget, deleteWebhookInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Deletes a previously created webhook by name. Deleting the webhook stops CodePipeline from starting a pipeline every time an external event occurs. The API returns successfully when trying to delete a webhook that is already deleted. If a deleted webhook is re-created by calling PutWebhook with the same name, it will have a different URL.
     * @param xAmzTarget  (required)
     * @param deleteWebhookInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteWebhookWithHttpInfo(String xAmzTarget, DeleteWebhookInput deleteWebhookInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = deleteWebhookValidateBeforeCall(xAmzTarget, deleteWebhookInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Deletes a previously created webhook by name. Deleting the webhook stops CodePipeline from starting a pipeline every time an external event occurs. The API returns successfully when trying to delete a webhook that is already deleted. If a deleted webhook is re-created by calling PutWebhook with the same name, it will have a different URL.
     * @param xAmzTarget  (required)
     * @param deleteWebhookInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteWebhookAsync(String xAmzTarget, DeleteWebhookInput deleteWebhookInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteWebhookValidateBeforeCall(xAmzTarget, deleteWebhookInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deregisterWebhookWithThirdParty
     * @param xAmzTarget  (required)
     * @param deregisterWebhookWithThirdPartyInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> WebhookNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deregisterWebhookWithThirdPartyCall(String xAmzTarget, DeregisterWebhookWithThirdPartyInput deregisterWebhookWithThirdPartyInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = deregisterWebhookWithThirdPartyInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.DeregisterWebhookWithThirdParty";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deregisterWebhookWithThirdPartyValidateBeforeCall(String xAmzTarget, DeregisterWebhookWithThirdPartyInput deregisterWebhookWithThirdPartyInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling deregisterWebhookWithThirdParty(Async)");
        }

        // verify the required parameter 'deregisterWebhookWithThirdPartyInput' is set
        if (deregisterWebhookWithThirdPartyInput == null) {
            throw new ApiException("Missing the required parameter 'deregisterWebhookWithThirdPartyInput' when calling deregisterWebhookWithThirdParty(Async)");
        }

        return deregisterWebhookWithThirdPartyCall(xAmzTarget, deregisterWebhookWithThirdPartyInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Removes the connection between the webhook that was created by CodePipeline and the external tool with events to be detected. Currently supported only for webhooks that target an action type of GitHub.
     * @param xAmzTarget  (required)
     * @param deregisterWebhookWithThirdPartyInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> WebhookNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public Object deregisterWebhookWithThirdParty(String xAmzTarget, DeregisterWebhookWithThirdPartyInput deregisterWebhookWithThirdPartyInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = deregisterWebhookWithThirdPartyWithHttpInfo(xAmzTarget, deregisterWebhookWithThirdPartyInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Removes the connection between the webhook that was created by CodePipeline and the external tool with events to be detected. Currently supported only for webhooks that target an action type of GitHub.
     * @param xAmzTarget  (required)
     * @param deregisterWebhookWithThirdPartyInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> WebhookNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deregisterWebhookWithThirdPartyWithHttpInfo(String xAmzTarget, DeregisterWebhookWithThirdPartyInput deregisterWebhookWithThirdPartyInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = deregisterWebhookWithThirdPartyValidateBeforeCall(xAmzTarget, deregisterWebhookWithThirdPartyInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Removes the connection between the webhook that was created by CodePipeline and the external tool with events to be detected. Currently supported only for webhooks that target an action type of GitHub.
     * @param xAmzTarget  (required)
     * @param deregisterWebhookWithThirdPartyInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> WebhookNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deregisterWebhookWithThirdPartyAsync(String xAmzTarget, DeregisterWebhookWithThirdPartyInput deregisterWebhookWithThirdPartyInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deregisterWebhookWithThirdPartyValidateBeforeCall(xAmzTarget, deregisterWebhookWithThirdPartyInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for disableStageTransition
     * @param xAmzTarget  (required)
     * @param disableStageTransitionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> StageNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call disableStageTransitionCall(String xAmzTarget, DisableStageTransitionInput disableStageTransitionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = disableStageTransitionInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.DisableStageTransition";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call disableStageTransitionValidateBeforeCall(String xAmzTarget, DisableStageTransitionInput disableStageTransitionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling disableStageTransition(Async)");
        }

        // verify the required parameter 'disableStageTransitionInput' is set
        if (disableStageTransitionInput == null) {
            throw new ApiException("Missing the required parameter 'disableStageTransitionInput' when calling disableStageTransition(Async)");
        }

        return disableStageTransitionCall(xAmzTarget, disableStageTransitionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Prevents artifacts in a pipeline from transitioning to the next stage in the pipeline.
     * @param xAmzTarget  (required)
     * @param disableStageTransitionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> StageNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public void disableStageTransition(String xAmzTarget, DisableStageTransitionInput disableStageTransitionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        disableStageTransitionWithHttpInfo(xAmzTarget, disableStageTransitionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * Prevents artifacts in a pipeline from transitioning to the next stage in the pipeline.
     * @param xAmzTarget  (required)
     * @param disableStageTransitionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> StageNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> disableStageTransitionWithHttpInfo(String xAmzTarget, DisableStageTransitionInput disableStageTransitionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = disableStageTransitionValidateBeforeCall(xAmzTarget, disableStageTransitionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Prevents artifacts in a pipeline from transitioning to the next stage in the pipeline.
     * @param xAmzTarget  (required)
     * @param disableStageTransitionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> StageNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call disableStageTransitionAsync(String xAmzTarget, DisableStageTransitionInput disableStageTransitionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = disableStageTransitionValidateBeforeCall(xAmzTarget, disableStageTransitionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for enableStageTransition
     * @param xAmzTarget  (required)
     * @param enableStageTransitionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> StageNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call enableStageTransitionCall(String xAmzTarget, EnableStageTransitionInput enableStageTransitionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = enableStageTransitionInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.EnableStageTransition";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call enableStageTransitionValidateBeforeCall(String xAmzTarget, EnableStageTransitionInput enableStageTransitionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling enableStageTransition(Async)");
        }

        // verify the required parameter 'enableStageTransitionInput' is set
        if (enableStageTransitionInput == null) {
            throw new ApiException("Missing the required parameter 'enableStageTransitionInput' when calling enableStageTransition(Async)");
        }

        return enableStageTransitionCall(xAmzTarget, enableStageTransitionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Enables artifacts in a pipeline to transition to a stage in a pipeline.
     * @param xAmzTarget  (required)
     * @param enableStageTransitionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> StageNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public void enableStageTransition(String xAmzTarget, EnableStageTransitionInput enableStageTransitionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        enableStageTransitionWithHttpInfo(xAmzTarget, enableStageTransitionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * Enables artifacts in a pipeline to transition to a stage in a pipeline.
     * @param xAmzTarget  (required)
     * @param enableStageTransitionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> StageNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> enableStageTransitionWithHttpInfo(String xAmzTarget, EnableStageTransitionInput enableStageTransitionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = enableStageTransitionValidateBeforeCall(xAmzTarget, enableStageTransitionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Enables artifacts in a pipeline to transition to a stage in a pipeline.
     * @param xAmzTarget  (required)
     * @param enableStageTransitionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> StageNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call enableStageTransitionAsync(String xAmzTarget, EnableStageTransitionInput enableStageTransitionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = enableStageTransitionValidateBeforeCall(xAmzTarget, enableStageTransitionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getActionType
     * @param xAmzTarget  (required)
     * @param getActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getActionTypeCall(String xAmzTarget, GetActionTypeInput getActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = getActionTypeInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.GetActionType";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getActionTypeValidateBeforeCall(String xAmzTarget, GetActionTypeInput getActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling getActionType(Async)");
        }

        // verify the required parameter 'getActionTypeInput' is set
        if (getActionTypeInput == null) {
            throw new ApiException("Missing the required parameter 'getActionTypeInput' when calling getActionType(Async)");
        }

        return getActionTypeCall(xAmzTarget, getActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Returns information about an action type created for an external provider, where the action is to be used by customers of the external provider. The action can be created with any supported integration model.
     * @param xAmzTarget  (required)
     * @param getActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetActionTypeOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public GetActionTypeOutput getActionType(String xAmzTarget, GetActionTypeInput getActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetActionTypeOutput> localVarResp = getActionTypeWithHttpInfo(xAmzTarget, getActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Returns information about an action type created for an external provider, where the action is to be used by customers of the external provider. The action can be created with any supported integration model.
     * @param xAmzTarget  (required)
     * @param getActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetActionTypeOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetActionTypeOutput> getActionTypeWithHttpInfo(String xAmzTarget, GetActionTypeInput getActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getActionTypeValidateBeforeCall(xAmzTarget, getActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetActionTypeOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Returns information about an action type created for an external provider, where the action is to be used by customers of the external provider. The action can be created with any supported integration model.
     * @param xAmzTarget  (required)
     * @param getActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getActionTypeAsync(String xAmzTarget, GetActionTypeInput getActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetActionTypeOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = getActionTypeValidateBeforeCall(xAmzTarget, getActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetActionTypeOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getJobDetails
     * @param xAmzTarget  (required)
     * @param getJobDetailsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getJobDetailsCall(String xAmzTarget, GetJobDetailsInput getJobDetailsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = getJobDetailsInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.GetJobDetails";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getJobDetailsValidateBeforeCall(String xAmzTarget, GetJobDetailsInput getJobDetailsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling getJobDetails(Async)");
        }

        // verify the required parameter 'getJobDetailsInput' is set
        if (getJobDetailsInput == null) {
            throw new ApiException("Missing the required parameter 'getJobDetailsInput' when calling getJobDetails(Async)");
        }

        return getJobDetailsCall(xAmzTarget, getJobDetailsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt;Returns information about a job. Used for custom actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param getJobDetailsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetJobDetailsOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public GetJobDetailsOutput getJobDetails(String xAmzTarget, GetJobDetailsInput getJobDetailsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetJobDetailsOutput> localVarResp = getJobDetailsWithHttpInfo(xAmzTarget, getJobDetailsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt;Returns information about a job. Used for custom actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param getJobDetailsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetJobDetailsOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetJobDetailsOutput> getJobDetailsWithHttpInfo(String xAmzTarget, GetJobDetailsInput getJobDetailsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getJobDetailsValidateBeforeCall(xAmzTarget, getJobDetailsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetJobDetailsOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Returns information about a job. Used for custom actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param getJobDetailsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getJobDetailsAsync(String xAmzTarget, GetJobDetailsInput getJobDetailsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetJobDetailsOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = getJobDetailsValidateBeforeCall(xAmzTarget, getJobDetailsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetJobDetailsOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getPipeline
     * @param xAmzTarget  (required)
     * @param getPipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineVersionNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPipelineCall(String xAmzTarget, GetPipelineInput getPipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = getPipelineInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.GetPipeline";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getPipelineValidateBeforeCall(String xAmzTarget, GetPipelineInput getPipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling getPipeline(Async)");
        }

        // verify the required parameter 'getPipelineInput' is set
        if (getPipelineInput == null) {
            throw new ApiException("Missing the required parameter 'getPipelineInput' when calling getPipeline(Async)");
        }

        return getPipelineCall(xAmzTarget, getPipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Returns the metadata, structure, stages, and actions of a pipeline. Can be used to return the entire structure of a pipeline in JSON format, which can then be modified and used to update the pipeline structure with &lt;a&gt;UpdatePipeline&lt;/a&gt;.
     * @param xAmzTarget  (required)
     * @param getPipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetPipelineOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineVersionNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public GetPipelineOutput getPipeline(String xAmzTarget, GetPipelineInput getPipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetPipelineOutput> localVarResp = getPipelineWithHttpInfo(xAmzTarget, getPipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Returns the metadata, structure, stages, and actions of a pipeline. Can be used to return the entire structure of a pipeline in JSON format, which can then be modified and used to update the pipeline structure with &lt;a&gt;UpdatePipeline&lt;/a&gt;.
     * @param xAmzTarget  (required)
     * @param getPipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetPipelineOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineVersionNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetPipelineOutput> getPipelineWithHttpInfo(String xAmzTarget, GetPipelineInput getPipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getPipelineValidateBeforeCall(xAmzTarget, getPipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetPipelineOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Returns the metadata, structure, stages, and actions of a pipeline. Can be used to return the entire structure of a pipeline in JSON format, which can then be modified and used to update the pipeline structure with &lt;a&gt;UpdatePipeline&lt;/a&gt;.
     * @param xAmzTarget  (required)
     * @param getPipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineVersionNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPipelineAsync(String xAmzTarget, GetPipelineInput getPipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetPipelineOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = getPipelineValidateBeforeCall(xAmzTarget, getPipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetPipelineOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getPipelineExecution
     * @param xAmzTarget  (required)
     * @param getPipelineExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineExecutionNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPipelineExecutionCall(String xAmzTarget, GetPipelineExecutionInput getPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = getPipelineExecutionInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.GetPipelineExecution";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getPipelineExecutionValidateBeforeCall(String xAmzTarget, GetPipelineExecutionInput getPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling getPipelineExecution(Async)");
        }

        // verify the required parameter 'getPipelineExecutionInput' is set
        if (getPipelineExecutionInput == null) {
            throw new ApiException("Missing the required parameter 'getPipelineExecutionInput' when calling getPipelineExecution(Async)");
        }

        return getPipelineExecutionCall(xAmzTarget, getPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Returns information about an execution of a pipeline, including details about artifacts, the pipeline execution ID, and the name, version, and status of the pipeline.
     * @param xAmzTarget  (required)
     * @param getPipelineExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetPipelineExecutionOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineExecutionNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public GetPipelineExecutionOutput getPipelineExecution(String xAmzTarget, GetPipelineExecutionInput getPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetPipelineExecutionOutput> localVarResp = getPipelineExecutionWithHttpInfo(xAmzTarget, getPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Returns information about an execution of a pipeline, including details about artifacts, the pipeline execution ID, and the name, version, and status of the pipeline.
     * @param xAmzTarget  (required)
     * @param getPipelineExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetPipelineExecutionOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineExecutionNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetPipelineExecutionOutput> getPipelineExecutionWithHttpInfo(String xAmzTarget, GetPipelineExecutionInput getPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getPipelineExecutionValidateBeforeCall(xAmzTarget, getPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetPipelineExecutionOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Returns information about an execution of a pipeline, including details about artifacts, the pipeline execution ID, and the name, version, and status of the pipeline.
     * @param xAmzTarget  (required)
     * @param getPipelineExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineExecutionNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPipelineExecutionAsync(String xAmzTarget, GetPipelineExecutionInput getPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetPipelineExecutionOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = getPipelineExecutionValidateBeforeCall(xAmzTarget, getPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetPipelineExecutionOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getPipelineState
     * @param xAmzTarget  (required)
     * @param getPipelineStateInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPipelineStateCall(String xAmzTarget, GetPipelineStateInput getPipelineStateInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = getPipelineStateInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.GetPipelineState";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getPipelineStateValidateBeforeCall(String xAmzTarget, GetPipelineStateInput getPipelineStateInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling getPipelineState(Async)");
        }

        // verify the required parameter 'getPipelineStateInput' is set
        if (getPipelineStateInput == null) {
            throw new ApiException("Missing the required parameter 'getPipelineStateInput' when calling getPipelineState(Async)");
        }

        return getPipelineStateCall(xAmzTarget, getPipelineStateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt;Returns information about the state of a pipeline, including the stages and actions.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Values returned in the &lt;code&gt;revisionId&lt;/code&gt; and &lt;code&gt;revisionUrl&lt;/code&gt; fields indicate the source revision information, such as the commit ID, for the current state.&lt;/p&gt; &lt;/note&gt;
     * @param xAmzTarget  (required)
     * @param getPipelineStateInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetPipelineStateOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public GetPipelineStateOutput getPipelineState(String xAmzTarget, GetPipelineStateInput getPipelineStateInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetPipelineStateOutput> localVarResp = getPipelineStateWithHttpInfo(xAmzTarget, getPipelineStateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt;Returns information about the state of a pipeline, including the stages and actions.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Values returned in the &lt;code&gt;revisionId&lt;/code&gt; and &lt;code&gt;revisionUrl&lt;/code&gt; fields indicate the source revision information, such as the commit ID, for the current state.&lt;/p&gt; &lt;/note&gt;
     * @param xAmzTarget  (required)
     * @param getPipelineStateInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetPipelineStateOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetPipelineStateOutput> getPipelineStateWithHttpInfo(String xAmzTarget, GetPipelineStateInput getPipelineStateInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getPipelineStateValidateBeforeCall(xAmzTarget, getPipelineStateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetPipelineStateOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Returns information about the state of a pipeline, including the stages and actions.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Values returned in the &lt;code&gt;revisionId&lt;/code&gt; and &lt;code&gt;revisionUrl&lt;/code&gt; fields indicate the source revision information, such as the commit ID, for the current state.&lt;/p&gt; &lt;/note&gt;
     * @param xAmzTarget  (required)
     * @param getPipelineStateInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPipelineStateAsync(String xAmzTarget, GetPipelineStateInput getPipelineStateInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetPipelineStateOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = getPipelineStateValidateBeforeCall(xAmzTarget, getPipelineStateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetPipelineStateOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getThirdPartyJobDetails
     * @param xAmzTarget  (required)
     * @param getThirdPartyJobDetailsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidJobException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getThirdPartyJobDetailsCall(String xAmzTarget, GetThirdPartyJobDetailsInput getThirdPartyJobDetailsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = getThirdPartyJobDetailsInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.GetThirdPartyJobDetails";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getThirdPartyJobDetailsValidateBeforeCall(String xAmzTarget, GetThirdPartyJobDetailsInput getThirdPartyJobDetailsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling getThirdPartyJobDetails(Async)");
        }

        // verify the required parameter 'getThirdPartyJobDetailsInput' is set
        if (getThirdPartyJobDetailsInput == null) {
            throw new ApiException("Missing the required parameter 'getThirdPartyJobDetailsInput' when calling getThirdPartyJobDetails(Async)");
        }

        return getThirdPartyJobDetailsCall(xAmzTarget, getThirdPartyJobDetailsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt;Requests the details of a job for a third party action. Used for partner actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param getThirdPartyJobDetailsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetThirdPartyJobDetailsOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidJobException </td><td>  -  </td></tr>
     </table>
     */
    public GetThirdPartyJobDetailsOutput getThirdPartyJobDetails(String xAmzTarget, GetThirdPartyJobDetailsInput getThirdPartyJobDetailsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetThirdPartyJobDetailsOutput> localVarResp = getThirdPartyJobDetailsWithHttpInfo(xAmzTarget, getThirdPartyJobDetailsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt;Requests the details of a job for a third party action. Used for partner actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param getThirdPartyJobDetailsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetThirdPartyJobDetailsOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidJobException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetThirdPartyJobDetailsOutput> getThirdPartyJobDetailsWithHttpInfo(String xAmzTarget, GetThirdPartyJobDetailsInput getThirdPartyJobDetailsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getThirdPartyJobDetailsValidateBeforeCall(xAmzTarget, getThirdPartyJobDetailsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetThirdPartyJobDetailsOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Requests the details of a job for a third party action. Used for partner actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param getThirdPartyJobDetailsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidJobException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getThirdPartyJobDetailsAsync(String xAmzTarget, GetThirdPartyJobDetailsInput getThirdPartyJobDetailsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetThirdPartyJobDetailsOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = getThirdPartyJobDetailsValidateBeforeCall(xAmzTarget, getThirdPartyJobDetailsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetThirdPartyJobDetailsOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listActionExecutions
     * @param xAmzTarget  (required)
     * @param listActionExecutionsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PipelineExecutionNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listActionExecutionsCall(String xAmzTarget, ListActionExecutionsInput listActionExecutionsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = listActionExecutionsInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.ListActionExecutions";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listActionExecutionsValidateBeforeCall(String xAmzTarget, ListActionExecutionsInput listActionExecutionsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling listActionExecutions(Async)");
        }

        // verify the required parameter 'listActionExecutionsInput' is set
        if (listActionExecutionsInput == null) {
            throw new ApiException("Missing the required parameter 'listActionExecutionsInput' when calling listActionExecutions(Async)");
        }

        return listActionExecutionsCall(xAmzTarget, listActionExecutionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     * Lists the action executions that have occurred in a pipeline.
     * @param xAmzTarget  (required)
     * @param listActionExecutionsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ListActionExecutionsOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PipelineExecutionNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ListActionExecutionsOutput listActionExecutions(String xAmzTarget, ListActionExecutionsInput listActionExecutionsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        ApiResponse<ListActionExecutionsOutput> localVarResp = listActionExecutionsWithHttpInfo(xAmzTarget, listActionExecutionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Lists the action executions that have occurred in a pipeline.
     * @param xAmzTarget  (required)
     * @param listActionExecutionsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListActionExecutionsOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PipelineExecutionNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListActionExecutionsOutput> listActionExecutionsWithHttpInfo(String xAmzTarget, ListActionExecutionsInput listActionExecutionsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listActionExecutionsValidateBeforeCall(xAmzTarget, listActionExecutionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<ListActionExecutionsOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Lists the action executions that have occurred in a pipeline.
     * @param xAmzTarget  (required)
     * @param listActionExecutionsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PipelineExecutionNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listActionExecutionsAsync(String xAmzTarget, ListActionExecutionsInput listActionExecutionsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback<ListActionExecutionsOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = listActionExecutionsValidateBeforeCall(xAmzTarget, listActionExecutionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListActionExecutionsOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listActionTypes
     * @param xAmzTarget  (required)
     * @param listActionTypesInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listActionTypesCall(String xAmzTarget, ListActionTypesInput listActionTypesInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String nextToken, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = listActionTypesInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.ListActionTypes";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listActionTypesValidateBeforeCall(String xAmzTarget, ListActionTypesInput listActionTypesInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling listActionTypes(Async)");
        }

        // verify the required parameter 'listActionTypesInput' is set
        if (listActionTypesInput == null) {
            throw new ApiException("Missing the required parameter 'listActionTypesInput' when calling listActionTypes(Async)");
        }

        return listActionTypesCall(xAmzTarget, listActionTypesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, _callback);

    }

    /**
     * 
     * Gets a summary of all CodePipeline action types associated with your account.
     * @param xAmzTarget  (required)
     * @param listActionTypesInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param nextToken Pagination token (optional)
     * @return ListActionTypesOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public ListActionTypesOutput listActionTypes(String xAmzTarget, ListActionTypesInput listActionTypesInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String nextToken) throws ApiException {
        ApiResponse<ListActionTypesOutput> localVarResp = listActionTypesWithHttpInfo(xAmzTarget, listActionTypesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets a summary of all CodePipeline action types associated with your account.
     * @param xAmzTarget  (required)
     * @param listActionTypesInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListActionTypesOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListActionTypesOutput> listActionTypesWithHttpInfo(String xAmzTarget, ListActionTypesInput listActionTypesInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listActionTypesValidateBeforeCall(xAmzTarget, listActionTypesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, null);
        Type localVarReturnType = new TypeToken<ListActionTypesOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets a summary of all CodePipeline action types associated with your account.
     * @param xAmzTarget  (required)
     * @param listActionTypesInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listActionTypesAsync(String xAmzTarget, ListActionTypesInput listActionTypesInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String nextToken, final ApiCallback<ListActionTypesOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = listActionTypesValidateBeforeCall(xAmzTarget, listActionTypesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListActionTypesOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listPipelineExecutions
     * @param xAmzTarget  (required)
     * @param listPipelineExecutionsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPipelineExecutionsCall(String xAmzTarget, ListPipelineExecutionsInput listPipelineExecutionsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = listPipelineExecutionsInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.ListPipelineExecutions";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listPipelineExecutionsValidateBeforeCall(String xAmzTarget, ListPipelineExecutionsInput listPipelineExecutionsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling listPipelineExecutions(Async)");
        }

        // verify the required parameter 'listPipelineExecutionsInput' is set
        if (listPipelineExecutionsInput == null) {
            throw new ApiException("Missing the required parameter 'listPipelineExecutionsInput' when calling listPipelineExecutions(Async)");
        }

        return listPipelineExecutionsCall(xAmzTarget, listPipelineExecutionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     * Gets a summary of the most recent executions for a pipeline.
     * @param xAmzTarget  (required)
     * @param listPipelineExecutionsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ListPipelineExecutionsOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public ListPipelineExecutionsOutput listPipelineExecutions(String xAmzTarget, ListPipelineExecutionsInput listPipelineExecutionsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        ApiResponse<ListPipelineExecutionsOutput> localVarResp = listPipelineExecutionsWithHttpInfo(xAmzTarget, listPipelineExecutionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets a summary of the most recent executions for a pipeline.
     * @param xAmzTarget  (required)
     * @param listPipelineExecutionsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListPipelineExecutionsOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListPipelineExecutionsOutput> listPipelineExecutionsWithHttpInfo(String xAmzTarget, ListPipelineExecutionsInput listPipelineExecutionsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listPipelineExecutionsValidateBeforeCall(xAmzTarget, listPipelineExecutionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<ListPipelineExecutionsOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets a summary of the most recent executions for a pipeline.
     * @param xAmzTarget  (required)
     * @param listPipelineExecutionsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPipelineExecutionsAsync(String xAmzTarget, ListPipelineExecutionsInput listPipelineExecutionsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback<ListPipelineExecutionsOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = listPipelineExecutionsValidateBeforeCall(xAmzTarget, listPipelineExecutionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListPipelineExecutionsOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listPipelines
     * @param xAmzTarget  (required)
     * @param listPipelinesInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPipelinesCall(String xAmzTarget, ListPipelinesInput listPipelinesInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = listPipelinesInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.ListPipelines";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listPipelinesValidateBeforeCall(String xAmzTarget, ListPipelinesInput listPipelinesInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling listPipelines(Async)");
        }

        // verify the required parameter 'listPipelinesInput' is set
        if (listPipelinesInput == null) {
            throw new ApiException("Missing the required parameter 'listPipelinesInput' when calling listPipelines(Async)");
        }

        return listPipelinesCall(xAmzTarget, listPipelinesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     * Gets a summary of all of the pipelines associated with your account.
     * @param xAmzTarget  (required)
     * @param listPipelinesInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ListPipelinesOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public ListPipelinesOutput listPipelines(String xAmzTarget, ListPipelinesInput listPipelinesInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        ApiResponse<ListPipelinesOutput> localVarResp = listPipelinesWithHttpInfo(xAmzTarget, listPipelinesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets a summary of all of the pipelines associated with your account.
     * @param xAmzTarget  (required)
     * @param listPipelinesInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListPipelinesOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListPipelinesOutput> listPipelinesWithHttpInfo(String xAmzTarget, ListPipelinesInput listPipelinesInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listPipelinesValidateBeforeCall(xAmzTarget, listPipelinesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<ListPipelinesOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets a summary of all of the pipelines associated with your account.
     * @param xAmzTarget  (required)
     * @param listPipelinesInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPipelinesAsync(String xAmzTarget, ListPipelinesInput listPipelinesInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback<ListPipelinesOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = listPipelinesValidateBeforeCall(xAmzTarget, listPipelinesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListPipelinesOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listTagsForResource
     * @param xAmzTarget  (required)
     * @param listTagsForResourceInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidArnException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTagsForResourceCall(String xAmzTarget, ListTagsForResourceInput listTagsForResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = listTagsForResourceInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.ListTagsForResource";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listTagsForResourceValidateBeforeCall(String xAmzTarget, ListTagsForResourceInput listTagsForResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling listTagsForResource(Async)");
        }

        // verify the required parameter 'listTagsForResourceInput' is set
        if (listTagsForResourceInput == null) {
            throw new ApiException("Missing the required parameter 'listTagsForResourceInput' when calling listTagsForResource(Async)");
        }

        return listTagsForResourceCall(xAmzTarget, listTagsForResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     * Gets the set of key-value pairs (metadata) that are used to manage the resource.
     * @param xAmzTarget  (required)
     * @param listTagsForResourceInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ListTagsForResourceOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidArnException </td><td>  -  </td></tr>
     </table>
     */
    public ListTagsForResourceOutput listTagsForResource(String xAmzTarget, ListTagsForResourceInput listTagsForResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        ApiResponse<ListTagsForResourceOutput> localVarResp = listTagsForResourceWithHttpInfo(xAmzTarget, listTagsForResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets the set of key-value pairs (metadata) that are used to manage the resource.
     * @param xAmzTarget  (required)
     * @param listTagsForResourceInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListTagsForResourceOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidArnException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListTagsForResourceOutput> listTagsForResourceWithHttpInfo(String xAmzTarget, ListTagsForResourceInput listTagsForResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listTagsForResourceValidateBeforeCall(xAmzTarget, listTagsForResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<ListTagsForResourceOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets the set of key-value pairs (metadata) that are used to manage the resource.
     * @param xAmzTarget  (required)
     * @param listTagsForResourceInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidArnException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTagsForResourceAsync(String xAmzTarget, ListTagsForResourceInput listTagsForResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback<ListTagsForResourceOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = listTagsForResourceValidateBeforeCall(xAmzTarget, listTagsForResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListTagsForResourceOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listWebhooks
     * @param xAmzTarget  (required)
     * @param listWebhooksInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listWebhooksCall(String xAmzTarget, ListWebhooksInput listWebhooksInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = listWebhooksInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.ListWebhooks";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("MaxResults", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("NextToken", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listWebhooksValidateBeforeCall(String xAmzTarget, ListWebhooksInput listWebhooksInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling listWebhooks(Async)");
        }

        // verify the required parameter 'listWebhooksInput' is set
        if (listWebhooksInput == null) {
            throw new ApiException("Missing the required parameter 'listWebhooksInput' when calling listWebhooks(Async)");
        }

        return listWebhooksCall(xAmzTarget, listWebhooksInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     * Gets a listing of all the webhooks in this Amazon Web Services Region for this account. The output lists all webhooks and includes the webhook URL and ARN and the configuration for each webhook.
     * @param xAmzTarget  (required)
     * @param listWebhooksInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ListWebhooksOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public ListWebhooksOutput listWebhooks(String xAmzTarget, ListWebhooksInput listWebhooksInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        ApiResponse<ListWebhooksOutput> localVarResp = listWebhooksWithHttpInfo(xAmzTarget, listWebhooksInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets a listing of all the webhooks in this Amazon Web Services Region for this account. The output lists all webhooks and includes the webhook URL and ARN and the configuration for each webhook.
     * @param xAmzTarget  (required)
     * @param listWebhooksInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListWebhooksOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListWebhooksOutput> listWebhooksWithHttpInfo(String xAmzTarget, ListWebhooksInput listWebhooksInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listWebhooksValidateBeforeCall(xAmzTarget, listWebhooksInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<ListWebhooksOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets a listing of all the webhooks in this Amazon Web Services Region for this account. The output lists all webhooks and includes the webhook URL and ARN and the configuration for each webhook.
     * @param xAmzTarget  (required)
     * @param listWebhooksInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidNextTokenException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listWebhooksAsync(String xAmzTarget, ListWebhooksInput listWebhooksInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback<ListWebhooksOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = listWebhooksValidateBeforeCall(xAmzTarget, listWebhooksInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListWebhooksOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for pollForJobs
     * @param xAmzTarget  (required)
     * @param pollForJobsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call pollForJobsCall(String xAmzTarget, PollForJobsInput pollForJobsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = pollForJobsInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.PollForJobs";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call pollForJobsValidateBeforeCall(String xAmzTarget, PollForJobsInput pollForJobsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling pollForJobs(Async)");
        }

        // verify the required parameter 'pollForJobsInput' is set
        if (pollForJobsInput == null) {
            throw new ApiException("Missing the required parameter 'pollForJobsInput' when calling pollForJobs(Async)");
        }

        return pollForJobsCall(xAmzTarget, pollForJobsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt;Returns information about any jobs for CodePipeline to act on. &lt;code&gt;PollForJobs&lt;/code&gt; is valid only for action types with \&quot;Custom\&quot; in the owner field. If the action type contains &lt;code&gt;AWS&lt;/code&gt; or &lt;code&gt;ThirdParty&lt;/code&gt; in the owner field, the &lt;code&gt;PollForJobs&lt;/code&gt; action returns an error.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param pollForJobsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return PollForJobsOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public PollForJobsOutput pollForJobs(String xAmzTarget, PollForJobsInput pollForJobsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<PollForJobsOutput> localVarResp = pollForJobsWithHttpInfo(xAmzTarget, pollForJobsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt;Returns information about any jobs for CodePipeline to act on. &lt;code&gt;PollForJobs&lt;/code&gt; is valid only for action types with \&quot;Custom\&quot; in the owner field. If the action type contains &lt;code&gt;AWS&lt;/code&gt; or &lt;code&gt;ThirdParty&lt;/code&gt; in the owner field, the &lt;code&gt;PollForJobs&lt;/code&gt; action returns an error.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param pollForJobsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;PollForJobsOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PollForJobsOutput> pollForJobsWithHttpInfo(String xAmzTarget, PollForJobsInput pollForJobsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = pollForJobsValidateBeforeCall(xAmzTarget, pollForJobsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<PollForJobsOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Returns information about any jobs for CodePipeline to act on. &lt;code&gt;PollForJobs&lt;/code&gt; is valid only for action types with \&quot;Custom\&quot; in the owner field. If the action type contains &lt;code&gt;AWS&lt;/code&gt; or &lt;code&gt;ThirdParty&lt;/code&gt; in the owner field, the &lt;code&gt;PollForJobs&lt;/code&gt; action returns an error.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param pollForJobsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call pollForJobsAsync(String xAmzTarget, PollForJobsInput pollForJobsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<PollForJobsOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = pollForJobsValidateBeforeCall(xAmzTarget, pollForJobsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<PollForJobsOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for pollForThirdPartyJobs
     * @param xAmzTarget  (required)
     * @param pollForThirdPartyJobsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call pollForThirdPartyJobsCall(String xAmzTarget, PollForThirdPartyJobsInput pollForThirdPartyJobsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = pollForThirdPartyJobsInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.PollForThirdPartyJobs";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call pollForThirdPartyJobsValidateBeforeCall(String xAmzTarget, PollForThirdPartyJobsInput pollForThirdPartyJobsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling pollForThirdPartyJobs(Async)");
        }

        // verify the required parameter 'pollForThirdPartyJobsInput' is set
        if (pollForThirdPartyJobsInput == null) {
            throw new ApiException("Missing the required parameter 'pollForThirdPartyJobsInput' when calling pollForThirdPartyJobs(Async)");
        }

        return pollForThirdPartyJobsCall(xAmzTarget, pollForThirdPartyJobsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt;Determines whether there are any third party jobs for a job worker to act on. Used for partner actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param pollForThirdPartyJobsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return PollForThirdPartyJobsOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public PollForThirdPartyJobsOutput pollForThirdPartyJobs(String xAmzTarget, PollForThirdPartyJobsInput pollForThirdPartyJobsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<PollForThirdPartyJobsOutput> localVarResp = pollForThirdPartyJobsWithHttpInfo(xAmzTarget, pollForThirdPartyJobsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt;Determines whether there are any third party jobs for a job worker to act on. Used for partner actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param pollForThirdPartyJobsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;PollForThirdPartyJobsOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PollForThirdPartyJobsOutput> pollForThirdPartyJobsWithHttpInfo(String xAmzTarget, PollForThirdPartyJobsInput pollForThirdPartyJobsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = pollForThirdPartyJobsValidateBeforeCall(xAmzTarget, pollForThirdPartyJobsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<PollForThirdPartyJobsOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Determines whether there are any third party jobs for a job worker to act on. Used for partner actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts.&lt;/p&gt; &lt;/important&gt;
     * @param xAmzTarget  (required)
     * @param pollForThirdPartyJobsInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call pollForThirdPartyJobsAsync(String xAmzTarget, PollForThirdPartyJobsInput pollForThirdPartyJobsInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<PollForThirdPartyJobsOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = pollForThirdPartyJobsValidateBeforeCall(xAmzTarget, pollForThirdPartyJobsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<PollForThirdPartyJobsOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putActionRevision
     * @param xAmzTarget  (required)
     * @param putActionRevisionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> StageNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ActionNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putActionRevisionCall(String xAmzTarget, PutActionRevisionInput putActionRevisionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = putActionRevisionInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.PutActionRevision";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putActionRevisionValidateBeforeCall(String xAmzTarget, PutActionRevisionInput putActionRevisionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling putActionRevision(Async)");
        }

        // verify the required parameter 'putActionRevisionInput' is set
        if (putActionRevisionInput == null) {
            throw new ApiException("Missing the required parameter 'putActionRevisionInput' when calling putActionRevision(Async)");
        }

        return putActionRevisionCall(xAmzTarget, putActionRevisionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Provides information to CodePipeline about new revisions to a source.
     * @param xAmzTarget  (required)
     * @param putActionRevisionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return PutActionRevisionOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> StageNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ActionNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public PutActionRevisionOutput putActionRevision(String xAmzTarget, PutActionRevisionInput putActionRevisionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<PutActionRevisionOutput> localVarResp = putActionRevisionWithHttpInfo(xAmzTarget, putActionRevisionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Provides information to CodePipeline about new revisions to a source.
     * @param xAmzTarget  (required)
     * @param putActionRevisionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;PutActionRevisionOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> StageNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ActionNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PutActionRevisionOutput> putActionRevisionWithHttpInfo(String xAmzTarget, PutActionRevisionInput putActionRevisionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = putActionRevisionValidateBeforeCall(xAmzTarget, putActionRevisionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<PutActionRevisionOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Provides information to CodePipeline about new revisions to a source.
     * @param xAmzTarget  (required)
     * @param putActionRevisionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> StageNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ActionNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putActionRevisionAsync(String xAmzTarget, PutActionRevisionInput putActionRevisionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<PutActionRevisionOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = putActionRevisionValidateBeforeCall(xAmzTarget, putActionRevisionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<PutActionRevisionOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putApprovalResult
     * @param xAmzTarget  (required)
     * @param putApprovalResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> InvalidApprovalTokenException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ApprovalAlreadyCompletedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> StageNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ActionNotFoundException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putApprovalResultCall(String xAmzTarget, PutApprovalResultInput putApprovalResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = putApprovalResultInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.PutApprovalResult";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putApprovalResultValidateBeforeCall(String xAmzTarget, PutApprovalResultInput putApprovalResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling putApprovalResult(Async)");
        }

        // verify the required parameter 'putApprovalResultInput' is set
        if (putApprovalResultInput == null) {
            throw new ApiException("Missing the required parameter 'putApprovalResultInput' when calling putApprovalResult(Async)");
        }

        return putApprovalResultCall(xAmzTarget, putApprovalResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Provides the response to a manual approval request to CodePipeline. Valid responses include Approved and Rejected.
     * @param xAmzTarget  (required)
     * @param putApprovalResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return PutApprovalResultOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> InvalidApprovalTokenException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ApprovalAlreadyCompletedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> StageNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ActionNotFoundException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public PutApprovalResultOutput putApprovalResult(String xAmzTarget, PutApprovalResultInput putApprovalResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<PutApprovalResultOutput> localVarResp = putApprovalResultWithHttpInfo(xAmzTarget, putApprovalResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Provides the response to a manual approval request to CodePipeline. Valid responses include Approved and Rejected.
     * @param xAmzTarget  (required)
     * @param putApprovalResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;PutApprovalResultOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> InvalidApprovalTokenException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ApprovalAlreadyCompletedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> StageNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ActionNotFoundException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PutApprovalResultOutput> putApprovalResultWithHttpInfo(String xAmzTarget, PutApprovalResultInput putApprovalResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = putApprovalResultValidateBeforeCall(xAmzTarget, putApprovalResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<PutApprovalResultOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Provides the response to a manual approval request to CodePipeline. Valid responses include Approved and Rejected.
     * @param xAmzTarget  (required)
     * @param putApprovalResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> InvalidApprovalTokenException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ApprovalAlreadyCompletedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> StageNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ActionNotFoundException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putApprovalResultAsync(String xAmzTarget, PutApprovalResultInput putApprovalResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<PutApprovalResultOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = putApprovalResultValidateBeforeCall(xAmzTarget, putApprovalResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<PutApprovalResultOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putJobFailureResult
     * @param xAmzTarget  (required)
     * @param putJobFailureResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putJobFailureResultCall(String xAmzTarget, PutJobFailureResultInput putJobFailureResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = putJobFailureResultInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.PutJobFailureResult";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putJobFailureResultValidateBeforeCall(String xAmzTarget, PutJobFailureResultInput putJobFailureResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling putJobFailureResult(Async)");
        }

        // verify the required parameter 'putJobFailureResultInput' is set
        if (putJobFailureResultInput == null) {
            throw new ApiException("Missing the required parameter 'putJobFailureResultInput' when calling putJobFailureResult(Async)");
        }

        return putJobFailureResultCall(xAmzTarget, putJobFailureResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Represents the failure of a job as returned to the pipeline by a job worker. Used for custom actions only.
     * @param xAmzTarget  (required)
     * @param putJobFailureResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
     </table>
     */
    public void putJobFailureResult(String xAmzTarget, PutJobFailureResultInput putJobFailureResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        putJobFailureResultWithHttpInfo(xAmzTarget, putJobFailureResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * Represents the failure of a job as returned to the pipeline by a job worker. Used for custom actions only.
     * @param xAmzTarget  (required)
     * @param putJobFailureResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> putJobFailureResultWithHttpInfo(String xAmzTarget, PutJobFailureResultInput putJobFailureResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = putJobFailureResultValidateBeforeCall(xAmzTarget, putJobFailureResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Represents the failure of a job as returned to the pipeline by a job worker. Used for custom actions only.
     * @param xAmzTarget  (required)
     * @param putJobFailureResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putJobFailureResultAsync(String xAmzTarget, PutJobFailureResultInput putJobFailureResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = putJobFailureResultValidateBeforeCall(xAmzTarget, putJobFailureResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for putJobSuccessResult
     * @param xAmzTarget  (required)
     * @param putJobSuccessResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> OutputVariablesSizeExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putJobSuccessResultCall(String xAmzTarget, PutJobSuccessResultInput putJobSuccessResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = putJobSuccessResultInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.PutJobSuccessResult";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putJobSuccessResultValidateBeforeCall(String xAmzTarget, PutJobSuccessResultInput putJobSuccessResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling putJobSuccessResult(Async)");
        }

        // verify the required parameter 'putJobSuccessResultInput' is set
        if (putJobSuccessResultInput == null) {
            throw new ApiException("Missing the required parameter 'putJobSuccessResultInput' when calling putJobSuccessResult(Async)");
        }

        return putJobSuccessResultCall(xAmzTarget, putJobSuccessResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Represents the success of a job as returned to the pipeline by a job worker. Used for custom actions only.
     * @param xAmzTarget  (required)
     * @param putJobSuccessResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> OutputVariablesSizeExceededException </td><td>  -  </td></tr>
     </table>
     */
    public void putJobSuccessResult(String xAmzTarget, PutJobSuccessResultInput putJobSuccessResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        putJobSuccessResultWithHttpInfo(xAmzTarget, putJobSuccessResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * Represents the success of a job as returned to the pipeline by a job worker. Used for custom actions only.
     * @param xAmzTarget  (required)
     * @param putJobSuccessResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> OutputVariablesSizeExceededException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> putJobSuccessResultWithHttpInfo(String xAmzTarget, PutJobSuccessResultInput putJobSuccessResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = putJobSuccessResultValidateBeforeCall(xAmzTarget, putJobSuccessResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Represents the success of a job as returned to the pipeline by a job worker. Used for custom actions only.
     * @param xAmzTarget  (required)
     * @param putJobSuccessResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> OutputVariablesSizeExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putJobSuccessResultAsync(String xAmzTarget, PutJobSuccessResultInput putJobSuccessResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = putJobSuccessResultValidateBeforeCall(xAmzTarget, putJobSuccessResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for putThirdPartyJobFailureResult
     * @param xAmzTarget  (required)
     * @param putThirdPartyJobFailureResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putThirdPartyJobFailureResultCall(String xAmzTarget, PutThirdPartyJobFailureResultInput putThirdPartyJobFailureResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = putThirdPartyJobFailureResultInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.PutThirdPartyJobFailureResult";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putThirdPartyJobFailureResultValidateBeforeCall(String xAmzTarget, PutThirdPartyJobFailureResultInput putThirdPartyJobFailureResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling putThirdPartyJobFailureResult(Async)");
        }

        // verify the required parameter 'putThirdPartyJobFailureResultInput' is set
        if (putThirdPartyJobFailureResultInput == null) {
            throw new ApiException("Missing the required parameter 'putThirdPartyJobFailureResultInput' when calling putThirdPartyJobFailureResult(Async)");
        }

        return putThirdPartyJobFailureResultCall(xAmzTarget, putThirdPartyJobFailureResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Represents the failure of a third party job as returned to the pipeline by a job worker. Used for partner actions only.
     * @param xAmzTarget  (required)
     * @param putThirdPartyJobFailureResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
     </table>
     */
    public void putThirdPartyJobFailureResult(String xAmzTarget, PutThirdPartyJobFailureResultInput putThirdPartyJobFailureResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        putThirdPartyJobFailureResultWithHttpInfo(xAmzTarget, putThirdPartyJobFailureResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * Represents the failure of a third party job as returned to the pipeline by a job worker. Used for partner actions only.
     * @param xAmzTarget  (required)
     * @param putThirdPartyJobFailureResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> putThirdPartyJobFailureResultWithHttpInfo(String xAmzTarget, PutThirdPartyJobFailureResultInput putThirdPartyJobFailureResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = putThirdPartyJobFailureResultValidateBeforeCall(xAmzTarget, putThirdPartyJobFailureResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Represents the failure of a third party job as returned to the pipeline by a job worker. Used for partner actions only.
     * @param xAmzTarget  (required)
     * @param putThirdPartyJobFailureResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putThirdPartyJobFailureResultAsync(String xAmzTarget, PutThirdPartyJobFailureResultInput putThirdPartyJobFailureResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = putThirdPartyJobFailureResultValidateBeforeCall(xAmzTarget, putThirdPartyJobFailureResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for putThirdPartyJobSuccessResult
     * @param xAmzTarget  (required)
     * @param putThirdPartyJobSuccessResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putThirdPartyJobSuccessResultCall(String xAmzTarget, PutThirdPartyJobSuccessResultInput putThirdPartyJobSuccessResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = putThirdPartyJobSuccessResultInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.PutThirdPartyJobSuccessResult";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putThirdPartyJobSuccessResultValidateBeforeCall(String xAmzTarget, PutThirdPartyJobSuccessResultInput putThirdPartyJobSuccessResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling putThirdPartyJobSuccessResult(Async)");
        }

        // verify the required parameter 'putThirdPartyJobSuccessResultInput' is set
        if (putThirdPartyJobSuccessResultInput == null) {
            throw new ApiException("Missing the required parameter 'putThirdPartyJobSuccessResultInput' when calling putThirdPartyJobSuccessResult(Async)");
        }

        return putThirdPartyJobSuccessResultCall(xAmzTarget, putThirdPartyJobSuccessResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Represents the success of a third party job as returned to the pipeline by a job worker. Used for partner actions only.
     * @param xAmzTarget  (required)
     * @param putThirdPartyJobSuccessResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
     </table>
     */
    public void putThirdPartyJobSuccessResult(String xAmzTarget, PutThirdPartyJobSuccessResultInput putThirdPartyJobSuccessResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        putThirdPartyJobSuccessResultWithHttpInfo(xAmzTarget, putThirdPartyJobSuccessResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * Represents the success of a third party job as returned to the pipeline by a job worker. Used for partner actions only.
     * @param xAmzTarget  (required)
     * @param putThirdPartyJobSuccessResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> putThirdPartyJobSuccessResultWithHttpInfo(String xAmzTarget, PutThirdPartyJobSuccessResultInput putThirdPartyJobSuccessResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = putThirdPartyJobSuccessResultValidateBeforeCall(xAmzTarget, putThirdPartyJobSuccessResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Represents the success of a third party job as returned to the pipeline by a job worker. Used for partner actions only.
     * @param xAmzTarget  (required)
     * @param putThirdPartyJobSuccessResultInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> JobNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidJobStateException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidClientTokenException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putThirdPartyJobSuccessResultAsync(String xAmzTarget, PutThirdPartyJobSuccessResultInput putThirdPartyJobSuccessResultInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = putThirdPartyJobSuccessResultValidateBeforeCall(xAmzTarget, putThirdPartyJobSuccessResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for putWebhook
     * @param xAmzTarget  (required)
     * @param putWebhookInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> LimitExceededException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidWebhookFilterPatternException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidWebhookAuthenticationParametersException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 487 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putWebhookCall(String xAmzTarget, PutWebhookInput putWebhookInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = putWebhookInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.PutWebhook";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putWebhookValidateBeforeCall(String xAmzTarget, PutWebhookInput putWebhookInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling putWebhook(Async)");
        }

        // verify the required parameter 'putWebhookInput' is set
        if (putWebhookInput == null) {
            throw new ApiException("Missing the required parameter 'putWebhookInput' when calling putWebhook(Async)");
        }

        return putWebhookCall(xAmzTarget, putWebhookInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Defines a webhook and returns a unique webhook URL generated by CodePipeline. This URL can be supplied to third party source hosting providers to call every time there&#39;s a code change. When CodePipeline receives a POST request on this URL, the pipeline defined in the webhook is started as long as the POST request satisfied the authentication and filtering requirements supplied when defining the webhook. RegisterWebhookWithThirdParty and DeregisterWebhookWithThirdParty APIs can be used to automatically configure supported third parties to call the generated webhook URL.
     * @param xAmzTarget  (required)
     * @param putWebhookInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return PutWebhookOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> LimitExceededException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidWebhookFilterPatternException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidWebhookAuthenticationParametersException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 487 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public PutWebhookOutput putWebhook(String xAmzTarget, PutWebhookInput putWebhookInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<PutWebhookOutput> localVarResp = putWebhookWithHttpInfo(xAmzTarget, putWebhookInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Defines a webhook and returns a unique webhook URL generated by CodePipeline. This URL can be supplied to third party source hosting providers to call every time there&#39;s a code change. When CodePipeline receives a POST request on this URL, the pipeline defined in the webhook is started as long as the POST request satisfied the authentication and filtering requirements supplied when defining the webhook. RegisterWebhookWithThirdParty and DeregisterWebhookWithThirdParty APIs can be used to automatically configure supported third parties to call the generated webhook URL.
     * @param xAmzTarget  (required)
     * @param putWebhookInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;PutWebhookOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> LimitExceededException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidWebhookFilterPatternException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidWebhookAuthenticationParametersException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 487 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PutWebhookOutput> putWebhookWithHttpInfo(String xAmzTarget, PutWebhookInput putWebhookInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = putWebhookValidateBeforeCall(xAmzTarget, putWebhookInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<PutWebhookOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Defines a webhook and returns a unique webhook URL generated by CodePipeline. This URL can be supplied to third party source hosting providers to call every time there&#39;s a code change. When CodePipeline receives a POST request on this URL, the pipeline defined in the webhook is started as long as the POST request satisfied the authentication and filtering requirements supplied when defining the webhook. RegisterWebhookWithThirdParty and DeregisterWebhookWithThirdParty APIs can be used to automatically configure supported third parties to call the generated webhook URL.
     * @param xAmzTarget  (required)
     * @param putWebhookInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> LimitExceededException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidWebhookFilterPatternException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidWebhookAuthenticationParametersException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 487 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putWebhookAsync(String xAmzTarget, PutWebhookInput putWebhookInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<PutWebhookOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = putWebhookValidateBeforeCall(xAmzTarget, putWebhookInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<PutWebhookOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for registerWebhookWithThirdParty
     * @param xAmzTarget  (required)
     * @param registerWebhookWithThirdPartyInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> WebhookNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call registerWebhookWithThirdPartyCall(String xAmzTarget, RegisterWebhookWithThirdPartyInput registerWebhookWithThirdPartyInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = registerWebhookWithThirdPartyInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.RegisterWebhookWithThirdParty";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call registerWebhookWithThirdPartyValidateBeforeCall(String xAmzTarget, RegisterWebhookWithThirdPartyInput registerWebhookWithThirdPartyInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling registerWebhookWithThirdParty(Async)");
        }

        // verify the required parameter 'registerWebhookWithThirdPartyInput' is set
        if (registerWebhookWithThirdPartyInput == null) {
            throw new ApiException("Missing the required parameter 'registerWebhookWithThirdPartyInput' when calling registerWebhookWithThirdParty(Async)");
        }

        return registerWebhookWithThirdPartyCall(xAmzTarget, registerWebhookWithThirdPartyInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Configures a connection between the webhook that was created and the external tool with events to be detected.
     * @param xAmzTarget  (required)
     * @param registerWebhookWithThirdPartyInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> WebhookNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public Object registerWebhookWithThirdParty(String xAmzTarget, RegisterWebhookWithThirdPartyInput registerWebhookWithThirdPartyInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = registerWebhookWithThirdPartyWithHttpInfo(xAmzTarget, registerWebhookWithThirdPartyInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Configures a connection between the webhook that was created and the external tool with events to be detected.
     * @param xAmzTarget  (required)
     * @param registerWebhookWithThirdPartyInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> WebhookNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> registerWebhookWithThirdPartyWithHttpInfo(String xAmzTarget, RegisterWebhookWithThirdPartyInput registerWebhookWithThirdPartyInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = registerWebhookWithThirdPartyValidateBeforeCall(xAmzTarget, registerWebhookWithThirdPartyInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Configures a connection between the webhook that was created and the external tool with events to be detected.
     * @param xAmzTarget  (required)
     * @param registerWebhookWithThirdPartyInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> WebhookNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call registerWebhookWithThirdPartyAsync(String xAmzTarget, RegisterWebhookWithThirdPartyInput registerWebhookWithThirdPartyInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = registerWebhookWithThirdPartyValidateBeforeCall(xAmzTarget, registerWebhookWithThirdPartyInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for retryStageExecution
     * @param xAmzTarget  (required)
     * @param retryStageExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> StageNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> StageNotRetryableException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> NotLatestPipelineExecutionException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call retryStageExecutionCall(String xAmzTarget, RetryStageExecutionInput retryStageExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = retryStageExecutionInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.RetryStageExecution";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call retryStageExecutionValidateBeforeCall(String xAmzTarget, RetryStageExecutionInput retryStageExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling retryStageExecution(Async)");
        }

        // verify the required parameter 'retryStageExecutionInput' is set
        if (retryStageExecutionInput == null) {
            throw new ApiException("Missing the required parameter 'retryStageExecutionInput' when calling retryStageExecution(Async)");
        }

        return retryStageExecutionCall(xAmzTarget, retryStageExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Resumes the pipeline execution by retrying the last failed actions in a stage. You can retry a stage immediately if any of the actions in the stage fail. When you retry, all actions that are still in progress continue working, and failed actions are triggered again.
     * @param xAmzTarget  (required)
     * @param retryStageExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return RetryStageExecutionOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> StageNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> StageNotRetryableException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> NotLatestPipelineExecutionException </td><td>  -  </td></tr>
     </table>
     */
    public RetryStageExecutionOutput retryStageExecution(String xAmzTarget, RetryStageExecutionInput retryStageExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<RetryStageExecutionOutput> localVarResp = retryStageExecutionWithHttpInfo(xAmzTarget, retryStageExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Resumes the pipeline execution by retrying the last failed actions in a stage. You can retry a stage immediately if any of the actions in the stage fail. When you retry, all actions that are still in progress continue working, and failed actions are triggered again.
     * @param xAmzTarget  (required)
     * @param retryStageExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;RetryStageExecutionOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> StageNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> StageNotRetryableException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> NotLatestPipelineExecutionException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<RetryStageExecutionOutput> retryStageExecutionWithHttpInfo(String xAmzTarget, RetryStageExecutionInput retryStageExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = retryStageExecutionValidateBeforeCall(xAmzTarget, retryStageExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<RetryStageExecutionOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Resumes the pipeline execution by retrying the last failed actions in a stage. You can retry a stage immediately if any of the actions in the stage fail. When you retry, all actions that are still in progress continue working, and failed actions are triggered again.
     * @param xAmzTarget  (required)
     * @param retryStageExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> StageNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> StageNotRetryableException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> NotLatestPipelineExecutionException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call retryStageExecutionAsync(String xAmzTarget, RetryStageExecutionInput retryStageExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<RetryStageExecutionOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = retryStageExecutionValidateBeforeCall(xAmzTarget, retryStageExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<RetryStageExecutionOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for startPipelineExecution
     * @param xAmzTarget  (required)
     * @param startPipelineExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call startPipelineExecutionCall(String xAmzTarget, StartPipelineExecutionInput startPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = startPipelineExecutionInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.StartPipelineExecution";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call startPipelineExecutionValidateBeforeCall(String xAmzTarget, StartPipelineExecutionInput startPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling startPipelineExecution(Async)");
        }

        // verify the required parameter 'startPipelineExecutionInput' is set
        if (startPipelineExecutionInput == null) {
            throw new ApiException("Missing the required parameter 'startPipelineExecutionInput' when calling startPipelineExecution(Async)");
        }

        return startPipelineExecutionCall(xAmzTarget, startPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Starts the specified pipeline. Specifically, it begins processing the latest commit to the source location specified as part of the pipeline.
     * @param xAmzTarget  (required)
     * @param startPipelineExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return StartPipelineExecutionOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public StartPipelineExecutionOutput startPipelineExecution(String xAmzTarget, StartPipelineExecutionInput startPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<StartPipelineExecutionOutput> localVarResp = startPipelineExecutionWithHttpInfo(xAmzTarget, startPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Starts the specified pipeline. Specifically, it begins processing the latest commit to the source location specified as part of the pipeline.
     * @param xAmzTarget  (required)
     * @param startPipelineExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;StartPipelineExecutionOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<StartPipelineExecutionOutput> startPipelineExecutionWithHttpInfo(String xAmzTarget, StartPipelineExecutionInput startPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = startPipelineExecutionValidateBeforeCall(xAmzTarget, startPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<StartPipelineExecutionOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Starts the specified pipeline. Specifically, it begins processing the latest commit to the source location specified as part of the pipeline.
     * @param xAmzTarget  (required)
     * @param startPipelineExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call startPipelineExecutionAsync(String xAmzTarget, StartPipelineExecutionInput startPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<StartPipelineExecutionOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = startPipelineExecutionValidateBeforeCall(xAmzTarget, startPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<StartPipelineExecutionOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for stopPipelineExecution
     * @param xAmzTarget  (required)
     * @param stopPipelineExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PipelineExecutionNotStoppableException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> DuplicatedStopRequestException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call stopPipelineExecutionCall(String xAmzTarget, StopPipelineExecutionInput stopPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = stopPipelineExecutionInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.StopPipelineExecution";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call stopPipelineExecutionValidateBeforeCall(String xAmzTarget, StopPipelineExecutionInput stopPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling stopPipelineExecution(Async)");
        }

        // verify the required parameter 'stopPipelineExecutionInput' is set
        if (stopPipelineExecutionInput == null) {
            throw new ApiException("Missing the required parameter 'stopPipelineExecutionInput' when calling stopPipelineExecution(Async)");
        }

        return stopPipelineExecutionCall(xAmzTarget, stopPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Stops the specified pipeline execution. You choose to either stop the pipeline execution by completing in-progress actions without starting subsequent actions, or by abandoning in-progress actions. While completing or abandoning in-progress actions, the pipeline execution is in a &lt;code&gt;Stopping&lt;/code&gt; state. After all in-progress actions are completed or abandoned, the pipeline execution is in a &lt;code&gt;Stopped&lt;/code&gt; state.
     * @param xAmzTarget  (required)
     * @param stopPipelineExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return StopPipelineExecutionOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PipelineExecutionNotStoppableException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> DuplicatedStopRequestException </td><td>  -  </td></tr>
     </table>
     */
    public StopPipelineExecutionOutput stopPipelineExecution(String xAmzTarget, StopPipelineExecutionInput stopPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<StopPipelineExecutionOutput> localVarResp = stopPipelineExecutionWithHttpInfo(xAmzTarget, stopPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Stops the specified pipeline execution. You choose to either stop the pipeline execution by completing in-progress actions without starting subsequent actions, or by abandoning in-progress actions. While completing or abandoning in-progress actions, the pipeline execution is in a &lt;code&gt;Stopping&lt;/code&gt; state. After all in-progress actions are completed or abandoned, the pipeline execution is in a &lt;code&gt;Stopped&lt;/code&gt; state.
     * @param xAmzTarget  (required)
     * @param stopPipelineExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;StopPipelineExecutionOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PipelineExecutionNotStoppableException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> DuplicatedStopRequestException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<StopPipelineExecutionOutput> stopPipelineExecutionWithHttpInfo(String xAmzTarget, StopPipelineExecutionInput stopPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = stopPipelineExecutionValidateBeforeCall(xAmzTarget, stopPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<StopPipelineExecutionOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Stops the specified pipeline execution. You choose to either stop the pipeline execution by completing in-progress actions without starting subsequent actions, or by abandoning in-progress actions. While completing or abandoning in-progress actions, the pipeline execution is in a &lt;code&gt;Stopping&lt;/code&gt; state. After all in-progress actions are completed or abandoned, the pipeline execution is in a &lt;code&gt;Stopped&lt;/code&gt; state.
     * @param xAmzTarget  (required)
     * @param stopPipelineExecutionInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PipelineNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PipelineExecutionNotStoppableException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> DuplicatedStopRequestException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call stopPipelineExecutionAsync(String xAmzTarget, StopPipelineExecutionInput stopPipelineExecutionInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<StopPipelineExecutionOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = stopPipelineExecutionValidateBeforeCall(xAmzTarget, stopPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<StopPipelineExecutionOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for tagResource
     * @param xAmzTarget  (required)
     * @param tagResourceInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidArnException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call tagResourceCall(String xAmzTarget, TagResourceInput tagResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = tagResourceInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.TagResource";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call tagResourceValidateBeforeCall(String xAmzTarget, TagResourceInput tagResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling tagResource(Async)");
        }

        // verify the required parameter 'tagResourceInput' is set
        if (tagResourceInput == null) {
            throw new ApiException("Missing the required parameter 'tagResourceInput' when calling tagResource(Async)");
        }

        return tagResourceCall(xAmzTarget, tagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a resource. 
     * @param xAmzTarget  (required)
     * @param tagResourceInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidArnException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public Object tagResource(String xAmzTarget, TagResourceInput tagResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = tagResourceWithHttpInfo(xAmzTarget, tagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a resource. 
     * @param xAmzTarget  (required)
     * @param tagResourceInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidArnException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> tagResourceWithHttpInfo(String xAmzTarget, TagResourceInput tagResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = tagResourceValidateBeforeCall(xAmzTarget, tagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a resource. 
     * @param xAmzTarget  (required)
     * @param tagResourceInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidArnException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> TooManyTagsException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call tagResourceAsync(String xAmzTarget, TagResourceInput tagResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = tagResourceValidateBeforeCall(xAmzTarget, tagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for untagResource
     * @param xAmzTarget  (required)
     * @param untagResourceInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidArnException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call untagResourceCall(String xAmzTarget, UntagResourceInput untagResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = untagResourceInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.UntagResource";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call untagResourceValidateBeforeCall(String xAmzTarget, UntagResourceInput untagResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling untagResource(Async)");
        }

        // verify the required parameter 'untagResourceInput' is set
        if (untagResourceInput == null) {
            throw new ApiException("Missing the required parameter 'untagResourceInput' when calling untagResource(Async)");
        }

        return untagResourceCall(xAmzTarget, untagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Removes tags from an Amazon Web Services resource.
     * @param xAmzTarget  (required)
     * @param untagResourceInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidArnException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public Object untagResource(String xAmzTarget, UntagResourceInput untagResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = untagResourceWithHttpInfo(xAmzTarget, untagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Removes tags from an Amazon Web Services resource.
     * @param xAmzTarget  (required)
     * @param untagResourceInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidArnException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> untagResourceWithHttpInfo(String xAmzTarget, UntagResourceInput untagResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = untagResourceValidateBeforeCall(xAmzTarget, untagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Removes tags from an Amazon Web Services resource.
     * @param xAmzTarget  (required)
     * @param untagResourceInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidArnException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidTagsException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConcurrentModificationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call untagResourceAsync(String xAmzTarget, UntagResourceInput untagResourceInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = untagResourceValidateBeforeCall(xAmzTarget, untagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateActionType
     * @param xAmzTarget  (required)
     * @param updateActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> RequestFailedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateActionTypeCall(String xAmzTarget, UpdateActionTypeInput updateActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = updateActionTypeInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.UpdateActionType";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateActionTypeValidateBeforeCall(String xAmzTarget, UpdateActionTypeInput updateActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling updateActionType(Async)");
        }

        // verify the required parameter 'updateActionTypeInput' is set
        if (updateActionTypeInput == null) {
            throw new ApiException("Missing the required parameter 'updateActionTypeInput' when calling updateActionType(Async)");
        }

        return updateActionTypeCall(xAmzTarget, updateActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Updates an action type that was created with any supported integration model, where the action type is to be used by customers of the action type provider. Use a JSON file with the action definition and &lt;code&gt;UpdateActionType&lt;/code&gt; to provide the full structure.
     * @param xAmzTarget  (required)
     * @param updateActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> RequestFailedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public void updateActionType(String xAmzTarget, UpdateActionTypeInput updateActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        updateActionTypeWithHttpInfo(xAmzTarget, updateActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * Updates an action type that was created with any supported integration model, where the action type is to be used by customers of the action type provider. Use a JSON file with the action definition and &lt;code&gt;UpdateActionType&lt;/code&gt; to provide the full structure.
     * @param xAmzTarget  (required)
     * @param updateActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> RequestFailedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> updateActionTypeWithHttpInfo(String xAmzTarget, UpdateActionTypeInput updateActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = updateActionTypeValidateBeforeCall(xAmzTarget, updateActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Updates an action type that was created with any supported integration model, where the action type is to be used by customers of the action type provider. Use a JSON file with the action definition and &lt;code&gt;UpdateActionType&lt;/code&gt; to provide the full structure.
     * @param xAmzTarget  (required)
     * @param updateActionTypeInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> RequestFailedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ActionTypeNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateActionTypeAsync(String xAmzTarget, UpdateActionTypeInput updateActionTypeInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateActionTypeValidateBeforeCall(xAmzTarget, updateActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for updatePipeline
     * @param xAmzTarget  (required)
     * @param updatePipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidStageDeclarationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidActionDeclarationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidBlockerDeclarationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InvalidStructureException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> LimitExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updatePipelineCall(String xAmzTarget, UpdatePipelineInput updatePipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = updatePipelineInput;

        // create path and map variables
        String localVarPath = "/#X-Amz-Target=CodePipeline_20150709.UpdatePipeline";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzTarget != null) {
            localVarHeaderParams.put("X-Amz-Target", localVarApiClient.parameterToString(xAmzTarget));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updatePipelineValidateBeforeCall(String xAmzTarget, UpdatePipelineInput updatePipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAmzTarget' is set
        if (xAmzTarget == null) {
            throw new ApiException("Missing the required parameter 'xAmzTarget' when calling updatePipeline(Async)");
        }

        // verify the required parameter 'updatePipelineInput' is set
        if (updatePipelineInput == null) {
            throw new ApiException("Missing the required parameter 'updatePipelineInput' when calling updatePipeline(Async)");
        }

        return updatePipelineCall(xAmzTarget, updatePipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Updates a specified pipeline with edits or changes to its structure. Use a JSON file with the pipeline structure and &lt;code&gt;UpdatePipeline&lt;/code&gt; to provide the full structure of the pipeline. Updating the pipeline increases the version number of the pipeline by 1.
     * @param xAmzTarget  (required)
     * @param updatePipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return UpdatePipelineOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidStageDeclarationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidActionDeclarationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidBlockerDeclarationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InvalidStructureException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> LimitExceededException </td><td>  -  </td></tr>
     </table>
     */
    public UpdatePipelineOutput updatePipeline(String xAmzTarget, UpdatePipelineInput updatePipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<UpdatePipelineOutput> localVarResp = updatePipelineWithHttpInfo(xAmzTarget, updatePipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Updates a specified pipeline with edits or changes to its structure. Use a JSON file with the pipeline structure and &lt;code&gt;UpdatePipeline&lt;/code&gt; to provide the full structure of the pipeline. Updating the pipeline increases the version number of the pipeline by 1.
     * @param xAmzTarget  (required)
     * @param updatePipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;UpdatePipelineOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidStageDeclarationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidActionDeclarationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidBlockerDeclarationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InvalidStructureException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> LimitExceededException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdatePipelineOutput> updatePipelineWithHttpInfo(String xAmzTarget, UpdatePipelineInput updatePipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = updatePipelineValidateBeforeCall(xAmzTarget, updatePipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<UpdatePipelineOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Updates a specified pipeline with edits or changes to its structure. Use a JSON file with the pipeline structure and &lt;code&gt;UpdatePipeline&lt;/code&gt; to provide the full structure of the pipeline. Updating the pipeline increases the version number of the pipeline by 1.
     * @param xAmzTarget  (required)
     * @param updatePipelineInput  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InvalidStageDeclarationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InvalidActionDeclarationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InvalidBlockerDeclarationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InvalidStructureException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> LimitExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updatePipelineAsync(String xAmzTarget, UpdatePipelineInput updatePipelineInput, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<UpdatePipelineOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = updatePipelineValidateBeforeCall(xAmzTarget, updatePipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<UpdatePipelineOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
