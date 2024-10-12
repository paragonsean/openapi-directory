# AssetAttributeApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAssetFamiliesCodeAttributes**](AssetAttributeApi.md#getAssetFamiliesCodeAttributes) | **GET** /api/rest/v1/asset-families/{asset_family_code}/attributes | Get the list of attributes of a given asset family |
| [**getAssetFamilyAttributesCode**](AssetAttributeApi.md#getAssetFamilyAttributesCode) | **GET** /api/rest/v1/asset-families/{asset_family_code}/attributes/{code} | Get an attribute of a given asset family |
| [**patchAssetFamilyAttributesCode**](AssetAttributeApi.md#patchAssetFamilyAttributesCode) | **PATCH** /api/rest/v1/asset-families/{asset_family_code}/attributes/{code} | Update/create an attribute of a given asset family |


<a id="getAssetFamiliesCodeAttributes"></a>
# **getAssetFamiliesCodeAttributes**
> List&lt;GetAssetFamiliesCodeAttributes200ResponseInner&gt; getAssetFamiliesCodeAttributes(assetFamilyCode)

Get the list of attributes of a given asset family

This endpoint allows you to get the list of attributes of a given asset family.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetAttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssetAttributeApi apiInstance = new AssetAttributeApi(defaultClient);
    String assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
    try {
      List<GetAssetFamiliesCodeAttributes200ResponseInner> result = apiInstance.getAssetFamiliesCodeAttributes(assetFamilyCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetAttributeApi#getAssetFamiliesCodeAttributes");
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
| **assetFamilyCode** | **String**| Code of the asset family | |

### Return type

[**List&lt;GetAssetFamiliesCodeAttributes200ResponseInner&gt;**](GetAssetFamiliesCodeAttributes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the attributes of the given asset family |  -  |
| **401** | Authentication required |  -  |
| **406** | Not Acceptable |  -  |

<a id="getAssetFamilyAttributesCode"></a>
# **getAssetFamilyAttributesCode**
> GetAssetFamiliesCodeAttributes200ResponseInner getAssetFamilyAttributesCode(assetFamilyCode, code)

Get an attribute of a given asset family

This endpoint allows you to get the information about a given attribute for a given asset family.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetAttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssetAttributeApi apiInstance = new AssetAttributeApi(defaultClient);
    String assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
    String code = "code_example"; // String | Code of the resource
    try {
      GetAssetFamiliesCodeAttributes200ResponseInner result = apiInstance.getAssetFamilyAttributesCode(assetFamilyCode, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetAttributeApi#getAssetFamilyAttributesCode");
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
| **assetFamilyCode** | **String**| Code of the asset family | |
| **code** | **String**| Code of the resource | |

### Return type

[**GetAssetFamiliesCodeAttributes200ResponseInner**](GetAssetFamiliesCodeAttributes200ResponseInner.md)

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

<a id="patchAssetFamilyAttributesCode"></a>
# **patchAssetFamilyAttributesCode**
> patchAssetFamilyAttributesCode(assetFamilyCode, code, body)

Update/create an attribute of a given asset family

This endpoint allows you to update a given attribute for a given asset family. Note that if the attribute does not already exist for the given asset family, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetAttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssetAttributeApi apiInstance = new AssetAttributeApi(defaultClient);
    String assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
    String code = "code_example"; // String | Code of the resource
    GetAssetFamiliesCodeAttributes200ResponseInner body = new GetAssetFamiliesCodeAttributes200ResponseInner(); // GetAssetFamiliesCodeAttributes200ResponseInner | 
    try {
      apiInstance.patchAssetFamilyAttributesCode(assetFamilyCode, code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetAttributeApi#patchAssetFamilyAttributesCode");
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
| **assetFamilyCode** | **String**| Code of the asset family | |
| **code** | **String**| Code of the resource | |
| **body** | [**GetAssetFamiliesCodeAttributes200ResponseInner**](GetAssetFamiliesCodeAttributes200ResponseInner.md)|  | |

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

