# PartnersApi

All URIs are relative to *https://displayvideo.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**displayvideoPartnersBulkEditPartnerAssignedTargetingOptions**](PartnersApi.md#displayvideoPartnersBulkEditPartnerAssignedTargetingOptions) | **POST** /v1/partners/{partnerId}:bulkEditPartnerAssignedTargetingOptions |  |
| [**displayvideoPartnersChannelsCreate**](PartnersApi.md#displayvideoPartnersChannelsCreate) | **POST** /v1/partners/{partnerId}/channels |  |
| [**displayvideoPartnersChannelsList**](PartnersApi.md#displayvideoPartnersChannelsList) | **GET** /v1/partners/{partnerId}/channels |  |
| [**displayvideoPartnersChannelsPatch**](PartnersApi.md#displayvideoPartnersChannelsPatch) | **PATCH** /v1/partners/{partnerId}/channels/{channelId} |  |
| [**displayvideoPartnersChannelsSitesBulkEdit**](PartnersApi.md#displayvideoPartnersChannelsSitesBulkEdit) | **POST** /v1/partners/{partnerId}/channels/{channelId}/sites:bulkEdit |  |
| [**displayvideoPartnersChannelsSitesDelete**](PartnersApi.md#displayvideoPartnersChannelsSitesDelete) | **DELETE** /v1/partners/{partnerId}/channels/{channelId}/sites/{urlOrAppId} |  |
| [**displayvideoPartnersChannelsSitesList**](PartnersApi.md#displayvideoPartnersChannelsSitesList) | **GET** /v1/partners/{partnerId}/channels/{channelId}/sites |  |
| [**displayvideoPartnersChannelsSitesReplace**](PartnersApi.md#displayvideoPartnersChannelsSitesReplace) | **POST** /v1/partners/{partnerId}/channels/{channelId}/sites:replace |  |
| [**displayvideoPartnersGet**](PartnersApi.md#displayvideoPartnersGet) | **GET** /v1/partners/{partnerId} |  |
| [**displayvideoPartnersList**](PartnersApi.md#displayvideoPartnersList) | **GET** /v1/partners |  |
| [**displayvideoPartnersTargetingTypesAssignedTargetingOptionsCreate**](PartnersApi.md#displayvideoPartnersTargetingTypesAssignedTargetingOptionsCreate) | **POST** /v1/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions |  |
| [**displayvideoPartnersTargetingTypesAssignedTargetingOptionsDelete**](PartnersApi.md#displayvideoPartnersTargetingTypesAssignedTargetingOptionsDelete) | **DELETE** /v1/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId} |  |
| [**displayvideoPartnersTargetingTypesAssignedTargetingOptionsGet**](PartnersApi.md#displayvideoPartnersTargetingTypesAssignedTargetingOptionsGet) | **GET** /v1/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId} |  |
| [**displayvideoPartnersTargetingTypesAssignedTargetingOptionsList**](PartnersApi.md#displayvideoPartnersTargetingTypesAssignedTargetingOptionsList) | **GET** /v1/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions |  |


<a id="displayvideoPartnersBulkEditPartnerAssignedTargetingOptions"></a>
# **displayvideoPartnersBulkEditPartnerAssignedTargetingOptions**
> BulkEditPartnerAssignedTargetingOptionsResponse displayvideoPartnersBulkEditPartnerAssignedTargetingOptions(partnerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, bulkEditPartnerAssignedTargetingOptionsRequest)



Bulk edits targeting options under a single partner. The operation will delete the assigned targeting options provided in BulkEditPartnerAssignedTargetingOptionsRequest.deleteRequests and then create the assigned targeting options provided in BulkEditPartnerAssignedTargetingOptionsRequest.createRequests .

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

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

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerId = "partnerId_example"; // String | Required. The ID of the partner.
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
    BulkEditPartnerAssignedTargetingOptionsRequest bulkEditPartnerAssignedTargetingOptionsRequest = new BulkEditPartnerAssignedTargetingOptionsRequest(); // BulkEditPartnerAssignedTargetingOptionsRequest | 
    try {
      BulkEditPartnerAssignedTargetingOptionsResponse result = apiInstance.displayvideoPartnersBulkEditPartnerAssignedTargetingOptions(partnerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, bulkEditPartnerAssignedTargetingOptionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#displayvideoPartnersBulkEditPartnerAssignedTargetingOptions");
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
| **partnerId** | **String**| Required. The ID of the partner. | |
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
| **bulkEditPartnerAssignedTargetingOptionsRequest** | [**BulkEditPartnerAssignedTargetingOptionsRequest**](BulkEditPartnerAssignedTargetingOptionsRequest.md)|  | [optional] |

### Return type

[**BulkEditPartnerAssignedTargetingOptionsResponse**](BulkEditPartnerAssignedTargetingOptionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="displayvideoPartnersChannelsCreate"></a>
# **displayvideoPartnersChannelsCreate**
> Channel displayvideoPartnersChannelsCreate(partnerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserId, channel)



Creates a new channel. Returns the newly created channel if successful.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

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

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerId = "partnerId_example"; // String | The ID of the partner that owns the created channel.
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
    String advertiserId = "advertiserId_example"; // String | The ID of the advertiser that owns the created channel.
    Channel channel = new Channel(); // Channel | 
    try {
      Channel result = apiInstance.displayvideoPartnersChannelsCreate(partnerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserId, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#displayvideoPartnersChannelsCreate");
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
| **partnerId** | **String**| The ID of the partner that owns the created channel. | |
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
| **advertiserId** | **String**| The ID of the advertiser that owns the created channel. | [optional] |
| **channel** | [**Channel**](Channel.md)|  | [optional] |

### Return type

[**Channel**](Channel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="displayvideoPartnersChannelsList"></a>
# **displayvideoPartnersChannelsList**
> ListChannelsResponse displayvideoPartnersChannelsList(partnerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserId, filter, orderBy, pageSize, pageToken)



Lists channels for a partner or advertiser.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

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

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerId = "partnerId_example"; // String | The ID of the partner that owns the channels.
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
    String advertiserId = "advertiserId_example"; // String | The ID of the advertiser that owns the channels.
    String filter = "filter_example"; // String | Allows filtering by channel fields. Supported syntax: * Filter expressions for channel can only contain at most one restriction. * A restriction has the form of `{field} {operator} {value}`. * All fields must use the `HAS (:)` operator. Supported fields: * `displayName` Examples: * All channels for which the display name contains \"google\": `displayName : \"google\"`. The length of this field should be no more than 500 characters. Reference our [filter `LIST` requests](/display-video/api/guides/how-tos/filters) guide for more information.
    String orderBy = "orderBy_example"; // String | Field by which to sort the list. Acceptable values are: * `displayName` (default) * `channelId` The default sorting order is ascending. To specify descending order for a field, a suffix \" desc\" should be added to the field name. Example: `displayName desc`.
    Integer pageSize = 56; // Integer | Requested page size. Must be between `1` and `200`. If unspecified will default to `100`. Returns error code `INVALID_ARGUMENT` if an invalid value is specified.
    String pageToken = "pageToken_example"; // String | A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to `ListChannels` method. If not specified, the first page of results will be returned.
    try {
      ListChannelsResponse result = apiInstance.displayvideoPartnersChannelsList(partnerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserId, filter, orderBy, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#displayvideoPartnersChannelsList");
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
| **partnerId** | **String**| The ID of the partner that owns the channels. | |
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
| **advertiserId** | **String**| The ID of the advertiser that owns the channels. | [optional] |
| **filter** | **String**| Allows filtering by channel fields. Supported syntax: * Filter expressions for channel can only contain at most one restriction. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;HAS (:)&#x60; operator. Supported fields: * &#x60;displayName&#x60; Examples: * All channels for which the display name contains \&quot;google\&quot;: &#x60;displayName : \&quot;google\&quot;&#x60;. The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information. | [optional] |
| **orderBy** | **String**| Field by which to sort the list. Acceptable values are: * &#x60;displayName&#x60; (default) * &#x60;channelId&#x60; The default sorting order is ascending. To specify descending order for a field, a suffix \&quot; desc\&quot; should be added to the field name. Example: &#x60;displayName desc&#x60;. | [optional] |
| **pageSize** | **Integer**| Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified. | [optional] |
| **pageToken** | **String**| A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListChannels&#x60; method. If not specified, the first page of results will be returned. | [optional] |

### Return type

[**ListChannelsResponse**](ListChannelsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="displayvideoPartnersChannelsPatch"></a>
# **displayvideoPartnersChannelsPatch**
> Channel displayvideoPartnersChannelsPatch(partnerId, channelId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserId, updateMask, channel)



Updates a channel. Returns the updated channel if successful.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

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

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerId = "partnerId_example"; // String | The ID of the partner that owns the created channel.
    String channelId = "channelId_example"; // String | Output only. The unique ID of the channel. Assigned by the system.
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
    String advertiserId = "advertiserId_example"; // String | The ID of the advertiser that owns the created channel.
    String updateMask = "updateMask_example"; // String | Required. The mask to control which fields to update.
    Channel channel = new Channel(); // Channel | 
    try {
      Channel result = apiInstance.displayvideoPartnersChannelsPatch(partnerId, channelId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserId, updateMask, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#displayvideoPartnersChannelsPatch");
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
| **partnerId** | **String**| The ID of the partner that owns the created channel. | |
| **channelId** | **String**| Output only. The unique ID of the channel. Assigned by the system. | |
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
| **advertiserId** | **String**| The ID of the advertiser that owns the created channel. | [optional] |
| **updateMask** | **String**| Required. The mask to control which fields to update. | [optional] |
| **channel** | [**Channel**](Channel.md)|  | [optional] |

### Return type

[**Channel**](Channel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="displayvideoPartnersChannelsSitesBulkEdit"></a>
# **displayvideoPartnersChannelsSitesBulkEdit**
> BulkEditSitesResponse displayvideoPartnersChannelsSitesBulkEdit(partnerId, channelId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, bulkEditSitesRequest)



Bulk edits sites under a single channel. The operation will delete the sites provided in BulkEditSitesRequest.deleted_sites and then create the sites provided in BulkEditSitesRequest.created_sites.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

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

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerId = "partnerId_example"; // String | The ID of the partner that owns the parent channel.
    String channelId = "channelId_example"; // String | Required. The ID of the parent channel to which the sites belong.
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
    BulkEditSitesRequest bulkEditSitesRequest = new BulkEditSitesRequest(); // BulkEditSitesRequest | 
    try {
      BulkEditSitesResponse result = apiInstance.displayvideoPartnersChannelsSitesBulkEdit(partnerId, channelId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, bulkEditSitesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#displayvideoPartnersChannelsSitesBulkEdit");
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
| **partnerId** | **String**| The ID of the partner that owns the parent channel. | |
| **channelId** | **String**| Required. The ID of the parent channel to which the sites belong. | |
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
| **bulkEditSitesRequest** | [**BulkEditSitesRequest**](BulkEditSitesRequest.md)|  | [optional] |

### Return type

[**BulkEditSitesResponse**](BulkEditSitesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="displayvideoPartnersChannelsSitesDelete"></a>
# **displayvideoPartnersChannelsSitesDelete**
> Object displayvideoPartnersChannelsSitesDelete(partnerId, channelId, urlOrAppId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserId)



Deletes a site from a channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

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

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerId = "partnerId_example"; // String | The ID of the partner that owns the parent channel.
    String channelId = "channelId_example"; // String | Required. The ID of the parent channel to which the site belongs.
    String urlOrAppId = "urlOrAppId_example"; // String | Required. The URL or app ID of the site to delete.
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
    String advertiserId = "advertiserId_example"; // String | The ID of the advertiser that owns the parent channel.
    try {
      Object result = apiInstance.displayvideoPartnersChannelsSitesDelete(partnerId, channelId, urlOrAppId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#displayvideoPartnersChannelsSitesDelete");
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
| **partnerId** | **String**| The ID of the partner that owns the parent channel. | |
| **channelId** | **String**| Required. The ID of the parent channel to which the site belongs. | |
| **urlOrAppId** | **String**| Required. The URL or app ID of the site to delete. | |
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
| **advertiserId** | **String**| The ID of the advertiser that owns the parent channel. | [optional] |

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="displayvideoPartnersChannelsSitesList"></a>
# **displayvideoPartnersChannelsSitesList**
> ListSitesResponse displayvideoPartnersChannelsSitesList(partnerId, channelId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserId, filter, orderBy, pageSize, pageToken)



Lists sites in a channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

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

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerId = "partnerId_example"; // String | The ID of the partner that owns the parent channel.
    String channelId = "channelId_example"; // String | Required. The ID of the parent channel to which the requested sites belong.
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
    String advertiserId = "advertiserId_example"; // String | The ID of the advertiser that owns the parent channel.
    String filter = "filter_example"; // String | Allows filtering by site fields. Supported syntax: * Filter expressions for site retrieval can only contain at most one restriction. * A restriction has the form of `{field} {operator} {value}`. * All fields must use the `HAS (:)` operator. Supported fields: * `urlOrAppId` Examples: * All sites for which the URL or app ID contains \"google\": `urlOrAppId : \"google\"` The length of this field should be no more than 500 characters. Reference our [filter `LIST` requests](/display-video/api/guides/how-tos/filters) guide for more information.
    String orderBy = "orderBy_example"; // String | Field by which to sort the list. Acceptable values are: * `urlOrAppId` (default) The default sorting order is ascending. To specify descending order for a field, a suffix \" desc\" should be added to the field name. Example: `urlOrAppId desc`.
    Integer pageSize = 56; // Integer | Requested page size. Must be between `1` and `10000`. If unspecified will default to `100`. Returns error code `INVALID_ARGUMENT` if an invalid value is specified.
    String pageToken = "pageToken_example"; // String | A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to `ListSites` method. If not specified, the first page of results will be returned.
    try {
      ListSitesResponse result = apiInstance.displayvideoPartnersChannelsSitesList(partnerId, channelId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserId, filter, orderBy, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#displayvideoPartnersChannelsSitesList");
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
| **partnerId** | **String**| The ID of the partner that owns the parent channel. | |
| **channelId** | **String**| Required. The ID of the parent channel to which the requested sites belong. | |
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
| **advertiserId** | **String**| The ID of the advertiser that owns the parent channel. | [optional] |
| **filter** | **String**| Allows filtering by site fields. Supported syntax: * Filter expressions for site retrieval can only contain at most one restriction. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;HAS (:)&#x60; operator. Supported fields: * &#x60;urlOrAppId&#x60; Examples: * All sites for which the URL or app ID contains \&quot;google\&quot;: &#x60;urlOrAppId : \&quot;google\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information. | [optional] |
| **orderBy** | **String**| Field by which to sort the list. Acceptable values are: * &#x60;urlOrAppId&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot; desc\&quot; should be added to the field name. Example: &#x60;urlOrAppId desc&#x60;. | [optional] |
| **pageSize** | **Integer**| Requested page size. Must be between &#x60;1&#x60; and &#x60;10000&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified. | [optional] |
| **pageToken** | **String**| A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListSites&#x60; method. If not specified, the first page of results will be returned. | [optional] |

### Return type

[**ListSitesResponse**](ListSitesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="displayvideoPartnersChannelsSitesReplace"></a>
# **displayvideoPartnersChannelsSitesReplace**
> ReplaceSitesResponse displayvideoPartnersChannelsSitesReplace(partnerId, channelId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, replaceSitesRequest)



Replaces all of the sites under a single channel. The operation will replace the sites under a channel with the sites provided in ReplaceSitesRequest.new_sites. **This method regularly experiences high latency.** We recommend [increasing your default timeout](/display-video/api/guides/best-practices/timeouts#client_library_timeout) to avoid errors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

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

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerId = "partnerId_example"; // String | The ID of the partner that owns the parent channel.
    String channelId = "channelId_example"; // String | Required. The ID of the parent channel whose sites will be replaced.
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
    ReplaceSitesRequest replaceSitesRequest = new ReplaceSitesRequest(); // ReplaceSitesRequest | 
    try {
      ReplaceSitesResponse result = apiInstance.displayvideoPartnersChannelsSitesReplace(partnerId, channelId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, replaceSitesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#displayvideoPartnersChannelsSitesReplace");
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
| **partnerId** | **String**| The ID of the partner that owns the parent channel. | |
| **channelId** | **String**| Required. The ID of the parent channel whose sites will be replaced. | |
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
| **replaceSitesRequest** | [**ReplaceSitesRequest**](ReplaceSitesRequest.md)|  | [optional] |

### Return type

[**ReplaceSitesResponse**](ReplaceSitesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="displayvideoPartnersGet"></a>
# **displayvideoPartnersGet**
> Partner displayvideoPartnersGet(partnerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Gets a partner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

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

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerId = "partnerId_example"; // String | Required. The ID of the partner to fetch.
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
    try {
      Partner result = apiInstance.displayvideoPartnersGet(partnerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#displayvideoPartnersGet");
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
| **partnerId** | **String**| Required. The ID of the partner to fetch. | |
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

### Return type

[**Partner**](Partner.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="displayvideoPartnersList"></a>
# **displayvideoPartnersList**
> ListPartnersResponse displayvideoPartnersList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, orderBy, pageSize, pageToken)



Lists partners that are accessible to the current user. The order is defined by the order_by parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

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

    PartnersApi apiInstance = new PartnersApi(defaultClient);
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
    String filter = "filter_example"; // String | Allows filtering by partner fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`. * A restriction has the form of `{field} {operator} {value}`. * All fields must use the `EQUALS (=)` operator. Supported fields: * `entityStatus` Examples: * All active partners: `entityStatus=\"ENTITY_STATUS_ACTIVE\"` The length of this field should be no more than 500 characters. Reference our [filter `LIST` requests](/display-video/api/guides/how-tos/filters) guide for more information.
    String orderBy = "orderBy_example"; // String | Field by which to sort the list. Acceptable values are: * `displayName` The default sorting order is ascending. To specify descending order for a field, a suffix \"desc\" should be added to the field name. For example, `displayName desc`.
    Integer pageSize = 56; // Integer | Requested page size. Must be between `1` and `200`. If unspecified will default to `100`.
    String pageToken = "pageToken_example"; // String | A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to `ListPartners` method. If not specified, the first page of results will be returned.
    try {
      ListPartnersResponse result = apiInstance.displayvideoPartnersList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, orderBy, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#displayvideoPartnersList");
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
| **filter** | **String**| Allows filtering by partner fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;entityStatus&#x60; Examples: * All active partners: &#x60;entityStatus&#x3D;\&quot;ENTITY_STATUS_ACTIVE\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information. | [optional] |
| **orderBy** | **String**| Field by which to sort the list. Acceptable values are: * &#x60;displayName&#x60; The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. For example, &#x60;displayName desc&#x60;. | [optional] |
| **pageSize** | **Integer**| Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. | [optional] |
| **pageToken** | **String**| A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListPartners&#x60; method. If not specified, the first page of results will be returned. | [optional] |

### Return type

[**ListPartnersResponse**](ListPartnersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="displayvideoPartnersTargetingTypesAssignedTargetingOptionsCreate"></a>
# **displayvideoPartnersTargetingTypesAssignedTargetingOptionsCreate**
> AssignedTargetingOption displayvideoPartnersTargetingTypesAssignedTargetingOptionsCreate(partnerId, targetingType, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, assignedTargetingOption)



Assigns a targeting option to a partner. Returns the assigned targeting option if successful.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

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

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerId = "partnerId_example"; // String | Required. The ID of the partner.
    String targetingType = "TARGETING_TYPE_UNSPECIFIED"; // String | Required. Identifies the type of this assigned targeting option. Supported targeting types: * `TARGETING_TYPE_CHANNEL`
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
    AssignedTargetingOption assignedTargetingOption = new AssignedTargetingOption(); // AssignedTargetingOption | 
    try {
      AssignedTargetingOption result = apiInstance.displayvideoPartnersTargetingTypesAssignedTargetingOptionsCreate(partnerId, targetingType, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, assignedTargetingOption);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#displayvideoPartnersTargetingTypesAssignedTargetingOptionsCreate");
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
| **partnerId** | **String**| Required. The ID of the partner. | |
| **targetingType** | **String**| Required. Identifies the type of this assigned targeting option. Supported targeting types: * &#x60;TARGETING_TYPE_CHANNEL&#x60; | [enum: TARGETING_TYPE_UNSPECIFIED, TARGETING_TYPE_CHANNEL, TARGETING_TYPE_APP_CATEGORY, TARGETING_TYPE_APP, TARGETING_TYPE_URL, TARGETING_TYPE_DAY_AND_TIME, TARGETING_TYPE_AGE_RANGE, TARGETING_TYPE_REGIONAL_LOCATION_LIST, TARGETING_TYPE_PROXIMITY_LOCATION_LIST, TARGETING_TYPE_GENDER, TARGETING_TYPE_VIDEO_PLAYER_SIZE, TARGETING_TYPE_USER_REWARDED_CONTENT, TARGETING_TYPE_PARENTAL_STATUS, TARGETING_TYPE_CONTENT_INSTREAM_POSITION, TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION, TARGETING_TYPE_DEVICE_TYPE, TARGETING_TYPE_AUDIENCE_GROUP, TARGETING_TYPE_BROWSER, TARGETING_TYPE_HOUSEHOLD_INCOME, TARGETING_TYPE_ON_SCREEN_POSITION, TARGETING_TYPE_THIRD_PARTY_VERIFIER, TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION, TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION, TARGETING_TYPE_ENVIRONMENT, TARGETING_TYPE_CARRIER_AND_ISP, TARGETING_TYPE_OPERATING_SYSTEM, TARGETING_TYPE_DEVICE_MAKE_MODEL, TARGETING_TYPE_KEYWORD, TARGETING_TYPE_NEGATIVE_KEYWORD_LIST, TARGETING_TYPE_VIEWABILITY, TARGETING_TYPE_CATEGORY, TARGETING_TYPE_INVENTORY_SOURCE, TARGETING_TYPE_LANGUAGE, TARGETING_TYPE_AUTHORIZED_SELLER_STATUS, TARGETING_TYPE_GEO_REGION, TARGETING_TYPE_INVENTORY_SOURCE_GROUP, TARGETING_TYPE_EXCHANGE, TARGETING_TYPE_SUB_EXCHANGE, TARGETING_TYPE_POI, TARGETING_TYPE_BUSINESS_CHAIN, TARGETING_TYPE_CONTENT_DURATION, TARGETING_TYPE_CONTENT_STREAM_TYPE, TARGETING_TYPE_NATIVE_CONTENT_POSITION, TARGETING_TYPE_OMID, TARGETING_TYPE_AUDIO_CONTENT_TYPE, TARGETING_TYPE_CONTENT_GENRE] |
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
| **assignedTargetingOption** | [**AssignedTargetingOption**](AssignedTargetingOption.md)|  | [optional] |

### Return type

[**AssignedTargetingOption**](AssignedTargetingOption.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="displayvideoPartnersTargetingTypesAssignedTargetingOptionsDelete"></a>
# **displayvideoPartnersTargetingTypesAssignedTargetingOptionsDelete**
> Object displayvideoPartnersTargetingTypesAssignedTargetingOptionsDelete(partnerId, targetingType, assignedTargetingOptionId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Deletes an assigned targeting option from a partner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

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

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerId = "partnerId_example"; // String | Required. The ID of the partner.
    String targetingType = "TARGETING_TYPE_UNSPECIFIED"; // String | Required. Identifies the type of this assigned targeting option. Supported targeting types: * `TARGETING_TYPE_CHANNEL`
    String assignedTargetingOptionId = "assignedTargetingOptionId_example"; // String | Required. The ID of the assigned targeting option to delete.
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
    try {
      Object result = apiInstance.displayvideoPartnersTargetingTypesAssignedTargetingOptionsDelete(partnerId, targetingType, assignedTargetingOptionId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#displayvideoPartnersTargetingTypesAssignedTargetingOptionsDelete");
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
| **partnerId** | **String**| Required. The ID of the partner. | |
| **targetingType** | **String**| Required. Identifies the type of this assigned targeting option. Supported targeting types: * &#x60;TARGETING_TYPE_CHANNEL&#x60; | [enum: TARGETING_TYPE_UNSPECIFIED, TARGETING_TYPE_CHANNEL, TARGETING_TYPE_APP_CATEGORY, TARGETING_TYPE_APP, TARGETING_TYPE_URL, TARGETING_TYPE_DAY_AND_TIME, TARGETING_TYPE_AGE_RANGE, TARGETING_TYPE_REGIONAL_LOCATION_LIST, TARGETING_TYPE_PROXIMITY_LOCATION_LIST, TARGETING_TYPE_GENDER, TARGETING_TYPE_VIDEO_PLAYER_SIZE, TARGETING_TYPE_USER_REWARDED_CONTENT, TARGETING_TYPE_PARENTAL_STATUS, TARGETING_TYPE_CONTENT_INSTREAM_POSITION, TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION, TARGETING_TYPE_DEVICE_TYPE, TARGETING_TYPE_AUDIENCE_GROUP, TARGETING_TYPE_BROWSER, TARGETING_TYPE_HOUSEHOLD_INCOME, TARGETING_TYPE_ON_SCREEN_POSITION, TARGETING_TYPE_THIRD_PARTY_VERIFIER, TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION, TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION, TARGETING_TYPE_ENVIRONMENT, TARGETING_TYPE_CARRIER_AND_ISP, TARGETING_TYPE_OPERATING_SYSTEM, TARGETING_TYPE_DEVICE_MAKE_MODEL, TARGETING_TYPE_KEYWORD, TARGETING_TYPE_NEGATIVE_KEYWORD_LIST, TARGETING_TYPE_VIEWABILITY, TARGETING_TYPE_CATEGORY, TARGETING_TYPE_INVENTORY_SOURCE, TARGETING_TYPE_LANGUAGE, TARGETING_TYPE_AUTHORIZED_SELLER_STATUS, TARGETING_TYPE_GEO_REGION, TARGETING_TYPE_INVENTORY_SOURCE_GROUP, TARGETING_TYPE_EXCHANGE, TARGETING_TYPE_SUB_EXCHANGE, TARGETING_TYPE_POI, TARGETING_TYPE_BUSINESS_CHAIN, TARGETING_TYPE_CONTENT_DURATION, TARGETING_TYPE_CONTENT_STREAM_TYPE, TARGETING_TYPE_NATIVE_CONTENT_POSITION, TARGETING_TYPE_OMID, TARGETING_TYPE_AUDIO_CONTENT_TYPE, TARGETING_TYPE_CONTENT_GENRE] |
| **assignedTargetingOptionId** | **String**| Required. The ID of the assigned targeting option to delete. | |
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

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="displayvideoPartnersTargetingTypesAssignedTargetingOptionsGet"></a>
# **displayvideoPartnersTargetingTypesAssignedTargetingOptionsGet**
> AssignedTargetingOption displayvideoPartnersTargetingTypesAssignedTargetingOptionsGet(partnerId, targetingType, assignedTargetingOptionId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Gets a single targeting option assigned to a partner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

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

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerId = "partnerId_example"; // String | Required. The ID of the partner.
    String targetingType = "TARGETING_TYPE_UNSPECIFIED"; // String | Required. Identifies the type of this assigned targeting option. Supported targeting types: * `TARGETING_TYPE_CHANNEL`
    String assignedTargetingOptionId = "assignedTargetingOptionId_example"; // String | Required. An identifier unique to the targeting type in this partner that identifies the assigned targeting option being requested.
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
    try {
      AssignedTargetingOption result = apiInstance.displayvideoPartnersTargetingTypesAssignedTargetingOptionsGet(partnerId, targetingType, assignedTargetingOptionId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#displayvideoPartnersTargetingTypesAssignedTargetingOptionsGet");
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
| **partnerId** | **String**| Required. The ID of the partner. | |
| **targetingType** | **String**| Required. Identifies the type of this assigned targeting option. Supported targeting types: * &#x60;TARGETING_TYPE_CHANNEL&#x60; | [enum: TARGETING_TYPE_UNSPECIFIED, TARGETING_TYPE_CHANNEL, TARGETING_TYPE_APP_CATEGORY, TARGETING_TYPE_APP, TARGETING_TYPE_URL, TARGETING_TYPE_DAY_AND_TIME, TARGETING_TYPE_AGE_RANGE, TARGETING_TYPE_REGIONAL_LOCATION_LIST, TARGETING_TYPE_PROXIMITY_LOCATION_LIST, TARGETING_TYPE_GENDER, TARGETING_TYPE_VIDEO_PLAYER_SIZE, TARGETING_TYPE_USER_REWARDED_CONTENT, TARGETING_TYPE_PARENTAL_STATUS, TARGETING_TYPE_CONTENT_INSTREAM_POSITION, TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION, TARGETING_TYPE_DEVICE_TYPE, TARGETING_TYPE_AUDIENCE_GROUP, TARGETING_TYPE_BROWSER, TARGETING_TYPE_HOUSEHOLD_INCOME, TARGETING_TYPE_ON_SCREEN_POSITION, TARGETING_TYPE_THIRD_PARTY_VERIFIER, TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION, TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION, TARGETING_TYPE_ENVIRONMENT, TARGETING_TYPE_CARRIER_AND_ISP, TARGETING_TYPE_OPERATING_SYSTEM, TARGETING_TYPE_DEVICE_MAKE_MODEL, TARGETING_TYPE_KEYWORD, TARGETING_TYPE_NEGATIVE_KEYWORD_LIST, TARGETING_TYPE_VIEWABILITY, TARGETING_TYPE_CATEGORY, TARGETING_TYPE_INVENTORY_SOURCE, TARGETING_TYPE_LANGUAGE, TARGETING_TYPE_AUTHORIZED_SELLER_STATUS, TARGETING_TYPE_GEO_REGION, TARGETING_TYPE_INVENTORY_SOURCE_GROUP, TARGETING_TYPE_EXCHANGE, TARGETING_TYPE_SUB_EXCHANGE, TARGETING_TYPE_POI, TARGETING_TYPE_BUSINESS_CHAIN, TARGETING_TYPE_CONTENT_DURATION, TARGETING_TYPE_CONTENT_STREAM_TYPE, TARGETING_TYPE_NATIVE_CONTENT_POSITION, TARGETING_TYPE_OMID, TARGETING_TYPE_AUDIO_CONTENT_TYPE, TARGETING_TYPE_CONTENT_GENRE] |
| **assignedTargetingOptionId** | **String**| Required. An identifier unique to the targeting type in this partner that identifies the assigned targeting option being requested. | |
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

### Return type

[**AssignedTargetingOption**](AssignedTargetingOption.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="displayvideoPartnersTargetingTypesAssignedTargetingOptionsList"></a>
# **displayvideoPartnersTargetingTypesAssignedTargetingOptionsList**
> ListPartnerAssignedTargetingOptionsResponse displayvideoPartnersTargetingTypesAssignedTargetingOptionsList(partnerId, targetingType, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, orderBy, pageSize, pageToken)



Lists the targeting options assigned to a partner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

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

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerId = "partnerId_example"; // String | Required. The ID of the partner.
    String targetingType = "TARGETING_TYPE_UNSPECIFIED"; // String | Required. Identifies the type of assigned targeting options to list. Supported targeting types: * `TARGETING_TYPE_CHANNEL`
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
    String filter = "filter_example"; // String | Allows filtering by assigned targeting option fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by the logical operator `OR`. * A restriction has the form of `{field} {operator} {value}`. * All fields must use the `EQUALS (=)` operator. Supported fields: * `assignedTargetingOptionId` Examples: * `AssignedTargetingOption` resource with ID 123456: `assignedTargetingOptionId=\"123456\"` The length of this field should be no more than 500 characters. Reference our [filter `LIST` requests](/display-video/api/guides/how-tos/filters) guide for more information.
    String orderBy = "orderBy_example"; // String | Field by which to sort the list. Acceptable values are: * `assignedTargetingOptionId` (default) The default sorting order is ascending. To specify descending order for a field, a suffix \"desc\" should be added to the field name. Example: `assignedTargetingOptionId desc`.
    Integer pageSize = 56; // Integer | Requested page size. Must be between `1` and `200`. If unspecified will default to `100`. Returns error code `INVALID_ARGUMENT` if an invalid value is specified.
    String pageToken = "pageToken_example"; // String | A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to `ListPartnerAssignedTargetingOptions` method. If not specified, the first page of results will be returned.
    try {
      ListPartnerAssignedTargetingOptionsResponse result = apiInstance.displayvideoPartnersTargetingTypesAssignedTargetingOptionsList(partnerId, targetingType, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, orderBy, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#displayvideoPartnersTargetingTypesAssignedTargetingOptionsList");
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
| **partnerId** | **String**| Required. The ID of the partner. | |
| **targetingType** | **String**| Required. Identifies the type of assigned targeting options to list. Supported targeting types: * &#x60;TARGETING_TYPE_CHANNEL&#x60; | [enum: TARGETING_TYPE_UNSPECIFIED, TARGETING_TYPE_CHANNEL, TARGETING_TYPE_APP_CATEGORY, TARGETING_TYPE_APP, TARGETING_TYPE_URL, TARGETING_TYPE_DAY_AND_TIME, TARGETING_TYPE_AGE_RANGE, TARGETING_TYPE_REGIONAL_LOCATION_LIST, TARGETING_TYPE_PROXIMITY_LOCATION_LIST, TARGETING_TYPE_GENDER, TARGETING_TYPE_VIDEO_PLAYER_SIZE, TARGETING_TYPE_USER_REWARDED_CONTENT, TARGETING_TYPE_PARENTAL_STATUS, TARGETING_TYPE_CONTENT_INSTREAM_POSITION, TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION, TARGETING_TYPE_DEVICE_TYPE, TARGETING_TYPE_AUDIENCE_GROUP, TARGETING_TYPE_BROWSER, TARGETING_TYPE_HOUSEHOLD_INCOME, TARGETING_TYPE_ON_SCREEN_POSITION, TARGETING_TYPE_THIRD_PARTY_VERIFIER, TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION, TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION, TARGETING_TYPE_ENVIRONMENT, TARGETING_TYPE_CARRIER_AND_ISP, TARGETING_TYPE_OPERATING_SYSTEM, TARGETING_TYPE_DEVICE_MAKE_MODEL, TARGETING_TYPE_KEYWORD, TARGETING_TYPE_NEGATIVE_KEYWORD_LIST, TARGETING_TYPE_VIEWABILITY, TARGETING_TYPE_CATEGORY, TARGETING_TYPE_INVENTORY_SOURCE, TARGETING_TYPE_LANGUAGE, TARGETING_TYPE_AUTHORIZED_SELLER_STATUS, TARGETING_TYPE_GEO_REGION, TARGETING_TYPE_INVENTORY_SOURCE_GROUP, TARGETING_TYPE_EXCHANGE, TARGETING_TYPE_SUB_EXCHANGE, TARGETING_TYPE_POI, TARGETING_TYPE_BUSINESS_CHAIN, TARGETING_TYPE_CONTENT_DURATION, TARGETING_TYPE_CONTENT_STREAM_TYPE, TARGETING_TYPE_NATIVE_CONTENT_POSITION, TARGETING_TYPE_OMID, TARGETING_TYPE_AUDIO_CONTENT_TYPE, TARGETING_TYPE_CONTENT_GENRE] |
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
| **filter** | **String**| Allows filtering by assigned targeting option fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by the logical operator &#x60;OR&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;assignedTargetingOptionId&#x60; Examples: * &#x60;AssignedTargetingOption&#x60; resource with ID 123456: &#x60;assignedTargetingOptionId&#x3D;\&quot;123456\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information. | [optional] |
| **orderBy** | **String**| Field by which to sort the list. Acceptable values are: * &#x60;assignedTargetingOptionId&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;assignedTargetingOptionId desc&#x60;. | [optional] |
| **pageSize** | **Integer**| Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified. | [optional] |
| **pageToken** | **String**| A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListPartnerAssignedTargetingOptions&#x60; method. If not specified, the first page of results will be returned. | [optional] |

### Return type

[**ListPartnerAssignedTargetingOptionsResponse**](ListPartnerAssignedTargetingOptionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

