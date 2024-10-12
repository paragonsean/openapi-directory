# SnippetsApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSnippet**](SnippetsApi.md#deleteSnippet) | **DELETE** /v2/sites/{site_id}/snippet | DeleteSnippet |
| [**retrieveSnippet**](SnippetsApi.md#retrieveSnippet) | **GET** /v2/sites/{site_id}/snippet | RetrieveSnippet |
| [**upsertSnippet**](SnippetsApi.md#upsertSnippet) | **POST** /v2/sites/{site_id}/snippet | UpsertSnippet |


<a id="deleteSnippet"></a>
# **deleteSnippet**
> DeleteSnippetResponse deleteSnippet(siteId)

DeleteSnippet

Removes your snippet from a Square Online site.  You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.   __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String siteId = "siteId_example"; // String | The ID of the site that contains the snippet.
    try {
      DeleteSnippetResponse result = apiInstance.deleteSnippet(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#deleteSnippet");
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
| **siteId** | **String**| The ID of the site that contains the snippet. | |

### Return type

[**DeleteSnippetResponse**](DeleteSnippetResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveSnippet"></a>
# **retrieveSnippet**
> RetrieveSnippetResponse retrieveSnippet(siteId)

RetrieveSnippet

Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.  You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.   __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String siteId = "siteId_example"; // String | The ID of the site that contains the snippet.
    try {
      RetrieveSnippetResponse result = apiInstance.retrieveSnippet(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#retrieveSnippet");
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
| **siteId** | **String**| The ID of the site that contains the snippet. | |

### Return type

[**RetrieveSnippetResponse**](RetrieveSnippetResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="upsertSnippet"></a>
# **upsertSnippet**
> UpsertSnippetResponse upsertSnippet(siteId, upsertSnippetRequest)

UpsertSnippet

Adds a snippet to a Square Online site or updates the existing snippet on the site.  The snippet code is appended to the end of the &#x60;head&#x60; element on every page of the site, except checkout pages. A snippet application can add one snippet to a given site.   You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.   __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    String siteId = "siteId_example"; // String | The ID of the site where you want to add or update the snippet.
    UpsertSnippetRequest upsertSnippetRequest = new UpsertSnippetRequest(); // UpsertSnippetRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      UpsertSnippetResponse result = apiInstance.upsertSnippet(siteId, upsertSnippetRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#upsertSnippet");
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
| **siteId** | **String**| The ID of the site where you want to add or update the snippet. | |
| **upsertSnippetRequest** | [**UpsertSnippetRequest**](UpsertSnippetRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**UpsertSnippetResponse**](UpsertSnippetResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

