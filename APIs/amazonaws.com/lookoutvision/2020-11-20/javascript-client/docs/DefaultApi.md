# AmazonLookoutForVision.DefaultApi

All URIs are relative to *http://lookoutvision.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDataset**](DefaultApi.md#createDataset) | **POST** /2020-11-20/projects/{projectName}/datasets | 
[**createModel**](DefaultApi.md#createModel) | **POST** /2020-11-20/projects/{projectName}/models | 
[**createProject**](DefaultApi.md#createProject) | **POST** /2020-11-20/projects | 
[**deleteDataset**](DefaultApi.md#deleteDataset) | **DELETE** /2020-11-20/projects/{projectName}/datasets/{datasetType} | 
[**deleteModel**](DefaultApi.md#deleteModel) | **DELETE** /2020-11-20/projects/{projectName}/models/{modelVersion} | 
[**deleteProject**](DefaultApi.md#deleteProject) | **DELETE** /2020-11-20/projects/{projectName} | 
[**describeDataset**](DefaultApi.md#describeDataset) | **GET** /2020-11-20/projects/{projectName}/datasets/{datasetType} | 
[**describeModel**](DefaultApi.md#describeModel) | **GET** /2020-11-20/projects/{projectName}/models/{modelVersion} | 
[**describeModelPackagingJob**](DefaultApi.md#describeModelPackagingJob) | **GET** /2020-11-20/projects/{projectName}/modelpackagingjobs/{jobName} | 
[**describeProject**](DefaultApi.md#describeProject) | **GET** /2020-11-20/projects/{projectName} | 
[**detectAnomalies**](DefaultApi.md#detectAnomalies) | **POST** /2020-11-20/projects/{projectName}/models/{modelVersion}/detect#Content-Type | 
[**listDatasetEntries**](DefaultApi.md#listDatasetEntries) | **GET** /2020-11-20/projects/{projectName}/datasets/{datasetType}/entries | 
[**listModelPackagingJobs**](DefaultApi.md#listModelPackagingJobs) | **GET** /2020-11-20/projects/{projectName}/modelpackagingjobs | 
[**listModels**](DefaultApi.md#listModels) | **GET** /2020-11-20/projects/{projectName}/models | 
[**listProjects**](DefaultApi.md#listProjects) | **GET** /2020-11-20/projects | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /2020-11-20/tags/{resourceArn} | 
[**startModel**](DefaultApi.md#startModel) | **POST** /2020-11-20/projects/{projectName}/models/{modelVersion}/start | 
[**startModelPackagingJob**](DefaultApi.md#startModelPackagingJob) | **POST** /2020-11-20/projects/{projectName}/modelpackagingjobs | 
[**stopModel**](DefaultApi.md#stopModel) | **POST** /2020-11-20/projects/{projectName}/models/{modelVersion}/stop | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /2020-11-20/tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /2020-11-20/tags/{resourceArn}#tagKeys | 
[**updateDatasetEntries**](DefaultApi.md#updateDatasetEntries) | **PATCH** /2020-11-20/projects/{projectName}/datasets/{datasetType}/entries | 



## createDataset

> CreateDatasetResponse createDataset(projectName, createDatasetRequest, opts)



&lt;p&gt;Creates a new dataset in an Amazon Lookout for Vision project. &lt;code&gt;CreateDataset&lt;/code&gt; can create a training or a test dataset from a valid dataset source (&lt;code&gt;DatasetSource&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;If you want a single dataset project, specify &lt;code&gt;train&lt;/code&gt; for the value of &lt;code&gt;DatasetType&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To have a project with separate training and test datasets, call &lt;code&gt;CreateDataset&lt;/code&gt; twice. On the first call, specify &lt;code&gt;train&lt;/code&gt; for the value of &lt;code&gt;DatasetType&lt;/code&gt;. On the second call, specify &lt;code&gt;test&lt;/code&gt; for the value of &lt;code&gt;DatasetType&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:CreateDataset&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The name of the project in which you want to create a dataset.
let createDatasetRequest = new AmazonLookoutForVision.CreateDatasetRequest(); // CreateDatasetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmznClientToken': "xAmznClientToken_example" // String | <p>ClientToken is an idempotency token that ensures a call to <code>CreateDataset</code> completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from <code>CreateDataset</code>. In this case, safely retry your call to <code>CreateDataset</code> by using the same <code>ClientToken</code> parameter value.</p> <p>If you don't supply a value for <code>ClientToken</code>, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple dataset creation requests. You'll need to provide your own value for other use cases. </p> <p>An error occurs if the other input parameters are not the same as in the first request. Using a different value for <code>ClientToken</code> is considered a new call to <code>CreateDataset</code>. An idempotency token is active for 8 hours. </p>
};
apiInstance.createDataset(projectName, createDatasetRequest, opts, (error, data, response) => {
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
 **projectName** | **String**| The name of the project in which you want to create a dataset. | 
 **createDatasetRequest** | [**CreateDatasetRequest**](CreateDatasetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmznClientToken** | **String**| &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;CreateDataset&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;CreateDataset&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;CreateDataset&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value.&lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple dataset creation requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;CreateDataset&lt;/code&gt;. An idempotency token is active for 8 hours. &lt;/p&gt; | [optional] 

### Return type

[**CreateDatasetResponse**](CreateDatasetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createModel

> CreateModelResponse createModel(projectName, createModelRequest, opts)



&lt;p&gt;Creates a new version of a model within an an Amazon Lookout for Vision project. &lt;code&gt;CreateModel&lt;/code&gt; is an asynchronous operation in which Amazon Lookout for Vision trains, tests, and evaluates a new version of a model. &lt;/p&gt; &lt;p&gt;To get the current status, check the &lt;code&gt;Status&lt;/code&gt; field returned in the response from &lt;a&gt;DescribeModel&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If the project has a single dataset, Amazon Lookout for Vision internally splits the dataset to create a training and a test dataset. If the project has a training and a test dataset, Lookout for Vision uses the respective datasets to train and test the model. &lt;/p&gt; &lt;p&gt;After training completes, the evaluation metrics are stored at the location specified in &lt;code&gt;OutputConfig&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:CreateModel&lt;/code&gt; operation. If you want to tag your model, you also require permission to the &lt;code&gt;lookoutvision:TagResource&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The name of the project in which you want to create a model version.
let createModelRequest = new AmazonLookoutForVision.CreateModelRequest(); // CreateModelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmznClientToken': "xAmznClientToken_example" // String | <p>ClientToken is an idempotency token that ensures a call to <code>CreateModel</code> completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from <code>CreateModel</code>. In this case, safely retry your call to <code>CreateModel</code> by using the same <code>ClientToken</code> parameter value. </p> <p>If you don't supply a value for <code>ClientToken</code>, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from starting multiple training jobs. You'll need to provide your own value for other use cases. </p> <p>An error occurs if the other input parameters are not the same as in the first request. Using a different value for <code>ClientToken</code> is considered a new call to <code>CreateModel</code>. An idempotency token is active for 8 hours.</p>
};
apiInstance.createModel(projectName, createModelRequest, opts, (error, data, response) => {
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
 **projectName** | **String**| The name of the project in which you want to create a model version. | 
 **createModelRequest** | [**CreateModelRequest**](CreateModelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmznClientToken** | **String**| &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;CreateModel&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;CreateModel&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;CreateModel&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value. &lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from starting multiple training jobs. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;CreateModel&lt;/code&gt;. An idempotency token is active for 8 hours.&lt;/p&gt; | [optional] 

### Return type

[**CreateModelResponse**](CreateModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createProject

> CreateProjectResponse createProject(createProjectRequest, opts)



&lt;p&gt;Creates an empty Amazon Lookout for Vision project. After you create the project, add a dataset by calling &lt;a&gt;CreateDataset&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:CreateProject&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let createProjectRequest = new AmazonLookoutForVision.CreateProjectRequest(); // CreateProjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmznClientToken': "xAmznClientToken_example" // String | <p>ClientToken is an idempotency token that ensures a call to <code>CreateProject</code> completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from <code>CreateProject</code>. In this case, safely retry your call to <code>CreateProject</code> by using the same <code>ClientToken</code> parameter value. </p> <p>If you don't supply a value for <code>ClientToken</code>, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple project creation requests. You'll need to provide your own value for other use cases. </p> <p>An error occurs if the other input parameters are not the same as in the first request. Using a different value for <code>ClientToken</code> is considered a new call to <code>CreateProject</code>. An idempotency token is active for 8 hours.</p>
};
apiInstance.createProject(createProjectRequest, opts, (error, data, response) => {
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
 **createProjectRequest** | [**CreateProjectRequest**](CreateProjectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmznClientToken** | **String**| &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;CreateProject&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;CreateProject&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;CreateProject&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value. &lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple project creation requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;CreateProject&lt;/code&gt;. An idempotency token is active for 8 hours.&lt;/p&gt; | [optional] 

### Return type

[**CreateProjectResponse**](CreateProjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDataset

> Object deleteDataset(projectName, datasetType, opts)



&lt;p&gt;Deletes an existing Amazon Lookout for Vision &lt;code&gt;dataset&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;If your the project has a single dataset, you must create a new dataset before you can create a model.&lt;/p&gt; &lt;p&gt;If you project has a training dataset and a test dataset consider the following. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you delete the test dataset, your project reverts to a single dataset project. If you then train the model, Amazon Lookout for Vision internally splits the remaining dataset into a training and test dataset.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you delete the training dataset, you must create a training dataset before you can create a model.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DeleteDataset&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The name of the project that contains the dataset that you want to delete.
let datasetType = "datasetType_example"; // String | The type of the dataset to delete. Specify <code>train</code> to delete the training dataset. Specify <code>test</code> to delete the test dataset. To delete the dataset in a single dataset project, specify <code>train</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmznClientToken': "xAmznClientToken_example" // String | <p>ClientToken is an idempotency token that ensures a call to <code>DeleteDataset</code> completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from <code>DeleteDataset</code>. In this case, safely retry your call to <code>DeleteDataset</code> by using the same <code>ClientToken</code> parameter value. </p> <p>If you don't supply a value for <code>ClientToken</code>, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple deletetion requests. You'll need to provide your own value for other use cases. </p> <p>An error occurs if the other input parameters are not the same as in the first request. Using a different value for <code>ClientToken</code> is considered a new call to <code>DeleteDataset</code>. An idempotency token is active for 8 hours.</p>
};
apiInstance.deleteDataset(projectName, datasetType, opts, (error, data, response) => {
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
 **projectName** | **String**| The name of the project that contains the dataset that you want to delete. | 
 **datasetType** | **String**| The type of the dataset to delete. Specify &lt;code&gt;train&lt;/code&gt; to delete the training dataset. Specify &lt;code&gt;test&lt;/code&gt; to delete the test dataset. To delete the dataset in a single dataset project, specify &lt;code&gt;train&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmznClientToken** | **String**| &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;DeleteDataset&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;DeleteDataset&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;DeleteDataset&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value. &lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple deletetion requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;DeleteDataset&lt;/code&gt;. An idempotency token is active for 8 hours.&lt;/p&gt; | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteModel

> DeleteModelResponse deleteModel(projectName, modelVersion, opts)



&lt;p&gt;Deletes an Amazon Lookout for Vision model. You can&#39;t delete a running model. To stop a running model, use the &lt;a&gt;StopModel&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;It might take a few seconds to delete a model. To determine if a model has been deleted, call &lt;a&gt;ListModels&lt;/a&gt; and check if the version of the model (&lt;code&gt;ModelVersion&lt;/code&gt;) is in the &lt;code&gt;Models&lt;/code&gt; array. &lt;/p&gt; &lt;p/&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DeleteModel&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The name of the project that contains the model that you want to delete.
let modelVersion = "modelVersion_example"; // String | The version of the model that you want to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmznClientToken': "xAmznClientToken_example" // String | <p>ClientToken is an idempotency token that ensures a call to <code>DeleteModel</code> completes only once. You choose the value to pass. For example, an issue might prevent you from getting a response from <code>DeleteModel</code>. In this case, safely retry your call to <code>DeleteModel</code> by using the same <code>ClientToken</code> parameter value.</p> <p>If you don't supply a value for ClientToken, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple model deletion requests. You'll need to provide your own value for other use cases. </p> <p>An error occurs if the other input parameters are not the same as in the first request. Using a different value for <code>ClientToken</code> is considered a new call to <code>DeleteModel</code>. An idempotency token is active for 8 hours.</p>
};
apiInstance.deleteModel(projectName, modelVersion, opts, (error, data, response) => {
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
 **projectName** | **String**| The name of the project that contains the model that you want to delete. | 
 **modelVersion** | **String**| The version of the model that you want to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmznClientToken** | **String**| &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;DeleteModel&lt;/code&gt; completes only once. You choose the value to pass. For example, an issue might prevent you from getting a response from &lt;code&gt;DeleteModel&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;DeleteModel&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value.&lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for ClientToken, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple model deletion requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;DeleteModel&lt;/code&gt;. An idempotency token is active for 8 hours.&lt;/p&gt; | [optional] 

### Return type

[**DeleteModelResponse**](DeleteModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteProject

> DeleteProjectResponse deleteProject(projectName, opts)



&lt;p&gt;Deletes an Amazon Lookout for Vision project.&lt;/p&gt; &lt;p&gt;To delete a project, you must first delete each version of the model associated with the project. To delete a model use the &lt;a&gt;DeleteModel&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;You also have to delete the dataset(s) associated with the model. For more information, see &lt;a&gt;DeleteDataset&lt;/a&gt;. The images referenced by the training and test datasets aren&#39;t deleted. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DeleteProject&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The name of the project to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmznClientToken': "xAmznClientToken_example" // String | <p>ClientToken is an idempotency token that ensures a call to <code>DeleteProject</code> completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from <code>DeleteProject</code>. In this case, safely retry your call to <code>DeleteProject</code> by using the same <code>ClientToken</code> parameter value. </p> <p>If you don't supply a value for <code>ClientToken</code>, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple project deletion requests. You'll need to provide your own value for other use cases. </p> <p>An error occurs if the other input parameters are not the same as in the first request. Using a different value for <code>ClientToken</code> is considered a new call to <code>DeleteProject</code>. An idempotency token is active for 8 hours.</p>
};
apiInstance.deleteProject(projectName, opts, (error, data, response) => {
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
 **projectName** | **String**| The name of the project to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmznClientToken** | **String**| &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;DeleteProject&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;DeleteProject&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;DeleteProject&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value. &lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple project deletion requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;DeleteProject&lt;/code&gt;. An idempotency token is active for 8 hours.&lt;/p&gt; | [optional] 

### Return type

[**DeleteProjectResponse**](DeleteProjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeDataset

> DescribeDatasetResponse describeDataset(projectName, datasetType, opts)



&lt;p&gt;Describe an Amazon Lookout for Vision dataset.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DescribeDataset&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The name of the project that contains the dataset that you want to describe.
let datasetType = "datasetType_example"; // String | The type of the dataset to describe. Specify <code>train</code> to describe the training dataset. Specify <code>test</code> to describe the test dataset. If you have a single dataset project, specify <code>train</code> 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeDataset(projectName, datasetType, opts, (error, data, response) => {
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
 **projectName** | **String**| The name of the project that contains the dataset that you want to describe. | 
 **datasetType** | **String**| The type of the dataset to describe. Specify &lt;code&gt;train&lt;/code&gt; to describe the training dataset. Specify &lt;code&gt;test&lt;/code&gt; to describe the test dataset. If you have a single dataset project, specify &lt;code&gt;train&lt;/code&gt;  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeDatasetResponse**](DescribeDatasetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeModel

> DescribeModelResponse describeModel(projectName, modelVersion, opts)



&lt;p&gt;Describes a version of an Amazon Lookout for Vision model.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DescribeModel&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The project that contains the version of a model that you want to describe.
let modelVersion = "modelVersion_example"; // String | The version of the model that you want to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeModel(projectName, modelVersion, opts, (error, data, response) => {
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
 **projectName** | **String**| The project that contains the version of a model that you want to describe. | 
 **modelVersion** | **String**| The version of the model that you want to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeModelResponse**](DescribeModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeModelPackagingJob

> DescribeModelPackagingJobResponse describeModelPackagingJob(projectName, jobName, opts)



&lt;p&gt;Describes an Amazon Lookout for Vision model packaging job. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DescribeModelPackagingJob&lt;/code&gt; operation.&lt;/p&gt; &lt;p&gt;For more information, see &lt;i&gt;Using your Amazon Lookout for Vision model on an edge device&lt;/i&gt; in the Amazon Lookout for Vision Developer Guide. &lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The name of the project that contains the model packaging job that you want to describe. 
let jobName = "jobName_example"; // String | The job name for the model packaging job. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeModelPackagingJob(projectName, jobName, opts, (error, data, response) => {
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
 **projectName** | **String**| The name of the project that contains the model packaging job that you want to describe.  | 
 **jobName** | **String**| The job name for the model packaging job.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeModelPackagingJobResponse**](DescribeModelPackagingJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeProject

> DescribeProjectResponse describeProject(projectName, opts)



&lt;p&gt;Describes an Amazon Lookout for Vision project.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DescribeProject&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The name of the project that you want to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeProject(projectName, opts, (error, data, response) => {
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
 **projectName** | **String**| The name of the project that you want to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeProjectResponse**](DescribeProjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## detectAnomalies

> DetectAnomaliesResponse detectAnomalies(projectName, modelVersion, contentType, detectAnomaliesRequest, opts)



&lt;p&gt;Detects anomalies in an image that you supply. &lt;/p&gt; &lt;p&gt;The response from &lt;code&gt;DetectAnomalies&lt;/code&gt; includes a boolean prediction that the image contains one or more anomalies and a confidence value for the prediction. If the model is an image segmentation model, the response also includes segmentation information for each type of anomaly found in the image.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before calling &lt;code&gt;DetectAnomalies&lt;/code&gt;, you must first start your model with the &lt;a&gt;StartModel&lt;/a&gt; operation. You are charged for the amount of time, in minutes, that a model runs and for the number of anomaly detection units that your model uses. If you are not using a model, use the &lt;a&gt;StopModel&lt;/a&gt; operation to stop your model. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;For more information, see &lt;i&gt;Detecting anomalies in an image&lt;/i&gt; in the Amazon Lookout for Vision developer guide.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DetectAnomalies&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The name of the project that contains the model version that you want to use.
let modelVersion = "modelVersion_example"; // String | The version of the model that you want to use.
let contentType = "contentType_example"; // String | The type of the image passed in <code>Body</code>. Valid values are <code>image/png</code> (PNG format images) and <code>image/jpeg</code> (JPG format images). 
let detectAnomaliesRequest = new AmazonLookoutForVision.DetectAnomaliesRequest(); // DetectAnomaliesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.detectAnomalies(projectName, modelVersion, contentType, detectAnomaliesRequest, opts, (error, data, response) => {
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
 **projectName** | **String**| The name of the project that contains the model version that you want to use. | 
 **modelVersion** | **String**| The version of the model that you want to use. | 
 **contentType** | **String**| The type of the image passed in &lt;code&gt;Body&lt;/code&gt;. Valid values are &lt;code&gt;image/png&lt;/code&gt; (PNG format images) and &lt;code&gt;image/jpeg&lt;/code&gt; (JPG format images).  | 
 **detectAnomaliesRequest** | [**DetectAnomaliesRequest**](DetectAnomaliesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DetectAnomaliesResponse**](DetectAnomaliesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listDatasetEntries

> ListDatasetEntriesResponse listDatasetEntries(projectName, datasetType, opts)



&lt;p&gt;Lists the JSON Lines within a dataset. An Amazon Lookout for Vision JSON Line contains the anomaly information for a single image, including the image location and the assigned label.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:ListDatasetEntries&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The name of the project that contains the dataset that you want to list.
let datasetType = "datasetType_example"; // String | The type of the dataset that you want to list. Specify <code>train</code> to list the training dataset. Specify <code>test</code> to list the test dataset. If you have a single dataset project, specify <code>train</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'labeled': true, // Boolean | Specify <code>true</code> to include labeled entries, otherwise specify <code>false</code>. If you don't specify a value, Lookout for Vision returns all entries.
  'anomalyClass': "anomalyClass_example", // String | Specify <code>normal</code> to include only normal images. Specify <code>anomaly</code> to only include anomalous entries. If you don't specify a value, Amazon Lookout for Vision returns normal and anomalous images.
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Only includes entries before the specified date in the response. For example, <code>2020-06-23T00:00:00</code>.
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Only includes entries after the specified date in the response. For example, <code>2020-06-23T00:00:00</code>.
  'nextToken': "nextToken_example", // String | If the previous response was incomplete (because there is more data to retrieve), Amazon Lookout for Vision returns a pagination token in the response. You can use this pagination token to retrieve the next set of dataset entries.
  'maxResults': 56, // Number | The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100.
  'sourceRefContains': "sourceRefContains_example", // String | Perform a \"contains\" search on the values of the <code>source-ref</code> key within the dataset. For example a value of \"IMG_17\" returns all JSON Lines where the <code>source-ref</code> key value matches <i>*IMG_17*</i>.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listDatasetEntries(projectName, datasetType, opts, (error, data, response) => {
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
 **projectName** | **String**| The name of the project that contains the dataset that you want to list. | 
 **datasetType** | **String**| The type of the dataset that you want to list. Specify &lt;code&gt;train&lt;/code&gt; to list the training dataset. Specify &lt;code&gt;test&lt;/code&gt; to list the test dataset. If you have a single dataset project, specify &lt;code&gt;train&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **labeled** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to include labeled entries, otherwise specify &lt;code&gt;false&lt;/code&gt;. If you don&#39;t specify a value, Lookout for Vision returns all entries. | [optional] 
 **anomalyClass** | **String**| Specify &lt;code&gt;normal&lt;/code&gt; to include only normal images. Specify &lt;code&gt;anomaly&lt;/code&gt; to only include anomalous entries. If you don&#39;t specify a value, Amazon Lookout for Vision returns normal and anomalous images. | [optional] 
 **createdBefore** | **Date**| Only includes entries before the specified date in the response. For example, &lt;code&gt;2020-06-23T00:00:00&lt;/code&gt;. | [optional] 
 **createdAfter** | **Date**| Only includes entries after the specified date in the response. For example, &lt;code&gt;2020-06-23T00:00:00&lt;/code&gt;. | [optional] 
 **nextToken** | **String**| If the previous response was incomplete (because there is more data to retrieve), Amazon Lookout for Vision returns a pagination token in the response. You can use this pagination token to retrieve the next set of dataset entries. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100. | [optional] 
 **sourceRefContains** | **String**| Perform a \&quot;contains\&quot; search on the values of the &lt;code&gt;source-ref&lt;/code&gt; key within the dataset. For example a value of \&quot;IMG_17\&quot; returns all JSON Lines where the &lt;code&gt;source-ref&lt;/code&gt; key value matches &lt;i&gt;*IMG_17*&lt;/i&gt;. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListDatasetEntriesResponse**](ListDatasetEntriesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listModelPackagingJobs

> ListModelPackagingJobsResponse listModelPackagingJobs(projectName, opts)



&lt;p&gt; Lists the model packaging jobs created for an Amazon Lookout for Vision project. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:ListModelPackagingJobs&lt;/code&gt; operation. &lt;/p&gt; &lt;p&gt;For more information, see &lt;i&gt;Using your Amazon Lookout for Vision model on an edge device&lt;/i&gt; in the Amazon Lookout for Vision Developer Guide. &lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String |  The name of the project for which you want to list the model packaging jobs. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | If the previous response was incomplete (because there is more results to retrieve), Amazon Lookout for Vision returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. 
  'maxResults': 56, // Number | The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100. 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listModelPackagingJobs(projectName, opts, (error, data, response) => {
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
 **projectName** | **String**|  The name of the project for which you want to list the model packaging jobs.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| If the previous response was incomplete (because there is more results to retrieve), Amazon Lookout for Vision returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100.  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListModelPackagingJobsResponse**](ListModelPackagingJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listModels

> ListModelsResponse listModels(projectName, opts)



&lt;p&gt;Lists the versions of a model in an Amazon Lookout for Vision project.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;ListModels&lt;/code&gt; operation is eventually consistent. Recent calls to &lt;code&gt;CreateModel&lt;/code&gt; might take a while to appear in the response from &lt;code&gt;ListProjects&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:ListModels&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The name of the project that contains the model versions that you want to list.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | If the previous response was incomplete (because there is more data to retrieve), Amazon Lookout for Vision returns a pagination token in the response. You can use this pagination token to retrieve the next set of models.
  'maxResults': 56, // Number | The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listModels(projectName, opts, (error, data, response) => {
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
 **projectName** | **String**| The name of the project that contains the model versions that you want to list. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| If the previous response was incomplete (because there is more data to retrieve), Amazon Lookout for Vision returns a pagination token in the response. You can use this pagination token to retrieve the next set of models. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListModelsResponse**](ListModelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProjects

> ListProjectsResponse listProjects(opts)



&lt;p&gt;Lists the Amazon Lookout for Vision projects in your AWS account that are in the AWS Region in which you call &lt;code&gt;ListProjects&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;ListProjects&lt;/code&gt; operation is eventually consistent. Recent calls to &lt;code&gt;CreateProject&lt;/code&gt; and &lt;code&gt;DeleteProject&lt;/code&gt; might take a while to appear in the response from &lt;code&gt;ListProjects&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:ListProjects&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | If the previous response was incomplete (because there is more data to retrieve), Amazon Lookout for Vision returns a pagination token in the response. You can use this pagination token to retrieve the next set of projects.
  'maxResults': 56, // Number | The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listProjects(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| If the previous response was incomplete (because there is more data to retrieve), Amazon Lookout for Vision returns a pagination token in the response. You can use this pagination token to retrieve the next set of projects. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListProjectsResponse**](ListProjectsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



&lt;p&gt;Returns a list of tags attached to the specified Amazon Lookout for Vision model.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:ListTagsForResource&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the model for which you want to list tags. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the model for which you want to list tags.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startModel

> StartModelResponse startModel(projectName, modelVersion, startModelRequest, opts)



&lt;p&gt;Starts the running of the version of an Amazon Lookout for Vision model. Starting a model takes a while to complete. To check the current state of the model, use &lt;a&gt;DescribeModel&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;A model is ready to use when its status is &lt;code&gt;HOSTED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Once the model is running, you can detect custom labels in new images by calling &lt;a&gt;DetectAnomalies&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You are charged for the amount of time that the model is running. To stop a running model, call &lt;a&gt;StopModel&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:StartModel&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The name of the project that contains the model that you want to start.
let modelVersion = "modelVersion_example"; // String | The version of the model that you want to start.
let startModelRequest = new AmazonLookoutForVision.StartModelRequest(); // StartModelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmznClientToken': "xAmznClientToken_example" // String | <p>ClientToken is an idempotency token that ensures a call to <code>StartModel</code> completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from <code>StartModel</code>. In this case, safely retry your call to <code>StartModel</code> by using the same <code>ClientToken</code> parameter value. </p> <p>If you don't supply a value for <code>ClientToken</code>, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple start requests. You'll need to provide your own value for other use cases. </p> <p>An error occurs if the other input parameters are not the same as in the first request. Using a different value for <code>ClientToken</code> is considered a new call to <code>StartModel</code>. An idempotency token is active for 8 hours. </p>
};
apiInstance.startModel(projectName, modelVersion, startModelRequest, opts, (error, data, response) => {
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
 **projectName** | **String**| The name of the project that contains the model that you want to start. | 
 **modelVersion** | **String**| The version of the model that you want to start. | 
 **startModelRequest** | [**StartModelRequest**](StartModelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmznClientToken** | **String**| &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;StartModel&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;StartModel&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;StartModel&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value. &lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple start requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;StartModel&lt;/code&gt;. An idempotency token is active for 8 hours. &lt;/p&gt; | [optional] 

### Return type

[**StartModelResponse**](StartModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startModelPackagingJob

> StartModelPackagingJobResponse startModelPackagingJob(projectName, startModelPackagingJobRequest, opts)



&lt;p&gt;Starts an Amazon Lookout for Vision model packaging job. A model packaging job creates an AWS IoT Greengrass component for a Lookout for Vision model. You can use the component to deploy your model to an edge device managed by Greengrass. &lt;/p&gt; &lt;p&gt;Use the &lt;a&gt;DescribeModelPackagingJob&lt;/a&gt; API to determine the current status of the job. The model packaging job is complete if the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;SUCCEEDED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To deploy the component to the target device, use the component name and component version with the AWS IoT Greengrass &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CreateDeployment.html\&quot;&gt;CreateDeployment&lt;/a&gt; API.&lt;/p&gt; &lt;p&gt;This operation requires the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;lookoutvision:StartModelPackagingJob&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;s3:PutObject&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;s3:GetBucketLocation&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;kms:GenerateDataKey&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;greengrass:CreateComponentVersion&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;greengrass:DescribeComponent&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) &lt;code&gt;greengrass:TagResource&lt;/code&gt;. Only required if you want to tag the component.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;i&gt;Using your Amazon Lookout for Vision model on an edge device&lt;/i&gt; in the Amazon Lookout for Vision Developer Guide. &lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String |  The name of the project which contains the version of the model that you want to package. 
let startModelPackagingJobRequest = new AmazonLookoutForVision.StartModelPackagingJobRequest(); // StartModelPackagingJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmznClientToken': "xAmznClientToken_example" // String | <p>ClientToken is an idempotency token that ensures a call to <code>StartModelPackagingJob</code> completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from <code>StartModelPackagingJob</code>. In this case, safely retry your call to <code>StartModelPackagingJob</code> by using the same <code>ClientToken</code> parameter value.</p> <p>If you don't supply a value for <code>ClientToken</code>, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple dataset creation requests. You'll need to provide your own value for other use cases. </p> <p>An error occurs if the other input parameters are not the same as in the first request. Using a different value for <code>ClientToken</code> is considered a new call to <code>StartModelPackagingJob</code>. An idempotency token is active for 8 hours. </p>
};
apiInstance.startModelPackagingJob(projectName, startModelPackagingJobRequest, opts, (error, data, response) => {
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
 **projectName** | **String**|  The name of the project which contains the version of the model that you want to package.  | 
 **startModelPackagingJobRequest** | [**StartModelPackagingJobRequest**](StartModelPackagingJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmznClientToken** | **String**| &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;StartModelPackagingJob&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;StartModelPackagingJob&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;StartModelPackagingJob&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value.&lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple dataset creation requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;StartModelPackagingJob&lt;/code&gt;. An idempotency token is active for 8 hours. &lt;/p&gt; | [optional] 

### Return type

[**StartModelPackagingJobResponse**](StartModelPackagingJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopModel

> StopModelResponse stopModel(projectName, modelVersion, opts)



&lt;p&gt;Stops the hosting of a running model. The operation might take a while to complete. To check the current status, call &lt;a&gt;DescribeModel&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;After the model hosting stops, the &lt;code&gt;Status&lt;/code&gt; of the model is &lt;code&gt;TRAINED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:StopModel&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The name of the project that contains the model that you want to stop.
let modelVersion = "modelVersion_example"; // String | The version of the model that you want to stop.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmznClientToken': "xAmznClientToken_example" // String | <p>ClientToken is an idempotency token that ensures a call to <code>StopModel</code> completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from <code>StopModel</code>. In this case, safely retry your call to <code>StopModel</code> by using the same <code>ClientToken</code> parameter value.</p> <p>If you don't supply a value for <code>ClientToken</code>, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple stop requests. You'll need to provide your own value for other use cases. </p> <p>An error occurs if the other input parameters are not the same as in the first request. Using a different value for <code>ClientToken</code> is considered a new call to <code>StopModel</code>. An idempotency token is active for 8 hours. </p>
};
apiInstance.stopModel(projectName, modelVersion, opts, (error, data, response) => {
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
 **projectName** | **String**| The name of the project that contains the model that you want to stop. | 
 **modelVersion** | **String**| The version of the model that you want to stop. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmznClientToken** | **String**| &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;StopModel&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;StopModel&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;StopModel&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value.&lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple stop requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;StopModel&lt;/code&gt;. An idempotency token is active for 8 hours. &lt;/p&gt; | [optional] 

### Return type

[**StopModelResponse**](StopModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



&lt;p&gt;Adds one or more key-value tags to an Amazon Lookout for Vision model. For more information, see &lt;i&gt;Tagging a model&lt;/i&gt; in the &lt;i&gt;Amazon Lookout for Vision Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:TagResource&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the model to assign the tags.
let tagResourceRequest = new AmazonLookoutForVision.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceArn, tagResourceRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the model to assign the tags. | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
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

> Object untagResource(resourceArn, tagKeys, opts)



&lt;p&gt;Removes one or more tags from an Amazon Lookout for Vision model. For more information, see &lt;i&gt;Tagging a model&lt;/i&gt; in the &lt;i&gt;Amazon Lookout for Vision Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:UntagResource&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the model from which you want to remove tags. 
let tagKeys = ["null"]; // [String] | A list of the keys of the tags that you want to remove.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the model from which you want to remove tags.  | 
 **tagKeys** | [**[String]**](String.md)| A list of the keys of the tags that you want to remove. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDatasetEntries

> UpdateDatasetEntriesResponse updateDatasetEntries(projectName, datasetType, updateDatasetEntriesRequest, opts)



&lt;p&gt;Adds or updates one or more JSON Line entries in a dataset. A JSON Line includes information about an image used for training or testing an Amazon Lookout for Vision model.&lt;/p&gt; &lt;p&gt;To update an existing JSON Line, use the &lt;code&gt;source-ref&lt;/code&gt; field to identify the JSON Line. The JSON line that you supply replaces the existing JSON line. Any existing annotations that are not in the new JSON line are removed from the dataset. &lt;/p&gt; &lt;p&gt;For more information, see &lt;i&gt;Defining JSON lines for anomaly classification&lt;/i&gt; in the Amazon Lookout for Vision Developer Guide. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The images you reference in the &lt;code&gt;source-ref&lt;/code&gt; field of a JSON line, must be in the same S3 bucket as the existing images in the dataset. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Updating a dataset might take a while to complete. To check the current status, call &lt;a&gt;DescribeDataset&lt;/a&gt; and check the &lt;code&gt;Status&lt;/code&gt; field in the response.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:UpdateDatasetEntries&lt;/code&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLookoutForVision from 'amazon_lookout_for_vision';
let defaultClient = AmazonLookoutForVision.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLookoutForVision.DefaultApi();
let projectName = "projectName_example"; // String | The name of the project that contains the dataset that you want to update.
let datasetType = "datasetType_example"; // String | The type of the dataset that you want to update. Specify <code>train</code> to update the training dataset. Specify <code>test</code> to update the test dataset. If you have a single dataset project, specify <code>train</code>.
let updateDatasetEntriesRequest = new AmazonLookoutForVision.UpdateDatasetEntriesRequest(); // UpdateDatasetEntriesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmznClientToken': "xAmznClientToken_example" // String | <p>ClientToken is an idempotency token that ensures a call to <code>UpdateDatasetEntries</code> completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from <code>UpdateDatasetEntries</code>. In this case, safely retry your call to <code>UpdateDatasetEntries</code> by using the same <code>ClientToken</code> parameter value.</p> <p>If you don't supply a value for <code>ClientToken</code>, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple updates with the same dataset entries. You'll need to provide your own value for other use cases. </p> <p>An error occurs if the other input parameters are not the same as in the first request. Using a different value for <code>ClientToken</code> is considered a new call to <code>UpdateDatasetEntries</code>. An idempotency token is active for 8 hours. </p>
};
apiInstance.updateDatasetEntries(projectName, datasetType, updateDatasetEntriesRequest, opts, (error, data, response) => {
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
 **projectName** | **String**| The name of the project that contains the dataset that you want to update. | 
 **datasetType** | **String**| The type of the dataset that you want to update. Specify &lt;code&gt;train&lt;/code&gt; to update the training dataset. Specify &lt;code&gt;test&lt;/code&gt; to update the test dataset. If you have a single dataset project, specify &lt;code&gt;train&lt;/code&gt;. | 
 **updateDatasetEntriesRequest** | [**UpdateDatasetEntriesRequest**](UpdateDatasetEntriesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmznClientToken** | **String**| &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;UpdateDatasetEntries&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;UpdateDatasetEntries&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;UpdateDatasetEntries&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value.&lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple updates with the same dataset entries. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;UpdateDatasetEntries&lt;/code&gt;. An idempotency token is active for 8 hours. &lt;/p&gt; | [optional] 

### Return type

[**UpdateDatasetEntriesResponse**](UpdateDatasetEntriesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

