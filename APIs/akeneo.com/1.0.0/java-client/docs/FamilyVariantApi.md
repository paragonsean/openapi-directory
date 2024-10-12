# FamilyVariantApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFamiliesFamilyCodeVariants**](FamilyVariantApi.md#getFamiliesFamilyCodeVariants) | **GET** /api/rest/v1/families/{family_code}/variants | Get list of family variants |
| [**getFamiliesFamilyCodeVariantsCode**](FamilyVariantApi.md#getFamiliesFamilyCodeVariantsCode) | **GET** /api/rest/v1/families/{family_code}/variants/{code} | Get a family variant |
| [**patchFamiliesFamilyCodeVariants**](FamilyVariantApi.md#patchFamiliesFamilyCodeVariants) | **PATCH** /api/rest/v1/families/{family_code}/variants | Update/create several family variants |
| [**patchFamiliesFamilyCodeVariantsCode**](FamilyVariantApi.md#patchFamiliesFamilyCodeVariantsCode) | **PATCH** /api/rest/v1/families/{family_code}/variants/{code} | Update/create a family variant |


<a id="getFamiliesFamilyCodeVariants"></a>
# **getFamiliesFamilyCodeVariants**
> FamilyVariants getFamiliesFamilyCodeVariants(familyCode, page, limit, withCount)

Get list of family variants

This endpoint allows you to get a list of family variants. Family variants are paginated and sorted by code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FamilyVariantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    FamilyVariantApi apiInstance = new FamilyVariantApi(defaultClient);
    String familyCode = "familyCode_example"; // String | Code of the family
    Integer page = 1; // Integer | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
    Integer limit = 10; // Integer | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    Boolean withCount = false; // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    try {
      FamilyVariants result = apiInstance.getFamiliesFamilyCodeVariants(familyCode, page, limit, withCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FamilyVariantApi#getFamiliesFamilyCodeVariants");
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
| **page** | **Integer**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1] |
| **limit** | **Integer**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10] |
| **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false] |

### Return type

[**FamilyVariants**](FamilyVariants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, labels, variant_attribute_sets, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return family variants paginated |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="getFamiliesFamilyCodeVariantsCode"></a>
# **getFamiliesFamilyCodeVariantsCode**
> PostFamiliesFamilyCodeVariantsRequest getFamiliesFamilyCodeVariantsCode(familyCode, code)

Get a family variant

This endpoint allows you to get the information about a given family variant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FamilyVariantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    FamilyVariantApi apiInstance = new FamilyVariantApi(defaultClient);
    String familyCode = "familyCode_example"; // String | Code of the family
    String code = "code_example"; // String | Code of the resource
    try {
      PostFamiliesFamilyCodeVariantsRequest result = apiInstance.getFamiliesFamilyCodeVariantsCode(familyCode, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FamilyVariantApi#getFamiliesFamilyCodeVariantsCode");
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
| **code** | **String**| Code of the resource | |

### Return type

[**PostFamiliesFamilyCodeVariantsRequest**](PostFamiliesFamilyCodeVariantsRequest.md)

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

<a id="patchFamiliesFamilyCodeVariants"></a>
# **patchFamiliesFamilyCodeVariants**
> PatchAssetCategories200Response patchFamiliesFamilyCodeVariants(familyCode, body)

Update/create several family variants

This endpoint allows you to update and/or create several family variants at once, for a given family.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FamilyVariantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    FamilyVariantApi apiInstance = new FamilyVariantApi(defaultClient);
    String familyCode = "familyCode_example"; // String | Code of the family
    PatchFamiliesFamilyCodeVariantsRequest body = new PatchFamiliesFamilyCodeVariantsRequest(); // PatchFamiliesFamilyCodeVariantsRequest | 
    try {
      PatchAssetCategories200Response result = apiInstance.patchFamiliesFamilyCodeVariants(familyCode, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FamilyVariantApi#patchFamiliesFamilyCodeVariants");
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
| **body** | [**PatchFamiliesFamilyCodeVariantsRequest**](PatchFamiliesFamilyCodeVariantsRequest.md)|  | [optional] |

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

<a id="patchFamiliesFamilyCodeVariantsCode"></a>
# **patchFamiliesFamilyCodeVariantsCode**
> patchFamiliesFamilyCodeVariantsCode(familyCode, code, body)

Update/create a family variant

This endpoint allows you to update a given family variant. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no family variant exists for the given code, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FamilyVariantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    FamilyVariantApi apiInstance = new FamilyVariantApi(defaultClient);
    String familyCode = "familyCode_example"; // String | Code of the family
    String code = "code_example"; // String | Code of the resource
    PostFamiliesFamilyCodeVariantsRequest body = new PostFamiliesFamilyCodeVariantsRequest(); // PostFamiliesFamilyCodeVariantsRequest | 
    try {
      apiInstance.patchFamiliesFamilyCodeVariantsCode(familyCode, code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling FamilyVariantApi#patchFamiliesFamilyCodeVariantsCode");
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
| **code** | **String**| Code of the resource | |
| **body** | [**PostFamiliesFamilyCodeVariantsRequest**](PostFamiliesFamilyCodeVariantsRequest.md)|  | |

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

