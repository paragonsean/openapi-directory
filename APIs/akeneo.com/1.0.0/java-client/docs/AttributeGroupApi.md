# AttributeGroupApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**attributeGroupsGet**](AttributeGroupApi.md#attributeGroupsGet) | **GET** /api/rest/v1/attribute-groups/{code} | Get an attribute group |
| [**attributeGroupsGetList**](AttributeGroupApi.md#attributeGroupsGetList) | **GET** /api/rest/v1/attribute-groups | Get list of attribute groups |
| [**attributeGroupsPatch**](AttributeGroupApi.md#attributeGroupsPatch) | **PATCH** /api/rest/v1/attribute-groups/{code} | Update/create an attribute group |
| [**attributeGroupsPost**](AttributeGroupApi.md#attributeGroupsPost) | **POST** /api/rest/v1/attribute-groups | Create a new attribute group |
| [**severalAttributeGroupsPatch**](AttributeGroupApi.md#severalAttributeGroupsPatch) | **PATCH** /api/rest/v1/attribute-groups | Update/create several attribute groups |


<a id="attributeGroupsGet"></a>
# **attributeGroupsGet**
> AttributeGroupsPostRequest attributeGroupsGet(code)

Get an attribute group

This endpoint allows you to get the information about a given attribute group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeGroupApi apiInstance = new AttributeGroupApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    try {
      AttributeGroupsPostRequest result = apiInstance.attributeGroupsGet(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeGroupApi#attributeGroupsGet");
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

[**AttributeGroupsPostRequest**](AttributeGroupsPostRequest.md)

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

<a id="attributeGroupsGetList"></a>
# **attributeGroupsGetList**
> AttributeGroups attributeGroupsGetList(search, page, limit, withCount)

Get list of attribute groups

This endpoint allows you to get a list of attribute groups. Attribute groups are paginated and sorted by code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeGroupApi apiInstance = new AttributeGroupApi(defaultClient);
    String search = "search_example"; // String | Filter attribute groups, for more details see the <a href=\"/documentation/filter.html#filter-attribute-groups\">Filters</a> section.
    Integer page = 1; // Integer | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
    Integer limit = 10; // Integer | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    Boolean withCount = false; // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    try {
      AttributeGroups result = apiInstance.attributeGroupsGetList(search, page, limit, withCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeGroupApi#attributeGroupsGetList");
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
| **search** | **String**| Filter attribute groups, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-attribute-groups\&quot;&gt;Filters&lt;/a&gt; section. | [optional] |
| **page** | **Integer**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1] |
| **limit** | **Integer**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10] |
| **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false] |

### Return type

[**AttributeGroups**](AttributeGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _embedded, _links, current_page, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return attribute groups paginated |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="attributeGroupsPatch"></a>
# **attributeGroupsPatch**
> attributeGroupsPatch(code, body)

Update/create an attribute group

This endpoint allows you to update a given attribute group. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no attribute group exists for the given code, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeGroupApi apiInstance = new AttributeGroupApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    AttributeGroupsPostRequest body = new AttributeGroupsPostRequest(); // AttributeGroupsPostRequest | 
    try {
      apiInstance.attributeGroupsPatch(code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeGroupApi#attributeGroupsPatch");
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
| **body** | [**AttributeGroupsPostRequest**](AttributeGroupsPostRequest.md)|  | |

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

<a id="attributeGroupsPost"></a>
# **attributeGroupsPost**
> attributeGroupsPost(body)

Create a new attribute group

This endpoint allows you to create a new attribute group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeGroupApi apiInstance = new AttributeGroupApi(defaultClient);
    AttributeGroupsPostRequest body = new AttributeGroupsPostRequest(); // AttributeGroupsPostRequest | 
    try {
      apiInstance.attributeGroupsPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeGroupApi#attributeGroupsPost");
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
| **body** | [**AttributeGroupsPostRequest**](AttributeGroupsPostRequest.md)|  | [optional] |

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

<a id="severalAttributeGroupsPatch"></a>
# **severalAttributeGroupsPatch**
> PatchAssetCategories200Response severalAttributeGroupsPatch(body)

Update/create several attribute groups

This endpoint allows you to update and/or create several attribute groups at once.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeGroupApi apiInstance = new AttributeGroupApi(defaultClient);
    SeveralAttributeGroupsPatchRequest body = new SeveralAttributeGroupsPatchRequest(); // SeveralAttributeGroupsPatchRequest | 
    try {
      PatchAssetCategories200Response result = apiInstance.severalAttributeGroupsPatch(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeGroupApi#severalAttributeGroupsPatch");
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
| **body** | [**SeveralAttributeGroupsPatchRequest**](SeveralAttributeGroupsPatchRequest.md)|  | [optional] |

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

