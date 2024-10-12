# CategoryApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCategories**](CategoryApi.md#getCategories) | **GET** /api/rest/v1/categories | Get list of categories |
| [**getCategoriesCode**](CategoryApi.md#getCategoriesCode) | **GET** /api/rest/v1/categories/{code} | Get a category |
| [**getCategoryMediaFilesCodeDownload**](CategoryApi.md#getCategoryMediaFilesCodeDownload) | **GET** /api/rest/v1/category-media-files/{code}/download | Download a category media file |
| [**patchCategories**](CategoryApi.md#patchCategories) | **PATCH** /api/rest/v1/categories | Update/create several categories |
| [**patchCategoriesCode**](CategoryApi.md#patchCategoriesCode) | **PATCH** /api/rest/v1/categories/{code} | Update/create a category |
| [**postCategories**](CategoryApi.md#postCategories) | **POST** /api/rest/v1/categories | Create a new category |


<a id="getCategories"></a>
# **getCategories**
> Categories getCategories(search, page, limit, withCount, withPosition, withEnrichedAttributes)

Get list of categories

This endpoint allows you to get a list of categories. Categories are paginated and sorted by &#x60;root/left&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String search = "search_example"; // String | Filter categories, for more details see the <a href=\"/documentation/filter.html#filter-categories\">Filters</a> section.
    Integer page = 1; // Integer | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
    Integer limit = 10; // Integer | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    Boolean withCount = false; // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    Boolean withPosition = true; // Boolean | Return information about category position into its category tree (only available since the 7.0 version)
    Boolean withEnrichedAttributes = true; // Boolean | Return attribute values of the category (only available on SaaS platforms)
    try {
      Categories result = apiInstance.getCategories(search, page, limit, withCount, withPosition, withEnrichedAttributes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#getCategories");
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
| **search** | **String**| Filter categories, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-categories\&quot;&gt;Filters&lt;/a&gt; section. | [optional] |
| **page** | **Integer**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1] |
| **limit** | **Integer**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10] |
| **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false] |
| **withPosition** | **Boolean**| Return information about category position into its category tree (only available since the 7.0 version) | [optional] |
| **withEnrichedAttributes** | **Boolean**| Return attribute values of the category (only available on SaaS platforms) | [optional] |

### Return type

[**Categories**](Categories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _embedded, _links, current_page, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return categories paginated |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="getCategoriesCode"></a>
# **getCategoriesCode**
> PostCategoriesRequest getCategoriesCode(code, withPosition, withEnrichedAttributes)

Get a category

This endpoint allows you to get the information about a given category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    Boolean withPosition = true; // Boolean | Return information about category position into its category tree (only available since the 7.0 version)
    Boolean withEnrichedAttributes = true; // Boolean | Return attribute values of the category (only available on SaaS platforms)
    try {
      PostCategoriesRequest result = apiInstance.getCategoriesCode(code, withPosition, withEnrichedAttributes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#getCategoriesCode");
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
| **withPosition** | **Boolean**| Return information about category position into its category tree (only available since the 7.0 version) | [optional] |
| **withEnrichedAttributes** | **Boolean**| Return attribute values of the category (only available on SaaS platforms) | [optional] |

### Return type

[**PostCategoriesRequest**](PostCategoriesRequest.md)

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

<a id="getCategoryMediaFilesCodeDownload"></a>
# **getCategoryMediaFilesCodeDownload**
> getCategoryMediaFilesCodeDownload(code)

Download a category media file

This endpoint allows you to download a given media file that is used as an attribute value of a enriched category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    try {
      apiInstance.getCategoryMediaFilesCodeDownload(code);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#getCategoryMediaFilesCodeDownload");
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

null (empty response body)

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

<a id="patchCategories"></a>
# **patchCategories**
> PatchAssetCategories200Response patchCategories(body)

Update/create several categories

This endpoint allows you to update several categories at once.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    PatchCategoriesRequest body = new PatchCategoriesRequest(); // PatchCategoriesRequest | 
    try {
      PatchAssetCategories200Response result = apiInstance.patchCategories(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#patchCategories");
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
| **body** | [**PatchCategoriesRequest**](PatchCategoriesRequest.md)|  | [optional] |

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

<a id="patchCategoriesCode"></a>
# **patchCategoriesCode**
> patchCategoriesCode(code, body)

Update/create a category

This endpoint allows you to update a given category. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no category exists for the given code, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    PostCategoriesRequest body = new PostCategoriesRequest(); // PostCategoriesRequest | 
    try {
      apiInstance.patchCategoriesCode(code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#patchCategoriesCode");
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
| **body** | [**PostCategoriesRequest**](PostCategoriesRequest.md)|  | |

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

<a id="postCategories"></a>
# **postCategories**
> postCategories(body)

Create a new category

This endpoint allows you to create a new category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    PostCategoriesRequest body = new PostCategoriesRequest(); // PostCategoriesRequest | 
    try {
      apiInstance.postCategories(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#postCategories");
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
| **body** | [**PostCategoriesRequest**](PostCategoriesRequest.md)|  | [optional] |

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

