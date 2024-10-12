# aws_code_pipeline

AwsCodePipeline - JavaScript client for aws_code_pipeline
<fullname>CodePipeline</fullname> <p> <b>Overview</b> </p> <p>This is the CodePipeline API Reference. This guide provides descriptions of the actions and data types for CodePipeline. Some functionality for your pipeline can only be configured through the API. For more information, see the <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html\">CodePipeline User Guide</a>.</p> <p>You can use the CodePipeline API to work with pipelines, stages, actions, and transitions.</p> <p> <i>Pipelines</i> are models of automated release processes. Each pipeline is uniquely named, and consists of stages, actions, and transitions. </p> <p>You can work with pipelines by calling:</p> <ul> <li> <p> <a>CreatePipeline</a>, which creates a uniquely named pipeline.</p> </li> <li> <p> <a>DeletePipeline</a>, which deletes the specified pipeline.</p> </li> <li> <p> <a>GetPipeline</a>, which returns information about the pipeline structure and pipeline metadata, including the pipeline Amazon Resource Name (ARN).</p> </li> <li> <p> <a>GetPipelineExecution</a>, which returns information about a specific execution of a pipeline.</p> </li> <li> <p> <a>GetPipelineState</a>, which returns information about the current state of the stages and actions of a pipeline.</p> </li> <li> <p> <a>ListActionExecutions</a>, which returns action-level details for past executions. The details include full stage and action-level details, including individual action duration, status, any errors that occurred during the execution, and input and output artifact location details.</p> </li> <li> <p> <a>ListPipelines</a>, which gets a summary of all of the pipelines associated with your account.</p> </li> <li> <p> <a>ListPipelineExecutions</a>, which gets a summary of the most recent executions for a pipeline.</p> </li> <li> <p> <a>StartPipelineExecution</a>, which runs the most recent revision of an artifact through the pipeline.</p> </li> <li> <p> <a>StopPipelineExecution</a>, which stops the specified pipeline execution from continuing through the pipeline.</p> </li> <li> <p> <a>UpdatePipeline</a>, which updates a pipeline with edits or changes to the structure of the pipeline.</p> </li> </ul> <p>Pipelines include <i>stages</i>. Each stage contains one or more actions that must complete before the next stage begins. A stage results in success or failure. If a stage fails, the pipeline stops at that stage and remains stopped until either a new version of an artifact appears in the source location, or a user takes action to rerun the most recent artifact through the pipeline. You can call <a>GetPipelineState</a>, which displays the status of a pipeline, including the status of stages in the pipeline, or <a>GetPipeline</a>, which returns the entire structure of the pipeline, including the stages of that pipeline. For more information about the structure of stages and actions, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-structure.html\">CodePipeline Pipeline Structure Reference</a>.</p> <p>Pipeline stages include <i>actions</i> that are categorized into categories such as source or build actions performed in a stage of a pipeline. For example, you can use a source action to import artifacts into a pipeline from a source such as Amazon S3. Like stages, you do not work with actions directly in most cases, but you do define and interact with actions when working with pipeline operations such as <a>CreatePipeline</a> and <a>GetPipelineState</a>. Valid action categories are:</p> <ul> <li> <p>Source</p> </li> <li> <p>Build</p> </li> <li> <p>Test</p> </li> <li> <p>Deploy</p> </li> <li> <p>Approval</p> </li> <li> <p>Invoke</p> </li> </ul> <p>Pipelines also include <i>transitions</i>, which allow the transition of artifacts from one stage to the next in a pipeline after the actions in one stage complete.</p> <p>You can work with transitions by calling:</p> <ul> <li> <p> <a>DisableStageTransition</a>, which prevents artifacts from transitioning to the next stage in a pipeline.</p> </li> <li> <p> <a>EnableStageTransition</a>, which enables transition of artifacts between stages in a pipeline. </p> </li> </ul> <p> <b>Using the API to integrate with CodePipeline</b> </p> <p>For third-party integrators or developers who want to create their own integrations with CodePipeline, the expected sequence varies from the standard API user. To integrate with CodePipeline, developers need to work with the following items:</p> <p> <b>Jobs</b>, which are instances of an action. For example, a job for a source action might import a revision of an artifact from a source. </p> <p>You can work with jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetJobDetails</a>, which returns the details of a job.</p> </li> <li> <p> <a>PollForJobs</a>, which determines whether there are any jobs to act on.</p> </li> <li> <p> <a>PutJobFailureResult</a>, which provides details of a job failure. </p> </li> <li> <p> <a>PutJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul> <p> <b>Third party jobs</b>, which are instances of an action created by a partner action and integrated into CodePipeline. Partner actions are created by members of the Amazon Web Services Partner Network.</p> <p>You can work with third party jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeThirdPartyJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetThirdPartyJobDetails</a>, which requests the details of a job for a partner action.</p> </li> <li> <p> <a>PollForThirdPartyJobs</a>, which determines whether there are any jobs to act on. </p> </li> <li> <p> <a>PutThirdPartyJobFailureResult</a>, which provides details of a job failure.</p> </li> <li> <p> <a>PutThirdPartyJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul>
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2015-07-09
- Package version: 2015-07-09
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://github.com/mermade/aws2openapi](https://github.com/mermade/aws2openapi)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install aws_code_pipeline --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your aws_code_pipeline from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var AwsCodePipeline = require('aws_code_pipeline');

