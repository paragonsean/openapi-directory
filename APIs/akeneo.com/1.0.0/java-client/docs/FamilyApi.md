# FamilyApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFamilies**](FamilyApi.md#getFamilies) | **GET** /api/rest/v1/families | Get list of families |
| [**getFamiliesCode**](FamilyApi.md#getFamiliesCode) | **GET** /api/rest/v1/families/{code} | Get a family |
| [**patchFamilies**](FamilyApi.md#patchFamilies) | **PATCH** /api/rest/v1/families | Update/create several families |
| [**patchFamiliesCode**](FamilyApi.md#patchFamiliesCode) | **PATCH** /api/rest/v1/families/{code} | Update/create a family |
| [**postFamilies**](FamilyApi.md#postFamilies) | **POST** /api/rest/v1/families | Create a new family |
| [**postFamiliesFamilyCodeVariants**](FamilyApi.md#postFamiliesFamilyCodeVariants) | **POST** /api/rest/v1/families/{family_code}/variants | Create a new family variant |


<a id="getFamilies"></a>
# **getFamilies**
> Families getFamilies(search, page, limit, withCount)

Get list of families

This endpoint allows you to get a list of families. Families are paginated and sorted by code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FamilyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    FamilyApi apiInstance = new FamilyApi(defaultClient);
    String search = "search_example"; // String | Filter families, for more details see the <a href=\"/documentation/filter.html#filter-families\">Filters</a> section.
    Integer page = 1; // Integer | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
    Integer limit = 10; // Integer | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    Boolean withCount = false; // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    try {
      Families result = apiInstance.getFamilies(search, page, limit, withCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FamilyApi#getFamilies");
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
| **search** | **String**| Filter families, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-families\&quot;&gt;Filters&lt;/a&gt; section. | [optional] |
| **page** | **Integer**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1] |
| **limit** | **Integer**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10] |
| **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false] |

### Return type

[**Families**](Families.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _embedded, _links, current_page, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return families paginated |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="getFamiliesCode"></a>
# **getFamiliesCode**
> PostFamiliesRequest getFamiliesCode(code)

Get a family

This endpoint allows you to get the information about a given family.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FamilyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    FamilyApi apiInstance = new FamilyApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    try {
      PostFamiliesRequest result = apiInstance.getFamiliesCode(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FamilyApi#getFamiliesCode");
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

[**PostFamiliesRequest**](PostFamiliesRequest.md)

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

<a id="patchFamilies"></a>
# **patchFamilies**
> PatchAssetCategories200Response patchFamilies(body)

Update/create several families

This endpoint allows you to update and/or create several families at once.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FamilyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    FamilyApi apiInstance = new FamilyApi(defaultClient);
    PatchFamiliesRequest body = new PatchFamiliesRequest(); // PatchFamiliesRequest | 
    try {
      PatchAssetCategories200Response result = apiInstance.patchFamilies(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FamilyApi#patchFamilies");
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
| **body** | [**PatchFamiliesRequest**](PatchFamiliesRequest.md)|  | [optional] |

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

<a id="patchFamiliesCode"></a>
# **patchFamiliesCode**
> patchFamiliesCode(code, body)

Update/create a family

This endpoint allows you to update a given family. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no family exists for the given code, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FamilyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    FamilyApi apiInstance = new FamilyApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    PostFamiliesRequest body = new PostFamiliesRequest(); // PostFamiliesRequest | 
    try {
      apiInstance.patchFamiliesCode(code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling FamilyApi#patchFamiliesCode");
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
| **body** | [**PostFamiliesRequest**](PostFamiliesRequest.md)|  | |

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

<a id="postFamilies"></a>
# **postFamilies**
> postFamilies(body)

Create a new family

This endpoint allows you to create a new family.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FamilyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    FamilyApi apiInstance = new FamilyApi(defaultClient);
    PostFamiliesRequest body = new PostFamiliesRequest(); // PostFamiliesRequest | 
    try {
      apiInstance.postFamilies(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling FamilyApi#postFamilies");
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
| **body** | [**PostFamiliesRequest**](PostFamiliesRequest.md)|  | [optional] |

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

<a id="postFamiliesFamilyCodeVariants"></a>
# **postFamiliesFamilyCodeVariants**
> postFamiliesFamilyCodeVariants(familyCode, body)

Create a new family variant

This endpoint allows you to create a family variant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FamilyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    FamilyApi apiInstance = new FamilyApi(defaultClient);
    String familyCode = "familyCode_example"; // String | Code of the family
    PostFamiliesFamilyCodeVariantsRequest body = new PostFamiliesFamilyCodeVariantsRequest(); // PostFamiliesFamilyCodeVariantsRequest | 
    try {
      apiInstance.postFamiliesFamilyCodeVariants(familyCode, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling FamilyApi#postFamiliesFamilyCodeVariants");
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
| **familyCode** | **String**| Code of the family | |
| **body** | [**PostFamiliesFamilyCodeVariantsRequest**](PostFamiliesFamilyCodeVariantsRequest.md)|  | [optional] |

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

