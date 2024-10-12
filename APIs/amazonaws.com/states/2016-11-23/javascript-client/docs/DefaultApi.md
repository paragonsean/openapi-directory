# AwsStepFunctions.DefaultApi

All URIs are relative to *http://states.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createActivity**](DefaultApi.md#createActivity) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.CreateActivity | 
[**createStateMachine**](DefaultApi.md#createStateMachine) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.CreateStateMachine | 
[**createStateMachineAlias**](DefaultApi.md#createStateMachineAlias) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.CreateStateMachineAlias | 
[**deleteActivity**](DefaultApi.md#deleteActivity) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DeleteActivity | 
[**deleteStateMachine**](DefaultApi.md#deleteStateMachine) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DeleteStateMachine | 
[**deleteStateMachineAlias**](DefaultApi.md#deleteStateMachineAlias) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DeleteStateMachineAlias | 
[**deleteStateMachineVersion**](DefaultApi.md#deleteStateMachineVersion) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DeleteStateMachineVersion | 
[**describeActivity**](DefaultApi.md#describeActivity) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DescribeActivity | 
[**describeExecution**](DefaultApi.md#describeExecution) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DescribeExecution | 
[**describeMapRun**](DefaultApi.md#describeMapRun) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DescribeMapRun | 
[**describeStateMachine**](DefaultApi.md#describeStateMachine) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DescribeStateMachine | 
[**describeStateMachineAlias**](DefaultApi.md#describeStateMachineAlias) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DescribeStateMachineAlias | 
[**describeStateMachineForExecution**](DefaultApi.md#describeStateMachineForExecution) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DescribeStateMachineForExecution | 
[**getActivityTask**](DefaultApi.md#getActivityTask) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.GetActivityTask | 
[**getExecutionHistory**](DefaultApi.md#getExecutionHistory) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.GetExecutionHistory | 
[**listActivities**](DefaultApi.md#listActivities) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.ListActivities | 
[**listExecutions**](DefaultApi.md#listExecutions) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.ListExecutions | 
[**listMapRuns**](DefaultApi.md#listMapRuns) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.ListMapRuns | 
[**listStateMachineAliases**](DefaultApi.md#listStateMachineAliases) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.ListStateMachineAliases | 
[**listStateMachineVersions**](DefaultApi.md#listStateMachineVersions) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.ListStateMachineVersions | 
[**listStateMachines**](DefaultApi.md#listStateMachines) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.ListStateMachines | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.ListTagsForResource | 
[**publishStateMachineVersion**](DefaultApi.md#publishStateMachineVersion) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.PublishStateMachineVersion | 
[**sendTaskFailure**](DefaultApi.md#sendTaskFailure) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.SendTaskFailure | 
[**sendTaskHeartbeat**](DefaultApi.md#sendTaskHeartbeat) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.SendTaskHeartbeat | 
[**sendTaskSuccess**](DefaultApi.md#sendTaskSuccess) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.SendTaskSuccess | 
[**startExecution**](DefaultApi.md#startExecution) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.StartExecution | 
[**startSyncExecution**](DefaultApi.md#startSyncExecution) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.StartSyncExecution | 
[**stopExecution**](DefaultApi.md#stopExecution) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.StopExecution | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.TagResource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.UntagResource | 
[**updateMapRun**](DefaultApi.md#updateMapRun) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.UpdateMapRun | 
[**updateStateMachine**](DefaultApi.md#updateStateMachine) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.UpdateStateMachine | 
[**updateStateMachineAlias**](DefaultApi.md#updateStateMachineAlias) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.UpdateStateMachineAlias | 



## createActivity

> CreateActivityOutput createActivity(xAmzTarget, createActivityInput, opts)



&lt;p&gt;Creates an activity. An activity is a task that you write in any programming language and host on any machine that has access to Step Functions. Activities must poll Step Functions using the &lt;code&gt;GetActivityTask&lt;/code&gt; API action and respond using &lt;code&gt;SendTask*&lt;/code&gt; API actions. This function lets Step Functions know the existence of your activity and returns an identifier for use in a state machine and when polling from the activity.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;CreateActivity&lt;/code&gt; is an idempotent API. Subsequent requests won’t create a duplicate resource if it was already created. &lt;code&gt;CreateActivity&lt;/code&gt;&#39;s idempotency check is based on the activity &lt;code&gt;name&lt;/code&gt;. If a following request has different &lt;code&gt;tags&lt;/code&gt; values, Step Functions will ignore these differences and treat it as an idempotent request of the previous. In this case, &lt;code&gt;tags&lt;/code&gt; will not be updated, even if they are different.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createActivityInput = new AwsStepFunctions.CreateActivityInput(); // CreateActivityInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createActivity(xAmzTarget, createActivityInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **createActivityInput** | [**CreateActivityInput**](CreateActivityInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateActivityOutput**](CreateActivityOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStateMachine

> CreateStateMachineOutput createStateMachine(xAmzTarget, createStateMachineInput, opts)



&lt;p&gt;Creates a state machine. A state machine consists of a collection of states that can do work (&lt;code&gt;Task&lt;/code&gt; states), determine to which states to transition next (&lt;code&gt;Choice&lt;/code&gt; states), stop an execution with an error (&lt;code&gt;Fail&lt;/code&gt; states), and so on. State machines are specified using a JSON-based, structured language. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html\&quot;&gt;Amazon States Language&lt;/a&gt; in the Step Functions User Guide.&lt;/p&gt; &lt;p&gt;If you set the &lt;code&gt;publish&lt;/code&gt; parameter of this API action to &lt;code&gt;true&lt;/code&gt;, it publishes version &lt;code&gt;1&lt;/code&gt; as the first revision of the state machine.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;CreateStateMachine&lt;/code&gt; is an idempotent API. Subsequent requests won’t create a duplicate resource if it was already created. &lt;code&gt;CreateStateMachine&lt;/code&gt;&#39;s idempotency check is based on the state machine &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;definition&lt;/code&gt;, &lt;code&gt;type&lt;/code&gt;, &lt;code&gt;LoggingConfiguration&lt;/code&gt;, and &lt;code&gt;TracingConfiguration&lt;/code&gt;. The check is also based on the &lt;code&gt;publish&lt;/code&gt; and &lt;code&gt;versionDescription&lt;/code&gt; parameters. If a following request has a different &lt;code&gt;roleArn&lt;/code&gt; or &lt;code&gt;tags&lt;/code&gt;, Step Functions will ignore these differences and treat it as an idempotent request of the previous. In this case, &lt;code&gt;roleArn&lt;/code&gt; and &lt;code&gt;tags&lt;/code&gt; will not be updated, even if they are different.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createStateMachineInput = new AwsStepFunctions.CreateStateMachineInput(); // CreateStateMachineInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createStateMachine(xAmzTarget, createStateMachineInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **createStateMachineInput** | [**CreateStateMachineInput**](CreateStateMachineInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateStateMachineOutput**](CreateStateMachineOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStateMachineAlias

> CreateStateMachineAliasOutput createStateMachineAlias(xAmzTarget, createStateMachineAliasInput, opts)



&lt;p&gt;Creates an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt; for a state machine that points to one or two &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;versions&lt;/a&gt; of the same state machine. You can set your application to call &lt;a&gt;StartExecution&lt;/a&gt; with an alias and update the version the alias uses without changing the client&#39;s code.&lt;/p&gt; &lt;p&gt;You can also map an alias to split &lt;a&gt;StartExecution&lt;/a&gt; requests between two versions of a state machine. To do this, add a second &lt;code&gt;RoutingConfig&lt;/code&gt; object in the &lt;code&gt;routingConfiguration&lt;/code&gt; parameter. You must also specify the percentage of execution run requests each version should receive in both &lt;code&gt;RoutingConfig&lt;/code&gt; objects. Step Functions randomly chooses which version runs a given execution based on the percentage you specify.&lt;/p&gt; &lt;p&gt;To create an alias that points to a single version, specify a single &lt;code&gt;RoutingConfig&lt;/code&gt; object with a &lt;code&gt;weight&lt;/code&gt; set to 100.&lt;/p&gt; &lt;p&gt;You can create up to 100 aliases for each state machine. You must delete unused aliases using the &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; API action.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateStateMachineAlias&lt;/code&gt; is an idempotent API. Step Functions bases the idempotency check on the &lt;code&gt;stateMachineArn&lt;/code&gt;, &lt;code&gt;description&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, and &lt;code&gt;routingConfiguration&lt;/code&gt; parameters. Requests that contain the same values for these parameters return a successful idempotent response without creating a duplicate resource.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineAliases&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createStateMachineAliasInput = new AwsStepFunctions.CreateStateMachineAliasInput(); // CreateStateMachineAliasInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createStateMachineAlias(xAmzTarget, createStateMachineAliasInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **createStateMachineAliasInput** | [**CreateStateMachineAliasInput**](CreateStateMachineAliasInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateStateMachineAliasOutput**](CreateStateMachineAliasOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteActivity

> Object deleteActivity(xAmzTarget, deleteActivityInput, opts)



Deletes an activity.

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteActivityInput = new AwsStepFunctions.DeleteActivityInput(); // DeleteActivityInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteActivity(xAmzTarget, deleteActivityInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **deleteActivityInput** | [**DeleteActivityInput**](DeleteActivityInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteStateMachine

> Object deleteStateMachine(xAmzTarget, deleteStateMachineInput, opts)



&lt;p&gt;Deletes a state machine. This is an asynchronous operation: It sets the state machine&#39;s status to &lt;code&gt;DELETING&lt;/code&gt; and begins the deletion process. &lt;/p&gt; &lt;p&gt;A qualified state machine ARN can either refer to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine, a version ARN, or an alias ARN.&lt;/p&gt; &lt;p&gt;The following are some examples of qualified and unqualified state machine ARNs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a &lt;i&gt;Distributed Map state&lt;/i&gt;, the request fails with &lt;code&gt;ValidationException&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following unqualified state machine ARN refers to a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This API action also deletes all &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;versions&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;aliases&lt;/a&gt; associated with a state machine.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For &lt;code&gt;EXPRESS&lt;/code&gt; state machines, the deletion happens eventually (usually in less than a minute). Running executions may emit logs after &lt;code&gt;DeleteStateMachine&lt;/code&gt; API is called.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteStateMachineInput = new AwsStepFunctions.DeleteStateMachineInput(); // DeleteStateMachineInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteStateMachine(xAmzTarget, deleteStateMachineInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **deleteStateMachineInput** | [**DeleteStateMachineInput**](DeleteStateMachineInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteStateMachineAlias

> Object deleteStateMachineAlias(xAmzTarget, deleteStateMachineAliasInput, opts)



&lt;p&gt;Deletes a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;After you delete a state machine alias, you can&#39;t use it to start executions. When you delete a state machine alias, Step Functions doesn&#39;t delete the state machine versions that alias references.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineAliases&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteStateMachineAliasInput = new AwsStepFunctions.DeleteStateMachineAliasInput(); // DeleteStateMachineAliasInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteStateMachineAlias(xAmzTarget, deleteStateMachineAliasInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **deleteStateMachineAliasInput** | [**DeleteStateMachineAliasInput**](DeleteStateMachineAliasInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteStateMachineVersion

> Object deleteStateMachineVersion(xAmzTarget, deleteStateMachineVersionInput, opts)



&lt;p&gt;Deletes a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt;. After you delete a version, you can&#39;t call &lt;a&gt;StartExecution&lt;/a&gt; using that version&#39;s ARN or use the version with a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Deleting a state machine version won&#39;t terminate its in-progress executions.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;You can&#39;t delete a state machine version currently referenced by one or more aliases. Before you delete a version, you must either delete the aliases or update them to point to another state machine version.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PublishStateMachineVersion&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineVersions&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteStateMachineVersionInput = new AwsStepFunctions.DeleteStateMachineVersionInput(); // DeleteStateMachineVersionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteStateMachineVersion(xAmzTarget, deleteStateMachineVersionInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **deleteStateMachineVersionInput** | [**DeleteStateMachineVersionInput**](DeleteStateMachineVersionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeActivity

> DescribeActivityOutput describeActivity(xAmzTarget, describeActivityInput, opts)



&lt;p&gt;Describes an activity.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeActivityInput = new AwsStepFunctions.DescribeActivityInput(); // DescribeActivityInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeActivity(xAmzTarget, describeActivityInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **describeActivityInput** | [**DescribeActivityInput**](DescribeActivityInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeActivityOutput**](DescribeActivityOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeExecution

> DescribeExecutionOutput describeExecution(xAmzTarget, describeExecutionInput, opts)



&lt;p&gt;Provides information about a state machine execution, such as the state machine associated with the execution, the execution input and output, and relevant execution metadata. Use this API action to return the Map Run Amazon Resource Name (ARN) if the execution was dispatched by a Map Run.&lt;/p&gt; &lt;p&gt;If you specify a version or alias ARN when you call the &lt;a&gt;StartExecution&lt;/a&gt; API action, &lt;code&gt;DescribeExecution&lt;/code&gt; returns that ARN.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Executions of an &lt;code&gt;EXPRESS&lt;/code&gt; state machinearen&#39;t supported by &lt;code&gt;DescribeExecution&lt;/code&gt; unless a Map Run dispatched them.&lt;/p&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeExecutionInput = new AwsStepFunctions.DescribeExecutionInput(); // DescribeExecutionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeExecution(xAmzTarget, describeExecutionInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **describeExecutionInput** | [**DescribeExecutionInput**](DescribeExecutionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeExecutionOutput**](DescribeExecutionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeMapRun

> DescribeMapRunOutput describeMapRun(xAmzTarget, describeMapRunInput, opts)



Provides information about a Map Run&#39;s configuration, progress, and results. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html\&quot;&gt;Examining Map Run&lt;/a&gt; in the &lt;i&gt;Step Functions Developer Guide&lt;/i&gt;.

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeMapRunInput = new AwsStepFunctions.DescribeMapRunInput(); // DescribeMapRunInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeMapRun(xAmzTarget, describeMapRunInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **describeMapRunInput** | [**DescribeMapRunInput**](DescribeMapRunInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeMapRunOutput**](DescribeMapRunOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeStateMachine

> DescribeStateMachineOutput describeStateMachine(xAmzTarget, describeStateMachineInput, opts)



&lt;p&gt;Provides information about a state machine&#39;s definition, its IAM role Amazon Resource Name (ARN), and configuration.&lt;/p&gt; &lt;p&gt;A qualified state machine ARN can either refer to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine, a version ARN, or an alias ARN.&lt;/p&gt; &lt;p&gt;The following are some examples of qualified and unqualified state machine ARNs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a &lt;i&gt;Distributed Map state&lt;/i&gt;, the request fails with &lt;code&gt;ValidationException&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to an alias named &lt;code&gt;PROD&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine:PROD&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following unqualified state machine ARN refers to a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This API action returns the details for a state machine version if the &lt;code&gt;stateMachineArn&lt;/code&gt; you specify is a state machine version ARN.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeStateMachineInput = new AwsStepFunctions.DescribeStateMachineInput(); // DescribeStateMachineInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeStateMachine(xAmzTarget, describeStateMachineInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **describeStateMachineInput** | [**DescribeStateMachineInput**](DescribeStateMachineInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeStateMachineOutput**](DescribeStateMachineOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeStateMachineAlias

> DescribeStateMachineAliasOutput describeStateMachineAlias(xAmzTarget, describeStateMachineAliasInput, opts)



&lt;p&gt;Returns details about a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineAliases&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeStateMachineAliasInput = new AwsStepFunctions.DescribeStateMachineAliasInput(); // DescribeStateMachineAliasInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeStateMachineAlias(xAmzTarget, describeStateMachineAliasInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **describeStateMachineAliasInput** | [**DescribeStateMachineAliasInput**](DescribeStateMachineAliasInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeStateMachineAliasOutput**](DescribeStateMachineAliasOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeStateMachineForExecution

> DescribeStateMachineForExecutionOutput describeStateMachineForExecution(xAmzTarget, describeStateMachineForExecutionInput, opts)



&lt;p&gt;Provides information about a state machine&#39;s definition, its execution role ARN, and configuration. If a Map Run dispatched the execution, this action returns the Map Run Amazon Resource Name (ARN) in the response. The state machine returned is the state machine associated with the Map Run.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This API action is not supported by &lt;code&gt;EXPRESS&lt;/code&gt; state machines.&lt;/p&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeStateMachineForExecutionInput = new AwsStepFunctions.DescribeStateMachineForExecutionInput(); // DescribeStateMachineForExecutionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeStateMachineForExecution(xAmzTarget, describeStateMachineForExecutionInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **describeStateMachineForExecutionInput** | [**DescribeStateMachineForExecutionInput**](DescribeStateMachineForExecutionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeStateMachineForExecutionOutput**](DescribeStateMachineForExecutionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getActivityTask

> GetActivityTaskOutput getActivityTask(xAmzTarget, getActivityTaskInput, opts)



&lt;p&gt;Used by workers to retrieve a task (with the specified activity ARN) which has been scheduled for execution by a running state machine. This initiates a long poll, where the service holds the HTTP connection open and responds as soon as a task becomes available (i.e. an execution of a task of this type is needed.) The maximum time the service holds on to the request before responding is 60 seconds. If no task is available within 60 seconds, the poll returns a &lt;code&gt;taskToken&lt;/code&gt; with a null string.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API action isn&#39;t logged in CloudTrail.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;Workers should set their client side socket timeout to at least 65 seconds (5 seconds higher than the maximum time the service may hold the poll request).&lt;/p&gt; &lt;p&gt;Polling with &lt;code&gt;GetActivityTask&lt;/code&gt; can cause latency in some implementations. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/bp-activity-pollers.html\&quot;&gt;Avoid Latency When Polling for Activity Tasks&lt;/a&gt; in the Step Functions Developer Guide.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getActivityTaskInput = new AwsStepFunctions.GetActivityTaskInput(); // GetActivityTaskInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getActivityTask(xAmzTarget, getActivityTaskInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **getActivityTaskInput** | [**GetActivityTaskInput**](GetActivityTaskInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetActivityTaskOutput**](GetActivityTaskOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getExecutionHistory

> GetExecutionHistoryOutput getExecutionHistory(xAmzTarget, getExecutionHistoryInput, opts)



&lt;p&gt;Returns the history of the specified execution as a list of events. By default, the results are returned in ascending order of the &lt;code&gt;timeStamp&lt;/code&gt; of the events. Use the &lt;code&gt;reverseOrder&lt;/code&gt; parameter to get the latest events first.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;p&gt;This API action is not supported by &lt;code&gt;EXPRESS&lt;/code&gt; state machines.&lt;/p&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getExecutionHistoryInput = new AwsStepFunctions.GetExecutionHistoryInput(); // GetExecutionHistoryInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.getExecutionHistory(xAmzTarget, getExecutionHistoryInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **getExecutionHistoryInput** | [**GetExecutionHistoryInput**](GetExecutionHistoryInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**GetExecutionHistoryOutput**](GetExecutionHistoryOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listActivities

> ListActivitiesOutput listActivities(xAmzTarget, listActivitiesInput, opts)



&lt;p&gt;Lists the existing activities.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listActivitiesInput = new AwsStepFunctions.ListActivitiesInput(); // ListActivitiesInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listActivities(xAmzTarget, listActivitiesInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **listActivitiesInput** | [**ListActivitiesInput**](ListActivitiesInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListActivitiesOutput**](ListActivitiesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listExecutions

> ListExecutionsOutput listExecutions(xAmzTarget, listExecutionsInput, opts)



&lt;p&gt;Lists all executions of a state machine or a Map Run. You can list all executions related to a state machine by specifying a state machine Amazon Resource Name (ARN), or those related to a Map Run by specifying a Map Run ARN.&lt;/p&gt; &lt;p&gt;You can also provide a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt; ARN or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt; ARN to list the executions associated with a specific alias or version.&lt;/p&gt; &lt;p&gt;Results are sorted by time, with the most recent execution first.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This API action is not supported by &lt;code&gt;EXPRESS&lt;/code&gt; state machines.&lt;/p&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listExecutionsInput = new AwsStepFunctions.ListExecutionsInput(); // ListExecutionsInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listExecutions(xAmzTarget, listExecutionsInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **listExecutionsInput** | [**ListExecutionsInput**](ListExecutionsInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListExecutionsOutput**](ListExecutionsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listMapRuns

> ListMapRunsOutput listMapRuns(xAmzTarget, listMapRunsInput, opts)



Lists all Map Runs that were started by a given state machine execution. Use this API action to obtain Map Run ARNs, and then call &lt;code&gt;DescribeMapRun&lt;/code&gt; to obtain more information, if needed.

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listMapRunsInput = new AwsStepFunctions.ListMapRunsInput(); // ListMapRunsInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listMapRuns(xAmzTarget, listMapRunsInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **listMapRunsInput** | [**ListMapRunsInput**](ListMapRunsInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListMapRunsOutput**](ListMapRunsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listStateMachineAliases

> ListStateMachineAliasesOutput listStateMachineAliases(xAmzTarget, listStateMachineAliasesInput, opts)



&lt;p&gt;Lists &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;aliases&lt;/a&gt; for a specified state machine ARN. Results are sorted by time, with the most recently created aliases listed first. &lt;/p&gt; &lt;p&gt;To list aliases that reference a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt;, you can specify the version ARN in the &lt;code&gt;stateMachineArn&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listStateMachineAliasesInput = new AwsStepFunctions.ListStateMachineAliasesInput(); // ListStateMachineAliasesInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listStateMachineAliases(xAmzTarget, listStateMachineAliasesInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **listStateMachineAliasesInput** | [**ListStateMachineAliasesInput**](ListStateMachineAliasesInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListStateMachineAliasesOutput**](ListStateMachineAliasesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listStateMachineVersions

> ListStateMachineVersionsOutput listStateMachineVersions(xAmzTarget, listStateMachineVersionsInput, opts)



&lt;p&gt;Lists &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;versions&lt;/a&gt; for the specified state machine Amazon Resource Name (ARN).&lt;/p&gt; &lt;p&gt;The results are sorted in descending order of the version creation time.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PublishStateMachineVersion&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineVersion&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listStateMachineVersionsInput = new AwsStepFunctions.ListStateMachineVersionsInput(); // ListStateMachineVersionsInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listStateMachineVersions(xAmzTarget, listStateMachineVersionsInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **listStateMachineVersionsInput** | [**ListStateMachineVersionsInput**](ListStateMachineVersionsInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListStateMachineVersionsOutput**](ListStateMachineVersionsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listStateMachines

> ListStateMachinesOutput listStateMachines(xAmzTarget, listStateMachinesInput, opts)



&lt;p&gt;Lists the existing state machines.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listStateMachinesInput = new AwsStepFunctions.ListStateMachinesInput(); // ListStateMachinesInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listStateMachines(xAmzTarget, listStateMachinesInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **listStateMachinesInput** | [**ListStateMachinesInput**](ListStateMachinesInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListStateMachinesOutput**](ListStateMachinesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceOutput listTagsForResource(xAmzTarget, listTagsForResourceInput, opts)



&lt;p&gt;List tags for a given resource.&lt;/p&gt; &lt;p&gt;Tags may only contain Unicode letters, digits, white space, or these symbols: &lt;code&gt;_ . : / &#x3D; + - @&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceInput = new AwsStepFunctions.ListTagsForResourceInput(); // ListTagsForResourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(xAmzTarget, listTagsForResourceInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **listTagsForResourceInput** | [**ListTagsForResourceInput**](ListTagsForResourceInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceOutput**](ListTagsForResourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## publishStateMachineVersion

> PublishStateMachineVersionOutput publishStateMachineVersion(xAmzTarget, publishStateMachineVersionInput, opts)



&lt;p&gt;Creates a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt; from the current revision of a state machine. Use versions to create immutable snapshots of your state machine. You can start executions from versions either directly or with an alias. To create an alias, use &lt;a&gt;CreateStateMachineAlias&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can publish up to 1000 versions for each state machine. You must manually delete unused versions using the &lt;a&gt;DeleteStateMachineVersion&lt;/a&gt; API action.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PublishStateMachineVersion&lt;/code&gt; is an idempotent API. It doesn&#39;t create a duplicate state machine version if it already exists for the current revision. Step Functions bases &lt;code&gt;PublishStateMachineVersion&lt;/code&gt;&#39;s idempotency check on the &lt;code&gt;stateMachineArn&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, and &lt;code&gt;revisionId&lt;/code&gt; parameters. Requests with the same parameters return a successful idempotent response. If you don&#39;t specify a &lt;code&gt;revisionId&lt;/code&gt;, Step Functions checks for a previously published version of the state machine&#39;s current revision.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineVersion&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineVersions&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let publishStateMachineVersionInput = new AwsStepFunctions.PublishStateMachineVersionInput(); // PublishStateMachineVersionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.publishStateMachineVersion(xAmzTarget, publishStateMachineVersionInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **publishStateMachineVersionInput** | [**PublishStateMachineVersionInput**](PublishStateMachineVersionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PublishStateMachineVersionOutput**](PublishStateMachineVersionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendTaskFailure

> Object sendTaskFailure(xAmzTarget, sendTaskFailureInput, opts)



Used by activity workers and task states using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token\&quot;&gt;callback&lt;/a&gt; pattern to report that the task identified by the &lt;code&gt;taskToken&lt;/code&gt; failed.

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let sendTaskFailureInput = new AwsStepFunctions.SendTaskFailureInput(); // SendTaskFailureInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendTaskFailure(xAmzTarget, sendTaskFailureInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **sendTaskFailureInput** | [**SendTaskFailureInput**](SendTaskFailureInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendTaskHeartbeat

> Object sendTaskHeartbeat(xAmzTarget, sendTaskHeartbeatInput, opts)



&lt;p&gt;Used by activity workers and task states using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token\&quot;&gt;callback&lt;/a&gt; pattern to report to Step Functions that the task represented by the specified &lt;code&gt;taskToken&lt;/code&gt; is still making progress. This action resets the &lt;code&gt;Heartbeat&lt;/code&gt; clock. The &lt;code&gt;Heartbeat&lt;/code&gt; threshold is specified in the state machine&#39;s Amazon States Language definition (&lt;code&gt;HeartbeatSeconds&lt;/code&gt;). This action does not in itself create an event in the execution history. However, if the task times out, the execution history contains an &lt;code&gt;ActivityTimedOut&lt;/code&gt; entry for activities, or a &lt;code&gt;TaskTimedOut&lt;/code&gt; entry for for tasks using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-sync\&quot;&gt;job run&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token\&quot;&gt;callback&lt;/a&gt; pattern.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;Timeout&lt;/code&gt; of a task, defined in the state machine&#39;s Amazon States Language definition, is its maximum allowed duration, regardless of the number of &lt;a&gt;SendTaskHeartbeat&lt;/a&gt; requests received. Use &lt;code&gt;HeartbeatSeconds&lt;/code&gt; to configure the timeout interval for heartbeats.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let sendTaskHeartbeatInput = new AwsStepFunctions.SendTaskHeartbeatInput(); // SendTaskHeartbeatInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendTaskHeartbeat(xAmzTarget, sendTaskHeartbeatInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **sendTaskHeartbeatInput** | [**SendTaskHeartbeatInput**](SendTaskHeartbeatInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendTaskSuccess

> Object sendTaskSuccess(xAmzTarget, sendTaskSuccessInput, opts)



Used by activity workers and task states using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token\&quot;&gt;callback&lt;/a&gt; pattern to report that the task identified by the &lt;code&gt;taskToken&lt;/code&gt; completed successfully.

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let sendTaskSuccessInput = new AwsStepFunctions.SendTaskSuccessInput(); // SendTaskSuccessInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendTaskSuccess(xAmzTarget, sendTaskSuccessInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **sendTaskSuccessInput** | [**SendTaskSuccessInput**](SendTaskSuccessInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startExecution

> StartExecutionOutput startExecution(xAmzTarget, startExecutionInput, opts)



&lt;p&gt;Starts a state machine execution.&lt;/p&gt; &lt;p&gt;A qualified state machine ARN can either refer to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine, a version ARN, or an alias ARN.&lt;/p&gt; &lt;p&gt;The following are some examples of qualified and unqualified state machine ARNs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a &lt;i&gt;Distributed Map state&lt;/i&gt;, the request fails with &lt;code&gt;ValidationException&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to an alias named &lt;code&gt;PROD&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine:PROD&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following unqualified state machine ARN refers to a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you start an execution with an unqualified state machine ARN, Step Functions uses the latest revision of the state machine for the execution.&lt;/p&gt; &lt;p&gt;To start executions of a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt;, call &lt;code&gt;StartExecution&lt;/code&gt; and provide the version ARN or the ARN of an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt; that points to the version.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;StartExecution&lt;/code&gt; is idempotent for &lt;code&gt;STANDARD&lt;/code&gt; workflows. For a &lt;code&gt;STANDARD&lt;/code&gt; workflow, if you call &lt;code&gt;StartExecution&lt;/code&gt; with the same name and input as a running execution, the call succeeds and return the same response as the original request. If the execution is closed or if the input is different, it returns a &lt;code&gt;400 ExecutionAlreadyExists&lt;/code&gt; error. You can reuse names after 90 days. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartExecution&lt;/code&gt; isn&#39;t idempotent for &lt;code&gt;EXPRESS&lt;/code&gt; workflows. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startExecutionInput = new AwsStepFunctions.StartExecutionInput(); // StartExecutionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startExecution(xAmzTarget, startExecutionInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **startExecutionInput** | [**StartExecutionInput**](StartExecutionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartExecutionOutput**](StartExecutionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startSyncExecution

> StartSyncExecutionOutput startSyncExecution(xAmzTarget, startSyncExecutionInput, opts)



&lt;p&gt;Starts a Synchronous Express state machine execution. &lt;code&gt;StartSyncExecution&lt;/code&gt; is not available for &lt;code&gt;STANDARD&lt;/code&gt; workflows.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;StartSyncExecution&lt;/code&gt; will return a &lt;code&gt;200 OK&lt;/code&gt; response, even if your execution fails, because the status code in the API response doesn&#39;t reflect function errors. Error codes are reserved for errors that prevent your execution from running, such as permissions errors, limit errors, or issues with your state machine code and configuration. &lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;This API action isn&#39;t logged in CloudTrail.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startSyncExecutionInput = new AwsStepFunctions.StartSyncExecutionInput(); // StartSyncExecutionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startSyncExecution(xAmzTarget, startSyncExecutionInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **startSyncExecutionInput** | [**StartSyncExecutionInput**](StartSyncExecutionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartSyncExecutionOutput**](StartSyncExecutionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopExecution

> StopExecutionOutput stopExecution(xAmzTarget, stopExecutionInput, opts)



&lt;p&gt;Stops an execution.&lt;/p&gt; &lt;p&gt;This API action is not supported by &lt;code&gt;EXPRESS&lt;/code&gt; state machines.&lt;/p&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let stopExecutionInput = new AwsStepFunctions.StopExecutionInput(); // StopExecutionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopExecution(xAmzTarget, stopExecutionInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **stopExecutionInput** | [**StopExecutionInput**](StopExecutionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopExecutionOutput**](StopExecutionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(xAmzTarget, tagResourceInput, opts)



&lt;p&gt;Add a tag to a Step Functions resource.&lt;/p&gt; &lt;p&gt;An array of key-value pairs. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Billing and Cost Management User Guide&lt;/i&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html\&quot;&gt;Controlling Access Using IAM Tags&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Tags may only contain Unicode letters, digits, white space, or these symbols: &lt;code&gt;_ . : / &#x3D; + - @&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceInput = new AwsStepFunctions.TagResourceInput(); // TagResourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(xAmzTarget, tagResourceInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **tagResourceInput** | [**TagResourceInput**](TagResourceInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(xAmzTarget, untagResourceInput, opts)



Remove a tag from a Step Functions resource

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceInput = new AwsStepFunctions.UntagResourceInput(); // UntagResourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(xAmzTarget, untagResourceInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **untagResourceInput** | [**UntagResourceInput**](UntagResourceInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMapRun

> Object updateMapRun(xAmzTarget, updateMapRunInput, opts)



Updates an in-progress Map Run&#39;s configuration to include changes to the settings that control maximum concurrency and Map Run failure.

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateMapRunInput = new AwsStepFunctions.UpdateMapRunInput(); // UpdateMapRunInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateMapRun(xAmzTarget, updateMapRunInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **updateMapRunInput** | [**UpdateMapRunInput**](UpdateMapRunInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateStateMachine

> UpdateStateMachineOutput updateStateMachine(xAmzTarget, updateStateMachineInput, opts)



&lt;p&gt;Updates an existing state machine by modifying its &lt;code&gt;definition&lt;/code&gt;, &lt;code&gt;roleArn&lt;/code&gt;, or &lt;code&gt;loggingConfiguration&lt;/code&gt;. Running executions will continue to use the previous &lt;code&gt;definition&lt;/code&gt; and &lt;code&gt;roleArn&lt;/code&gt;. You must include at least one of &lt;code&gt;definition&lt;/code&gt; or &lt;code&gt;roleArn&lt;/code&gt; or you will receive a &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;A qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine. For example, the qualified state machine ARN &lt;code&gt;arn:partition:states:region:account-id:stateMachine:stateMachineName/mapStateLabel&lt;/code&gt; refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in the state machine named &lt;code&gt;stateMachineName&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;A qualified state machine ARN can either refer to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine, a version ARN, or an alias ARN.&lt;/p&gt; &lt;p&gt;The following are some examples of qualified and unqualified state machine ARNs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a &lt;i&gt;Distributed Map state&lt;/i&gt;, the request fails with &lt;code&gt;ValidationException&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to an alias named &lt;code&gt;PROD&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine:PROD&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following unqualified state machine ARN refers to a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;After you update your state machine, you can set the &lt;code&gt;publish&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt; in the same action to publish a new &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt;. This way, you can opt-in to strict versioning of your state machine.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Step Functions assigns monotonically increasing integers for state machine versions, starting at version number 1.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;All &lt;code&gt;StartExecution&lt;/code&gt; calls within a few seconds use the updated &lt;code&gt;definition&lt;/code&gt; and &lt;code&gt;roleArn&lt;/code&gt;. Executions started immediately after you call &lt;code&gt;UpdateStateMachine&lt;/code&gt; may use the previous state machine &lt;code&gt;definition&lt;/code&gt; and &lt;code&gt;roleArn&lt;/code&gt;. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateStateMachineInput = new AwsStepFunctions.UpdateStateMachineInput(); // UpdateStateMachineInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateStateMachine(xAmzTarget, updateStateMachineInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **updateStateMachineInput** | [**UpdateStateMachineInput**](UpdateStateMachineInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateStateMachineOutput**](UpdateStateMachineOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateStateMachineAlias

> UpdateStateMachineAliasOutput updateStateMachineAlias(xAmzTarget, updateStateMachineAliasInput, opts)



&lt;p&gt;Updates the configuration of an existing state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt; by modifying its &lt;code&gt;description&lt;/code&gt; or &lt;code&gt;routingConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You must specify at least one of the &lt;code&gt;description&lt;/code&gt; or &lt;code&gt;routingConfiguration&lt;/code&gt; parameters to update a state machine alias.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;UpdateStateMachineAlias&lt;/code&gt; is an idempotent API. Step Functions bases the idempotency check on the &lt;code&gt;stateMachineAliasArn&lt;/code&gt;, &lt;code&gt;description&lt;/code&gt;, and &lt;code&gt;routingConfiguration&lt;/code&gt; parameters. Requests with the same parameters return an idempotent response.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. All &lt;a&gt;StartExecution&lt;/a&gt; requests made within a few seconds use the latest alias configuration. Executions started immediately after calling &lt;code&gt;UpdateStateMachineAlias&lt;/code&gt; may use the previous routing configuration.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineAliases&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsStepFunctions from 'aws_step_functions';
let defaultClient = AwsStepFunctions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsStepFunctions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateStateMachineAliasInput = new AwsStepFunctions.UpdateStateMachineAliasInput(); // UpdateStateMachineAliasInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateStateMachineAlias(xAmzTarget, updateStateMachineAliasInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **updateStateMachineAliasInput** | [**UpdateStateMachineAliasInput**](UpdateStateMachineAliasInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateStateMachineAliasOutput**](UpdateStateMachineAliasOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

