# ChannelsPrivateChannelMembersApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteChannelPrivacyUser**](ChannelsPrivateChannelMembersApi.md#deleteChannelPrivacyUser) | **DELETE** /channels/{channel_id}/privacy/users/{user_id} | Restrict a user from viewing a private channel |
| [**getChannelPrivacyUsers**](ChannelsPrivateChannelMembersApi.md#getChannelPrivacyUsers) | **GET** /channels/{channel_id}/privacy/users | Get all the users who can view a private channel |
| [**setChannelPrivacyUser**](ChannelsPrivateChannelMembersApi.md#setChannelPrivacyUser) | **PUT** /channels/{channel_id}/privacy/users/{user_id} | Permit a specific user to view a private channel |
| [**setChannelPrivacyUsers**](ChannelsPrivateChannelMembersApi.md#setChannelPrivacyUsers) | **PUT** /channels/{channel_id}/privacy/users | Permit a list of users to view a private channel |


<a id="deleteChannelPrivacyUser"></a>
# **deleteChannelPrivacyUser**
> deleteChannelPrivacyUser(channelId, userId)

Restrict a user from viewing a private channel

This method prevents a single user from being able to access the specified private channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsPrivateChannelMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ChannelsPrivateChannelMembersApi apiInstance = new ChannelsPrivateChannelMembersApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      apiInstance.deleteChannelPrivacyUser(channelId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsPrivateChannelMembersApi#deleteChannelPrivacyUser");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The user can no longer view the private channel. |  -  |
| **401** | Error code 8003: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user doesn&#39;t own this channel. |  -  |
| **404** | Error code 2204: You can&#39;t add this user to a channel of this type. |  -  |

<a id="getChannelPrivacyUsers"></a>
# **getChannelPrivacyUsers**
> List&lt;User&gt; getChannelPrivacyUsers(channelId, direction, page, perPage)

Get all the users who can view a private channel

This method gets all the users who have access to the specified private channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsPrivateChannelMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ChannelsPrivateChannelMembersApi apiInstance = new ChannelsPrivateChannelMembersApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<User> result = apiInstance.getChannelPrivacyUsers(channelId, direction, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsPrivateChannelMembersApi#getChannelPrivacyUsers");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The users were returned. |  -  |
| **401** | Error code 8003: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user doesn&#39;t own this channel. |  -  |
| **404** | Error code 2204: You can&#39;t add this user to a channel of this type. |  -  |

<a id="setChannelPrivacyUser"></a>
# **setChannelPrivacyUser**
> setChannelPrivacyUser(channelId, userId)

Permit a specific user to view a private channel

This method gives a single user access to the specified private channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsPrivateChannelMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ChannelsPrivateChannelMembersApi apiInstance = new ChannelsPrivateChannelMembersApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      apiInstance.setChannelPrivacyUser(channelId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsPrivateChannelMembersApi#setChannelPrivacyUser");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user can now view the private channel. |  -  |
| **401** | Error code 8003: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user doesn&#39;t own this channel. |  -  |
| **404** | Error code 2204: You can&#39;t add this user to a channel of this type. |  -  |

<a id="setChannelPrivacyUsers"></a>
# **setChannelPrivacyUsers**
> List&lt;User&gt; setChannelPrivacyUsers(channelId, setChannelPrivacyUsersRequest)

Permit a list of users to view a private channel

This method gives multiple users access to the specified private channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsPrivateChannelMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ChannelsPrivateChannelMembersApi apiInstance = new ChannelsPrivateChannelMembersApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    SetChannelPrivacyUsersRequest setChannelPrivacyUsersRequest = new SetChannelPrivacyUsersRequest(); // SetChannelPrivacyUsersRequest | 
    try {
      List<User> result = apiInstance.setChannelPrivacyUsers(channelId, setChannelPrivacyUsersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsPrivateChannelMembersApi#setChannelPrivacyUsers");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
| **setChannelPrivacyUsersRequest** | [**SetChannelPrivacyUsersRequest**](SetChannelPrivacyUsersRequest.md)|  | |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.user+json
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The users can now view the private channel. |  -  |
| **400** | * Error code 2205: There was no request body, or the request body is malformed. * Error code 2900: At least one of the specified user accounts doesn&#39;t exist. |  -  |
| **401** | Error code 8003: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user doesn&#39;t own this channel. |  -  |
| **404** | Error code 2204: You can&#39;t add one or more of these users to a channel of this type. |  -  |

