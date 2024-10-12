# PredictionsApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/training*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deletePrediction**](PredictionsApiApi.md#deletePrediction) | **DELETE** /projects/{projectId}/predictions | Delete a set of predicted images and their associated prediction results. |
| [**queryPredictions**](PredictionsApiApi.md#queryPredictions) | **POST** /projects/{projectId}/predictions/query | Get images that were sent to your prediction endpoint. |
| [**quickTestImage**](PredictionsApiApi.md#quickTestImage) | **POST** /projects/{projectId}/quicktest/image | Quick test an image. |
| [**quickTestImageUrl**](PredictionsApiApi.md#quickTestImageUrl) | **POST** /projects/{projectId}/quicktest/url | Quick test an image url. |


<a id="deletePrediction"></a>
# **deletePrediction**
> deletePrediction(projectId, ids, trainingKey)

Delete a set of predicted images and their associated prediction results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PredictionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/training");

    PredictionsApiApi apiInstance = new PredictionsApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    List<UUID> ids = Arrays.asList(); // List<UUID> | The prediction ids. Limited to 64.
    String trainingKey = "{API Key}"; // String | API key.
    try {
      apiInstance.deletePrediction(projectId, ids, trainingKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling PredictionsApiApi#deletePrediction");
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
| **projectId** | **UUID**| The project id. | |
| **ids** | [**List&lt;UUID&gt;**](UUID.md)| The prediction ids. Limited to 64. | |
| **trainingKey** | **String**| API key. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response |  -  |

<a id="queryPredictions"></a>
# **queryPredictions**
> PredictionQueryResult queryPredictions(projectId, trainingKey, predictionQueryToken)

Get images that were sent to your prediction endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PredictionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/training");

    PredictionsApiApi apiInstance = new PredictionsApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id.
    String trainingKey = "{API Key}"; // String | API key.
    PredictionQueryToken predictionQueryToken = new PredictionQueryToken(); // PredictionQueryToken | Parameters used to query the predictions. Limited to combining 2 tags.
    try {
      PredictionQueryResult result = apiInstance.queryPredictions(projectId, trainingKey, predictionQueryToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PredictionsApiApi#queryPredictions");
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
| **projectId** | **UUID**| The project id. | |
| **trainingKey** | **String**| API key. | |
| **predictionQueryToken** | [**PredictionQueryToken**](PredictionQueryToken.md)| Parameters used to query the predictions. Limited to combining 2 tags. | |

### Return type

[**PredictionQueryResult**](PredictionQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="quickTestImage"></a>
# **quickTestImage**
> ImagePrediction quickTestImage(projectId, trainingKey, imageData, iterationId)

Quick test an image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PredictionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/training");

    PredictionsApiApi apiInstance = new PredictionsApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    String trainingKey = "{API Key}"; // String | API key.
    File imageData = new File("/path/to/file"); // File | Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 6MB.
    UUID iterationId = UUID.fromString("fe1e83c4-6f50-4899-9544-6bb08cf0e15a"); // UUID | Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified.
    try {
      ImagePrediction result = apiInstance.quickTestImage(projectId, trainingKey, imageData, iterationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PredictionsApiApi#quickTestImage");
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
| **projectId** | **UUID**| The project id. | |
| **trainingKey** | **String**| API key. | |
| **imageData** | **File**| Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 6MB. | |
| **iterationId** | **UUID**| Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified. | [optional] |

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="quickTestImageUrl"></a>
# **quickTestImageUrl**
> ImagePrediction quickTestImageUrl(projectId, trainingKey, imageUrl, iterationId)

Quick test an image url.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PredictionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/training");

    PredictionsApiApi apiInstance = new PredictionsApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project to evaluate against.
    String trainingKey = "{API Key}"; // String | API key.
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | An ImageUrl that contains the url of the image to be evaluated.
    UUID iterationId = UUID.fromString("fe1e83c4-6f50-4899-9544-6bb08cf0e15a"); // UUID | Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified.
    try {
      ImagePrediction result = apiInstance.quickTestImageUrl(projectId, trainingKey, imageUrl, iterationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PredictionsApiApi#quickTestImageUrl");
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
| **projectId** | **UUID**| The project to evaluate against. | |
| **trainingKey** | **String**| API key. | |
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| An ImageUrl that contains the url of the image to be evaluated. | |
| **iterationId** | **UUID**| Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified. | [optional] |

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

