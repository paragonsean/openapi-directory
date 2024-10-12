# AuthenticationApiControllerApi

All URIs are relative to *http://faceidentity-beta.azurewebsites.net/api/v1.0.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authenticateUser**](AuthenticationApiControllerApi.md#authenticateUser) | **POST** /authentication/customer/token | Get Token |
| [**register**](AuthenticationApiControllerApi.md#register) | **POST** /authentication/customer/registration | Customer Registration |


<a id="authenticateUser"></a>
# **authenticateUser**
> JwtResponse authenticateUser(loginUser)

Get Token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApiControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://faceidentity-beta.azurewebsites.net/api/v1.0.0");

    AuthenticationApiControllerApi apiInstance = new AuthenticationApiControllerApi(defaultClient);
    LoginUser loginUser = new LoginUser(); // LoginUser | The LoginUser definition used to returns the token for authentication
    try {
      JwtResponse result = apiInstance.authenticateUser(loginUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApiControllerApi#authenticateUser");
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
| **loginUser** | [**LoginUser**](LoginUser.md)| The LoginUser definition used to returns the token for authentication | |

### Return type

[**JwtResponse**](JwtResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **400** | Unexpected error |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="register"></a>
# **register**
> ResponseStatus register(register)

Customer Registration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApiControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://faceidentity-beta.azurewebsites.net/api/v1.0.0");

    AuthenticationApiControllerApi apiInstance = new AuthenticationApiControllerApi(defaultClient);
    Customer register = new Customer(); // Customer | The RegistrationForm definition is used to register the customer
    try {
      ResponseStatus result = apiInstance.register(register);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApiControllerApi#register");
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
| **register** | [**Customer**](Customer.md)| The RegistrationForm definition is used to register the customer | |

### Return type

[**ResponseStatus**](ResponseStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **400** | Unexpected error |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

