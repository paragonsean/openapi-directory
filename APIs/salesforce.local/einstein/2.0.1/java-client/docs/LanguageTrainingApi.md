# LanguageTrainingApi

All URIs are relative to *http://salesforce.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTrainStatusAndProgress**](LanguageTrainingApi.md#getTrainStatusAndProgress) | **GET** /v2/language/train/{modelId} | Get Training Status |
| [**retrain**](LanguageTrainingApi.md#retrain) | **POST** /v2/language/retrain | Retrain a Dataset |
| [**train**](LanguageTrainingApi.md#train) | **POST** /v2/language/train | Train a Dataset |


<a id="getTrainStatusAndProgress"></a>
# **getTrainStatusAndProgress**
> TrainResponse getTrainStatusAndProgress(modelId)

Get Training Status

Returns the status of a model&#39;s training process. Use the progress field to determine how far the training has progressed. When training completes successfully, the status is SUCCEEDED and the progress is 1.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageTrainingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageTrainingApi apiInstance = new LanguageTrainingApi(defaultClient);
    String modelId = "SomeModelId"; // String | Model Id
    try {
      TrainResponse result = apiInstance.getTrainStatusAndProgress(modelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageTrainingApi#getTrainStatusAndProgress");
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

[**TrainResponse**](TrainResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Training Status |  -  |

<a id="retrain"></a>
# **retrain**
> TrainResponse retrain(algorithm, epochs, learningRate, modelId, trainParams)

Retrain a Dataset

Retrains a dataset and updates a model. Use this API call when you want to update a model and keep the model ID instead of creating a new model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageTrainingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageTrainingApi apiInstance = new LanguageTrainingApi(defaultClient);
    String algorithm = "algorithm_example"; // String | Algorithm used for train
    Integer epochs = 56; // Integer | Number of training iterations for the neural network. Optional.
    Float learningRate = 3.4F; // Float | N/A for intent or sentiment models.
    String modelId = "modelId_example"; // String | ID of the model to be updated from the training.
    V2LanguageTrainParams trainParams = new V2LanguageTrainParams(); // V2LanguageTrainParams | 
    try {
      TrainResponse result = apiInstance.retrain(algorithm, epochs, learningRate, modelId, trainParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageTrainingApi#retrain");
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
| **algorithm** | **String**| Algorithm used for train | [optional] |
| **epochs** | **Integer**| Number of training iterations for the neural network. Optional. | [optional] |
| **learningRate** | **Float**| N/A for intent or sentiment models. | [optional] |
| **modelId** | **String**| ID of the model to be updated from the training. | [optional] |
| **trainParams** | [**V2LanguageTrainParams**](V2LanguageTrainParams.md)|  | [optional] |

### Return type

[**TrainResponse**](TrainResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Training Status |  -  |

<a id="train"></a>
# **train**
> TrainResponse train(algorithm, datasetId, epochs, learningRate, name, trainParams)

Train a Dataset

Trains a dataset and creates a model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageTrainingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageTrainingApi apiInstance = new LanguageTrainingApi(defaultClient);
    String algorithm = "algorithm_example"; // String | Algorithm used for train
    Long datasetId = 56L; // Long | ID of the dataset to train.
    Integer epochs = 56; // Integer | Number of training iterations for the neural network. Optional.
    Double learningRate = 3.4D; // Double | N/A for intent or sentiment models.
    String name = "name_example"; // String | Name of the model. Maximum length is 180 characters.
    V2LanguageTrainParams trainParams = new V2LanguageTrainParams(); // V2LanguageTrainParams | 
    try {
      TrainResponse result = apiInstance.train(algorithm, datasetId, epochs, learningRate, name, trainParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageTrainingApi#train");
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
| **algorithm** | **String**| Algorithm used for train | [optional] |
| **datasetId** | **Long**| ID of the dataset to train. | [optional] |
| **epochs** | **Integer**| Number of training iterations for the neural network. Optional. | [optional] |
| **learningRate** | **Double**| N/A for intent or sentiment models. | [optional] |
| **name** | **String**| Name of the model. Maximum length is 180 characters. | [optional] |
| **trainParams** | [**V2LanguageTrainParams**](V2LanguageTrainParams.md)|  | [optional] |

### Return type

[**TrainResponse**](TrainResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Training Status |  -  |

