# PublicSecuritySecurityApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**login**](PublicSecuritySecurityApi.md#login) | **POST** /v2/public/security/login | Login |
| [**lostPassword**](PublicSecuritySecurityApi.md#lostPassword) | **POST** /v2/public/security/lostpassword | Lost password |
| [**register**](PublicSecuritySecurityApi.md#register) | **POST** /v2/public/security/register | User Registration |


<a id="login"></a>
# **login**
> ApiCredentials login(loginRequest)

Login

User Login - The login will give your tokens

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicSecuritySecurityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    PublicSecuritySecurityApi apiInstance = new PublicSecuritySecurityApi(defaultClient);
    LoginRequest loginRequest = new LoginRequest(); // LoginRequest | 
    try {
      ApiCredentials result = apiInstance.login(loginRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicSecuritySecurityApi#login");
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
| **loginRequest** | [**LoginRequest**](LoginRequest.md)|  | |

### Return type

[**ApiCredentials**](ApiCredentials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your tokens |  -  |
| **400** | Bad Request |  -  |
| **403** | Invalid credentials |  -  |
| **500** | Occurs when something goes wrong |  -  |

<a id="lostPassword"></a>
# **lostPassword**
> lostPassword(body)

Lost password

Lost password - Your password will be regenerated and sent to your email

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicSecuritySecurityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    PublicSecuritySecurityApi apiInstance = new PublicSecuritySecurityApi(defaultClient);
    String body = "body_example"; // String | Your email
    try {
      apiInstance.lostPassword(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicSecuritySecurityApi#lostPassword");
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
| **body** | **String**| Your email | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | New password sent |  -  |
| **400** | Bad Request |  -  |
| **404** | Email not found |  -  |
| **500** | Occurs when something goes wrong |  -  |
| **502** | Problem with SMTP service |  -  |

<a id="register"></a>
# **register**
> register(registerRequest)

User Registration

User Registration - Create a new user on BeezUP

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicSecuritySecurityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    PublicSecuritySecurityApi apiInstance = new PublicSecuritySecurityApi(defaultClient);
    RegisterRequest registerRequest = new RegisterRequest(); // RegisterRequest | 
    try {
      apiInstance.register(registerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicSecuritySecurityApi#register");
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
| **registerRequest** | [**RegisterRequest**](RegisterRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Customer registered |  -  |
| **400** | Email or password is invalid. Disposable email are refused. |  -  |
| **409** | Email already used |  -  |
| **500** | Occurs when something goes wrong |  -  |

