# SessionsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSessions**](SessionsApi.md#deleteSessions) | **DELETE** /sessions | Delete user session (log out) |
| [**postSessions**](SessionsApi.md#postSessions) | **POST** /sessions | Create user session (log in) |


<a id="deleteSessions"></a>
# **deleteSessions**
> deleteSessions()

Delete user session (log out)

Delete user session (log out)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    try {
      apiInstance.deleteSessions();
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#deleteSessions");
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
| **204** | No body. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postSessions"></a>
# **postSessions**
> SessionEntity postSessions(otp, partialSessionId, password, username)

Create user session (log in)

Create user session (log in)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String otp = "otp_example"; // String | If this user has a 2FA device, provide its OTP or code here.
    String partialSessionId = "partialSessionId_example"; // String | Identifier for a partially-completed login
    String password = "password_example"; // String | Password for sign in
    String username = "username_example"; // String | Username to sign in as
    try {
      SessionEntity result = apiInstance.postSessions(otp, partialSessionId, password, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#postSessions");
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
| **otp** | **String**| If this user has a 2FA device, provide its OTP or code here. | [optional] |
| **partialSessionId** | **String**| Identifier for a partially-completed login | [optional] |
| **password** | **String**| Password for sign in | [optional] |
| **username** | **String**| Username to sign in as | [optional] |

### Return type

[**SessionEntity**](SessionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The Sessions object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

