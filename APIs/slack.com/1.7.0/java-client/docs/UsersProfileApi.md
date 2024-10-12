# UsersProfileApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersProfileGet**](UsersProfileApi.md#usersProfileGet) | **GET** /users.profile.get |  |
| [**usersProfileSet**](UsersProfileApi.md#usersProfileSet) | **POST** /users.profile.set |  |


<a id="usersProfileGet"></a>
# **usersProfileGet**
> UsersProfileGetSchema usersProfileGet(token, includeLabels, user)



Retrieves a user&#39;s profile information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsersProfileApi apiInstance = new UsersProfileApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users.profile:read`
    Boolean includeLabels = true; // Boolean | Include labels for each ID in custom profile fields
    String user = "user_example"; // String | User to retrieve profile info for
    try {
      UsersProfileGetSchema result = apiInstance.usersProfileGet(token, includeLabels, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersProfileApi#usersProfileGet");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;users.profile:read&#x60; | |
| **includeLabels** | **Boolean**| Include labels for each ID in custom profile fields | [optional] |
| **user** | **String**| User to retrieve profile info for | [optional] |

### Return type

[**UsersProfileGetSchema**](UsersProfileGetSchema.md)

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

<a id="usersProfileSet"></a>
# **usersProfileSet**
> UsersProfileSetSchema usersProfileSet(token, name, profile, user, value)



Set the profile information for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsersProfileApi apiInstance = new UsersProfileApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users.profile:write`
    String name = "name_example"; // String | Name of a single key to set. Usable only if `profile` is not passed.
    String profile = "profile_example"; // String | Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set. Each field name is limited to 255 characters.
    String user = "user_example"; // String | ID of user to change. This argument may only be specified by team admins on paid teams.
    String value = "value_example"; // String | Value to set a single key to. Usable only if `profile` is not passed.
    try {
      UsersProfileSetSchema result = apiInstance.usersProfileSet(token, name, profile, user, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersProfileApi#usersProfileSet");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;users.profile:write&#x60; | |
| **name** | **String**| Name of a single key to set. Usable only if &#x60;profile&#x60; is not passed. | [optional] |
| **profile** | **String**| Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set. Each field name is limited to 255 characters. | [optional] |
| **user** | **String**| ID of user to change. This argument may only be specified by team admins on paid teams. | [optional] |
| **value** | **String**| Value to set a single key to. Usable only if &#x60;profile&#x60; is not passed. | [optional] |

### Return type

[**UsersProfileSetSchema**](UsersProfileSetSchema.md)

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

