# VisionModelsApi

All URIs are relative to *http://salesforce.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteModel1**](VisionModelsApi.md#deleteModel1) | **DELETE** /v2/vision/models/{modelId} | Delete a Model |
| [**getTrainedModelLearningCurve1**](VisionModelsApi.md#getTrainedModelLearningCurve1) | **GET** /v2/vision/models/{modelId}/lc | Get Model Learning Curve |
| [**getTrainedModelMetrics1**](VisionModelsApi.md#getTrainedModelMetrics1) | **GET** /v2/vision/models/{modelId} | Get Model Metrics |
| [**getTrainedModels1**](VisionModelsApi.md#getTrainedModels1) | **GET** /v2/vision/datasets/{datasetId}/models | Get All Models |


<a id="deleteModel1"></a>
# **deleteModel1**
> DeletionResponse deleteModel1(modelId)

Delete a Model

Deletes the specified model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionModelsApi apiInstance = new VisionModelsApi(defaultClient);
    String modelId = "SomeModelId"; // String | 
    try {
      DeletionResponse result = apiInstance.deleteModel1(modelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionModelsApi#deleteModel1");
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
| **modelId** | **String**|  | |

### Return type

[**DeletionResponse**](DeletionResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Deletion submitted |  -  |

<a id="getTrainedModelLearningCurve1"></a>
# **getTrainedModelLearningCurve1**
> LearningCurveList getTrainedModelLearningCurve1(modelId, offset, count)

Get Model Learning Curve

Returns the metrics for each epoch in a model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionModelsApi apiInstance = new VisionModelsApi(defaultClient);
    String modelId = "SomeModelId"; // String | 
    String offset = "0"; // String | Index of the epoch from which you want to start paging
    String count = "25"; // String | Number of epoch to return. Maximum valid value is 25.
    try {
      LearningCurveList result = apiInstance.getTrainedModelLearningCurve1(modelId, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionModelsApi#getTrainedModelLearningCurve1");
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
| **modelId** | **String**|  | |
| **offset** | **String**| Index of the epoch from which you want to start paging | [optional] [default to 0] |
| **count** | **String**| Number of epoch to return. Maximum valid value is 25. | [optional] [default to 25] |

### Return type

[**LearningCurveList**](LearningCurveList.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Learning Curve |  -  |

<a id="getTrainedModelMetrics1"></a>
# **getTrainedModelMetrics1**
> Metrics getTrainedModelMetrics1(modelId)

Get Model Metrics

Returns the metrics for a model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionModelsApi apiInstance = new VisionModelsApi(defaultClient);
    String modelId = "SomeModelId"; // String | 
    try {
      Metrics result = apiInstance.getTrainedModelMetrics1(modelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionModelsApi#getTrainedModelMetrics1");
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
| **modelId** | **String**|  | |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Model Metrics |  -  |

<a id="getTrainedModels1"></a>
# **getTrainedModels1**
> ModelList getTrainedModels1(datasetId, offset, count)

Get All Models

Returns all models for the specified dataset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionModelsApi apiInstance = new VisionModelsApi(defaultClient);
    String datasetId = "SomeDatasetId"; // String | Dataset Id
    String offset = "0"; // String | Index of the model from which you want to start paging.
    String count = "100"; // String | Number of models to return.
    try {
      ModelList result = apiInstance.getTrainedModels1(datasetId, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionModelsApi#getTrainedModels1");
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
| **datasetId** | **String**| Dataset Id | |
| **offset** | **String**| Index of the model from which you want to start paging. | [optional] [default to 0] |
| **count** | **String**| Number of models to return. | [optional] [default to 100] |

### Return type

[**ModelList**](ModelList.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

