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

import org.openapitools.client.ApiException;
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
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * Returns information about a specified job and whether that job has been received by the job worker. Used for custom actions only.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void acknowledgeJobTest() throws ApiException {
        String xAmzTarget = null;
        AcknowledgeJobInput acknowledgeJobInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        AcknowledgeJobOutput response = api.acknowledgeJob(xAmzTarget, acknowledgeJobInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Confirms a job worker has received the specified job. Used for partner actions only.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void acknowledgeThirdPartyJobTest() throws ApiException {
        String xAmzTarget = null;
        AcknowledgeThirdPartyJobInput acknowledgeThirdPartyJobInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        AcknowledgeThirdPartyJobOutput response = api.acknowledgeThirdPartyJob(xAmzTarget, acknowledgeThirdPartyJobInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Creates a new custom action that can be used in all pipelines associated with the Amazon Web Services account. Only used for custom actions.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createCustomActionTypeTest() throws ApiException {
        String xAmzTarget = null;
        CreateCustomActionTypeInput createCustomActionTypeInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateCustomActionTypeOutput response = api.createCustomActionType(xAmzTarget, createCustomActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Creates a pipeline.&lt;/p&gt; &lt;note&gt; &lt;p&gt;In the pipeline structure, you must include either &lt;code&gt;artifactStore&lt;/code&gt; or &lt;code&gt;artifactStores&lt;/code&gt; in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use &lt;code&gt;artifactStores&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createPipelineTest() throws ApiException {
        String xAmzTarget = null;
        CreatePipelineInput createPipelineInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreatePipelineOutput response = api.createPipeline(xAmzTarget, createPipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Marks a custom action as deleted. &lt;code&gt;PollForJobs&lt;/code&gt; for the custom action fails after the action is marked for deletion. Used for custom actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;To re-create a custom action after it has been deleted you must use a string in the version field that has never been used before. This string can be an incremented version number, for example. To restore a deleted custom action, use a JSON file that is identical to the deleted action, including the original string in the version field.&lt;/p&gt; &lt;/important&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteCustomActionTypeTest() throws ApiException {
        String xAmzTarget = null;
        DeleteCustomActionTypeInput deleteCustomActionTypeInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.deleteCustomActionType(xAmzTarget, deleteCustomActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Deletes the specified pipeline.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deletePipelineTest() throws ApiException {
        String xAmzTarget = null;
        DeletePipelineInput deletePipelineInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.deletePipeline(xAmzTarget, deletePipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Deletes a previously created webhook by name. Deleting the webhook stops CodePipeline from starting a pipeline every time an external event occurs. The API returns successfully when trying to delete a webhook that is already deleted. If a deleted webhook is re-created by calling PutWebhook with the same name, it will have a different URL.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteWebhookTest() throws ApiException {
        String xAmzTarget = null;
        DeleteWebhookInput deleteWebhookInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.deleteWebhook(xAmzTarget, deleteWebhookInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Removes the connection between the webhook that was created by CodePipeline and the external tool with events to be detected. Currently supported only for webhooks that target an action type of GitHub.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deregisterWebhookWithThirdPartyTest() throws ApiException {
        String xAmzTarget = null;
        DeregisterWebhookWithThirdPartyInput deregisterWebhookWithThirdPartyInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.deregisterWebhookWithThirdParty(xAmzTarget, deregisterWebhookWithThirdPartyInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Prevents artifacts in a pipeline from transitioning to the next stage in the pipeline.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void disableStageTransitionTest() throws ApiException {
        String xAmzTarget = null;
        DisableStageTransitionInput disableStageTransitionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.disableStageTransition(xAmzTarget, disableStageTransitionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Enables artifacts in a pipeline to transition to a stage in a pipeline.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void enableStageTransitionTest() throws ApiException {
        String xAmzTarget = null;
        EnableStageTransitionInput enableStageTransitionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.enableStageTransition(xAmzTarget, enableStageTransitionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns information about an action type created for an external provider, where the action is to be used by customers of the external provider. The action can be created with any supported integration model.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getActionTypeTest() throws ApiException {
        String xAmzTarget = null;
        GetActionTypeInput getActionTypeInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetActionTypeOutput response = api.getActionType(xAmzTarget, getActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Returns information about a job. Used for custom actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.&lt;/p&gt; &lt;/important&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getJobDetailsTest() throws ApiException {
        String xAmzTarget = null;
        GetJobDetailsInput getJobDetailsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetJobDetailsOutput response = api.getJobDetails(xAmzTarget, getJobDetailsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns the metadata, structure, stages, and actions of a pipeline. Can be used to return the entire structure of a pipeline in JSON format, which can then be modified and used to update the pipeline structure with &lt;a&gt;UpdatePipeline&lt;/a&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPipelineTest() throws ApiException {
        String xAmzTarget = null;
        GetPipelineInput getPipelineInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetPipelineOutput response = api.getPipeline(xAmzTarget, getPipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns information about an execution of a pipeline, including details about artifacts, the pipeline execution ID, and the name, version, and status of the pipeline.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPipelineExecutionTest() throws ApiException {
        String xAmzTarget = null;
        GetPipelineExecutionInput getPipelineExecutionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetPipelineExecutionOutput response = api.getPipelineExecution(xAmzTarget, getPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Returns information about the state of a pipeline, including the stages and actions.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Values returned in the &lt;code&gt;revisionId&lt;/code&gt; and &lt;code&gt;revisionUrl&lt;/code&gt; fields indicate the source revision information, such as the commit ID, for the current state.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPipelineStateTest() throws ApiException {
        String xAmzTarget = null;
        GetPipelineStateInput getPipelineStateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetPipelineStateOutput response = api.getPipelineState(xAmzTarget, getPipelineStateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Requests the details of a job for a third party action. Used for partner actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.&lt;/p&gt; &lt;/important&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getThirdPartyJobDetailsTest() throws ApiException {
        String xAmzTarget = null;
        GetThirdPartyJobDetailsInput getThirdPartyJobDetailsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetThirdPartyJobDetailsOutput response = api.getThirdPartyJobDetails(xAmzTarget, getThirdPartyJobDetailsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Lists the action executions that have occurred in a pipeline.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listActionExecutionsTest() throws ApiException {
        String xAmzTarget = null;
        ListActionExecutionsInput listActionExecutionsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListActionExecutionsOutput response = api.listActionExecutions(xAmzTarget, listActionExecutionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets a summary of all CodePipeline action types associated with your account.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listActionTypesTest() throws ApiException {
        String xAmzTarget = null;
        ListActionTypesInput listActionTypesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String nextToken = null;
        ListActionTypesOutput response = api.listActionTypes(xAmzTarget, listActionTypesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken);
        // TODO: test validations
    }

    /**
     * Gets a summary of the most recent executions for a pipeline.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listPipelineExecutionsTest() throws ApiException {
        String xAmzTarget = null;
        ListPipelineExecutionsInput listPipelineExecutionsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListPipelineExecutionsOutput response = api.listPipelineExecutions(xAmzTarget, listPipelineExecutionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets a summary of all of the pipelines associated with your account.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listPipelinesTest() throws ApiException {
        String xAmzTarget = null;
        ListPipelinesInput listPipelinesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListPipelinesOutput response = api.listPipelines(xAmzTarget, listPipelinesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets the set of key-value pairs (metadata) that are used to manage the resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listTagsForResourceTest() throws ApiException {
        String xAmzTarget = null;
        ListTagsForResourceInput listTagsForResourceInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListTagsForResourceOutput response = api.listTagsForResource(xAmzTarget, listTagsForResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets a listing of all the webhooks in this Amazon Web Services Region for this account. The output lists all webhooks and includes the webhook URL and ARN and the configuration for each webhook.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listWebhooksTest() throws ApiException {
        String xAmzTarget = null;
        ListWebhooksInput listWebhooksInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListWebhooksOutput response = api.listWebhooks(xAmzTarget, listWebhooksInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Returns information about any jobs for CodePipeline to act on. &lt;code&gt;PollForJobs&lt;/code&gt; is valid only for action types with \&quot;Custom\&quot; in the owner field. If the action type contains &lt;code&gt;AWS&lt;/code&gt; or &lt;code&gt;ThirdParty&lt;/code&gt; in the owner field, the &lt;code&gt;PollForJobs&lt;/code&gt; action returns an error.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.&lt;/p&gt; &lt;/important&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void pollForJobsTest() throws ApiException {
        String xAmzTarget = null;
        PollForJobsInput pollForJobsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        PollForJobsOutput response = api.pollForJobs(xAmzTarget, pollForJobsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Determines whether there are any third party jobs for a job worker to act on. Used for partner actions only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts.&lt;/p&gt; &lt;/important&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void pollForThirdPartyJobsTest() throws ApiException {
        String xAmzTarget = null;
        PollForThirdPartyJobsInput pollForThirdPartyJobsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        PollForThirdPartyJobsOutput response = api.pollForThirdPartyJobs(xAmzTarget, pollForThirdPartyJobsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Provides information to CodePipeline about new revisions to a source.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putActionRevisionTest() throws ApiException {
        String xAmzTarget = null;
        PutActionRevisionInput putActionRevisionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        PutActionRevisionOutput response = api.putActionRevision(xAmzTarget, putActionRevisionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Provides the response to a manual approval request to CodePipeline. Valid responses include Approved and Rejected.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putApprovalResultTest() throws ApiException {
        String xAmzTarget = null;
        PutApprovalResultInput putApprovalResultInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        PutApprovalResultOutput response = api.putApprovalResult(xAmzTarget, putApprovalResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Represents the failure of a job as returned to the pipeline by a job worker. Used for custom actions only.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putJobFailureResultTest() throws ApiException {
        String xAmzTarget = null;
        PutJobFailureResultInput putJobFailureResultInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.putJobFailureResult(xAmzTarget, putJobFailureResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Represents the success of a job as returned to the pipeline by a job worker. Used for custom actions only.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putJobSuccessResultTest() throws ApiException {
        String xAmzTarget = null;
        PutJobSuccessResultInput putJobSuccessResultInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.putJobSuccessResult(xAmzTarget, putJobSuccessResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Represents the failure of a third party job as returned to the pipeline by a job worker. Used for partner actions only.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putThirdPartyJobFailureResultTest() throws ApiException {
        String xAmzTarget = null;
        PutThirdPartyJobFailureResultInput putThirdPartyJobFailureResultInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.putThirdPartyJobFailureResult(xAmzTarget, putThirdPartyJobFailureResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Represents the success of a third party job as returned to the pipeline by a job worker. Used for partner actions only.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putThirdPartyJobSuccessResultTest() throws ApiException {
        String xAmzTarget = null;
        PutThirdPartyJobSuccessResultInput putThirdPartyJobSuccessResultInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.putThirdPartyJobSuccessResult(xAmzTarget, putThirdPartyJobSuccessResultInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Defines a webhook and returns a unique webhook URL generated by CodePipeline. This URL can be supplied to third party source hosting providers to call every time there&#39;s a code change. When CodePipeline receives a POST request on this URL, the pipeline defined in the webhook is started as long as the POST request satisfied the authentication and filtering requirements supplied when defining the webhook. RegisterWebhookWithThirdParty and DeregisterWebhookWithThirdParty APIs can be used to automatically configure supported third parties to call the generated webhook URL.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putWebhookTest() throws ApiException {
        String xAmzTarget = null;
        PutWebhookInput putWebhookInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        PutWebhookOutput response = api.putWebhook(xAmzTarget, putWebhookInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Configures a connection between the webhook that was created and the external tool with events to be detected.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void registerWebhookWithThirdPartyTest() throws ApiException {
        String xAmzTarget = null;
        RegisterWebhookWithThirdPartyInput registerWebhookWithThirdPartyInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.registerWebhookWithThirdParty(xAmzTarget, registerWebhookWithThirdPartyInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Resumes the pipeline execution by retrying the last failed actions in a stage. You can retry a stage immediately if any of the actions in the stage fail. When you retry, all actions that are still in progress continue working, and failed actions are triggered again.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void retryStageExecutionTest() throws ApiException {
        String xAmzTarget = null;
        RetryStageExecutionInput retryStageExecutionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        RetryStageExecutionOutput response = api.retryStageExecution(xAmzTarget, retryStageExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Starts the specified pipeline. Specifically, it begins processing the latest commit to the source location specified as part of the pipeline.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startPipelineExecutionTest() throws ApiException {
        String xAmzTarget = null;
        StartPipelineExecutionInput startPipelineExecutionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        StartPipelineExecutionOutput response = api.startPipelineExecution(xAmzTarget, startPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Stops the specified pipeline execution. You choose to either stop the pipeline execution by completing in-progress actions without starting subsequent actions, or by abandoning in-progress actions. While completing or abandoning in-progress actions, the pipeline execution is in a &lt;code&gt;Stopping&lt;/code&gt; state. After all in-progress actions are completed or abandoned, the pipeline execution is in a &lt;code&gt;Stopped&lt;/code&gt; state.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void stopPipelineExecutionTest() throws ApiException {
        String xAmzTarget = null;
        StopPipelineExecutionInput stopPipelineExecutionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        StopPipelineExecutionOutput response = api.stopPipelineExecution(xAmzTarget, stopPipelineExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a resource. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void tagResourceTest() throws ApiException {
        String xAmzTarget = null;
        TagResourceInput tagResourceInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.tagResource(xAmzTarget, tagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Removes tags from an Amazon Web Services resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void untagResourceTest() throws ApiException {
        String xAmzTarget = null;
        UntagResourceInput untagResourceInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.untagResource(xAmzTarget, untagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Updates an action type that was created with any supported integration model, where the action type is to be used by customers of the action type provider. Use a JSON file with the action definition and &lt;code&gt;UpdateActionType&lt;/code&gt; to provide the full structure.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateActionTypeTest() throws ApiException {
        String xAmzTarget = null;
        UpdateActionTypeInput updateActionTypeInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.updateActionType(xAmzTarget, updateActionTypeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Updates a specified pipeline with edits or changes to its structure. Use a JSON file with the pipeline structure and &lt;code&gt;UpdatePipeline&lt;/code&gt; to provide the full structure of the pipeline. Updating the pipeline increases the version number of the pipeline by 1.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updatePipelineTest() throws ApiException {
        String xAmzTarget = null;
        UpdatePipelineInput updatePipelineInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdatePipelineOutput response = api.updatePipeline(xAmzTarget, updatePipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

}
