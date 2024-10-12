# ListManagementImageListsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listManagementImageListsCreate**](ListManagementImageListsApi.md#listManagementImageListsCreate) | **POST** /contentmoderator/lists/v1.0/imagelists |  |
| [**listManagementImageListsDelete**](ListManagementImageListsApi.md#listManagementImageListsDelete) | **DELETE** /contentmoderator/lists/v1.0/imagelists/{listId} |  |
| [**listManagementImageListsGetAllImageLists**](ListManagementImageListsApi.md#listManagementImageListsGetAllImageLists) | **GET** /contentmoderator/lists/v1.0/imagelists |  |
| [**listManagementImageListsGetDetails**](ListManagementImageListsApi.md#listManagementImageListsGetDetails) | **GET** /contentmoderator/lists/v1.0/imagelists/{listId} |  |
| [**listManagementImageListsRefreshIndex**](ListManagementImageListsApi.md#listManagementImageListsRefreshIndex) | **POST** /contentmoderator/lists/v1.0/imagelists/{listId}/RefreshIndex |  |
| [**listManagementImageListsUpdate**](ListManagementImageListsApi.md#listManagementImageListsUpdate) | **PUT** /contentmoderator/lists/v1.0/imagelists/{listId} |  |


<a id="listManagementImageListsCreate"></a>
# **listManagementImageListsCreate**
> ImageList listManagementImageListsCreate(contentType, body)



Creates an image list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementImageListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementImageListsApi apiInstance = new ListManagementImageListsApi(defaultClient);
    String contentType = "contentType_example"; // String | The content type.
    ListManagementImageListsCreateRequest body = new ListManagementImageListsCreateRequest(); // ListManagementImageListsCreateRequest | Schema of the body.
    try {
      ImageList result = apiInstance.listManagementImageListsCreate(contentType, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementImageListsApi#listManagementImageListsCreate");
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
| **contentType** | **String**| The content type. | |
| **body** | [**ListManagementImageListsCreateRequest**](ListManagementImageListsCreateRequest.md)| Schema of the body. | |

### Return type

[**ImageList**](ImageList.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response. |  -  |

<a id="listManagementImageListsDelete"></a>
# **listManagementImageListsDelete**
> String listManagementImageListsDelete(listId)



Deletes image list with the list Id equal to list Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementImageListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementImageListsApi apiInstance = new ListManagementImageListsApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    try {
      String result = apiInstance.listManagementImageListsDelete(listId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementImageListsApi#listManagementImageListsDelete");
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

<a id="listManagementImageListsGetAllImageLists"></a>
# **listManagementImageListsGetAllImageLists**
> List&lt;ImageList&gt; listManagementImageListsGetAllImageLists()



Gets all the Image Lists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementImageListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementImageListsApi apiInstance = new ListManagementImageListsApi(defaultClient);
    try {
      List<ImageList> result = apiInstance.listManagementImageListsGetAllImageLists();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementImageListsApi#listManagementImageListsGetAllImageLists");
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

[**List&lt;ImageList&gt;**](ImageList.md)

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

<a id="listManagementImageListsGetDetails"></a>
# **listManagementImageListsGetDetails**
> ImageList listManagementImageListsGetDetails(listId)



Returns the details of the image list with list Id equal to list Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementImageListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementImageListsApi apiInstance = new ListManagementImageListsApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    try {
      ImageList result = apiInstance.listManagementImageListsGetDetails(listId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementImageListsApi#listManagementImageListsGetDetails");
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

[**ImageList**](ImageList.md)

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

<a id="listManagementImageListsRefreshIndex"></a>
# **listManagementImageListsRefreshIndex**
> RefreshIndex listManagementImageListsRefreshIndex(listId)



Refreshes the index of the list with list Id equal to list Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementImageListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementImageListsApi apiInstance = new ListManagementImageListsApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    try {
      RefreshIndex result = apiInstance.listManagementImageListsRefreshIndex(listId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementImageListsApi#listManagementImageListsRefreshIndex");
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

[**RefreshIndex**](RefreshIndex.md)

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

<a id="listManagementImageListsUpdate"></a>
# **listManagementImageListsUpdate**
> ImageList listManagementImageListsUpdate(listId, contentType, body)



Updates an image list with list Id equal to list Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementImageListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementImageListsApi apiInstance = new ListManagementImageListsApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    String contentType = "contentType_example"; // String | The content type.
    ListManagementImageListsCreateRequest body = new ListManagementImageListsCreateRequest(); // ListManagementImageListsCreateRequest | Schema of the body.
    try {
      ImageList result = apiInstance.listManagementImageListsUpdate(listId, contentType, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementImageListsApi#listManagementImageListsUpdate");
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
| **contentType** | **String**| The content type. | |
| **body** | [**ListManagementImageListsCreateRequest**](ListManagementImageListsCreateRequest.md)| Schema of the body. | |

### Return type

[**ImageList**](ImageList.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response. |  -  |

