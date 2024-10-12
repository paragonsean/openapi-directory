# DefaultApi

All URIs are relative to *http://states.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createActivity**](DefaultApi.md#createActivity) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.CreateActivity |  |
| [**createStateMachine**](DefaultApi.md#createStateMachine) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.CreateStateMachine |  |
| [**createStateMachineAlias**](DefaultApi.md#createStateMachineAlias) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.CreateStateMachineAlias |  |
| [**deleteActivity**](DefaultApi.md#deleteActivity) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DeleteActivity |  |
| [**deleteStateMachine**](DefaultApi.md#deleteStateMachine) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DeleteStateMachine |  |
| [**deleteStateMachineAlias**](DefaultApi.md#deleteStateMachineAlias) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DeleteStateMachineAlias |  |
| [**deleteStateMachineVersion**](DefaultApi.md#deleteStateMachineVersion) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DeleteStateMachineVersion |  |
| [**describeActivity**](DefaultApi.md#describeActivity) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DescribeActivity |  |
| [**describeExecution**](DefaultApi.md#describeExecution) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DescribeExecution |  |
| [**describeMapRun**](DefaultApi.md#describeMapRun) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DescribeMapRun |  |
| [**describeStateMachine**](DefaultApi.md#describeStateMachine) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DescribeStateMachine |  |
| [**describeStateMachineAlias**](DefaultApi.md#describeStateMachineAlias) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DescribeStateMachineAlias |  |
| [**describeStateMachineForExecution**](DefaultApi.md#describeStateMachineForExecution) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.DescribeStateMachineForExecution |  |
| [**getActivityTask**](DefaultApi.md#getActivityTask) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.GetActivityTask |  |
| [**getExecutionHistory**](DefaultApi.md#getExecutionHistory) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.GetExecutionHistory |  |
| [**listActivities**](DefaultApi.md#listActivities) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.ListActivities |  |
| [**listExecutions**](DefaultApi.md#listExecutions) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.ListExecutions |  |
| [**listMapRuns**](DefaultApi.md#listMapRuns) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.ListMapRuns |  |
| [**listStateMachineAliases**](DefaultApi.md#listStateMachineAliases) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.ListStateMachineAliases |  |
| [**listStateMachineVersions**](DefaultApi.md#listStateMachineVersions) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.ListStateMachineVersions |  |
| [**listStateMachines**](DefaultApi.md#listStateMachines) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.ListStateMachines |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.ListTagsForResource |  |
| [**publishStateMachineVersion**](DefaultApi.md#publishStateMachineVersion) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.PublishStateMachineVersion |  |
| [**sendTaskFailure**](DefaultApi.md#sendTaskFailure) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.SendTaskFailure |  |
| [**sendTaskHeartbeat**](DefaultApi.md#sendTaskHeartbeat) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.SendTaskHeartbeat |  |
| [**sendTaskSuccess**](DefaultApi.md#sendTaskSuccess) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.SendTaskSuccess |  |
| [**startExecution**](DefaultApi.md#startExecution) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.StartExecution |  |
| [**startSyncExecution**](DefaultApi.md#startSyncExecution) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.StartSyncExecution |  |
| [**stopExecution**](DefaultApi.md#stopExecution) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.StopExecution |  |
| [**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.TagResource |  |
| [**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.UntagResource |  |
| [**updateMapRun**](DefaultApi.md#updateMapRun) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.UpdateMapRun |  |
| [**updateStateMachine**](DefaultApi.md#updateStateMachine) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.UpdateStateMachine |  |
| [**updateStateMachineAlias**](DefaultApi.md#updateStateMachineAlias) | **POST** /#X-Amz-Target&#x3D;AWSStepFunctions.UpdateStateMachineAlias |  |


<a id="createActivity"></a>
# **createActivity**
> CreateActivityOutput createActivity(xAmzTarget, createActivityInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an activity. An activity is a task that you write in any programming language and host on any machine that has access to Step Functions. Activities must poll Step Functions using the &lt;code&gt;GetActivityTask&lt;/code&gt; API action and respond using &lt;code&gt;SendTask*&lt;/code&gt; API actions. This function lets Step Functions know the existence of your activity and returns an identifier for use in a state machine and when polling from the activity.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;CreateActivity&lt;/code&gt; is an idempotent API. Subsequent requests won’t create a duplicate resource if it was already created. &lt;code&gt;CreateActivity&lt;/code&gt;&#39;s idempotency check is based on the activity &lt;code&gt;name&lt;/code&gt;. If a following request has different &lt;code&gt;tags&lt;/code&gt; values, Step Functions will ignore these differences and treat it as an idempotent request of the previous. In this case, &lt;code&gt;tags&lt;/code&gt; will not be updated, even if they are different.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.CreateActivity"; // String | 
    CreateActivityInput createActivityInput = new CreateActivityInput(); // CreateActivityInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateActivityOutput result = apiInstance.createActivity(xAmzTarget, createActivityInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createActivity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.CreateActivity] |
| **createActivityInput** | [**CreateActivityInput**](CreateActivityInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateActivityOutput**](CreateActivityOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ActivityLimitExceeded |  -  |
| **481** | InvalidName |  -  |
| **482** | TooManyTags |  -  |

<a id="createStateMachine"></a>
# **createStateMachine**
> CreateStateMachineOutput createStateMachine(xAmzTarget, createStateMachineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a state machine. A state machine consists of a collection of states that can do work (&lt;code&gt;Task&lt;/code&gt; states), determine to which states to transition next (&lt;code&gt;Choice&lt;/code&gt; states), stop an execution with an error (&lt;code&gt;Fail&lt;/code&gt; states), and so on. State machines are specified using a JSON-based, structured language. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html\&quot;&gt;Amazon States Language&lt;/a&gt; in the Step Functions User Guide.&lt;/p&gt; &lt;p&gt;If you set the &lt;code&gt;publish&lt;/code&gt; parameter of this API action to &lt;code&gt;true&lt;/code&gt;, it publishes version &lt;code&gt;1&lt;/code&gt; as the first revision of the state machine.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;CreateStateMachine&lt;/code&gt; is an idempotent API. Subsequent requests won’t create a duplicate resource if it was already created. &lt;code&gt;CreateStateMachine&lt;/code&gt;&#39;s idempotency check is based on the state machine &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;definition&lt;/code&gt;, &lt;code&gt;type&lt;/code&gt;, &lt;code&gt;LoggingConfiguration&lt;/code&gt;, and &lt;code&gt;TracingConfiguration&lt;/code&gt;. The check is also based on the &lt;code&gt;publish&lt;/code&gt; and &lt;code&gt;versionDescription&lt;/code&gt; parameters. If a following request has a different &lt;code&gt;roleArn&lt;/code&gt; or &lt;code&gt;tags&lt;/code&gt;, Step Functions will ignore these differences and treat it as an idempotent request of the previous. In this case, &lt;code&gt;roleArn&lt;/code&gt; and &lt;code&gt;tags&lt;/code&gt; will not be updated, even if they are different.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.CreateStateMachine"; // String | 
    CreateStateMachineInput createStateMachineInput = new CreateStateMachineInput(); // CreateStateMachineInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateStateMachineOutput result = apiInstance.createStateMachine(xAmzTarget, createStateMachineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createStateMachine");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.CreateStateMachine] |
| **createStateMachineInput** | [**CreateStateMachineInput**](CreateStateMachineInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateStateMachineOutput**](CreateStateMachineOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArn |  -  |
| **481** | InvalidDefinition |  -  |
| **482** | InvalidName |  -  |
| **483** | InvalidLoggingConfiguration |  -  |
| **484** | InvalidTracingConfiguration |  -  |
| **485** | StateMachineAlreadyExists |  -  |
| **486** | StateMachineDeleting |  -  |
| **487** | StateMachineLimitExceeded |  -  |
| **488** | StateMachineTypeNotSupported |  -  |
| **489** | TooManyTags |  -  |
| **490** | ValidationException |  -  |
| **491** | ConflictException |  -  |

<a id="createStateMachineAlias"></a>
# **createStateMachineAlias**
> CreateStateMachineAliasOutput createStateMachineAlias(xAmzTarget, createStateMachineAliasInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt; for a state machine that points to one or two &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;versions&lt;/a&gt; of the same state machine. You can set your application to call &lt;a&gt;StartExecution&lt;/a&gt; with an alias and update the version the alias uses without changing the client&#39;s code.&lt;/p&gt; &lt;p&gt;You can also map an alias to split &lt;a&gt;StartExecution&lt;/a&gt; requests between two versions of a state machine. To do this, add a second &lt;code&gt;RoutingConfig&lt;/code&gt; object in the &lt;code&gt;routingConfiguration&lt;/code&gt; parameter. You must also specify the percentage of execution run requests each version should receive in both &lt;code&gt;RoutingConfig&lt;/code&gt; objects. Step Functions randomly chooses which version runs a given execution based on the percentage you specify.&lt;/p&gt; &lt;p&gt;To create an alias that points to a single version, specify a single &lt;code&gt;RoutingConfig&lt;/code&gt; object with a &lt;code&gt;weight&lt;/code&gt; set to 100.&lt;/p&gt; &lt;p&gt;You can create up to 100 aliases for each state machine. You must delete unused aliases using the &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; API action.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateStateMachineAlias&lt;/code&gt; is an idempotent API. Step Functions bases the idempotency check on the &lt;code&gt;stateMachineArn&lt;/code&gt;, &lt;code&gt;description&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, and &lt;code&gt;routingConfiguration&lt;/code&gt; parameters. Requests that contain the same values for these parameters return a successful idempotent response without creating a duplicate resource.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineAliases&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.CreateStateMachineAlias"; // String | 
    CreateStateMachineAliasInput createStateMachineAliasInput = new CreateStateMachineAliasInput(); // CreateStateMachineAliasInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateStateMachineAliasOutput result = apiInstance.createStateMachineAlias(xAmzTarget, createStateMachineAliasInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createStateMachineAlias");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.CreateStateMachineAlias] |
| **createStateMachineAliasInput** | [**CreateStateMachineAliasInput**](CreateStateMachineAliasInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateStateMachineAliasOutput**](CreateStateMachineAliasOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArn |  -  |
| **481** | InvalidName |  -  |
| **482** | ValidationException |  -  |
| **483** | StateMachineDeleting |  -  |
| **484** | ResourceNotFound |  -  |
| **485** | ConflictException |  -  |
| **486** | ServiceQuotaExceededException |  -  |

<a id="deleteActivity"></a>
# **deleteActivity**
> Object deleteActivity(xAmzTarget, deleteActivityInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes an activity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.DeleteActivity"; // String | 
    DeleteActivityInput deleteActivityInput = new DeleteActivityInput(); // DeleteActivityInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteActivity(xAmzTarget, deleteActivityInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteActivity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.DeleteActivity] |
| **deleteActivityInput** | [**DeleteActivityInput**](DeleteActivityInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArn |  -  |

<a id="deleteStateMachine"></a>
# **deleteStateMachine**
> Object deleteStateMachine(xAmzTarget, deleteStateMachineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a state machine. This is an asynchronous operation: It sets the state machine&#39;s status to &lt;code&gt;DELETING&lt;/code&gt; and begins the deletion process. &lt;/p&gt; &lt;p&gt;A qualified state machine ARN can either refer to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine, a version ARN, or an alias ARN.&lt;/p&gt; &lt;p&gt;The following are some examples of qualified and unqualified state machine ARNs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a &lt;i&gt;Distributed Map state&lt;/i&gt;, the request fails with &lt;code&gt;ValidationException&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following unqualified state machine ARN refers to a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This API action also deletes all &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;versions&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;aliases&lt;/a&gt; associated with a state machine.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For &lt;code&gt;EXPRESS&lt;/code&gt; state machines, the deletion happens eventually (usually in less than a minute). Running executions may emit logs after &lt;code&gt;DeleteStateMachine&lt;/code&gt; API is called.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.DeleteStateMachine"; // String | 
    DeleteStateMachineInput deleteStateMachineInput = new DeleteStateMachineInput(); // DeleteStateMachineInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteStateMachine(xAmzTarget, deleteStateMachineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteStateMachine");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.DeleteStateMachine] |
| **deleteStateMachineInput** | [**DeleteStateMachineInput**](DeleteStateMachineInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArn |  -  |
| **481** | ValidationException |  -  |

<a id="deleteStateMachineAlias"></a>
# **deleteStateMachineAlias**
> Object deleteStateMachineAlias(xAmzTarget, deleteStateMachineAliasInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;After you delete a state machine alias, you can&#39;t use it to start executions. When you delete a state machine alias, Step Functions doesn&#39;t delete the state machine versions that alias references.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineAliases&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.DeleteStateMachineAlias"; // String | 
    DeleteStateMachineAliasInput deleteStateMachineAliasInput = new DeleteStateMachineAliasInput(); // DeleteStateMachineAliasInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteStateMachineAlias(xAmzTarget, deleteStateMachineAliasInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteStateMachineAlias");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.DeleteStateMachineAlias] |
| **deleteStateMachineAliasInput** | [**DeleteStateMachineAliasInput**](DeleteStateMachineAliasInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ValidationException |  -  |
| **481** | InvalidArn |  -  |
| **482** | ResourceNotFound |  -  |
| **483** | ConflictException |  -  |

<a id="deleteStateMachineVersion"></a>
# **deleteStateMachineVersion**
> Object deleteStateMachineVersion(xAmzTarget, deleteStateMachineVersionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt;. After you delete a version, you can&#39;t call &lt;a&gt;StartExecution&lt;/a&gt; using that version&#39;s ARN or use the version with a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Deleting a state machine version won&#39;t terminate its in-progress executions.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;You can&#39;t delete a state machine version currently referenced by one or more aliases. Before you delete a version, you must either delete the aliases or update them to point to another state machine version.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PublishStateMachineVersion&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineVersions&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.DeleteStateMachineVersion"; // String | 
    DeleteStateMachineVersionInput deleteStateMachineVersionInput = new DeleteStateMachineVersionInput(); // DeleteStateMachineVersionInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteStateMachineVersion(xAmzTarget, deleteStateMachineVersionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteStateMachineVersion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.DeleteStateMachineVersion] |
| **deleteStateMachineVersionInput** | [**DeleteStateMachineVersionInput**](DeleteStateMachineVersionInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ValidationException |  -  |
| **481** | InvalidArn |  -  |
| **482** | ConflictException |  -  |

<a id="describeActivity"></a>
# **describeActivity**
> DescribeActivityOutput describeActivity(xAmzTarget, describeActivityInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Describes an activity.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.DescribeActivity"; // String | 
    DescribeActivityInput describeActivityInput = new DescribeActivityInput(); // DescribeActivityInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeActivityOutput result = apiInstance.describeActivity(xAmzTarget, describeActivityInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeActivity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.DescribeActivity] |
| **describeActivityInput** | [**DescribeActivityInput**](DescribeActivityInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeActivityOutput**](DescribeActivityOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ActivityDoesNotExist |  -  |
| **481** | InvalidArn |  -  |

<a id="describeExecution"></a>
# **describeExecution**
> DescribeExecutionOutput describeExecution(xAmzTarget, describeExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Provides information about a state machine execution, such as the state machine associated with the execution, the execution input and output, and relevant execution metadata. Use this API action to return the Map Run Amazon Resource Name (ARN) if the execution was dispatched by a Map Run.&lt;/p&gt; &lt;p&gt;If you specify a version or alias ARN when you call the &lt;a&gt;StartExecution&lt;/a&gt; API action, &lt;code&gt;DescribeExecution&lt;/code&gt; returns that ARN.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Executions of an &lt;code&gt;EXPRESS&lt;/code&gt; state machinearen&#39;t supported by &lt;code&gt;DescribeExecution&lt;/code&gt; unless a Map Run dispatched them.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.DescribeExecution"; // String | 
    DescribeExecutionInput describeExecutionInput = new DescribeExecutionInput(); // DescribeExecutionInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeExecutionOutput result = apiInstance.describeExecution(xAmzTarget, describeExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeExecution");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.DescribeExecution] |
| **describeExecutionInput** | [**DescribeExecutionInput**](DescribeExecutionInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeExecutionOutput**](DescribeExecutionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ExecutionDoesNotExist |  -  |
| **481** | InvalidArn |  -  |

<a id="describeMapRun"></a>
# **describeMapRun**
> DescribeMapRunOutput describeMapRun(xAmzTarget, describeMapRunInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Provides information about a Map Run&#39;s configuration, progress, and results. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html\&quot;&gt;Examining Map Run&lt;/a&gt; in the &lt;i&gt;Step Functions Developer Guide&lt;/i&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.DescribeMapRun"; // String | 
    DescribeMapRunInput describeMapRunInput = new DescribeMapRunInput(); // DescribeMapRunInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeMapRunOutput result = apiInstance.describeMapRun(xAmzTarget, describeMapRunInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeMapRun");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.DescribeMapRun] |
| **describeMapRunInput** | [**DescribeMapRunInput**](DescribeMapRunInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeMapRunOutput**](DescribeMapRunOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFound |  -  |
| **481** | InvalidArn |  -  |

<a id="describeStateMachine"></a>
# **describeStateMachine**
> DescribeStateMachineOutput describeStateMachine(xAmzTarget, describeStateMachineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Provides information about a state machine&#39;s definition, its IAM role Amazon Resource Name (ARN), and configuration.&lt;/p&gt; &lt;p&gt;A qualified state machine ARN can either refer to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine, a version ARN, or an alias ARN.&lt;/p&gt; &lt;p&gt;The following are some examples of qualified and unqualified state machine ARNs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a &lt;i&gt;Distributed Map state&lt;/i&gt;, the request fails with &lt;code&gt;ValidationException&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to an alias named &lt;code&gt;PROD&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine:PROD&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following unqualified state machine ARN refers to a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This API action returns the details for a state machine version if the &lt;code&gt;stateMachineArn&lt;/code&gt; you specify is a state machine version ARN.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.DescribeStateMachine"; // String | 
    DescribeStateMachineInput describeStateMachineInput = new DescribeStateMachineInput(); // DescribeStateMachineInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeStateMachineOutput result = apiInstance.describeStateMachine(xAmzTarget, describeStateMachineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeStateMachine");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.DescribeStateMachine] |
| **describeStateMachineInput** | [**DescribeStateMachineInput**](DescribeStateMachineInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeStateMachineOutput**](DescribeStateMachineOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArn |  -  |
| **481** | StateMachineDoesNotExist |  -  |

<a id="describeStateMachineAlias"></a>
# **describeStateMachineAlias**
> DescribeStateMachineAliasOutput describeStateMachineAlias(xAmzTarget, describeStateMachineAliasInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns details about a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineAliases&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.DescribeStateMachineAlias"; // String | 
    DescribeStateMachineAliasInput describeStateMachineAliasInput = new DescribeStateMachineAliasInput(); // DescribeStateMachineAliasInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeStateMachineAliasOutput result = apiInstance.describeStateMachineAlias(xAmzTarget, describeStateMachineAliasInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeStateMachineAlias");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.DescribeStateMachineAlias] |
| **describeStateMachineAliasInput** | [**DescribeStateMachineAliasInput**](DescribeStateMachineAliasInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeStateMachineAliasOutput**](DescribeStateMachineAliasOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ValidationException |  -  |
| **481** | InvalidArn |  -  |
| **482** | ResourceNotFound |  -  |

<a id="describeStateMachineForExecution"></a>
# **describeStateMachineForExecution**
> DescribeStateMachineForExecutionOutput describeStateMachineForExecution(xAmzTarget, describeStateMachineForExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Provides information about a state machine&#39;s definition, its execution role ARN, and configuration. If a Map Run dispatched the execution, this action returns the Map Run Amazon Resource Name (ARN) in the response. The state machine returned is the state machine associated with the Map Run.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This API action is not supported by &lt;code&gt;EXPRESS&lt;/code&gt; state machines.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.DescribeStateMachineForExecution"; // String | 
    DescribeStateMachineForExecutionInput describeStateMachineForExecutionInput = new DescribeStateMachineForExecutionInput(); // DescribeStateMachineForExecutionInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeStateMachineForExecutionOutput result = apiInstance.describeStateMachineForExecution(xAmzTarget, describeStateMachineForExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeStateMachineForExecution");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.DescribeStateMachineForExecution] |
| **describeStateMachineForExecutionInput** | [**DescribeStateMachineForExecutionInput**](DescribeStateMachineForExecutionInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeStateMachineForExecutionOutput**](DescribeStateMachineForExecutionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ExecutionDoesNotExist |  -  |
| **481** | InvalidArn |  -  |

<a id="getActivityTask"></a>
# **getActivityTask**
> GetActivityTaskOutput getActivityTask(xAmzTarget, getActivityTaskInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Used by workers to retrieve a task (with the specified activity ARN) which has been scheduled for execution by a running state machine. This initiates a long poll, where the service holds the HTTP connection open and responds as soon as a task becomes available (i.e. an execution of a task of this type is needed.) The maximum time the service holds on to the request before responding is 60 seconds. If no task is available within 60 seconds, the poll returns a &lt;code&gt;taskToken&lt;/code&gt; with a null string.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API action isn&#39;t logged in CloudTrail.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;Workers should set their client side socket timeout to at least 65 seconds (5 seconds higher than the maximum time the service may hold the poll request).&lt;/p&gt; &lt;p&gt;Polling with &lt;code&gt;GetActivityTask&lt;/code&gt; can cause latency in some implementations. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/bp-activity-pollers.html\&quot;&gt;Avoid Latency When Polling for Activity Tasks&lt;/a&gt; in the Step Functions Developer Guide.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.GetActivityTask"; // String | 
    GetActivityTaskInput getActivityTaskInput = new GetActivityTaskInput(); // GetActivityTaskInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetActivityTaskOutput result = apiInstance.getActivityTask(xAmzTarget, getActivityTaskInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getActivityTask");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.GetActivityTask] |
| **getActivityTaskInput** | [**GetActivityTaskInput**](GetActivityTaskInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetActivityTaskOutput**](GetActivityTaskOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ActivityDoesNotExist |  -  |
| **481** | ActivityWorkerLimitExceeded |  -  |
| **482** | InvalidArn |  -  |

<a id="getExecutionHistory"></a>
# **getExecutionHistory**
> GetExecutionHistoryOutput getExecutionHistory(xAmzTarget, getExecutionHistoryInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Returns the history of the specified execution as a list of events. By default, the results are returned in ascending order of the &lt;code&gt;timeStamp&lt;/code&gt; of the events. Use the &lt;code&gt;reverseOrder&lt;/code&gt; parameter to get the latest events first.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;p&gt;This API action is not supported by &lt;code&gt;EXPRESS&lt;/code&gt; state machines.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.GetExecutionHistory"; // String | 
    GetExecutionHistoryInput getExecutionHistoryInput = new GetExecutionHistoryInput(); // GetExecutionHistoryInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      GetExecutionHistoryOutput result = apiInstance.getExecutionHistory(xAmzTarget, getExecutionHistoryInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getExecutionHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.GetExecutionHistory] |
| **getExecutionHistoryInput** | [**GetExecutionHistoryInput**](GetExecutionHistoryInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**GetExecutionHistoryOutput**](GetExecutionHistoryOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ExecutionDoesNotExist |  -  |
| **481** | InvalidArn |  -  |
| **482** | InvalidToken |  -  |

<a id="listActivities"></a>
# **listActivities**
> ListActivitiesOutput listActivities(xAmzTarget, listActivitiesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Lists the existing activities.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.ListActivities"; // String | 
    ListActivitiesInput listActivitiesInput = new ListActivitiesInput(); // ListActivitiesInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListActivitiesOutput result = apiInstance.listActivities(xAmzTarget, listActivitiesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listActivities");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.ListActivities] |
| **listActivitiesInput** | [**ListActivitiesInput**](ListActivitiesInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListActivitiesOutput**](ListActivitiesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidToken |  -  |

<a id="listExecutions"></a>
# **listExecutions**
> ListExecutionsOutput listExecutions(xAmzTarget, listExecutionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Lists all executions of a state machine or a Map Run. You can list all executions related to a state machine by specifying a state machine Amazon Resource Name (ARN), or those related to a Map Run by specifying a Map Run ARN.&lt;/p&gt; &lt;p&gt;You can also provide a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt; ARN or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt; ARN to list the executions associated with a specific alias or version.&lt;/p&gt; &lt;p&gt;Results are sorted by time, with the most recent execution first.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This API action is not supported by &lt;code&gt;EXPRESS&lt;/code&gt; state machines.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.ListExecutions"; // String | 
    ListExecutionsInput listExecutionsInput = new ListExecutionsInput(); // ListExecutionsInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListExecutionsOutput result = apiInstance.listExecutions(xAmzTarget, listExecutionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listExecutions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.ListExecutions] |
| **listExecutionsInput** | [**ListExecutionsInput**](ListExecutionsInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListExecutionsOutput**](ListExecutionsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArn |  -  |
| **481** | InvalidToken |  -  |
| **482** | StateMachineDoesNotExist |  -  |
| **483** | StateMachineTypeNotSupported |  -  |
| **484** | ValidationException |  -  |
| **485** | ResourceNotFound |  -  |

<a id="listMapRuns"></a>
# **listMapRuns**
> ListMapRunsOutput listMapRuns(xAmzTarget, listMapRunsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Lists all Map Runs that were started by a given state machine execution. Use this API action to obtain Map Run ARNs, and then call &lt;code&gt;DescribeMapRun&lt;/code&gt; to obtain more information, if needed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.ListMapRuns"; // String | 
    ListMapRunsInput listMapRunsInput = new ListMapRunsInput(); // ListMapRunsInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListMapRunsOutput result = apiInstance.listMapRuns(xAmzTarget, listMapRunsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listMapRuns");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.ListMapRuns] |
| **listMapRunsInput** | [**ListMapRunsInput**](ListMapRunsInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListMapRunsOutput**](ListMapRunsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ExecutionDoesNotExist |  -  |
| **481** | InvalidArn |  -  |
| **482** | InvalidToken |  -  |

<a id="listStateMachineAliases"></a>
# **listStateMachineAliases**
> ListStateMachineAliasesOutput listStateMachineAliases(xAmzTarget, listStateMachineAliasesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Lists &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;aliases&lt;/a&gt; for a specified state machine ARN. Results are sorted by time, with the most recently created aliases listed first. &lt;/p&gt; &lt;p&gt;To list aliases that reference a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt;, you can specify the version ARN in the &lt;code&gt;stateMachineArn&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.ListStateMachineAliases"; // String | 
    ListStateMachineAliasesInput listStateMachineAliasesInput = new ListStateMachineAliasesInput(); // ListStateMachineAliasesInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListStateMachineAliasesOutput result = apiInstance.listStateMachineAliases(xAmzTarget, listStateMachineAliasesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listStateMachineAliases");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.ListStateMachineAliases] |
| **listStateMachineAliasesInput** | [**ListStateMachineAliasesInput**](ListStateMachineAliasesInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListStateMachineAliasesOutput**](ListStateMachineAliasesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArn |  -  |
| **481** | InvalidToken |  -  |
| **482** | ResourceNotFound |  -  |
| **483** | StateMachineDoesNotExist |  -  |
| **484** | StateMachineDeleting |  -  |

<a id="listStateMachineVersions"></a>
# **listStateMachineVersions**
> ListStateMachineVersionsOutput listStateMachineVersions(xAmzTarget, listStateMachineVersionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Lists &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;versions&lt;/a&gt; for the specified state machine Amazon Resource Name (ARN).&lt;/p&gt; &lt;p&gt;The results are sorted in descending order of the version creation time.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PublishStateMachineVersion&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineVersion&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.ListStateMachineVersions"; // String | 
    ListStateMachineVersionsInput listStateMachineVersionsInput = new ListStateMachineVersionsInput(); // ListStateMachineVersionsInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListStateMachineVersionsOutput result = apiInstance.listStateMachineVersions(xAmzTarget, listStateMachineVersionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listStateMachineVersions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.ListStateMachineVersions] |
| **listStateMachineVersionsInput** | [**ListStateMachineVersionsInput**](ListStateMachineVersionsInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListStateMachineVersionsOutput**](ListStateMachineVersionsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ValidationException |  -  |
| **481** | InvalidArn |  -  |
| **482** | InvalidToken |  -  |

<a id="listStateMachines"></a>
# **listStateMachines**
> ListStateMachinesOutput listStateMachines(xAmzTarget, listStateMachinesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Lists the existing state machines.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.ListStateMachines"; // String | 
    ListStateMachinesInput listStateMachinesInput = new ListStateMachinesInput(); // ListStateMachinesInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListStateMachinesOutput result = apiInstance.listStateMachines(xAmzTarget, listStateMachinesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listStateMachines");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.ListStateMachines] |
| **listStateMachinesInput** | [**ListStateMachinesInput**](ListStateMachinesInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListStateMachinesOutput**](ListStateMachinesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidToken |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceOutput listTagsForResource(xAmzTarget, listTagsForResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;List tags for a given resource.&lt;/p&gt; &lt;p&gt;Tags may only contain Unicode letters, digits, white space, or these symbols: &lt;code&gt;_ . : / &#x3D; + - @&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.ListTagsForResource"; // String | 
    ListTagsForResourceInput listTagsForResourceInput = new ListTagsForResourceInput(); // ListTagsForResourceInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceOutput result = apiInstance.listTagsForResource(xAmzTarget, listTagsForResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForResource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.ListTagsForResource] |
| **listTagsForResourceInput** | [**ListTagsForResourceInput**](ListTagsForResourceInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListTagsForResourceOutput**](ListTagsForResourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArn |  -  |
| **481** | ResourceNotFound |  -  |

<a id="publishStateMachineVersion"></a>
# **publishStateMachineVersion**
> PublishStateMachineVersionOutput publishStateMachineVersion(xAmzTarget, publishStateMachineVersionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt; from the current revision of a state machine. Use versions to create immutable snapshots of your state machine. You can start executions from versions either directly or with an alias. To create an alias, use &lt;a&gt;CreateStateMachineAlias&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can publish up to 1000 versions for each state machine. You must manually delete unused versions using the &lt;a&gt;DeleteStateMachineVersion&lt;/a&gt; API action.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PublishStateMachineVersion&lt;/code&gt; is an idempotent API. It doesn&#39;t create a duplicate state machine version if it already exists for the current revision. Step Functions bases &lt;code&gt;PublishStateMachineVersion&lt;/code&gt;&#39;s idempotency check on the &lt;code&gt;stateMachineArn&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, and &lt;code&gt;revisionId&lt;/code&gt; parameters. Requests with the same parameters return a successful idempotent response. If you don&#39;t specify a &lt;code&gt;revisionId&lt;/code&gt;, Step Functions checks for a previously published version of the state machine&#39;s current revision.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineVersion&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineVersions&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.PublishStateMachineVersion"; // String | 
    PublishStateMachineVersionInput publishStateMachineVersionInput = new PublishStateMachineVersionInput(); // PublishStateMachineVersionInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PublishStateMachineVersionOutput result = apiInstance.publishStateMachineVersion(xAmzTarget, publishStateMachineVersionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publishStateMachineVersion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.PublishStateMachineVersion] |
| **publishStateMachineVersionInput** | [**PublishStateMachineVersionInput**](PublishStateMachineVersionInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PublishStateMachineVersionOutput**](PublishStateMachineVersionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ValidationException |  -  |
| **481** | StateMachineDeleting |  -  |
| **482** | StateMachineDoesNotExist |  -  |
| **483** | ServiceQuotaExceededException |  -  |
| **484** | ConflictException |  -  |
| **485** | InvalidArn |  -  |

<a id="sendTaskFailure"></a>
# **sendTaskFailure**
> Object sendTaskFailure(xAmzTarget, sendTaskFailureInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Used by activity workers and task states using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token\&quot;&gt;callback&lt;/a&gt; pattern to report that the task identified by the &lt;code&gt;taskToken&lt;/code&gt; failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.SendTaskFailure"; // String | 
    SendTaskFailureInput sendTaskFailureInput = new SendTaskFailureInput(); // SendTaskFailureInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.sendTaskFailure(xAmzTarget, sendTaskFailureInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendTaskFailure");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.SendTaskFailure] |
| **sendTaskFailureInput** | [**SendTaskFailureInput**](SendTaskFailureInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | TaskDoesNotExist |  -  |
| **481** | InvalidToken |  -  |
| **482** | TaskTimedOut |  -  |

<a id="sendTaskHeartbeat"></a>
# **sendTaskHeartbeat**
> Object sendTaskHeartbeat(xAmzTarget, sendTaskHeartbeatInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Used by activity workers and task states using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token\&quot;&gt;callback&lt;/a&gt; pattern to report to Step Functions that the task represented by the specified &lt;code&gt;taskToken&lt;/code&gt; is still making progress. This action resets the &lt;code&gt;Heartbeat&lt;/code&gt; clock. The &lt;code&gt;Heartbeat&lt;/code&gt; threshold is specified in the state machine&#39;s Amazon States Language definition (&lt;code&gt;HeartbeatSeconds&lt;/code&gt;). This action does not in itself create an event in the execution history. However, if the task times out, the execution history contains an &lt;code&gt;ActivityTimedOut&lt;/code&gt; entry for activities, or a &lt;code&gt;TaskTimedOut&lt;/code&gt; entry for for tasks using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-sync\&quot;&gt;job run&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token\&quot;&gt;callback&lt;/a&gt; pattern.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;Timeout&lt;/code&gt; of a task, defined in the state machine&#39;s Amazon States Language definition, is its maximum allowed duration, regardless of the number of &lt;a&gt;SendTaskHeartbeat&lt;/a&gt; requests received. Use &lt;code&gt;HeartbeatSeconds&lt;/code&gt; to configure the timeout interval for heartbeats.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.SendTaskHeartbeat"; // String | 
    SendTaskHeartbeatInput sendTaskHeartbeatInput = new SendTaskHeartbeatInput(); // SendTaskHeartbeatInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.sendTaskHeartbeat(xAmzTarget, sendTaskHeartbeatInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendTaskHeartbeat");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.SendTaskHeartbeat] |
| **sendTaskHeartbeatInput** | [**SendTaskHeartbeatInput**](SendTaskHeartbeatInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | TaskDoesNotExist |  -  |
| **481** | InvalidToken |  -  |
| **482** | TaskTimedOut |  -  |

<a id="sendTaskSuccess"></a>
# **sendTaskSuccess**
> Object sendTaskSuccess(xAmzTarget, sendTaskSuccessInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Used by activity workers and task states using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token\&quot;&gt;callback&lt;/a&gt; pattern to report that the task identified by the &lt;code&gt;taskToken&lt;/code&gt; completed successfully.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.SendTaskSuccess"; // String | 
    SendTaskSuccessInput sendTaskSuccessInput = new SendTaskSuccessInput(); // SendTaskSuccessInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.sendTaskSuccess(xAmzTarget, sendTaskSuccessInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendTaskSuccess");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.SendTaskSuccess] |
| **sendTaskSuccessInput** | [**SendTaskSuccessInput**](SendTaskSuccessInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | TaskDoesNotExist |  -  |
| **481** | InvalidOutput |  -  |
| **482** | InvalidToken |  -  |
| **483** | TaskTimedOut |  -  |

<a id="startExecution"></a>
# **startExecution**
> StartExecutionOutput startExecution(xAmzTarget, startExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Starts a state machine execution.&lt;/p&gt; &lt;p&gt;A qualified state machine ARN can either refer to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine, a version ARN, or an alias ARN.&lt;/p&gt; &lt;p&gt;The following are some examples of qualified and unqualified state machine ARNs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a &lt;i&gt;Distributed Map state&lt;/i&gt;, the request fails with &lt;code&gt;ValidationException&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to an alias named &lt;code&gt;PROD&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine:PROD&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following unqualified state machine ARN refers to a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you start an execution with an unqualified state machine ARN, Step Functions uses the latest revision of the state machine for the execution.&lt;/p&gt; &lt;p&gt;To start executions of a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt;, call &lt;code&gt;StartExecution&lt;/code&gt; and provide the version ARN or the ARN of an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt; that points to the version.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;StartExecution&lt;/code&gt; is idempotent for &lt;code&gt;STANDARD&lt;/code&gt; workflows. For a &lt;code&gt;STANDARD&lt;/code&gt; workflow, if you call &lt;code&gt;StartExecution&lt;/code&gt; with the same name and input as a running execution, the call succeeds and return the same response as the original request. If the execution is closed or if the input is different, it returns a &lt;code&gt;400 ExecutionAlreadyExists&lt;/code&gt; error. You can reuse names after 90 days. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartExecution&lt;/code&gt; isn&#39;t idempotent for &lt;code&gt;EXPRESS&lt;/code&gt; workflows. &lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.StartExecution"; // String | 
    StartExecutionInput startExecutionInput = new StartExecutionInput(); // StartExecutionInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartExecutionOutput result = apiInstance.startExecution(xAmzTarget, startExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startExecution");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.StartExecution] |
| **startExecutionInput** | [**StartExecutionInput**](StartExecutionInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartExecutionOutput**](StartExecutionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ExecutionLimitExceeded |  -  |
| **481** | ExecutionAlreadyExists |  -  |
| **482** | InvalidArn |  -  |
| **483** | InvalidExecutionInput |  -  |
| **484** | InvalidName |  -  |
| **485** | StateMachineDoesNotExist |  -  |
| **486** | StateMachineDeleting |  -  |
| **487** | ValidationException |  -  |

<a id="startSyncExecution"></a>
# **startSyncExecution**
> StartSyncExecutionOutput startSyncExecution(xAmzTarget, startSyncExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Starts a Synchronous Express state machine execution. &lt;code&gt;StartSyncExecution&lt;/code&gt; is not available for &lt;code&gt;STANDARD&lt;/code&gt; workflows.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;StartSyncExecution&lt;/code&gt; will return a &lt;code&gt;200 OK&lt;/code&gt; response, even if your execution fails, because the status code in the API response doesn&#39;t reflect function errors. Error codes are reserved for errors that prevent your execution from running, such as permissions errors, limit errors, or issues with your state machine code and configuration. &lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;This API action isn&#39;t logged in CloudTrail.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.StartSyncExecution"; // String | 
    StartSyncExecutionInput startSyncExecutionInput = new StartSyncExecutionInput(); // StartSyncExecutionInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartSyncExecutionOutput result = apiInstance.startSyncExecution(xAmzTarget, startSyncExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startSyncExecution");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.StartSyncExecution] |
| **startSyncExecutionInput** | [**StartSyncExecutionInput**](StartSyncExecutionInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartSyncExecutionOutput**](StartSyncExecutionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArn |  -  |
| **481** | InvalidExecutionInput |  -  |
| **482** | InvalidName |  -  |
| **483** | StateMachineDoesNotExist |  -  |
| **484** | StateMachineDeleting |  -  |
| **485** | StateMachineTypeNotSupported |  -  |

<a id="stopExecution"></a>
# **stopExecution**
> StopExecutionOutput stopExecution(xAmzTarget, stopExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Stops an execution.&lt;/p&gt; &lt;p&gt;This API action is not supported by &lt;code&gt;EXPRESS&lt;/code&gt; state machines.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.StopExecution"; // String | 
    StopExecutionInput stopExecutionInput = new StopExecutionInput(); // StopExecutionInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StopExecutionOutput result = apiInstance.stopExecution(xAmzTarget, stopExecutionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stopExecution");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.StopExecution] |
| **stopExecutionInput** | [**StopExecutionInput**](StopExecutionInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StopExecutionOutput**](StopExecutionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ExecutionDoesNotExist |  -  |
| **481** | InvalidArn |  -  |
| **482** | ValidationException |  -  |

<a id="tagResource"></a>
# **tagResource**
> Object tagResource(xAmzTarget, tagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Add a tag to a Step Functions resource.&lt;/p&gt; &lt;p&gt;An array of key-value pairs. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Billing and Cost Management User Guide&lt;/i&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html\&quot;&gt;Controlling Access Using IAM Tags&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Tags may only contain Unicode letters, digits, white space, or these symbols: &lt;code&gt;_ . : / &#x3D; + - @&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.TagResource"; // String | 
    TagResourceInput tagResourceInput = new TagResourceInput(); // TagResourceInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.tagResource(xAmzTarget, tagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagResource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.TagResource] |
| **tagResourceInput** | [**TagResourceInput**](TagResourceInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArn |  -  |
| **481** | ResourceNotFound |  -  |
| **482** | TooManyTags |  -  |

<a id="untagResource"></a>
# **untagResource**
> Object untagResource(xAmzTarget, untagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Remove a tag from a Step Functions resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.UntagResource"; // String | 
    UntagResourceInput untagResourceInput = new UntagResourceInput(); // UntagResourceInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.untagResource(xAmzTarget, untagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagResource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.UntagResource] |
| **untagResourceInput** | [**UntagResourceInput**](UntagResourceInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArn |  -  |
| **481** | ResourceNotFound |  -  |

<a id="updateMapRun"></a>
# **updateMapRun**
> Object updateMapRun(xAmzTarget, updateMapRunInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates an in-progress Map Run&#39;s configuration to include changes to the settings that control maximum concurrency and Map Run failure.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.UpdateMapRun"; // String | 
    UpdateMapRunInput updateMapRunInput = new UpdateMapRunInput(); // UpdateMapRunInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.updateMapRun(xAmzTarget, updateMapRunInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateMapRun");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.UpdateMapRun] |
| **updateMapRunInput** | [**UpdateMapRunInput**](UpdateMapRunInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFound |  -  |
| **481** | InvalidArn |  -  |
| **482** | ValidationException |  -  |

<a id="updateStateMachine"></a>
# **updateStateMachine**
> UpdateStateMachineOutput updateStateMachine(xAmzTarget, updateStateMachineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates an existing state machine by modifying its &lt;code&gt;definition&lt;/code&gt;, &lt;code&gt;roleArn&lt;/code&gt;, or &lt;code&gt;loggingConfiguration&lt;/code&gt;. Running executions will continue to use the previous &lt;code&gt;definition&lt;/code&gt; and &lt;code&gt;roleArn&lt;/code&gt;. You must include at least one of &lt;code&gt;definition&lt;/code&gt; or &lt;code&gt;roleArn&lt;/code&gt; or you will receive a &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;A qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine. For example, the qualified state machine ARN &lt;code&gt;arn:partition:states:region:account-id:stateMachine:stateMachineName/mapStateLabel&lt;/code&gt; refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in the state machine named &lt;code&gt;stateMachineName&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;A qualified state machine ARN can either refer to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine, a version ARN, or an alias ARN.&lt;/p&gt; &lt;p&gt;The following are some examples of qualified and unqualified state machine ARNs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a &lt;i&gt;Distributed Map state&lt;/i&gt;, the request fails with &lt;code&gt;ValidationException&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to an alias named &lt;code&gt;PROD&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine:PROD&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following unqualified state machine ARN refers to a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;After you update your state machine, you can set the &lt;code&gt;publish&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt; in the same action to publish a new &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt;. This way, you can opt-in to strict versioning of your state machine.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Step Functions assigns monotonically increasing integers for state machine versions, starting at version number 1.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;All &lt;code&gt;StartExecution&lt;/code&gt; calls within a few seconds use the updated &lt;code&gt;definition&lt;/code&gt; and &lt;code&gt;roleArn&lt;/code&gt;. Executions started immediately after you call &lt;code&gt;UpdateStateMachine&lt;/code&gt; may use the previous state machine &lt;code&gt;definition&lt;/code&gt; and &lt;code&gt;roleArn&lt;/code&gt;. &lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.UpdateStateMachine"; // String | 
    UpdateStateMachineInput updateStateMachineInput = new UpdateStateMachineInput(); // UpdateStateMachineInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateStateMachineOutput result = apiInstance.updateStateMachine(xAmzTarget, updateStateMachineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateStateMachine");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.UpdateStateMachine] |
| **updateStateMachineInput** | [**UpdateStateMachineInput**](UpdateStateMachineInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateStateMachineOutput**](UpdateStateMachineOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArn |  -  |
| **481** | InvalidDefinition |  -  |
| **482** | InvalidLoggingConfiguration |  -  |
| **483** | InvalidTracingConfiguration |  -  |
| **484** | MissingRequiredParameter |  -  |
| **485** | StateMachineDeleting |  -  |
| **486** | StateMachineDoesNotExist |  -  |
| **487** | ServiceQuotaExceededException |  -  |
| **488** | ConflictException |  -  |
| **489** | ValidationException |  -  |

<a id="updateStateMachineAlias"></a>
# **updateStateMachineAlias**
> UpdateStateMachineAliasOutput updateStateMachineAlias(xAmzTarget, updateStateMachineAliasInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates the configuration of an existing state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt; by modifying its &lt;code&gt;description&lt;/code&gt; or &lt;code&gt;routingConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You must specify at least one of the &lt;code&gt;description&lt;/code&gt; or &lt;code&gt;routingConfiguration&lt;/code&gt; parameters to update a state machine alias.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;UpdateStateMachineAlias&lt;/code&gt; is an idempotent API. Step Functions bases the idempotency check on the &lt;code&gt;stateMachineAliasArn&lt;/code&gt;, &lt;code&gt;description&lt;/code&gt;, and &lt;code&gt;routingConfiguration&lt;/code&gt; parameters. Requests with the same parameters return an idempotent response.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. All &lt;a&gt;StartExecution&lt;/a&gt; requests made within a few seconds use the latest alias configuration. Executions started immediately after calling &lt;code&gt;UpdateStateMachineAlias&lt;/code&gt; may use the previous routing configuration.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineAliases&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://states.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSStepFunctions.UpdateStateMachineAlias"; // String | 
    UpdateStateMachineAliasInput updateStateMachineAliasInput = new UpdateStateMachineAliasInput(); // UpdateStateMachineAliasInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateStateMachineAliasOutput result = apiInstance.updateStateMachineAlias(xAmzTarget, updateStateMachineAliasInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateStateMachineAlias");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSStepFunctions.UpdateStateMachineAlias] |
| **updateStateMachineAliasInput** | [**UpdateStateMachineAliasInput**](UpdateStateMachineAliasInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateStateMachineAliasOutput**](UpdateStateMachineAliasOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ValidationException |  -  |
| **481** | InvalidArn |  -  |
| **482** | ResourceNotFound |  -  |
| **483** | ConflictException |  -  |

