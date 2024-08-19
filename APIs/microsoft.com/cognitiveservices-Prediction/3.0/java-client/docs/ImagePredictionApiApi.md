# ImagePredictionApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/prediction*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**classifyImage**](ImagePredictionApiApi.md#classifyImage) | **POST** /{projectId}/classify/iterations/{publishedName}/image | Classify an image and saves the result. |
| [**classifyImageUrl**](ImagePredictionApiApi.md#classifyImageUrl) | **POST** /{projectId}/classify/iterations/{publishedName}/url | Classify an image url and saves the result. |
| [**classifyImageUrlWithNoStore**](ImagePredictionApiApi.md#classifyImageUrlWithNoStore) | **POST** /{projectId}/classify/iterations/{publishedName}/url/nostore | Classify an image url without saving the result. |
| [**classifyImageWithNoStore**](ImagePredictionApiApi.md#classifyImageWithNoStore) | **POST** /{projectId}/classify/iterations/{publishedName}/image/nostore | Classify an image without saving the result. |
| [**detectImage**](ImagePredictionApiApi.md#detectImage) | **POST** /{projectId}/detect/iterations/{publishedName}/image | Detect objects in an image and saves the result. |
| [**detectImageUrl**](ImagePredictionApiApi.md#detectImageUrl) | **POST** /{projectId}/detect/iterations/{publishedName}/url | Detect objects in an image url and saves the result. |
| [**detectImageUrlWithNoStore**](ImagePredictionApiApi.md#detectImageUrlWithNoStore) | **POST** /{projectId}/detect/iterations/{publishedName}/url/nostore | Detect objects in an image url without saving the result. |
| [**detectImageWithNoStore**](ImagePredictionApiApi.md#detectImageWithNoStore) | **POST** /{projectId}/detect/iterations/{publishedName}/image/nostore | Detect objects in an image without saving the result. |


<a id="classifyImage"></a>
# **classifyImage**
> ImagePrediction classifyImage(projectId, publishedName, imageData, application)

Classify an image and saves the result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagePredictionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/prediction");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ImagePredictionApiApi apiInstance = new ImagePredictionApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    String publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
    File imageData = new File("/path/to/file"); // File | Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 4MB.
    String application = "application_example"; // String | Optional. Specifies the name of application using the endpoint.
    try {
      ImagePrediction result = apiInstance.classifyImage(projectId, publishedName, imageData, application);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagePredictionApiApi#classifyImage");
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
| **publishedName** | **String**| Specifies the name of the model to evaluate against. | |
| **imageData** | **File**| Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 4MB. | |
| **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] |

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="classifyImageUrl"></a>
# **classifyImageUrl**
> ImagePrediction classifyImageUrl(projectId, publishedName, imageUrl, application)

Classify an image url and saves the result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagePredictionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/prediction");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ImagePredictionApiApi apiInstance = new ImagePredictionApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    String publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | An ImageUrl that contains the url of the image to be evaluated.
    String application = "application_example"; // String | Optional. Specifies the name of application using the endpoint.
    try {
      ImagePrediction result = apiInstance.classifyImageUrl(projectId, publishedName, imageUrl, application);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagePredictionApiApi#classifyImageUrl");
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
| **publishedName** | **String**| Specifies the name of the model to evaluate against. | |
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| An ImageUrl that contains the url of the image to be evaluated. | |
| **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] |

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="classifyImageUrlWithNoStore"></a>
# **classifyImageUrlWithNoStore**
> ImagePrediction classifyImageUrlWithNoStore(projectId, publishedName, imageUrl, application)

Classify an image url without saving the result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagePredictionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/prediction");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ImagePredictionApiApi apiInstance = new ImagePredictionApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    String publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated.
    String application = "application_example"; // String | Optional. Specifies the name of application using the endpoint.
    try {
      ImagePrediction result = apiInstance.classifyImageUrlWithNoStore(projectId, publishedName, imageUrl, application);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagePredictionApiApi#classifyImageUrlWithNoStore");
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
| **publishedName** | **String**| Specifies the name of the model to evaluate against. | |
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated. | |
| **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] |

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="classifyImageWithNoStore"></a>
# **classifyImageWithNoStore**
> ImagePrediction classifyImageWithNoStore(projectId, publishedName, imageData, application)

Classify an image without saving the result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagePredictionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/prediction");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ImagePredictionApiApi apiInstance = new ImagePredictionApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    String publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
    File imageData = new File("/path/to/file"); // File | Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 0MB.
    String application = "application_example"; // String | Optional. Specifies the name of application using the endpoint.
    try {
      ImagePrediction result = apiInstance.classifyImageWithNoStore(projectId, publishedName, imageData, application);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagePredictionApiApi#classifyImageWithNoStore");
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
| **publishedName** | **String**| Specifies the name of the model to evaluate against. | |
| **imageData** | **File**| Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 0MB. | |
| **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] |

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="detectImage"></a>
# **detectImage**
> ImagePrediction detectImage(projectId, publishedName, imageData, application)

Detect objects in an image and saves the result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagePredictionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/prediction");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ImagePredictionApiApi apiInstance = new ImagePredictionApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    String publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
    File imageData = new File("/path/to/file"); // File | Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 4MB.
    String application = "application_example"; // String | Optional. Specifies the name of application using the endpoint.
    try {
      ImagePrediction result = apiInstance.detectImage(projectId, publishedName, imageData, application);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagePredictionApiApi#detectImage");
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
| **publishedName** | **String**| Specifies the name of the model to evaluate against. | |
| **imageData** | **File**| Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 4MB. | |
| **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] |

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="detectImageUrl"></a>
# **detectImageUrl**
> ImagePrediction detectImageUrl(projectId, publishedName, imageUrl, application)

Detect objects in an image url and saves the result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagePredictionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/prediction");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ImagePredictionApiApi apiInstance = new ImagePredictionApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    String publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | An ImageUrl that contains the url of the image to be evaluated.
    String application = "application_example"; // String | Optional. Specifies the name of application using the endpoint.
    try {
      ImagePrediction result = apiInstance.detectImageUrl(projectId, publishedName, imageUrl, application);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagePredictionApiApi#detectImageUrl");
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
| **publishedName** | **String**| Specifies the name of the model to evaluate against. | |
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| An ImageUrl that contains the url of the image to be evaluated. | |
| **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] |

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="detectImageUrlWithNoStore"></a>
# **detectImageUrlWithNoStore**
> ImagePrediction detectImageUrlWithNoStore(projectId, publishedName, imageUrl, application)

Detect objects in an image url without saving the result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagePredictionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/prediction");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ImagePredictionApiApi apiInstance = new ImagePredictionApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    String publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated.
    String application = "application_example"; // String | Optional. Specifies the name of application using the endpoint.
    try {
      ImagePrediction result = apiInstance.detectImageUrlWithNoStore(projectId, publishedName, imageUrl, application);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagePredictionApiApi#detectImageUrlWithNoStore");
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
| **publishedName** | **String**| Specifies the name of the model to evaluate against. | |
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated. | |
| **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] |

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="detectImageWithNoStore"></a>
# **detectImageWithNoStore**
> ImagePrediction detectImageWithNoStore(projectId, publishedName, imageData, application)

Detect objects in an image without saving the result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagePredictionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/prediction");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ImagePredictionApiApi apiInstance = new ImagePredictionApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    String publishedName = "MyModel1"; // String | Specifies the name of the model to evaluate against.
    File imageData = new File("/path/to/file"); // File | Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 0MB.
    String application = "application_example"; // String | Optional. Specifies the name of application using the endpoint.
    try {
      ImagePrediction result = apiInstance.detectImageWithNoStore(projectId, publishedName, imageData, application);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagePredictionApiApi#detectImageWithNoStore");
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
| **publishedName** | **String**| Specifies the name of the model to evaluate against. | |
| **imageData** | **File**| Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 0MB. | |
| **application** | **String**| Optional. Specifies the name of application using the endpoint. | [optional] |

### Return type

[**ImagePrediction**](ImagePrediction.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

