# LanguageModelsApi

All URIs are relative to *http://salesforce.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteModel**](LanguageModelsApi.md#deleteModel) | **DELETE** /v2/language/models/{modelId} | Delete a Model |
| [**getTrainedModelLearningCurve**](LanguageModelsApi.md#getTrainedModelLearningCurve) | **GET** /v2/language/models/{modelId}/lc | Get Model Learning Curve |
| [**getTrainedModelMetrics**](LanguageModelsApi.md#getTrainedModelMetrics) | **GET** /v2/language/models/{modelId} | Get Model Metrics |
| [**getTrainedModels**](LanguageModelsApi.md#getTrainedModels) | **GET** /v2/language/datasets/{datasetId}/models | Get All Models |


<a id="deleteModel"></a>
# **deleteModel**
> DeletionResponse deleteModel(modelId)

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
import org.openapitools.client.api.LanguageModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageModelsApi apiInstance = new LanguageModelsApi(defaultClient);
    String modelId = "SomeModelId"; // String | Model Id
    try {
      DeletionResponse result = apiInstance.deleteModel(modelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageModelsApi#deleteModel");
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
| **modelId** | **String**| Model Id | |

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

<a id="getTrainedModelLearningCurve"></a>
# **getTrainedModelLearningCurve**
> LearningCurveList getTrainedModelLearningCurve(modelId, offset, count)

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
import org.openapitools.client.api.LanguageModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageModelsApi apiInstance = new LanguageModelsApi(defaultClient);
    String modelId = "SomeModelId"; // String | Model Id
    String offset = "0"; // String | Index of the epoch from which you want to start paging
    String count = "25"; // String | Number of epoch to return. Maximum valid value is 25.
    try {
      LearningCurveList result = apiInstance.getTrainedModelLearningCurve(modelId, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageModelsApi#getTrainedModelLearningCurve");
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
| **modelId** | **String**| Model Id | |
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

<a id="getTrainedModelMetrics"></a>
# **getTrainedModelMetrics**
> Metrics getTrainedModelMetrics(modelId)

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
import org.openapitools.client.api.LanguageModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageModelsApi apiInstance = new LanguageModelsApi(defaultClient);
    String modelId = "SomeModelId"; // String | Model Id
    try {
      Metrics result = apiInstance.getTrainedModelMetrics(modelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageModelsApi#getTrainedModelMetrics");
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
| **modelId** | **String**| Model Id | |

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

<a id="getTrainedModels"></a>
# **getTrainedModels**
> ModelList getTrainedModels(datasetId, offset, count)

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
import org.openapitools.client.api.LanguageModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageModelsApi apiInstance = new LanguageModelsApi(defaultClient);
    String datasetId = "SomeDatasetId"; // String | Dataset Id
    String offset = "0"; // String | Index of the model from which you want to start paging.
    String count = "100"; // String | Number of models to return.
    try {
      ModelList result = apiInstance.getTrainedModels(datasetId, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageModelsApi#getTrainedModels");
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

