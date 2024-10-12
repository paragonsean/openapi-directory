# PasswordsApi

All URIs are relative to *http://c19qrserver.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changePasswordPost**](PasswordsApi.md#changePasswordPost) | **POST** /changePassword | Used for changing your password |
| [**requestPasswordResetPost**](PasswordsApi.md#requestPasswordResetPost) | **POST** /requestPasswordReset | Used for requesting a password reset code |
| [**verifyPasswordChangePost**](PasswordsApi.md#verifyPasswordChangePost) | **POST** /verifyPasswordChange | Used for resetting your password when you forgot it |


<a id="changePasswordPost"></a>
# **changePasswordPost**
> changePasswordPost(sample)

Used for changing your password

Pass in your old password and your new password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PasswordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://c19qrserver.local");
    
    // Configure API key authorization: TokenHeader
    ApiKeyAuth TokenHeader = (ApiKeyAuth) defaultClient.getAuthentication("TokenHeader");
    TokenHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenHeader.setApiKeyPrefix("Token");

    PasswordsApi apiInstance = new PasswordsApi(defaultClient);
    Sample sample = new Sample(); // Sample | Change Password Payload
    try {
      apiInstance.changePasswordPost(sample);
    } catch (ApiException e) {
      System.err.println("Exception when calling PasswordsApi#changePasswordPost");
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
| **sample** | [**Sample**](Sample.md)| Change Password Payload | |

### Return type

null (empty response body)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="requestPasswordResetPost"></a>
# **requestPasswordResetPost**
> RequestPasswordResetResponse requestPasswordResetPost(sample2)

Used for requesting a password reset code

The admin should run this on behalf of a user who forgot their password.  The API will generate a password reset code which the admin should then provide to the user. The user can use their client to reset their password. Normally the password reset code is mailed to the user, but I didn&#39;t want to do this in this case because I didn&#39;t want to  introduce the complicated dependency of having an SMTP server just for this purpose. Doing it this way makes it easy for people to adopt this  API. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PasswordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://c19qrserver.local");
    
    // Configure API key authorization: TokenHeader
    ApiKeyAuth TokenHeader = (ApiKeyAuth) defaultClient.getAuthentication("TokenHeader");
    TokenHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenHeader.setApiKeyPrefix("Token");

    PasswordsApi apiInstance = new PasswordsApi(defaultClient);
    Sample2 sample2 = new Sample2(); // Sample2 | Request Password Reset Payload
    try {
      RequestPasswordResetResponse result = apiInstance.requestPasswordResetPost(sample2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PasswordsApi#requestPasswordResetPost");
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
| **sample2** | [**Sample2**](Sample2.md)| Request Password Reset Payload | |

### Return type

[**RequestPasswordResetResponse**](RequestPasswordResetResponse.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="verifyPasswordChangePost"></a>
# **verifyPasswordChangePost**
> verifyPasswordChangePost(sample4)

Used for resetting your password when you forgot it

Another endpoint will generate a password reset code for you. You should  use the client app to submit the reset code along with the new password to change your password. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PasswordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://c19qrserver.local");
    
    // Configure API key authorization: TokenHeader
    ApiKeyAuth TokenHeader = (ApiKeyAuth) defaultClient.getAuthentication("TokenHeader");
    TokenHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenHeader.setApiKeyPrefix("Token");

    PasswordsApi apiInstance = new PasswordsApi(defaultClient);
    Sample4 sample4 = new Sample4(); // Sample4 | Password Reset Payload
    try {
      apiInstance.verifyPasswordChangePost(sample4);
    } catch (ApiException e) {
      System.err.println("Exception when calling PasswordsApi#verifyPasswordChangePost");
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
| **sample4** | [**Sample4**](Sample4.md)| Password Reset Payload | |

### Return type

null (empty response body)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

