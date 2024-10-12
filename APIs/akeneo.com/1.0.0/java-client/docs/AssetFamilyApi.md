# AssetFamilyApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAssetFamilies**](AssetFamilyApi.md#getAssetFamilies) | **GET** /api/rest/v1/asset-families | Get list of asset families |
| [**getAssetFamilyCode**](AssetFamilyApi.md#getAssetFamilyCode) | **GET** /api/rest/v1/asset-families/{code} | Get an asset family |
| [**patchAssetFamilyCode**](AssetFamilyApi.md#patchAssetFamilyCode) | **PATCH** /api/rest/v1/asset-families/{code} | Update/create an asset family |


<a id="getAssetFamilies"></a>
# **getAssetFamilies**
> AssetFamilies getAssetFamilies(searchAfter)

Get list of asset families

This endpoint allows you to get a list of asset families. Asset families are paginated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetFamilyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssetFamilyApi apiInstance = new AssetFamilyApi(defaultClient);
    String searchAfter = "cursor to the first page"; // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    try {
      AssetFamilies result = apiInstance.getAssetFamilies(searchAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetFamilyApi#getAssetFamilies");
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
| **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to cursor to the first page] |

### Return type

[**AssetFamilies**](AssetFamilies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _embedded, _links, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return asset families paginated |  -  |
| **401** | Authentication required |  -  |
| **406** | Not Acceptable |  -  |

<a id="getAssetFamilyCode"></a>
# **getAssetFamilyCode**
> GetAssetFamilyCode200Response getAssetFamilyCode(code)

Get an asset family

This endpoint allows you to get the information about a given asset family.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetFamilyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssetFamilyApi apiInstance = new AssetFamilyApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    try {
      GetAssetFamilyCode200Response result = apiInstance.getAssetFamilyCode(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetFamilyApi#getAssetFamilyCode");
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

[**GetAssetFamilyCode200Response**](GetAssetFamilyCode200Response.md)

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
| **404** | Resource not found |  -  |
| **406** | Not Acceptable |  -  |

<a id="patchAssetFamilyCode"></a>
# **patchAssetFamilyCode**
> patchAssetFamilyCode(code, body)

Update/create an asset family

This endpoint allows you to update a given asset family. Note that if the asset family does not already exist, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetFamilyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssetFamilyApi apiInstance = new AssetFamilyApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    GetAssetFamilyCode200Response body = new GetAssetFamilyCode200Response(); // GetAssetFamilyCode200Response | 
    try {
      apiInstance.patchAssetFamilyCode(code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetFamilyApi#patchAssetFamilyCode");
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
| **body** | [**GetAssetFamilyCode200Response**](GetAssetFamilyCode200Response.md)|  | |

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
| **401** | Authentication required |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |

