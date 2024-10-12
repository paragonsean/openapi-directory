# PagesApi

All URIs are relative to *https://dev.to/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPagesGet**](PagesApi.md#apiPagesGet) | **GET** /api/pages | show details for all pages |
| [**apiPagesIdDelete**](PagesApi.md#apiPagesIdDelete) | **DELETE** /api/pages/{id} | remove a page |
| [**apiPagesIdGet**](PagesApi.md#apiPagesIdGet) | **GET** /api/pages/{id} | show details for a page |
| [**apiPagesIdPut**](PagesApi.md#apiPagesIdPut) | **PUT** /api/pages/{id} | update details for a page |
| [**apiPagesPost**](PagesApi.md#apiPagesPost) | **POST** /api/pages | pages |


<a id="apiPagesGet"></a>
# **apiPagesGet**
> List&lt;Page&gt; apiPagesGet()

show details for all pages

This endpoint allows the client to retrieve details for all Page objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");

    PagesApi apiInstance = new PagesApi(defaultClient);
    try {
      List<Page> result = apiInstance.apiPagesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#apiPagesGet");
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

[**List&lt;Page&gt;**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |

<a id="apiPagesIdDelete"></a>
# **apiPagesIdDelete**
> Page apiPagesIdDelete(id)

remove a page

This endpoint allows the client to delete a single Page object, specified by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    PagesApi apiInstance = new PagesApi(defaultClient);
    Integer id = 1; // Integer | The ID of the page.
    try {
      Page result = apiInstance.apiPagesIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#apiPagesIdDelete");
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
| **id** | **Integer**| The ID of the page. | |

### Return type

[**Page**](Page.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |
| **422** | unprocessable |  -  |

<a id="apiPagesIdGet"></a>
# **apiPagesIdGet**
> Page apiPagesIdGet(id)

show details for a page

This endpoint allows the client to retrieve details for a single Page object, specified by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");

    PagesApi apiInstance = new PagesApi(defaultClient);
    Integer id = 1; // Integer | The ID of the page.
    try {
      Page result = apiInstance.apiPagesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#apiPagesIdGet");
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
| **id** | **Integer**| The ID of the page. | |

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |

<a id="apiPagesIdPut"></a>
# **apiPagesIdPut**
> Page apiPagesIdPut(id, page)

update details for a page

This endpoint allows the client to retrieve details for a single Page object, specified by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    PagesApi apiInstance = new PagesApi(defaultClient);
    Integer id = 1; // Integer | The ID of the page.
    Page page = new Page(); // Page | 
    try {
      Page result = apiInstance.apiPagesIdPut(id, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#apiPagesIdPut");
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
| **id** | **Integer**| The ID of the page. | |
| **page** | [**Page**](Page.md)|  | [optional] |

### Return type

[**Page**](Page.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |
| **422** | unprocessable |  -  |

<a id="apiPagesPost"></a>
# **apiPagesPost**
> apiPagesPost(apiPagesPostRequest)

pages

This endpoint allows the client to create a new page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    PagesApi apiInstance = new PagesApi(defaultClient);
    ApiPagesPostRequest apiPagesPostRequest = new ApiPagesPostRequest(); // ApiPagesPostRequest | 
    try {
      apiInstance.apiPagesPost(apiPagesPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#apiPagesPost");
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
| **apiPagesPostRequest** | [**ApiPagesPostRequest**](ApiPagesPostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |
| **422** | unprocessable |  -  |

