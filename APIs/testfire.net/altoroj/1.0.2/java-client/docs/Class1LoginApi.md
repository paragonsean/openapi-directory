# Class1LoginApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkLogin**](Class1LoginApi.md#checkLogin) | **GET** /login | Check if any user is logged in |
| [**login**](Class1LoginApi.md#login) | **POST** /login | Login method |


<a id="checkLogin"></a>
# **checkLogin**
> checkLogin(authorization)

Check if any user is logged in

If a user is loggedin the username will be returned

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class1LoginApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    Class1LoginApi apiInstance = new Class1LoginApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
    try {
      apiInstance.checkLogin(authorization);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class1LoginApi#checkLogin");
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
| **authorization** | **String**| Authorization token (provided upon successful login) | |

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
| **200** | Logged in |  -  |
| **401** | Logged out |  -  |

<a id="login"></a>
# **login**
> login(body)

Login method

After a successful login a token is returned. This is a Bearer token. To authenticate with it use the Authorization header and set value to Bearer empty space and the token value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class1LoginApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    Class1LoginApi apiInstance = new Class1LoginApi(defaultClient);
    Login body = new Login(); // Login | Username and password combination to allow users to log-in
    try {
      apiInstance.login(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class1LoginApi#login");
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
| **body** | [**Login**](Login.md)| Username and password combination to allow users to log-in | |

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
| **200** | Success message when login is complete |  -  |
| **400** | Bad parameters: Please check provided values |  -  |
| **500** | Internal server error: Please see error message or logs for details |  -  |

