# AdminUsersApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminUsersAssign**](AdminUsersApi.md#adminUsersAssign) | **POST** /admin.users.assign |  |
| [**adminUsersInvite**](AdminUsersApi.md#adminUsersInvite) | **POST** /admin.users.invite |  |
| [**adminUsersList**](AdminUsersApi.md#adminUsersList) | **GET** /admin.users.list |  |
| [**adminUsersRemove**](AdminUsersApi.md#adminUsersRemove) | **POST** /admin.users.remove |  |
| [**adminUsersSetAdmin**](AdminUsersApi.md#adminUsersSetAdmin) | **POST** /admin.users.setAdmin |  |
| [**adminUsersSetExpiration**](AdminUsersApi.md#adminUsersSetExpiration) | **POST** /admin.users.setExpiration |  |
| [**adminUsersSetOwner**](AdminUsersApi.md#adminUsersSetOwner) | **POST** /admin.users.setOwner |  |
| [**adminUsersSetRegular**](AdminUsersApi.md#adminUsersSetRegular) | **POST** /admin.users.setRegular |  |


<a id="adminUsersAssign"></a>
# **adminUsersAssign**
> DefaultSuccessTemplate adminUsersAssign(token, teamId, userId, channelIds, isRestricted, isUltraRestricted)



Add an Enterprise user to a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminUsersApi apiInstance = new AdminUsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
    String teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
    String userId = "userId_example"; // String | The ID of the user to add to the workspace.
    String channelIds = "channelIds_example"; // String | Comma separated values of channel IDs to add user in the new workspace.
    Boolean isRestricted = true; // Boolean | True if user should be added to the workspace as a guest.
    Boolean isUltraRestricted = true; // Boolean | True if user should be added to the workspace as a single-channel guest.
    try {
      DefaultSuccessTemplate result = apiInstance.adminUsersAssign(token, teamId, userId, channelIds, isRestricted, isUltraRestricted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminUsersApi#adminUsersAssign");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | |
| **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | |
| **userId** | **String**| The ID of the user to add to the workspace. | |
| **channelIds** | **String**| Comma separated values of channel IDs to add user in the new workspace. | [optional] |
| **isRestricted** | **Boolean**| True if user should be added to the workspace as a guest. | [optional] |
| **isUltraRestricted** | **Boolean**| True if user should be added to the workspace as a single-channel guest. | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="adminUsersInvite"></a>
# **adminUsersInvite**
> DefaultSuccessTemplate adminUsersInvite(token, channelIds, email, teamId, customMessage, guestExpirationTs, isRestricted, isUltraRestricted, realName, resend)



Invite a user to a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminUsersApi apiInstance = new AdminUsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
    String channelIds = "channelIds_example"; // String | A comma-separated list of `channel_id`s for this user to join. At least one channel is required.
    String email = "email_example"; // String | The email address of the person to invite.
    String teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
    String customMessage = "customMessage_example"; // String | An optional message to send to the user in the invite email.
    String guestExpirationTs = "guestExpirationTs_example"; // String | Timestamp when guest account should be disabled. Only include this timestamp if you are inviting a guest user and you want their account to expire on a certain date.
    Boolean isRestricted = true; // Boolean | Is this user a multi-channel guest user? (default: false)
    Boolean isUltraRestricted = true; // Boolean | Is this user a single channel guest user? (default: false)
    String realName = "realName_example"; // String | Full name of the user.
    Boolean resend = true; // Boolean | Allow this invite to be resent in the future if a user has not signed up yet. (default: false)
    try {
      DefaultSuccessTemplate result = apiInstance.adminUsersInvite(token, channelIds, email, teamId, customMessage, guestExpirationTs, isRestricted, isUltraRestricted, realName, resend);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminUsersApi#adminUsersInvite");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | |
| **channelIds** | **String**| A comma-separated list of &#x60;channel_id&#x60;s for this user to join. At least one channel is required. | |
| **email** | **String**| The email address of the person to invite. | |
| **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | |
| **customMessage** | **String**| An optional message to send to the user in the invite email. | [optional] |
| **guestExpirationTs** | **String**| Timestamp when guest account should be disabled. Only include this timestamp if you are inviting a guest user and you want their account to expire on a certain date. | [optional] |
| **isRestricted** | **Boolean**| Is this user a multi-channel guest user? (default: false) | [optional] |
| **isUltraRestricted** | **Boolean**| Is this user a single channel guest user? (default: false) | [optional] |
| **realName** | **String**| Full name of the user. | [optional] |
| **resend** | **Boolean**| Allow this invite to be resent in the future if a user has not signed up yet. (default: false) | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="adminUsersList"></a>
# **adminUsersList**
> DefaultSuccessTemplate adminUsersList(token, teamId, cursor, limit)



List users on a workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminUsersApi apiInstance = new AdminUsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.users:read`
    String teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
    String cursor = "cursor_example"; // String | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.
    Integer limit = 56; // Integer | Limit for how many users to be retrieved per page
    try {
      DefaultSuccessTemplate result = apiInstance.adminUsersList(token, teamId, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminUsersApi#adminUsersList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:read&#x60; | |
| **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | |
| **cursor** | **String**| Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page. | [optional] |
| **limit** | **Integer**| Limit for how many users to be retrieved per page | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="adminUsersRemove"></a>
# **adminUsersRemove**
> DefaultSuccessTemplate adminUsersRemove(token, teamId, userId)



Remove a user from a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminUsersApi apiInstance = new AdminUsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
    String teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
    String userId = "userId_example"; // String | The ID of the user to remove.
    try {
      DefaultSuccessTemplate result = apiInstance.adminUsersRemove(token, teamId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminUsersApi#adminUsersRemove");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | |
| **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | |
| **userId** | **String**| The ID of the user to remove. | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="adminUsersSetAdmin"></a>
# **adminUsersSetAdmin**
> DefaultSuccessTemplate adminUsersSetAdmin(token, teamId, userId)



Set an existing guest, regular user, or owner to be an admin user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminUsersApi apiInstance = new AdminUsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
    String teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
    String userId = "userId_example"; // String | The ID of the user to designate as an admin.
    try {
      DefaultSuccessTemplate result = apiInstance.adminUsersSetAdmin(token, teamId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminUsersApi#adminUsersSetAdmin");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | |
| **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | |
| **userId** | **String**| The ID of the user to designate as an admin. | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="adminUsersSetExpiration"></a>
# **adminUsersSetExpiration**
> DefaultSuccessTemplate adminUsersSetExpiration(token, expirationTs, teamId, userId)



Set an expiration for a guest user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminUsersApi apiInstance = new AdminUsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
    Integer expirationTs = 56; // Integer | Timestamp when guest account should be disabled.
    String teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
    String userId = "userId_example"; // String | The ID of the user to set an expiration for.
    try {
      DefaultSuccessTemplate result = apiInstance.adminUsersSetExpiration(token, expirationTs, teamId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminUsersApi#adminUsersSetExpiration");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | |
| **expirationTs** | **Integer**| Timestamp when guest account should be disabled. | |
| **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | |
| **userId** | **String**| The ID of the user to set an expiration for. | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="adminUsersSetOwner"></a>
# **adminUsersSetOwner**
> DefaultSuccessTemplate adminUsersSetOwner(token, teamId, userId)



Set an existing guest, regular user, or admin user to be a workspace owner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminUsersApi apiInstance = new AdminUsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
    String teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
    String userId = "userId_example"; // String | Id of the user to promote to owner.
    try {
      DefaultSuccessTemplate result = apiInstance.adminUsersSetOwner(token, teamId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminUsersApi#adminUsersSetOwner");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | |
| **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | |
| **userId** | **String**| Id of the user to promote to owner. | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="adminUsersSetRegular"></a>
# **adminUsersSetRegular**
> DefaultSuccessTemplate adminUsersSetRegular(token, teamId, userId)



Set an existing guest user, admin user, or owner to be a regular user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminUsersApi apiInstance = new AdminUsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
    String teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
    String userId = "userId_example"; // String | The ID of the user to designate as a regular user.
    try {
      DefaultSuccessTemplate result = apiInstance.adminUsersSetRegular(token, teamId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminUsersApi#adminUsersSetRegular");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | |
| **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | |
| **userId** | **String**| The ID of the user to designate as a regular user. | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

