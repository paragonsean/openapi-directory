# UsersApi

All URIs are relative to *http://whatsapp.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUser**](UsersApi.md#createUser) | **POST** /users | Create-User |
| [**deleteUser**](UsersApi.md#deleteUser) | **DELETE** /users/{UserUsername} | Delete-User |
| [**getUser**](UsersApi.md#getUser) | **GET** /users/{UserUsername} | Get-User |
| [**loginUser**](UsersApi.md#loginUser) | **POST** /users/login | Login-User |
| [**logoutUser**](UsersApi.md#logoutUser) | **POST** /users/logout | Logout-User |
| [**updateUser**](UsersApi.md#updateUser) | **PUT** /users/{UserUsername} | Update-User |


<a id="createUser"></a>
# **createUser**
> UserResponse createUser(createUserRequestBody)

Create-User

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
    defaultClient.setBasePath("http://whatsapp.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    CreateUserRequestBody createUserRequestBody = new CreateUserRequestBody(); // CreateUserRequestBody | 
    try {
      UserResponse result = apiInstance.createUser(createUserRequestBody);
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
| **createUserRequestBody** | [**CreateUserRequestBody**](CreateUserRequestBody.md)|  | |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="deleteUser"></a>
# **deleteUser**
> UserResponse deleteUser(userUsername)

Delete-User

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
    defaultClient.setBasePath("http://whatsapp.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userUsername = "userUsername_example"; // String | 
    try {
      UserResponse result = apiInstance.deleteUser(userUsername);
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
| **userUsername** | **String**|  | |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getUser"></a>
# **getUser**
> DetailedUserResponse getUser(userUsername)

Get-User

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
    defaultClient.setBasePath("http://whatsapp.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userUsername = "userUsername_example"; // String | 
    try {
      DetailedUserResponse result = apiInstance.getUser(userUsername);
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
| **userUsername** | **String**|  | |

### Return type

[**DetailedUserResponse**](DetailedUserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="loginUser"></a>
# **loginUser**
> UserLoginResponse loginUser(loginAdminRequestBody)

Login-User

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
    defaultClient.setBasePath("http://whatsapp.local");
    
    // Configure HTTP basic authorization: httpBasic
    HttpBasicAuth httpBasic = (HttpBasicAuth) defaultClient.getAuthentication("httpBasic");
    httpBasic.setUsername("YOUR USERNAME");
    httpBasic.setPassword("YOUR PASSWORD");

    UsersApi apiInstance = new UsersApi(defaultClient);
    LoginAdminRequestBody loginAdminRequestBody = new LoginAdminRequestBody(); // LoginAdminRequestBody | 
    try {
      UserLoginResponse result = apiInstance.loginUser(loginAdminRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#loginUser");
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
| **loginAdminRequestBody** | [**LoginAdminRequestBody**](LoginAdminRequestBody.md)|  | [optional] |

### Return type

[**UserLoginResponse**](UserLoginResponse.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="logoutUser"></a>
# **logoutUser**
> logoutUser()

Logout-User

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
    defaultClient.setBasePath("http://whatsapp.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      apiInstance.logoutUser();
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#logoutUser");
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

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updateUser"></a>
# **updateUser**
> UserResponse updateUser(userUsername, updateUserRequestBody)

Update-User

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
    defaultClient.setBasePath("http://whatsapp.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userUsername = "userUsername_example"; // String | 
    UpdateUserRequestBody updateUserRequestBody = new UpdateUserRequestBody(); // UpdateUserRequestBody | 
    try {
      UserResponse result = apiInstance.updateUser(userUsername, updateUserRequestBody);
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
| **userUsername** | **String**|  | |
| **updateUserRequestBody** | [**UpdateUserRequestBody**](UpdateUserRequestBody.md)|  | |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

