# ListManagementTermListsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listManagementTermListsCreate**](ListManagementTermListsApi.md#listManagementTermListsCreate) | **POST** /contentmoderator/lists/v1.0/termlists |  |
| [**listManagementTermListsDelete**](ListManagementTermListsApi.md#listManagementTermListsDelete) | **DELETE** /contentmoderator/lists/v1.0/termlists/{listId} |  |
| [**listManagementTermListsGetAllTermLists**](ListManagementTermListsApi.md#listManagementTermListsGetAllTermLists) | **GET** /contentmoderator/lists/v1.0/termlists |  |
| [**listManagementTermListsGetDetails**](ListManagementTermListsApi.md#listManagementTermListsGetDetails) | **GET** /contentmoderator/lists/v1.0/termlists/{listId} |  |
| [**listManagementTermListsRefreshIndex**](ListManagementTermListsApi.md#listManagementTermListsRefreshIndex) | **POST** /contentmoderator/lists/v1.0/termlists/{listId}/RefreshIndex |  |
| [**listManagementTermListsUpdate**](ListManagementTermListsApi.md#listManagementTermListsUpdate) | **PUT** /contentmoderator/lists/v1.0/termlists/{listId} |  |


<a id="listManagementTermListsCreate"></a>
# **listManagementTermListsCreate**
> TermList listManagementTermListsCreate(contentType, body)



Creates a Term List

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementTermListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementTermListsApi apiInstance = new ListManagementTermListsApi(defaultClient);
    String contentType = "contentType_example"; // String | The content type.
    ListManagementImageListsCreateRequest body = new ListManagementImageListsCreateRequest(); // ListManagementImageListsCreateRequest | Schema of the body.
    try {
      TermList result = apiInstance.listManagementTermListsCreate(contentType, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementTermListsApi#listManagementTermListsCreate");
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

[**TermList**](TermList.md)

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

<a id="listManagementTermListsDelete"></a>
# **listManagementTermListsDelete**
> String listManagementTermListsDelete(listId)



Deletes term list with the list Id equal to list Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementTermListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementTermListsApi apiInstance = new ListManagementTermListsApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    try {
      String result = apiInstance.listManagementTermListsDelete(listId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementTermListsApi#listManagementTermListsDelete");
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

<a id="listManagementTermListsGetAllTermLists"></a>
# **listManagementTermListsGetAllTermLists**
> List&lt;TermList&gt; listManagementTermListsGetAllTermLists()



gets all the Term Lists

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementTermListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementTermListsApi apiInstance = new ListManagementTermListsApi(defaultClient);
    try {
      List<TermList> result = apiInstance.listManagementTermListsGetAllTermLists();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementTermListsApi#listManagementTermListsGetAllTermLists");
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

[**List&lt;TermList&gt;**](TermList.md)

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

<a id="listManagementTermListsGetDetails"></a>
# **listManagementTermListsGetDetails**
> TermList listManagementTermListsGetDetails(listId)



Returns list Id details of the term list with list Id equal to list Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementTermListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementTermListsApi apiInstance = new ListManagementTermListsApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    try {
      TermList result = apiInstance.listManagementTermListsGetDetails(listId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementTermListsApi#listManagementTermListsGetDetails");
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

[**TermList**](TermList.md)

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

<a id="listManagementTermListsRefreshIndex"></a>
# **listManagementTermListsRefreshIndex**
> RefreshIndex listManagementTermListsRefreshIndex(listId, language)



Refreshes the index of the list with list Id equal to list ID passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementTermListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementTermListsApi apiInstance = new ListManagementTermListsApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    String language = "language_example"; // String | Language of the terms.
    try {
      RefreshIndex result = apiInstance.listManagementTermListsRefreshIndex(listId, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementTermListsApi#listManagementTermListsRefreshIndex");
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
| **language** | **String**| Language of the terms. | |

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

<a id="listManagementTermListsUpdate"></a>
# **listManagementTermListsUpdate**
> TermList listManagementTermListsUpdate(listId, contentType, body)



Updates an Term List.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementTermListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementTermListsApi apiInstance = new ListManagementTermListsApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    String contentType = "contentType_example"; // String | The content type.
    ListManagementImageListsCreateRequest body = new ListManagementImageListsCreateRequest(); // ListManagementImageListsCreateRequest | Schema of the body.
    try {
      TermList result = apiInstance.listManagementTermListsUpdate(listId, contentType, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementTermListsApi#listManagementTermListsUpdate");
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

[**TermList**](TermList.md)

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

