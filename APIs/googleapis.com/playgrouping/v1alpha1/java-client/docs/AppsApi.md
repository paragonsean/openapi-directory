# AppsApi

All URIs are relative to *https://playgrouping.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**playgroupingAppsTokensTagsCreateOrUpdate**](AppsApi.md#playgroupingAppsTokensTagsCreateOrUpdate) | **POST** /v1alpha1/{appPackage}/{token}/tags:createOrUpdate |  |
| [**playgroupingAppsTokensVerify**](AppsApi.md#playgroupingAppsTokensVerify) | **POST** /v1alpha1/{appPackage}/{token}:verify |  |


<a id="playgroupingAppsTokensTagsCreateOrUpdate"></a>
# **playgroupingAppsTokensTagsCreateOrUpdate**
> CreateOrUpdateTagsResponse playgroupingAppsTokensTagsCreateOrUpdate(appPackage, token, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, createOrUpdateTagsRequest)



Create or update tags for the user and app that are represented by the given token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://playgrouping.googleapis.com");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String appPackage = "appPackage_example"; // String | Required. App whose tags are being manipulated. Format: apps/{package_name}
    String token = "token_example"; // String | Required. Token for which the tags are being inserted or updated. Format: tokens/{token}
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    CreateOrUpdateTagsRequest createOrUpdateTagsRequest = new CreateOrUpdateTagsRequest(); // CreateOrUpdateTagsRequest | 
    try {
      CreateOrUpdateTagsResponse result = apiInstance.playgroupingAppsTokensTagsCreateOrUpdate(appPackage, token, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, createOrUpdateTagsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#playgroupingAppsTokensTagsCreateOrUpdate");
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
| **appPackage** | **String**| Required. App whose tags are being manipulated. Format: apps/{package_name} | |
| **token** | **String**| Required. Token for which the tags are being inserted or updated. Format: tokens/{token} | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **createOrUpdateTagsRequest** | [**CreateOrUpdateTagsRequest**](CreateOrUpdateTagsRequest.md)|  | [optional] |

### Return type

[**CreateOrUpdateTagsResponse**](CreateOrUpdateTagsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="playgroupingAppsTokensVerify"></a>
# **playgroupingAppsTokensVerify**
> Object playgroupingAppsTokensVerify(appPackage, token, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, verifyTokenRequest)



Verify an API token by asserting the app and persona it belongs to. The verification is a protection against client-side attacks and will fail if the contents of the token don&#39;t match the provided values. A token must be verified before it can be used to manipulate user tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://playgrouping.googleapis.com");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String appPackage = "appPackage_example"; // String | Required. App the token belongs to. Format: apps/{package_name}
    String token = "token_example"; // String | Required. The token to be verified. Format: tokens/{token}
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    VerifyTokenRequest verifyTokenRequest = new VerifyTokenRequest(); // VerifyTokenRequest | 
    try {
      Object result = apiInstance.playgroupingAppsTokensVerify(appPackage, token, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, verifyTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#playgroupingAppsTokensVerify");
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
| **appPackage** | **String**| Required. App the token belongs to. Format: apps/{package_name} | |
| **token** | **String**| Required. The token to be verified. Format: tokens/{token} | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **verifyTokenRequest** | [**VerifyTokenRequest**](VerifyTokenRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

