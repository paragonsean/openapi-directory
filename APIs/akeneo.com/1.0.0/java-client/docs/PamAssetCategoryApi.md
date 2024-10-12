# PamAssetCategoryApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAssetCategories**](PamAssetCategoryApi.md#getAssetCategories) | **GET** /api/rest/v1/asset-categories | Get list of PAM asset categories |
| [**getAssetCategoriesCode**](PamAssetCategoryApi.md#getAssetCategoriesCode) | **GET** /api/rest/v1/asset-categories/{code} | Get a PAM asset category |
| [**patchAssetCategories**](PamAssetCategoryApi.md#patchAssetCategories) | **PATCH** /api/rest/v1/asset-categories | Update/create several PAM asset categories |
| [**patchAssetCategoriesCode**](PamAssetCategoryApi.md#patchAssetCategoriesCode) | **PATCH** /api/rest/v1/asset-categories/{code} | Update/create a PAM asset category |
| [**postAssetCategories**](PamAssetCategoryApi.md#postAssetCategories) | **POST** /api/rest/v1/asset-categories | Create a new PAM asset category |


<a id="getAssetCategories"></a>
# **getAssetCategories**
> PAMAssetCategories getAssetCategories(page, limit, withCount)

Get list of PAM asset categories

This endpoint allows you to get a list of PAM asset categories. PAM asset categories are paginated and sorted by &#x60;root/left&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PamAssetCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    PamAssetCategoryApi apiInstance = new PamAssetCategoryApi(defaultClient);
    Integer page = 1; // Integer | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
    Integer limit = 10; // Integer | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    Boolean withCount = false; // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    try {
      PAMAssetCategories result = apiInstance.getAssetCategories(page, limit, withCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PamAssetCategoryApi#getAssetCategories");
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
| **page** | **Integer**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1] |
| **limit** | **Integer**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10] |
| **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false] |

### Return type

[**PAMAssetCategories**](PAMAssetCategories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _embedded, _links, current_page, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns PAM asset categories paginated |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="getAssetCategoriesCode"></a>
# **getAssetCategoriesCode**
> PostAssetCategoriesRequest getAssetCategoriesCode(code)

Get a PAM asset category

This endpoint allows you to get the information about a given PAM asset category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PamAssetCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    PamAssetCategoryApi apiInstance = new PamAssetCategoryApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    try {
      PostAssetCategoriesRequest result = apiInstance.getAssetCategoriesCode(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PamAssetCategoryApi#getAssetCategoriesCode");
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
| **code** | **String**| Code of the resource | |

### Return type

[**PostAssetCategoriesRequest**](PostAssetCategoriesRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **404** | Resource not found |  -  |
| **406** | Not Acceptable |  -  |

<a id="patchAssetCategories"></a>
# **patchAssetCategories**
> PatchAssetCategories200Response patchAssetCategories(body)

Update/create several PAM asset categories

This endpoint allows you to update several PAM asset categories at once.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PamAssetCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    PamAssetCategoryApi apiInstance = new PamAssetCategoryApi(defaultClient);
    PatchAssetCategoriesRequest body = new PatchAssetCategoriesRequest(); // PatchAssetCategoriesRequest | 
    try {
      PatchAssetCategories200Response result = apiInstance.patchAssetCategories(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PamAssetCategoryApi#patchAssetCategories");
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
| **body** | [**PatchAssetCategoriesRequest**](PatchAssetCategoriesRequest.md)|  | [optional] |

### Return type

[**PatchAssetCategories200Response**](PatchAssetCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **413** | Request Entity Too Large |  -  |
| **415** | Unsupported Media type |  -  |

<a id="patchAssetCategoriesCode"></a>
# **patchAssetCategoriesCode**
> patchAssetCategoriesCode(code, body)

Update/create a PAM asset category

This endpoint allows you to update a given PAM asset category. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no category exists for the given code, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PamAssetCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    PamAssetCategoryApi apiInstance = new PamAssetCategoryApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    PostAssetCategoriesRequest body = new PostAssetCategoriesRequest(); // PostAssetCategoriesRequest | 
    try {
      apiInstance.patchAssetCategoriesCode(code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PamAssetCategoryApi#patchAssetCategoriesCode");
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
| **code** | **String**| Code of the resource | |
| **body** | [**PostAssetCategoriesRequest**](PostAssetCategoriesRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message, _links

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Location - URI of the created resource <br>  |
| **204** | No content to return |  * Location - URI of the created resource <br>  |
| **400** | Bad request |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |

<a id="postAssetCategories"></a>
# **postAssetCategories**
> postAssetCategories(body)

Create a new PAM asset category

This endpoint allows you to create a new PAM asset category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PamAssetCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    PamAssetCategoryApi apiInstance = new PamAssetCategoryApi(defaultClient);
    PostAssetCategoriesRequest body = new PostAssetCategoriesRequest(); // PostAssetCategoriesRequest | 
    try {
      apiInstance.postAssetCategories(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PamAssetCategoryApi#postAssetCategories");
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
| **body** | [**PostAssetCategoriesRequest**](PostAssetCategoriesRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message, _links

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Location - URI of the created resource <br>  |
| **400** | Bad request |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |

