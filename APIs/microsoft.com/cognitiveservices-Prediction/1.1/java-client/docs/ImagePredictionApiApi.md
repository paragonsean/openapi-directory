# ImagePredictionApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**predictImage**](ImagePredictionApiApi.md#predictImage) | **POST** /{projectId}/image | Predict an image and saves the result |
| [**predictImageUrl**](ImagePredictionApiApi.md#predictImageUrl) | **POST** /{projectId}/url | Predict an image url and saves the result |
| [**predictImageUrlWithNoStore**](ImagePredictionApiApi.md#predictImageUrlWithNoStore) | **POST** /{projectId}/url/nostore | Predict an image url without saving the result |
| [**predictImageWithNoStore**](ImagePredictionApiApi.md#predictImageWithNoStore) | **POST** /{projectId}/image/nostore | Predict an image without saving the result |


<a id="predictImage"></a>
# **predictImage**
> ImagePredictionResultModel predictImage(projectId, predictionKey, imageData, iterationId, application)

Predict an image and saves the result

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagePredictionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction");

    ImagePredictionApiApi apiInstance = new ImagePredictionApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id
    String predictionKey = "{API Key}"; // String | 
    File imageData = new File("/path/to/file"); // File | 
    UUID iterationId = UUID.fromString("fe1e83c4-6f50-4899-9544-6bb08cf0e15a"); // UUID | Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified
    String application = "application_example"; // String | Optional. Specifies the name of application using the endpoint
    try {
      ImagePredictionResultModel result = apiInstance.predictImage(projectId, predictionKey, imageData, iterationId, application);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagePredictionApiApi#predictImage");
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
| **projectId** | **UUID**| The project id | |
| **predictionKey** | **String**|  | |
| **imageData** | **File**|  | |
| **iterationId** | **UUID**| Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified | [optional] |
| **application** | **String**| Optional. Specifies the name of application using the endpoint | [optional] |

### Return type

[**ImagePredictionResultModel**](ImagePredictionResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="predictImageUrl"></a>
# **predictImageUrl**
> ImagePredictionResultModel predictImageUrl(projectId, predictionKey, imageUrl, iterationId, application)

Predict an image url and saves the result

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagePredictionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction");

    ImagePredictionApiApi apiInstance = new ImagePredictionApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id
    String predictionKey = "{API Key}"; // String | 
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated
    UUID iterationId = UUID.fromString("fe1e83c4-6f50-4899-9544-6bb08cf0e15a"); // UUID | Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified
    String application = "application_example"; // String | Optional. Specifies the name of application using the endpoint
    try {
      ImagePredictionResultModel result = apiInstance.predictImageUrl(projectId, predictionKey, imageUrl, iterationId, application);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagePredictionApiApi#predictImageUrl");
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
| **projectId** | **UUID**| The project id | |
| **predictionKey** | **String**|  | |
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated | |
| **iterationId** | **UUID**| Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified | [optional] |
| **application** | **String**| Optional. Specifies the name of application using the endpoint | [optional] |

### Return type

[**ImagePredictionResultModel**](ImagePredictionResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="predictImageUrlWithNoStore"></a>
# **predictImageUrlWithNoStore**
> ImagePredictionResultModel predictImageUrlWithNoStore(projectId, predictionKey, imageUrl, iterationId, application)

Predict an image url without saving the result

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagePredictionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction");

    ImagePredictionApiApi apiInstance = new ImagePredictionApiApi(defaultClient);
    UUID projectId = UUID.randomUUID(); // UUID | The project id
    String predictionKey = "{API Key}"; // String | 
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated
    UUID iterationId = UUID.randomUUID(); // UUID | Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified
    String application = "application_example"; // String | Optional. Specifies the name of application using the endpoint
    try {
      ImagePredictionResultModel result = apiInstance.predictImageUrlWithNoStore(projectId, predictionKey, imageUrl, iterationId, application);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagePredictionApiApi#predictImageUrlWithNoStore");
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
| **projectId** | **UUID**| The project id | |
| **predictionKey** | **String**|  | |
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated | |
| **iterationId** | **UUID**| Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified | [optional] |
| **application** | **String**| Optional. Specifies the name of application using the endpoint | [optional] |

### Return type

[**ImagePredictionResultModel**](ImagePredictionResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="predictImageWithNoStore"></a>
# **predictImageWithNoStore**
> ImagePredictionResultModel predictImageWithNoStore(projectId, predictionKey, imageData, iterationId, application)

Predict an image without saving the result

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagePredictionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction");

    ImagePredictionApiApi apiInstance = new ImagePredictionApiApi(defaultClient);
    UUID projectId = UUID.randomUUID(); // UUID | The project id
    String predictionKey = "{API Key}"; // String | 
    File imageData = new File("/path/to/file"); // File | 
    UUID iterationId = UUID.randomUUID(); // UUID | Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified
    String application = "application_example"; // String | Optional. Specifies the name of application using the endpoint
    try {
      ImagePredictionResultModel result = apiInstance.predictImageWithNoStore(projectId, predictionKey, imageData, iterationId, application);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagePredictionApiApi#predictImageWithNoStore");
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
| **projectId** | **UUID**| The project id | |
| **predictionKey** | **String**|  | |
| **imageData** | **File**|  | |
| **iterationId** | **UUID**| Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified | [optional] |
| **application** | **String**| Optional. Specifies the name of application using the endpoint | [optional] |

### Return type

[**ImagePredictionResultModel**](ImagePredictionResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

