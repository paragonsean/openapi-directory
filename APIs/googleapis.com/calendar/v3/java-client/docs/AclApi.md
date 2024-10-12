# AclApi

All URIs are relative to *https://www.googleapis.com/calendar/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**calendarAclDelete**](AclApi.md#calendarAclDelete) | **DELETE** /calendars/{calendarId}/acl/{ruleId} |  |
| [**calendarAclGet**](AclApi.md#calendarAclGet) | **GET** /calendars/{calendarId}/acl/{ruleId} |  |
| [**calendarAclInsert**](AclApi.md#calendarAclInsert) | **POST** /calendars/{calendarId}/acl |  |
| [**calendarAclList**](AclApi.md#calendarAclList) | **GET** /calendars/{calendarId}/acl |  |
| [**calendarAclPatch**](AclApi.md#calendarAclPatch) | **PATCH** /calendars/{calendarId}/acl/{ruleId} |  |
| [**calendarAclUpdate**](AclApi.md#calendarAclUpdate) | **PUT** /calendars/{calendarId}/acl/{ruleId} |  |
| [**calendarAclWatch**](AclApi.md#calendarAclWatch) | **POST** /calendars/{calendarId}/acl/watch |  |


<a id="calendarAclDelete"></a>
# **calendarAclDelete**
> calendarAclDelete(calendarId, ruleId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Deletes an access control rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AclApi;

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

    AclApi apiInstance = new AclApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String ruleId = "ruleId_example"; // String | ACL rule identifier.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      apiInstance.calendarAclDelete(calendarId, ruleId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
    } catch (ApiException e) {
      System.err.println("Exception when calling AclApi#calendarAclDelete");
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
| **ruleId** | **String**| ACL rule identifier. | |
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

<a id="calendarAclGet"></a>
# **calendarAclGet**
> AclRule calendarAclGet(calendarId, ruleId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Returns an access control rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AclApi;

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

    AclApi apiInstance = new AclApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String ruleId = "ruleId_example"; // String | ACL rule identifier.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      AclRule result = apiInstance.calendarAclGet(calendarId, ruleId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AclApi#calendarAclGet");
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
| **ruleId** | **String**| ACL rule identifier. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**AclRule**](AclRule.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarAclInsert"></a>
# **calendarAclInsert**
> AclRule calendarAclInsert(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, sendNotifications, aclRule)



Creates an access control rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AclApi;

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

    AclApi apiInstance = new AclApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean sendNotifications = true; // Boolean | Whether to send notifications about the calendar sharing change. Optional. The default is True.
    AclRule aclRule = new AclRule(); // AclRule | 
    try {
      AclRule result = apiInstance.calendarAclInsert(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, sendNotifications, aclRule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AclApi#calendarAclInsert");
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
| **sendNotifications** | **Boolean**| Whether to send notifications about the calendar sharing change. Optional. The default is True. | [optional] |
| **aclRule** | [**AclRule**](AclRule.md)|  | [optional] |

### Return type

[**AclRule**](AclRule.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarAclList"></a>
# **calendarAclList**
> Acl calendarAclList(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken, showDeleted, syncToken)



Returns the rules in the access control list for the calendar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AclApi;

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

    AclApi apiInstance = new AclApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional.
    String pageToken = "pageToken_example"; // String | Token specifying which result page to return. Optional.
    Boolean showDeleted = true; // Boolean | Whether to include deleted ACLs in the result. Deleted ACLs are represented by role equal to \"none\". Deleted ACLs will always be included if syncToken is provided. Optional. The default is False.
    String syncToken = "syncToken_example"; // String | Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All entries deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries.
    try {
      Acl result = apiInstance.calendarAclList(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken, showDeleted, syncToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AclApi#calendarAclList");
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
| **maxResults** | **Integer**| Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional. | [optional] |
| **pageToken** | **String**| Token specifying which result page to return. Optional. | [optional] |
| **showDeleted** | **Boolean**| Whether to include deleted ACLs in the result. Deleted ACLs are represented by role equal to \&quot;none\&quot;. Deleted ACLs will always be included if syncToken is provided. Optional. The default is False. | [optional] |
| **syncToken** | **String**| Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All entries deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries. | [optional] |

### Return type

[**Acl**](Acl.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarAclPatch"></a>
# **calendarAclPatch**
> AclRule calendarAclPatch(calendarId, ruleId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, sendNotifications, aclRule)



Updates an access control rule. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AclApi;

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

    AclApi apiInstance = new AclApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String ruleId = "ruleId_example"; // String | ACL rule identifier.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean sendNotifications = true; // Boolean | Whether to send notifications about the calendar sharing change. Note that there are no notifications on access removal. Optional. The default is True.
    AclRule aclRule = new AclRule(); // AclRule | 
    try {
      AclRule result = apiInstance.calendarAclPatch(calendarId, ruleId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, sendNotifications, aclRule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AclApi#calendarAclPatch");
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
| **ruleId** | **String**| ACL rule identifier. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **sendNotifications** | **Boolean**| Whether to send notifications about the calendar sharing change. Note that there are no notifications on access removal. Optional. The default is True. | [optional] |
| **aclRule** | [**AclRule**](AclRule.md)|  | [optional] |

### Return type

[**AclRule**](AclRule.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarAclUpdate"></a>
# **calendarAclUpdate**
> AclRule calendarAclUpdate(calendarId, ruleId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, sendNotifications, aclRule)



Updates an access control rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AclApi;

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

    AclApi apiInstance = new AclApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String ruleId = "ruleId_example"; // String | ACL rule identifier.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean sendNotifications = true; // Boolean | Whether to send notifications about the calendar sharing change. Note that there are no notifications on access removal. Optional. The default is True.
    AclRule aclRule = new AclRule(); // AclRule | 
    try {
      AclRule result = apiInstance.calendarAclUpdate(calendarId, ruleId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, sendNotifications, aclRule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AclApi#calendarAclUpdate");
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
| **ruleId** | **String**| ACL rule identifier. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **sendNotifications** | **Boolean**| Whether to send notifications about the calendar sharing change. Note that there are no notifications on access removal. Optional. The default is True. | [optional] |
| **aclRule** | [**AclRule**](AclRule.md)|  | [optional] |

### Return type

[**AclRule**](AclRule.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarAclWatch"></a>
# **calendarAclWatch**
> Channel calendarAclWatch(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken, showDeleted, syncToken, channel)



Watch for changes to ACL resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AclApi;

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

    AclApi apiInstance = new AclApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional.
    String pageToken = "pageToken_example"; // String | Token specifying which result page to return. Optional.
    Boolean showDeleted = true; // Boolean | Whether to include deleted ACLs in the result. Deleted ACLs are represented by role equal to \"none\". Deleted ACLs will always be included if syncToken is provided. Optional. The default is False.
    String syncToken = "syncToken_example"; // String | Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All entries deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries.
    Channel channel = new Channel(); // Channel | 
    try {
      Channel result = apiInstance.calendarAclWatch(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken, showDeleted, syncToken, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AclApi#calendarAclWatch");
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
| **maxResults** | **Integer**| Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional. | [optional] |
| **pageToken** | **String**| Token specifying which result page to return. Optional. | [optional] |
| **showDeleted** | **Boolean**| Whether to include deleted ACLs in the result. Deleted ACLs are represented by role equal to \&quot;none\&quot;. Deleted ACLs will always be included if syncToken is provided. Optional. The default is False. | [optional] |
| **syncToken** | **String**| Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All entries deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries. | [optional] |
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

