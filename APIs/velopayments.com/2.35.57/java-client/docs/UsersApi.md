# UsersApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteUserByIdV2**](UsersApi.md#deleteUserByIdV2) | **DELETE** /v2/users/{userId} | Delete a User |
| [**disableUserV2**](UsersApi.md#disableUserV2) | **POST** /v2/users/{userId}/disable | Disable a User |
| [**enableUserV2**](UsersApi.md#enableUserV2) | **POST** /v2/users/{userId}/enable | Enable a User |
| [**getSelf**](UsersApi.md#getSelf) | **GET** /v2/users/self | Get Self |
| [**getUserByIdV2**](UsersApi.md#getUserByIdV2) | **GET** /v2/users/{userId} | Get User |
| [**inviteUser**](UsersApi.md#inviteUser) | **POST** /v2/users/invite | Invite a User |
| [**listUsers**](UsersApi.md#listUsers) | **GET** /v2/users | List Users |
| [**registerSms**](UsersApi.md#registerSms) | **POST** /v2/users/registration/sms | Register SMS Number |
| [**resendToken_0**](UsersApi.md#resendToken_0) | **POST** /v2/users/{userId}/tokens | Resend a token |
| [**roleUpdate**](UsersApi.md#roleUpdate) | **POST** /v2/users/{userId}/roleUpdate | Update User Role |
| [**unlockUserV2**](UsersApi.md#unlockUserV2) | **POST** /v2/users/{userId}/unlock | Unlock a User |
| [**unregisterMFA**](UsersApi.md#unregisterMFA) | **POST** /v2/users/{userId}/mfa/unregister | Unregister MFA for the user |
| [**unregisterMFAForSelf**](UsersApi.md#unregisterMFAForSelf) | **POST** /v2/users/self/mfa/unregister | Unregister MFA for Self |
| [**updatePasswordSelf**](UsersApi.md#updatePasswordSelf) | **POST** /v2/users/self/password | Update Password for self |
| [**userDetailsUpdate**](UsersApi.md#userDetailsUpdate) | **POST** /v2/users/{userId}/userDetailsUpdate | Update User Details |
| [**userDetailsUpdateForSelf**](UsersApi.md#userDetailsUpdateForSelf) | **POST** /v2/users/self/userDetailsUpdate | Update User Details for self |
| [**validatePasswordSelf**](UsersApi.md#validatePasswordSelf) | **POST** /v2/users/self/password/validate | Validate the proposed password |


<a id="deleteUserByIdV2"></a>
# **deleteUserByIdV2**
> deleteUserByIdV2(userId)

Delete a User

Delete User by Id. 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UUID userId = UUID.randomUUID(); // UUID | The UUID of the User.
    try {
      apiInstance.deleteUserByIdV2(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#deleteUserByIdV2");
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
| **userId** | **UUID**| The UUID of the User. | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | request completed okay |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="disableUserV2"></a>
# **disableUserV2**
> disableUserV2(userId)

Disable a User

&lt;p&gt;If a user is enabled this endpoint will disable them &lt;/p&gt; &lt;p&gt;The invoker must have the appropriate permission &lt;/p&gt; &lt;p&gt;A user cannot disable themself &lt;/p&gt; &lt;p&gt;When a user is disabled any active access tokens will be revoked and the user will not be able to log in&lt;/p&gt; 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UUID userId = UUID.randomUUID(); // UUID | The UUID of the User.
    try {
      apiInstance.disableUserV2(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#disableUserV2");
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
| **userId** | **UUID**| The UUID of the User. | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success the user was disabled or was already disabled |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="enableUserV2"></a>
# **enableUserV2**
> enableUserV2(userId)

Enable a User

&lt;p&gt;If a user has been disabled this endpoints will enable them &lt;/p&gt; &lt;p&gt;The invoker must have the appropriate permission &lt;/p&gt; &lt;p&gt;A user cannot enable themself &lt;/p&gt; &lt;p&gt;If the user is a payor user and the payor is disabled this operation is not allowed&lt;/p&gt; &lt;p&gt;If enabling a payor user would breach the limit for master admin payor users the request will be rejected &lt;/p&gt; 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UUID userId = UUID.randomUUID(); // UUID | The UUID of the User.
    try {
      apiInstance.enableUserV2(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#enableUserV2");
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
| **userId** | **UUID**| The UUID of the User. | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success the user was enabled or was already enabled |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="getSelf"></a>
# **getSelf**
> UserResponse getSelf()

Get Self

Get the user&#39;s details 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      UserResponse result = apiInstance.getSelf();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getSelf");
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

[**UserResponse**](UserResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get User Details |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

<a id="getUserByIdV2"></a>
# **getUserByIdV2**
> UserResponse getUserByIdV2(userId)

Get User

Get a Single User by Id. 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UUID userId = UUID.randomUUID(); // UUID | The UUID of the User.
    try {
      UserResponse result = apiInstance.getUserByIdV2(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserByIdV2");
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
| **userId** | **UUID**| The UUID of the User. | |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get User Details |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="inviteUser"></a>
# **inviteUser**
> inviteUser(inviteUserRequest)

Invite a User

Create a User and invite them to the system 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    InviteUserRequest inviteUserRequest = new InviteUserRequest(); // InviteUserRequest | Details of User to invite
    try {
      apiInstance.inviteUser(inviteUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#inviteUser");
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
| **inviteUserRequest** | [**InviteUserRequest**](InviteUserRequest.md)| Details of User to invite | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. The user was invited successfully |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **409** | The request contained data that would result in a duplicate value  |  -  |
| **412** | The request could not be completed as a precondition was not met  |  -  |

<a id="listUsers"></a>
# **listUsers**
> PagedUserResponse listUsers(type, status, entityId, payeeType, page, pageSize, sort)

List Users

Get a paginated response listing the Users

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UserType type = UserType.fromValue("BACKOFFICE"); // UserType | The Type of the User.
    UserStatus status = UserStatus.fromValue("ENABLED"); // UserStatus | The status of the User.
    UUID entityId = UUID.randomUUID(); // UUID | The entityId of the User.
    PayeeType payeeType = PayeeType.fromValue("COMPANY"); // PayeeType | The Type of the Payee entity. Either COMPANY or INDIVIDUAL.
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | The number of results to return in a page
    String sort = "email:asc"; // String | List of sort fields (e.g. ?sort=email:asc,lastName:asc) Default is email:asc 'name' The supported sort fields are - email, lastNmae. 
    try {
      PagedUserResponse result = apiInstance.listUsers(type, status, entityId, payeeType, page, pageSize, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#listUsers");
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
| **type** | [**UserType**](.md)| The Type of the User. | [optional] [enum: BACKOFFICE, PAYOR, PAYEE] |
| **status** | [**UserStatus**](.md)| The status of the User. | [optional] [enum: ENABLED, DISABLED, PENDING] |
| **entityId** | **UUID**| The entityId of the User. | [optional] |
| **payeeType** | [**PayeeType**](.md)| The Type of the Payee entity. Either COMPANY or INDIVIDUAL. | [optional] [enum: COMPANY, INDIVIDUAL] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 25] |
| **sort** | **String**| List of sort fields (e.g. ?sort&#x3D;email:asc,lastName:asc) Default is email:asc &#39;name&#39; The supported sort fields are - email, lastNmae.  | [optional] [default to email:asc] |

### Return type

[**PagedUserResponse**](PagedUserResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated list of Users filtered by query parameters |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

<a id="registerSms"></a>
# **registerSms**
> registerSms(registerSmsRequest)

Register SMS Number

&lt;p&gt;Register an Sms number and send an OTP to it &lt;/p&gt; &lt;p&gt;Used for manual verification of a user &lt;/p&gt; &lt;p&gt;The backoffice user initiates the request to send the OTP to the user&#39;s sms &lt;/p&gt; &lt;p&gt;The user then reads back the OTP which the backoffice user enters in the verifactionCode property for requests that require it&lt;/p&gt; 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    RegisterSmsRequest registerSmsRequest = new RegisterSmsRequest(); // RegisterSmsRequest | a SMS Number to send an OTP to
    try {
      apiInstance.registerSms(registerSmsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#registerSms");
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
| **registerSmsRequest** | [**RegisterSmsRequest**](RegisterSmsRequest.md)| a SMS Number to send an OTP to | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | request completed okay |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

<a id="resendToken_0"></a>
# **resendToken_0**
> resendToken_0(userId, resendTokenRequest)

Resend a token

&lt;p&gt;Resend the specified token &lt;/p&gt; &lt;p&gt;The token to resend must already exist for the user &lt;/p&gt; &lt;p&gt;It will be revoked and a new one issued&lt;/p&gt; 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UUID userId = UUID.randomUUID(); // UUID | The UUID of the User.
    ResendTokenRequest resendTokenRequest = new ResendTokenRequest(); // ResendTokenRequest | The type of token to resend
    try {
      apiInstance.resendToken_0(userId, resendTokenRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#resendToken_0");
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
| **userId** | **UUID**| The UUID of the User. | |
| **resendTokenRequest** | [**ResendTokenRequest**](ResendTokenRequest.md)| The type of token to resend | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | request completed okay |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

<a id="roleUpdate"></a>
# **roleUpdate**
> roleUpdate(userId, roleUpdateRequest)

Update User Role

&lt;p&gt;Update the user&#39;s Role&lt;/p&gt; 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UUID userId = UUID.randomUUID(); // UUID | The UUID of the User.
    RoleUpdateRequest roleUpdateRequest = new RoleUpdateRequest(); // RoleUpdateRequest | The Role to change to
    try {
      apiInstance.roleUpdate(userId, roleUpdateRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#roleUpdate");
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
| **userId** | **UUID**| The UUID of the User. | |
| **roleUpdateRequest** | [**RoleUpdateRequest**](RoleUpdateRequest.md)| The Role to change to | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | request completed okay |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="unlockUserV2"></a>
# **unlockUserV2**
> unlockUserV2(userId)

Unlock a User

If a user is locked this endpoint will unlock them 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UUID userId = UUID.randomUUID(); // UUID | The UUID of the User.
    try {
      apiInstance.unlockUserV2(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#unlockUserV2");
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
| **userId** | **UUID**| The UUID of the User. | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success the user was unlocked or was already unlocked |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="unregisterMFA"></a>
# **unregisterMFA**
> unregisterMFA(userId, unregisterMFARequest)

Unregister MFA for the user

&lt;p&gt;Unregister the MFA device for the user &lt;/p&gt; &lt;p&gt;If the user does not require further verification then a register new MFA device token will be sent to them via their email address&lt;/p&gt; 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UUID userId = UUID.randomUUID(); // UUID | The UUID of the User.
    UnregisterMFARequest unregisterMFARequest = new UnregisterMFARequest(); // UnregisterMFARequest | The MFA Type to unregister
    try {
      apiInstance.unregisterMFA(userId, unregisterMFARequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#unregisterMFA");
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
| **userId** | **UUID**| The UUID of the User. | |
| **unregisterMFARequest** | [**UnregisterMFARequest**](UnregisterMFARequest.md)| The MFA Type to unregister | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | the MFA Type to unregister |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="unregisterMFAForSelf"></a>
# **unregisterMFAForSelf**
> unregisterMFAForSelf(selfMFATypeUnregisterRequest, authorization)

Unregister MFA for Self

&lt;p&gt;Unregister the MFA device for the user &lt;/p&gt; &lt;p&gt;If the user does not require further verification then a register new MFA device token will be sent to them via their email address&lt;/p&gt; 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    SelfMFATypeUnregisterRequest selfMFATypeUnregisterRequest = new SelfMFATypeUnregisterRequest(); // SelfMFATypeUnregisterRequest | The MFA Type to unregister
    String authorization = "authorization_example"; // String | Bearer token authorization leg of validate
    try {
      apiInstance.unregisterMFAForSelf(selfMFATypeUnregisterRequest, authorization);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#unregisterMFAForSelf");
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
| **selfMFATypeUnregisterRequest** | [**SelfMFATypeUnregisterRequest**](SelfMFATypeUnregisterRequest.md)| The MFA Type to unregister | |
| **authorization** | **String**| Bearer token authorization leg of validate | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | the MFA Type to unregister |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

<a id="updatePasswordSelf"></a>
# **updatePasswordSelf**
> updatePasswordSelf(selfUpdatePasswordRequest)

Update Password for self

Update password for self 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    SelfUpdatePasswordRequest selfUpdatePasswordRequest = new SelfUpdatePasswordRequest(); // SelfUpdatePasswordRequest | The password
    try {
      apiInstance.updatePasswordSelf(selfUpdatePasswordRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#updatePasswordSelf");
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
| **selfUpdatePasswordRequest** | [**SelfUpdatePasswordRequest**](SelfUpdatePasswordRequest.md)| The password | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | the password was submitted and accepted |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

<a id="userDetailsUpdate"></a>
# **userDetailsUpdate**
> userDetailsUpdate(userId, userDetailsUpdateRequest)

Update User Details

&lt;p&gt;Update the profile details for the given user&lt;/p&gt; &lt;p&gt;When updating Payor users with the role of payor.master_admin a verificationCode is required&lt;/p&gt; 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UUID userId = UUID.randomUUID(); // UUID | The UUID of the User.
    UserDetailsUpdateRequest userDetailsUpdateRequest = new UserDetailsUpdateRequest(); // UserDetailsUpdateRequest | The details of the user to update
    try {
      apiInstance.userDetailsUpdate(userId, userDetailsUpdateRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#userDetailsUpdate");
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
| **userId** | **UUID**| The UUID of the User. | |
| **userDetailsUpdateRequest** | [**UserDetailsUpdateRequest**](UserDetailsUpdateRequest.md)| The details of the user to update | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | request completed okay |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |
| **409** | The request contained data that would result in a duplicate value  |  -  |

<a id="userDetailsUpdateForSelf"></a>
# **userDetailsUpdateForSelf**
> userDetailsUpdateForSelf(payeeUserSelfUpdateRequest)

Update User Details for self

&lt;p&gt;Update the profile details for the given user&lt;/p&gt; &lt;p&gt;Only Payee user types are supported&lt;/p&gt; 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    PayeeUserSelfUpdateRequest payeeUserSelfUpdateRequest = new PayeeUserSelfUpdateRequest(); // PayeeUserSelfUpdateRequest | The details of the user to update
    try {
      apiInstance.userDetailsUpdateForSelf(payeeUserSelfUpdateRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#userDetailsUpdateForSelf");
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
| **payeeUserSelfUpdateRequest** | [**PayeeUserSelfUpdateRequest**](PayeeUserSelfUpdateRequest.md)| The details of the user to update | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | request completed okay |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **409** | The request contained data that would result in a duplicate value  |  -  |

<a id="validatePasswordSelf"></a>
# **validatePasswordSelf**
> ValidatePasswordResponse validatePasswordSelf(passwordRequest)

Validate the proposed password

validate the password and return a score 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    PasswordRequest passwordRequest = new PasswordRequest(); // PasswordRequest | The password
    try {
      ValidatePasswordResponse result = apiInstance.validatePasswordSelf(passwordRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#validatePasswordSelf");
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
| **passwordRequest** | [**PasswordRequest**](PasswordRequest.md)| The password | |

### Return type

[**ValidatePasswordResponse**](ValidatePasswordResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the password was checked and a score returned |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

