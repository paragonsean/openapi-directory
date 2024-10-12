# AuthenticationApiControllerApi

All URIs are relative to *http://apibeta.uscann.net/apiv1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authenticateUser**](AuthenticationApiControllerApi.md#authenticateUser) | **POST** /authentication/token | authenticate the user and returns the token |
| [**forgotPassword**](AuthenticationApiControllerApi.md#forgotPassword) | **POST** /authentication/forgotPassword | forgotPassword |
| [**register**](AuthenticationApiControllerApi.md#register) | **POST** /authentication/register | register |
| [**setForgotPassword**](AuthenticationApiControllerApi.md#setForgotPassword) | **POST** /authentication/setForgotPassword | validates the mail token and set new password |
| [**validateMailToken**](AuthenticationApiControllerApi.md#validateMailToken) | **POST** /authentication/validateMailToken | validates the mail token |


<a id="authenticateUser"></a>
# **authenticateUser**
> JwtResponse authenticateUser(contentType, loginUser)

authenticate the user and returns the token

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
    defaultClient.setBasePath("http://apibeta.uscann.net/apiv1");

    AuthenticationApiControllerApi apiInstance = new AuthenticationApiControllerApi(defaultClient);
    String contentType = "application/json"; // String | 
    LoginUser loginUser = new LoginUser(); // LoginUser | The LoginUser definition used to returns the token for authentication
    try {
      JwtResponse result = apiInstance.authenticateUser(contentType, loginUser);
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
| **contentType** | **String**|  | [default to application/json] |
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

<a id="forgotPassword"></a>
# **forgotPassword**
> ResponseStatus forgotPassword(contentType, forgotPassword)

forgotPassword

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
    defaultClient.setBasePath("http://apibeta.uscann.net/apiv1");

    AuthenticationApiControllerApi apiInstance = new AuthenticationApiControllerApi(defaultClient);
    String contentType = "application/json"; // String | 
    EmailModel forgotPassword = new EmailModel(); // EmailModel | The User email used to send email
    try {
      ResponseStatus result = apiInstance.forgotPassword(contentType, forgotPassword);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApiControllerApi#forgotPassword");
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
| **contentType** | **String**|  | [default to application/json] |
| **forgotPassword** | [**EmailModel**](EmailModel.md)| The User email used to send email | |

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

<a id="register"></a>
# **register**
> ResponseStatus register(contentType, register)

register

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
    defaultClient.setBasePath("http://apibeta.uscann.net/apiv1");

    AuthenticationApiControllerApi apiInstance = new AuthenticationApiControllerApi(defaultClient);
    String contentType = "application/json"; // String | 
    RegistrationModel register = new RegistrationModel(); // RegistrationModel | The RegistrationForm definition is used to register the customer
    try {
      ResponseStatus result = apiInstance.register(contentType, register);
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
| **contentType** | **String**|  | [default to application/json] |
| **register** | [**RegistrationModel**](RegistrationModel.md)| The RegistrationForm definition is used to register the customer | |

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

<a id="setForgotPassword"></a>
# **setForgotPassword**
> ResponseStatus setForgotPassword(contentType, token)

validates the mail token and set new password

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
    defaultClient.setBasePath("http://apibeta.uscann.net/apiv1");

    AuthenticationApiControllerApi apiInstance = new AuthenticationApiControllerApi(defaultClient);
    String contentType = "application/json"; // String | 
    ForgotMailToken token = new ForgotMailToken(); // ForgotMailToken | The ForgotMailToken definition used to returns status of password reset
    try {
      ResponseStatus result = apiInstance.setForgotPassword(contentType, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApiControllerApi#setForgotPassword");
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
| **contentType** | **String**|  | [default to application/json] |
| **token** | [**ForgotMailToken**](ForgotMailToken.md)| The ForgotMailToken definition used to returns status of password reset | |

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

<a id="validateMailToken"></a>
# **validateMailToken**
> ResponseStatus validateMailToken(contentType, token)

validates the mail token

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
    defaultClient.setBasePath("http://apibeta.uscann.net/apiv1");

    AuthenticationApiControllerApi apiInstance = new AuthenticationApiControllerApi(defaultClient);
    String contentType = "application/json"; // String | 
    MailToken token = new MailToken(); // MailToken | The MailToken definition used to returns status of validation
    try {
      ResponseStatus result = apiInstance.validateMailToken(contentType, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApiControllerApi#validateMailToken");
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
| **contentType** | **String**|  | [default to application/json] |
| **token** | [**MailToken**](MailToken.md)| The MailToken definition used to returns status of validation | |

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

