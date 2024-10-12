# ChangeLogsApi

All URIs are relative to *https://dfareporting.googleapis.com/dfareporting/v3.3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dfareportingChangeLogsGet**](ChangeLogsApi.md#dfareportingChangeLogsGet) | **GET** /userprofiles/{profileId}/changeLogs/{id} |  |
| [**dfareportingChangeLogsList**](ChangeLogsApi.md#dfareportingChangeLogsList) | **GET** /userprofiles/{profileId}/changeLogs |  |


<a id="dfareportingChangeLogsGet"></a>
# **dfareportingChangeLogsGet**
> ChangeLog dfareportingChangeLogsGet(profileId, id, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Gets one change log by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangeLogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dfareporting.googleapis.com/dfareporting/v3.3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ChangeLogsApi apiInstance = new ChangeLogsApi(defaultClient);
    String profileId = "profileId_example"; // String | User profile ID associated with this request.
    String id = "id_example"; // String | Change log ID.
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
      ChangeLog result = apiInstance.dfareportingChangeLogsGet(profileId, id, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangeLogsApi#dfareportingChangeLogsGet");
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
| **profileId** | **String**| User profile ID associated with this request. | |
| **id** | **String**| Change log ID. | |
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

[**ChangeLog**](ChangeLog.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dfareportingChangeLogsList"></a>
# **dfareportingChangeLogsList**
> ChangeLogsListResponse dfareportingChangeLogsList(profileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, action, ids, maxChangeTime, maxResults, minChangeTime, objectIds, objectType, pageToken, searchString, userProfileIds)



Retrieves a list of change logs. This method supports paging.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangeLogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dfareporting.googleapis.com/dfareporting/v3.3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ChangeLogsApi apiInstance = new ChangeLogsApi(defaultClient);
    String profileId = "profileId_example"; // String | User profile ID associated with this request.
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
    String action = "ACTION_CREATE"; // String | Select only change logs with the specified action.
    List<String> ids = Arrays.asList(); // List<String> | Select only change logs with these IDs.
    String maxChangeTime = "maxChangeTime_example"; // String | Select only change logs whose change time is before the specified maxChangeTime.The time should be formatted as an RFC3339 date/time string. For example, for 10:54 PM on July 18th, 2015, in the America/New York time zone, the format is \"2015-07-18T22:54:00-04:00\". In other words, the year, month, day, the letter T, the hour (24-hour clock system), minute, second, and then the time zone offset.
    Integer maxResults = 56; // Integer | Maximum number of results to return.
    String minChangeTime = "minChangeTime_example"; // String | Select only change logs whose change time is after the specified minChangeTime.The time should be formatted as an RFC3339 date/time string. For example, for 10:54 PM on July 18th, 2015, in the America/New York time zone, the format is \"2015-07-18T22:54:00-04:00\". In other words, the year, month, day, the letter T, the hour (24-hour clock system), minute, second, and then the time zone offset.
    List<String> objectIds = Arrays.asList(); // List<String> | Select only change logs with these object IDs.
    String objectType = "OBJECT_ADVERTISER"; // String | Select only change logs with the specified object type.
    String pageToken = "pageToken_example"; // String | Value of the nextPageToken from the previous result page.
    String searchString = "searchString_example"; // String | Select only change logs whose object ID, user name, old or new values match the search string.
    List<String> userProfileIds = Arrays.asList(); // List<String> | Select only change logs with these user profile IDs.
    try {
      ChangeLogsListResponse result = apiInstance.dfareportingChangeLogsList(profileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, action, ids, maxChangeTime, maxResults, minChangeTime, objectIds, objectType, pageToken, searchString, userProfileIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangeLogsApi#dfareportingChangeLogsList");
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
| **profileId** | **String**| User profile ID associated with this request. | |
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
| **action** | **String**| Select only change logs with the specified action. | [optional] [enum: ACTION_CREATE, ACTION_UPDATE, ACTION_DELETE, ACTION_ENABLE, ACTION_DISABLE, ACTION_ADD, ACTION_REMOVE, ACTION_MARK_AS_DEFAULT, ACTION_ASSOCIATE, ACTION_ASSIGN, ACTION_UNASSIGN, ACTION_SEND, ACTION_LINK, ACTION_UNLINK, ACTION_PUSH, ACTION_EMAIL_TAGS, ACTION_SHARE] |
| **ids** | [**List&lt;String&gt;**](String.md)| Select only change logs with these IDs. | [optional] |
| **maxChangeTime** | **String**| Select only change logs whose change time is before the specified maxChangeTime.The time should be formatted as an RFC3339 date/time string. For example, for 10:54 PM on July 18th, 2015, in the America/New York time zone, the format is \&quot;2015-07-18T22:54:00-04:00\&quot;. In other words, the year, month, day, the letter T, the hour (24-hour clock system), minute, second, and then the time zone offset. | [optional] |
| **maxResults** | **Integer**| Maximum number of results to return. | [optional] |
| **minChangeTime** | **String**| Select only change logs whose change time is after the specified minChangeTime.The time should be formatted as an RFC3339 date/time string. For example, for 10:54 PM on July 18th, 2015, in the America/New York time zone, the format is \&quot;2015-07-18T22:54:00-04:00\&quot;. In other words, the year, month, day, the letter T, the hour (24-hour clock system), minute, second, and then the time zone offset. | [optional] |
| **objectIds** | [**List&lt;String&gt;**](String.md)| Select only change logs with these object IDs. | [optional] |
| **objectType** | **String**| Select only change logs with the specified object type. | [optional] [enum: OBJECT_ADVERTISER, OBJECT_FLOODLIGHT_CONFIGURATION, OBJECT_AD, OBJECT_FLOODLIGHT_ACTVITY, OBJECT_CAMPAIGN, OBJECT_FLOODLIGHT_ACTIVITY_GROUP, OBJECT_CREATIVE, OBJECT_PLACEMENT, OBJECT_DFA_SITE, OBJECT_USER_ROLE, OBJECT_USER_PROFILE, OBJECT_ADVERTISER_GROUP, OBJECT_ACCOUNT, OBJECT_SUBACCOUNT, OBJECT_RICHMEDIA_CREATIVE, OBJECT_INSTREAM_CREATIVE, OBJECT_MEDIA_ORDER, OBJECT_CONTENT_CATEGORY, OBJECT_PLACEMENT_STRATEGY, OBJECT_SD_SITE, OBJECT_SIZE, OBJECT_CREATIVE_GROUP, OBJECT_CREATIVE_ASSET, OBJECT_USER_PROFILE_FILTER, OBJECT_LANDING_PAGE, OBJECT_CREATIVE_FIELD, OBJECT_REMARKETING_LIST, OBJECT_PROVIDED_LIST_CLIENT, OBJECT_EVENT_TAG, OBJECT_CREATIVE_BUNDLE, OBJECT_BILLING_ACCOUNT_GROUP, OBJECT_BILLING_FEATURE, OBJECT_RATE_CARD, OBJECT_ACCOUNT_BILLING_FEATURE, OBJECT_BILLING_MINIMUM_FEE, OBJECT_BILLING_PROFILE, OBJECT_PLAYSTORE_LINK, OBJECT_TARGETING_TEMPLATE, OBJECT_SEARCH_LIFT_STUDY, OBJECT_FLOODLIGHT_DV360_LINK] |
| **pageToken** | **String**| Value of the nextPageToken from the previous result page. | [optional] |
| **searchString** | **String**| Select only change logs whose object ID, user name, old or new values match the search string. | [optional] |
| **userProfileIds** | [**List&lt;String&gt;**](String.md)| Select only change logs with these user profile IDs. | [optional] |

### Return type

[**ChangeLogsListResponse**](ChangeLogsListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

