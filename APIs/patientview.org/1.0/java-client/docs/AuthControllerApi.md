# AuthControllerApi

All URIs are relative to *https://www.patientview.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBasicUserInformation**](AuthControllerApi.md#getBasicUserInformation) | **GET** /auth/{token}/basicuserinformation | Get Basic User Information |
| [**logIn**](AuthControllerApi.md#logIn) | **POST** /auth/login | Log In |
| [**logOut**](AuthControllerApi.md#logOut) | **DELETE** /auth/logout/{token} | Log Out |


<a id="getBasicUserInformation"></a>
# **getBasicUserInformation**
> User getBasicUserInformation(token)

Get Basic User Information

Once logged in and have a token, get basic user information including group role membership

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    AuthControllerApi apiInstance = new AuthControllerApi(defaultClient);
    String token = "token_example"; // String | token
    try {
      User result = apiInstance.getBasicUserInformation(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthControllerApi#getBasicUserInformation");
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
| **token** | **String**| token | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="logIn"></a>
# **logIn**
> UserToken logIn(credentials)

Log In

Authenticate using username and password, returns token, which must be added to X-Auth-Token in header of all future requests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    AuthControllerApi apiInstance = new AuthControllerApi(defaultClient);
    Credentials credentials = new Credentials(); // Credentials | credentials
    try {
      UserToken result = apiInstance.logIn(credentials);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthControllerApi#logIn");
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
| **credentials** | [**Credentials**](Credentials.md)| credentials | [optional] |

### Return type

[**UserToken**](UserToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="logOut"></a>
# **logOut**
> logOut(token)

Log Out

Log Out

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    AuthControllerApi apiInstance = new AuthControllerApi(defaultClient);
    String token = "token_example"; // String | token
    try {
      apiInstance.logOut(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthControllerApi#logOut");
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
| **token** | **String**| token | |

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
| **200** | Description was not specified |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

