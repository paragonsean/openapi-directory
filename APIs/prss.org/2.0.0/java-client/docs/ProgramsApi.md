# ProgramsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2ProgramsIdGet**](ProgramsApi.md#apiV2ProgramsIdGet) | **GET** /api/v2/programs/{id} | Returns the program matching the given ID. |
| [**apiV2ProgramsSearchGet**](ProgramsApi.md#apiV2ProgramsSearchGet) | **GET** /api/v2/programs/search | Optimized free-text search for programs using various filters. |


<a id="apiV2ProgramsIdGet"></a>
# **apiV2ProgramsIdGet**
> Program apiV2ProgramsIdGet(id)

Returns the program matching the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgramsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProgramsApi apiInstance = new ProgramsApi(defaultClient);
    Long id = 56L; // Long | The ID of the program to operate on.
    try {
      Program result = apiInstance.apiV2ProgramsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgramsApi#apiV2ProgramsIdGet");
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
| **id** | **Long**| The ID of the program to operate on. | |

### Return type

[**Program**](Program.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The matching program. |  -  |
| **403** | Authorization failed, or the user is not permitted to view this program. |  -  |
| **404** | The program cannot be found. |  -  |

<a id="apiV2ProgramsSearchGet"></a>
# **apiV2ProgramsSearchGet**
> List&lt;Program&gt; apiV2ProgramsSearchGet(keywords, pageStart, pageSize)

Optimized free-text search for programs using various filters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgramsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProgramsApi apiInstance = new ProgramsApi(defaultClient);
    String keywords = "keywords_example"; // String | Free text search that matches against the program title or description.
    Integer pageStart = 0; // Integer | The start page of the results to return. The first item is indexed at 0.
    Integer pageSize = 500; // Integer | The number of items to return. Must be between 0 and 500, inclusive.
    try {
      List<Program> result = apiInstance.apiV2ProgramsSearchGet(keywords, pageStart, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgramsApi#apiV2ProgramsSearchGet");
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
| **keywords** | **String**| Free text search that matches against the program title or description. | [optional] |
| **pageStart** | **Integer**| The start page of the results to return. The first item is indexed at 0. | [optional] [default to 0] |
| **pageSize** | **Integer**| The number of items to return. Must be between 0 and 500, inclusive. | [optional] [default to 500] |

### Return type

[**List&lt;Program&gt;**](Program.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Programs matching the search request sorted by relevance. |  -  |
| **403** | Authorization failed, username or password not found or incorrect. |  -  |

