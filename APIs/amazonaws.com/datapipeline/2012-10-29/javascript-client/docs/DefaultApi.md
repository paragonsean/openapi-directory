# AwsDataPipeline.DefaultApi

All URIs are relative to *http://datapipeline.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activatePipeline**](DefaultApi.md#activatePipeline) | **POST** /#X-Amz-Target&#x3D;DataPipeline.ActivatePipeline | 
[**addTags**](DefaultApi.md#addTags) | **POST** /#X-Amz-Target&#x3D;DataPipeline.AddTags | 
[**createPipeline**](DefaultApi.md#createPipeline) | **POST** /#X-Amz-Target&#x3D;DataPipeline.CreatePipeline | 
[**deactivatePipeline**](DefaultApi.md#deactivatePipeline) | **POST** /#X-Amz-Target&#x3D;DataPipeline.DeactivatePipeline | 
[**deletePipeline**](DefaultApi.md#deletePipeline) | **POST** /#X-Amz-Target&#x3D;DataPipeline.DeletePipeline | 
[**describeObjects**](DefaultApi.md#describeObjects) | **POST** /#X-Amz-Target&#x3D;DataPipeline.DescribeObjects | 
[**describePipelines**](DefaultApi.md#describePipelines) | **POST** /#X-Amz-Target&#x3D;DataPipeline.DescribePipelines | 
[**evaluateExpression**](DefaultApi.md#evaluateExpression) | **POST** /#X-Amz-Target&#x3D;DataPipeline.EvaluateExpression | 
[**getPipelineDefinition**](DefaultApi.md#getPipelineDefinition) | **POST** /#X-Amz-Target&#x3D;DataPipeline.GetPipelineDefinition | 
[**listPipelines**](DefaultApi.md#listPipelines) | **POST** /#X-Amz-Target&#x3D;DataPipeline.ListPipelines | 
[**pollForTask**](DefaultApi.md#pollForTask) | **POST** /#X-Amz-Target&#x3D;DataPipeline.PollForTask | 
[**putPipelineDefinition**](DefaultApi.md#putPipelineDefinition) | **POST** /#X-Amz-Target&#x3D;DataPipeline.PutPipelineDefinition | 
[**queryObjects**](DefaultApi.md#queryObjects) | **POST** /#X-Amz-Target&#x3D;DataPipeline.QueryObjects | 
[**removeTags**](DefaultApi.md#removeTags) | **POST** /#X-Amz-Target&#x3D;DataPipeline.RemoveTags | 
[**reportTaskProgress**](DefaultApi.md#reportTaskProgress) | **POST** /#X-Amz-Target&#x3D;DataPipeline.ReportTaskProgress | 
[**reportTaskRunnerHeartbeat**](DefaultApi.md#reportTaskRunnerHeartbeat) | **POST** /#X-Amz-Target&#x3D;DataPipeline.ReportTaskRunnerHeartbeat | 
[**setStatus**](DefaultApi.md#setStatus) | **POST** /#X-Amz-Target&#x3D;DataPipeline.SetStatus | 
[**setTaskStatus**](DefaultApi.md#setTaskStatus) | **POST** /#X-Amz-Target&#x3D;DataPipeline.SetTaskStatus | 
[**validatePipelineDefinition**](DefaultApi.md#validatePipelineDefinition) | **POST** /#X-Amz-Target&#x3D;DataPipeline.ValidatePipelineDefinition | 



## activatePipeline

> Object activatePipeline(xAmzTarget, activatePipelineInput, opts)



&lt;p&gt;Validates the specified pipeline and starts processing pipeline tasks. If the pipeline does not pass validation, activation fails.&lt;/p&gt; &lt;p&gt;If you need to pause the pipeline to investigate an issue with a component, such as a data source or script, call &lt;a&gt;DeactivatePipeline&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To activate a finished pipeline, modify the end date for the pipeline and then activate it.&lt;/p&gt;

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let activatePipelineInput = new AwsDataPipeline.ActivatePipelineInput(); // ActivatePipelineInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.activatePipeline(xAmzTarget, activatePipelineInput, opts, (error, data, response) => {
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
 **activatePipelineInput** | [**ActivatePipelineInput**](ActivatePipelineInput.md)|  | 
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


## addTags

> Object addTags(xAmzTarget, addTagsInput, opts)



Adds or modifies tags for the specified pipeline.

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let addTagsInput = new AwsDataPipeline.AddTagsInput(); // AddTagsInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addTags(xAmzTarget, addTagsInput, opts, (error, data, response) => {
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
 **addTagsInput** | [**AddTagsInput**](AddTagsInput.md)|  | 
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


## createPipeline

> CreatePipelineOutput createPipeline(xAmzTarget, createPipelineInput, opts)



Creates a new, empty pipeline. Use &lt;a&gt;PutPipelineDefinition&lt;/a&gt; to populate the pipeline.

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createPipelineInput = new AwsDataPipeline.CreatePipelineInput(); // CreatePipelineInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPipeline(xAmzTarget, createPipelineInput, opts, (error, data, response) => {
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
 **createPipelineInput** | [**CreatePipelineInput**](CreatePipelineInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePipelineOutput**](CreatePipelineOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deactivatePipeline

> Object deactivatePipeline(xAmzTarget, deactivatePipelineInput, opts)



&lt;p&gt;Deactivates the specified running pipeline. The pipeline is set to the &lt;code&gt;DEACTIVATING&lt;/code&gt; state until the deactivation process completes.&lt;/p&gt; &lt;p&gt;To resume a deactivated pipeline, use &lt;a&gt;ActivatePipeline&lt;/a&gt;. By default, the pipeline resumes from the last completed execution. Optionally, you can specify the date and time to resume the pipeline.&lt;/p&gt;

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deactivatePipelineInput = new AwsDataPipeline.DeactivatePipelineInput(); // DeactivatePipelineInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deactivatePipeline(xAmzTarget, deactivatePipelineInput, opts, (error, data, response) => {
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
 **deactivatePipelineInput** | [**DeactivatePipelineInput**](DeactivatePipelineInput.md)|  | 
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


## deletePipeline

> deletePipeline(xAmzTarget, deletePipelineInput, opts)



&lt;p&gt;Deletes a pipeline, its pipeline definition, and its run history. AWS Data Pipeline attempts to cancel instances associated with the pipeline that are currently being processed by task runners.&lt;/p&gt; &lt;p&gt;Deleting a pipeline cannot be undone. You cannot query or restore a deleted pipeline. To temporarily pause a pipeline instead of deleting it, call &lt;a&gt;SetStatus&lt;/a&gt; with the status set to &lt;code&gt;PAUSE&lt;/code&gt; on individual components. Components that are paused by &lt;a&gt;SetStatus&lt;/a&gt; can be resumed.&lt;/p&gt;

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deletePipelineInput = new AwsDataPipeline.DeletePipelineInput(); // DeletePipelineInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deletePipeline(xAmzTarget, deletePipelineInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **deletePipelineInput** | [**DeletePipelineInput**](DeletePipelineInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeObjects

> DescribeObjectsOutput describeObjects(xAmzTarget, describeObjectsInput, opts)



Gets the object definitions for a set of objects associated with the pipeline. Object definitions are composed of a set of fields that define the properties of the object.

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeObjectsInput = new AwsDataPipeline.DescribeObjectsInput(); // DescribeObjectsInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example" // String | Pagination token
};
apiInstance.describeObjects(xAmzTarget, describeObjectsInput, opts, (error, data, response) => {
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
 **describeObjectsInput** | [**DescribeObjectsInput**](DescribeObjectsInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **marker** | **String**| Pagination token | [optional] 

### Return type

[**DescribeObjectsOutput**](DescribeObjectsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describePipelines

> DescribePipelinesOutput describePipelines(xAmzTarget, describePipelinesInput, opts)



&lt;p&gt;Retrieves metadata about one or more pipelines. The information retrieved includes the name of the pipeline, the pipeline identifier, its current state, and the user account that owns the pipeline. Using account credentials, you can retrieve metadata about pipelines that you or your IAM users have created. If you are using an IAM user account, you can retrieve metadata about only those pipelines for which you have read permissions.&lt;/p&gt; &lt;p&gt;To retrieve the full pipeline definition instead of metadata about the pipeline, call &lt;a&gt;GetPipelineDefinition&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describePipelinesInput = new AwsDataPipeline.DescribePipelinesInput(); // DescribePipelinesInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describePipelines(xAmzTarget, describePipelinesInput, opts, (error, data, response) => {
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
 **describePipelinesInput** | [**DescribePipelinesInput**](DescribePipelinesInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribePipelinesOutput**](DescribePipelinesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## evaluateExpression

> EvaluateExpressionOutput evaluateExpression(xAmzTarget, evaluateExpressionInput, opts)



Task runners call &lt;code&gt;EvaluateExpression&lt;/code&gt; to evaluate a string in the context of the specified object. For example, a task runner can evaluate SQL queries stored in Amazon S3.

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let evaluateExpressionInput = new AwsDataPipeline.EvaluateExpressionInput(); // EvaluateExpressionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.evaluateExpression(xAmzTarget, evaluateExpressionInput, opts, (error, data, response) => {
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
 **evaluateExpressionInput** | [**EvaluateExpressionInput**](EvaluateExpressionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**EvaluateExpressionOutput**](EvaluateExpressionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getPipelineDefinition

> GetPipelineDefinitionOutput getPipelineDefinition(xAmzTarget, getPipelineDefinitionInput, opts)



Gets the definition of the specified pipeline. You can call &lt;code&gt;GetPipelineDefinition&lt;/code&gt; to retrieve the pipeline definition that you provided using &lt;a&gt;PutPipelineDefinition&lt;/a&gt;.

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getPipelineDefinitionInput = new AwsDataPipeline.GetPipelineDefinitionInput(); // GetPipelineDefinitionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPipelineDefinition(xAmzTarget, getPipelineDefinitionInput, opts, (error, data, response) => {
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
 **getPipelineDefinitionInput** | [**GetPipelineDefinitionInput**](GetPipelineDefinitionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPipelineDefinitionOutput**](GetPipelineDefinitionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPipelines

> ListPipelinesOutput listPipelines(xAmzTarget, listPipelinesInput, opts)



Lists the pipeline identifiers for all active pipelines that you have permission to access.

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listPipelinesInput = new AwsDataPipeline.ListPipelinesInput(); // ListPipelinesInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example" // String | Pagination token
};
apiInstance.listPipelines(xAmzTarget, listPipelinesInput, opts, (error, data, response) => {
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
 **listPipelinesInput** | [**ListPipelinesInput**](ListPipelinesInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **marker** | **String**| Pagination token | [optional] 

### Return type

[**ListPipelinesOutput**](ListPipelinesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pollForTask

> PollForTaskOutput pollForTask(xAmzTarget, pollForTaskInput, opts)



&lt;p&gt;Task runners call &lt;code&gt;PollForTask&lt;/code&gt; to receive a task to perform from AWS Data Pipeline. The task runner specifies which tasks it can perform by setting a value for the &lt;code&gt;workerGroup&lt;/code&gt; parameter. The task returned can come from any of the pipelines that match the &lt;code&gt;workerGroup&lt;/code&gt; value passed in by the task runner and that was launched using the IAM user credentials specified by the task runner.&lt;/p&gt; &lt;p&gt;If tasks are ready in the work queue, &lt;code&gt;PollForTask&lt;/code&gt; returns a response immediately. If no tasks are available in the queue, &lt;code&gt;PollForTask&lt;/code&gt; uses long-polling and holds on to a poll connection for up to a 90 seconds, during which time the first newly scheduled task is handed to the task runner. To accomodate this, set the socket timeout in your task runner to 90 seconds. The task runner should not call &lt;code&gt;PollForTask&lt;/code&gt; again on the same &lt;code&gt;workerGroup&lt;/code&gt; until it receives a response, and this can take up to 90 seconds. &lt;/p&gt;

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let pollForTaskInput = new AwsDataPipeline.PollForTaskInput(); // PollForTaskInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.pollForTask(xAmzTarget, pollForTaskInput, opts, (error, data, response) => {
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
 **pollForTaskInput** | [**PollForTaskInput**](PollForTaskInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PollForTaskOutput**](PollForTaskOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPipelineDefinition

> PutPipelineDefinitionOutput putPipelineDefinition(xAmzTarget, putPipelineDefinitionInput, opts)



&lt;p&gt;Adds tasks, schedules, and preconditions to the specified pipeline. You can use &lt;code&gt;PutPipelineDefinition&lt;/code&gt; to populate a new pipeline.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PutPipelineDefinition&lt;/code&gt; also validates the configuration as it adds it to the pipeline. Changes to the pipeline are saved unless one of the following three validation errors exists in the pipeline. &lt;/p&gt; &lt;ol&gt; &lt;li&gt;An object is missing a name or identifier field.&lt;/li&gt; &lt;li&gt;A string or reference field is empty.&lt;/li&gt; &lt;li&gt;The number of objects in the pipeline exceeds the maximum allowed objects.&lt;/li&gt; &lt;li&gt;The pipeline is in a FINISHED state.&lt;/li&gt; &lt;/ol&gt; &lt;p&gt; Pipeline object definitions are passed to the &lt;code&gt;PutPipelineDefinition&lt;/code&gt; action and returned by the &lt;a&gt;GetPipelineDefinition&lt;/a&gt; action. &lt;/p&gt;

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let putPipelineDefinitionInput = new AwsDataPipeline.PutPipelineDefinitionInput(); // PutPipelineDefinitionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putPipelineDefinition(xAmzTarget, putPipelineDefinitionInput, opts, (error, data, response) => {
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
 **putPipelineDefinitionInput** | [**PutPipelineDefinitionInput**](PutPipelineDefinitionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutPipelineDefinitionOutput**](PutPipelineDefinitionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryObjects

> QueryObjectsOutput queryObjects(xAmzTarget, queryObjectsInput, opts)



Queries the specified pipeline for the names of objects that match the specified set of conditions.

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let queryObjectsInput = new AwsDataPipeline.QueryObjectsInput(); // QueryObjectsInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'limit': "limit_example", // String | Pagination limit
  'marker': "marker_example" // String | Pagination token
};
apiInstance.queryObjects(xAmzTarget, queryObjectsInput, opts, (error, data, response) => {
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
 **queryObjectsInput** | [**QueryObjectsInput**](QueryObjectsInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **limit** | **String**| Pagination limit | [optional] 
 **marker** | **String**| Pagination token | [optional] 

### Return type

[**QueryObjectsOutput**](QueryObjectsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeTags

> Object removeTags(xAmzTarget, removeTagsInput, opts)



Removes existing tags from the specified pipeline.

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let removeTagsInput = new AwsDataPipeline.RemoveTagsInput(); // RemoveTagsInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.removeTags(xAmzTarget, removeTagsInput, opts, (error, data, response) => {
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
 **removeTagsInput** | [**RemoveTagsInput**](RemoveTagsInput.md)|  | 
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


## reportTaskProgress

> ReportTaskProgressOutput reportTaskProgress(xAmzTarget, reportTaskProgressInput, opts)



&lt;p&gt;Task runners call &lt;code&gt;ReportTaskProgress&lt;/code&gt; when assigned a task to acknowledge that it has the task. If the web service does not receive this acknowledgement within 2 minutes, it assigns the task in a subsequent &lt;a&gt;PollForTask&lt;/a&gt; call. After this initial acknowledgement, the task runner only needs to report progress every 15 minutes to maintain its ownership of the task. You can change this reporting time from 15 minutes by specifying a &lt;code&gt;reportProgressTimeout&lt;/code&gt; field in your pipeline.&lt;/p&gt; &lt;p&gt;If a task runner does not report its status after 5 minutes, AWS Data Pipeline assumes that the task runner is unable to process the task and reassigns the task in a subsequent response to &lt;a&gt;PollForTask&lt;/a&gt;. Task runners should call &lt;code&gt;ReportTaskProgress&lt;/code&gt; every 60 seconds.&lt;/p&gt;

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let reportTaskProgressInput = new AwsDataPipeline.ReportTaskProgressInput(); // ReportTaskProgressInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.reportTaskProgress(xAmzTarget, reportTaskProgressInput, opts, (error, data, response) => {
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
 **reportTaskProgressInput** | [**ReportTaskProgressInput**](ReportTaskProgressInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ReportTaskProgressOutput**](ReportTaskProgressOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reportTaskRunnerHeartbeat

> ReportTaskRunnerHeartbeatOutput reportTaskRunnerHeartbeat(xAmzTarget, reportTaskRunnerHeartbeatInput, opts)



Task runners call &lt;code&gt;ReportTaskRunnerHeartbeat&lt;/code&gt; every 15 minutes to indicate that they are operational. If the AWS Data Pipeline Task Runner is launched on a resource managed by AWS Data Pipeline, the web service can use this call to detect when the task runner application has failed and restart a new instance.

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let reportTaskRunnerHeartbeatInput = new AwsDataPipeline.ReportTaskRunnerHeartbeatInput(); // ReportTaskRunnerHeartbeatInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.reportTaskRunnerHeartbeat(xAmzTarget, reportTaskRunnerHeartbeatInput, opts, (error, data, response) => {
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
 **reportTaskRunnerHeartbeatInput** | [**ReportTaskRunnerHeartbeatInput**](ReportTaskRunnerHeartbeatInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ReportTaskRunnerHeartbeatOutput**](ReportTaskRunnerHeartbeatOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setStatus

> setStatus(xAmzTarget, setStatusInput, opts)



Requests that the status of the specified physical or logical pipeline objects be updated in the specified pipeline. This update might not occur immediately, but is eventually consistent. The status that can be set depends on the type of object (for example, DataNode or Activity). You cannot perform this operation on &lt;code&gt;FINISHED&lt;/code&gt; pipelines and attempting to do so returns &lt;code&gt;InvalidRequestException&lt;/code&gt;.

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let setStatusInput = new AwsDataPipeline.SetStatusInput(); // SetStatusInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.setStatus(xAmzTarget, setStatusInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **setStatusInput** | [**SetStatusInput**](SetStatusInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setTaskStatus

> Object setTaskStatus(xAmzTarget, setTaskStatusInput, opts)



Task runners call &lt;code&gt;SetTaskStatus&lt;/code&gt; to notify AWS Data Pipeline that a task is completed and provide information about the final status. A task runner makes this call regardless of whether the task was sucessful. A task runner does not need to call &lt;code&gt;SetTaskStatus&lt;/code&gt; for tasks that are canceled by the web service during a call to &lt;a&gt;ReportTaskProgress&lt;/a&gt;.

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let setTaskStatusInput = new AwsDataPipeline.SetTaskStatusInput(); // SetTaskStatusInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.setTaskStatus(xAmzTarget, setTaskStatusInput, opts, (error, data, response) => {
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
 **setTaskStatusInput** | [**SetTaskStatusInput**](SetTaskStatusInput.md)|  | 
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


## validatePipelineDefinition

> ValidatePipelineDefinitionOutput validatePipelineDefinition(xAmzTarget, validatePipelineDefinitionInput, opts)



Validates the specified pipeline definition to ensure that it is well formed and can be run without error.

### Example

```javascript
import AwsDataPipeline from 'aws_data_pipeline';
let defaultClient = AwsDataPipeline.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsDataPipeline.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let validatePipelineDefinitionInput = new AwsDataPipeline.ValidatePipelineDefinitionInput(); // ValidatePipelineDefinitionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.validatePipelineDefinition(xAmzTarget, validatePipelineDefinitionInput, opts, (error, data, response) => {
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
 **validatePipelineDefinitionInput** | [**ValidatePipelineDefinitionInput**](ValidatePipelineDefinitionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ValidatePipelineDefinitionOutput**](ValidatePipelineDefinitionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

