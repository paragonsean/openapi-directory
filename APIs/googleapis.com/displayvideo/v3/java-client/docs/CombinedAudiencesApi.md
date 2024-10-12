# CombinedAudiencesApi

All URIs are relative to *https://displayvideo.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**displayvideoCombinedAudiencesGet**](CombinedAudiencesApi.md#displayvideoCombinedAudiencesGet) | **GET** /v3/combinedAudiences/{combinedAudienceId} |  |
| [**displayvideoCombinedAudiencesList**](CombinedAudiencesApi.md#displayvideoCombinedAudiencesList) | **GET** /v3/combinedAudiences |  |


<a id="displayvideoCombinedAudiencesGet"></a>
# **displayvideoCombinedAudiencesGet**
> CombinedAudience displayvideoCombinedAudiencesGet(combinedAudienceId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserId, partnerId)



Gets a combined audience.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CombinedAudiencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://displayvideo.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CombinedAudiencesApi apiInstance = new CombinedAudiencesApi(defaultClient);
    String combinedAudienceId = "combinedAudienceId_example"; // String | Required. The ID of the combined audience to fetch.
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
    String advertiserId = "advertiserId_example"; // String | The ID of the advertiser that has access to the fetched combined audience.
    String partnerId = "partnerId_example"; // String | The ID of the partner that has access to the fetched combined audience.
    try {
      CombinedAudience result = apiInstance.displayvideoCombinedAudiencesGet(combinedAudienceId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserId, partnerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CombinedAudiencesApi#displayvideoCombinedAudiencesGet");
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
| **combinedAudienceId** | **String**| Required. The ID of the combined audience to fetch. | |
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
| **advertiserId** | **String**| The ID of the advertiser that has access to the fetched combined audience. | [optional] |
| **partnerId** | **String**| The ID of the partner that has access to the fetched combined audience. | [optional] |

### Return type

[**CombinedAudience**](CombinedAudience.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="displayvideoCombinedAudiencesList"></a>
# **displayvideoCombinedAudiencesList**
> ListCombinedAudiencesResponse displayvideoCombinedAudiencesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserId, filter, orderBy, pageSize, pageToken, partnerId)



Lists combined audiences. The order is defined by the order_by parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CombinedAudiencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://displayvideo.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CombinedAudiencesApi apiInstance = new CombinedAudiencesApi(defaultClient);
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
    String advertiserId = "advertiserId_example"; // String | The ID of the advertiser that has access to the fetched combined audiences.
    String filter = "filter_example"; // String | Allows filtering by combined audience fields. Supported syntax: * Filter expressions for combined audiences can only contain at most one restriction. * A restriction has the form of `{field} {operator} {value}`. * All fields must use the `HAS (:)` operator. Supported fields: * `displayName` Examples: * All combined audiences for which the display name contains \"Google\": `displayName : \"Google\"`. The length of this field should be no more than 500 characters. Reference our [filter `LIST` requests](/display-video/api/guides/how-tos/filters) guide for more information.
    String orderBy = "orderBy_example"; // String | Field by which to sort the list. Acceptable values are: * `combinedAudienceId` (default) * `displayName` The default sorting order is ascending. To specify descending order for a field, a suffix \"desc\" should be added to the field name. Example: `displayName desc`.
    Integer pageSize = 56; // Integer | Requested page size. Must be between `1` and `200`. If unspecified will default to `100`. Returns error code `INVALID_ARGUMENT` if an invalid value is specified.
    String pageToken = "pageToken_example"; // String | A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to `ListCombinedAudiences` method. If not specified, the first page of results will be returned.
    String partnerId = "partnerId_example"; // String | The ID of the partner that has access to the fetched combined audiences.
    try {
      ListCombinedAudiencesResponse result = apiInstance.displayvideoCombinedAudiencesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserId, filter, orderBy, pageSize, pageToken, partnerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CombinedAudiencesApi#displayvideoCombinedAudiencesList");
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
| **advertiserId** | **String**| The ID of the advertiser that has access to the fetched combined audiences. | [optional] |
| **filter** | **String**| Allows filtering by combined audience fields. Supported syntax: * Filter expressions for combined audiences can only contain at most one restriction. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;HAS (:)&#x60; operator. Supported fields: * &#x60;displayName&#x60; Examples: * All combined audiences for which the display name contains \&quot;Google\&quot;: &#x60;displayName : \&quot;Google\&quot;&#x60;. The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information. | [optional] |
| **orderBy** | **String**| Field by which to sort the list. Acceptable values are: * &#x60;combinedAudienceId&#x60; (default) * &#x60;displayName&#x60; The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;displayName desc&#x60;. | [optional] |
| **pageSize** | **Integer**| Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified. | [optional] |
| **pageToken** | **String**| A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListCombinedAudiences&#x60; method. If not specified, the first page of results will be returned. | [optional] |
| **partnerId** | **String**| The ID of the partner that has access to the fetched combined audiences. | [optional] |

### Return type

[**ListCombinedAudiencesResponse**](ListCombinedAudiencesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

