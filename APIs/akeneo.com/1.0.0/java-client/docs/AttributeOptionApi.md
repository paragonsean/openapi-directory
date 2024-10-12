# AttributeOptionApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAttributesAttributeCodeOptions**](AttributeOptionApi.md#getAttributesAttributeCodeOptions) | **GET** /api/rest/v1/attributes/{attribute_code}/options | Get list of attribute options |
| [**getAttributesAttributeCodeOptionsCode**](AttributeOptionApi.md#getAttributesAttributeCodeOptionsCode) | **GET** /api/rest/v1/attributes/{attribute_code}/options/{code} | Get an attribute option |
| [**patchAttributesAttributeCodeOptions**](AttributeOptionApi.md#patchAttributesAttributeCodeOptions) | **PATCH** /api/rest/v1/attributes/{attribute_code}/options | Update/create several attribute options |
| [**patchAttributesAttributeCodeOptionsCode**](AttributeOptionApi.md#patchAttributesAttributeCodeOptionsCode) | **PATCH** /api/rest/v1/attributes/{attribute_code}/options/{code} | Update/create an attribute option |
| [**postAttributesAttributeCodeOptions**](AttributeOptionApi.md#postAttributesAttributeCodeOptions) | **POST** /api/rest/v1/attributes/{attribute_code}/options | Create a new attribute option |


<a id="getAttributesAttributeCodeOptions"></a>
# **getAttributesAttributeCodeOptions**
> AttributeOptions getAttributesAttributeCodeOptions(attributeCode, page, limit, withCount)

Get list of attribute options

This endpoint allows you to get a list of attribute options. Attribute options are paginated and sorted by code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeOptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeOptionApi apiInstance = new AttributeOptionApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | Code of the attribute
    Integer page = 1; // Integer | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
    Integer limit = 10; // Integer | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    Boolean withCount = false; // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    try {
      AttributeOptions result = apiInstance.getAttributesAttributeCodeOptions(attributeCode, page, limit, withCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeOptionApi#getAttributesAttributeCodeOptions");
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
| **attributeCode** | **String**| Code of the attribute | |
| **page** | **Integer**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1] |
| **limit** | **Integer**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10] |
| **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false] |

### Return type

[**AttributeOptions**](AttributeOptions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _embedded, _links, current_page, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return attribute options paginated |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="getAttributesAttributeCodeOptionsCode"></a>
# **getAttributesAttributeCodeOptionsCode**
> PostAttributesAttributeCodeOptionsRequest getAttributesAttributeCodeOptionsCode(attributeCode, code)

Get an attribute option

This endpoint allows you to get the information about a given attribute option.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeOptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeOptionApi apiInstance = new AttributeOptionApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | Code of the attribute
    String code = "code_example"; // String | Code of the resource
    try {
      PostAttributesAttributeCodeOptionsRequest result = apiInstance.getAttributesAttributeCodeOptionsCode(attributeCode, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeOptionApi#getAttributesAttributeCodeOptionsCode");
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
| **attributeCode** | **String**| Code of the attribute | |
| **code** | **String**| Code of the resource | |

### Return type

[**PostAttributesAttributeCodeOptionsRequest**](PostAttributesAttributeCodeOptionsRequest.md)

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

<a id="patchAttributesAttributeCodeOptions"></a>
# **patchAttributesAttributeCodeOptions**
> PatchAssetCategories200Response patchAttributesAttributeCodeOptions(attributeCode, body)

Update/create several attribute options

This endpoint allows you to update several attribute options at once.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeOptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeOptionApi apiInstance = new AttributeOptionApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | Code of the attribute
    PatchAttributesAttributeCodeOptionsRequest body = new PatchAttributesAttributeCodeOptionsRequest(); // PatchAttributesAttributeCodeOptionsRequest | 
    try {
      PatchAssetCategories200Response result = apiInstance.patchAttributesAttributeCodeOptions(attributeCode, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeOptionApi#patchAttributesAttributeCodeOptions");
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
| **attributeCode** | **String**| Code of the attribute | |
| **body** | [**PatchAttributesAttributeCodeOptionsRequest**](PatchAttributesAttributeCodeOptionsRequest.md)|  | [optional] |

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

<a id="patchAttributesAttributeCodeOptionsCode"></a>
# **patchAttributesAttributeCodeOptionsCode**
> patchAttributesAttributeCodeOptionsCode(attributeCode, code, body)

Update/create an attribute option

This endpoint allows you to update a given attribute option. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no attribute option exists for the given code, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeOptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeOptionApi apiInstance = new AttributeOptionApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | Code of the attribute
    String code = "code_example"; // String | Code of the resource
    PostAttributesAttributeCodeOptionsRequest body = new PostAttributesAttributeCodeOptionsRequest(); // PostAttributesAttributeCodeOptionsRequest | 
    try {
      apiInstance.patchAttributesAttributeCodeOptionsCode(attributeCode, code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeOptionApi#patchAttributesAttributeCodeOptionsCode");
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
| **attributeCode** | **String**| Code of the attribute | |
| **code** | **String**| Code of the resource | |
| **body** | [**PostAttributesAttributeCodeOptionsRequest**](PostAttributesAttributeCodeOptionsRequest.md)|  | |

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

<a id="postAttributesAttributeCodeOptions"></a>
# **postAttributesAttributeCodeOptions**
> postAttributesAttributeCodeOptions(attributeCode, body)

Create a new attribute option

This endpoint allows you to create a new attribute option.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeOptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AttributeOptionApi apiInstance = new AttributeOptionApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | Code of the attribute
    PostAttributesAttributeCodeOptionsRequest body = new PostAttributesAttributeCodeOptionsRequest(); // PostAttributesAttributeCodeOptionsRequest | 
    try {
      apiInstance.postAttributesAttributeCodeOptions(attributeCode, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeOptionApi#postAttributesAttributeCodeOptions");
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
| **attributeCode** | **String**| Code of the attribute | |
| **body** | [**PostAttributesAttributeCodeOptionsRequest**](PostAttributesAttributeCodeOptionsRequest.md)|  | [optional] |

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