var defaultClient = AwsCodePipeline.ApiClient.instance;
// Configure API key authorization: hmac
var hmac = defaultClient.authentications['hmac'];
hmac.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix['Authorization'] = "Token"

var api = new AwsCodePipeline.DefaultApi()
var xAmzTarget = "xAmzTarget_example"; // {String} 
var acknowledgeJobInput = new AwsCodePipeline.AcknowledgeJobInput(); // {AcknowledgeJobInput} 
var opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // {String} 
  'xAmzDate': "xAmzDate_example", // {String} 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // {String} 
  'xAmzCredential': "xAmzCredential_example", // {String} 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // {String} 
  'xAmzSignature': "xAmzSignature_example", // {String} 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // {String} 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.acknowledgeJob(xAmzTarget, acknowledgeJobInput, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *http://codepipeline.us-east-1.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AwsCodePipeline.DefaultApi* | [**acknowledgeJob**](docs/DefaultApi.md#acknowledgeJob) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.AcknowledgeJob | 
*AwsCodePipeline.DefaultApi* | [**acknowledgeThirdPartyJob**](docs/DefaultApi.md#acknowledgeThirdPartyJob) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.AcknowledgeThirdPartyJob | 
*AwsCodePipeline.DefaultApi* | [**createCustomActionType**](docs/DefaultApi.md#createCustomActionType) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.CreateCustomActionType | 
*AwsCodePipeline.DefaultApi* | [**createPipeline**](docs/DefaultApi.md#createPipeline) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.CreatePipeline | 
*AwsCodePipeline.DefaultApi* | [**deleteCustomActionType**](docs/DefaultApi.md#deleteCustomActionType) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.DeleteCustomActionType | 
*AwsCodePipeline.DefaultApi* | [**deletePipeline**](docs/DefaultApi.md#deletePipeline) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.DeletePipeline | 
*AwsCodePipeline.DefaultApi* | [**deleteWebhook**](docs/DefaultApi.md#deleteWebhook) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.DeleteWebhook | 
*AwsCodePipeline.DefaultApi* | [**deregisterWebhookWithThirdParty**](docs/DefaultApi.md#deregisterWebhookWithThirdParty) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.DeregisterWebhookWithThirdParty | 
*AwsCodePipeline.DefaultApi* | [**disableStageTransition**](docs/DefaultApi.md#disableStageTransition) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.DisableStageTransition | 
*AwsCodePipeline.DefaultApi* | [**enableStageTransition**](docs/DefaultApi.md#enableStageTransition) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.EnableStageTransition | 
*AwsCodePipeline.DefaultApi* | [**getActionType**](docs/DefaultApi.md#getActionType) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.GetActionType | 
*AwsCodePipeline.DefaultApi* | [**getJobDetails**](docs/DefaultApi.md#getJobDetails) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.GetJobDetails | 
*AwsCodePipeline.DefaultApi* | [**getPipeline**](docs/DefaultApi.md#getPipeline) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.GetPipeline | 
*AwsCodePipeline.DefaultApi* | [**getPipelineExecution**](docs/DefaultApi.md#getPipelineExecution) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.GetPipelineExecution | 
*AwsCodePipeline.DefaultApi* | [**getPipelineState**](docs/DefaultApi.md#getPipelineState) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.GetPipelineState | 
*AwsCodePipeline.DefaultApi* | [**getThirdPartyJobDetails**](docs/DefaultApi.md#getThirdPartyJobDetails) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.GetThirdPartyJobDetails | 
*AwsCodePipeline.DefaultApi* | [**listActionExecutions**](docs/DefaultApi.md#listActionExecutions) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.ListActionExecutions | 
*AwsCodePipeline.DefaultApi* | [**listActionTypes**](docs/DefaultApi.md#listActionTypes) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.ListActionTypes | 
*AwsCodePipeline.DefaultApi* | [**listPipelineExecutions**](docs/DefaultApi.md#listPipelineExecutions) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.ListPipelineExecutions | 
*AwsCodePipeline.DefaultApi* | [**listPipelines**](docs/DefaultApi.md#listPipelines) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.ListPipelines | 
*AwsCodePipeline.DefaultApi* | [**listTagsForResource**](docs/DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.ListTagsForResource | 
*AwsCodePipeline.DefaultApi* | [**listWebhooks**](docs/DefaultApi.md#listWebhooks) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.ListWebhooks | 
*AwsCodePipeline.DefaultApi* | [**pollForJobs**](docs/DefaultApi.md#pollForJobs) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PollForJobs | 
*AwsCodePipeline.DefaultApi* | [**pollForThirdPartyJobs**](docs/DefaultApi.md#pollForThirdPartyJobs) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PollForThirdPartyJobs | 
*AwsCodePipeline.DefaultApi* | [**putActionRevision**](docs/DefaultApi.md#putActionRevision) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PutActionRevision | 
*AwsCodePipeline.DefaultApi* | [**putApprovalResult**](docs/DefaultApi.md#putApprovalResult) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PutApprovalResult | 
*AwsCodePipeline.DefaultApi* | [**putJobFailureResult**](docs/DefaultApi.md#putJobFailureResult) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PutJobFailureResult | 
*AwsCodePipeline.DefaultApi* | [**putJobSuccessResult**](docs/DefaultApi.md#putJobSuccessResult) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PutJobSuccessResult | 
*AwsCodePipeline.DefaultApi* | [**putThirdPartyJobFailureResult**](docs/DefaultApi.md#putThirdPartyJobFailureResult) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PutThirdPartyJobFailureResult | 
*AwsCodePipeline.DefaultApi* | [**putThirdPartyJobSuccessResult**](docs/DefaultApi.md#putThirdPartyJobSuccessResult) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PutThirdPartyJobSuccessResult | 
*AwsCodePipeline.DefaultApi* | [**putWebhook**](docs/DefaultApi.md#putWebhook) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.PutWebhook | 
*AwsCodePipeline.DefaultApi* | [**registerWebhookWithThirdParty**](docs/DefaultApi.md#registerWebhookWithThirdParty) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.RegisterWebhookWithThirdParty | 
*AwsCodePipeline.DefaultApi* | [**retryStageExecution**](docs/DefaultApi.md#retryStageExecution) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.RetryStageExecution | 
*AwsCodePipeline.DefaultApi* | [**startPipelineExecution**](docs/DefaultApi.md#startPipelineExecution) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.StartPipelineExecution | 
*AwsCodePipeline.DefaultApi* | [**stopPipelineExecution**](docs/DefaultApi.md#stopPipelineExecution) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.StopPipelineExecution | 
*AwsCodePipeline.DefaultApi* | [**tagResource**](docs/DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.TagResource | 
*AwsCodePipeline.DefaultApi* | [**untagResource**](docs/DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.UntagResource | 
*AwsCodePipeline.DefaultApi* | [**updateActionType**](docs/DefaultApi.md#updateActionType) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.UpdateActionType | 
*AwsCodePipeline.DefaultApi* | [**updatePipeline**](docs/DefaultApi.md#updatePipeline) | **POST** /#X-Amz-Target&#x3D;CodePipeline_20150709.UpdatePipeline | 


## Documentation for Models

 - [AwsCodePipeline.AWSSessionCredentials](docs/AWSSessionCredentials.md)
 - [AwsCodePipeline.AcknowledgeJobInput](docs/AcknowledgeJobInput.md)
 - [AwsCodePipeline.AcknowledgeJobOutput](docs/AcknowledgeJobOutput.md)
 - [AwsCodePipeline.AcknowledgeThirdPartyJobInput](docs/AcknowledgeThirdPartyJobInput.md)
 - [AwsCodePipeline.AcknowledgeThirdPartyJobOutput](docs/AcknowledgeThirdPartyJobOutput.md)
 - [AwsCodePipeline.ActionCategory](docs/ActionCategory.md)
 - [AwsCodePipeline.ActionConfiguration](docs/ActionConfiguration.md)
 - [AwsCodePipeline.ActionConfigurationProperty](docs/ActionConfigurationProperty.md)
 - [AwsCodePipeline.ActionConfigurationPropertyType](docs/ActionConfigurationPropertyType.md)
 - [AwsCodePipeline.ActionContext](docs/ActionContext.md)
 - [AwsCodePipeline.ActionDeclaration](docs/ActionDeclaration.md)
 - [AwsCodePipeline.ActionDeclarationActionTypeId](docs/ActionDeclarationActionTypeId.md)
 - [AwsCodePipeline.ActionExecution](docs/ActionExecution.md)
 - [AwsCodePipeline.ActionExecutionDetail](docs/ActionExecutionDetail.md)
 - [AwsCodePipeline.ActionExecutionDetailInput](docs/ActionExecutionDetailInput.md)
 - [AwsCodePipeline.ActionExecutionDetailOutput](docs/ActionExecutionDetailOutput.md)
 - [AwsCodePipeline.ActionExecutionErrorDetails](docs/ActionExecutionErrorDetails.md)
 - [AwsCodePipeline.ActionExecutionFilter](docs/ActionExecutionFilter.md)
 - [AwsCodePipeline.ActionExecutionInput](docs/ActionExecutionInput.md)
 - [AwsCodePipeline.ActionExecutionOutput](docs/ActionExecutionOutput.md)
 - [AwsCodePipeline.ActionExecutionOutputExecutionResult](docs/ActionExecutionOutputExecutionResult.md)
 - [AwsCodePipeline.ActionExecutionResult](docs/ActionExecutionResult.md)
 - [AwsCodePipeline.ActionExecutionStatus](docs/ActionExecutionStatus.md)
 - [AwsCodePipeline.ActionOwner](docs/ActionOwner.md)
 - [AwsCodePipeline.ActionRevision](docs/ActionRevision.md)
 - [AwsCodePipeline.ActionState](docs/ActionState.md)
 - [AwsCodePipeline.ActionStateLatestExecution](docs/ActionStateLatestExecution.md)
 - [AwsCodePipeline.ActionType](docs/ActionType.md)
 - [AwsCodePipeline.ActionTypeArtifactDetails](docs/ActionTypeArtifactDetails.md)
 - [AwsCodePipeline.ActionTypeDeclaration](docs/ActionTypeDeclaration.md)
 - [AwsCodePipeline.ActionTypeDeclarationExecutor](docs/ActionTypeDeclarationExecutor.md)
 - [AwsCodePipeline.ActionTypeDeclarationId](docs/ActionTypeDeclarationId.md)
 - [AwsCodePipeline.ActionTypeDeclarationInputArtifactDetails](docs/ActionTypeDeclarationInputArtifactDetails.md)
 - [AwsCodePipeline.ActionTypeDeclarationOutputArtifactDetails](docs/ActionTypeDeclarationOutputArtifactDetails.md)
 - [AwsCodePipeline.ActionTypeDeclarationPermissions](docs/ActionTypeDeclarationPermissions.md)
 - [AwsCodePipeline.ActionTypeDeclarationUrls](docs/ActionTypeDeclarationUrls.md)
 - [AwsCodePipeline.ActionTypeExecutor](docs/ActionTypeExecutor.md)
 - [AwsCodePipeline.ActionTypeExecutorConfiguration](docs/ActionTypeExecutorConfiguration.md)
 - [AwsCodePipeline.ActionTypeId](docs/ActionTypeId.md)
 - [AwsCodePipeline.ActionTypeIdentifier](docs/ActionTypeIdentifier.md)
 - [AwsCodePipeline.ActionTypePermissions](docs/ActionTypePermissions.md)
 - [AwsCodePipeline.ActionTypeProperty](docs/ActionTypeProperty.md)
 - [AwsCodePipeline.ActionTypeSettings](docs/ActionTypeSettings.md)
 - [AwsCodePipeline.ActionTypeUrls](docs/ActionTypeUrls.md)
 - [AwsCodePipeline.ApprovalResult](docs/ApprovalResult.md)
 - [AwsCodePipeline.ApprovalStatus](docs/ApprovalStatus.md)
 - [AwsCodePipeline.Artifact](docs/Artifact.md)
 - [AwsCodePipeline.ArtifactDetail](docs/ArtifactDetail.md)
 - [AwsCodePipeline.ArtifactDetailS3location](docs/ArtifactDetailS3location.md)
 - [AwsCodePipeline.ArtifactDetails](docs/ArtifactDetails.md)
 - [AwsCodePipeline.ArtifactLocation](docs/ArtifactLocation.md)
 - [AwsCodePipeline.ArtifactLocationS3Location](docs/ArtifactLocationS3Location.md)
 - [AwsCodePipeline.ArtifactLocationType](docs/ArtifactLocationType.md)
 - [AwsCodePipeline.ArtifactRevision](docs/ArtifactRevision.md)
 - [AwsCodePipeline.ArtifactStore](docs/ArtifactStore.md)
 - [AwsCodePipeline.ArtifactStoreEncryptionKey](docs/ArtifactStoreEncryptionKey.md)
 - [AwsCodePipeline.ArtifactStoreType](docs/ArtifactStoreType.md)
 - [AwsCodePipeline.BlockerDeclaration](docs/BlockerDeclaration.md)
 - [AwsCodePipeline.BlockerType](docs/BlockerType.md)
 - [AwsCodePipeline.CreateCustomActionTypeInput](docs/CreateCustomActionTypeInput.md)
 - [AwsCodePipeline.CreateCustomActionTypeInputInputArtifactDetails](docs/CreateCustomActionTypeInputInputArtifactDetails.md)
 - [AwsCodePipeline.CreateCustomActionTypeInputOutputArtifactDetails](docs/CreateCustomActionTypeInputOutputArtifactDetails.md)
 - [AwsCodePipeline.CreateCustomActionTypeInputSettings](docs/CreateCustomActionTypeInputSettings.md)
 - [AwsCodePipeline.CreateCustomActionTypeOutput](docs/CreateCustomActionTypeOutput.md)
 - [AwsCodePipeline.CreateCustomActionTypeOutputActionType](docs/CreateCustomActionTypeOutputActionType.md)
 - [AwsCodePipeline.CreatePipelineInput](docs/CreatePipelineInput.md)
 - [AwsCodePipeline.CreatePipelineOutput](docs/CreatePipelineOutput.md)
 - [AwsCodePipeline.CreatePipelineOutputPipeline](docs/CreatePipelineOutputPipeline.md)
 - [AwsCodePipeline.CurrentRevision](docs/CurrentRevision.md)
 - [AwsCodePipeline.DeleteCustomActionTypeInput](docs/DeleteCustomActionTypeInput.md)
 - [AwsCodePipeline.DeletePipelineInput](docs/DeletePipelineInput.md)
 - [AwsCodePipeline.DeleteWebhookInput](docs/DeleteWebhookInput.md)
 - [AwsCodePipeline.DeregisterWebhookWithThirdPartyInput](docs/DeregisterWebhookWithThirdPartyInput.md)
 - [AwsCodePipeline.DisableStageTransitionInput](docs/DisableStageTransitionInput.md)
 - [AwsCodePipeline.EnableStageTransitionInput](docs/EnableStageTransitionInput.md)
 - [AwsCodePipeline.EncryptionKey](docs/EncryptionKey.md)
 - [AwsCodePipeline.EncryptionKeyType](docs/EncryptionKeyType.md)
 - [AwsCodePipeline.ErrorDetails](docs/ErrorDetails.md)
 - [AwsCodePipeline.ExecutionDetails](docs/ExecutionDetails.md)
 - [AwsCodePipeline.ExecutionTrigger](docs/ExecutionTrigger.md)
 - [AwsCodePipeline.ExecutorConfiguration](docs/ExecutorConfiguration.md)
 - [AwsCodePipeline.ExecutorConfigurationJobWorkerExecutorConfiguration](docs/ExecutorConfigurationJobWorkerExecutorConfiguration.md)
 - [AwsCodePipeline.ExecutorConfigurationLambdaExecutorConfiguration](docs/ExecutorConfigurationLambdaExecutorConfiguration.md)
 - [AwsCodePipeline.ExecutorType](docs/ExecutorType.md)
 - [AwsCodePipeline.FailureDetails](docs/FailureDetails.md)
 - [AwsCodePipeline.FailureType](docs/FailureType.md)
 - [AwsCodePipeline.GetActionTypeInput](docs/GetActionTypeInput.md)
 - [AwsCodePipeline.GetActionTypeOutput](docs/GetActionTypeOutput.md)
 - [AwsCodePipeline.GetActionTypeOutputActionType](docs/GetActionTypeOutputActionType.md)
 - [AwsCodePipeline.GetJobDetailsInput](docs/GetJobDetailsInput.md)
 - [AwsCodePipeline.GetJobDetailsOutput](docs/GetJobDetailsOutput.md)
 - [AwsCodePipeline.GetJobDetailsOutputJobDetails](docs/GetJobDetailsOutputJobDetails.md)
 - [AwsCodePipeline.GetPipelineExecutionInput](docs/GetPipelineExecutionInput.md)
 - [AwsCodePipeline.GetPipelineExecutionOutput](docs/GetPipelineExecutionOutput.md)
 - [AwsCodePipeline.GetPipelineExecutionOutputPipelineExecution](docs/GetPipelineExecutionOutputPipelineExecution.md)
 - [AwsCodePipeline.GetPipelineInput](docs/GetPipelineInput.md)
 - [AwsCodePipeline.GetPipelineOutput](docs/GetPipelineOutput.md)
 - [AwsCodePipeline.GetPipelineOutputMetadata](docs/GetPipelineOutputMetadata.md)
 - [AwsCodePipeline.GetPipelineStateInput](docs/GetPipelineStateInput.md)
 - [AwsCodePipeline.GetPipelineStateOutput](docs/GetPipelineStateOutput.md)
 - [AwsCodePipeline.GetThirdPartyJobDetailsInput](docs/GetThirdPartyJobDetailsInput.md)
 - [AwsCodePipeline.GetThirdPartyJobDetailsOutput](docs/GetThirdPartyJobDetailsOutput.md)
 - [AwsCodePipeline.GetThirdPartyJobDetailsOutputJobDetails](docs/GetThirdPartyJobDetailsOutputJobDetails.md)
 - [AwsCodePipeline.InputArtifact](docs/InputArtifact.md)
 - [AwsCodePipeline.Job](docs/Job.md)
 - [AwsCodePipeline.JobData](docs/JobData.md)
 - [AwsCodePipeline.JobDataActionConfiguration](docs/JobDataActionConfiguration.md)
 - [AwsCodePipeline.JobDataArtifactCredentials](docs/JobDataArtifactCredentials.md)
 - [AwsCodePipeline.JobDataEncryptionKey](docs/JobDataEncryptionKey.md)
 - [AwsCodePipeline.JobDataPipelineContext](docs/JobDataPipelineContext.md)
 - [AwsCodePipeline.JobDetails](docs/JobDetails.md)
 - [AwsCodePipeline.JobDetailsData](docs/JobDetailsData.md)
 - [AwsCodePipeline.JobStatus](docs/JobStatus.md)
 - [AwsCodePipeline.JobWorkerExecutorConfiguration](docs/JobWorkerExecutorConfiguration.md)
 - [AwsCodePipeline.LambdaExecutorConfiguration](docs/LambdaExecutorConfiguration.md)
 - [AwsCodePipeline.ListActionExecutionsInput](docs/ListActionExecutionsInput.md)
 - [AwsCodePipeline.ListActionExecutionsInputFilter](docs/ListActionExecutionsInputFilter.md)
 - [AwsCodePipeline.ListActionExecutionsOutput](docs/ListActionExecutionsOutput.md)
 - [AwsCodePipeline.ListActionTypesInput](docs/ListActionTypesInput.md)
 - [AwsCodePipeline.ListActionTypesOutput](docs/ListActionTypesOutput.md)
 - [AwsCodePipeline.ListPipelineExecutionsInput](docs/ListPipelineExecutionsInput.md)
 - [AwsCodePipeline.ListPipelineExecutionsOutput](docs/ListPipelineExecutionsOutput.md)
 - [AwsCodePipeline.ListPipelinesInput](docs/ListPipelinesInput.md)
 - [AwsCodePipeline.ListPipelinesOutput](docs/ListPipelinesOutput.md)
 - [AwsCodePipeline.ListTagsForResourceInput](docs/ListTagsForResourceInput.md)
 - [AwsCodePipeline.ListTagsForResourceOutput](docs/ListTagsForResourceOutput.md)
 - [AwsCodePipeline.ListWebhookItem](docs/ListWebhookItem.md)
 - [AwsCodePipeline.ListWebhookItemDefinition](docs/ListWebhookItemDefinition.md)
 - [AwsCodePipeline.ListWebhooksInput](docs/ListWebhooksInput.md)
 - [AwsCodePipeline.ListWebhooksOutput](docs/ListWebhooksOutput.md)
 - [AwsCodePipeline.OutputArtifact](docs/OutputArtifact.md)
 - [AwsCodePipeline.PipelineContext](docs/PipelineContext.md)
 - [AwsCodePipeline.PipelineContextAction](docs/PipelineContextAction.md)
 - [AwsCodePipeline.PipelineContextStage](docs/PipelineContextStage.md)
 - [AwsCodePipeline.PipelineDeclaration](docs/PipelineDeclaration.md)
 - [AwsCodePipeline.PipelineDeclarationArtifactStore](docs/PipelineDeclarationArtifactStore.md)
 - [AwsCodePipeline.PipelineExecution](docs/PipelineExecution.md)
 - [AwsCodePipeline.PipelineExecutionStatus](docs/PipelineExecutionStatus.md)
 - [AwsCodePipeline.PipelineExecutionSummary](docs/PipelineExecutionSummary.md)
 - [AwsCodePipeline.PipelineExecutionSummaryStopTrigger](docs/PipelineExecutionSummaryStopTrigger.md)
 - [AwsCodePipeline.PipelineExecutionSummaryTrigger](docs/PipelineExecutionSummaryTrigger.md)
 - [AwsCodePipeline.PipelineMetadata](docs/PipelineMetadata.md)
 - [AwsCodePipeline.PipelineSummary](docs/PipelineSummary.md)
 - [AwsCodePipeline.PollForJobsInput](docs/PollForJobsInput.md)
 - [AwsCodePipeline.PollForJobsInputActionTypeId](docs/PollForJobsInputActionTypeId.md)
 - [AwsCodePipeline.PollForJobsOutput](docs/PollForJobsOutput.md)
 - [AwsCodePipeline.PollForThirdPartyJobsInput](docs/PollForThirdPartyJobsInput.md)
 - [AwsCodePipeline.PollForThirdPartyJobsOutput](docs/PollForThirdPartyJobsOutput.md)
 - [AwsCodePipeline.PutActionRevisionInput](docs/PutActionRevisionInput.md)
 - [AwsCodePipeline.PutActionRevisionInputActionRevision](docs/PutActionRevisionInputActionRevision.md)
 - [AwsCodePipeline.PutActionRevisionOutput](docs/PutActionRevisionOutput.md)
 - [AwsCodePipeline.PutApprovalResultInput](docs/PutApprovalResultInput.md)
 - [AwsCodePipeline.PutApprovalResultInputResult](docs/PutApprovalResultInputResult.md)
 - [AwsCodePipeline.PutApprovalResultOutput](docs/PutApprovalResultOutput.md)
 - [AwsCodePipeline.PutJobFailureResultInput](docs/PutJobFailureResultInput.md)
 - [AwsCodePipeline.PutJobFailureResultInputFailureDetails](docs/PutJobFailureResultInputFailureDetails.md)
 - [AwsCodePipeline.PutJobSuccessResultInput](docs/PutJobSuccessResultInput.md)
 - [AwsCodePipeline.PutJobSuccessResultInputCurrentRevision](docs/PutJobSuccessResultInputCurrentRevision.md)
 - [AwsCodePipeline.PutJobSuccessResultInputExecutionDetails](docs/PutJobSuccessResultInputExecutionDetails.md)
 - [AwsCodePipeline.PutThirdPartyJobFailureResultInput](docs/PutThirdPartyJobFailureResultInput.md)
 - [AwsCodePipeline.PutThirdPartyJobFailureResultInputFailureDetails](docs/PutThirdPartyJobFailureResultInputFailureDetails.md)
 - [AwsCodePipeline.PutThirdPartyJobSuccessResultInput](docs/PutThirdPartyJobSuccessResultInput.md)
 - [AwsCodePipeline.PutThirdPartyJobSuccessResultInputCurrentRevision](docs/PutThirdPartyJobSuccessResultInputCurrentRevision.md)
 - [AwsCodePipeline.PutThirdPartyJobSuccessResultInputExecutionDetails](docs/PutThirdPartyJobSuccessResultInputExecutionDetails.md)
 - [AwsCodePipeline.PutWebhookInput](docs/PutWebhookInput.md)
 - [AwsCodePipeline.PutWebhookInputWebhook](docs/PutWebhookInputWebhook.md)
 - [AwsCodePipeline.PutWebhookOutput](docs/PutWebhookOutput.md)
 - [AwsCodePipeline.PutWebhookOutputWebhook](docs/PutWebhookOutputWebhook.md)
 - [AwsCodePipeline.RegisterWebhookWithThirdPartyInput](docs/RegisterWebhookWithThirdPartyInput.md)
 - [AwsCodePipeline.RetryStageExecutionInput](docs/RetryStageExecutionInput.md)
 - [AwsCodePipeline.RetryStageExecutionOutput](docs/RetryStageExecutionOutput.md)
 - [AwsCodePipeline.S3ArtifactLocation](docs/S3ArtifactLocation.md)
 - [AwsCodePipeline.S3Location](docs/S3Location.md)
 - [AwsCodePipeline.SourceRevision](docs/SourceRevision.md)
 - [AwsCodePipeline.StageContext](docs/StageContext.md)
 - [AwsCodePipeline.StageDeclaration](docs/StageDeclaration.md)
 - [AwsCodePipeline.StageExecution](docs/StageExecution.md)
 - [AwsCodePipeline.StageExecutionStatus](docs/StageExecutionStatus.md)
 - [AwsCodePipeline.StageRetryMode](docs/StageRetryMode.md)
 - [AwsCodePipeline.StageState](docs/StageState.md)
 - [AwsCodePipeline.StageStateInboundTransitionState](docs/StageStateInboundTransitionState.md)
 - [AwsCodePipeline.StageStateLatestExecution](docs/StageStateLatestExecution.md)
 - [AwsCodePipeline.StageTransitionType](docs/StageTransitionType.md)
 - [AwsCodePipeline.StartPipelineExecutionInput](docs/StartPipelineExecutionInput.md)
 - [AwsCodePipeline.StartPipelineExecutionOutput](docs/StartPipelineExecutionOutput.md)
 - [AwsCodePipeline.StopExecutionTrigger](docs/StopExecutionTrigger.md)
 - [AwsCodePipeline.StopPipelineExecutionInput](docs/StopPipelineExecutionInput.md)
 - [AwsCodePipeline.StopPipelineExecutionOutput](docs/StopPipelineExecutionOutput.md)
 - [AwsCodePipeline.Tag](docs/Tag.md)
 - [AwsCodePipeline.TagResourceInput](docs/TagResourceInput.md)
 - [AwsCodePipeline.ThirdPartyJob](docs/ThirdPartyJob.md)
 - [AwsCodePipeline.ThirdPartyJobData](docs/ThirdPartyJobData.md)
 - [AwsCodePipeline.ThirdPartyJobDataArtifactCredentials](docs/ThirdPartyJobDataArtifactCredentials.md)
 - [AwsCodePipeline.ThirdPartyJobDataEncryptionKey](docs/ThirdPartyJobDataEncryptionKey.md)
 - [AwsCodePipeline.ThirdPartyJobDataPipelineContext](docs/ThirdPartyJobDataPipelineContext.md)
 - [AwsCodePipeline.ThirdPartyJobDetails](docs/ThirdPartyJobDetails.md)
 - [AwsCodePipeline.ThirdPartyJobDetailsData](docs/ThirdPartyJobDetailsData.md)
 - [AwsCodePipeline.TransitionState](docs/TransitionState.md)
 - [AwsCodePipeline.TriggerType](docs/TriggerType.md)
 - [AwsCodePipeline.UntagResourceInput](docs/UntagResourceInput.md)
 - [AwsCodePipeline.UpdateActionTypeInput](docs/UpdateActionTypeInput.md)
 - [AwsCodePipeline.UpdateActionTypeInputActionType](docs/UpdateActionTypeInputActionType.md)
 - [AwsCodePipeline.UpdatePipelineInput](docs/UpdatePipelineInput.md)
 - [AwsCodePipeline.UpdatePipelineInputPipeline](docs/UpdatePipelineInputPipeline.md)
 - [AwsCodePipeline.UpdatePipelineOutput](docs/UpdatePipelineOutput.md)
 - [AwsCodePipeline.UpdatePipelineOutputPipeline](docs/UpdatePipelineOutputPipeline.md)
 - [AwsCodePipeline.WebhookAuthConfiguration](docs/WebhookAuthConfiguration.md)
 - [AwsCodePipeline.WebhookAuthenticationType](docs/WebhookAuthenticationType.md)
 - [AwsCodePipeline.WebhookDefinition](docs/WebhookDefinition.md)
 - [AwsCodePipeline.WebhookDefinitionAuthenticationConfiguration](docs/WebhookDefinitionAuthenticationConfiguration.md)
 - [AwsCodePipeline.WebhookFilterRule](docs/WebhookFilterRule.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### hmac


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

