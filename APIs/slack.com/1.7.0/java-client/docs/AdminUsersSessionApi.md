# AdminUsersSessionApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminUsersSessionInvalidate**](AdminUsersSessionApi.md#adminUsersSessionInvalidate) | **POST** /admin.users.session.invalidate |  |
| [**adminUsersSessionReset**](AdminUsersSessionApi.md#adminUsersSessionReset) | **POST** /admin.users.session.reset |  |


<a id="adminUsersSessionInvalidate"></a>
# **adminUsersSessionInvalidate**
> DefaultSuccessTemplate adminUsersSessionInvalidate(token, sessionId, teamId)



Invalidate a single session for a user by session_id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminUsersSessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminUsersSessionApi apiInstance = new AdminUsersSessionApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
    Integer sessionId = 56; // Integer | 
    String teamId = "teamId_example"; // String | ID of the team that the session belongs to
    try {
      DefaultSuccessTemplate result = apiInstance.adminUsersSessionInvalidate(token, sessionId, teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminUsersSessionApi#adminUsersSessionInvalidate");
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
| **sessionId** | **Integer**|  | |
| **teamId** | **String**| ID of the team that the session belongs to | |

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

<a id="adminUsersSessionReset"></a>
# **adminUsersSessionReset**
> DefaultSuccessTemplate adminUsersSessionReset(token, userId, mobileOnly, webOnly)



Wipes all valid sessions on all devices for a given user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminUsersSessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminUsersSessionApi apiInstance = new AdminUsersSessionApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
    String userId = "userId_example"; // String | The ID of the user to wipe sessions for
    Boolean mobileOnly = true; // Boolean | Only expire mobile sessions (default: false)
    Boolean webOnly = true; // Boolean | Only expire web sessions (default: false)
    try {
      DefaultSuccessTemplate result = apiInstance.adminUsersSessionReset(token, userId, mobileOnly, webOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminUsersSessionApi#adminUsersSessionReset");
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
| **userId** | **String**| The ID of the user to wipe sessions for | |
| **mobileOnly** | **Boolean**| Only expire mobile sessions (default: false) | [optional] |
| **webOnly** | **Boolean**| Only expire web sessions (default: false) | [optional] |

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

