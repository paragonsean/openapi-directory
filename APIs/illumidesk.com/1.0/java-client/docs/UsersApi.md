# UsersApi

All URIs are relative to *https://api.illumidesk.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**me**](UsersApi.md#me) | **GET** /v1/me | A convenience endpoint that is equivalent to GET /v1/users/profiles/&lt;my user id&gt;/ |
| [**userAvatarDelete**](UsersApi.md#userAvatarDelete) | **DELETE** /v1/users/{user}/avatar/ | Delete avatar |
| [**userAvatarGet**](UsersApi.md#userAvatarGet) | **GET** /v1/users/{user}/avatar/ | Retrieve user&#39;s avatar |
| [**userAvatarSet**](UsersApi.md#userAvatarSet) | **POST** /v1/users/{user}/avatar/ | Add user avatar |
| [**userAvatarUpdate**](UsersApi.md#userAvatarUpdate) | **PATCH** /v1/users/{user}/avatar/ | Update a project file |
| [**usersApiKeyList**](UsersApi.md#usersApiKeyList) | **GET** /v1/users/{user}/api-key/ | Retrieve account&#39;s API key |
| [**usersCreate**](UsersApi.md#usersCreate) | **POST** /v1/users/profiles/ | Create new user |
| [**usersDelete**](UsersApi.md#usersDelete) | **DELETE** /v1/users/profiles/{user}/ | Delete a user |
| [**usersEmailsCreate**](UsersApi.md#usersEmailsCreate) | **POST** /v1/users/{user}/emails/ | Create an email address |
| [**usersEmailsDelete**](UsersApi.md#usersEmailsDelete) | **DELETE** /v1/users/{user}/emails/{email_id}/ | Delete an email address |
| [**usersEmailsList**](UsersApi.md#usersEmailsList) | **GET** /v1/users/{user}/emails/ | Retrieve account email addresses |
| [**usersEmailsRead**](UsersApi.md#usersEmailsRead) | **GET** /v1/users/{user}/emails/{email_id}/ | Retrieve a user&#39;s email addresses |
| [**usersEmailsReplace**](UsersApi.md#usersEmailsReplace) | **PUT** /v1/users/{user}/emails/{email_id}/ | Replace an email address |
| [**usersEmailsUpdate**](UsersApi.md#usersEmailsUpdate) | **PATCH** /v1/users/{user}/emails/{email_id}/ | Update an email address |
| [**usersList**](UsersApi.md#usersList) | **GET** /v1/users/profiles/ | Get user list |
| [**usersRead**](UsersApi.md#usersRead) | **GET** /v1/users/profiles/{user}/ | Retrieve a user |
| [**usersSshKeyList**](UsersApi.md#usersSshKeyList) | **GET** /v1/users/{user}/ssh-key/ | Retrieve an SSH key |
| [**usersSshKeyReset**](UsersApi.md#usersSshKeyReset) | **POST** /v1/users/{user}/ssh-key/reset/ | Recreate an SSH key |
| [**usersUpdate**](UsersApi.md#usersUpdate) | **PATCH** /v1/users/profiles/{user}/ | Update a user |


<a id="me"></a>
# **me**
> User me()

A convenience endpoint that is equivalent to GET /v1/users/profiles/&lt;my user id&gt;/

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      User result = apiInstance.me();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#me");
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

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User information retrieved. |  -  |

<a id="userAvatarDelete"></a>
# **userAvatarDelete**
> userAvatarDelete(user)

Delete avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String user = "user_example"; // String | User unique identifier expressed as UUID or username.
    try {
      apiInstance.userAvatarDelete(user);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#userAvatarDelete");
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
| **user** | **String**| User unique identifier expressed as UUID or username. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Avatar deleted |  -  |
| **404** | Avatar not found |  -  |

<a id="userAvatarGet"></a>
# **userAvatarGet**
> userAvatarGet(user)

Retrieve user&#39;s avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String user = "user_example"; // String | User unique identifier expressed as UUIDor username.
    try {
      apiInstance.userAvatarGet(user);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#userAvatarGet");
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
| **user** | **String**| User unique identifier expressed as UUIDor username. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User avatar |  -  |

<a id="userAvatarSet"></a>
# **userAvatarSet**
> User userAvatarSet(user)

Add user avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String user = "user_example"; // String | User unique identifier expressed as UUID or username.
    try {
      User result = apiInstance.userAvatarSet(user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#userAvatarSet");
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
| **user** | **String**| User unique identifier expressed as UUID or username. | |

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added user avatar |  -  |
| **400** | Invalid data supplied |  -  |

<a id="userAvatarUpdate"></a>
# **userAvatarUpdate**
> User userAvatarUpdate(user)

Update a project file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String user = "user_example"; // String | User unique identifier expressed as UUID or username.
    try {
      User result = apiInstance.userAvatarUpdate(user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#userAvatarUpdate");
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
| **user** | **String**| User unique identifier expressed as UUID or username. | |

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Avatar updated. |  -  |
| **400** | Invalid data supplied. |  -  |
| **404** | Avatar not found. |  -  |

<a id="usersApiKeyList"></a>
# **usersApiKeyList**
> usersApiKeyList(user)

Retrieve account&#39;s API key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String user = "user_example"; // String | User unique identifier expressed as UUID or username.
    try {
      apiInstance.usersApiKeyList(user);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersApiKeyList");
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
| **user** | **String**| User unique identifier expressed as UUID or username. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Api Key |  -  |

<a id="usersCreate"></a>
# **usersCreate**
> User usersCreate(userData)

Create new user

Only admin users can create new users. New users have active status by default.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UserData userData = new UserData(); // UserData | 
    try {
      User result = apiInstance.usersCreate(userData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersCreate");
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
| **userData** | [**UserData**](UserData.md)|  | [optional] |

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | User created |  -  |
| **400** | Invalid data supplied |  -  |

<a id="usersDelete"></a>
# **usersDelete**
> usersDelete(user)

Delete a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String user = "user_example"; // String | User identifier expressed as UUID or username.
    try {
      apiInstance.usersDelete(user);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersDelete");
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
| **user** | **String**| User identifier expressed as UUID or username. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | User deleted. |  -  |
| **404** | User not found |  -  |

<a id="usersEmailsCreate"></a>
# **usersEmailsCreate**
> Email usersEmailsCreate(user, emailData)

Create an email address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String user = "user_example"; // String | User unique identifier expressed as UUID or username.
    EmailData emailData = new EmailData(); // EmailData | 
    try {
      Email result = apiInstance.usersEmailsCreate(user, emailData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersEmailsCreate");
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
| **user** | **String**| User unique identifier expressed as UUID or username. | |
| **emailData** | [**EmailData**](EmailData.md)|  | [optional] |

### Return type

[**Email**](Email.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Email created |  -  |
| **400** | Invalid data supplied |  -  |

<a id="usersEmailsDelete"></a>
# **usersEmailsDelete**
> usersEmailsDelete(emailId, user)

Delete an email address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String emailId = "emailId_example"; // String | Email unique identifier expressed as UUID.
    String user = "user_example"; // String | User unique identifier expressed as UUID or username.
    try {
      apiInstance.usersEmailsDelete(emailId, user);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersEmailsDelete");
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
| **emailId** | **String**| Email unique identifier expressed as UUID. | |
| **user** | **String**| User unique identifier expressed as UUID or username. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Email deleted. |  -  |
| **404** | Email not found. |  -  |

<a id="usersEmailsList"></a>
# **usersEmailsList**
> List&lt;Email&gt; usersEmailsList(user, limit, offset, ordering)

Retrieve account email addresses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String user = "user_example"; // String | User unique identifier as expressed as UUID or username.
    String limit = "limit_example"; // String | Limite when getting email list.
    String offset = "offset_example"; // String | Offset when getting email list.
    String ordering = "ordering_example"; // String | Ordering when getting email list.
    try {
      List<Email> result = apiInstance.usersEmailsList(user, limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersEmailsList");
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
| **user** | **String**| User unique identifier as expressed as UUID or username. | |
| **limit** | **String**| Limite when getting email list. | [optional] |
| **offset** | **String**| Offset when getting email list. | [optional] |
| **ordering** | **String**| Ordering when getting email list. | [optional] |

### Return type

[**List&lt;Email&gt;**](Email.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Email list |  -  |

<a id="usersEmailsRead"></a>
# **usersEmailsRead**
> Email usersEmailsRead(emailId, user)

Retrieve a user&#39;s email addresses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String emailId = "emailId_example"; // String | Email unique identifier expressed as UUID.
    String user = "user_example"; // String | User unique identifier expressed as UUID or username.
    try {
      Email result = apiInstance.usersEmailsRead(emailId, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersEmailsRead");
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
| **emailId** | **String**| Email unique identifier expressed as UUID. | |
| **user** | **String**| User unique identifier expressed as UUID or username. | |

### Return type

[**Email**](Email.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Email retrieved |  -  |
| **404** | Email not found |  -  |

<a id="usersEmailsReplace"></a>
# **usersEmailsReplace**
> Email usersEmailsReplace(emailId, user, emailData)

Replace an email address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String emailId = "emailId_example"; // String | Email unique identifier expressed as UUID.
    String user = "user_example"; // String | User unique identifier expressed as UUID or username.
    EmailData emailData = new EmailData(); // EmailData | 
    try {
      Email result = apiInstance.usersEmailsReplace(emailId, user, emailData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersEmailsReplace");
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
| **emailId** | **String**| Email unique identifier expressed as UUID. | |
| **user** | **String**| User unique identifier expressed as UUID or username. | |
| **emailData** | [**EmailData**](EmailData.md)|  | [optional] |

### Return type

[**Email**](Email.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Email updated |  -  |
| **400** | Invalid data supplied |  -  |

<a id="usersEmailsUpdate"></a>
# **usersEmailsUpdate**
> Email usersEmailsUpdate(emailId, user, emailData)

Update an email address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String emailId = "emailId_example"; // String | Email unique identifier expressed as UUID.
    String user = "user_example"; // String | User unique identifier expressed as UUID or username.
    EmailData emailData = new EmailData(); // EmailData | 
    try {
      Email result = apiInstance.usersEmailsUpdate(emailId, user, emailData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersEmailsUpdate");
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
| **emailId** | **String**| Email unique identifier expressed as UUID. | |
| **user** | **String**| User unique identifier expressed as UUID or username. | |
| **emailData** | [**EmailData**](EmailData.md)|  | [optional] |

### Return type

[**Email**](Email.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Email updated |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Email not found |  -  |

<a id="usersList"></a>
# **usersList**
> List&lt;User&gt; usersList(limit, offset, username, email, ordering)

Get user list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String limit = "limit_example"; // String | Limit user list.
    String offset = "offset_example"; // String | Offset when getting users.
    String username = "username_example"; // String | User username.
    String email = "email_example"; // String | User email.
    String ordering = "ordering_example"; // String | Ordering when getting users.
    try {
      List<User> result = apiInstance.usersList(limit, offset, username, email, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersList");
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
| **limit** | **String**| Limit user list. | [optional] |
| **offset** | **String**| Offset when getting users. | [optional] |
| **username** | **String**| User username. | [optional] |
| **email** | **String**| User email. | [optional] |
| **ordering** | **String**| Ordering when getting users. | [optional] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User list |  -  |

<a id="usersRead"></a>
# **usersRead**
> User usersRead(user)

Retrieve a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String user = "user_example"; // String | Unique identifier expressed as UUID or username.
    try {
      User result = apiInstance.usersRead(user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersRead");
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
| **user** | **String**| Unique identifier expressed as UUID or username. | |

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User retrieved. |  -  |
| **404** | User not found. |  -  |

<a id="usersSshKeyList"></a>
# **usersSshKeyList**
> usersSshKeyList(user)

Retrieve an SSH key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String user = "user_example"; // String | User unique identifier expressed as UUID or username.
    try {
      apiInstance.usersSshKeyList(user);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersSshKeyList");
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
| **user** | **String**| User unique identifier expressed as UUID or username. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SSH Key. |  -  |

<a id="usersSshKeyReset"></a>
# **usersSshKeyReset**
> usersSshKeyReset(user)

Recreate an SSH key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String user = "user_example"; // String | User unique identifier expressed as UUID or username.
    try {
      apiInstance.usersSshKeyReset(user);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersSshKeyReset");
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
| **user** | **String**| User unique identifier expressed as UUID or username. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Reset SSH Key successfully. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="usersUpdate"></a>
# **usersUpdate**
> User usersUpdate(user, userData)

Update a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String user = "user_example"; // String | User unique identifier expressed as UUID or username.
    UserData userData = new UserData(); // UserData | 
    try {
      User result = apiInstance.usersUpdate(user, userData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUpdate");
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
| **user** | **String**| User unique identifier expressed as UUID or username. | |
| **userData** | [**UserData**](UserData.md)|  | [optional] |

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User updated. |  -  |
| **400** | Invalid data supplied. |  -  |
| **404** | User not found. |  -  |

