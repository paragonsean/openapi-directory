# FaceCheckApiApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiDeletePicPost**](FaceCheckApiApi.md#apiDeletePicPost) | **POST** /api/delete_pic | Remove an image from a search request |
| [**apiInfoPost**](FaceCheckApiApi.md#apiInfoPost) | **POST** /api/info | Returns remaining search credits, search engine online status, and number of indexed faces |
| [**apiSearchPost**](FaceCheckApiApi.md#apiSearchPost) | **POST** /api/search |  |
| [**apiUploadPicPost**](FaceCheckApiApi.md#apiUploadPicPost) | **POST** /api/upload_pic |  |


<a id="apiDeletePicPost"></a>
# **apiDeletePicPost**
> BrowserJsonResponse apiDeletePicPost(idSearch, idPic)

Remove an image from a search request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FaceCheckApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FaceCheckApiApi apiInstance = new FaceCheckApiApi(defaultClient);
    String idSearch = "idSearch_example"; // String | 
    String idPic = "idPic_example"; // String | 
    try {
      BrowserJsonResponse result = apiInstance.apiDeletePicPost(idSearch, idPic);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FaceCheckApiApi#apiDeletePicPost");
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
| **idSearch** | **String**|  | [optional] |
| **idPic** | **String**|  | [optional] |

### Return type

[**BrowserJsonResponse**](BrowserJsonResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiInfoPost"></a>
# **apiInfoPost**
> InfoResponse apiInfoPost()

Returns remaining search credits, search engine online status, and number of indexed faces

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FaceCheckApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FaceCheckApiApi apiInstance = new FaceCheckApiApi(defaultClient);
    try {
      InfoResponse result = apiInstance.apiInfoPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FaceCheckApiApi#apiInfoPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InfoResponse**](InfoResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiSearchPost"></a>
# **apiSearchPost**
> BrowserJsonResponse apiSearchPost(searchData)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FaceCheckApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FaceCheckApiApi apiInstance = new FaceCheckApiApi(defaultClient);
    SearchData searchData = new SearchData(); // SearchData | 
    try {
      BrowserJsonResponse result = apiInstance.apiSearchPost(searchData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FaceCheckApiApi#apiSearchPost");
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
| **searchData** | [**SearchData**](SearchData.md)|  | [optional] |

### Return type

[**BrowserJsonResponse**](BrowserJsonResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiUploadPicPost"></a>
# **apiUploadPicPost**
> BrowserJsonResponse apiUploadPicPost(idSearch, images)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FaceCheckApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FaceCheckApiApi apiInstance = new FaceCheckApiApi(defaultClient);
    String idSearch = "idSearch_example"; // String | 
    List<File> images = Arrays.asList(); // List<File> | 
    try {
      BrowserJsonResponse result = apiInstance.apiUploadPicPost(idSearch, images);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FaceCheckApiApi#apiUploadPicPost");
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
| **idSearch** | **String**|  | [optional] |
| **images** | **List&lt;File&gt;**|  | [optional] |

### Return type

[**BrowserJsonResponse**](BrowserJsonResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

