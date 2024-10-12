# ListManagementImageApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listManagementImageAddImage**](ListManagementImageApi.md#listManagementImageAddImage) | **POST** /contentmoderator/lists/v1.0/imagelists/{listId}/images |  |
| [**listManagementImageDeleteAllImages**](ListManagementImageApi.md#listManagementImageDeleteAllImages) | **DELETE** /contentmoderator/lists/v1.0/imagelists/{listId}/images |  |
| [**listManagementImageDeleteImage**](ListManagementImageApi.md#listManagementImageDeleteImage) | **DELETE** /contentmoderator/lists/v1.0/imagelists/{listId}/images/{ImageId} |  |
| [**listManagementImageGetAllImageIds**](ListManagementImageApi.md#listManagementImageGetAllImageIds) | **GET** /contentmoderator/lists/v1.0/imagelists/{listId}/images |  |


<a id="listManagementImageAddImage"></a>
# **listManagementImageAddImage**
> Image listManagementImageAddImage(listId, tag, label)



Add an image to the list with list Id equal to list Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementImageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementImageApi apiInstance = new ListManagementImageApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    Integer tag = 56; // Integer | Tag for the image.
    String label = "label_example"; // String | The image label.
    try {
      Image result = apiInstance.listManagementImageAddImage(listId, tag, label);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementImageApi#listManagementImageAddImage");
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
| **listId** | **String**| List Id of the image list. | |
| **tag** | **Integer**| Tag for the image. | [optional] |
| **label** | **String**| The image label. | [optional] |

### Return type

[**Image**](Image.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response. |  -  |

<a id="listManagementImageDeleteAllImages"></a>
# **listManagementImageDeleteAllImages**
> String listManagementImageDeleteAllImages(listId)



Deletes all images from the list with list Id equal to list Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementImageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementImageApi apiInstance = new ListManagementImageApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    try {
      String result = apiInstance.listManagementImageDeleteAllImages(listId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementImageApi#listManagementImageDeleteAllImages");
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
| **listId** | **String**| List Id of the image list. | |

### Return type

**String**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response. |  -  |

<a id="listManagementImageDeleteImage"></a>
# **listManagementImageDeleteImage**
> String listManagementImageDeleteImage(listId, imageId)



Deletes an image from the list with list Id and image Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementImageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementImageApi apiInstance = new ListManagementImageApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    String imageId = "imageId_example"; // String | Id of the image.
    try {
      String result = apiInstance.listManagementImageDeleteImage(listId, imageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementImageApi#listManagementImageDeleteImage");
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
| **listId** | **String**| List Id of the image list. | |
| **imageId** | **String**| Id of the image. | |

### Return type

**String**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response. |  -  |

<a id="listManagementImageGetAllImageIds"></a>
# **listManagementImageGetAllImageIds**
> ImageIds listManagementImageGetAllImageIds(listId)



Gets all image Ids from the list with list Id equal to list Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementImageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementImageApi apiInstance = new ListManagementImageApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    try {
      ImageIds result = apiInstance.listManagementImageGetAllImageIds(listId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementImageApi#listManagementImageGetAllImageIds");
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
| **listId** | **String**| List Id of the image list. | |

### Return type

[**ImageIds**](ImageIds.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response. |  -  |

