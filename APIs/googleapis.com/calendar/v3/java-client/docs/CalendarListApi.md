# CalendarListApi

All URIs are relative to *https://www.googleapis.com/calendar/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**calendarCalendarListDelete**](CalendarListApi.md#calendarCalendarListDelete) | **DELETE** /users/me/calendarList/{calendarId} |  |
| [**calendarCalendarListGet**](CalendarListApi.md#calendarCalendarListGet) | **GET** /users/me/calendarList/{calendarId} |  |
| [**calendarCalendarListInsert**](CalendarListApi.md#calendarCalendarListInsert) | **POST** /users/me/calendarList |  |
| [**calendarCalendarListList**](CalendarListApi.md#calendarCalendarListList) | **GET** /users/me/calendarList |  |
| [**calendarCalendarListPatch**](CalendarListApi.md#calendarCalendarListPatch) | **PATCH** /users/me/calendarList/{calendarId} |  |
| [**calendarCalendarListUpdate**](CalendarListApi.md#calendarCalendarListUpdate) | **PUT** /users/me/calendarList/{calendarId} |  |
| [**calendarCalendarListWatch**](CalendarListApi.md#calendarCalendarListWatch) | **POST** /users/me/calendarList/watch |  |


<a id="calendarCalendarListDelete"></a>
# **calendarCalendarListDelete**
> calendarCalendarListDelete(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Removes a calendar from the user&#39;s calendar list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarListApi apiInstance = new CalendarListApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      apiInstance.calendarCalendarListDelete(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarListApi#calendarCalendarListDelete");
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
| **calendarId** | **String**| Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarCalendarListGet"></a>
# **calendarCalendarListGet**
> CalendarListEntry calendarCalendarListGet(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Returns a calendar from the user&#39;s calendar list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarListApi apiInstance = new CalendarListApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      CalendarListEntry result = apiInstance.calendarCalendarListGet(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarListApi#calendarCalendarListGet");
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
| **calendarId** | **String**| Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**CalendarListEntry**](CalendarListEntry.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarCalendarListInsert"></a>
# **calendarCalendarListInsert**
> CalendarListEntry calendarCalendarListInsert(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, colorRgbFormat, calendarListEntry)



Inserts an existing calendar into the user&#39;s calendar list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarListApi apiInstance = new CalendarListApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean colorRgbFormat = true; // Boolean | Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False.
    CalendarListEntry calendarListEntry = new CalendarListEntry(); // CalendarListEntry | 
    try {
      CalendarListEntry result = apiInstance.calendarCalendarListInsert(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, colorRgbFormat, calendarListEntry);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarListApi#calendarCalendarListInsert");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **colorRgbFormat** | **Boolean**| Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False. | [optional] |
| **calendarListEntry** | [**CalendarListEntry**](CalendarListEntry.md)|  | [optional] |

### Return type

[**CalendarListEntry**](CalendarListEntry.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarCalendarListList"></a>
# **calendarCalendarListList**
> CalendarList calendarCalendarListList(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, minAccessRole, pageToken, showDeleted, showHidden, syncToken)



Returns the calendars on the user&#39;s calendar list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarListApi apiInstance = new CalendarListApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional.
    String minAccessRole = "freeBusyReader"; // String | The minimum access role for the user in the returned entries. Optional. The default is no restriction.
    String pageToken = "pageToken_example"; // String | Token specifying which result page to return. Optional.
    Boolean showDeleted = true; // Boolean | Whether to include deleted calendar list entries in the result. Optional. The default is False.
    Boolean showHidden = true; // Boolean | Whether to show hidden entries. Optional. The default is False.
    String syncToken = "syncToken_example"; // String | Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. If only read-only fields such as calendar properties or ACLs have changed, the entry won't be returned. All entries deleted and hidden since the previous list request will always be in the result set and it is not allowed to set showDeleted neither showHidden to False. To ensure client state consistency minAccessRole query parameter cannot be specified together with nextSyncToken. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries.
    try {
      CalendarList result = apiInstance.calendarCalendarListList(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, minAccessRole, pageToken, showDeleted, showHidden, syncToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarListApi#calendarCalendarListList");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **maxResults** | **Integer**| Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional. | [optional] |
| **minAccessRole** | **String**| The minimum access role for the user in the returned entries. Optional. The default is no restriction. | [optional] [enum: freeBusyReader, owner, reader, writer] |
| **pageToken** | **String**| Token specifying which result page to return. Optional. | [optional] |
| **showDeleted** | **Boolean**| Whether to include deleted calendar list entries in the result. Optional. The default is False. | [optional] |
| **showHidden** | **Boolean**| Whether to show hidden entries. Optional. The default is False. | [optional] |
| **syncToken** | **String**| Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. If only read-only fields such as calendar properties or ACLs have changed, the entry won&#39;t be returned. All entries deleted and hidden since the previous list request will always be in the result set and it is not allowed to set showDeleted neither showHidden to False. To ensure client state consistency minAccessRole query parameter cannot be specified together with nextSyncToken. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries. | [optional] |

### Return type

[**CalendarList**](CalendarList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarCalendarListPatch"></a>
# **calendarCalendarListPatch**
> CalendarListEntry calendarCalendarListPatch(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, colorRgbFormat, calendarListEntry)



Updates an existing calendar on the user&#39;s calendar list. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarListApi apiInstance = new CalendarListApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean colorRgbFormat = true; // Boolean | Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False.
    CalendarListEntry calendarListEntry = new CalendarListEntry(); // CalendarListEntry | 
    try {
      CalendarListEntry result = apiInstance.calendarCalendarListPatch(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, colorRgbFormat, calendarListEntry);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarListApi#calendarCalendarListPatch");
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
| **calendarId** | **String**| Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **colorRgbFormat** | **Boolean**| Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False. | [optional] |
| **calendarListEntry** | [**CalendarListEntry**](CalendarListEntry.md)|  | [optional] |

### Return type

[**CalendarListEntry**](CalendarListEntry.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarCalendarListUpdate"></a>
# **calendarCalendarListUpdate**
> CalendarListEntry calendarCalendarListUpdate(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, colorRgbFormat, calendarListEntry)



Updates an existing calendar on the user&#39;s calendar list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarListApi apiInstance = new CalendarListApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean colorRgbFormat = true; // Boolean | Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False.
    CalendarListEntry calendarListEntry = new CalendarListEntry(); // CalendarListEntry | 
    try {
      CalendarListEntry result = apiInstance.calendarCalendarListUpdate(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, colorRgbFormat, calendarListEntry);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarListApi#calendarCalendarListUpdate");
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
| **calendarId** | **String**| Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **colorRgbFormat** | **Boolean**| Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False. | [optional] |
| **calendarListEntry** | [**CalendarListEntry**](CalendarListEntry.md)|  | [optional] |

### Return type

[**CalendarListEntry**](CalendarListEntry.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarCalendarListWatch"></a>
# **calendarCalendarListWatch**
> Channel calendarCalendarListWatch(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, minAccessRole, pageToken, showDeleted, showHidden, syncToken, channel)



Watch for changes to CalendarList resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarListApi apiInstance = new CalendarListApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional.
    String minAccessRole = "freeBusyReader"; // String | The minimum access role for the user in the returned entries. Optional. The default is no restriction.
    String pageToken = "pageToken_example"; // String | Token specifying which result page to return. Optional.
    Boolean showDeleted = true; // Boolean | Whether to include deleted calendar list entries in the result. Optional. The default is False.
    Boolean showHidden = true; // Boolean | Whether to show hidden entries. Optional. The default is False.
    String syncToken = "syncToken_example"; // String | Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. If only read-only fields such as calendar properties or ACLs have changed, the entry won't be returned. All entries deleted and hidden since the previous list request will always be in the result set and it is not allowed to set showDeleted neither showHidden to False. To ensure client state consistency minAccessRole query parameter cannot be specified together with nextSyncToken. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries.
    Channel channel = new Channel(); // Channel | 
    try {
      Channel result = apiInstance.calendarCalendarListWatch(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, minAccessRole, pageToken, showDeleted, showHidden, syncToken, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarListApi#calendarCalendarListWatch");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **maxResults** | **Integer**| Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional. | [optional] |
| **minAccessRole** | **String**| The minimum access role for the user in the returned entries. Optional. The default is no restriction. | [optional] [enum: freeBusyReader, owner, reader, writer] |
| **pageToken** | **String**| Token specifying which result page to return. Optional. | [optional] |
| **showDeleted** | **Boolean**| Whether to include deleted calendar list entries in the result. Optional. The default is False. | [optional] |
| **showHidden** | **Boolean**| Whether to show hidden entries. Optional. The default is False. | [optional] |
| **syncToken** | **String**| Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. If only read-only fields such as calendar properties or ACLs have changed, the entry won&#39;t be returned. All entries deleted and hidden since the previous list request will always be in the result set and it is not allowed to set showDeleted neither showHidden to False. To ensure client state consistency minAccessRole query parameter cannot be specified together with nextSyncToken. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries. | [optional] |
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

