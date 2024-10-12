# UsersApi

All URIs are relative to *http://discourse.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminGetUser**](UsersApi.md#adminGetUser) | **GET** /admin/users/{id}.json | Get a user by id |
| [**adminListUsers**](UsersApi.md#adminListUsers) | **GET** /admin/users/list/{flag}.json | Get a list of users |
| [**anonymizeUser**](UsersApi.md#anonymizeUser) | **PUT** /admin/users/{id}/anonymize.json | Anonymize a user |
| [**changePassword**](UsersApi.md#changePassword) | **PUT** /users/password-reset/{token}.json | Change password |
| [**createUser**](UsersApi.md#createUser) | **POST** /users.json | Creates a user |
| [**deleteUser**](UsersApi.md#deleteUser) | **DELETE** /admin/users/{id}.json | Delete a user |
| [**getUser**](UsersApi.md#getUser) | **GET** /u/{username}.json | Get a single user by username |
| [**getUserEmails**](UsersApi.md#getUserEmails) | **GET** /u/{username}/emails.json | Get email addresses belonging to a user |
| [**getUserExternalId**](UsersApi.md#getUserExternalId) | **GET** /u/by-external/{external_id}.json | Get a user by external_id |
| [**getUserIdentiyProviderExternalId**](UsersApi.md#getUserIdentiyProviderExternalId) | **GET** /u/by-external/{provider}/{external_id}.json | Get a user by identity provider external ID |
| [**listUserActions**](UsersApi.md#listUserActions) | **GET** /user_actions.json | Get a list of user actions |
| [**listUserBadges_0**](UsersApi.md#listUserBadges_0) | **GET** /user-badges/{username}.json | List badges for a user |
| [**listUsersPublic**](UsersApi.md#listUsersPublic) | **GET** /directory_items.json | Get a public list of users |
| [**logOutUser**](UsersApi.md#logOutUser) | **POST** /admin/users/{id}/log_out.json | Log a user out |
| [**refreshGravatar**](UsersApi.md#refreshGravatar) | **POST** /user_avatar/{username}/refresh_gravatar.json | Refresh gravatar |
| [**sendPasswordResetEmail**](UsersApi.md#sendPasswordResetEmail) | **POST** /session/forgot_password.json | Send password reset email |
| [**silenceUser**](UsersApi.md#silenceUser) | **PUT** /admin/users/{id}/silence.json | Silence a user |
| [**suspendUser**](UsersApi.md#suspendUser) | **PUT** /admin/users/{id}/suspend.json | Suspend a user |
| [**updateAvatar**](UsersApi.md#updateAvatar) | **PUT** /u/{username}/preferences/avatar/pick.json | Update avatar |
| [**updateEmail**](UsersApi.md#updateEmail) | **PUT** /u/{username}/preferences/email.json | Update email |
| [**updateUser**](UsersApi.md#updateUser) | **PUT** /u/{username}.json | Update a user |
| [**updateUsername**](UsersApi.md#updateUsername) | **PUT** /u/{username}/preferences/username.json | Update username |


<a id="adminGetUser"></a>
# **adminGetUser**
> AdminGetUser200Response adminGetUser(id)

Get a user by id

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      AdminGetUser200Response result = apiInstance.adminGetUser(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#adminGetUser");
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
| **id** | **Integer**|  | |

### Return type

[**AdminGetUser200Response**](AdminGetUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="adminListUsers"></a>
# **adminListUsers**
> Set&lt;AdminListUsers200ResponseInner&gt; adminListUsers(flag, order, asc, page, showEmails)

Get a list of users

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String flag = "active"; // String | 
    String order = "created"; // String | 
    String asc = "true"; // String | 
    Integer page = 56; // Integer | 
    Boolean showEmails = true; // Boolean | 
    try {
      Set<AdminListUsers200ResponseInner> result = apiInstance.adminListUsers(flag, order, asc, page, showEmails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#adminListUsers");
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
| **flag** | **String**|  | [enum: active, new, staff, suspended, blocked, suspect] |
| **order** | **String**|  | [optional] [enum: created, last_emailed, seen, username, email, trust_level, days_visited, posts_read, topics_viewed, posts, read_time] |
| **asc** | **String**|  | [optional] [enum: true] |
| **page** | **Integer**|  | [optional] |
| **showEmails** | **Boolean**|  | [optional] |

### Return type

[**Set&lt;AdminListUsers200ResponseInner&gt;**](AdminListUsers200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="anonymizeUser"></a>
# **anonymizeUser**
> AnonymizeUser200Response anonymizeUser(id)

Anonymize a user

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      AnonymizeUser200Response result = apiInstance.anonymizeUser(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#anonymizeUser");
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
| **id** | **Integer**|  | |

### Return type

[**AnonymizeUser200Response**](AnonymizeUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="changePassword"></a>
# **changePassword**
> changePassword(token, changePasswordRequest)

Change password

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String token = "token_example"; // String | 
    ChangePasswordRequest changePasswordRequest = new ChangePasswordRequest(); // ChangePasswordRequest | 
    try {
      apiInstance.changePassword(token, changePasswordRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#changePassword");
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
| **token** | **String**|  | |
| **changePasswordRequest** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="createUser"></a>
# **createUser**
> CreateUser200Response createUser(apiKey, apiUsername, createUserRequest)

Creates a user

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    CreateUserRequest createUserRequest = new CreateUserRequest(); // CreateUserRequest | 
    try {
      CreateUser200Response result = apiInstance.createUser(apiKey, apiUsername, createUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#createUser");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **createUserRequest** | [**CreateUserRequest**](CreateUserRequest.md)|  | [optional] |

### Return type

[**CreateUser200Response**](CreateUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user created |  -  |

<a id="deleteUser"></a>
# **deleteUser**
> DeleteUser200Response deleteUser(id, deleteUserRequest)

Delete a user

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | 
    DeleteUserRequest deleteUserRequest = new DeleteUserRequest(); // DeleteUserRequest | 
    try {
      DeleteUser200Response result = apiInstance.deleteUser(id, deleteUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#deleteUser");
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
| **id** | **Integer**|  | |
| **deleteUserRequest** | [**DeleteUserRequest**](DeleteUserRequest.md)|  | [optional] |

### Return type

[**DeleteUser200Response**](DeleteUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="getUser"></a>
# **getUser**
> GetUserExternalId200Response getUser(apiKey, apiUsername, username)

Get a single user by username

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String username = "username_example"; // String | 
    try {
      GetUserExternalId200Response result = apiInstance.getUser(apiKey, apiUsername, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUser");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **username** | **String**|  | |

### Return type

[**GetUserExternalId200Response**](GetUserExternalId200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user response |  -  |

<a id="getUserEmails"></a>
# **getUserEmails**
> GetUserEmails200Response getUserEmails(username)

Get email addresses belonging to a user

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String username = "username_example"; // String | 
    try {
      GetUserEmails200Response result = apiInstance.getUserEmails(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserEmails");
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
| **username** | **String**|  | |

### Return type

[**GetUserEmails200Response**](GetUserEmails200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="getUserExternalId"></a>
# **getUserExternalId**
> GetUserExternalId200Response getUserExternalId(apiKey, apiUsername, externalId)

Get a user by external_id

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String externalId = "externalId_example"; // String | 
    try {
      GetUserExternalId200Response result = apiInstance.getUserExternalId(apiKey, apiUsername, externalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserExternalId");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **externalId** | **String**|  | |

### Return type

[**GetUserExternalId200Response**](GetUserExternalId200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user response |  -  |

<a id="getUserIdentiyProviderExternalId"></a>
# **getUserIdentiyProviderExternalId**
> GetUserExternalId200Response getUserIdentiyProviderExternalId(apiKey, apiUsername, provider, externalId)

Get a user by identity provider external ID

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String provider = "provider_example"; // String | Authentication provider name. Can be found in the provider callback URL: `/auth/{provider}/callback`
    String externalId = "externalId_example"; // String | 
    try {
      GetUserExternalId200Response result = apiInstance.getUserIdentiyProviderExternalId(apiKey, apiUsername, provider, externalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserIdentiyProviderExternalId");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **provider** | **String**| Authentication provider name. Can be found in the provider callback URL: &#x60;/auth/{provider}/callback&#x60; | |
| **externalId** | **String**|  | |

### Return type

[**GetUserExternalId200Response**](GetUserExternalId200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user response |  -  |

<a id="listUserActions"></a>
# **listUserActions**
> ListUserActions200Response listUserActions(offset, username, filter)

Get a list of user actions

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer offset = 56; // Integer | 
    String username = "username_example"; // String | 
    String filter = "filter_example"; // String | 
    try {
      ListUserActions200Response result = apiInstance.listUserActions(offset, username, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#listUserActions");
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
| **offset** | **Integer**|  | |
| **username** | **String**|  | |
| **filter** | **String**|  | |

### Return type

[**ListUserActions200Response**](ListUserActions200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="listUserBadges_0"></a>
# **listUserBadges_0**
> ListUserBadges200Response listUserBadges_0(username)

List badges for a user

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String username = "username_example"; // String | 
    try {
      ListUserBadges200Response result = apiInstance.listUserBadges_0(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#listUserBadges_0");
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
| **username** | **String**|  | |

### Return type

[**ListUserBadges200Response**](ListUserBadges200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="listUsersPublic"></a>
# **listUsersPublic**
> ListUsersPublic200Response listUsersPublic(period, order, asc, page)

Get a public list of users

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String period = "daily"; // String | 
    String order = "likes_received"; // String | 
    String asc = "true"; // String | 
    Integer page = 56; // Integer | 
    try {
      ListUsersPublic200Response result = apiInstance.listUsersPublic(period, order, asc, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#listUsersPublic");
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
| **period** | **String**|  | [enum: daily, weekly, monthly, quarterly, yearly, all] |
| **order** | **String**|  | [enum: likes_received, likes_given, topic_count, post_count, topics_entered, posts_read, days_visited] |
| **asc** | **String**|  | [optional] [enum: true] |
| **page** | **Integer**|  | [optional] |

### Return type

[**ListUsersPublic200Response**](ListUsersPublic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | directory items response |  -  |

<a id="logOutUser"></a>
# **logOutUser**
> DeleteGroup200Response logOutUser(id)

Log a user out

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      DeleteGroup200Response result = apiInstance.logOutUser(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#logOutUser");
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
| **id** | **Integer**|  | |

### Return type

[**DeleteGroup200Response**](DeleteGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="refreshGravatar"></a>
# **refreshGravatar**
> RefreshGravatar200Response refreshGravatar(username)

Refresh gravatar

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String username = "username_example"; // String | 
    try {
      RefreshGravatar200Response result = apiInstance.refreshGravatar(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#refreshGravatar");
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
| **username** | **String**|  | |

### Return type

[**RefreshGravatar200Response**](RefreshGravatar200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="sendPasswordResetEmail"></a>
# **sendPasswordResetEmail**
> SendPasswordResetEmail200Response sendPasswordResetEmail(sendPasswordResetEmailRequest)

Send password reset email

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    SendPasswordResetEmailRequest sendPasswordResetEmailRequest = new SendPasswordResetEmailRequest(); // SendPasswordResetEmailRequest | 
    try {
      SendPasswordResetEmail200Response result = apiInstance.sendPasswordResetEmail(sendPasswordResetEmailRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#sendPasswordResetEmail");
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
| **sendPasswordResetEmailRequest** | [**SendPasswordResetEmailRequest**](SendPasswordResetEmailRequest.md)|  | [optional] |

### Return type

[**SendPasswordResetEmail200Response**](SendPasswordResetEmail200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="silenceUser"></a>
# **silenceUser**
> SilenceUser200Response silenceUser(id, silenceUserRequest)

Silence a user

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | 
    SilenceUserRequest silenceUserRequest = new SilenceUserRequest(); // SilenceUserRequest | 
    try {
      SilenceUser200Response result = apiInstance.silenceUser(id, silenceUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#silenceUser");
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
| **id** | **Integer**|  | |
| **silenceUserRequest** | [**SilenceUserRequest**](SilenceUserRequest.md)|  | [optional] |

### Return type

[**SilenceUser200Response**](SilenceUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="suspendUser"></a>
# **suspendUser**
> SuspendUser200Response suspendUser(id, suspendUserRequest)

Suspend a user

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | 
    SuspendUserRequest suspendUserRequest = new SuspendUserRequest(); // SuspendUserRequest | 
    try {
      SuspendUser200Response result = apiInstance.suspendUser(id, suspendUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#suspendUser");
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
| **id** | **Integer**|  | |
| **suspendUserRequest** | [**SuspendUserRequest**](SuspendUserRequest.md)|  | [optional] |

### Return type

[**SuspendUser200Response**](SuspendUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="updateAvatar"></a>
# **updateAvatar**
> DeleteGroup200Response updateAvatar(username, updateAvatarRequest)

Update avatar

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String username = "username_example"; // String | 
    UpdateAvatarRequest updateAvatarRequest = new UpdateAvatarRequest(); // UpdateAvatarRequest | 
    try {
      DeleteGroup200Response result = apiInstance.updateAvatar(username, updateAvatarRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#updateAvatar");
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
| **username** | **String**|  | |
| **updateAvatarRequest** | [**UpdateAvatarRequest**](UpdateAvatarRequest.md)|  | [optional] |

### Return type

[**DeleteGroup200Response**](DeleteGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | avatar updated |  -  |

<a id="updateEmail"></a>
# **updateEmail**
> updateEmail(username, updateEmailRequest)

Update email

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String username = "username_example"; // String | 
    UpdateEmailRequest updateEmailRequest = new UpdateEmailRequest(); // UpdateEmailRequest | 
    try {
      apiInstance.updateEmail(username, updateEmailRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#updateEmail");
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
| **username** | **String**|  | |
| **updateEmailRequest** | [**UpdateEmailRequest**](UpdateEmailRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | email updated |  -  |

<a id="updateUser"></a>
# **updateUser**
> UpdateUser200Response updateUser(apiKey, apiUsername, username, updateUserRequest)

Update a user

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String username = "username_example"; // String | 
    UpdateUserRequest updateUserRequest = new UpdateUserRequest(); // UpdateUserRequest | 
    try {
      UpdateUser200Response result = apiInstance.updateUser(apiKey, apiUsername, username, updateUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#updateUser");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **username** | **String**|  | |
| **updateUserRequest** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | [optional] |

### Return type

[**UpdateUser200Response**](UpdateUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user updated |  -  |

<a id="updateUsername"></a>
# **updateUsername**
> updateUsername(username, updateUsernameRequest)

Update username

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
    defaultClient.setBasePath("http://discourse.local");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String username = "username_example"; // String | 
    UpdateUsernameRequest updateUsernameRequest = new UpdateUsernameRequest(); // UpdateUsernameRequest | 
    try {
      apiInstance.updateUsername(username, updateUsernameRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#updateUsername");
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
| **username** | **String**|  | |
| **updateUsernameRequest** | [**UpdateUsernameRequest**](UpdateUsernameRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | username updated |  -  |

