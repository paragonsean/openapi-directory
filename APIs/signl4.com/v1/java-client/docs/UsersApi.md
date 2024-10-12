# UsersApi

All URIs are relative to *https://connect.signl4.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersGet**](UsersApi.md#usersGet) | **GET** /users | Get all Users |
| [**usersUserIdChangePasswordPut**](UsersApi.md#usersUserIdChangePasswordPut) | **PUT** /users/{userId}/changePassword | Updates the password of a user |
| [**usersUserIdCheckPermissionsPost**](UsersApi.md#usersUserIdCheckPermissionsPost) | **POST** /users/{userId}/checkPermissions | Checks if a user has the provided permission. |
| [**usersUserIdDutyStatusGet**](UsersApi.md#usersUserIdDutyStatusGet) | **GET** /users/{userId}/dutyStatus | Get duty status by user Id |
| [**usersUserIdGet**](UsersApi.md#usersUserIdGet) | **GET** /users/{userId} | Get User by Id |
| [**usersUserIdImageGet**](UsersApi.md#usersUserIdImageGet) | **GET** /users/{userId}/image |  |
| [**usersUserIdImagePost**](UsersApi.md#usersUserIdImagePost) | **POST** /users/{userId}/image | Uploaded a profile image for a specified user. |
| [**usersUserIdProfilePut**](UsersApi.md#usersUserIdProfilePut) | **PUT** /users/{userId}/profile | Updates user profile of an user |
| [**usersUserIdPunchInAsManagerPost**](UsersApi.md#usersUserIdPunchInAsManagerPost) | **POST** /users/{userId}/punchInAsManager | Punch User in as Manager |
| [**usersUserIdPunchInPost**](UsersApi.md#usersUserIdPunchInPost) | **POST** /users/{userId}/punchIn | Punch User in |
| [**usersUserIdPunchOutPost**](UsersApi.md#usersUserIdPunchOutPost) | **POST** /users/{userId}/punchOut | Punch User out |
| [**usersUserIdSetupProgressGet**](UsersApi.md#usersUserIdSetupProgressGet) | **GET** /users/{userId}/setupProgress | Gets setup progress of a specific user. |


<a id="usersGet"></a>
# **usersGet**
> List&lt;UserInfo&gt; usersGet()

Get all Users

Returns a list of user objects with details such as their email address and duty information. Only users who  are part of your team will be returned.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      List<UserInfo> result = apiInstance.usersGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGet");
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

[**List&lt;UserInfo&gt;**](UserInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User could be successfully identified. |  -  |
| **400** | Required authentifaction info could not be found in the request/claims. |  -  |
| **403** | You&#39;re not allowed to request the users with their information. |  -  |
| **404** | Required entities could not be found in the database. |  -  |

<a id="usersUserIdChangePasswordPut"></a>
# **usersUserIdChangePasswordPut**
> usersUserIdChangePasswordPut(userId, updatePasswordInfo)

Updates the password of a user

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | User ID of user whose password should be changed.
    UpdatePasswordInfo updatePasswordInfo = new UpdatePasswordInfo(); // UpdatePasswordInfo | 
    try {
      apiInstance.usersUserIdChangePasswordPut(userId, updatePasswordInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUserIdChangePasswordPut");
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
| **userId** | **String**| User ID of user whose password should be changed. | |
| **updatePasswordInfo** | [**UpdatePasswordInfo**](UpdatePasswordInfo.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Server Error |  -  |

<a id="usersUserIdCheckPermissionsPost"></a>
# **usersUserIdCheckPermissionsPost**
> UserImage usersUserIdCheckPermissionsPost(userId, teamId, stringItemsWrapper)

Checks if a user has the provided permission.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | ID of the user to check permissions for.
    String teamId = "teamId_example"; // String | 
    StringItemsWrapper stringItemsWrapper = new StringItemsWrapper(); // StringItemsWrapper | List of permissions to check
    try {
      UserImage result = apiInstance.usersUserIdCheckPermissionsPost(userId, teamId, stringItemsWrapper);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUserIdCheckPermissionsPost");
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
| **userId** | **String**| ID of the user to check permissions for. | |
| **teamId** | **String**|  | [optional] |
| **stringItemsWrapper** | [**StringItemsWrapper**](StringItemsWrapper.md)| List of permissions to check | [optional] |

### Return type

[**UserImage**](UserImage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="usersUserIdDutyStatusGet"></a>
# **usersUserIdDutyStatusGet**
> UserDutyInfo usersUserIdDutyStatusGet(userId)

Get duty status by user Id

Returns a object with duty information.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | Identifier of the user to get. Use 'Me' to get information about the currently logged in user. This is not possible with an api key.  Can also be an email address of a user in the team or the unique id of an according user object.”
    try {
      UserDutyInfo result = apiInstance.usersUserIdDutyStatusGet(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUserIdDutyStatusGet");
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
| **userId** | **String**| Identifier of the user to get. Use &#39;Me&#39; to get information about the currently logged in user. This is not possible with an api key.  Can also be an email address of a user in the team or the unique id of an according user object.” | |

### Return type

[**UserDutyInfo**](UserDutyInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Duty successfully loaded. |  -  |
| **400** | Required authentifaction info could not be found in the request/claims. |  -  |
| **403** | You&#39;re not allowed to request that duty information. |  -  |
| **404** | Required entities could not be found in the database. |  -  |

<a id="usersUserIdGet"></a>
# **usersUserIdGet**
> UserInfo usersUserIdGet(userId)

Get User by Id

Returns a user object with details such as his email address and duty information.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | Identifier of the user to get. Use 'Me' to get information about the currently logged in user. This is not possible with an api key.  Can also be an email address of a user in the team or the unique id of an according user object.”
    try {
      UserInfo result = apiInstance.usersUserIdGet(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUserIdGet");
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
| **userId** | **String**| Identifier of the user to get. Use &#39;Me&#39; to get information about the currently logged in user. This is not possible with an api key.  Can also be an email address of a user in the team or the unique id of an according user object.” | |

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User could be successfully identified. |  -  |
| **400** | Required authentifaction info could not be found in the request/claims. |  -  |
| **403** | You&#39;re not allowed to request that user&#39;s information. |  -  |
| **404** | Required entities could not be found in the database. |  -  |

<a id="usersUserIdImageGet"></a>
# **usersUserIdImageGet**
> UserImage usersUserIdImageGet(userId, height, width)



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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | 
    Integer height = 56; // Integer | 
    Integer width = 56; // Integer | 
    try {
      UserImage result = apiInstance.usersUserIdImageGet(userId, height, width);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUserIdImageGet");
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
| **height** | **Integer**|  | [optional] |
| **width** | **Integer**|  | [optional] |

### Return type

[**UserImage**](UserImage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="usersUserIdImagePost"></a>
# **usersUserIdImagePost**
> usersUserIdImagePost(userId)

Uploaded a profile image for a specified user.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | Id of the user.
    try {
      apiInstance.usersUserIdImagePost(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUserIdImagePost");
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
| **userId** | **String**| Id of the user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **204** | The image was successfully uploaded. |  -  |
| **400** | Either a passed parameter was either empty/null or the request&#39;s multipart does not contain a  file. |  -  |
| **403** | User is not allowed to upoload an image for the specified user. |  -  |
| **404** | Either the user was not found or they aren&#39;t activated yet. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="usersUserIdProfilePut"></a>
# **usersUserIdProfilePut**
> UserInfo usersUserIdProfilePut(userId, userProfile)

Updates user profile of an user

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | ID of user to update.
    UserProfile userProfile = new UserProfile(); // UserProfile | 
    try {
      UserInfo result = apiInstance.usersUserIdProfilePut(userId, userProfile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUserIdProfilePut");
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
| **userId** | **String**| ID of user to update. | |
| **userProfile** | [**UserProfile**](UserProfile.md)|  | [optional] |

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Server Error |  -  |

<a id="usersUserIdPunchInAsManagerPost"></a>
# **usersUserIdPunchInAsManagerPost**
> UserDutyInfo usersUserIdPunchInAsManagerPost(userId)

Punch User in as Manager

The specified user will be punched in to duty as a manager.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | Identifier of the user to punch in. Use 'Me' to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.”
    try {
      UserDutyInfo result = apiInstance.usersUserIdPunchInAsManagerPost(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUserIdPunchInAsManagerPost");
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
| **userId** | **String**| Identifier of the user to punch in. Use &#39;Me&#39; to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.” | |

### Return type

[**UserDutyInfo**](UserDutyInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **403** | The user tried to change the punch in a different user. |  -  |
| **404** | Required entities could not be found in the database. |  -  |

<a id="usersUserIdPunchInPost"></a>
# **usersUserIdPunchInPost**
> UserDutyInfo usersUserIdPunchInPost(userId)

Punch User in

The specified user will be punched in to duty.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | Identifier of the user to punch in. Use 'Me' to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.”
    try {
      UserDutyInfo result = apiInstance.usersUserIdPunchInPost(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUserIdPunchInPost");
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
| **userId** | **String**| Identifier of the user to punch in. Use &#39;Me&#39; to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.” | |

### Return type

[**UserDutyInfo**](UserDutyInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **403** | The user tried to change the punch in a different user. |  -  |
| **404** | Required entities could not be found in the database. |  -  |

<a id="usersUserIdPunchOutPost"></a>
# **usersUserIdPunchOutPost**
> UserDutyInfo usersUserIdPunchOutPost(userId)

Punch User out

The specified user will be punched out from duty.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | Identifier of the user to punch out. Use 'Me' to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.”
    try {
      UserDutyInfo result = apiInstance.usersUserIdPunchOutPost(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUserIdPunchOutPost");
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
| **userId** | **String**| Identifier of the user to punch out. Use &#39;Me&#39; to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.” | |

### Return type

[**UserDutyInfo**](UserDutyInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user was punched out successfully. |  -  |
| **400** | Required authentifaction information could not be found in the request/claims. |  -  |
| **403** | The requesting user tried to punch out someone else, which is not allowed. |  -  |
| **404** | The desired user was not found by passed id. |  -  |
| **409** | The desired user was not punched out because it would violate  the minumum on-duty members setting  from the team. |  -  |

<a id="usersUserIdSetupProgressGet"></a>
# **usersUserIdSetupProgressGet**
> UserSetupProgress usersUserIdSetupProgressGet(userId)

Gets setup progress of a specific user.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | ID of the user the progress should be retrieved for.
    try {
      UserSetupProgress result = apiInstance.usersUserIdSetupProgressGet(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUserIdSetupProgressGet");
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
| **userId** | **String**| ID of the user the progress should be retrieved for. | |

### Return type

[**UserSetupProgress**](UserSetupProgress.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

