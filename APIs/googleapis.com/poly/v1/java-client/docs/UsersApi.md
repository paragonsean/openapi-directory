# UsersApi

All URIs are relative to *https://poly.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**polyUsersAssetsList**](UsersApi.md#polyUsersAssetsList) | **GET** /v1/{name}/assets |  |
| [**polyUsersLikedassetsList**](UsersApi.md#polyUsersLikedassetsList) | **GET** /v1/{name}/likedassets |  |


<a id="polyUsersAssetsList"></a>
# **polyUsersAssetsList**
> ListUserAssetsResponse polyUsersAssetsList(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, format, orderBy, pageSize, pageToken, visibility)



Lists assets authored by the given user. Only the value &#39;me&#39;, representing the currently-authenticated user, is supported. May include assets with an access level of PRIVATE or UNLISTED and assets which are All Rights Reserved for the currently-authenticated user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://poly.googleapis.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String name = "name_example"; // String | A valid user id. Currently, only the special value 'me', representing the currently-authenticated user is supported. To use 'me', you must pass an OAuth token with the request.
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
    String format = "format_example"; // String | Return only assets with the matching format. Acceptable values are: `BLOCKS`, `FBX`, `GLTF`, `GLTF2`, `OBJ`, and `TILT`.
    String orderBy = "orderBy_example"; // String | Specifies an ordering for assets. Acceptable values are: `BEST`, `NEWEST`, `OLDEST`. Defaults to `BEST`, which ranks assets based on a combination of popularity and other features.
    Integer pageSize = 56; // Integer | The maximum number of assets to be returned. This value must be between `1` and `100`. Defaults to `20`.
    String pageToken = "pageToken_example"; // String | Specifies a continuation token from a previous search whose results were split into multiple pages. To get the next page, submit the same request specifying the value from next_page_token.
    String visibility = "VISIBILITY_UNSPECIFIED"; // String | The visibility of the assets to be returned. Defaults to VISIBILITY_UNSPECIFIED which returns all assets.
    try {
      ListUserAssetsResponse result = apiInstance.polyUsersAssetsList(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, format, orderBy, pageSize, pageToken, visibility);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#polyUsersAssetsList");
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
| **name** | **String**| A valid user id. Currently, only the special value &#39;me&#39;, representing the currently-authenticated user is supported. To use &#39;me&#39;, you must pass an OAuth token with the request. | |
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
| **format** | **String**| Return only assets with the matching format. Acceptable values are: &#x60;BLOCKS&#x60;, &#x60;FBX&#x60;, &#x60;GLTF&#x60;, &#x60;GLTF2&#x60;, &#x60;OBJ&#x60;, and &#x60;TILT&#x60;. | [optional] |
| **orderBy** | **String**| Specifies an ordering for assets. Acceptable values are: &#x60;BEST&#x60;, &#x60;NEWEST&#x60;, &#x60;OLDEST&#x60;. Defaults to &#x60;BEST&#x60;, which ranks assets based on a combination of popularity and other features. | [optional] |
| **pageSize** | **Integer**| The maximum number of assets to be returned. This value must be between &#x60;1&#x60; and &#x60;100&#x60;. Defaults to &#x60;20&#x60;. | [optional] |
| **pageToken** | **String**| Specifies a continuation token from a previous search whose results were split into multiple pages. To get the next page, submit the same request specifying the value from next_page_token. | [optional] |
| **visibility** | **String**| The visibility of the assets to be returned. Defaults to VISIBILITY_UNSPECIFIED which returns all assets. | [optional] [enum: VISIBILITY_UNSPECIFIED, PUBLISHED, PRIVATE] |

### Return type

[**ListUserAssetsResponse**](ListUserAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="polyUsersLikedassetsList"></a>
# **polyUsersLikedassetsList**
> ListLikedAssetsResponse polyUsersLikedassetsList(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, format, orderBy, pageSize, pageToken)



Lists assets that the user has liked. Only the value &#39;me&#39;, representing the currently-authenticated user, is supported. May include assets with an access level of UNLISTED.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://poly.googleapis.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String name = "name_example"; // String | A valid user id. Currently, only the special value 'me', representing the currently-authenticated user is supported. To use 'me', you must pass an OAuth token with the request.
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
    String format = "format_example"; // String | Return only assets with the matching format. Acceptable values are: `BLOCKS`, `FBX`, `GLTF`, `GLTF2`, `OBJ`, `TILT`.
    String orderBy = "orderBy_example"; // String | Specifies an ordering for assets. Acceptable values are: `BEST`, `NEWEST`, `OLDEST`, 'LIKED_TIME'. Defaults to `LIKED_TIME`, which ranks assets based on how recently they were liked.
    Integer pageSize = 56; // Integer | The maximum number of assets to be returned. This value must be between `1` and `100`. Defaults to `20`.
    String pageToken = "pageToken_example"; // String | Specifies a continuation token from a previous search whose results were split into multiple pages. To get the next page, submit the same request specifying the value from next_page_token.
    try {
      ListLikedAssetsResponse result = apiInstance.polyUsersLikedassetsList(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, format, orderBy, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#polyUsersLikedassetsList");
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
| **name** | **String**| A valid user id. Currently, only the special value &#39;me&#39;, representing the currently-authenticated user is supported. To use &#39;me&#39;, you must pass an OAuth token with the request. | |
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
| **format** | **String**| Return only assets with the matching format. Acceptable values are: &#x60;BLOCKS&#x60;, &#x60;FBX&#x60;, &#x60;GLTF&#x60;, &#x60;GLTF2&#x60;, &#x60;OBJ&#x60;, &#x60;TILT&#x60;. | [optional] |
| **orderBy** | **String**| Specifies an ordering for assets. Acceptable values are: &#x60;BEST&#x60;, &#x60;NEWEST&#x60;, &#x60;OLDEST&#x60;, &#39;LIKED_TIME&#39;. Defaults to &#x60;LIKED_TIME&#x60;, which ranks assets based on how recently they were liked. | [optional] |
| **pageSize** | **Integer**| The maximum number of assets to be returned. This value must be between &#x60;1&#x60; and &#x60;100&#x60;. Defaults to &#x60;20&#x60;. | [optional] |
| **pageToken** | **String**| Specifies a continuation token from a previous search whose results were split into multiple pages. To get the next page, submit the same request specifying the value from next_page_token. | [optional] |

### Return type

[**ListLikedAssetsResponse**](ListLikedAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

