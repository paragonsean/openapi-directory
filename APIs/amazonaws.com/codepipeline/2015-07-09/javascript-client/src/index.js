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


import ApiClient from './ApiClient';
import AWSSessionCredentials from './model/AWSSessionCredentials';
import AcknowledgeJobInput from './model/AcknowledgeJobInput';
import AcknowledgeJobOutput from './model/AcknowledgeJobOutput';
import AcknowledgeThirdPartyJobInput from './model/AcknowledgeThirdPartyJobInput';
import AcknowledgeThirdPartyJobOutput from './model/AcknowledgeThirdPartyJobOutput';
import ActionCategory from './model/ActionCategory';
import ActionConfiguration from './model/ActionConfiguration';
import ActionConfigurationProperty from './model/ActionConfigurationProperty';
import ActionConfigurationPropertyType from './model/ActionConfigurationPropertyType';
import ActionContext from './model/ActionContext';
import ActionDeclaration from './model/ActionDeclaration';
import ActionDeclarationActionTypeId from './model/ActionDeclarationActionTypeId';
import ActionExecution from './model/ActionExecution';
import ActionExecutionDetail from './model/ActionExecutionDetail';
import ActionExecutionDetailInput from './model/ActionExecutionDetailInput';
import ActionExecutionDetailOutput from './model/ActionExecutionDetailOutput';
import ActionExecutionErrorDetails from './model/ActionExecutionErrorDetails';
import ActionExecutionFilter from './model/ActionExecutionFilter';
import ActionExecutionInput from './model/ActionExecutionInput';
import ActionExecutionOutput from './model/ActionExecutionOutput';
import ActionExecutionOutputExecutionResult from './model/ActionExecutionOutputExecutionResult';
import ActionExecutionResult from './model/ActionExecutionResult';
import ActionExecutionStatus from './model/ActionExecutionStatus';
import ActionOwner from './model/ActionOwner';
import ActionRevision from './model/ActionRevision';
import ActionState from './model/ActionState';
import ActionStateLatestExecution from './model/ActionStateLatestExecution';
import ActionType from './model/ActionType';
import ActionTypeArtifactDetails from './model/ActionTypeArtifactDetails';
import ActionTypeDeclaration from './model/ActionTypeDeclaration';
import ActionTypeDeclarationExecutor from './model/ActionTypeDeclarationExecutor';
import ActionTypeDeclarationId from './model/ActionTypeDeclarationId';
import ActionTypeDeclarationInputArtifactDetails from './model/ActionTypeDeclarationInputArtifactDetails';
import ActionTypeDeclarationOutputArtifactDetails from './model/ActionTypeDeclarationOutputArtifactDetails';
import ActionTypeDeclarationPermissions from './model/ActionTypeDeclarationPermissions';
import ActionTypeDeclarationUrls from './model/ActionTypeDeclarationUrls';
import ActionTypeExecutor from './model/ActionTypeExecutor';
import ActionTypeExecutorConfiguration from './model/ActionTypeExecutorConfiguration';
import ActionTypeId from './model/ActionTypeId';
import ActionTypeIdentifier from './model/ActionTypeIdentifier';
import ActionTypePermissions from './model/ActionTypePermissions';
import ActionTypeProperty from './model/ActionTypeProperty';
import ActionTypeSettings from './model/ActionTypeSettings';
import ActionTypeUrls from './model/ActionTypeUrls';
import ApprovalResult from './model/ApprovalResult';
import ApprovalStatus from './model/ApprovalStatus';
import Artifact from './model/Artifact';
import ArtifactDetail from './model/ArtifactDetail';
import ArtifactDetailS3location from './model/ArtifactDetailS3location';
import ArtifactDetails from './model/ArtifactDetails';
import ArtifactLocation from './model/ArtifactLocation';
import ArtifactLocationS3Location from './model/ArtifactLocationS3Location';
import ArtifactLocationType from './model/ArtifactLocationType';
import ArtifactRevision from './model/ArtifactRevision';
import ArtifactStore from './model/ArtifactStore';
import ArtifactStoreEncryptionKey from './model/ArtifactStoreEncryptionKey';
import ArtifactStoreType from './model/ArtifactStoreType';
import BlockerDeclaration from './model/BlockerDeclaration';
import BlockerType from './model/BlockerType';
import CreateCustomActionTypeInput from './model/CreateCustomActionTypeInput';
import CreateCustomActionTypeInputInputArtifactDetails from './model/CreateCustomActionTypeInputInputArtifactDetails';
import CreateCustomActionTypeInputOutputArtifactDetails from './model/CreateCustomActionTypeInputOutputArtifactDetails';
import CreateCustomActionTypeInputSettings from './model/CreateCustomActionTypeInputSettings';
import CreateCustomActionTypeOutput from './model/CreateCustomActionTypeOutput';
import CreateCustomActionTypeOutputActionType from './model/CreateCustomActionTypeOutputActionType';
import CreatePipelineInput from './model/CreatePipelineInput';
import CreatePipelineOutput from './model/CreatePipelineOutput';
import CreatePipelineOutputPipeline from './model/CreatePipelineOutputPipeline';
import CurrentRevision from './model/CurrentRevision';
import DeleteCustomActionTypeInput from './model/DeleteCustomActionTypeInput';
import DeletePipelineInput from './model/DeletePipelineInput';
import DeleteWebhookInput from './model/DeleteWebhookInput';
import DeregisterWebhookWithThirdPartyInput from './model/DeregisterWebhookWithThirdPartyInput';
import DisableStageTransitionInput from './model/DisableStageTransitionInput';
import EnableStageTransitionInput from './model/EnableStageTransitionInput';
import EncryptionKey from './model/EncryptionKey';
import EncryptionKeyType from './model/EncryptionKeyType';
import ErrorDetails from './model/ErrorDetails';
import ExecutionDetails from './model/ExecutionDetails';
import ExecutionTrigger from './model/ExecutionTrigger';
import ExecutorConfiguration from './model/ExecutorConfiguration';
import ExecutorConfigurationJobWorkerExecutorConfiguration from './model/ExecutorConfigurationJobWorkerExecutorConfiguration';
import ExecutorConfigurationLambdaExecutorConfiguration from './model/ExecutorConfigurationLambdaExecutorConfiguration';
import ExecutorType from './model/ExecutorType';
import FailureDetails from './model/FailureDetails';
import FailureType from './model/FailureType';
import GetActionTypeInput from './model/GetActionTypeInput';
import GetActionTypeOutput from './model/GetActionTypeOutput';
import GetActionTypeOutputActionType from './model/GetActionTypeOutputActionType';
import GetJobDetailsInput from './model/GetJobDetailsInput';
import GetJobDetailsOutput from './model/GetJobDetailsOutput';
import GetJobDetailsOutputJobDetails from './model/GetJobDetailsOutputJobDetails';
import GetPipelineExecutionInput from './model/GetPipelineExecutionInput';
import GetPipelineExecutionOutput from './model/GetPipelineExecutionOutput';
import GetPipelineExecutionOutputPipelineExecution from './model/GetPipelineExecutionOutputPipelineExecution';
import GetPipelineInput from './model/GetPipelineInput';
import GetPipelineOutput from './model/GetPipelineOutput';
import GetPipelineOutputMetadata from './model/GetPipelineOutputMetadata';
import GetPipelineStateInput from './model/GetPipelineStateInput';
import GetPipelineStateOutput from './model/GetPipelineStateOutput';
import GetThirdPartyJobDetailsInput from './model/GetThirdPartyJobDetailsInput';
import GetThirdPartyJobDetailsOutput from './model/GetThirdPartyJobDetailsOutput';
import GetThirdPartyJobDetailsOutputJobDetails from './model/GetThirdPartyJobDetailsOutputJobDetails';
import InputArtifact from './model/InputArtifact';
import Job from './model/Job';
import JobData from './model/JobData';
import JobDataActionConfiguration from './model/JobDataActionConfiguration';
import JobDataArtifactCredentials from './model/JobDataArtifactCredentials';
import JobDataEncryptionKey from './model/JobDataEncryptionKey';
import JobDataPipelineContext from './model/JobDataPipelineContext';
import JobDetails from './model/JobDetails';
import JobDetailsData from './model/JobDetailsData';
import JobStatus from './model/JobStatus';
import JobWorkerExecutorConfiguration from './model/JobWorkerExecutorConfiguration';
import LambdaExecutorConfiguration from './model/LambdaExecutorConfiguration';
import ListActionExecutionsInput from './model/ListActionExecutionsInput';
import ListActionExecutionsInputFilter from './model/ListActionExecutionsInputFilter';
import ListActionExecutionsOutput from './model/ListActionExecutionsOutput';
import ListActionTypesInput from './model/ListActionTypesInput';
import ListActionTypesOutput from './model/ListActionTypesOutput';
import ListPipelineExecutionsInput from './model/ListPipelineExecutionsInput';
import ListPipelineExecutionsOutput from './model/ListPipelineExecutionsOutput';
import ListPipelinesInput from './model/ListPipelinesInput';
import ListPipelinesOutput from './model/ListPipelinesOutput';
import ListTagsForResourceInput from './model/ListTagsForResourceInput';
import ListTagsForResourceOutput from './model/ListTagsForResourceOutput';
import ListWebhookItem from './model/ListWebhookItem';
import ListWebhookItemDefinition from './model/ListWebhookItemDefinition';
import ListWebhooksInput from './model/ListWebhooksInput';
import ListWebhooksOutput from './model/ListWebhooksOutput';
import OutputArtifact from './model/OutputArtifact';
import PipelineContext from './model/PipelineContext';
import PipelineContextAction from './model/PipelineContextAction';
import PipelineContextStage from './model/PipelineContextStage';
import PipelineDeclaration from './model/PipelineDeclaration';
import PipelineDeclarationArtifactStore from './model/PipelineDeclarationArtifactStore';
import PipelineExecution from './model/PipelineExecution';
import PipelineExecutionStatus from './model/PipelineExecutionStatus';
import PipelineExecutionSummary from './model/PipelineExecutionSummary';
import PipelineExecutionSummaryStopTrigger from './model/PipelineExecutionSummaryStopTrigger';
import PipelineExecutionSummaryTrigger from './model/PipelineExecutionSummaryTrigger';
import PipelineMetadata from './model/PipelineMetadata';
import PipelineSummary from './model/PipelineSummary';
import PollForJobsInput from './model/PollForJobsInput';
import PollForJobsInputActionTypeId from './model/PollForJobsInputActionTypeId';
import PollForJobsOutput from './model/PollForJobsOutput';
import PollForThirdPartyJobsInput from './model/PollForThirdPartyJobsInput';
import PollForThirdPartyJobsOutput from './model/PollForThirdPartyJobsOutput';
import PutActionRevisionInput from './model/PutActionRevisionInput';
import PutActionRevisionInputActionRevision from './model/PutActionRevisionInputActionRevision';
import PutActionRevisionOutput from './model/PutActionRevisionOutput';
import PutApprovalResultInput from './model/PutApprovalResultInput';
import PutApprovalResultInputResult from './model/PutApprovalResultInputResult';
import PutApprovalResultOutput from './model/PutApprovalResultOutput';
import PutJobFailureResultInput from './model/PutJobFailureResultInput';
import PutJobFailureResultInputFailureDetails from './model/PutJobFailureResultInputFailureDetails';
import PutJobSuccessResultInput from './model/PutJobSuccessResultInput';
import PutJobSuccessResultInputCurrentRevision from './model/PutJobSuccessResultInputCurrentRevision';
import PutJobSuccessResultInputExecutionDetails from './model/PutJobSuccessResultInputExecutionDetails';
import PutThirdPartyJobFailureResultInput from './model/PutThirdPartyJobFailureResultInput';
import PutThirdPartyJobFailureResultInputFailureDetails from './model/PutThirdPartyJobFailureResultInputFailureDetails';
import PutThirdPartyJobSuccessResultInput from './model/PutThirdPartyJobSuccessResultInput';
import PutThirdPartyJobSuccessResultInputCurrentRevision from './model/PutThirdPartyJobSuccessResultInputCurrentRevision';
import PutThirdPartyJobSuccessResultInputExecutionDetails from './model/PutThirdPartyJobSuccessResultInputExecutionDetails';
import PutWebhookInput from './model/PutWebhookInput';
import PutWebhookInputWebhook from './model/PutWebhookInputWebhook';
import PutWebhookOutput from './model/PutWebhookOutput';
import PutWebhookOutputWebhook from './model/PutWebhookOutputWebhook';
import RegisterWebhookWithThirdPartyInput from './model/RegisterWebhookWithThirdPartyInput';
import RetryStageExecutionInput from './model/RetryStageExecutionInput';
import RetryStageExecutionOutput from './model/RetryStageExecutionOutput';
import S3ArtifactLocation from './model/S3ArtifactLocation';
import S3Location from './model/S3Location';
import SourceRevision from './model/SourceRevision';
import StageContext from './model/StageContext';
import StageDeclaration from './model/StageDeclaration';
import StageExecution from './model/StageExecution';
import StageExecutionStatus from './model/StageExecutionStatus';
import StageRetryMode from './model/StageRetryMode';
import StageState from './model/StageState';
import StageStateInboundTransitionState from './model/StageStateInboundTransitionState';
import StageStateLatestExecution from './model/StageStateLatestExecution';
import StageTransitionType from './model/StageTransitionType';
import StartPipelineExecutionInput from './model/StartPipelineExecutionInput';
import StartPipelineExecutionOutput from './model/StartPipelineExecutionOutput';
import StopExecutionTrigger from './model/StopExecutionTrigger';
import StopPipelineExecutionInput from './model/StopPipelineExecutionInput';
import StopPipelineExecutionOutput from './model/StopPipelineExecutionOutput';
import Tag from './model/Tag';
import TagResourceInput from './model/TagResourceInput';
import ThirdPartyJob from './model/ThirdPartyJob';
import ThirdPartyJobData from './model/ThirdPartyJobData';
import ThirdPartyJobDataArtifactCredentials from './model/ThirdPartyJobDataArtifactCredentials';
import ThirdPartyJobDataEncryptionKey from './model/ThirdPartyJobDataEncryptionKey';
import ThirdPartyJobDataPipelineContext from './model/ThirdPartyJobDataPipelineContext';
import ThirdPartyJobDetails from './model/ThirdPartyJobDetails';
import ThirdPartyJobDetailsData from './model/ThirdPartyJobDetailsData';
import TransitionState from './model/TransitionState';
import TriggerType from './model/TriggerType';
import UntagResourceInput from './model/UntagResourceInput';
import UpdateActionTypeInput from './model/UpdateActionTypeInput';
import UpdateActionTypeInputActionType from './model/UpdateActionTypeInputActionType';
import UpdatePipelineInput from './model/UpdatePipelineInput';
import UpdatePipelineInputPipeline from './model/UpdatePipelineInputPipeline';
import UpdatePipelineOutput from './model/UpdatePipelineOutput';
import UpdatePipelineOutputPipeline from './model/UpdatePipelineOutputPipeline';
import WebhookAuthConfiguration from './model/WebhookAuthConfiguration';
import WebhookAuthenticationType from './model/WebhookAuthenticationType';
import WebhookDefinition from './model/WebhookDefinition';
import WebhookDefinitionAuthenticationConfiguration from './model/WebhookDefinitionAuthenticationConfiguration';
import WebhookFilterRule from './model/WebhookFilterRule';
import DefaultApi from './api/DefaultApi';


/**
* &lt;fullname&gt;CodePipeline&lt;/fullname&gt; &lt;p&gt; &lt;b&gt;Overview&lt;/b&gt; &lt;/p&gt; &lt;p&gt;This is the CodePipeline API Reference. This guide provides descriptions of the actions and data types for CodePipeline. Some functionality for your pipeline can only be configured through the API. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html\&quot;&gt;CodePipeline User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can use the CodePipeline API to work with pipelines, stages, actions, and transitions.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Pipelines&lt;/i&gt; are models of automated release processes. Each pipeline is uniquely named, and consists of stages, actions, and transitions. &lt;/p&gt; &lt;p&gt;You can work with pipelines by calling:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreatePipeline&lt;/a&gt;, which creates a uniquely named pipeline.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeletePipeline&lt;/a&gt;, which deletes the specified pipeline.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetPipeline&lt;/a&gt;, which returns information about the pipeline structure and pipeline metadata, including the pipeline Amazon Resource Name (ARN).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetPipelineExecution&lt;/a&gt;, which returns information about a specific execution of a pipeline.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetPipelineState&lt;/a&gt;, which returns information about the current state of the stages and actions of a pipeline.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListActionExecutions&lt;/a&gt;, which returns action-level details for past executions. The details include full stage and action-level details, including individual action duration, status, any errors that occurred during the execution, and input and output artifact location details.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListPipelines&lt;/a&gt;, which gets a summary of all of the pipelines associated with your account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListPipelineExecutions&lt;/a&gt;, which gets a summary of the most recent executions for a pipeline.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;StartPipelineExecution&lt;/a&gt;, which runs the most recent revision of an artifact through the pipeline.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;StopPipelineExecution&lt;/a&gt;, which stops the specified pipeline execution from continuing through the pipeline.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdatePipeline&lt;/a&gt;, which updates a pipeline with edits or changes to the structure of the pipeline.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Pipelines include &lt;i&gt;stages&lt;/i&gt;. Each stage contains one or more actions that must complete before the next stage begins. A stage results in success or failure. If a stage fails, the pipeline stops at that stage and remains stopped until either a new version of an artifact appears in the source location, or a user takes action to rerun the most recent artifact through the pipeline. You can call &lt;a&gt;GetPipelineState&lt;/a&gt;, which displays the status of a pipeline, including the status of stages in the pipeline, or &lt;a&gt;GetPipeline&lt;/a&gt;, which returns the entire structure of the pipeline, including the stages of that pipeline. For more information about the structure of stages and actions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-structure.html\&quot;&gt;CodePipeline Pipeline Structure Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Pipeline stages include &lt;i&gt;actions&lt;/i&gt; that are categorized into categories such as source or build actions performed in a stage of a pipeline. For example, you can use a source action to import artifacts into a pipeline from a source such as Amazon S3. Like stages, you do not work with actions directly in most cases, but you do define and interact with actions when working with pipeline operations such as &lt;a&gt;CreatePipeline&lt;/a&gt; and &lt;a&gt;GetPipelineState&lt;/a&gt;. Valid action categories are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Source&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Build&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Test&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Deploy&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Approval&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Invoke&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Pipelines also include &lt;i&gt;transitions&lt;/i&gt;, which allow the transition of artifacts from one stage to the next in a pipeline after the actions in one stage complete.&lt;/p&gt; &lt;p&gt;You can work with transitions by calling:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DisableStageTransition&lt;/a&gt;, which prevents artifacts from transitioning to the next stage in a pipeline.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;EnableStageTransition&lt;/a&gt;, which enables transition of artifacts between stages in a pipeline. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Using the API to integrate with CodePipeline&lt;/b&gt; &lt;/p&gt; &lt;p&gt;For third-party integrators or developers who want to create their own integrations with CodePipeline, the expected sequence varies from the standard API user. To integrate with CodePipeline, developers need to work with the following items:&lt;/p&gt; &lt;p&gt; &lt;b&gt;Jobs&lt;/b&gt;, which are instances of an action. For example, a job for a source action might import a revision of an artifact from a source. &lt;/p&gt; &lt;p&gt;You can work with jobs by calling:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;AcknowledgeJob&lt;/a&gt;, which confirms whether a job worker has received the specified job.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetJobDetails&lt;/a&gt;, which returns the details of a job.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PollForJobs&lt;/a&gt;, which determines whether there are any jobs to act on.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PutJobFailureResult&lt;/a&gt;, which provides details of a job failure. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PutJobSuccessResult&lt;/a&gt;, which provides details of a job success.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Third party jobs&lt;/b&gt;, which are instances of an action created by a partner action and integrated into CodePipeline. Partner actions are created by members of the Amazon Web Services Partner Network.&lt;/p&gt; &lt;p&gt;You can work with third party jobs by calling:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;AcknowledgeThirdPartyJob&lt;/a&gt;, which confirms whether a job worker has received the specified job.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetThirdPartyJobDetails&lt;/a&gt;, which requests the details of a job for a partner action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PollForThirdPartyJobs&lt;/a&gt;, which determines whether there are any jobs to act on. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PutThirdPartyJobFailureResult&lt;/a&gt;, which provides details of a job failure.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PutThirdPartyJobSuccessResult&lt;/a&gt;, which provides details of a job success.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var AwsCodePipeline = require('index'); // See note below*.
* var xxxSvc = new AwsCodePipeline.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new AwsCodePipeline.Yyy(); // Construct a model instance.
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
* var xxxSvc = new AwsCodePipeline.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new AwsCodePipeline.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2015-07-09
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AWSSessionCredentials model constructor.
     * @property {module:model/AWSSessionCredentials}
     */
    AWSSessionCredentials,

    /**
     * The AcknowledgeJobInput model constructor.
     * @property {module:model/AcknowledgeJobInput}
     */
    AcknowledgeJobInput,

    /**
     * The AcknowledgeJobOutput model constructor.
     * @property {module:model/AcknowledgeJobOutput}
     */
    AcknowledgeJobOutput,

    /**
     * The AcknowledgeThirdPartyJobInput model constructor.
     * @property {module:model/AcknowledgeThirdPartyJobInput}
     */
    AcknowledgeThirdPartyJobInput,

    /**
     * The AcknowledgeThirdPartyJobOutput model constructor.
     * @property {module:model/AcknowledgeThirdPartyJobOutput}
     */
    AcknowledgeThirdPartyJobOutput,

    /**
     * The ActionCategory model constructor.
     * @property {module:model/ActionCategory}
     */
    ActionCategory,

    /**
     * The ActionConfiguration model constructor.
     * @property {module:model/ActionConfiguration}
     */
    ActionConfiguration,

    /**
     * The ActionConfigurationProperty model constructor.
     * @property {module:model/ActionConfigurationProperty}
     */
    ActionConfigurationProperty,

    /**
     * The ActionConfigurationPropertyType model constructor.
     * @property {module:model/ActionConfigurationPropertyType}
     */
    ActionConfigurationPropertyType,

    /**
     * The ActionContext model constructor.
     * @property {module:model/ActionContext}
     */
    ActionContext,

    /**
     * The ActionDeclaration model constructor.
     * @property {module:model/ActionDeclaration}
     */
    ActionDeclaration,

    /**
     * The ActionDeclarationActionTypeId model constructor.
     * @property {module:model/ActionDeclarationActionTypeId}
     */
    ActionDeclarationActionTypeId,

    /**
     * The ActionExecution model constructor.
     * @property {module:model/ActionExecution}
     */
    ActionExecution,

    /**
     * The ActionExecutionDetail model constructor.
     * @property {module:model/ActionExecutionDetail}
     */
    ActionExecutionDetail,

    /**
     * The ActionExecutionDetailInput model constructor.
     * @property {module:model/ActionExecutionDetailInput}
     */
    ActionExecutionDetailInput,

    /**
     * The ActionExecutionDetailOutput model constructor.
     * @property {module:model/ActionExecutionDetailOutput}
     */
    ActionExecutionDetailOutput,

    /**
     * The ActionExecutionErrorDetails model constructor.
     * @property {module:model/ActionExecutionErrorDetails}
     */
    ActionExecutionErrorDetails,

    /**
     * The ActionExecutionFilter model constructor.
     * @property {module:model/ActionExecutionFilter}
     */
    ActionExecutionFilter,

    /**
     * The ActionExecutionInput model constructor.
     * @property {module:model/ActionExecutionInput}
     */
    ActionExecutionInput,

    /**
     * The ActionExecutionOutput model constructor.
     * @property {module:model/ActionExecutionOutput}
     */
    ActionExecutionOutput,

    /**
     * The ActionExecutionOutputExecutionResult model constructor.
     * @property {module:model/ActionExecutionOutputExecutionResult}
     */
    ActionExecutionOutputExecutionResult,

    /**
     * The ActionExecutionResult model constructor.
     * @property {module:model/ActionExecutionResult}
     */
    ActionExecutionResult,

    /**
     * The ActionExecutionStatus model constructor.
     * @property {module:model/ActionExecutionStatus}
     */
    ActionExecutionStatus,

    /**
     * The ActionOwner model constructor.
     * @property {module:model/ActionOwner}
     */
    ActionOwner,

    /**
     * The ActionRevision model constructor.
     * @property {module:model/ActionRevision}
     */
    ActionRevision,

    /**
     * The ActionState model constructor.
     * @property {module:model/ActionState}
     */
    ActionState,

    /**
     * The ActionStateLatestExecution model constructor.
     * @property {module:model/ActionStateLatestExecution}
     */
    ActionStateLatestExecution,

    /**
     * The ActionType model constructor.
     * @property {module:model/ActionType}
     */
    ActionType,

    /**
     * The ActionTypeArtifactDetails model constructor.
     * @property {module:model/ActionTypeArtifactDetails}
     */
    ActionTypeArtifactDetails,

    /**
     * The ActionTypeDeclaration model constructor.
     * @property {module:model/ActionTypeDeclaration}
     */
    ActionTypeDeclaration,

    /**
     * The ActionTypeDeclarationExecutor model constructor.
     * @property {module:model/ActionTypeDeclarationExecutor}
     */
    ActionTypeDeclarationExecutor,

    /**
     * The ActionTypeDeclarationId model constructor.
     * @property {module:model/ActionTypeDeclarationId}
     */
    ActionTypeDeclarationId,

    /**
     * The ActionTypeDeclarationInputArtifactDetails model constructor.
     * @property {module:model/ActionTypeDeclarationInputArtifactDetails}
     */
    ActionTypeDeclarationInputArtifactDetails,

    /**
     * The ActionTypeDeclarationOutputArtifactDetails model constructor.
     * @property {module:model/ActionTypeDeclarationOutputArtifactDetails}
     */
    ActionTypeDeclarationOutputArtifactDetails,

    /**
     * The ActionTypeDeclarationPermissions model constructor.
     * @property {module:model/ActionTypeDeclarationPermissions}
     */
    ActionTypeDeclarationPermissions,

    /**
     * The ActionTypeDeclarationUrls model constructor.
     * @property {module:model/ActionTypeDeclarationUrls}
     */
    ActionTypeDeclarationUrls,

    /**
     * The ActionTypeExecutor model constructor.
     * @property {module:model/ActionTypeExecutor}
     */
    ActionTypeExecutor,

    /**
     * The ActionTypeExecutorConfiguration model constructor.
     * @property {module:model/ActionTypeExecutorConfiguration}
     */
    ActionTypeExecutorConfiguration,

    /**
     * The ActionTypeId model constructor.
     * @property {module:model/ActionTypeId}
     */
    ActionTypeId,

    /**
     * The ActionTypeIdentifier model constructor.
     * @property {module:model/ActionTypeIdentifier}
     */
    ActionTypeIdentifier,

    /**
     * The ActionTypePermissions model constructor.
     * @property {module:model/ActionTypePermissions}
     */
    ActionTypePermissions,

    /**
     * The ActionTypeProperty model constructor.
     * @property {module:model/ActionTypeProperty}
     */
    ActionTypeProperty,

    /**
     * The ActionTypeSettings model constructor.
     * @property {module:model/ActionTypeSettings}
     */
    ActionTypeSettings,

    /**
     * The ActionTypeUrls model constructor.
     * @property {module:model/ActionTypeUrls}
     */
    ActionTypeUrls,

    /**
     * The ApprovalResult model constructor.
     * @property {module:model/ApprovalResult}
     */
    ApprovalResult,

    /**
     * The ApprovalStatus model constructor.
     * @property {module:model/ApprovalStatus}
     */
    ApprovalStatus,

    /**
     * The Artifact model constructor.
     * @property {module:model/Artifact}
     */
    Artifact,

    /**
     * The ArtifactDetail model constructor.
     * @property {module:model/ArtifactDetail}
     */
    ArtifactDetail,

    /**
     * The ArtifactDetailS3location model constructor.
     * @property {module:model/ArtifactDetailS3location}
     */
    ArtifactDetailS3location,

    /**
     * The ArtifactDetails model constructor.
     * @property {module:model/ArtifactDetails}
     */
    ArtifactDetails,

    /**
     * The ArtifactLocation model constructor.
     * @property {module:model/ArtifactLocation}
     */
    ArtifactLocation,

    /**
     * The ArtifactLocationS3Location model constructor.
     * @property {module:model/ArtifactLocationS3Location}
     */
    ArtifactLocationS3Location,

    /**
     * The ArtifactLocationType model constructor.
     * @property {module:model/ArtifactLocationType}
     */
    ArtifactLocationType,

    /**
     * The ArtifactRevision model constructor.
     * @property {module:model/ArtifactRevision}
     */
    ArtifactRevision,

    /**
     * The ArtifactStore model constructor.
     * @property {module:model/ArtifactStore}
     */
    ArtifactStore,

    /**
     * The ArtifactStoreEncryptionKey model constructor.
     * @property {module:model/ArtifactStoreEncryptionKey}
     */
    ArtifactStoreEncryptionKey,

    /**
     * The ArtifactStoreType model constructor.
     * @property {module:model/ArtifactStoreType}
     */
    ArtifactStoreType,

    /**
     * The BlockerDeclaration model constructor.
     * @property {module:model/BlockerDeclaration}
     */
    BlockerDeclaration,

    /**
     * The BlockerType model constructor.
     * @property {module:model/BlockerType}
     */
    BlockerType,

    /**
     * The CreateCustomActionTypeInput model constructor.
     * @property {module:model/CreateCustomActionTypeInput}
     */
    CreateCustomActionTypeInput,

    /**
     * The CreateCustomActionTypeInputInputArtifactDetails model constructor.
     * @property {module:model/CreateCustomActionTypeInputInputArtifactDetails}
     */
    CreateCustomActionTypeInputInputArtifactDetails,

    /**
     * The CreateCustomActionTypeInputOutputArtifactDetails model constructor.
     * @property {module:model/CreateCustomActionTypeInputOutputArtifactDetails}
     */
    CreateCustomActionTypeInputOutputArtifactDetails,

    /**
     * The CreateCustomActionTypeInputSettings model constructor.
     * @property {module:model/CreateCustomActionTypeInputSettings}
     */
    CreateCustomActionTypeInputSettings,

    /**
     * The CreateCustomActionTypeOutput model constructor.
     * @property {module:model/CreateCustomActionTypeOutput}
     */
    CreateCustomActionTypeOutput,

    /**
     * The CreateCustomActionTypeOutputActionType model constructor.
     * @property {module:model/CreateCustomActionTypeOutputActionType}
     */
    CreateCustomActionTypeOutputActionType,

    /**
     * The CreatePipelineInput model constructor.
     * @property {module:model/CreatePipelineInput}
     */
    CreatePipelineInput,

    /**
     * The CreatePipelineOutput model constructor.
     * @property {module:model/CreatePipelineOutput}
     */
    CreatePipelineOutput,

    /**
     * The CreatePipelineOutputPipeline model constructor.
     * @property {module:model/CreatePipelineOutputPipeline}
     */
    CreatePipelineOutputPipeline,

    /**
     * The CurrentRevision model constructor.
     * @property {module:model/CurrentRevision}
     */
    CurrentRevision,

    /**
     * The DeleteCustomActionTypeInput model constructor.
     * @property {module:model/DeleteCustomActionTypeInput}
     */
    DeleteCustomActionTypeInput,

    /**
     * The DeletePipelineInput model constructor.
     * @property {module:model/DeletePipelineInput}
     */
    DeletePipelineInput,

    /**
     * The DeleteWebhookInput model constructor.
     * @property {module:model/DeleteWebhookInput}
     */
    DeleteWebhookInput,

    /**
     * The DeregisterWebhookWithThirdPartyInput model constructor.
     * @property {module:model/DeregisterWebhookWithThirdPartyInput}
     */
    DeregisterWebhookWithThirdPartyInput,

    /**
     * The DisableStageTransitionInput model constructor.
     * @property {module:model/DisableStageTransitionInput}
     */
    DisableStageTransitionInput,

    /**
     * The EnableStageTransitionInput model constructor.
     * @property {module:model/EnableStageTransitionInput}
     */
    EnableStageTransitionInput,

    /**
     * The EncryptionKey model constructor.
     * @property {module:model/EncryptionKey}
     */
    EncryptionKey,

    /**
     * The EncryptionKeyType model constructor.
     * @property {module:model/EncryptionKeyType}
     */
    EncryptionKeyType,

    /**
     * The ErrorDetails model constructor.
     * @property {module:model/ErrorDetails}
     */
    ErrorDetails,

    /**
     * The ExecutionDetails model constructor.
     * @property {module:model/ExecutionDetails}
     */
    ExecutionDetails,

    /**
     * The ExecutionTrigger model constructor.
     * @property {module:model/ExecutionTrigger}
     */
    ExecutionTrigger,

    /**
     * The ExecutorConfiguration model constructor.
     * @property {module:model/ExecutorConfiguration}
     */
    ExecutorConfiguration,

    /**
     * The ExecutorConfigurationJobWorkerExecutorConfiguration model constructor.
     * @property {module:model/ExecutorConfigurationJobWorkerExecutorConfiguration}
     */
    ExecutorConfigurationJobWorkerExecutorConfiguration,

    /**
     * The ExecutorConfigurationLambdaExecutorConfiguration model constructor.
     * @property {module:model/ExecutorConfigurationLambdaExecutorConfiguration}
     */
    ExecutorConfigurationLambdaExecutorConfiguration,

    /**
     * The ExecutorType model constructor.
     * @property {module:model/ExecutorType}
     */
    ExecutorType,

    /**
     * The FailureDetails model constructor.
     * @property {module:model/FailureDetails}
     */
    FailureDetails,

    /**
     * The FailureType model constructor.
     * @property {module:model/FailureType}
     */
    FailureType,

    /**
     * The GetActionTypeInput model constructor.
     * @property {module:model/GetActionTypeInput}
     */
    GetActionTypeInput,

    /**
     * The GetActionTypeOutput model constructor.
     * @property {module:model/GetActionTypeOutput}
     */
    GetActionTypeOutput,

    /**
     * The GetActionTypeOutputActionType model constructor.
     * @property {module:model/GetActionTypeOutputActionType}
     */
    GetActionTypeOutputActionType,

    /**
     * The GetJobDetailsInput model constructor.
     * @property {module:model/GetJobDetailsInput}
     */
    GetJobDetailsInput,

    /**
     * The GetJobDetailsOutput model constructor.
     * @property {module:model/GetJobDetailsOutput}
     */
    GetJobDetailsOutput,

    /**
     * The GetJobDetailsOutputJobDetails model constructor.
     * @property {module:model/GetJobDetailsOutputJobDetails}
     */
    GetJobDetailsOutputJobDetails,

    /**
     * The GetPipelineExecutionInput model constructor.
     * @property {module:model/GetPipelineExecutionInput}
     */
    GetPipelineExecutionInput,

    /**
     * The GetPipelineExecutionOutput model constructor.
     * @property {module:model/GetPipelineExecutionOutput}
     */
    GetPipelineExecutionOutput,

    /**
     * The GetPipelineExecutionOutputPipelineExecution model constructor.
     * @property {module:model/GetPipelineExecutionOutputPipelineExecution}
     */
    GetPipelineExecutionOutputPipelineExecution,

    /**
     * The GetPipelineInput model constructor.
     * @property {module:model/GetPipelineInput}
     */
    GetPipelineInput,

    /**
     * The GetPipelineOutput model constructor.
     * @property {module:model/GetPipelineOutput}
     */
    GetPipelineOutput,

    /**
     * The GetPipelineOutputMetadata model constructor.
     * @property {module:model/GetPipelineOutputMetadata}
     */
    GetPipelineOutputMetadata,

    /**
     * The GetPipelineStateInput model constructor.
     * @property {module:model/GetPipelineStateInput}
     */
    GetPipelineStateInput,

    /**
     * The GetPipelineStateOutput model constructor.
     * @property {module:model/GetPipelineStateOutput}
     */
    GetPipelineStateOutput,

    /**
     * The GetThirdPartyJobDetailsInput model constructor.
     * @property {module:model/GetThirdPartyJobDetailsInput}
     */
    GetThirdPartyJobDetailsInput,

    /**
     * The GetThirdPartyJobDetailsOutput model constructor.
     * @property {module:model/GetThirdPartyJobDetailsOutput}
     */
    GetThirdPartyJobDetailsOutput,

    /**
     * The GetThirdPartyJobDetailsOutputJobDetails model constructor.
     * @property {module:model/GetThirdPartyJobDetailsOutputJobDetails}
     */
    GetThirdPartyJobDetailsOutputJobDetails,

    /**
     * The InputArtifact model constructor.
     * @property {module:model/InputArtifact}
     */
    InputArtifact,

    /**
     * The Job model constructor.
     * @property {module:model/Job}
     */
    Job,

    /**
     * The JobData model constructor.
     * @property {module:model/JobData}
     */
    JobData,

    /**
     * The JobDataActionConfiguration model constructor.
     * @property {module:model/JobDataActionConfiguration}
     */
    JobDataActionConfiguration,

    /**
     * The JobDataArtifactCredentials model constructor.
     * @property {module:model/JobDataArtifactCredentials}
     */
    JobDataArtifactCredentials,

    /**
     * The JobDataEncryptionKey model constructor.
     * @property {module:model/JobDataEncryptionKey}
     */
    JobDataEncryptionKey,

    /**
     * The JobDataPipelineContext model constructor.
     * @property {module:model/JobDataPipelineContext}
     */
    JobDataPipelineContext,

    /**
     * The JobDetails model constructor.
     * @property {module:model/JobDetails}
     */
    JobDetails,

    /**
     * The JobDetailsData model constructor.
     * @property {module:model/JobDetailsData}
     */
    JobDetailsData,

    /**
     * The JobStatus model constructor.
     * @property {module:model/JobStatus}
     */
    JobStatus,

    /**
     * The JobWorkerExecutorConfiguration model constructor.
     * @property {module:model/JobWorkerExecutorConfiguration}
     */
    JobWorkerExecutorConfiguration,

    /**
     * The LambdaExecutorConfiguration model constructor.
     * @property {module:model/LambdaExecutorConfiguration}
     */
    LambdaExecutorConfiguration,

    /**
     * The ListActionExecutionsInput model constructor.
     * @property {module:model/ListActionExecutionsInput}
     */
    ListActionExecutionsInput,

    /**
     * The ListActionExecutionsInputFilter model constructor.
     * @property {module:model/ListActionExecutionsInputFilter}
     */
    ListActionExecutionsInputFilter,

    /**
     * The ListActionExecutionsOutput model constructor.
     * @property {module:model/ListActionExecutionsOutput}
     */
    ListActionExecutionsOutput,

    /**
     * The ListActionTypesInput model constructor.
     * @property {module:model/ListActionTypesInput}
     */
    ListActionTypesInput,

    /**
     * The ListActionTypesOutput model constructor.
     * @property {module:model/ListActionTypesOutput}
     */
    ListActionTypesOutput,

    /**
     * The ListPipelineExecutionsInput model constructor.
     * @property {module:model/ListPipelineExecutionsInput}
     */
    ListPipelineExecutionsInput,

    /**
     * The ListPipelineExecutionsOutput model constructor.
     * @property {module:model/ListPipelineExecutionsOutput}
     */
    ListPipelineExecutionsOutput,

    /**
     * The ListPipelinesInput model constructor.
     * @property {module:model/ListPipelinesInput}
     */
    ListPipelinesInput,

    /**
     * The ListPipelinesOutput model constructor.
     * @property {module:model/ListPipelinesOutput}
     */
    ListPipelinesOutput,

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
     * The ListWebhookItem model constructor.
     * @property {module:model/ListWebhookItem}
     */
    ListWebhookItem,

    /**
     * The ListWebhookItemDefinition model constructor.
     * @property {module:model/ListWebhookItemDefinition}
     */
    ListWebhookItemDefinition,

    /**
     * The ListWebhooksInput model constructor.
     * @property {module:model/ListWebhooksInput}
     */
    ListWebhooksInput,

    /**
     * The ListWebhooksOutput model constructor.
     * @property {module:model/ListWebhooksOutput}
     */
    ListWebhooksOutput,

    /**
     * The OutputArtifact model constructor.
     * @property {module:model/OutputArtifact}
     */
    OutputArtifact,

    /**
     * The PipelineContext model constructor.
     * @property {module:model/PipelineContext}
     */
    PipelineContext,

    /**
     * The PipelineContextAction model constructor.
     * @property {module:model/PipelineContextAction}
     */
    PipelineContextAction,

    /**
     * The PipelineContextStage model constructor.
     * @property {module:model/PipelineContextStage}
     */
    PipelineContextStage,

    /**
     * The PipelineDeclaration model constructor.
     * @property {module:model/PipelineDeclaration}
     */
    PipelineDeclaration,

    /**
     * The PipelineDeclarationArtifactStore model constructor.
     * @property {module:model/PipelineDeclarationArtifactStore}
     */
    PipelineDeclarationArtifactStore,

    /**
     * The PipelineExecution model constructor.
     * @property {module:model/PipelineExecution}
     */
    PipelineExecution,

    /**
     * The PipelineExecutionStatus model constructor.
     * @property {module:model/PipelineExecutionStatus}
     */
    PipelineExecutionStatus,

    /**
     * The PipelineExecutionSummary model constructor.
     * @property {module:model/PipelineExecutionSummary}
     */
    PipelineExecutionSummary,

    /**
     * The PipelineExecutionSummaryStopTrigger model constructor.
     * @property {module:model/PipelineExecutionSummaryStopTrigger}
     */
    PipelineExecutionSummaryStopTrigger,

    /**
     * The PipelineExecutionSummaryTrigger model constructor.
     * @property {module:model/PipelineExecutionSummaryTrigger}
     */
    PipelineExecutionSummaryTrigger,

    /**
     * The PipelineMetadata model constructor.
     * @property {module:model/PipelineMetadata}
     */
    PipelineMetadata,

    /**
     * The PipelineSummary model constructor.
     * @property {module:model/PipelineSummary}
     */
    PipelineSummary,

    /**
     * The PollForJobsInput model constructor.
     * @property {module:model/PollForJobsInput}
     */
    PollForJobsInput,

    /**
     * The PollForJobsInputActionTypeId model constructor.
     * @property {module:model/PollForJobsInputActionTypeId}
     */
    PollForJobsInputActionTypeId,

    /**
     * The PollForJobsOutput model constructor.
     * @property {module:model/PollForJobsOutput}
     */
    PollForJobsOutput,

    /**
     * The PollForThirdPartyJobsInput model constructor.
     * @property {module:model/PollForThirdPartyJobsInput}
     */
    PollForThirdPartyJobsInput,

    /**
     * The PollForThirdPartyJobsOutput model constructor.
     * @property {module:model/PollForThirdPartyJobsOutput}
     */
    PollForThirdPartyJobsOutput,

    /**
     * The PutActionRevisionInput model constructor.
     * @property {module:model/PutActionRevisionInput}
     */
    PutActionRevisionInput,

    /**
     * The PutActionRevisionInputActionRevision model constructor.
     * @property {module:model/PutActionRevisionInputActionRevision}
     */
    PutActionRevisionInputActionRevision,

    /**
     * The PutActionRevisionOutput model constructor.
     * @property {module:model/PutActionRevisionOutput}
     */
    PutActionRevisionOutput,

    /**
     * The PutApprovalResultInput model constructor.
     * @property {module:model/PutApprovalResultInput}
     */
    PutApprovalResultInput,

    /**
     * The PutApprovalResultInputResult model constructor.
     * @property {module:model/PutApprovalResultInputResult}
     */
    PutApprovalResultInputResult,

    /**
     * The PutApprovalResultOutput model constructor.
     * @property {module:model/PutApprovalResultOutput}
     */
    PutApprovalResultOutput,

    /**
     * The PutJobFailureResultInput model constructor.
     * @property {module:model/PutJobFailureResultInput}
     */
    PutJobFailureResultInput,

    /**
     * The PutJobFailureResultInputFailureDetails model constructor.
     * @property {module:model/PutJobFailureResultInputFailureDetails}
     */
    PutJobFailureResultInputFailureDetails,

    /**
     * The PutJobSuccessResultInput model constructor.
     * @property {module:model/PutJobSuccessResultInput}
     */
    PutJobSuccessResultInput,

    /**
     * The PutJobSuccessResultInputCurrentRevision model constructor.
     * @property {module:model/PutJobSuccessResultInputCurrentRevision}
     */
    PutJobSuccessResultInputCurrentRevision,

    /**
     * The PutJobSuccessResultInputExecutionDetails model constructor.
     * @property {module:model/PutJobSuccessResultInputExecutionDetails}
     */
    PutJobSuccessResultInputExecutionDetails,

    /**
     * The PutThirdPartyJobFailureResultInput model constructor.
     * @property {module:model/PutThirdPartyJobFailureResultInput}
     */
    PutThirdPartyJobFailureResultInput,

    /**
     * The PutThirdPartyJobFailureResultInputFailureDetails model constructor.
     * @property {module:model/PutThirdPartyJobFailureResultInputFailureDetails}
     */
    PutThirdPartyJobFailureResultInputFailureDetails,

    /**
     * The PutThirdPartyJobSuccessResultInput model constructor.
     * @property {module:model/PutThirdPartyJobSuccessResultInput}
     */
    PutThirdPartyJobSuccessResultInput,

    /**
     * The PutThirdPartyJobSuccessResultInputCurrentRevision model constructor.
     * @property {module:model/PutThirdPartyJobSuccessResultInputCurrentRevision}
     */
    PutThirdPartyJobSuccessResultInputCurrentRevision,

    /**
     * The PutThirdPartyJobSuccessResultInputExecutionDetails model constructor.
     * @property {module:model/PutThirdPartyJobSuccessResultInputExecutionDetails}
     */
    PutThirdPartyJobSuccessResultInputExecutionDetails,

    /**
     * The PutWebhookInput model constructor.
     * @property {module:model/PutWebhookInput}
     */
    PutWebhookInput,

    /**
     * The PutWebhookInputWebhook model constructor.
     * @property {module:model/PutWebhookInputWebhook}
     */
    PutWebhookInputWebhook,

    /**
     * The PutWebhookOutput model constructor.
     * @property {module:model/PutWebhookOutput}
     */
    PutWebhookOutput,

    /**
     * The PutWebhookOutputWebhook model constructor.
     * @property {module:model/PutWebhookOutputWebhook}
     */
    PutWebhookOutputWebhook,

    /**
     * The RegisterWebhookWithThirdPartyInput model constructor.
     * @property {module:model/RegisterWebhookWithThirdPartyInput}
     */
    RegisterWebhookWithThirdPartyInput,

    /**
     * The RetryStageExecutionInput model constructor.
     * @property {module:model/RetryStageExecutionInput}
     */
    RetryStageExecutionInput,

    /**
     * The RetryStageExecutionOutput model constructor.
     * @property {module:model/RetryStageExecutionOutput}
     */
    RetryStageExecutionOutput,

    /**
     * The S3ArtifactLocation model constructor.
     * @property {module:model/S3ArtifactLocation}
     */
    S3ArtifactLocation,

    /**
     * The S3Location model constructor.
     * @property {module:model/S3Location}
     */
    S3Location,

    /**
     * The SourceRevision model constructor.
     * @property {module:model/SourceRevision}
     */
    SourceRevision,

    /**
     * The StageContext model constructor.
     * @property {module:model/StageContext}
     */
    StageContext,

    /**
     * The StageDeclaration model constructor.
     * @property {module:model/StageDeclaration}
     */
    StageDeclaration,

    /**
     * The StageExecution model constructor.
     * @property {module:model/StageExecution}
     */
    StageExecution,

    /**
     * The StageExecutionStatus model constructor.
     * @property {module:model/StageExecutionStatus}
     */
    StageExecutionStatus,

    /**
     * The StageRetryMode model constructor.
     * @property {module:model/StageRetryMode}
     */
    StageRetryMode,

    /**
     * The StageState model constructor.
     * @property {module:model/StageState}
     */
    StageState,

    /**
     * The StageStateInboundTransitionState model constructor.
     * @property {module:model/StageStateInboundTransitionState}
     */
    StageStateInboundTransitionState,

    /**
     * The StageStateLatestExecution model constructor.
     * @property {module:model/StageStateLatestExecution}
     */
    StageStateLatestExecution,

    /**
     * The StageTransitionType model constructor.
     * @property {module:model/StageTransitionType}
     */
    StageTransitionType,

    /**
     * The StartPipelineExecutionInput model constructor.
     * @property {module:model/StartPipelineExecutionInput}
     */
    StartPipelineExecutionInput,

    /**
     * The StartPipelineExecutionOutput model constructor.
     * @property {module:model/StartPipelineExecutionOutput}
     */
    StartPipelineExecutionOutput,

    /**
     * The StopExecutionTrigger model constructor.
     * @property {module:model/StopExecutionTrigger}
     */
    StopExecutionTrigger,

    /**
     * The StopPipelineExecutionInput model constructor.
     * @property {module:model/StopPipelineExecutionInput}
     */
    StopPipelineExecutionInput,

    /**
     * The StopPipelineExecutionOutput model constructor.
     * @property {module:model/StopPipelineExecutionOutput}
     */
    StopPipelineExecutionOutput,

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
     * The ThirdPartyJob model constructor.
     * @property {module:model/ThirdPartyJob}
     */
    ThirdPartyJob,

    /**
     * The ThirdPartyJobData model constructor.
     * @property {module:model/ThirdPartyJobData}
     */
    ThirdPartyJobData,

    /**
     * The ThirdPartyJobDataArtifactCredentials model constructor.
     * @property {module:model/ThirdPartyJobDataArtifactCredentials}
     */
    ThirdPartyJobDataArtifactCredentials,

    /**
     * The ThirdPartyJobDataEncryptionKey model constructor.
     * @property {module:model/ThirdPartyJobDataEncryptionKey}
     */
    ThirdPartyJobDataEncryptionKey,

    /**
     * The ThirdPartyJobDataPipelineContext model constructor.
     * @property {module:model/ThirdPartyJobDataPipelineContext}
     */
    ThirdPartyJobDataPipelineContext,

    /**
     * The ThirdPartyJobDetails model constructor.
     * @property {module:model/ThirdPartyJobDetails}
     */
    ThirdPartyJobDetails,

    /**
     * The ThirdPartyJobDetailsData model constructor.
     * @property {module:model/ThirdPartyJobDetailsData}
     */
    ThirdPartyJobDetailsData,

    /**
     * The TransitionState model constructor.
     * @property {module:model/TransitionState}
     */
    TransitionState,

    /**
     * The TriggerType model constructor.
     * @property {module:model/TriggerType}
     */
    TriggerType,

    /**
     * The UntagResourceInput model constructor.
     * @property {module:model/UntagResourceInput}
     */
    UntagResourceInput,

    /**
     * The UpdateActionTypeInput model constructor.
     * @property {module:model/UpdateActionTypeInput}
     */
    UpdateActionTypeInput,

    /**
     * The UpdateActionTypeInputActionType model constructor.
     * @property {module:model/UpdateActionTypeInputActionType}
     */
    UpdateActionTypeInputActionType,

    /**
     * The UpdatePipelineInput model constructor.
     * @property {module:model/UpdatePipelineInput}
     */
    UpdatePipelineInput,

    /**
     * The UpdatePipelineInputPipeline model constructor.
     * @property {module:model/UpdatePipelineInputPipeline}
     */
    UpdatePipelineInputPipeline,

    /**
     * The UpdatePipelineOutput model constructor.
     * @property {module:model/UpdatePipelineOutput}
     */
    UpdatePipelineOutput,

    /**
     * The UpdatePipelineOutputPipeline model constructor.
     * @property {module:model/UpdatePipelineOutputPipeline}
     */
    UpdatePipelineOutputPipeline,

    /**
     * The WebhookAuthConfiguration model constructor.
     * @property {module:model/WebhookAuthConfiguration}
     */
    WebhookAuthConfiguration,

    /**
     * The WebhookAuthenticationType model constructor.
     * @property {module:model/WebhookAuthenticationType}
     */
    WebhookAuthenticationType,

    /**
     * The WebhookDefinition model constructor.
     * @property {module:model/WebhookDefinition}
     */
    WebhookDefinition,

    /**
     * The WebhookDefinitionAuthenticationConfiguration model constructor.
     * @property {module:model/WebhookDefinitionAuthenticationConfiguration}
     */
    WebhookDefinitionAuthenticationConfiguration,

    /**
     * The WebhookFilterRule model constructor.
     * @property {module:model/WebhookFilterRule}
     */
    WebhookFilterRule,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
