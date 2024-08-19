# DefaultApi

All URIs are relative to *http://machinelearning.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addTags**](DefaultApi.md#addTags) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.AddTags |  |
| [**createBatchPrediction**](DefaultApi.md#createBatchPrediction) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.CreateBatchPrediction |  |
| [**createDataSourceFromRDS**](DefaultApi.md#createDataSourceFromRDS) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.CreateDataSourceFromRDS |  |
| [**createDataSourceFromRedshift**](DefaultApi.md#createDataSourceFromRedshift) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.CreateDataSourceFromRedshift |  |
| [**createDataSourceFromS3**](DefaultApi.md#createDataSourceFromS3) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.CreateDataSourceFromS3 |  |
| [**createEvaluation**](DefaultApi.md#createEvaluation) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.CreateEvaluation |  |
| [**createMLModel**](DefaultApi.md#createMLModel) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.CreateMLModel |  |
| [**createRealtimeEndpoint**](DefaultApi.md#createRealtimeEndpoint) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.CreateRealtimeEndpoint |  |
| [**deleteBatchPrediction**](DefaultApi.md#deleteBatchPrediction) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DeleteBatchPrediction |  |
| [**deleteDataSource**](DefaultApi.md#deleteDataSource) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DeleteDataSource |  |
| [**deleteEvaluation**](DefaultApi.md#deleteEvaluation) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DeleteEvaluation |  |
| [**deleteMLModel**](DefaultApi.md#deleteMLModel) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DeleteMLModel |  |
| [**deleteRealtimeEndpoint**](DefaultApi.md#deleteRealtimeEndpoint) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DeleteRealtimeEndpoint |  |
| [**deleteTags**](DefaultApi.md#deleteTags) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DeleteTags |  |
| [**describeBatchPredictions**](DefaultApi.md#describeBatchPredictions) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DescribeBatchPredictions |  |
| [**describeDataSources**](DefaultApi.md#describeDataSources) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DescribeDataSources |  |
| [**describeEvaluations**](DefaultApi.md#describeEvaluations) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DescribeEvaluations |  |
| [**describeMLModels**](DefaultApi.md#describeMLModels) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DescribeMLModels |  |
| [**describeTags**](DefaultApi.md#describeTags) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.DescribeTags |  |
| [**getBatchPrediction**](DefaultApi.md#getBatchPrediction) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.GetBatchPrediction |  |
| [**getDataSource**](DefaultApi.md#getDataSource) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.GetDataSource |  |
| [**getEvaluation**](DefaultApi.md#getEvaluation) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.GetEvaluation |  |
| [**getMLModel**](DefaultApi.md#getMLModel) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.GetMLModel |  |
| [**predict**](DefaultApi.md#predict) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.Predict |  |
| [**updateBatchPrediction**](DefaultApi.md#updateBatchPrediction) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.UpdateBatchPrediction |  |
| [**updateDataSource**](DefaultApi.md#updateDataSource) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.UpdateDataSource |  |
| [**updateEvaluation**](DefaultApi.md#updateEvaluation) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.UpdateEvaluation |  |
| [**updateMLModel**](DefaultApi.md#updateMLModel) | **POST** /#X-Amz-Target&#x3D;AmazonML_20141212.UpdateMLModel |  |


<a id="addTags"></a>
# **addTags**
> AddTagsOutput addTags(xAmzTarget, addTagsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Adds one or more tags to an object, up to a limit of 10. Each tag consists of a key and an optional value. If you add a tag using a key that is already associated with the ML object, &lt;code&gt;AddTags&lt;/code&gt; updates the tag&#39;s value.

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.AddTags"; // String | 
    AddTagsInput addTagsInput = new AddTagsInput(); // AddTagsInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AddTagsOutput result = apiInstance.addTags(xAmzTarget, addTagsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addTags");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.AddTags] |
| **addTagsInput** | [**AddTagsInput**](AddTagsInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AddTagsOutput**](AddTagsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | InvalidTagException |  -  |
| **482** | TagLimitExceededException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="createBatchPrediction"></a>
# **createBatchPrediction**
> CreateBatchPredictionOutput createBatchPrediction(xAmzTarget, createBatchPredictionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Generates predictions for a group of observations. The observations to process exist in one or more data files referenced by a &lt;code&gt;DataSource&lt;/code&gt;. This operation creates a new &lt;code&gt;BatchPrediction&lt;/code&gt;, and uses an &lt;code&gt;MLModel&lt;/code&gt; and the data files referenced by the &lt;code&gt;DataSource&lt;/code&gt; as information sources. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateBatchPrediction&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateBatchPrediction&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;BatchPrediction&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;BatchPrediction&lt;/code&gt; completes, Amazon ML sets the status to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;You can poll for status updates by using the &lt;a&gt;GetBatchPrediction&lt;/a&gt; operation and checking the &lt;code&gt;Status&lt;/code&gt; parameter of the result. After the &lt;code&gt;COMPLETED&lt;/code&gt; status appears, the results are available in the location specified by the &lt;code&gt;OutputUri&lt;/code&gt; parameter.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.CreateBatchPrediction"; // String | 
    CreateBatchPredictionInput createBatchPredictionInput = new CreateBatchPredictionInput(); // CreateBatchPredictionInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateBatchPredictionOutput result = apiInstance.createBatchPrediction(xAmzTarget, createBatchPredictionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createBatchPrediction");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.CreateBatchPrediction] |
| **createBatchPredictionInput** | [**CreateBatchPredictionInput**](CreateBatchPredictionInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateBatchPredictionOutput**](CreateBatchPredictionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | InternalServerException |  -  |
| **482** | IdempotentParameterMismatchException |  -  |

<a id="createDataSourceFromRDS"></a>
# **createDataSourceFromRDS**
> CreateDataSourceFromRDSOutput createDataSourceFromRDS(xAmzTarget, createDataSourceFromRDSInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a &lt;code&gt;DataSource&lt;/code&gt; object from an &lt;a href&#x3D;\&quot;http://aws.amazon.com/rds/\&quot;&gt; Amazon Relational Database Service&lt;/a&gt; (Amazon RDS). A &lt;code&gt;DataSource&lt;/code&gt; references data that can be used to perform &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateDataSourceFromRDS&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateDataSourceFromRDS&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;DataSource&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;DataSource&lt;/code&gt; is created and ready for use, Amazon ML sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;code&gt;DataSource&lt;/code&gt; in the &lt;code&gt;COMPLETED&lt;/code&gt; or &lt;code&gt;PENDING&lt;/code&gt; state can be used only to perform &lt;code&gt;&amp;gt;CreateMLModel&lt;/code&gt;&amp;gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations. &lt;/p&gt; &lt;p&gt; If Amazon ML cannot accept the input source, it sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;FAILED&lt;/code&gt; and includes an error message in the &lt;code&gt;Message&lt;/code&gt; attribute of the &lt;code&gt;GetDataSource&lt;/code&gt; operation response. &lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.CreateDataSourceFromRDS"; // String | 
    CreateDataSourceFromRDSInput createDataSourceFromRDSInput = new CreateDataSourceFromRDSInput(); // CreateDataSourceFromRDSInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateDataSourceFromRDSOutput result = apiInstance.createDataSourceFromRDS(xAmzTarget, createDataSourceFromRDSInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createDataSourceFromRDS");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.CreateDataSourceFromRDS] |
| **createDataSourceFromRDSInput** | [**CreateDataSourceFromRDSInput**](CreateDataSourceFromRDSInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateDataSourceFromRDSOutput**](CreateDataSourceFromRDSOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | InternalServerException |  -  |
| **482** | IdempotentParameterMismatchException |  -  |

<a id="createDataSourceFromRedshift"></a>
# **createDataSourceFromRedshift**
> CreateDataSourceFromRedshiftOutput createDataSourceFromRedshift(xAmzTarget, createDataSourceFromRedshiftInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a &lt;code&gt;DataSource&lt;/code&gt; from a database hosted on an Amazon Redshift cluster. A &lt;code&gt;DataSource&lt;/code&gt; references data that can be used to perform either &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateDataSourceFromRedshift&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateDataSourceFromRedshift&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;DataSource&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;DataSource&lt;/code&gt; is created and ready for use, Amazon ML sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;code&gt;DataSource&lt;/code&gt; in &lt;code&gt;COMPLETED&lt;/code&gt; or &lt;code&gt;PENDING&lt;/code&gt; states can be used to perform only &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations. &lt;/p&gt; &lt;p&gt; If Amazon ML can&#39;t accept the input source, it sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;FAILED&lt;/code&gt; and includes an error message in the &lt;code&gt;Message&lt;/code&gt; attribute of the &lt;code&gt;GetDataSource&lt;/code&gt; operation response. &lt;/p&gt; &lt;p&gt;The observations should be contained in the database hosted on an Amazon Redshift cluster and should be specified by a &lt;code&gt;SelectSqlQuery&lt;/code&gt; query. Amazon ML executes an &lt;code&gt;Unload&lt;/code&gt; command in Amazon Redshift to transfer the result set of the &lt;code&gt;SelectSqlQuery&lt;/code&gt; query to &lt;code&gt;S3StagingLocation&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;After the &lt;code&gt;DataSource&lt;/code&gt; has been created, it&#39;s ready for use in evaluations and batch predictions. If you plan to use the &lt;code&gt;DataSource&lt;/code&gt; to train an &lt;code&gt;MLModel&lt;/code&gt;, the &lt;code&gt;DataSource&lt;/code&gt; also requires a recipe. A recipe describes how each input variable will be used in training an &lt;code&gt;MLModel&lt;/code&gt;. Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.&lt;/p&gt; &lt;p&gt;You can&#39;t change an existing datasource, but you can copy and modify the settings from an existing Amazon Redshift datasource to create a new datasource. To do so, call &lt;code&gt;GetDataSource&lt;/code&gt; for an existing datasource and copy the values to a &lt;code&gt;CreateDataSource&lt;/code&gt; call. Change the settings that you want to change and make sure that all required fields have the appropriate values.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.CreateDataSourceFromRedshift"; // String | 
    CreateDataSourceFromRedshiftInput createDataSourceFromRedshiftInput = new CreateDataSourceFromRedshiftInput(); // CreateDataSourceFromRedshiftInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateDataSourceFromRedshiftOutput result = apiInstance.createDataSourceFromRedshift(xAmzTarget, createDataSourceFromRedshiftInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createDataSourceFromRedshift");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.CreateDataSourceFromRedshift] |
| **createDataSourceFromRedshiftInput** | [**CreateDataSourceFromRedshiftInput**](CreateDataSourceFromRedshiftInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateDataSourceFromRedshiftOutput**](CreateDataSourceFromRedshiftOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | InternalServerException |  -  |
| **482** | IdempotentParameterMismatchException |  -  |

<a id="createDataSourceFromS3"></a>
# **createDataSourceFromS3**
> CreateDataSourceFromS3Output createDataSourceFromS3(xAmzTarget, createDataSourceFromS3Input, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a &lt;code&gt;DataSource&lt;/code&gt; object. A &lt;code&gt;DataSource&lt;/code&gt; references data that can be used to perform &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateDataSourceFromS3&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateDataSourceFromS3&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;DataSource&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;DataSource&lt;/code&gt; has been created and is ready for use, Amazon ML sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;code&gt;DataSource&lt;/code&gt; in the &lt;code&gt;COMPLETED&lt;/code&gt; or &lt;code&gt;PENDING&lt;/code&gt; state can be used to perform only &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt; or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations. &lt;/p&gt; &lt;p&gt; If Amazon ML can&#39;t accept the input source, it sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;FAILED&lt;/code&gt; and includes an error message in the &lt;code&gt;Message&lt;/code&gt; attribute of the &lt;code&gt;GetDataSource&lt;/code&gt; operation response. &lt;/p&gt; &lt;p&gt;The observation data used in a &lt;code&gt;DataSource&lt;/code&gt; should be ready to use; that is, it should have a consistent structure, and missing data values should be kept to a minimum. The observation data must reside in one or more .csv files in an Amazon Simple Storage Service (Amazon S3) location, along with a schema that describes the data items by name and type. The same schema must be used for all of the data files referenced by the &lt;code&gt;DataSource&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;After the &lt;code&gt;DataSource&lt;/code&gt; has been created, it&#39;s ready to use in evaluations and batch predictions. If you plan to use the &lt;code&gt;DataSource&lt;/code&gt; to train an &lt;code&gt;MLModel&lt;/code&gt;, the &lt;code&gt;DataSource&lt;/code&gt; also needs a recipe. A recipe describes how each input variable will be used in training an &lt;code&gt;MLModel&lt;/code&gt;. Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.CreateDataSourceFromS3"; // String | 
    CreateDataSourceFromS3Input createDataSourceFromS3Input = new CreateDataSourceFromS3Input(); // CreateDataSourceFromS3Input | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateDataSourceFromS3Output result = apiInstance.createDataSourceFromS3(xAmzTarget, createDataSourceFromS3Input, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createDataSourceFromS3");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.CreateDataSourceFromS3] |
| **createDataSourceFromS3Input** | [**CreateDataSourceFromS3Input**](CreateDataSourceFromS3Input.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateDataSourceFromS3Output**](CreateDataSourceFromS3Output.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | InternalServerException |  -  |
| **482** | IdempotentParameterMismatchException |  -  |

<a id="createEvaluation"></a>
# **createEvaluation**
> CreateEvaluationOutput createEvaluation(xAmzTarget, createEvaluationInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new &lt;code&gt;Evaluation&lt;/code&gt; of an &lt;code&gt;MLModel&lt;/code&gt;. An &lt;code&gt;MLModel&lt;/code&gt; is evaluated on a set of observations associated to a &lt;code&gt;DataSource&lt;/code&gt;. Like a &lt;code&gt;DataSource&lt;/code&gt; for an &lt;code&gt;MLModel&lt;/code&gt;, the &lt;code&gt;DataSource&lt;/code&gt; for an &lt;code&gt;Evaluation&lt;/code&gt; contains values for the &lt;code&gt;Target Variable&lt;/code&gt;. The &lt;code&gt;Evaluation&lt;/code&gt; compares the predicted result for each observation to the actual outcome and provides a summary so that you know how effective the &lt;code&gt;MLModel&lt;/code&gt; functions on the test data. Evaluation generates a relevant performance metric, such as BinaryAUC, RegressionRMSE or MulticlassAvgFScore based on the corresponding &lt;code&gt;MLModelType&lt;/code&gt;: &lt;code&gt;BINARY&lt;/code&gt;, &lt;code&gt;REGRESSION&lt;/code&gt; or &lt;code&gt;MULTICLASS&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateEvaluation&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateEvaluation&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the evaluation status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;Evaluation&lt;/code&gt; is created and ready for use, Amazon ML sets the status to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetEvaluation&lt;/code&gt; operation to check progress of the evaluation during the creation operation.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.CreateEvaluation"; // String | 
    CreateEvaluationInput createEvaluationInput = new CreateEvaluationInput(); // CreateEvaluationInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateEvaluationOutput result = apiInstance.createEvaluation(xAmzTarget, createEvaluationInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createEvaluation");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.CreateEvaluation] |
| **createEvaluationInput** | [**CreateEvaluationInput**](CreateEvaluationInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateEvaluationOutput**](CreateEvaluationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | InternalServerException |  -  |
| **482** | IdempotentParameterMismatchException |  -  |

<a id="createMLModel"></a>
# **createMLModel**
> CreateMLModelOutput createMLModel(xAmzTarget, createMLModelInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new &lt;code&gt;MLModel&lt;/code&gt; using the &lt;code&gt;DataSource&lt;/code&gt; and the recipe as information sources. &lt;/p&gt; &lt;p&gt;An &lt;code&gt;MLModel&lt;/code&gt; is nearly immutable. Users can update only the &lt;code&gt;MLModelName&lt;/code&gt; and the &lt;code&gt;ScoreThreshold&lt;/code&gt; in an &lt;code&gt;MLModel&lt;/code&gt; without creating a new &lt;code&gt;MLModel&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateMLModel&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateMLModel&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;MLModel&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;MLModel&lt;/code&gt; has been created and ready is for use, Amazon ML sets the status to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetMLModel&lt;/code&gt; operation to check the progress of the &lt;code&gt;MLModel&lt;/code&gt; during the creation operation.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateMLModel&lt;/code&gt; requires a &lt;code&gt;DataSource&lt;/code&gt; with computed statistics, which can be created by setting &lt;code&gt;ComputeStatistics&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt; in &lt;code&gt;CreateDataSourceFromRDS&lt;/code&gt;, &lt;code&gt;CreateDataSourceFromS3&lt;/code&gt;, or &lt;code&gt;CreateDataSourceFromRedshift&lt;/code&gt; operations. &lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.CreateMLModel"; // String | 
    CreateMLModelInput createMLModelInput = new CreateMLModelInput(); // CreateMLModelInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateMLModelOutput result = apiInstance.createMLModel(xAmzTarget, createMLModelInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createMLModel");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.CreateMLModel] |
| **createMLModelInput** | [**CreateMLModelInput**](CreateMLModelInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateMLModelOutput**](CreateMLModelOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | InternalServerException |  -  |
| **482** | IdempotentParameterMismatchException |  -  |

<a id="createRealtimeEndpoint"></a>
# **createRealtimeEndpoint**
> CreateRealtimeEndpointOutput createRealtimeEndpoint(xAmzTarget, createRealtimeEndpointInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a real-time endpoint for the &lt;code&gt;MLModel&lt;/code&gt;. The endpoint contains the URI of the &lt;code&gt;MLModel&lt;/code&gt;; that is, the location to send real-time prediction requests for the specified &lt;code&gt;MLModel&lt;/code&gt;.

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.CreateRealtimeEndpoint"; // String | 
    CreateRealtimeEndpointInput createRealtimeEndpointInput = new CreateRealtimeEndpointInput(); // CreateRealtimeEndpointInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateRealtimeEndpointOutput result = apiInstance.createRealtimeEndpoint(xAmzTarget, createRealtimeEndpointInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createRealtimeEndpoint");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.CreateRealtimeEndpoint] |
| **createRealtimeEndpointInput** | [**CreateRealtimeEndpointInput**](CreateRealtimeEndpointInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateRealtimeEndpointOutput**](CreateRealtimeEndpointOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="deleteBatchPrediction"></a>
# **deleteBatchPrediction**
> DeleteBatchPredictionOutput deleteBatchPrediction(xAmzTarget, deleteBatchPredictionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Assigns the DELETED status to a &lt;code&gt;BatchPrediction&lt;/code&gt;, rendering it unusable.&lt;/p&gt; &lt;p&gt;After using the &lt;code&gt;DeleteBatchPrediction&lt;/code&gt; operation, you can use the &lt;a&gt;GetBatchPrediction&lt;/a&gt; operation to verify that the status of the &lt;code&gt;BatchPrediction&lt;/code&gt; changed to DELETED.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Caution:&lt;/b&gt; The result of the &lt;code&gt;DeleteBatchPrediction&lt;/code&gt; operation is irreversible.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.DeleteBatchPrediction"; // String | 
    DeleteBatchPredictionInput deleteBatchPredictionInput = new DeleteBatchPredictionInput(); // DeleteBatchPredictionInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteBatchPredictionOutput result = apiInstance.deleteBatchPrediction(xAmzTarget, deleteBatchPredictionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteBatchPrediction");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.DeleteBatchPrediction] |
| **deleteBatchPredictionInput** | [**DeleteBatchPredictionInput**](DeleteBatchPredictionInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteBatchPredictionOutput**](DeleteBatchPredictionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="deleteDataSource"></a>
# **deleteDataSource**
> DeleteDataSourceOutput deleteDataSource(xAmzTarget, deleteDataSourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Assigns the DELETED status to a &lt;code&gt;DataSource&lt;/code&gt;, rendering it unusable.&lt;/p&gt; &lt;p&gt;After using the &lt;code&gt;DeleteDataSource&lt;/code&gt; operation, you can use the &lt;a&gt;GetDataSource&lt;/a&gt; operation to verify that the status of the &lt;code&gt;DataSource&lt;/code&gt; changed to DELETED.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Caution:&lt;/b&gt; The results of the &lt;code&gt;DeleteDataSource&lt;/code&gt; operation are irreversible.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.DeleteDataSource"; // String | 
    DeleteDataSourceInput deleteDataSourceInput = new DeleteDataSourceInput(); // DeleteDataSourceInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteDataSourceOutput result = apiInstance.deleteDataSource(xAmzTarget, deleteDataSourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDataSource");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.DeleteDataSource] |
| **deleteDataSourceInput** | [**DeleteDataSourceInput**](DeleteDataSourceInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteDataSourceOutput**](DeleteDataSourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="deleteEvaluation"></a>
# **deleteEvaluation**
> DeleteEvaluationOutput deleteEvaluation(xAmzTarget, deleteEvaluationInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Assigns the &lt;code&gt;DELETED&lt;/code&gt; status to an &lt;code&gt;Evaluation&lt;/code&gt;, rendering it unusable.&lt;/p&gt; &lt;p&gt;After invoking the &lt;code&gt;DeleteEvaluation&lt;/code&gt; operation, you can use the &lt;code&gt;GetEvaluation&lt;/code&gt; operation to verify that the status of the &lt;code&gt;Evaluation&lt;/code&gt; changed to &lt;code&gt;DELETED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Caution:&lt;/b&gt; The results of the &lt;code&gt;DeleteEvaluation&lt;/code&gt; operation are irreversible.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.DeleteEvaluation"; // String | 
    DeleteEvaluationInput deleteEvaluationInput = new DeleteEvaluationInput(); // DeleteEvaluationInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteEvaluationOutput result = apiInstance.deleteEvaluation(xAmzTarget, deleteEvaluationInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteEvaluation");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.DeleteEvaluation] |
| **deleteEvaluationInput** | [**DeleteEvaluationInput**](DeleteEvaluationInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteEvaluationOutput**](DeleteEvaluationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="deleteMLModel"></a>
# **deleteMLModel**
> DeleteMLModelOutput deleteMLModel(xAmzTarget, deleteMLModelInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Assigns the &lt;code&gt;DELETED&lt;/code&gt; status to an &lt;code&gt;MLModel&lt;/code&gt;, rendering it unusable.&lt;/p&gt; &lt;p&gt;After using the &lt;code&gt;DeleteMLModel&lt;/code&gt; operation, you can use the &lt;code&gt;GetMLModel&lt;/code&gt; operation to verify that the status of the &lt;code&gt;MLModel&lt;/code&gt; changed to DELETED.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Caution:&lt;/b&gt; The result of the &lt;code&gt;DeleteMLModel&lt;/code&gt; operation is irreversible.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.DeleteMLModel"; // String | 
    DeleteMLModelInput deleteMLModelInput = new DeleteMLModelInput(); // DeleteMLModelInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteMLModelOutput result = apiInstance.deleteMLModel(xAmzTarget, deleteMLModelInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteMLModel");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.DeleteMLModel] |
| **deleteMLModelInput** | [**DeleteMLModelInput**](DeleteMLModelInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteMLModelOutput**](DeleteMLModelOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="deleteRealtimeEndpoint"></a>
# **deleteRealtimeEndpoint**
> DeleteRealtimeEndpointOutput deleteRealtimeEndpoint(xAmzTarget, deleteRealtimeEndpointInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes a real time endpoint of an &lt;code&gt;MLModel&lt;/code&gt;.

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.DeleteRealtimeEndpoint"; // String | 
    DeleteRealtimeEndpointInput deleteRealtimeEndpointInput = new DeleteRealtimeEndpointInput(); // DeleteRealtimeEndpointInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteRealtimeEndpointOutput result = apiInstance.deleteRealtimeEndpoint(xAmzTarget, deleteRealtimeEndpointInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteRealtimeEndpoint");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.DeleteRealtimeEndpoint] |
| **deleteRealtimeEndpointInput** | [**DeleteRealtimeEndpointInput**](DeleteRealtimeEndpointInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteRealtimeEndpointOutput**](DeleteRealtimeEndpointOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="deleteTags"></a>
# **deleteTags**
> DeleteTagsOutput deleteTags(xAmzTarget, deleteTagsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the specified tags associated with an ML object. After this operation is complete, you can&#39;t recover deleted tags.&lt;/p&gt; &lt;p&gt;If you specify a tag that doesn&#39;t exist, Amazon ML ignores it.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.DeleteTags"; // String | 
    DeleteTagsInput deleteTagsInput = new DeleteTagsInput(); // DeleteTagsInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteTagsOutput result = apiInstance.deleteTags(xAmzTarget, deleteTagsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteTags");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.DeleteTags] |
| **deleteTagsInput** | [**DeleteTagsInput**](DeleteTagsInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteTagsOutput**](DeleteTagsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | InvalidTagException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalServerException |  -  |

<a id="describeBatchPredictions"></a>
# **describeBatchPredictions**
> DescribeBatchPredictionsOutput describeBatchPredictions(xAmzTarget, describeBatchPredictionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken)



Returns a list of &lt;code&gt;BatchPrediction&lt;/code&gt; operations that match the search criteria in the request.

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.DescribeBatchPredictions"; // String | 
    DescribeBatchPredictionsInput describeBatchPredictionsInput = new DescribeBatchPredictionsInput(); // DescribeBatchPredictionsInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String limit = "limit_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      DescribeBatchPredictionsOutput result = apiInstance.describeBatchPredictions(xAmzTarget, describeBatchPredictionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeBatchPredictions");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.DescribeBatchPredictions] |
| **describeBatchPredictionsInput** | [**DescribeBatchPredictionsInput**](DescribeBatchPredictionsInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**DescribeBatchPredictionsOutput**](DescribeBatchPredictionsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | InternalServerException |  -  |

<a id="describeDataSources"></a>
# **describeDataSources**
> DescribeDataSourcesOutput describeDataSources(xAmzTarget, describeDataSourcesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken)



Returns a list of &lt;code&gt;DataSource&lt;/code&gt; that match the search criteria in the request.

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.DescribeDataSources"; // String | 
    DescribeDataSourcesInput describeDataSourcesInput = new DescribeDataSourcesInput(); // DescribeDataSourcesInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String limit = "limit_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      DescribeDataSourcesOutput result = apiInstance.describeDataSources(xAmzTarget, describeDataSourcesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeDataSources");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.DescribeDataSources] |
| **describeDataSourcesInput** | [**DescribeDataSourcesInput**](DescribeDataSourcesInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**DescribeDataSourcesOutput**](DescribeDataSourcesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | InternalServerException |  -  |

<a id="describeEvaluations"></a>
# **describeEvaluations**
> DescribeEvaluationsOutput describeEvaluations(xAmzTarget, describeEvaluationsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken)



Returns a list of &lt;code&gt;DescribeEvaluations&lt;/code&gt; that match the search criteria in the request.

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.DescribeEvaluations"; // String | 
    DescribeEvaluationsInput describeEvaluationsInput = new DescribeEvaluationsInput(); // DescribeEvaluationsInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String limit = "limit_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      DescribeEvaluationsOutput result = apiInstance.describeEvaluations(xAmzTarget, describeEvaluationsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeEvaluations");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.DescribeEvaluations] |
| **describeEvaluationsInput** | [**DescribeEvaluationsInput**](DescribeEvaluationsInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**DescribeEvaluationsOutput**](DescribeEvaluationsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | InternalServerException |  -  |

<a id="describeMLModels"></a>
# **describeMLModels**
> DescribeMLModelsOutput describeMLModels(xAmzTarget, describeMLModelsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken)



Returns a list of &lt;code&gt;MLModel&lt;/code&gt; that match the search criteria in the request.

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.DescribeMLModels"; // String | 
    DescribeMLModelsInput describeMLModelsInput = new DescribeMLModelsInput(); // DescribeMLModelsInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String limit = "limit_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      DescribeMLModelsOutput result = apiInstance.describeMLModels(xAmzTarget, describeMLModelsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeMLModels");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.DescribeMLModels] |
| **describeMLModelsInput** | [**DescribeMLModelsInput**](DescribeMLModelsInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**DescribeMLModelsOutput**](DescribeMLModelsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | InternalServerException |  -  |

<a id="describeTags"></a>
# **describeTags**
> DescribeTagsOutput describeTags(xAmzTarget, describeTagsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Describes one or more of the tags for your Amazon ML object.

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.DescribeTags"; // String | 
    DescribeTagsInput describeTagsInput = new DescribeTagsInput(); // DescribeTagsInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeTagsOutput result = apiInstance.describeTags(xAmzTarget, describeTagsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeTags");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.DescribeTags] |
| **describeTagsInput** | [**DescribeTagsInput**](DescribeTagsInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeTagsOutput**](DescribeTagsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="getBatchPrediction"></a>
# **getBatchPrediction**
> GetBatchPredictionOutput getBatchPrediction(xAmzTarget, getBatchPredictionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns a &lt;code&gt;BatchPrediction&lt;/code&gt; that includes detailed metadata, status, and data file information for a &lt;code&gt;Batch Prediction&lt;/code&gt; request.

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.GetBatchPrediction"; // String | 
    GetBatchPredictionInput getBatchPredictionInput = new GetBatchPredictionInput(); // GetBatchPredictionInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetBatchPredictionOutput result = apiInstance.getBatchPrediction(xAmzTarget, getBatchPredictionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getBatchPrediction");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.GetBatchPrediction] |
| **getBatchPredictionInput** | [**GetBatchPredictionInput**](GetBatchPredictionInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetBatchPredictionOutput**](GetBatchPredictionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="getDataSource"></a>
# **getDataSource**
> GetDataSourceOutput getDataSource(xAmzTarget, getDataSourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns a &lt;code&gt;DataSource&lt;/code&gt; that includes metadata and data file information, as well as the current status of the &lt;code&gt;DataSource&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetDataSource&lt;/code&gt; provides results in normal or verbose format. The verbose format adds the schema description and the list of files pointed to by the DataSource to the normal format.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.GetDataSource"; // String | 
    GetDataSourceInput getDataSourceInput = new GetDataSourceInput(); // GetDataSourceInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetDataSourceOutput result = apiInstance.getDataSource(xAmzTarget, getDataSourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDataSource");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.GetDataSource] |
| **getDataSourceInput** | [**GetDataSourceInput**](GetDataSourceInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetDataSourceOutput**](GetDataSourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="getEvaluation"></a>
# **getEvaluation**
> GetEvaluationOutput getEvaluation(xAmzTarget, getEvaluationInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns an &lt;code&gt;Evaluation&lt;/code&gt; that includes metadata as well as the current status of the &lt;code&gt;Evaluation&lt;/code&gt;.

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.GetEvaluation"; // String | 
    GetEvaluationInput getEvaluationInput = new GetEvaluationInput(); // GetEvaluationInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetEvaluationOutput result = apiInstance.getEvaluation(xAmzTarget, getEvaluationInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getEvaluation");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.GetEvaluation] |
| **getEvaluationInput** | [**GetEvaluationInput**](GetEvaluationInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetEvaluationOutput**](GetEvaluationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="getMLModel"></a>
# **getMLModel**
> GetMLModelOutput getMLModel(xAmzTarget, getMLModelInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns an &lt;code&gt;MLModel&lt;/code&gt; that includes detailed metadata, data source information, and the current status of the &lt;code&gt;MLModel&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetMLModel&lt;/code&gt; provides results in normal or verbose format. &lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.GetMLModel"; // String | 
    GetMLModelInput getMLModelInput = new GetMLModelInput(); // GetMLModelInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetMLModelOutput result = apiInstance.getMLModel(xAmzTarget, getMLModelInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMLModel");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.GetMLModel] |
| **getMLModelInput** | [**GetMLModelInput**](GetMLModelInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetMLModelOutput**](GetMLModelOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="predict"></a>
# **predict**
> PredictOutput predict(xAmzTarget, predictInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Generates a prediction for the observation using the specified &lt;code&gt;ML Model&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Note:&lt;/b&gt; Not all response parameters will be populated. Whether a response parameter is populated depends on the type of model requested.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.Predict"; // String | 
    PredictInput predictInput = new PredictInput(); // PredictInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PredictOutput result = apiInstance.predict(xAmzTarget, predictInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#predict");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.Predict] |
| **predictInput** | [**PredictInput**](PredictInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PredictOutput**](PredictOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | LimitExceededException |  -  |
| **483** | InternalServerException |  -  |
| **484** | PredictorNotMountedException |  -  |

<a id="updateBatchPrediction"></a>
# **updateBatchPrediction**
> UpdateBatchPredictionOutput updateBatchPrediction(xAmzTarget, updateBatchPredictionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates the &lt;code&gt;BatchPredictionName&lt;/code&gt; of a &lt;code&gt;BatchPrediction&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetBatchPrediction&lt;/code&gt; operation to view the contents of the updated data element.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.UpdateBatchPrediction"; // String | 
    UpdateBatchPredictionInput updateBatchPredictionInput = new UpdateBatchPredictionInput(); // UpdateBatchPredictionInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateBatchPredictionOutput result = apiInstance.updateBatchPrediction(xAmzTarget, updateBatchPredictionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateBatchPrediction");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.UpdateBatchPrediction] |
| **updateBatchPredictionInput** | [**UpdateBatchPredictionInput**](UpdateBatchPredictionInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateBatchPredictionOutput**](UpdateBatchPredictionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="updateDataSource"></a>
# **updateDataSource**
> UpdateDataSourceOutput updateDataSource(xAmzTarget, updateDataSourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates the &lt;code&gt;DataSourceName&lt;/code&gt; of a &lt;code&gt;DataSource&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetDataSource&lt;/code&gt; operation to view the contents of the updated data element.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.UpdateDataSource"; // String | 
    UpdateDataSourceInput updateDataSourceInput = new UpdateDataSourceInput(); // UpdateDataSourceInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateDataSourceOutput result = apiInstance.updateDataSource(xAmzTarget, updateDataSourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateDataSource");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.UpdateDataSource] |
| **updateDataSourceInput** | [**UpdateDataSourceInput**](UpdateDataSourceInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateDataSourceOutput**](UpdateDataSourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="updateEvaluation"></a>
# **updateEvaluation**
> UpdateEvaluationOutput updateEvaluation(xAmzTarget, updateEvaluationInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates the &lt;code&gt;EvaluationName&lt;/code&gt; of an &lt;code&gt;Evaluation&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetEvaluation&lt;/code&gt; operation to view the contents of the updated data element.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.UpdateEvaluation"; // String | 
    UpdateEvaluationInput updateEvaluationInput = new UpdateEvaluationInput(); // UpdateEvaluationInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateEvaluationOutput result = apiInstance.updateEvaluation(xAmzTarget, updateEvaluationInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateEvaluation");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.UpdateEvaluation] |
| **updateEvaluationInput** | [**UpdateEvaluationInput**](UpdateEvaluationInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateEvaluationOutput**](UpdateEvaluationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="updateMLModel"></a>
# **updateMLModel**
> UpdateMLModelOutput updateMLModel(xAmzTarget, updateMLModelInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates the &lt;code&gt;MLModelName&lt;/code&gt; and the &lt;code&gt;ScoreThreshold&lt;/code&gt; of an &lt;code&gt;MLModel&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetMLModel&lt;/code&gt; operation to view the contents of the updated data element.&lt;/p&gt;

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
    defaultClient.setBasePath("http://machinelearning.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AmazonML_20141212.UpdateMLModel"; // String | 
    UpdateMLModelInput updateMLModelInput = new UpdateMLModelInput(); // UpdateMLModelInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateMLModelOutput result = apiInstance.updateMLModel(xAmzTarget, updateMLModelInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateMLModel");
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
| **xAmzTarget** | **String**|  | [enum: AmazonML_20141212.UpdateMLModel] |
| **updateMLModelInput** | [**UpdateMLModelInput**](UpdateMLModelInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateMLModelOutput**](UpdateMLModelOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInputException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

