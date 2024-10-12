# AttributeApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAttributes**](AttributeApi.md#getAttributes) | **GET** /api/rest/v1/attributes | Get list of attributes |
| [**getAttributesCode**](AttributeApi.md#getAttributesCode) | **GET** /api/rest/v1/attributes/{code} | Get an attribute |
| [**patchAttributes**](AttributeApi.md#patchAttributes) | **PATCH** /api/rest/v1/attributes | Update/create several attributes |
| [**patchAttributesCode**](AttributeApi.md#patchAttributesCode) | **PATCH** /api/rest/v1/attributes/{code} | Update/create an attribute |
| [**postAttributes**](AttributeApi.md#postAttributes) | **POST** /api/rest/v1/attributes | Create a new attribute |


<a id="getAttributes"></a>
# **getAttributes**
> Attributes getAttributes(search, page, limit, withCount, withTableSelectOptions)

Get list of attributes

This endpoint allows you to get a list of attributes. Attributes are paginated and sorted by code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String search = "search_example"; // String | Filter attributes, for more details see the <a href=\"/documentation/filter.html#filter-attributes\">Filters</a> section.
    Integer page = 1; // Integer | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
    Integer limit = 10; // Integer | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    Boolean withCount = false; // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    Boolean withTableSelectOptions = false; // Boolean | Return the options of 'select' column types (of a table attribute) in the response. (Only available since the 7.0 version)
    try {
      Attributes result = apiInstance.getAttributes(search, page, limit, withCount, withTableSelectOptions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#getAttributes");
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
| **search** | **String**| Filter attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-attributes\&quot;&gt;Filters&lt;/a&gt; section. | [optional] |
| **page** | **Integer**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1] |
| **limit** | **Integer**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10] |
| **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false] |
| **withTableSelectOptions** | **Boolean**| Return the options of &#39;select&#39; column types (of a table attribute) in the response. (Only available since the 7.0 version) | [optional] [default to false] |

### Return type

[**Attributes**](Attributes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _embedded, _links, current_page, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return attributes paginated |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="getAttributesCode"></a>
# **getAttributesCode**
> PostAttributesRequest getAttributesCode(code, withTableSelectOptions)

Get an attribute

This endpoint allows you to get the information about a given attribute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    Boolean withTableSelectOptions = false; // Boolean | Return the options of 'select' column types (of a table attribute) in the response. (Only available since the 7.0 version)
    try {
      PostAttributesRequest result = apiInstance.getAttributesCode(code, withTableSelectOptions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#getAttributesCode");
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
| **withTableSelectOptions** | **Boolean**| Return the options of &#39;select&#39; column types (of a table attribute) in the response. (Only available since the 7.0 version) | [optional] [default to false] |

### Return type

[**PostAttributesRequest**](PostAttributesRequest.md)

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

<a id="patchAttributes"></a>
# **patchAttributes**
> PatchAssetCategories200Response patchAttributes(body)

Update/create several attributes

This endpoint allows you to update and/or create several attributes at once.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    PatchAttributesRequest body = new PatchAttributesRequest(); // PatchAttributesRequest | 
    try {
      PatchAssetCategories200Response result = apiInstance.patchAttributes(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#patchAttributes");
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
| **body** | [**PatchAttributesRequest**](PatchAttributesRequest.md)|  | [optional] |

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

<a id="patchAttributesCode"></a>
# **patchAttributesCode**
> patchAttributesCode(code, body)

Update/create an attribute

This endpoint allows you to update a given attribute. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no attribute exists for the given code, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    PostAttributesRequest body = new PostAttributesRequest(); // PostAttributesRequest | 
    try {
      apiInstance.patchAttributesCode(code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#patchAttributesCode");
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
| **body** | [**PostAttributesRequest**](PostAttributesRequest.md)|  | |

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

<a id="postAttributes"></a>
# **postAttributes**
> postAttributes(body)

Create a new attribute

This endpoint allows you to create a new attribute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    PostAttributesRequest body = new PostAttributesRequest(); // PostAttributesRequest | 
    try {
      apiInstance.postAttributes(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#postAttributes");
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
| **body** | [**PostAttributesRequest**](PostAttributesRequest.md)|  | [optional] |

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

