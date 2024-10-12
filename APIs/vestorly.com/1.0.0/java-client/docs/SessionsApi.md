# SessionsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**login**](SessionsApi.md#login) | **POST** /sessions |  |
| [**logout**](SessionsApi.md#logout) | **DELETE** /sessions/{id} |  |


<a id="login"></a>
# **login**
> Session login(username, password)



Login To Vestorly Platform

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
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String username = "username_example"; // String | Username in the vestorly platform
    String password = "password_example"; // String | Password in Vestorly Platform
    try {
      Session result = apiInstance.login(username, password);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#login");
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
| **username** | **String**| Username in the vestorly platform | |
| **password** | **String**| Password in Vestorly Platform | |

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="logout"></a>
# **logout**
> SessionLogoutResponse logout(vestorlyAuth, id)



Logout of the vestorly platform

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
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Authenication token
    String id = "id_example"; // String | ID of pet to session
    try {
      SessionLogoutResponse result = apiInstance.logout(vestorlyAuth, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#logout");
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
| **vestorlyAuth** | **String**| Authenication token | |
| **id** | **String**| ID of pet to session | |

### Return type

[**SessionLogoutResponse**](SessionLogoutResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | You have successfully logged out of the vestorly platform |  -  |

