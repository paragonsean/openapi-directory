# SecurityApi

All URIs are relative to *http://superset.apache.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**securityCsrfTokenGet**](SecurityApi.md#securityCsrfTokenGet) | **GET** /security/csrf_token/ |  |
| [**securityLoginPost**](SecurityApi.md#securityLoginPost) | **POST** /security/login |  |
| [**securityRefreshPost**](SecurityApi.md#securityRefreshPost) | **POST** /security/refresh |  |


<a id="securityCsrfTokenGet"></a>
# **securityCsrfTokenGet**
> SecurityCsrfTokenGet200Response securityCsrfTokenGet()



Fetch the CSRF token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecurityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    SecurityApi apiInstance = new SecurityApi(defaultClient);
    try {
      SecurityCsrfTokenGet200Response result = apiInstance.securityCsrfTokenGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecurityApi#securityCsrfTokenGet");
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

[**SecurityCsrfTokenGet200Response**](SecurityCsrfTokenGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result contains the CSRF token |  -  |
| **401** | Unauthorized |  -  |
| **500** | Fatal error |  -  |

<a id="securityLoginPost"></a>
# **securityLoginPost**
> SecurityLoginPost200Response securityLoginPost(securityLoginPostRequest)



Authenticate and get a JWT access and refresh token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecurityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");

    SecurityApi apiInstance = new SecurityApi(defaultClient);
    SecurityLoginPostRequest securityLoginPostRequest = new SecurityLoginPostRequest(); // SecurityLoginPostRequest | 
    try {
      SecurityLoginPost200Response result = apiInstance.securityLoginPost(securityLoginPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecurityApi#securityLoginPost");
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
| **securityLoginPostRequest** | [**SecurityLoginPostRequest**](SecurityLoginPostRequest.md)|  | |

### Return type

[**SecurityLoginPost200Response**](SecurityLoginPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authentication Successful |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Fatal error |  -  |

<a id="securityRefreshPost"></a>
# **securityRefreshPost**
> SecurityRefreshPost200Response securityRefreshPost()



Use the refresh token to get a new JWT access token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecurityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt_refresh
    HttpBearerAuth jwt_refresh = (HttpBearerAuth) defaultClient.getAuthentication("jwt_refresh");
    jwt_refresh.setBearerToken("BEARER TOKEN");

    SecurityApi apiInstance = new SecurityApi(defaultClient);
    try {
      SecurityRefreshPost200Response result = apiInstance.securityRefreshPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecurityApi#securityRefreshPost");
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

[**SecurityRefreshPost200Response**](SecurityRefreshPost200Response.md)

### Authorization

[jwt_refresh](../README.md#jwt_refresh)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Refresh Successful |  -  |
| **401** | Unauthorized |  -  |
| **500** | Fatal error |  -  |

