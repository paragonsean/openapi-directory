# PamAssetVariationFileApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVariationFilesChannelCodeLocaleCode**](PamAssetVariationFileApi.md#getVariationFilesChannelCodeLocaleCode) | **GET** /api/rest/v1/assets/{asset_code}/variation-files/{channel_code}/{locale_code} | Get a variation file |
| [**getVariationFilesChannelCodeLocaleCodeDownload**](PamAssetVariationFileApi.md#getVariationFilesChannelCodeLocaleCodeDownload) | **GET** /api/rest/v1/assets/{asset_code}/variation-files/{channel_code}/{locale_code}/download | Download a variation file |
| [**postVariationFilesChannelCodeLocaleCode**](PamAssetVariationFileApi.md#postVariationFilesChannelCodeLocaleCode) | **POST** /api/rest/v1/assets/{asset_code}/variation-files/{channel_code}/{locale_code} | Upload a new variation file |


<a id="getVariationFilesChannelCodeLocaleCode"></a>
# **getVariationFilesChannelCodeLocaleCode**
> GetVariationFilesChannelCodeLocaleCode200Response getVariationFilesChannelCodeLocaleCode(assetCode, channelCode, localeCode)

Get a variation file

This endpoint allows you to get the information about a variation file of a given PAM asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PamAssetVariationFileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    PamAssetVariationFileApi apiInstance = new PamAssetVariationFileApi(defaultClient);
    String assetCode = "assetCode_example"; // String | Code of the asset
    String channelCode = "channelCode_example"; // String | Code of the channel
    String localeCode = "localeCode_example"; // String | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable
    try {
      GetVariationFilesChannelCodeLocaleCode200Response result = apiInstance.getVariationFilesChannelCodeLocaleCode(assetCode, channelCode, localeCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PamAssetVariationFileApi#getVariationFilesChannelCodeLocaleCode");
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
| **channelCode** | **String**| Code of the channel | |
| **localeCode** | **String**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | |

### Return type

[**GetVariationFilesChannelCodeLocaleCode200Response**](GetVariationFilesChannelCodeLocaleCode200Response.md)

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

<a id="getVariationFilesChannelCodeLocaleCodeDownload"></a>
# **getVariationFilesChannelCodeLocaleCodeDownload**
> getVariationFilesChannelCodeLocaleCodeDownload(assetCode, channelCode, localeCode)

Download a variation file

This endpoint allows you to download a given variation file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PamAssetVariationFileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    PamAssetVariationFileApi apiInstance = new PamAssetVariationFileApi(defaultClient);
    String assetCode = "assetCode_example"; // String | Code of the asset
    String channelCode = "channelCode_example"; // String | Code of the channel
    String localeCode = "localeCode_example"; // String | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable
    try {
      apiInstance.getVariationFilesChannelCodeLocaleCodeDownload(assetCode, channelCode, localeCode);
    } catch (ApiException e) {
      System.err.println("Exception when calling PamAssetVariationFileApi#getVariationFilesChannelCodeLocaleCodeDownload");
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
| **channelCode** | **String**| Code of the channel | |
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

<a id="postVariationFilesChannelCodeLocaleCode"></a>
# **postVariationFilesChannelCodeLocaleCode**
> postVariationFilesChannelCodeLocaleCode(assetCode, channelCode, localeCode, contentType, body)

Upload a new variation file

This endpoint allows you to upload a new variation file for a given PAM asset, channel and locale.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PamAssetVariationFileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    PamAssetVariationFileApi apiInstance = new PamAssetVariationFileApi(defaultClient);
    String assetCode = "assetCode_example"; // String | Code of the asset
    String channelCode = "channelCode_example"; // String | Code of the channel
    String localeCode = "localeCode_example"; // String | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable
    String contentType = "contentType_example"; // String | Equal to 'multipart/form-data', no other value allowed
    PostReferenceFilesLocaleCodeRequest body = new PostReferenceFilesLocaleCodeRequest(); // PostReferenceFilesLocaleCodeRequest | 
    try {
      apiInstance.postVariationFilesChannelCodeLocaleCode(assetCode, channelCode, localeCode, contentType, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PamAssetVariationFileApi#postVariationFilesChannelCodeLocaleCode");
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
| **channelCode** | **String**| Code of the channel | |
| **localeCode** | **String**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | |
| **contentType** | **String**| Equal to &#39;multipart/form-data&#39;, no other value allowed | |
| **body** | [**PostReferenceFilesLocaleCodeRequest**](PostReferenceFilesLocaleCodeRequest.md)|  | [optional] |

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
| **404** | Resource not found |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |

