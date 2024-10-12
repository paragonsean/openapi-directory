# openapi-java-client

AWS CodePipeline
- API version: 2015-07-09
  - Build date: 2024-10-12T12:02:26.715942-04:00[America/New_York]
  - Generator version: 7.9.0

<fullname>CodePipeline</fullname> <p> <b>Overview</b> </p> <p>This is the CodePipeline API Reference. This guide provides descriptions of the actions and data types for CodePipeline. Some functionality for your pipeline can only be configured through the API. For more information, see the <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html\">CodePipeline User Guide</a>.</p> <p>You can use the CodePipeline API to work with pipelines, stages, actions, and transitions.</p> <p> <i>Pipelines</i> are models of automated release processes. Each pipeline is uniquely named, and consists of stages, actions, and transitions. </p> <p>You can work with pipelines by calling:</p> <ul> <li> <p> <a>CreatePipeline</a>, which creates a uniquely named pipeline.</p> </li> <li> <p> <a>DeletePipeline</a>, which deletes the specified pipeline.</p> </li> <li> <p> <a>GetPipeline</a>, which returns information about the pipeline structure and pipeline metadata, including the pipeline Amazon Resource Name (ARN).</p> </li> <li> <p> <a>GetPipelineExecution</a>, which returns information about a specific execution of a pipeline.</p> </li> <li> <p> <a>GetPipelineState</a>, which returns information about the current state of the stages and actions of a pipeline.</p> </li> <li> <p> <a>ListActionExecutions</a>, which returns action-level details for past executions. The details include full stage and action-level details, including individual action duration, status, any errors that occurred during the execution, and input and output artifact location details.</p> </li> <li> <p> <a>ListPipelines</a>, which gets a summary of all of the pipelines associated with your account.</p> </li> <li> <p> <a>ListPipelineExecutions</a>, which gets a summary of the most recent executions for a pipeline.</p> </li> <li> <p> <a>StartPipelineExecution</a>, which runs the most recent revision of an artifact through the pipeline.</p> </li> <li> <p> <a>StopPipelineExecution</a>, which stops the specified pipeline execution from continuing through the pipeline.</p> </li> <li> <p> <a>UpdatePipeline</a>, which updates a pipeline with edits or changes to the structure of the pipeline.</p> </li> </ul> <p>Pipelines include <i>stages</i>. Each stage contains one or more actions that must complete before the next stage begins. A stage results in success or failure. If a stage fails, the pipeline stops at that stage and remains stopped until either a new version of an artifact appears in the source location, or a user takes action to rerun the most recent artifact through the pipeline. You can call <a>GetPipelineState</a>, which displays the status of a pipeline, including the status of stages in the pipeline, or <a>GetPipeline</a>, which returns the entire structure of the pipeline, including the stages of that pipeline. For more information about the structure of stages and actions, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-structure.html\">CodePipeline Pipeline Structure Reference</a>.</p> <p>Pipeline stages include <i>actions</i> that are categorized into categories such as source or build actions performed in a stage of a pipeline. For example, you can use a source action to import artifacts into a pipeline from a source such as Amazon S3. Like stages, you do not work with actions directly in most cases, but you do define and interact with actions when working with pipeline operations such as <a>CreatePipeline</a> and <a>GetPipelineState</a>. Valid action categories are:</p> <ul> <li> <p>Source</p> </li> <li> <p>Build</p> </li> <li> <p>Test</p> </li> <li> <p>Deploy</p> </li> <li> <p>Approval</p> </li> <li> <p>Invoke</p> </li> </ul> <p>Pipelines also include <i>transitions</i>, which allow the transition of artifacts from one stage to the next in a pipeline after the actions in one stage complete.</p> <p>You can work with transitions by calling:</p> <ul> <li> <p> <a>DisableStageTransition</a>, which prevents artifacts from transitioning to the next stage in a pipeline.</p> </li> <li> <p> <a>EnableStageTransition</a>, which enables transition of artifacts between stages in a pipeline. </p> </li> </ul> <p> <b>Using the API to integrate with CodePipeline</b> </p> <p>For third-party integrators or developers who want to create their own integrations with CodePipeline, the expected sequence varies from the standard API user. To integrate with CodePipeline, developers need to work with the following items:</p> <p> <b>Jobs</b>, which are instances of an action. For example, a job for a source action might import a revision of an artifact from a source. </p> <p>You can work with jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetJobDetails</a>, which returns the details of a job.</p> </li> <li> <p> <a>PollForJobs</a>, which determines whether there are any jobs to act on.</p> </li> <li> <p> <a>PutJobFailureResult</a>, which provides details of a job failure. </p> </li> <li> <p> <a>PutJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul> <p> <b>Third party jobs</b>, which are instances of an action created by a partner action and integrated into CodePipeline. Partner actions are created by members of the Amazon Web Services Partner Network.</p> <p>You can work with third party jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeThirdPartyJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetThirdPartyJobDetails</a>, which requests the details of a job for a partner action.</p> </li> <li> <p> <a>PollForThirdPartyJobs</a>, which determines whether there are any jobs to act on. </p> </li> <li> <p> <a>PutThirdPartyJobFailureResult</a>, which provides details of a job failure.</p> </li> <li> <p> <a>PutThirdPartyJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul>

  For more information, please visit [https://github.com/mermade/aws2openapi](https://github.com/mermade/aws2openapi)

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>2015-07-09</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:2015-07-09"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-2015-07-09.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codepipeline.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CodePipeline_20150709.AcknowledgeJob"; // String | 
    AcknowledgeJobInput acknowledgeJobInput = new AcknowledgeJobInput(); // AcknowledgeJobInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AcknowledgeJobOutput result = apiInstance.acknowledgeJob(xAmzTarget, acknowledgeJobInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#acknowledgeJob");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://codepipeline.us-east-1.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**acknowledgeJob**](docs/DefaultApi.md#acknowledgeJob) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.AcknowledgeJob | 
*DefaultApi* | [**acknowledgeThirdPartyJob**](docs/DefaultApi.md#acknowledgeThirdPartyJob) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.AcknowledgeThirdPartyJob | 
*DefaultApi* | [**createCustomActionType**](docs/DefaultApi.md#createCustomActionType) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.CreateCustomActionType | 
*DefaultApi* | [**createPipeline**](docs/DefaultApi.md#createPipeline) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.CreatePipeline | 
*DefaultApi* | [**deleteCustomActionType**](docs/DefaultApi.md#deleteCustomActionType) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.DeleteCustomActionType | 
*DefaultApi* | [**deletePipeline**](docs/DefaultApi.md#deletePipeline) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.DeletePipeline | 
*DefaultApi* | [**deleteWebhook**](docs/DefaultApi.md#deleteWebhook) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.DeleteWebhook | 
*DefaultApi* | [**deregisterWebhookWithThirdParty**](docs/DefaultApi.md#deregisterWebhookWithThirdParty) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.DeregisterWebhookWithThirdParty | 
*DefaultApi* | [**disableStageTransition**](docs/DefaultApi.md#disableStageTransition) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.DisableStageTransition | 
*DefaultApi* | [**enableStageTransition**](docs/DefaultApi.md#enableStageTransition) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.EnableStageTransition | 
*DefaultApi* | [**getActionType**](docs/DefaultApi.md#getActionType) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.GetActionType | 
*DefaultApi* | [**getJobDetails**](docs/DefaultApi.md#getJobDetails) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.GetJobDetails | 
*DefaultApi* | [**getPipeline**](docs/DefaultApi.md#getPipeline) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.GetPipeline | 
*DefaultApi* | [**getPipelineExecution**](docs/DefaultApi.md#getPipelineExecution) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.GetPipelineExecution | 
*DefaultApi* | [**getPipelineState**](docs/DefaultApi.md#getPipelineState) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.GetPipelineState | 
*DefaultApi* | [**getThirdPartyJobDetails**](docs/DefaultApi.md#getThirdPartyJobDetails) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.GetThirdPartyJobDetails | 
*DefaultApi* | [**listActionExecutions**](docs/DefaultApi.md#listActionExecutions) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.ListActionExecutions | 
*DefaultApi* | [**listActionTypes**](docs/DefaultApi.md#listActionTypes) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.ListActionTypes | 
*DefaultApi* | [**listPipelineExecutions**](docs/DefaultApi.md#listPipelineExecutions) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.ListPipelineExecutions | 
*DefaultApi* | [**listPipelines**](docs/DefaultApi.md#listPipelines) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.ListPipelines | 
*DefaultApi* | [**listTagsForResource**](docs/DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.ListTagsForResource | 
*DefaultApi* | [**listWebhooks**](docs/DefaultApi.md#listWebhooks) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.ListWebhooks | 
*DefaultApi* | [**pollForJobs**](docs/DefaultApi.md#pollForJobs) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PollForJobs | 
*DefaultApi* | [**pollForThirdPartyJobs**](docs/DefaultApi.md#pollForThirdPartyJobs) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PollForThirdPartyJobs | 
*DefaultApi* | [**putActionRevision**](docs/DefaultApi.md#putActionRevision) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PutActionRevision | 
*DefaultApi* | [**putApprovalResult**](docs/DefaultApi.md#putApprovalResult) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PutApprovalResult | 
*DefaultApi* | [**putJobFailureResult**](docs/DefaultApi.md#putJobFailureResult) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PutJobFailureResult | 
*DefaultApi* | [**putJobSuccessResult**](docs/DefaultApi.md#putJobSuccessResult) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PutJobSuccessResult | 
*DefaultApi* | [**putThirdPartyJobFailureResult**](docs/DefaultApi.md#putThirdPartyJobFailureResult) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PutThirdPartyJobFailureResult | 
*DefaultApi* | [**putThirdPartyJobSuccessResult**](docs/DefaultApi.md#putThirdPartyJobSuccessResult) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PutThirdPartyJobSuccessResult | 
*DefaultApi* | [**putWebhook**](docs/DefaultApi.md#putWebhook) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PutWebhook | 
*DefaultApi* | [**registerWebhookWithThirdParty**](docs/DefaultApi.md#registerWebhookWithThirdParty) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.RegisterWebhookWithThirdParty | 
*DefaultApi* | [**retryStageExecution**](docs/DefaultApi.md#retryStageExecution) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.RetryStageExecution | 
*DefaultApi* | [**startPipelineExecution**](docs/DefaultApi.md#startPipelineExecution) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.StartPipelineExecution | 
*DefaultApi* | [**stopPipelineExecution**](docs/DefaultApi.md#stopPipelineExecution) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.StopPipelineExecution | 
*DefaultApi* | [**tagResource**](docs/DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.TagResource | 
*DefaultApi* | [**untagResource**](docs/DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.UntagResource | 
*DefaultApi* | [**updateActionType**](docs/DefaultApi.md#updateActionType) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.UpdateActionType | 
*DefaultApi* | [**updatePipeline**](docs/DefaultApi.md#updatePipeline) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.UpdatePipeline | 


## Documentation for Models

 - [AWSSessionCredentials](docs/AWSSessionCredentials.md)
 - [AcknowledgeJobInput](docs/AcknowledgeJobInput.md)
 - [AcknowledgeJobOutput](docs/AcknowledgeJobOutput.md)
 - [AcknowledgeThirdPartyJobInput](docs/AcknowledgeThirdPartyJobInput.md)
 - [AcknowledgeThirdPartyJobOutput](docs/AcknowledgeThirdPartyJobOutput.md)
 - [ActionCategory](docs/ActionCategory.md)
 - [ActionConfiguration](docs/ActionConfiguration.md)
 - [ActionConfigurationProperty](docs/ActionConfigurationProperty.md)
 - [ActionConfigurationPropertyType](docs/ActionConfigurationPropertyType.md)
 - [ActionContext](docs/ActionContext.md)
 - [ActionDeclaration](docs/ActionDeclaration.md)
 - [ActionDeclarationActionTypeId](docs/ActionDeclarationActionTypeId.md)
 - [ActionExecution](docs/ActionExecution.md)
 - [ActionExecutionDetail](docs/ActionExecutionDetail.md)
 - [ActionExecutionDetailInput](docs/ActionExecutionDetailInput.md)
 - [ActionExecutionDetailOutput](docs/ActionExecutionDetailOutput.md)
 - [ActionExecutionErrorDetails](docs/ActionExecutionErrorDetails.md)
 - [ActionExecutionFilter](docs/ActionExecutionFilter.md)
 - [ActionExecutionInput](docs/ActionExecutionInput.md)
 - [ActionExecutionOutput](docs/ActionExecutionOutput.md)
 - [ActionExecutionOutputExecutionResult](docs/ActionExecutionOutputExecutionResult.md)
 - [ActionExecutionResult](docs/ActionExecutionResult.md)
 - [ActionExecutionStatus](docs/ActionExecutionStatus.md)
 - [ActionOwner](docs/ActionOwner.md)
 - [ActionRevision](docs/ActionRevision.md)
 - [ActionState](docs/ActionState.md)
 - [ActionStateLatestExecution](docs/ActionStateLatestExecution.md)
 - [ActionType](docs/ActionType.md)
 - [ActionTypeArtifactDetails](docs/ActionTypeArtifactDetails.md)
 - [ActionTypeDeclaration](docs/ActionTypeDeclaration.md)
 - [ActionTypeDeclarationExecutor](docs/ActionTypeDeclarationExecutor.md)
 - [ActionTypeDeclarationId](docs/ActionTypeDeclarationId.md)
 - [ActionTypeDeclarationInputArtifactDetails](docs/ActionTypeDeclarationInputArtifactDetails.md)
 - [ActionTypeDeclarationOutputArtifactDetails](docs/ActionTypeDeclarationOutputArtifactDetails.md)
 - [ActionTypeDeclarationPermissions](docs/ActionTypeDeclarationPermissions.md)
 - [ActionTypeDeclarationUrls](docs/ActionTypeDeclarationUrls.md)
 - [ActionTypeExecutor](docs/ActionTypeExecutor.md)
 - [ActionTypeExecutorConfiguration](docs/ActionTypeExecutorConfiguration.md)
 - [ActionTypeId](docs/ActionTypeId.md)
 - [ActionTypeIdentifier](docs/ActionTypeIdentifier.md)
 - [ActionTypePermissions](docs/ActionTypePermissions.md)
 - [ActionTypeProperty](docs/ActionTypeProperty.md)
 - [ActionTypeSettings](docs/ActionTypeSettings.md)
 - [ActionTypeUrls](docs/ActionTypeUrls.md)
 - [ApprovalResult](docs/ApprovalResult.md)
 - [ApprovalStatus](docs/ApprovalStatus.md)
 - [Artifact](docs/Artifact.md)
 - [ArtifactDetail](docs/ArtifactDetail.md)
 - [ArtifactDetailS3location](docs/ArtifactDetailS3location.md)
 - [ArtifactDetails](docs/ArtifactDetails.md)
 - [ArtifactLocation](docs/ArtifactLocation.md)
 - [ArtifactLocationS3Location](docs/ArtifactLocationS3Location.md)
 - [ArtifactLocationType](docs/ArtifactLocationType.md)
 - [ArtifactRevision](docs/ArtifactRevision.md)
 - [ArtifactStore](docs/ArtifactStore.md)
 - [ArtifactStoreEncryptionKey](docs/ArtifactStoreEncryptionKey.md)
 - [ArtifactStoreType](docs/ArtifactStoreType.md)
 - [BlockerDeclaration](docs/BlockerDeclaration.md)
 - [BlockerType](docs/BlockerType.md)
 - [CreateCustomActionTypeInput](docs/CreateCustomActionTypeInput.md)
 - [CreateCustomActionTypeInputInputArtifactDetails](docs/CreateCustomActionTypeInputInputArtifactDetails.md)
 - [CreateCustomActionTypeInputOutputArtifactDetails](docs/CreateCustomActionTypeInputOutputArtifactDetails.md)
 - [CreateCustomActionTypeInputSettings](docs/CreateCustomActionTypeInputSettings.md)
 - [CreateCustomActionTypeOutput](docs/CreateCustomActionTypeOutput.md)
 - [CreateCustomActionTypeOutputActionType](docs/CreateCustomActionTypeOutputActionType.md)
 - [CreatePipelineInput](docs/CreatePipelineInput.md)
 - [CreatePipelineOutput](docs/CreatePipelineOutput.md)
 - [CreatePipelineOutputPipeline](docs/CreatePipelineOutputPipeline.md)
 - [CurrentRevision](docs/CurrentRevision.md)
 - [DeleteCustomActionTypeInput](docs/DeleteCustomActionTypeInput.md)
 - [DeletePipelineInput](docs/DeletePipelineInput.md)
 - [DeleteWebhookInput](docs/DeleteWebhookInput.md)
 - [DeregisterWebhookWithThirdPartyInput](docs/DeregisterWebhookWithThirdPartyInput.md)
 - [DisableStageTransitionInput](docs/DisableStageTransitionInput.md)
 - [EnableStageTransitionInput](docs/EnableStageTransitionInput.md)
 - [EncryptionKey](docs/EncryptionKey.md)
 - [EncryptionKeyType](docs/EncryptionKeyType.md)
 - [ErrorDetails](docs/ErrorDetails.md)
 - [ExecutionDetails](docs/ExecutionDetails.md)
 - [ExecutionTrigger](docs/ExecutionTrigger.md)
 - [ExecutorConfiguration](docs/ExecutorConfiguration.md)
 - [ExecutorConfigurationJobWorkerExecutorConfiguration](docs/ExecutorConfigurationJobWorkerExecutorConfiguration.md)
 - [ExecutorConfigurationLambdaExecutorConfiguration](docs/ExecutorConfigurationLambdaExecutorConfiguration.md)
 - [ExecutorType](docs/ExecutorType.md)
 - [FailureDetails](docs/FailureDetails.md)
 - [FailureType](docs/FailureType.md)
 - [GetActionTypeInput](docs/GetActionTypeInput.md)
 - [GetActionTypeOutput](docs/GetActionTypeOutput.md)
 - [GetActionTypeOutputActionType](docs/GetActionTypeOutputActionType.md)
 - [GetJobDetailsInput](docs/GetJobDetailsInput.md)
 - [GetJobDetailsOutput](docs/GetJobDetailsOutput.md)
 - [GetJobDetailsOutputJobDetails](docs/GetJobDetailsOutputJobDetails.md)
 - [GetPipelineExecutionInput](docs/GetPipelineExecutionInput.md)
 - [GetPipelineExecutionOutput](docs/GetPipelineExecutionOutput.md)
 - [GetPipelineExecutionOutputPipelineExecution](docs/GetPipelineExecutionOutputPipelineExecution.md)
 - [GetPipelineInput](docs/GetPipelineInput.md)
 - [GetPipelineOutput](docs/GetPipelineOutput.md)
 - [GetPipelineOutputMetadata](docs/GetPipelineOutputMetadata.md)
 - [GetPipelineStateInput](docs/GetPipelineStateInput.md)
 - [GetPipelineStateOutput](docs/GetPipelineStateOutput.md)
 - [GetThirdPartyJobDetailsInput](docs/GetThirdPartyJobDetailsInput.md)
 - [GetThirdPartyJobDetailsOutput](docs/GetThirdPartyJobDetailsOutput.md)
 - [GetThirdPartyJobDetailsOutputJobDetails](docs/GetThirdPartyJobDetailsOutputJobDetails.md)
 - [InputArtifact](docs/InputArtifact.md)
 - [Job](docs/Job.md)
 - [JobData](docs/JobData.md)
 - [JobDataActionConfiguration](docs/JobDataActionConfiguration.md)
 - [JobDataArtifactCredentials](docs/JobDataArtifactCredentials.md)
 - [JobDataEncryptionKey](docs/JobDataEncryptionKey.md)
 - [JobDataPipelineContext](docs/JobDataPipelineContext.md)
 - [JobDetails](docs/JobDetails.md)
 - [JobDetailsData](docs/JobDetailsData.md)
 - [JobStatus](docs/JobStatus.md)
 - [JobWorkerExecutorConfiguration](docs/JobWorkerExecutorConfiguration.md)
 - [LambdaExecutorConfiguration](docs/LambdaExecutorConfiguration.md)
 - [ListActionExecutionsInput](docs/ListActionExecutionsInput.md)
 - [ListActionExecutionsInputFilter](docs/ListActionExecutionsInputFilter.md)
 - [ListActionExecutionsOutput](docs/ListActionExecutionsOutput.md)
 - [ListActionTypesInput](docs/ListActionTypesInput.md)
 - [ListActionTypesOutput](docs/ListActionTypesOutput.md)
 - [ListPipelineExecutionsInput](docs/ListPipelineExecutionsInput.md)
 - [ListPipelineExecutionsOutput](docs/ListPipelineExecutionsOutput.md)
 - [ListPipelinesInput](docs/ListPipelinesInput.md)
 - [ListPipelinesOutput](docs/ListPipelinesOutput.md)
 - [ListTagsForResourceInput](docs/ListTagsForResourceInput.md)
 - [ListTagsForResourceOutput](docs/ListTagsForResourceOutput.md)
 - [ListWebhookItem](docs/ListWebhookItem.md)
 - [ListWebhookItemDefinition](docs/ListWebhookItemDefinition.md)
 - [ListWebhooksInput](docs/ListWebhooksInput.md)
 - [ListWebhooksOutput](docs/ListWebhooksOutput.md)
 - [OutputArtifact](docs/OutputArtifact.md)
 - [PipelineContext](docs/PipelineContext.md)
 - [PipelineContextAction](docs/PipelineContextAction.md)
 - [PipelineContextStage](docs/PipelineContextStage.md)
 - [PipelineDeclaration](docs/PipelineDeclaration.md)
 - [PipelineDeclarationArtifactStore](docs/PipelineDeclarationArtifactStore.md)
 - [PipelineExecution](docs/PipelineExecution.md)
 - [PipelineExecutionStatus](docs/PipelineExecutionStatus.md)
 - [PipelineExecutionSummary](docs/PipelineExecutionSummary.md)
 - [PipelineExecutionSummaryStopTrigger](docs/PipelineExecutionSummaryStopTrigger.md)
 - [PipelineExecutionSummaryTrigger](docs/PipelineExecutionSummaryTrigger.md)
 - [PipelineMetadata](docs/PipelineMetadata.md)
 - [PipelineSummary](docs/PipelineSummary.md)
 - [PollForJobsInput](docs/PollForJobsInput.md)
 - [PollForJobsInputActionTypeId](docs/PollForJobsInputActionTypeId.md)
 - [PollForJobsOutput](docs/PollForJobsOutput.md)
 - [PollForThirdPartyJobsInput](docs/PollForThirdPartyJobsInput.md)
 - [PollForThirdPartyJobsOutput](docs/PollForThirdPartyJobsOutput.md)
 - [PutActionRevisionInput](docs/PutActionRevisionInput.md)
 - [PutActionRevisionInputActionRevision](docs/PutActionRevisionInputActionRevision.md)
 - [PutActionRevisionOutput](docs/PutActionRevisionOutput.md)
 - [PutApprovalResultInput](docs/PutApprovalResultInput.md)
 - [PutApprovalResultInputResult](docs/PutApprovalResultInputResult.md)
 - [PutApprovalResultOutput](docs/PutApprovalResultOutput.md)
 - [PutJobFailureResultInput](docs/PutJobFailureResultInput.md)
 - [PutJobFailureResultInputFailureDetails](docs/PutJobFailureResultInputFailureDetails.md)
 - [PutJobSuccessResultInput](docs/PutJobSuccessResultInput.md)
 - [PutJobSuccessResultInputCurrentRevision](docs/PutJobSuccessResultInputCurrentRevision.md)
 - [PutJobSuccessResultInputExecutionDetails](docs/PutJobSuccessResultInputExecutionDetails.md)
 - [PutThirdPartyJobFailureResultInput](docs/PutThirdPartyJobFailureResultInput.md)
 - [PutThirdPartyJobFailureResultInputFailureDetails](docs/PutThirdPartyJobFailureResultInputFailureDetails.md)
 - [PutThirdPartyJobSuccessResultInput](docs/PutThirdPartyJobSuccessResultInput.md)
 - [PutThirdPartyJobSuccessResultInputCurrentRevision](docs/PutThirdPartyJobSuccessResultInputCurrentRevision.md)
 - [PutThirdPartyJobSuccessResultInputExecutionDetails](docs/PutThirdPartyJobSuccessResultInputExecutionDetails.md)
 - [PutWebhookInput](docs/PutWebhookInput.md)
 - [PutWebhookInputWebhook](docs/PutWebhookInputWebhook.md)
 - [PutWebhookOutput](docs/PutWebhookOutput.md)
 - [PutWebhookOutputWebhook](docs/PutWebhookOutputWebhook.md)
 - [RegisterWebhookWithThirdPartyInput](docs/RegisterWebhookWithThirdPartyInput.md)
 - [RetryStageExecutionInput](docs/RetryStageExecutionInput.md)
 - [RetryStageExecutionOutput](docs/RetryStageExecutionOutput.md)
 - [S3ArtifactLocation](docs/S3ArtifactLocation.md)
 - [S3Location](docs/S3Location.md)
 - [SourceRevision](docs/SourceRevision.md)
 - [StageContext](docs/StageContext.md)
 - [StageDeclaration](docs/StageDeclaration.md)
 - [StageExecution](docs/StageExecution.md)
 - [StageExecutionStatus](docs/StageExecutionStatus.md)
 - [StageRetryMode](docs/StageRetryMode.md)
 - [StageState](docs/StageState.md)
 - [StageStateInboundTransitionState](docs/StageStateInboundTransitionState.md)
 - [StageStateLatestExecution](docs/StageStateLatestExecution.md)
 - [StageTransitionType](docs/StageTransitionType.md)
 - [StartPipelineExecutionInput](docs/StartPipelineExecutionInput.md)
 - [StartPipelineExecutionOutput](docs/StartPipelineExecutionOutput.md)
 - [StopExecutionTrigger](docs/StopExecutionTrigger.md)
 - [StopPipelineExecutionInput](docs/StopPipelineExecutionInput.md)
 - [StopPipelineExecutionOutput](docs/StopPipelineExecutionOutput.md)
 - [Tag](docs/Tag.md)
 - [TagResourceInput](docs/TagResourceInput.md)
 - [ThirdPartyJob](docs/ThirdPartyJob.md)
 - [ThirdPartyJobData](docs/ThirdPartyJobData.md)
 - [ThirdPartyJobDataArtifactCredentials](docs/ThirdPartyJobDataArtifactCredentials.md)
 - [ThirdPartyJobDataEncryptionKey](docs/ThirdPartyJobDataEncryptionKey.md)
 - [ThirdPartyJobDataPipelineContext](docs/ThirdPartyJobDataPipelineContext.md)
 - [ThirdPartyJobDetails](docs/ThirdPartyJobDetails.md)
 - [ThirdPartyJobDetailsData](docs/ThirdPartyJobDetailsData.md)
 - [TransitionState](docs/TransitionState.md)
 - [TriggerType](docs/TriggerType.md)
 - [UntagResourceInput](docs/UntagResourceInput.md)
 - [UpdateActionTypeInput](docs/UpdateActionTypeInput.md)
 - [UpdateActionTypeInputActionType](docs/UpdateActionTypeInputActionType.md)
 - [UpdatePipelineInput](docs/UpdatePipelineInput.md)
 - [UpdatePipelineInputPipeline](docs/UpdatePipelineInputPipeline.md)
 - [UpdatePipelineOutput](docs/UpdatePipelineOutput.md)
 - [UpdatePipelineOutputPipeline](docs/UpdatePipelineOutputPipeline.md)
 - [WebhookAuthConfiguration](docs/WebhookAuthConfiguration.md)
 - [WebhookAuthenticationType](docs/WebhookAuthenticationType.md)
 - [WebhookDefinition](docs/WebhookDefinition.md)
 - [WebhookDefinitionAuthenticationConfiguration](docs/WebhookDefinitionAuthenticationConfiguration.md)
 - [WebhookFilterRule](docs/WebhookFilterRule.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="hmac"></a>
### hmac

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

mike.ralphson@gmail.com

