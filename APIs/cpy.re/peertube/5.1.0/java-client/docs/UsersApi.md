# UsersApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addUser**](UsersApi.md#addUser) | **POST** /api/v1/users | Create a user |
| [**confirmTwoFactorRequest**](UsersApi.md#confirmTwoFactorRequest) | **POST** /api/v1/users/{id}/two-factor/confirm-request | Confirm two factor auth |
| [**delUser**](UsersApi.md#delUser) | **DELETE** /api/v1/users/{id} | Delete a user |
| [**disableTwoFactor**](UsersApi.md#disableTwoFactor) | **POST** /api/v1/users/{id}/two-factor/disable | Disable two factor auth |
| [**getUser**](UsersApi.md#getUser) | **GET** /api/v1/users/{id} | Get a user |
| [**getUsers**](UsersApi.md#getUsers) | **GET** /api/v1/users | List users |
| [**putUser**](UsersApi.md#putUser) | **PUT** /api/v1/users/{id} | Update a user |
| [**requestTwoFactor**](UsersApi.md#requestTwoFactor) | **POST** /api/v1/users/{id}/two-factor/request | Request two factor auth |
| [**resendEmailToVerifyUser**](UsersApi.md#resendEmailToVerifyUser) | **POST** /api/v1/users/ask-send-verify-email | Resend user verification link |
| [**verifyUser**](UsersApi.md#verifyUser) | **POST** /api/v1/users/{id}/verify-email | Verify a user |


<a id="addUser"></a>
# **addUser**
> AddUserResponse addUser(addUser)

Create a user

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
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    AddUser addUser = new AddUser(); // AddUser | If the smtp server is configured, you can leave the password empty and an email will be sent asking the user to set it first. 
    try {
      AddUserResponse result = apiInstance.addUser(addUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#addUser");
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
| **addUser** | [**AddUser**](AddUser.md)| If the smtp server is configured, you can leave the password empty and an email will be sent asking the user to set it first.  | |

### Return type

[**AddUserResponse**](AddUserResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user created |  -  |
| **403** | insufficient authority to create an admin or moderator |  -  |

<a id="confirmTwoFactorRequest"></a>
# **confirmTwoFactorRequest**
> confirmTwoFactorRequest(id, confirmTwoFactorRequestRequest)

Confirm two factor auth

Confirm a two factor authentication request

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
    defaultClient.setBasePath("https://peertube2.cpy.re");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | Entity id
    ConfirmTwoFactorRequestRequest confirmTwoFactorRequestRequest = new ConfirmTwoFactorRequestRequest(); // ConfirmTwoFactorRequestRequest | 
    try {
      apiInstance.confirmTwoFactorRequest(id, confirmTwoFactorRequestRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#confirmTwoFactorRequest");
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
| **id** | **Integer**| Entity id | |
| **confirmTwoFactorRequestRequest** | [**ConfirmTwoFactorRequestRequest**](ConfirmTwoFactorRequestRequest.md)|  | [optional] |

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
| **204** | successful operation |  -  |
| **403** | invalid request token or OTP token |  -  |
| **404** | user not found |  -  |

<a id="delUser"></a>
# **delUser**
> delUser(id)

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
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | Entity id
    try {
      apiInstance.delUser(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#delUser");
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
| **id** | **Integer**| Entity id | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="disableTwoFactor"></a>
# **disableTwoFactor**
> disableTwoFactor(id, disableTwoFactorRequest)

Disable two factor auth

Disable two factor authentication of a user

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
    defaultClient.setBasePath("https://peertube2.cpy.re");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | Entity id
    DisableTwoFactorRequest disableTwoFactorRequest = new DisableTwoFactorRequest(); // DisableTwoFactorRequest | 
    try {
      apiInstance.disableTwoFactor(id, disableTwoFactorRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#disableTwoFactor");
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
| **id** | **Integer**| Entity id | |
| **disableTwoFactorRequest** | [**DisableTwoFactorRequest**](DisableTwoFactorRequest.md)|  | [optional] |

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
| **204** | successful operation |  -  |
| **403** | invalid password |  -  |
| **404** | user not found |  -  |

<a id="getUser"></a>
# **getUser**
> GetUser200Response getUser(id, withStats)

Get a user

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
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | Entity id
    Boolean withStats = true; // Boolean | include statistics about the user (only available as a moderator/admin)
    try {
      GetUser200Response result = apiInstance.getUser(id, withStats);
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
| **id** | **Integer**| Entity id | |
| **withStats** | **Boolean**| include statistics about the user (only available as a moderator/admin) | [optional] |

### Return type

[**GetUser200Response**](GetUser200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | As an admin/moderator, you can request a response augmented with statistics about the user&#39;s moderation relations and videos usage, by using the &#x60;withStats&#x60; parameter.  |  -  |

<a id="getUsers"></a>
# **getUsers**
> List&lt;User&gt; getUsers(search, blocked, start, count, sort)

List users

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
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String search = "search_example"; // String | Plain text search that will match with user usernames or emails
    Boolean blocked = true; // Boolean | Filter results down to (un)banned users
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-id"; // String | Sort users by criteria
    try {
      List<User> result = apiInstance.getUsers(search, blocked, start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUsers");
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
| **search** | **String**| Plain text search that will match with user usernames or emails | [optional] |
| **blocked** | **Boolean**| Filter results down to (un)banned users | [optional] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort users by criteria | [optional] [enum: -id, -username, -createdAt] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="putUser"></a>
# **putUser**
> putUser(id, updateUser)

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
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | Entity id
    UpdateUser updateUser = new UpdateUser(); // UpdateUser | 
    try {
      apiInstance.putUser(id, updateUser);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#putUser");
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
| **id** | **Integer**| Entity id | |
| **updateUser** | [**UpdateUser**](UpdateUser.md)|  | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="requestTwoFactor"></a>
# **requestTwoFactor**
> List&lt;RequestTwoFactorResponse&gt; requestTwoFactor(id, disableTwoFactorRequest)

Request two factor auth

Request two factor authentication for a user

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
    defaultClient.setBasePath("https://peertube2.cpy.re");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | Entity id
    DisableTwoFactorRequest disableTwoFactorRequest = new DisableTwoFactorRequest(); // DisableTwoFactorRequest | 
    try {
      List<RequestTwoFactorResponse> result = apiInstance.requestTwoFactor(id, disableTwoFactorRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#requestTwoFactor");
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
| **id** | **Integer**| Entity id | |
| **disableTwoFactorRequest** | [**DisableTwoFactorRequest**](DisableTwoFactorRequest.md)|  | [optional] |

### Return type

[**List&lt;RequestTwoFactorResponse&gt;**](RequestTwoFactorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **403** | invalid password |  -  |
| **404** | user not found |  -  |

<a id="resendEmailToVerifyUser"></a>
# **resendEmailToVerifyUser**
> resendEmailToVerifyUser(resendEmailToVerifyUserRequest)

Resend user verification link

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
    defaultClient.setBasePath("https://peertube2.cpy.re");

    UsersApi apiInstance = new UsersApi(defaultClient);
    ResendEmailToVerifyUserRequest resendEmailToVerifyUserRequest = new ResendEmailToVerifyUserRequest(); // ResendEmailToVerifyUserRequest | 
    try {
      apiInstance.resendEmailToVerifyUser(resendEmailToVerifyUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#resendEmailToVerifyUser");
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
| **resendEmailToVerifyUserRequest** | [**ResendEmailToVerifyUserRequest**](ResendEmailToVerifyUserRequest.md)|  | [optional] |

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
| **204** | successful operation |  -  |

<a id="verifyUser"></a>
# **verifyUser**
> verifyUser(id, verifyUserRequest)

Verify a user

Following a user registration, the new user will receive an email asking to click a link containing a secret. This endpoint can also be used to verify a new email set in the user account. 

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
    defaultClient.setBasePath("https://peertube2.cpy.re");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | Entity id
    VerifyUserRequest verifyUserRequest = new VerifyUserRequest(); // VerifyUserRequest | 
    try {
      apiInstance.verifyUser(id, verifyUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#verifyUser");
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
| **id** | **Integer**| Entity id | |
| **verifyUserRequest** | [**VerifyUserRequest**](VerifyUserRequest.md)|  | [optional] |

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
| **204** | successful operation |  -  |
| **403** | invalid verification string |  -  |
| **404** | user not found |  -  |

