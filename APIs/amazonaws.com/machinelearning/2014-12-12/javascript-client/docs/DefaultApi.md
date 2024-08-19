# AmazonMachineLearning.DefaultApi

All URIs are relative to *http://machinelearning.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addTags**](DefaultApi.md#addTags) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.AddTags | 
[**createBatchPrediction**](DefaultApi.md#createBatchPrediction) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.CreateBatchPrediction | 
[**createDataSourceFromRDS**](DefaultApi.md#createDataSourceFromRDS) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.CreateDataSourceFromRDS | 
[**createDataSourceFromRedshift**](DefaultApi.md#createDataSourceFromRedshift) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.CreateDataSourceFromRedshift | 
[**createDataSourceFromS3**](DefaultApi.md#createDataSourceFromS3) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.CreateDataSourceFromS3 | 
[**createEvaluation**](DefaultApi.md#createEvaluation) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.CreateEvaluation | 
[**createMLModel**](DefaultApi.md#createMLModel) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.CreateMLModel | 
[**createRealtimeEndpoint**](DefaultApi.md#createRealtimeEndpoint) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.CreateRealtimeEndpoint | 
[**deleteBatchPrediction**](DefaultApi.md#deleteBatchPrediction) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DeleteBatchPrediction | 
[**deleteDataSource**](DefaultApi.md#deleteDataSource) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DeleteDataSource | 
[**deleteEvaluation**](DefaultApi.md#deleteEvaluation) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DeleteEvaluation | 
[**deleteMLModel**](DefaultApi.md#deleteMLModel) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DeleteMLModel | 
[**deleteRealtimeEndpoint**](DefaultApi.md#deleteRealtimeEndpoint) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DeleteRealtimeEndpoint | 
[**deleteTags**](DefaultApi.md#deleteTags) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DeleteTags | 
[**describeBatchPredictions**](DefaultApi.md#describeBatchPredictions) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DescribeBatchPredictions | 
[**describeDataSources**](DefaultApi.md#describeDataSources) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DescribeDataSources | 
[**describeEvaluations**](DefaultApi.md#describeEvaluations) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DescribeEvaluations | 
[**describeMLModels**](DefaultApi.md#describeMLModels) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DescribeMLModels | 
[**describeTags**](DefaultApi.md#describeTags) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DescribeTags | 
[**getBatchPrediction**](DefaultApi.md#getBatchPrediction) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.GetBatchPrediction | 
[**getDataSource**](DefaultApi.md#getDataSource) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.GetDataSource | 
[**getEvaluation**](DefaultApi.md#getEvaluation) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.GetEvaluation | 
[**getMLModel**](DefaultApi.md#getMLModel) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.GetMLModel | 
[**predict**](DefaultApi.md#predict) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.Predict | 
[**updateBatchPrediction**](DefaultApi.md#updateBatchPrediction) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.UpdateBatchPrediction | 
[**updateDataSource**](DefaultApi.md#updateDataSource) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.UpdateDataSource | 
[**updateEvaluation**](DefaultApi.md#updateEvaluation) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.UpdateEvaluation | 
[**updateMLModel**](DefaultApi.md#updateMLModel) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.UpdateMLModel | 



## addTags

> AddTagsOutput addTags(xAmzTarget, addTagsInput, opts)



Adds one or more tags to an object, up to a limit of 10. Each tag consists of a key and an optional value. If you add a tag using a key that is already associated with the ML object, &lt;code&gt;AddTags&lt;/code&gt; updates the tag&#39;s value.

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let addTagsInput = new AmazonMachineLearning.AddTagsInput(); // AddTagsInput | 
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

[**AddTagsOutput**](AddTagsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBatchPrediction

> CreateBatchPredictionOutput createBatchPrediction(xAmzTarget, createBatchPredictionInput, opts)



&lt;p&gt;Generates predictions for a group of observations. The observations to process exist in one or more data files referenced by a &lt;code&gt;DataSource&lt;/code&gt;. This operation creates a new &lt;code&gt;BatchPrediction&lt;/code&gt;, and uses an &lt;code&gt;MLModel&lt;/code&gt; and the data files referenced by the &lt;code&gt;DataSource&lt;/code&gt; as information sources. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateBatchPrediction&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateBatchPrediction&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;BatchPrediction&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;BatchPrediction&lt;/code&gt; completes, Amazon ML sets the status to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;You can poll for status updates by using the &lt;a&gt;GetBatchPrediction&lt;/a&gt; operation and checking the &lt;code&gt;Status&lt;/code&gt; parameter of the result. After the &lt;code&gt;COMPLETED&lt;/code&gt; status appears, the results are available in the location specified by the &lt;code&gt;OutputUri&lt;/code&gt; parameter.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createBatchPredictionInput = new AmazonMachineLearning.CreateBatchPredictionInput(); // CreateBatchPredictionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBatchPrediction(xAmzTarget, createBatchPredictionInput, opts, (error, data, response) => {
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
 **createBatchPredictionInput** | [**CreateBatchPredictionInput**](CreateBatchPredictionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBatchPredictionOutput**](CreateBatchPredictionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDataSourceFromRDS

> CreateDataSourceFromRDSOutput createDataSourceFromRDS(xAmzTarget, createDataSourceFromRDSInput, opts)



&lt;p&gt;Creates a &lt;code&gt;DataSource&lt;/code&gt; object from an &lt;a href&#x3D;\&quot;http://aws.amazon.com/rds/\&quot;&gt; Amazon Relational Database Service&lt;/a&gt; (Amazon RDS). A &lt;code&gt;DataSource&lt;/code&gt; references data that can be used to perform &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateDataSourceFromRDS&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateDataSourceFromRDS&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;DataSource&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;DataSource&lt;/code&gt; is created and ready for use, Amazon ML sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;code&gt;DataSource&lt;/code&gt; in the &lt;code&gt;COMPLETED&lt;/code&gt; or &lt;code&gt;PENDING&lt;/code&gt; state can be used only to perform &lt;code&gt;&amp;gt;CreateMLModel&lt;/code&gt;&amp;gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations. &lt;/p&gt; &lt;p&gt; If Amazon ML cannot accept the input source, it sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;FAILED&lt;/code&gt; and includes an error message in the &lt;code&gt;Message&lt;/code&gt; attribute of the &lt;code&gt;GetDataSource&lt;/code&gt; operation response. &lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createDataSourceFromRDSInput = new AmazonMachineLearning.CreateDataSourceFromRDSInput(); // CreateDataSourceFromRDSInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDataSourceFromRDS(xAmzTarget, createDataSourceFromRDSInput, opts, (error, data, response) => {
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
 **createDataSourceFromRDSInput** | [**CreateDataSourceFromRDSInput**](CreateDataSourceFromRDSInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDataSourceFromRDSOutput**](CreateDataSourceFromRDSOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDataSourceFromRedshift

> CreateDataSourceFromRedshiftOutput createDataSourceFromRedshift(xAmzTarget, createDataSourceFromRedshiftInput, opts)



&lt;p&gt;Creates a &lt;code&gt;DataSource&lt;/code&gt; from a database hosted on an Amazon Redshift cluster. A &lt;code&gt;DataSource&lt;/code&gt; references data that can be used to perform either &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateDataSourceFromRedshift&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateDataSourceFromRedshift&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;DataSource&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;DataSource&lt;/code&gt; is created and ready for use, Amazon ML sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;code&gt;DataSource&lt;/code&gt; in &lt;code&gt;COMPLETED&lt;/code&gt; or &lt;code&gt;PENDING&lt;/code&gt; states can be used to perform only &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations. &lt;/p&gt; &lt;p&gt; If Amazon ML can&#39;t accept the input source, it sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;FAILED&lt;/code&gt; and includes an error message in the &lt;code&gt;Message&lt;/code&gt; attribute of the &lt;code&gt;GetDataSource&lt;/code&gt; operation response. &lt;/p&gt; &lt;p&gt;The observations should be contained in the database hosted on an Amazon Redshift cluster and should be specified by a &lt;code&gt;SelectSqlQuery&lt;/code&gt; query. Amazon ML executes an &lt;code&gt;Unload&lt;/code&gt; command in Amazon Redshift to transfer the result set of the &lt;code&gt;SelectSqlQuery&lt;/code&gt; query to &lt;code&gt;S3StagingLocation&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;After the &lt;code&gt;DataSource&lt;/code&gt; has been created, it&#39;s ready for use in evaluations and batch predictions. If you plan to use the &lt;code&gt;DataSource&lt;/code&gt; to train an &lt;code&gt;MLModel&lt;/code&gt;, the &lt;code&gt;DataSource&lt;/code&gt; also requires a recipe. A recipe describes how each input variable will be used in training an &lt;code&gt;MLModel&lt;/code&gt;. Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.&lt;/p&gt; &lt;p&gt;You can&#39;t change an existing datasource, but you can copy and modify the settings from an existing Amazon Redshift datasource to create a new datasource. To do so, call &lt;code&gt;GetDataSource&lt;/code&gt; for an existing datasource and copy the values to a &lt;code&gt;CreateDataSource&lt;/code&gt; call. Change the settings that you want to change and make sure that all required fields have the appropriate values.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createDataSourceFromRedshiftInput = new AmazonMachineLearning.CreateDataSourceFromRedshiftInput(); // CreateDataSourceFromRedshiftInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDataSourceFromRedshift(xAmzTarget, createDataSourceFromRedshiftInput, opts, (error, data, response) => {
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
 **createDataSourceFromRedshiftInput** | [**CreateDataSourceFromRedshiftInput**](CreateDataSourceFromRedshiftInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDataSourceFromRedshiftOutput**](CreateDataSourceFromRedshiftOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDataSourceFromS3

> CreateDataSourceFromS3Output createDataSourceFromS3(xAmzTarget, createDataSourceFromS3Input, opts)



&lt;p&gt;Creates a &lt;code&gt;DataSource&lt;/code&gt; object. A &lt;code&gt;DataSource&lt;/code&gt; references data that can be used to perform &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateDataSourceFromS3&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateDataSourceFromS3&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;DataSource&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;DataSource&lt;/code&gt; has been created and is ready for use, Amazon ML sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;code&gt;DataSource&lt;/code&gt; in the &lt;code&gt;COMPLETED&lt;/code&gt; or &lt;code&gt;PENDING&lt;/code&gt; state can be used to perform only &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt; or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations. &lt;/p&gt; &lt;p&gt; If Amazon ML can&#39;t accept the input source, it sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;FAILED&lt;/code&gt; and includes an error message in the &lt;code&gt;Message&lt;/code&gt; attribute of the &lt;code&gt;GetDataSource&lt;/code&gt; operation response. &lt;/p&gt; &lt;p&gt;The observation data used in a &lt;code&gt;DataSource&lt;/code&gt; should be ready to use; that is, it should have a consistent structure, and missing data values should be kept to a minimum. The observation data must reside in one or more .csv files in an Amazon Simple Storage Service (Amazon S3) location, along with a schema that describes the data items by name and type. The same schema must be used for all of the data files referenced by the &lt;code&gt;DataSource&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;After the &lt;code&gt;DataSource&lt;/code&gt; has been created, it&#39;s ready to use in evaluations and batch predictions. If you plan to use the &lt;code&gt;DataSource&lt;/code&gt; to train an &lt;code&gt;MLModel&lt;/code&gt;, the &lt;code&gt;DataSource&lt;/code&gt; also needs a recipe. A recipe describes how each input variable will be used in training an &lt;code&gt;MLModel&lt;/code&gt;. Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createDataSourceFromS3Input = new AmazonMachineLearning.CreateDataSourceFromS3Input(); // CreateDataSourceFromS3Input | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDataSourceFromS3(xAmzTarget, createDataSourceFromS3Input, opts, (error, data, response) => {
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
 **createDataSourceFromS3Input** | [**CreateDataSourceFromS3Input**](CreateDataSourceFromS3Input.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDataSourceFromS3Output**](CreateDataSourceFromS3Output.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createEvaluation

> CreateEvaluationOutput createEvaluation(xAmzTarget, createEvaluationInput, opts)



&lt;p&gt;Creates a new &lt;code&gt;Evaluation&lt;/code&gt; of an &lt;code&gt;MLModel&lt;/code&gt;. An &lt;code&gt;MLModel&lt;/code&gt; is evaluated on a set of observations associated to a &lt;code&gt;DataSource&lt;/code&gt;. Like a &lt;code&gt;DataSource&lt;/code&gt; for an &lt;code&gt;MLModel&lt;/code&gt;, the &lt;code&gt;DataSource&lt;/code&gt; for an &lt;code&gt;Evaluation&lt;/code&gt; contains values for the &lt;code&gt;Target Variable&lt;/code&gt;. The &lt;code&gt;Evaluation&lt;/code&gt; compares the predicted result for each observation to the actual outcome and provides a summary so that you know how effective the &lt;code&gt;MLModel&lt;/code&gt; functions on the test data. Evaluation generates a relevant performance metric, such as BinaryAUC, RegressionRMSE or MulticlassAvgFScore based on the corresponding &lt;code&gt;MLModelType&lt;/code&gt;: &lt;code&gt;BINARY&lt;/code&gt;, &lt;code&gt;REGRESSION&lt;/code&gt; or &lt;code&gt;MULTICLASS&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateEvaluation&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateEvaluation&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the evaluation status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;Evaluation&lt;/code&gt; is created and ready for use, Amazon ML sets the status to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetEvaluation&lt;/code&gt; operation to check progress of the evaluation during the creation operation.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createEvaluationInput = new AmazonMachineLearning.CreateEvaluationInput(); // CreateEvaluationInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createEvaluation(xAmzTarget, createEvaluationInput, opts, (error, data, response) => {
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
 **createEvaluationInput** | [**CreateEvaluationInput**](CreateEvaluationInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateEvaluationOutput**](CreateEvaluationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMLModel

> CreateMLModelOutput createMLModel(xAmzTarget, createMLModelInput, opts)



&lt;p&gt;Creates a new &lt;code&gt;MLModel&lt;/code&gt; using the &lt;code&gt;DataSource&lt;/code&gt; and the recipe as information sources. &lt;/p&gt; &lt;p&gt;An &lt;code&gt;MLModel&lt;/code&gt; is nearly immutable. Users can update only the &lt;code&gt;MLModelName&lt;/code&gt; and the &lt;code&gt;ScoreThreshold&lt;/code&gt; in an &lt;code&gt;MLModel&lt;/code&gt; without creating a new &lt;code&gt;MLModel&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateMLModel&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateMLModel&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;MLModel&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;MLModel&lt;/code&gt; has been created and ready is for use, Amazon ML sets the status to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetMLModel&lt;/code&gt; operation to check the progress of the &lt;code&gt;MLModel&lt;/code&gt; during the creation operation.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateMLModel&lt;/code&gt; requires a &lt;code&gt;DataSource&lt;/code&gt; with computed statistics, which can be created by setting &lt;code&gt;ComputeStatistics&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt; in &lt;code&gt;CreateDataSourceFromRDS&lt;/code&gt;, &lt;code&gt;CreateDataSourceFromS3&lt;/code&gt;, or &lt;code&gt;CreateDataSourceFromRedshift&lt;/code&gt; operations. &lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createMLModelInput = new AmazonMachineLearning.CreateMLModelInput(); // CreateMLModelInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMLModel(xAmzTarget, createMLModelInput, opts, (error, data, response) => {
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
 **createMLModelInput** | [**CreateMLModelInput**](CreateMLModelInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMLModelOutput**](CreateMLModelOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRealtimeEndpoint

> CreateRealtimeEndpointOutput createRealtimeEndpoint(xAmzTarget, createRealtimeEndpointInput, opts)



Creates a real-time endpoint for the &lt;code&gt;MLModel&lt;/code&gt;. The endpoint contains the URI of the &lt;code&gt;MLModel&lt;/code&gt;; that is, the location to send real-time prediction requests for the specified &lt;code&gt;MLModel&lt;/code&gt;.

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createRealtimeEndpointInput = new AmazonMachineLearning.CreateRealtimeEndpointInput(); // CreateRealtimeEndpointInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRealtimeEndpoint(xAmzTarget, createRealtimeEndpointInput, opts, (error, data, response) => {
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
 **createRealtimeEndpointInput** | [**CreateRealtimeEndpointInput**](CreateRealtimeEndpointInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRealtimeEndpointOutput**](CreateRealtimeEndpointOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteBatchPrediction

> DeleteBatchPredictionOutput deleteBatchPrediction(xAmzTarget, deleteBatchPredictionInput, opts)



&lt;p&gt;Assigns the DELETED status to a &lt;code&gt;BatchPrediction&lt;/code&gt;, rendering it unusable.&lt;/p&gt; &lt;p&gt;After using the &lt;code&gt;DeleteBatchPrediction&lt;/code&gt; operation, you can use the &lt;a&gt;GetBatchPrediction&lt;/a&gt; operation to verify that the status of the &lt;code&gt;BatchPrediction&lt;/code&gt; changed to DELETED.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Caution:&lt;/b&gt; The result of the &lt;code&gt;DeleteBatchPrediction&lt;/code&gt; operation is irreversible.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteBatchPredictionInput = new AmazonMachineLearning.DeleteBatchPredictionInput(); // DeleteBatchPredictionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBatchPrediction(xAmzTarget, deleteBatchPredictionInput, opts, (error, data, response) => {
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
 **deleteBatchPredictionInput** | [**DeleteBatchPredictionInput**](DeleteBatchPredictionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteBatchPredictionOutput**](DeleteBatchPredictionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDataSource

> DeleteDataSourceOutput deleteDataSource(xAmzTarget, deleteDataSourceInput, opts)



&lt;p&gt;Assigns the DELETED status to a &lt;code&gt;DataSource&lt;/code&gt;, rendering it unusable.&lt;/p&gt; &lt;p&gt;After using the &lt;code&gt;DeleteDataSource&lt;/code&gt; operation, you can use the &lt;a&gt;GetDataSource&lt;/a&gt; operation to verify that the status of the &lt;code&gt;DataSource&lt;/code&gt; changed to DELETED.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Caution:&lt;/b&gt; The results of the &lt;code&gt;DeleteDataSource&lt;/code&gt; operation are irreversible.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteDataSourceInput = new AmazonMachineLearning.DeleteDataSourceInput(); // DeleteDataSourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDataSource(xAmzTarget, deleteDataSourceInput, opts, (error, data, response) => {
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
 **deleteDataSourceInput** | [**DeleteDataSourceInput**](DeleteDataSourceInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteDataSourceOutput**](DeleteDataSourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteEvaluation

> DeleteEvaluationOutput deleteEvaluation(xAmzTarget, deleteEvaluationInput, opts)



&lt;p&gt;Assigns the &lt;code&gt;DELETED&lt;/code&gt; status to an &lt;code&gt;Evaluation&lt;/code&gt;, rendering it unusable.&lt;/p&gt; &lt;p&gt;After invoking the &lt;code&gt;DeleteEvaluation&lt;/code&gt; operation, you can use the &lt;code&gt;GetEvaluation&lt;/code&gt; operation to verify that the status of the &lt;code&gt;Evaluation&lt;/code&gt; changed to &lt;code&gt;DELETED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Caution:&lt;/b&gt; The results of the &lt;code&gt;DeleteEvaluation&lt;/code&gt; operation are irreversible.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteEvaluationInput = new AmazonMachineLearning.DeleteEvaluationInput(); // DeleteEvaluationInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteEvaluation(xAmzTarget, deleteEvaluationInput, opts, (error, data, response) => {
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
 **deleteEvaluationInput** | [**DeleteEvaluationInput**](DeleteEvaluationInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteEvaluationOutput**](DeleteEvaluationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteMLModel

> DeleteMLModelOutput deleteMLModel(xAmzTarget, deleteMLModelInput, opts)



&lt;p&gt;Assigns the &lt;code&gt;DELETED&lt;/code&gt; status to an &lt;code&gt;MLModel&lt;/code&gt;, rendering it unusable.&lt;/p&gt; &lt;p&gt;After using the &lt;code&gt;DeleteMLModel&lt;/code&gt; operation, you can use the &lt;code&gt;GetMLModel&lt;/code&gt; operation to verify that the status of the &lt;code&gt;MLModel&lt;/code&gt; changed to DELETED.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Caution:&lt;/b&gt; The result of the &lt;code&gt;DeleteMLModel&lt;/code&gt; operation is irreversible.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteMLModelInput = new AmazonMachineLearning.DeleteMLModelInput(); // DeleteMLModelInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMLModel(xAmzTarget, deleteMLModelInput, opts, (error, data, response) => {
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
 **deleteMLModelInput** | [**DeleteMLModelInput**](DeleteMLModelInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteMLModelOutput**](DeleteMLModelOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteRealtimeEndpoint

> DeleteRealtimeEndpointOutput deleteRealtimeEndpoint(xAmzTarget, deleteRealtimeEndpointInput, opts)



Deletes a real time endpoint of an &lt;code&gt;MLModel&lt;/code&gt;.

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteRealtimeEndpointInput = new AmazonMachineLearning.DeleteRealtimeEndpointInput(); // DeleteRealtimeEndpointInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRealtimeEndpoint(xAmzTarget, deleteRealtimeEndpointInput, opts, (error, data, response) => {
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
 **deleteRealtimeEndpointInput** | [**DeleteRealtimeEndpointInput**](DeleteRealtimeEndpointInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteRealtimeEndpointOutput**](DeleteRealtimeEndpointOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTags

> DeleteTagsOutput deleteTags(xAmzTarget, deleteTagsInput, opts)



&lt;p&gt;Deletes the specified tags associated with an ML object. After this operation is complete, you can&#39;t recover deleted tags.&lt;/p&gt; &lt;p&gt;If you specify a tag that doesn&#39;t exist, Amazon ML ignores it.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteTagsInput = new AmazonMachineLearning.DeleteTagsInput(); // DeleteTagsInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteTags(xAmzTarget, deleteTagsInput, opts, (error, data, response) => {
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
 **deleteTagsInput** | [**DeleteTagsInput**](DeleteTagsInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteTagsOutput**](DeleteTagsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeBatchPredictions

> DescribeBatchPredictionsOutput describeBatchPredictions(xAmzTarget, describeBatchPredictionsInput, opts)



Returns a list of &lt;code&gt;BatchPrediction&lt;/code&gt; operations that match the search criteria in the request.

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeBatchPredictionsInput = new AmazonMachineLearning.DescribeBatchPredictionsInput(); // DescribeBatchPredictionsInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'limit': "limit_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.describeBatchPredictions(xAmzTarget, describeBatchPredictionsInput, opts, (error, data, response) => {
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
 **describeBatchPredictionsInput** | [**DescribeBatchPredictionsInput**](DescribeBatchPredictionsInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **limit** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**DescribeBatchPredictionsOutput**](DescribeBatchPredictionsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeDataSources

> DescribeDataSourcesOutput describeDataSources(xAmzTarget, describeDataSourcesInput, opts)



Returns a list of &lt;code&gt;DataSource&lt;/code&gt; that match the search criteria in the request.

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeDataSourcesInput = new AmazonMachineLearning.DescribeDataSourcesInput(); // DescribeDataSourcesInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'limit': "limit_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.describeDataSources(xAmzTarget, describeDataSourcesInput, opts, (error, data, response) => {
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
 **describeDataSourcesInput** | [**DescribeDataSourcesInput**](DescribeDataSourcesInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **limit** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**DescribeDataSourcesOutput**](DescribeDataSourcesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeEvaluations

> DescribeEvaluationsOutput describeEvaluations(xAmzTarget, describeEvaluationsInput, opts)



Returns a list of &lt;code&gt;DescribeEvaluations&lt;/code&gt; that match the search criteria in the request.

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeEvaluationsInput = new AmazonMachineLearning.DescribeEvaluationsInput(); // DescribeEvaluationsInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'limit': "limit_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.describeEvaluations(xAmzTarget, describeEvaluationsInput, opts, (error, data, response) => {
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
 **describeEvaluationsInput** | [**DescribeEvaluationsInput**](DescribeEvaluationsInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **limit** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**DescribeEvaluationsOutput**](DescribeEvaluationsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeMLModels

> DescribeMLModelsOutput describeMLModels(xAmzTarget, describeMLModelsInput, opts)



Returns a list of &lt;code&gt;MLModel&lt;/code&gt; that match the search criteria in the request.

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeMLModelsInput = new AmazonMachineLearning.DescribeMLModelsInput(); // DescribeMLModelsInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'limit': "limit_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.describeMLModels(xAmzTarget, describeMLModelsInput, opts, (error, data, response) => {
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
 **describeMLModelsInput** | [**DescribeMLModelsInput**](DescribeMLModelsInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **limit** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**DescribeMLModelsOutput**](DescribeMLModelsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeTags

> DescribeTagsOutput describeTags(xAmzTarget, describeTagsInput, opts)



Describes one or more of the tags for your Amazon ML object.

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeTagsInput = new AmazonMachineLearning.DescribeTagsInput(); // DescribeTagsInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeTags(xAmzTarget, describeTagsInput, opts, (error, data, response) => {
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
 **describeTagsInput** | [**DescribeTagsInput**](DescribeTagsInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeTagsOutput**](DescribeTagsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getBatchPrediction

> GetBatchPredictionOutput getBatchPrediction(xAmzTarget, getBatchPredictionInput, opts)



Returns a &lt;code&gt;BatchPrediction&lt;/code&gt; that includes detailed metadata, status, and data file information for a &lt;code&gt;Batch Prediction&lt;/code&gt; request.

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getBatchPredictionInput = new AmazonMachineLearning.GetBatchPredictionInput(); // GetBatchPredictionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBatchPrediction(xAmzTarget, getBatchPredictionInput, opts, (error, data, response) => {
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
 **getBatchPredictionInput** | [**GetBatchPredictionInput**](GetBatchPredictionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBatchPredictionOutput**](GetBatchPredictionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDataSource

> GetDataSourceOutput getDataSource(xAmzTarget, getDataSourceInput, opts)



&lt;p&gt;Returns a &lt;code&gt;DataSource&lt;/code&gt; that includes metadata and data file information, as well as the current status of the &lt;code&gt;DataSource&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetDataSource&lt;/code&gt; provides results in normal or verbose format. The verbose format adds the schema description and the list of files pointed to by the DataSource to the normal format.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getDataSourceInput = new AmazonMachineLearning.GetDataSourceInput(); // GetDataSourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDataSource(xAmzTarget, getDataSourceInput, opts, (error, data, response) => {
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
 **getDataSourceInput** | [**GetDataSourceInput**](GetDataSourceInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDataSourceOutput**](GetDataSourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getEvaluation

> GetEvaluationOutput getEvaluation(xAmzTarget, getEvaluationInput, opts)



Returns an &lt;code&gt;Evaluation&lt;/code&gt; that includes metadata as well as the current status of the &lt;code&gt;Evaluation&lt;/code&gt;.

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getEvaluationInput = new AmazonMachineLearning.GetEvaluationInput(); // GetEvaluationInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEvaluation(xAmzTarget, getEvaluationInput, opts, (error, data, response) => {
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
 **getEvaluationInput** | [**GetEvaluationInput**](GetEvaluationInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEvaluationOutput**](GetEvaluationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getMLModel

> GetMLModelOutput getMLModel(xAmzTarget, getMLModelInput, opts)



&lt;p&gt;Returns an &lt;code&gt;MLModel&lt;/code&gt; that includes detailed metadata, data source information, and the current status of the &lt;code&gt;MLModel&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetMLModel&lt;/code&gt; provides results in normal or verbose format. &lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getMLModelInput = new AmazonMachineLearning.GetMLModelInput(); // GetMLModelInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMLModel(xAmzTarget, getMLModelInput, opts, (error, data, response) => {
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
 **getMLModelInput** | [**GetMLModelInput**](GetMLModelInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMLModelOutput**](GetMLModelOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## predict

> PredictOutput predict(xAmzTarget, predictInput, opts)



&lt;p&gt;Generates a prediction for the observation using the specified &lt;code&gt;ML Model&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Note:&lt;/b&gt; Not all response parameters will be populated. Whether a response parameter is populated depends on the type of model requested.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let predictInput = new AmazonMachineLearning.PredictInput(); // PredictInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.predict(xAmzTarget, predictInput, opts, (error, data, response) => {
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
 **predictInput** | [**PredictInput**](PredictInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PredictOutput**](PredictOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBatchPrediction

> UpdateBatchPredictionOutput updateBatchPrediction(xAmzTarget, updateBatchPredictionInput, opts)



&lt;p&gt;Updates the &lt;code&gt;BatchPredictionName&lt;/code&gt; of a &lt;code&gt;BatchPrediction&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetBatchPrediction&lt;/code&gt; operation to view the contents of the updated data element.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateBatchPredictionInput = new AmazonMachineLearning.UpdateBatchPredictionInput(); // UpdateBatchPredictionInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBatchPrediction(xAmzTarget, updateBatchPredictionInput, opts, (error, data, response) => {
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
 **updateBatchPredictionInput** | [**UpdateBatchPredictionInput**](UpdateBatchPredictionInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBatchPredictionOutput**](UpdateBatchPredictionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDataSource

> UpdateDataSourceOutput updateDataSource(xAmzTarget, updateDataSourceInput, opts)



&lt;p&gt;Updates the &lt;code&gt;DataSourceName&lt;/code&gt; of a &lt;code&gt;DataSource&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetDataSource&lt;/code&gt; operation to view the contents of the updated data element.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateDataSourceInput = new AmazonMachineLearning.UpdateDataSourceInput(); // UpdateDataSourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDataSource(xAmzTarget, updateDataSourceInput, opts, (error, data, response) => {
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
 **updateDataSourceInput** | [**UpdateDataSourceInput**](UpdateDataSourceInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateDataSourceOutput**](UpdateDataSourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEvaluation

> UpdateEvaluationOutput updateEvaluation(xAmzTarget, updateEvaluationInput, opts)



&lt;p&gt;Updates the &lt;code&gt;EvaluationName&lt;/code&gt; of an &lt;code&gt;Evaluation&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetEvaluation&lt;/code&gt; operation to view the contents of the updated data element.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateEvaluationInput = new AmazonMachineLearning.UpdateEvaluationInput(); // UpdateEvaluationInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateEvaluation(xAmzTarget, updateEvaluationInput, opts, (error, data, response) => {
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
 **updateEvaluationInput** | [**UpdateEvaluationInput**](UpdateEvaluationInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateEvaluationOutput**](UpdateEvaluationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMLModel

> UpdateMLModelOutput updateMLModel(xAmzTarget, updateMLModelInput, opts)



&lt;p&gt;Updates the &lt;code&gt;MLModelName&lt;/code&gt; and the &lt;code&gt;ScoreThreshold&lt;/code&gt; of an &lt;code&gt;MLModel&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetMLModel&lt;/code&gt; operation to view the contents of the updated data element.&lt;/p&gt;

### Example

```javascript
import AmazonMachineLearning from 'amazon_machine_learning';
let defaultClient = AmazonMachineLearning.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMachineLearning.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateMLModelInput = new AmazonMachineLearning.UpdateMLModelInput(); // UpdateMLModelInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateMLModel(xAmzTarget, updateMLModelInput, opts, (error, data, response) => {
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
 **updateMLModelInput** | [**UpdateMLModelInput**](UpdateMLModelInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateMLModelOutput**](UpdateMLModelOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

