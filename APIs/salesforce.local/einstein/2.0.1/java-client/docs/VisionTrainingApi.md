# VisionTrainingApi

All URIs are relative to *http://salesforce.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTrainStatusAndProgress1**](VisionTrainingApi.md#getTrainStatusAndProgress1) | **GET** /v2/vision/train/{modelId} | Get Training Status |
| [**retrain1**](VisionTrainingApi.md#retrain1) | **POST** /v2/vision/retrain | Retrain a Dataset |
| [**train1**](VisionTrainingApi.md#train1) | **POST** /v2/vision/train | Train a Dataset |


<a id="getTrainStatusAndProgress1"></a>
# **getTrainStatusAndProgress1**
> TrainResponse getTrainStatusAndProgress1(modelId)

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
import org.openapitools.client.api.VisionTrainingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionTrainingApi apiInstance = new VisionTrainingApi(defaultClient);
    String modelId = "SomeModelId"; // String | 
    try {
      TrainResponse result = apiInstance.getTrainStatusAndProgress1(modelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionTrainingApi#getTrainStatusAndProgress1");
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

<a id="retrain1"></a>
# **retrain1**
> TrainResponse retrain1(algorithm, epochs, learningRate, modelId, trainParams)

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
import org.openapitools.client.api.VisionTrainingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionTrainingApi apiInstance = new VisionTrainingApi(defaultClient);
    String algorithm = "algorithm_example"; // String | Specifies the algorithm used to train the dataset. Optional. Use this parameter only when training a dataset with a type of image-detection. Valid values are object-detection-v1 and retail-execution.
    Integer epochs = 56; // Integer | Number of training iterations for the neural network. Optional.
    Float learningRate = 3.4F; // Float | Specifies how much the gradient affects the optimization of the model at each time step. Optional.
    String modelId = "modelId_example"; // String | ID of the model to be updated from the training.
    V2VisionTrainParams trainParams = new V2VisionTrainParams(); // V2VisionTrainParams | 
    try {
      TrainResponse result = apiInstance.retrain1(algorithm, epochs, learningRate, modelId, trainParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionTrainingApi#retrain1");
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
| **algorithm** | **String**| Specifies the algorithm used to train the dataset. Optional. Use this parameter only when training a dataset with a type of image-detection. Valid values are object-detection-v1 and retail-execution. | [optional] |
| **epochs** | **Integer**| Number of training iterations for the neural network. Optional. | [optional] |
| **learningRate** | **Float**| Specifies how much the gradient affects the optimization of the model at each time step. Optional. | [optional] |
| **modelId** | **String**| ID of the model to be updated from the training. | [optional] |
| **trainParams** | [**V2VisionTrainParams**](V2VisionTrainParams.md)|  | [optional] |

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

<a id="train1"></a>
# **train1**
> TrainResponse train1(algorithm, datasetId, epochs, learningRate, name, trainParams)

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
import org.openapitools.client.api.VisionTrainingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionTrainingApi apiInstance = new VisionTrainingApi(defaultClient);
    String algorithm = "algorithm_example"; // String | Specifies the algorithm used to train the dataset. Optional. Use this parameter only when training a dataset with a type of image-detection. Valid values are object-detection-v1 and retail-execution.
    Long datasetId = 56L; // Long | ID of the dataset to train.
    Integer epochs = 56; // Integer | Number of training iterations for the neural network. Optional.
    Double learningRate = 3.4D; // Double | Specifies how much the gradient affects the optimization of the model at each time step. Optional.
    String name = "name_example"; // String | Name of the model. Maximum length is 180 characters.
    V2VisionTrainParams trainParams = new V2VisionTrainParams(); // V2VisionTrainParams | 
    try {
      TrainResponse result = apiInstance.train1(algorithm, datasetId, epochs, learningRate, name, trainParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionTrainingApi#train1");
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
| **algorithm** | **String**| Specifies the algorithm used to train the dataset. Optional. Use this parameter only when training a dataset with a type of image-detection. Valid values are object-detection-v1 and retail-execution. | [optional] |
| **datasetId** | **Long**| ID of the dataset to train. | [optional] |
| **epochs** | **Integer**| Number of training iterations for the neural network. Optional. | [optional] |
| **learningRate** | **Double**| Specifies how much the gradient affects the optimization of the model at each time step. Optional. | [optional] |
| **name** | **String**| Name of the model. Maximum length is 180 characters. | [optional] |
| **trainParams** | [**V2VisionTrainParams**](V2VisionTrainParams.md)|  | [optional] |

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

