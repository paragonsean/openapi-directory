# PamAssetReferenceFileApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getReferenceFilesChannelCodeLocaleCodeDownload**](PamAssetReferenceFileApi.md#getReferenceFilesChannelCodeLocaleCodeDownload) | **GET** /api/rest/v1/assets/{asset_code}/reference-files/{locale_code}/download | Download a reference file |
| [**getReferenceFilesLocaleCode**](PamAssetReferenceFileApi.md#getReferenceFilesLocaleCode) | **GET** /api/rest/v1/assets/{asset_code}/reference-files/{locale_code} | Get a reference file |
| [**postReferenceFilesLocaleCode**](PamAssetReferenceFileApi.md#postReferenceFilesLocaleCode) | **POST** /api/rest/v1/assets/{asset_code}/reference-files/{locale_code} | Upload a new reference file |


<a id="getReferenceFilesChannelCodeLocaleCodeDownload"></a>
# **getReferenceFilesChannelCodeLocaleCodeDownload**
> getReferenceFilesChannelCodeLocaleCodeDownload(assetCode, localeCode)

Download a reference file

This endpoint allows you to download a given reference file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PamAssetReferenceFileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    PamAssetReferenceFileApi apiInstance = new PamAssetReferenceFileApi(defaultClient);
    String assetCode = "assetCode_example"; // String | Code of the asset
    String localeCode = "localeCode_example"; // String | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable
    try {
      apiInstance.getReferenceFilesChannelCodeLocaleCodeDownload(assetCode, localeCode);
    } catch (ApiException e) {
      System.err.println("Exception when calling PamAssetReferenceFileApi#getReferenceFilesChannelCodeLocaleCodeDownload");
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
| **assetCode** | **String**| Code of the asset | |
| **localeCode** | **String**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | |

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

<a id="getReferenceFilesLocaleCode"></a>
# **getReferenceFilesLocaleCode**
> GetReferenceFilesLocaleCode200Response getReferenceFilesLocaleCode(assetCode, localeCode)

Get a reference file

This endpoint allows you to get the information about a reference file of a given PAM asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PamAssetReferenceFileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    PamAssetReferenceFileApi apiInstance = new PamAssetReferenceFileApi(defaultClient);
    String assetCode = "assetCode_example"; // String | Code of the asset
    String localeCode = "localeCode_example"; // String | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable
    try {
      GetReferenceFilesLocaleCode200Response result = apiInstance.getReferenceFilesLocaleCode(assetCode, localeCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PamAssetReferenceFileApi#getReferenceFilesLocaleCode");
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
| **assetCode** | **String**| Code of the asset | |
| **localeCode** | **String**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | |

### Return type

[**GetReferenceFilesLocaleCode200Response**](GetReferenceFilesLocaleCode200Response.md)

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

<a id="postReferenceFilesLocaleCode"></a>
# **postReferenceFilesLocaleCode**
> PostReferenceFilesLocaleCode201Response postReferenceFilesLocaleCode(assetCode, localeCode, contentType, body)

Upload a new reference file

This endpoint allows you to upload a new reference file for a given PAM asset and locale. It will also automatically generate all the variation files corresponding to this reference file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PamAssetReferenceFileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    PamAssetReferenceFileApi apiInstance = new PamAssetReferenceFileApi(defaultClient);
    String assetCode = "assetCode_example"; // String | Code of the asset
    String localeCode = "localeCode_example"; // String | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable
    String contentType = "contentType_example"; // String | Equal to 'multipart/form-data', no other value allowed
    PostReferenceFilesLocaleCodeRequest body = new PostReferenceFilesLocaleCodeRequest(); // PostReferenceFilesLocaleCodeRequest | 
    try {
      PostReferenceFilesLocaleCode201Response result = apiInstance.postReferenceFilesLocaleCode(assetCode, localeCode, contentType, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PamAssetReferenceFileApi#postReferenceFilesLocaleCode");
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
| **assetCode** | **String**| Code of the asset | |
| **localeCode** | **String**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | |
| **contentType** | **String**| Equal to &#39;multipart/form-data&#39;, no other value allowed | |
| **body** | [**PostReferenceFilesLocaleCodeRequest**](PostReferenceFilesLocaleCodeRequest.md)|  | [optional] |

### Return type

[**PostReferenceFilesLocaleCode201Response**](PostReferenceFilesLocaleCode201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message, _links

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Uploaded |  * Location - URI of the created resource <br>  |
| **400** | Bad request |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **404** | Resource not found |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |

