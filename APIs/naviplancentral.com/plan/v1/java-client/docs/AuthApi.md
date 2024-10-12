# AuthApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authLoginByModel**](AuthApi.md#authLoginByModel) | **POST** /api/auth/Login | Start a session with the DomainProviders user store |
| [**authLogout**](AuthApi.md#authLogout) | **POST** /api/auth/Logout |  |
| [**authPasswordRequirements**](AuthApi.md#authPasswordRequirements) | **GET** /api/auth/LoginConfiguration | Gets the login rules |
| [**authResumeSession**](AuthApi.md#authResumeSession) | **POST** /api/auth/ResumeSession | Validate and extend the duration of a session |


<a id="authLoginByModel"></a>
# **authLoginByModel**
> PublicSessionInfoModel authLoginByModel(model)

Start a session with the DomainProviders user store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    AuthApi apiInstance = new AuthApi(defaultClient);
    LoginModel model = new LoginModel(); // LoginModel | DomainProvider username and password
    try {
      PublicSessionInfoModel result = apiInstance.authLoginByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authLoginByModel");
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
| **model** | [**LoginModel**](LoginModel.md)| DomainProvider username and password | |

### Return type

[**PublicSessionInfoModel**](PublicSessionInfoModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ApiSession |  -  |
| **401** | Invalid request parameters |  -  |
| **500** | Invalid HTTP scheme |  -  |

<a id="authLogout"></a>
# **authLogout**
> authLogout()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      apiInstance.authLogout();
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authLogout");
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
| **200** | OK |  -  |

<a id="authPasswordRequirements"></a>
# **authPasswordRequirements**
> authPasswordRequirements()

Gets the login rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      apiInstance.authPasswordRequirements();
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authPasswordRequirements");
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
| **200** | OK |  -  |

<a id="authResumeSession"></a>
# **authResumeSession**
> PublicSessionInfoModel authResumeSession()

Validate and extend the duration of a session

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      PublicSessionInfoModel result = apiInstance.authResumeSession();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authResumeSession");
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

[**PublicSessionInfoModel**](PublicSessionInfoModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | resume session |  -  |
| **401** | Unauthorized |  -  |

