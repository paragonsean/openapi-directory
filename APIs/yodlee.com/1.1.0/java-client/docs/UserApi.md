# UserApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAccessTokens**](UserApi.md#getAccessTokens) | **GET** /user/accessTokens | Get Access Tokens |
| [**getUser**](UserApi.md#getUser) | **GET** /user | Get User Details |
| [**registerUser**](UserApi.md#registerUser) | **POST** /user/register | Register User |
| [**samlLogin**](UserApi.md#samlLogin) | **POST** /user/samlLogin | Saml Login |
| [**unregister**](UserApi.md#unregister) | **DELETE** /user/unregister | Delete User |
| [**updateUser**](UserApi.md#updateUser) | **PUT** /user | Update User Details |
| [**userLogout**](UserApi.md#userLogout) | **POST** /user/logout | User Logout |


<a id="getAccessTokens"></a>
# **getAccessTokens**
> UserAccessTokensResponse getAccessTokens(appIds)

Get Access Tokens

The Get Access Tokens service is used to retrieve the access tokens for the application id(s) provided.&lt;br&gt;URL in the response can be used to launch the application for which token is requested.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;This endpoint is deprecated for customers using the API Key-based authentication and is applicable only to customers who use the SAML-based authentication.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserApi apiInstance = new UserApi(defaultClient);
    String appIds = "appIds_example"; // String | appIds
    try {
      UserAccessTokensResponse result = apiInstance.getAccessTokens(appIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getAccessTokens");
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
| **appIds** | **String**| appIds | |

### Return type

[**UserAccessTokensResponse**](UserAccessTokensResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getUser"></a>
# **getUser**
> UserDetailResponse getUser()

Get User Details

The get user details service is used to get the user profile information and the application preferences set at the time of user registration.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserApi apiInstance = new UserApi(defaultClient);
    try {
      UserDetailResponse result = apiInstance.getUser();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUser");
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

[**UserDetailResponse**](UserDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="registerUser"></a>
# **registerUser**
> UserResponse registerUser(userRequest)

Register User

The register user service is used to register a user in Yodlee.&lt;br&gt;The loginName cannot include spaces and must be between 3 and 150 characters.&lt;br&gt;locale passed must be one of the supported locales for the customer. &lt;br&gt;Currency provided in the input will be respected in the derived services and the amount fields in the response will be provided in the preferred currency.&lt;br&gt;userParam is accepted as a body parameter. &lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;The content type has to be passed as application/json for the body parameter.&lt;/li&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserApi apiInstance = new UserApi(defaultClient);
    UserRequest userRequest = new UserRequest(); // UserRequest | userRequest
    try {
      UserResponse result = apiInstance.registerUser(userRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#registerUser");
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
| **userRequest** | [**UserRequest**](UserRequest.md)| userRequest | |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Login Successful |  -  |
| **400** | Y800 : Invalid value for loginName&lt;br&gt;Y800 : Invalid value for email&lt;br&gt;Y801 : Invalid length for loginName&lt;br&gt; |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="samlLogin"></a>
# **samlLogin**
> UserResponse samlLogin(issuer, samlResponse, source)

Saml Login

The SAML login service is used to authenticate system users with a SAML response.&lt;br&gt;A new user will be created with the input provided if that user isn&#39;t already in the system.&lt;br&gt;For existing users, the system will make updates based on changes or new information.&lt;br&gt;When authentication is successful, a user session token is returned.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;The content type has to be passed as application/x-www-form-urlencoded. &lt;li&gt;issuer, source and samlResponse should be passed as body parameters.&lt;/li&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserApi apiInstance = new UserApi(defaultClient);
    String issuer = "issuer_example"; // String | issuer
    String samlResponse = "samlResponse_example"; // String | samlResponse
    String source = "source_example"; // String | source
    try {
      UserResponse result = apiInstance.samlLogin(issuer, samlResponse, source);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#samlLogin");
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
| **issuer** | **String**| issuer | |
| **samlResponse** | **String**| samlResponse | |
| **source** | **String**| source | [optional] |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y013 : Invalid value for samlResponse&lt;br&gt;Y013 : Invalid value for issuer |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="unregister"></a>
# **unregister**
> unregister()

Delete User

The delete user service is used to delete or unregister a user from Yodlee. &lt;br&gt;Once deleted, the information related to the users cannot be retrieved. &lt;br&gt;The HTTP response code is 204 (Success without content)&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserApi apiInstance = new UserApi(defaultClient);
    try {
      apiInstance.unregister();
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#unregister");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="updateUser"></a>
# **updateUser**
> updateUser(updateUserRequest)

Update User Details

The update user details service is used to update user details like name, address, currency preference, etc.&lt;br&gt;Currency provided in the input will be respected in the &lt;a href&#x3D;\&quot;https://developer.yodlee.com/api-reference#tag/Derived\&quot;&gt;derived&lt;/a&gt; services and the amount fields in the response will be provided in the preferred currency.&lt;br&gt;The HTTP response code is 204 (Success without content). &lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserApi apiInstance = new UserApi(defaultClient);
    UpdateUserRequest updateUserRequest = new UpdateUserRequest(); // UpdateUserRequest | userRequest
    try {
      apiInstance.updateUser(updateUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#updateUser");
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
| **updateUserRequest** | [**UpdateUserRequest**](UpdateUserRequest.md)| userRequest | |

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
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="userLogout"></a>
# **userLogout**
> userLogout()

User Logout

&lt;b&gt;Deprecated&lt;/b&gt;: This endpoint is deprecated for API Key-based authentication. The user logout service allows the user to log out of the application.&lt;br&gt;The service does not return a response body. The HTTP response code is 204 (Success with no content).&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserApi apiInstance = new UserApi(defaultClient);
    try {
      apiInstance.userLogout();
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userLogout");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Logout successful |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

