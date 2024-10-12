# ModerationApi

All URIs are relative to *https://chat.stream-io-api.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ban_0**](ModerationApi.md#ban_0) | **POST** /moderation/ban | Ban user |
| [**createBlockList_0**](ModerationApi.md#createBlockList_0) | **POST** /blocklists | Create block list |
| [**deactivateUser_1**](ModerationApi.md#deactivateUser_1) | **POST** /users/{user_id}/deactivate | Deactivate user |
| [**deactivateUsers_1**](ModerationApi.md#deactivateUsers_1) | **POST** /users/deactivate | Deactivate users |
| [**deleteBlockList_0**](ModerationApi.md#deleteBlockList_0) | **DELETE** /blocklists/{name} | Delete block list |
| [**deleteUser_1**](ModerationApi.md#deleteUser_1) | **DELETE** /users/{user_id} | Delete user |
| [**deleteUsers_1**](ModerationApi.md#deleteUsers_1) | **POST** /users/delete | Delete Users |
| [**flag**](ModerationApi.md#flag) | **POST** /moderation/flag | Flag |
| [**getBlockList_0**](ModerationApi.md#getBlockList_0) | **GET** /blocklists/{name} | Get block list |
| [**listBlockLists_0**](ModerationApi.md#listBlockLists_0) | **GET** /blocklists | List block lists |
| [**muteUser_0**](ModerationApi.md#muteUser_0) | **POST** /moderation/mute | Mute user |
| [**queryBannedUsers_0**](ModerationApi.md#queryBannedUsers_0) | **GET** /query_banned_users | Query Banned Users |
| [**queryMessageFlags_0**](ModerationApi.md#queryMessageFlags_0) | **GET** /moderation/flags/message | Query Message Flags |
| [**reactivateUser_1**](ModerationApi.md#reactivateUser_1) | **POST** /users/{user_id}/reactivate | Reactivate user |
| [**reactivateUsers_1**](ModerationApi.md#reactivateUsers_1) | **POST** /users/reactivate | Reactivate users |
| [**unban_0**](ModerationApi.md#unban_0) | **DELETE** /moderation/ban | Unban user |
| [**unflag**](ModerationApi.md#unflag) | **POST** /moderation/unflag | Unflag |
| [**unmuteUser_0**](ModerationApi.md#unmuteUser_0) | **POST** /moderation/unmute | Unmute user |
| [**updateBlockList_0**](ModerationApi.md#updateBlockList_0) | **PUT** /blocklists/{name} | Update block list |


<a id="ban_0"></a>
# **ban_0**
> Response ban_0(banRequest)

Ban user

Restricts user activity either in specific channel or globally  Sends events: - user.banned  Required permissions: - BanChannelMember - BanUser 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    BanRequest banRequest = new BanRequest(); // BanRequest | 
    try {
      Response result = apiInstance.ban_0(banRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#ban_0");
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
| **banRequest** | [**BanRequest**](BanRequest.md)|  | |

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="createBlockList_0"></a>
# **createBlockList_0**
> Response createBlockList_0(createBlockListRequest)

Create block list

Creates a new application blocklist, once created the blocklist can be used by any channel type 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    CreateBlockListRequest createBlockListRequest = new CreateBlockListRequest(); // CreateBlockListRequest | Block list
    try {
      Response result = apiInstance.createBlockList_0(createBlockListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#createBlockList_0");
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
| **createBlockListRequest** | [**CreateBlockListRequest**](CreateBlockListRequest.md)| Block list | |

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="deactivateUser_1"></a>
# **deactivateUser_1**
> DeactivateUserResponse deactivateUser_1(userId, deactivateUserRequest)

Deactivate user

Deactivates user with possibility to activate it back  Sends events: - user.deactivated 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    String userId = "userId_example"; // String | 
    DeactivateUserRequest deactivateUserRequest = new DeactivateUserRequest(); // DeactivateUserRequest | 
    try {
      DeactivateUserResponse result = apiInstance.deactivateUser_1(userId, deactivateUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#deactivateUser_1");
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
| **userId** | **String**|  | |
| **deactivateUserRequest** | [**DeactivateUserRequest**](DeactivateUserRequest.md)|  | |

### Return type

[**DeactivateUserResponse**](DeactivateUserResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="deactivateUsers_1"></a>
# **deactivateUsers_1**
> DeactivateUsersResponse deactivateUsers_1(deactivateUsersRequest)

Deactivate users

Deactivate users in batches  Sends events: - user.deactivated 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    DeactivateUsersRequest deactivateUsersRequest = new DeactivateUsersRequest(); // DeactivateUsersRequest | 
    try {
      DeactivateUsersResponse result = apiInstance.deactivateUsers_1(deactivateUsersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#deactivateUsers_1");
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
| **deactivateUsersRequest** | [**DeactivateUsersRequest**](DeactivateUsersRequest.md)|  | |

### Return type

[**DeactivateUsersResponse**](DeactivateUsersResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="deleteBlockList_0"></a>
# **deleteBlockList_0**
> Response deleteBlockList_0(name)

Delete block list

Deletes previously created application blocklist 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    String name = "name_example"; // String | 
    try {
      Response result = apiInstance.deleteBlockList_0(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#deleteBlockList_0");
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
| **name** | **String**|  | |

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="deleteUser_1"></a>
# **deleteUser_1**
> DeleteUserResponse deleteUser_1(userId, markMessagesDeleted, hardDelete, deleteConversationChannels)

Delete user

Deletes user and optionally all their belongings. The Endpoint is deprecated, please use &#39;Delete Users&#39; endpoint instead  Sends events: - channel.deleted - message.deleted - user.deleted 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    String userId = "userId_example"; // String | 
    Boolean markMessagesDeleted = true; // Boolean | 
    Boolean hardDelete = true; // Boolean | 
    Boolean deleteConversationChannels = true; // Boolean | 
    try {
      DeleteUserResponse result = apiInstance.deleteUser_1(userId, markMessagesDeleted, hardDelete, deleteConversationChannels);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#deleteUser_1");
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
| **userId** | **String**|  | |
| **markMessagesDeleted** | **Boolean**|  | [optional] |
| **hardDelete** | **Boolean**|  | [optional] |
| **deleteConversationChannels** | **Boolean**|  | [optional] |

### Return type

[**DeleteUserResponse**](DeleteUserResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="deleteUsers_1"></a>
# **deleteUsers_1**
> DeleteUsersResponse deleteUsers_1(deleteUsersRequest)

Delete Users

Deletes users and optionally all their belongings asynchronously.  Sends events: - channel.deleted - user.deleted 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    DeleteUsersRequest deleteUsersRequest = new DeleteUsersRequest(); // DeleteUsersRequest | 
    try {
      DeleteUsersResponse result = apiInstance.deleteUsers_1(deleteUsersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#deleteUsers_1");
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
| **deleteUsersRequest** | [**DeleteUsersRequest**](DeleteUsersRequest.md)|  | |

### Return type

[**DeleteUsersResponse**](DeleteUsersResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="flag"></a>
# **flag**
> FlagResponse flag(flagRequest)

Flag

Reports message or user for review by moderators  Sends events: - message.flagged - user.flagged  Required permissions: - FlagMessage - FlagUser 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    FlagRequest flagRequest = new FlagRequest(); // FlagRequest | 
    try {
      FlagResponse result = apiInstance.flag(flagRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#flag");
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
| **flagRequest** | [**FlagRequest**](FlagRequest.md)|  | |

### Return type

[**FlagResponse**](FlagResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="getBlockList_0"></a>
# **getBlockList_0**
> GetBlockListResponse getBlockList_0(name)

Get block list

Returns block list by given name 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    String name = "name_example"; // String | 
    try {
      GetBlockListResponse result = apiInstance.getBlockList_0(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#getBlockList_0");
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
| **name** | **String**|  | |

### Return type

[**GetBlockListResponse**](GetBlockListResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="listBlockLists_0"></a>
# **listBlockLists_0**
> ListBlockListResponse listBlockLists_0()

List block lists

Returns all available block lists 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    try {
      ListBlockListResponse result = apiInstance.listBlockLists_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#listBlockLists_0");
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

[**ListBlockListResponse**](ListBlockListResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="muteUser_0"></a>
# **muteUser_0**
> MuteUserResponse muteUser_0(muteUserRequest)

Mute user

Mutes one or several users  Sends events: - user.muted  Required permissions: - MuteUser 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    MuteUserRequest muteUserRequest = new MuteUserRequest(); // MuteUserRequest | 
    try {
      MuteUserResponse result = apiInstance.muteUser_0(muteUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#muteUser_0");
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
| **muteUserRequest** | [**MuteUserRequest**](MuteUserRequest.md)|  | |

### Return type

[**MuteUserResponse**](MuteUserResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="queryBannedUsers_0"></a>
# **queryBannedUsers_0**
> QueryBannedUsersResponse queryBannedUsers_0(payload)

Query Banned Users

Find and filter channel scoped or global user bans  Required permissions: - ReadChannel 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    QueryBannedUsersRequest payload = new QueryBannedUsersRequest(); // QueryBannedUsersRequest | 
    try {
      QueryBannedUsersResponse result = apiInstance.queryBannedUsers_0(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#queryBannedUsers_0");
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
| **payload** | [**QueryBannedUsersRequest**](.md)|  | [optional] |

### Return type

[**QueryBannedUsersResponse**](QueryBannedUsersResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="queryMessageFlags_0"></a>
# **queryMessageFlags_0**
> QueryMessageFlagsResponse queryMessageFlags_0(payload)

Query Message Flags

Find and filter message flags  Required permissions: - ReadMessageFlags 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    QueryMessageFlagsRequest payload = new QueryMessageFlagsRequest(); // QueryMessageFlagsRequest | 
    try {
      QueryMessageFlagsResponse result = apiInstance.queryMessageFlags_0(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#queryMessageFlags_0");
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
| **payload** | [**QueryMessageFlagsRequest**](.md)|  | [optional] |

### Return type

[**QueryMessageFlagsResponse**](QueryMessageFlagsResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="reactivateUser_1"></a>
# **reactivateUser_1**
> ReactivateUserResponse reactivateUser_1(userId, reactivateUserRequest)

Reactivate user

Activates user who&#39;s been deactivated previously  Sends events: - user.reactivated 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    String userId = "userId_example"; // String | 
    ReactivateUserRequest reactivateUserRequest = new ReactivateUserRequest(); // ReactivateUserRequest | 
    try {
      ReactivateUserResponse result = apiInstance.reactivateUser_1(userId, reactivateUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#reactivateUser_1");
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
| **userId** | **String**|  | |
| **reactivateUserRequest** | [**ReactivateUserRequest**](ReactivateUserRequest.md)|  | |

### Return type

[**ReactivateUserResponse**](ReactivateUserResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="reactivateUsers_1"></a>
# **reactivateUsers_1**
> ReactivateUsersResponse reactivateUsers_1(reactivateUsersRequest)

Reactivate users

Reactivate users in batches  Sends events: - user.reactivated 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    ReactivateUsersRequest reactivateUsersRequest = new ReactivateUsersRequest(); // ReactivateUsersRequest | 
    try {
      ReactivateUsersResponse result = apiInstance.reactivateUsers_1(reactivateUsersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#reactivateUsers_1");
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
| **reactivateUsersRequest** | [**ReactivateUsersRequest**](ReactivateUsersRequest.md)|  | |

### Return type

[**ReactivateUsersResponse**](ReactivateUsersResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="unban_0"></a>
# **unban_0**
> Response unban_0(targetUserId, type, id)

Unban user

Removes previously applied ban  Sends events: - user.unbanned  Required permissions: - BanChannelMember - BanUser 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    String targetUserId = "targetUserId_example"; // String | 
    String type = "type_example"; // String | 
    String id = "id_example"; // String | 
    try {
      Response result = apiInstance.unban_0(targetUserId, type, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#unban_0");
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
| **targetUserId** | **String**|  | [optional] |
| **type** | **String**|  | [optional] |
| **id** | **String**|  | [optional] |

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="unflag"></a>
# **unflag**
> FlagResponse unflag(flagRequest)

Unflag

Removes previously created user or message flag  Required permissions: - FlagMessage - FlagUser 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    FlagRequest flagRequest = new FlagRequest(); // FlagRequest | 
    try {
      FlagResponse result = apiInstance.unflag(flagRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#unflag");
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
| **flagRequest** | [**FlagRequest**](FlagRequest.md)|  | |

### Return type

[**FlagResponse**](FlagResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="unmuteUser_0"></a>
# **unmuteUser_0**
> UnmuteResponse unmuteUser_0(unmuteUserRequest)

Unmute user

Unmutes previously muted user  Sends events: - user.unmuted  Required permissions: - MuteUser 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    UnmuteUserRequest unmuteUserRequest = new UnmuteUserRequest(); // UnmuteUserRequest | 
    try {
      UnmuteResponse result = apiInstance.unmuteUser_0(unmuteUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#unmuteUser_0");
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
| **unmuteUserRequest** | [**UnmuteUserRequest**](UnmuteUserRequest.md)|  | |

### Return type

[**UnmuteResponse**](UnmuteResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="updateBlockList_0"></a>
# **updateBlockList_0**
> Response updateBlockList_0(name, updateBlockListRequest)

Update block list

Updates contents of the block list 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    ModerationApi apiInstance = new ModerationApi(defaultClient);
    String name = "name_example"; // String | 
    UpdateBlockListRequest updateBlockListRequest = new UpdateBlockListRequest(); // UpdateBlockListRequest | 
    try {
      Response result = apiInstance.updateBlockList_0(name, updateBlockListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModerationApi#updateBlockList_0");
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
| **name** | **String**|  | |
| **updateBlockListRequest** | [**UpdateBlockListRequest**](UpdateBlockListRequest.md)|  | |

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

