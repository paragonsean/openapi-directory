# AssetAttributeOptionApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAssetAttributesAttributeCodeOptionsCode**](AssetAttributeOptionApi.md#getAssetAttributesAttributeCodeOptionsCode) | **GET** /api/rest/v1/asset-families/{asset_family_code}/attributes/{attribute_code}/options/{code} | Get an attribute option for a given attribute of a given asset family |
| [**getAssetFamilyAttributesAttributeCodeOptions**](AssetAttributeOptionApi.md#getAssetFamilyAttributesAttributeCodeOptions) | **GET** /api/rest/v1/asset-families/{asset_family_code}/attributes/{attribute_code}/options | Get a list of attribute options of a given attribute for a given asset family |
| [**patchAssetAttributesAttributeCodeOptionsCode**](AssetAttributeOptionApi.md#patchAssetAttributesAttributeCodeOptionsCode) | **PATCH** /api/rest/v1/asset-families/{asset_family_code}/attributes/{attribute_code}/options/{code} | Update/create an asset attribute option for a given asset family |


<a id="getAssetAttributesAttributeCodeOptionsCode"></a>
# **getAssetAttributesAttributeCodeOptionsCode**
> GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner getAssetAttributesAttributeCodeOptionsCode(assetFamilyCode, attributeCode, code)

Get an attribute option for a given attribute of a given asset family

This endpoint allows you to get the information about a given asset attribute option.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetAttributeOptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssetAttributeOptionApi apiInstance = new AssetAttributeOptionApi(defaultClient);
    String assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
    String attributeCode = "attributeCode_example"; // String | Code of the attribute
    String code = "code_example"; // String | Code of the resource
    try {
      GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner result = apiInstance.getAssetAttributesAttributeCodeOptionsCode(assetFamilyCode, attributeCode, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetAttributeOptionApi#getAssetAttributesAttributeCodeOptionsCode");
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
| **attributeCode** | **String**| Code of the attribute | |
| **code** | **String**| Code of the resource | |

### Return type

[**GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner**](GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner.md)

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

<a id="getAssetFamilyAttributesAttributeCodeOptions"></a>
# **getAssetFamilyAttributesAttributeCodeOptions**
> List&lt;GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner&gt; getAssetFamilyAttributesAttributeCodeOptions(assetFamilyCode, attributeCode)

Get a list of attribute options of a given attribute for a given asset family

This endpoint allows you to get a list of attribute options for a given asset family.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetAttributeOptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssetAttributeOptionApi apiInstance = new AssetAttributeOptionApi(defaultClient);
    String assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
    String attributeCode = "attributeCode_example"; // String | Code of the attribute
    try {
      List<GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner> result = apiInstance.getAssetFamilyAttributesAttributeCodeOptions(assetFamilyCode, attributeCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetAttributeOptionApi#getAssetFamilyAttributesAttributeCodeOptions");
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
| **attributeCode** | **String**| Code of the attribute | |

### Return type

[**List&lt;GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner&gt;**](GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the options of the given attribute of the given asset family |  -  |
| **401** | Authentication required |  -  |
| **406** | Not Acceptable |  -  |

<a id="patchAssetAttributesAttributeCodeOptionsCode"></a>
# **patchAssetAttributesAttributeCodeOptionsCode**
> patchAssetAttributesAttributeCodeOptionsCode(assetFamilyCode, attributeCode, code, body)

Update/create an asset attribute option for a given asset family

This endpoint allows you to update a given option for a given attribute and a given asset family. Learn more about the &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the option does not already exist for the given attribute of the given asset family, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetAttributeOptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssetAttributeOptionApi apiInstance = new AssetAttributeOptionApi(defaultClient);
    String assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
    String attributeCode = "attributeCode_example"; // String | Code of the attribute
    String code = "code_example"; // String | Code of the resource
    GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner body = new GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner(); // GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner | 
    try {
      apiInstance.patchAssetAttributesAttributeCodeOptionsCode(assetFamilyCode, attributeCode, code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetAttributeOptionApi#patchAssetAttributesAttributeCodeOptionsCode");
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
| **attributeCode** | **String**| Code of the attribute | |
| **code** | **String**| Code of the resource | |
| **body** | [**GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner**](GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner.md)|  | |

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

