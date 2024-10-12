# SocialApi

All URIs are relative to *https://www.bungie.net/Platform*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**socialAcceptFriendRequest**](SocialApi.md#socialAcceptFriendRequest) | **POST** /Social/Friends/Requests/Accept/{membershipId}/ |  |
| [**socialDeclineFriendRequest**](SocialApi.md#socialDeclineFriendRequest) | **POST** /Social/Friends/Requests/Decline/{membershipId}/ |  |
| [**socialGetFriendList**](SocialApi.md#socialGetFriendList) | **GET** /Social/Friends/ |  |
| [**socialGetFriendRequestList**](SocialApi.md#socialGetFriendRequestList) | **GET** /Social/Friends/Requests/ |  |
| [**socialGetPlatformFriendList**](SocialApi.md#socialGetPlatformFriendList) | **GET** /Social/PlatformFriends/{friendPlatform}/{page}/ |  |
| [**socialIssueFriendRequest**](SocialApi.md#socialIssueFriendRequest) | **POST** /Social/Friends/Add/{membershipId}/ |  |
| [**socialRemoveFriend**](SocialApi.md#socialRemoveFriend) | **POST** /Social/Friends/Remove/{membershipId}/ |  |
| [**socialRemoveFriendRequest**](SocialApi.md#socialRemoveFriendRequest) | **POST** /Social/Friends/Requests/Remove/{membershipId}/ |  |


<a id="socialAcceptFriendRequest"></a>
# **socialAcceptFriendRequest**
> GroupV2GetUserClanInviteSetting200Response socialAcceptFriendRequest(membershipId)



Accepts a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SocialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SocialApi apiInstance = new SocialApi(defaultClient);
    String membershipId = "membershipId_example"; // String | The membership id of the user you wish to accept.
    try {
      GroupV2GetUserClanInviteSetting200Response result = apiInstance.socialAcceptFriendRequest(membershipId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SocialApi#socialAcceptFriendRequest");
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
| **membershipId** | **String**| The membership id of the user you wish to accept. | |

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="socialDeclineFriendRequest"></a>
# **socialDeclineFriendRequest**
> GroupV2GetUserClanInviteSetting200Response socialDeclineFriendRequest(membershipId)



Declines a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SocialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SocialApi apiInstance = new SocialApi(defaultClient);
    String membershipId = "membershipId_example"; // String | The membership id of the user you wish to decline.
    try {
      GroupV2GetUserClanInviteSetting200Response result = apiInstance.socialDeclineFriendRequest(membershipId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SocialApi#socialDeclineFriendRequest");
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
| **membershipId** | **String**| The membership id of the user you wish to decline. | |

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="socialGetFriendList"></a>
# **socialGetFriendList**
> SocialGetFriendList200Response socialGetFriendList()



Returns your Bungie Friend list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SocialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SocialApi apiInstance = new SocialApi(defaultClient);
    try {
      SocialGetFriendList200Response result = apiInstance.socialGetFriendList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SocialApi#socialGetFriendList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SocialGetFriendList200Response**](SocialGetFriendList200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="socialGetFriendRequestList"></a>
# **socialGetFriendRequestList**
> SocialGetFriendRequestList200Response socialGetFriendRequestList()



Returns your friend request queue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SocialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SocialApi apiInstance = new SocialApi(defaultClient);
    try {
      SocialGetFriendRequestList200Response result = apiInstance.socialGetFriendRequestList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SocialApi#socialGetFriendRequestList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SocialGetFriendRequestList200Response**](SocialGetFriendRequestList200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="socialGetPlatformFriendList"></a>
# **socialGetPlatformFriendList**
> SocialGetPlatformFriendList200Response socialGetPlatformFriendList(friendPlatform, page)



Gets the platform friend of the requested type, with additional information if they have Bungie accounts. Must have a recent login session with said platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SocialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    SocialApi apiInstance = new SocialApi(defaultClient);
    Integer friendPlatform = 56; // Integer | The platform friend type.
    String page = "page_example"; // String | The zero based page to return. Page size is 100.
    try {
      SocialGetPlatformFriendList200Response result = apiInstance.socialGetPlatformFriendList(friendPlatform, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SocialApi#socialGetPlatformFriendList");
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
| **friendPlatform** | **Integer**| The platform friend type. | |
| **page** | **String**| The zero based page to return. Page size is 100. | |

### Return type

[**SocialGetPlatformFriendList200Response**](SocialGetPlatformFriendList200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="socialIssueFriendRequest"></a>
# **socialIssueFriendRequest**
> GroupV2GetUserClanInviteSetting200Response socialIssueFriendRequest(membershipId)



Requests a friend relationship with the target user. Any of the target user&#39;s linked membership ids are valid inputs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SocialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SocialApi apiInstance = new SocialApi(defaultClient);
    String membershipId = "membershipId_example"; // String | The membership id of the user you wish to add.
    try {
      GroupV2GetUserClanInviteSetting200Response result = apiInstance.socialIssueFriendRequest(membershipId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SocialApi#socialIssueFriendRequest");
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
| **membershipId** | **String**| The membership id of the user you wish to add. | |

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="socialRemoveFriend"></a>
# **socialRemoveFriend**
> GroupV2GetUserClanInviteSetting200Response socialRemoveFriend(membershipId)



Remove a friend relationship with the target user. The user must be on your friend list, though no error will occur if they are not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SocialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SocialApi apiInstance = new SocialApi(defaultClient);
    String membershipId = "membershipId_example"; // String | The membership id of the user you wish to remove.
    try {
      GroupV2GetUserClanInviteSetting200Response result = apiInstance.socialRemoveFriend(membershipId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SocialApi#socialRemoveFriend");
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
| **membershipId** | **String**| The membership id of the user you wish to remove. | |

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="socialRemoveFriendRequest"></a>
# **socialRemoveFriendRequest**
> GroupV2GetUserClanInviteSetting200Response socialRemoveFriendRequest(membershipId)



Remove a friend relationship with the target user. The user must be on your outgoing request friend list, though no error will occur if they are not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SocialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SocialApi apiInstance = new SocialApi(defaultClient);
    String membershipId = "membershipId_example"; // String | The membership id of the user you wish to remove.
    try {
      GroupV2GetUserClanInviteSetting200Response result = apiInstance.socialRemoveFriendRequest(membershipId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SocialApi#socialRemoveFriendRequest");
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
| **membershipId** | **String**| The membership id of the user you wish to remove. | |

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

