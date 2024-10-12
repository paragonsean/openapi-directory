# LocaleApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLocales**](LocaleApi.md#getLocales) | **GET** /api/rest/v1/locales | Get a list of locales |
| [**getLocalesCode**](LocaleApi.md#getLocalesCode) | **GET** /api/rest/v1/locales/{code} | Get a locale |


<a id="getLocales"></a>
# **getLocales**
> Locales getLocales(search, page, limit, withCount)

Get a list of locales

This endpoint allows you to get a list of locales. Locales are paginated and sorted by code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocaleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    LocaleApi apiInstance = new LocaleApi(defaultClient);
    String search = "search_example"; // String | Filter locales, for more details see the <a href=\"/documentation/filter.html\">Filters</a> section
    Integer page = 1; // Integer | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
    Integer limit = 10; // Integer | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    Boolean withCount = false; // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    try {
      Locales result = apiInstance.getLocales(search, page, limit, withCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocaleApi#getLocales");
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
| **search** | **String**| Filter locales, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html\&quot;&gt;Filters&lt;/a&gt; section | [optional] |
| **page** | **Integer**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1] |
| **limit** | **Integer**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10] |
| **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false] |

### Return type

[**Locales**](Locales.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _embedded, _links, current_page, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return locales paginated |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="getLocalesCode"></a>
# **getLocalesCode**
> GetLocalesCode200Response getLocalesCode(code)

Get a locale

This endpoint allows you to get the information about a given locale.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocaleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    LocaleApi apiInstance = new LocaleApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    try {
      GetLocalesCode200Response result = apiInstance.getLocalesCode(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocaleApi#getLocalesCode");
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

[**GetLocalesCode200Response**](GetLocalesCode200Response.md)

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

