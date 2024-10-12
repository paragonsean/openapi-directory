# UsersInIQualifyApi

All URIs are relative to *https://api.iqualify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersPost**](UsersInIQualifyApi.md#usersPost) | **POST** /users | Add new user |
| [**usersUserEmailGet**](UsersInIQualifyApi.md#usersUserEmailGet) | **GET** /users/{userEmail} | Find user by email |
| [**usersUserEmailInviteEmailPost**](UsersInIQualifyApi.md#usersUserEmailInviteEmailPost) | **POST** /users/{userEmail}/invite-email | Resend invitation email |
| [**usersUserEmailOfferingsGet**](UsersInIQualifyApi.md#usersUserEmailOfferingsGet) | **GET** /users/{userEmail}/offerings | Find user&#39;s offerings |
| [**usersUserEmailOfferingsPost**](UsersInIQualifyApi.md#usersUserEmailOfferingsPost) | **POST** /users/{userEmail}/offerings | Adds the user to the specified offerings as a learner |
| [**usersUserEmailPatch**](UsersInIQualifyApi.md#usersUserEmailPatch) | **PATCH** /users/{userEmail} | Update user |
| [**usersUserEmailPermissionsPermissionNamePost**](UsersInIQualifyApi.md#usersUserEmailPermissionsPermissionNamePost) | **POST** /users/{userEmail}/permissions/{permissionName} | Add permission to user |
| [**usersUserEmailSuspendPut**](UsersInIQualifyApi.md#usersUserEmailSuspendPut) | **PUT** /users/{userEmail}/suspend | Suspend user |


<a id="usersPost"></a>
# **usersPost**
> UserResponse usersPost(user)

Add new user

Creates a new user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersInIQualifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    UsersInIQualifyApi apiInstance = new UsersInIQualifyApi(defaultClient);
    User user = new User(); // User | user
    try {
      UserResponse result = apiInstance.usersPost(user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersInIQualifyApi#usersPost");
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
| **user** | [**User**](User.md)| user | |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | user added |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="usersUserEmailGet"></a>
# **usersUserEmailGet**
> UserResponse usersUserEmailGet(userEmail)

Find user by email

Responds with a user matching the specified email.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersInIQualifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    UsersInIQualifyApi apiInstance = new UsersInIQualifyApi(defaultClient);
    String userEmail = "userEmail_example"; // String | user's email
    try {
      UserResponse result = apiInstance.usersUserEmailGet(userEmail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersInIQualifyApi#usersUserEmailGet");
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
| **userEmail** | **String**| user&#39;s email | |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user data |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="usersUserEmailInviteEmailPost"></a>
# **usersUserEmailInviteEmailPost**
> usersUserEmailInviteEmailPost(userEmail)

Resend invitation email

Re-sends an invitation e-mail to the specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersInIQualifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    UsersInIQualifyApi apiInstance = new UsersInIQualifyApi(defaultClient);
    String userEmail = "userEmail_example"; // String | user's email
    try {
      apiInstance.usersUserEmailInviteEmailPost(userEmail);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersInIQualifyApi#usersUserEmailInviteEmailPost");
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
| **userEmail** | **String**| user&#39;s email | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successfully requested invitation e-mail sending |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="usersUserEmailOfferingsGet"></a>
# **usersUserEmailOfferingsGet**
> List&lt;OfferingMetadataResponse&gt; usersUserEmailOfferingsGet(userEmail)

Find user&#39;s offerings

Responds with all offerings that the user in.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersInIQualifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    UsersInIQualifyApi apiInstance = new UsersInIQualifyApi(defaultClient);
    String userEmail = "userEmail_example"; // String | user's email
    try {
      List<OfferingMetadataResponse> result = apiInstance.usersUserEmailOfferingsGet(userEmail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersInIQualifyApi#usersUserEmailOfferingsGet");
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
| **userEmail** | **String**| user&#39;s email | |

### Return type

[**List&lt;OfferingMetadataResponse&gt;**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user&#39;s offerings |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="usersUserEmailOfferingsPost"></a>
# **usersUserEmailOfferingsPost**
> List&lt;OfferingMetadataResponse&gt; usersUserEmailOfferingsPost(userEmail, requestBody)

Adds the user to the specified offerings as a learner

Adds a user to an array of offerings by offeringId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersInIQualifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    UsersInIQualifyApi apiInstance = new UsersInIQualifyApi(defaultClient);
    String userEmail = "userEmail_example"; // String | user's email
    List<String> requestBody = Arrays.asList(); // List<String> | offering ids
    try {
      List<OfferingMetadataResponse> result = apiInstance.usersUserEmailOfferingsPost(userEmail, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersInIQualifyApi#usersUserEmailOfferingsPost");
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
| **userEmail** | **String**| user&#39;s email | |
| **requestBody** | [**List&lt;String&gt;**](String.md)| offering ids | |

### Return type

[**List&lt;OfferingMetadataResponse&gt;**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user&#39;s offerings |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="usersUserEmailPatch"></a>
# **usersUserEmailPatch**
> UserResponse usersUserEmailPatch(userEmail, user)

Update user

Updates the specified user by email.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersInIQualifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    UsersInIQualifyApi apiInstance = new UsersInIQualifyApi(defaultClient);
    String userEmail = "userEmail_example"; // String | user's email
    User user = new User(); // User | 
    try {
      UserResponse result = apiInstance.usersUserEmailPatch(userEmail, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersInIQualifyApi#usersUserEmailPatch");
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
| **userEmail** | **String**| user&#39;s email | |
| **user** | [**User**](User.md)|  | [optional] |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user updated |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="usersUserEmailPermissionsPermissionNamePost"></a>
# **usersUserEmailPermissionsPermissionNamePost**
> UserResponse usersUserEmailPermissionsPermissionNamePost(userEmail, permissionName)

Add permission to user

Adds additional permissions to the specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersInIQualifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    UsersInIQualifyApi apiInstance = new UsersInIQualifyApi(defaultClient);
    String userEmail = "userEmail_example"; // String | user's email
    String permissionName = "builder"; // String | permission name
    try {
      UserResponse result = apiInstance.usersUserEmailPermissionsPermissionNamePost(userEmail, permissionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersInIQualifyApi#usersUserEmailPermissionsPermissionNamePost");
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
| **userEmail** | **String**| user&#39;s email | |
| **permissionName** | **String**| permission name | [enum: builder, manager] |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | permission successfully added to user |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="usersUserEmailSuspendPut"></a>
# **usersUserEmailSuspendPut**
> usersUserEmailSuspendPut(userEmail, suspendedRequest)

Suspend user

Suspends the specified user&#39;s account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersInIQualifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    UsersInIQualifyApi apiInstance = new UsersInIQualifyApi(defaultClient);
    String userEmail = "userEmail_example"; // String | user's email
    SuspendedRequest suspendedRequest = new SuspendedRequest(); // SuspendedRequest | 
    try {
      apiInstance.usersUserEmailSuspendPut(userEmail, suspendedRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersInIQualifyApi#usersUserEmailSuspendPut");
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
| **userEmail** | **String**| user&#39;s email | |
| **suspendedRequest** | [**SuspendedRequest**](SuspendedRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | User suspended. |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

