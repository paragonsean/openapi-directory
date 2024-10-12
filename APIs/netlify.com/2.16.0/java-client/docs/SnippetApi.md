# SnippetApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSiteSnippet**](SnippetApi.md#createSiteSnippet) | **POST** /sites/{site_id}/snippets |  |
| [**deleteSiteSnippet**](SnippetApi.md#deleteSiteSnippet) | **DELETE** /sites/{site_id}/snippets/{snippet_id} |  |
| [**getSiteSnippet**](SnippetApi.md#getSiteSnippet) | **GET** /sites/{site_id}/snippets/{snippet_id} |  |
| [**listSiteSnippets**](SnippetApi.md#listSiteSnippets) | **GET** /sites/{site_id}/snippets |  |
| [**updateSiteSnippet**](SnippetApi.md#updateSiteSnippet) | **PUT** /sites/{site_id}/snippets/{snippet_id} |  |


<a id="createSiteSnippet"></a>
# **createSiteSnippet**
> Snippet createSiteSnippet(siteId, snippet)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SnippetApi apiInstance = new SnippetApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    Snippet snippet = new Snippet(); // Snippet | 
    try {
      Snippet result = apiInstance.createSiteSnippet(siteId, snippet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetApi#createSiteSnippet");
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
| **siteId** | **String**|  | |
| **snippet** | [**Snippet**](Snippet.md)|  | |

### Return type

[**Snippet**](Snippet.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **0** | error |  -  |

<a id="deleteSiteSnippet"></a>
# **deleteSiteSnippet**
> deleteSiteSnippet(siteId, snippetId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SnippetApi apiInstance = new SnippetApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String snippetId = "snippetId_example"; // String | 
    try {
      apiInstance.deleteSiteSnippet(siteId, snippetId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetApi#deleteSiteSnippet");
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
| **siteId** | **String**|  | |
| **snippetId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | error |  -  |

<a id="getSiteSnippet"></a>
# **getSiteSnippet**
> Snippet getSiteSnippet(siteId, snippetId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SnippetApi apiInstance = new SnippetApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String snippetId = "snippetId_example"; // String | 
    try {
      Snippet result = apiInstance.getSiteSnippet(siteId, snippetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetApi#getSiteSnippet");
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
| **siteId** | **String**|  | |
| **snippetId** | **String**|  | |

### Return type

[**Snippet**](Snippet.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="listSiteSnippets"></a>
# **listSiteSnippets**
> List&lt;Snippet&gt; listSiteSnippets(siteId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SnippetApi apiInstance = new SnippetApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      List<Snippet> result = apiInstance.listSiteSnippets(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetApi#listSiteSnippets");
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
| **siteId** | **String**|  | |

### Return type

[**List&lt;Snippet&gt;**](Snippet.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="updateSiteSnippet"></a>
# **updateSiteSnippet**
> updateSiteSnippet(siteId, snippetId, snippet)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SnippetApi apiInstance = new SnippetApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String snippetId = "snippetId_example"; // String | 
    Snippet snippet = new Snippet(); // Snippet | 
    try {
      apiInstance.updateSiteSnippet(siteId, snippetId, snippet);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetApi#updateSiteSnippet");
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
| **siteId** | **String**|  | |
| **snippetId** | **String**|  | |
| **snippet** | [**Snippet**](Snippet.md)|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | error |  -  |

