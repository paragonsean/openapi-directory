# RegisterApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**acceptRegistration**](RegisterApi.md#acceptRegistration) | **POST** /api/v1/users/registrations/{registrationId}/accept | Accept registration |
| [**deleteRegistration**](RegisterApi.md#deleteRegistration) | **DELETE** /api/v1/users/registrations/{registrationId} | Delete registration |
| [**listRegistrations**](RegisterApi.md#listRegistrations) | **GET** /api/v1/users/registrations | List registrations |
| [**registerUser**](RegisterApi.md#registerUser) | **POST** /api/v1/users/register | Register a user |
| [**rejectRegistration**](RegisterApi.md#rejectRegistration) | **POST** /api/v1/users/registrations/{registrationId}/reject | Reject registration |
| [**requestRegistration**](RegisterApi.md#requestRegistration) | **POST** /api/v1/users/registrations/request | Request registration |
| [**resendEmailToVerifyRegistration**](RegisterApi.md#resendEmailToVerifyRegistration) | **POST** /api/v1/users/registrations/ask-send-verify-email | Resend verification link to registration email |
| [**resendEmailToVerifyUser_0**](RegisterApi.md#resendEmailToVerifyUser_0) | **POST** /api/v1/users/ask-send-verify-email | Resend user verification link |
| [**verifyRegistrationEmail**](RegisterApi.md#verifyRegistrationEmail) | **POST** /api/v1/users/registrations/{registrationId}/verify-email | Verify a registration email |
| [**verifyUser_0**](RegisterApi.md#verifyUser_0) | **POST** /api/v1/users/{id}/verify-email | Verify a user |


<a id="acceptRegistration"></a>
# **acceptRegistration**
> acceptRegistration(registrationId, userRegistrationAcceptOrReject)

Accept registration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    RegisterApi apiInstance = new RegisterApi(defaultClient);
    Integer registrationId = 56; // Integer | Registration ID
    UserRegistrationAcceptOrReject userRegistrationAcceptOrReject = new UserRegistrationAcceptOrReject(); // UserRegistrationAcceptOrReject | 
    try {
      apiInstance.acceptRegistration(registrationId, userRegistrationAcceptOrReject);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisterApi#acceptRegistration");
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
| **registrationId** | **Integer**| Registration ID | |
| **userRegistrationAcceptOrReject** | [**UserRegistrationAcceptOrReject**](UserRegistrationAcceptOrReject.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="deleteRegistration"></a>
# **deleteRegistration**
> deleteRegistration(registrationId)

Delete registration

Delete the registration entry. It will not remove the user associated with this registration (if any)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    RegisterApi apiInstance = new RegisterApi(defaultClient);
    Integer registrationId = 56; // Integer | Registration ID
    try {
      apiInstance.deleteRegistration(registrationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisterApi#deleteRegistration");
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
| **registrationId** | **Integer**| Registration ID | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="listRegistrations"></a>
# **listRegistrations**
> ListRegistrations200Response listRegistrations(start, count, search, sort)

List registrations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    RegisterApi apiInstance = new RegisterApi(defaultClient);
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String search = "search_example"; // String | 
    String sort = "-createdAt"; // String | 
    try {
      ListRegistrations200Response result = apiInstance.listRegistrations(start, count, search, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisterApi#listRegistrations");
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
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **search** | **String**|  | [optional] |
| **sort** | **String**|  | [optional] [enum: -createdAt, createdAt, state, -state] |

### Return type

[**ListRegistrations200Response**](ListRegistrations200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="registerUser"></a>
# **registerUser**
> registerUser(registerUser)

Register a user

Signup has to be enabled and signup approval is not required

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    RegisterApi apiInstance = new RegisterApi(defaultClient);
    RegisterUser registerUser = new RegisterUser(); // RegisterUser | 
    try {
      apiInstance.registerUser(registerUser);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisterApi#registerUser");
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
| **registerUser** | [**RegisterUser**](RegisterUser.md)|  | |

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
| **204** | successful operation |  -  |
| **400** | request error |  -  |
| **403** | user registration is not enabled, user limit is reached, registration is not allowed for the ip, requires approval or blocked by a plugin |  -  |
| **409** | a user with this username, channel name or email already exists |  -  |

<a id="rejectRegistration"></a>
# **rejectRegistration**
> rejectRegistration(registrationId, userRegistrationAcceptOrReject)

Reject registration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    RegisterApi apiInstance = new RegisterApi(defaultClient);
    Integer registrationId = 56; // Integer | Registration ID
    UserRegistrationAcceptOrReject userRegistrationAcceptOrReject = new UserRegistrationAcceptOrReject(); // UserRegistrationAcceptOrReject | 
    try {
      apiInstance.rejectRegistration(registrationId, userRegistrationAcceptOrReject);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisterApi#rejectRegistration");
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
| **registrationId** | **Integer**| Registration ID | |
| **userRegistrationAcceptOrReject** | [**UserRegistrationAcceptOrReject**](UserRegistrationAcceptOrReject.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="requestRegistration"></a>
# **requestRegistration**
> UserRegistration requestRegistration(userRegistrationRequest)

Request registration

Signup has to be enabled and require approval on the instance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    RegisterApi apiInstance = new RegisterApi(defaultClient);
    UserRegistrationRequest userRegistrationRequest = new UserRegistrationRequest(); // UserRegistrationRequest | 
    try {
      UserRegistration result = apiInstance.requestRegistration(userRegistrationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisterApi#requestRegistration");
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
| **userRegistrationRequest** | [**UserRegistrationRequest**](UserRegistrationRequest.md)|  | [optional] |

### Return type

[**UserRegistration**](UserRegistration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | request error or signup approval is not enabled on the instance |  -  |
| **403** | user registration is not enabled, user limit is reached, registration is not allowed for the ip or blocked by a plugin |  -  |
| **409** | a user or registration with this username, channel name or email already exists |  -  |

<a id="resendEmailToVerifyRegistration"></a>
# **resendEmailToVerifyRegistration**
> resendEmailToVerifyRegistration(resendEmailToVerifyRegistrationRequest)

Resend verification link to registration email

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    RegisterApi apiInstance = new RegisterApi(defaultClient);
    ResendEmailToVerifyRegistrationRequest resendEmailToVerifyRegistrationRequest = new ResendEmailToVerifyRegistrationRequest(); // ResendEmailToVerifyRegistrationRequest | 
    try {
      apiInstance.resendEmailToVerifyRegistration(resendEmailToVerifyRegistrationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisterApi#resendEmailToVerifyRegistration");
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
| **resendEmailToVerifyRegistrationRequest** | [**ResendEmailToVerifyRegistrationRequest**](ResendEmailToVerifyRegistrationRequest.md)|  | [optional] |

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
| **204** | successful operation |  -  |

<a id="resendEmailToVerifyUser_0"></a>
# **resendEmailToVerifyUser_0**
> resendEmailToVerifyUser_0(resendEmailToVerifyUserRequest)

Resend user verification link

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    RegisterApi apiInstance = new RegisterApi(defaultClient);
    ResendEmailToVerifyUserRequest resendEmailToVerifyUserRequest = new ResendEmailToVerifyUserRequest(); // ResendEmailToVerifyUserRequest | 
    try {
      apiInstance.resendEmailToVerifyUser_0(resendEmailToVerifyUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisterApi#resendEmailToVerifyUser_0");
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
| **resendEmailToVerifyUserRequest** | [**ResendEmailToVerifyUserRequest**](ResendEmailToVerifyUserRequest.md)|  | [optional] |

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
| **204** | successful operation |  -  |

<a id="verifyRegistrationEmail"></a>
# **verifyRegistrationEmail**
> verifyRegistrationEmail(registrationId, verifyRegistrationEmailRequest)

Verify a registration email

Following a user registration request, the user will receive an email asking to click a link containing a secret. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    RegisterApi apiInstance = new RegisterApi(defaultClient);
    Integer registrationId = 56; // Integer | Registration ID
    VerifyRegistrationEmailRequest verifyRegistrationEmailRequest = new VerifyRegistrationEmailRequest(); // VerifyRegistrationEmailRequest | 
    try {
      apiInstance.verifyRegistrationEmail(registrationId, verifyRegistrationEmailRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisterApi#verifyRegistrationEmail");
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
| **registrationId** | **Integer**| Registration ID | |
| **verifyRegistrationEmailRequest** | [**VerifyRegistrationEmailRequest**](VerifyRegistrationEmailRequest.md)|  | [optional] |

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
| **204** | successful operation |  -  |
| **403** | invalid verification string |  -  |
| **404** | registration not found |  -  |

<a id="verifyUser_0"></a>
# **verifyUser_0**
> verifyUser_0(id, verifyUserRequest)

Verify a user

Following a user registration, the new user will receive an email asking to click a link containing a secret. This endpoint can also be used to verify a new email set in the user account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    RegisterApi apiInstance = new RegisterApi(defaultClient);
    Integer id = 56; // Integer | Entity id
    VerifyUserRequest verifyUserRequest = new VerifyUserRequest(); // VerifyUserRequest | 
    try {
      apiInstance.verifyUser_0(id, verifyUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisterApi#verifyUser_0");
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
| **id** | **Integer**| Entity id | |
| **verifyUserRequest** | [**VerifyUserRequest**](VerifyUserRequest.md)|  | [optional] |

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
| **204** | successful operation |  -  |
| **403** | invalid verification string |  -  |
| **404** | user not found |  -  |

