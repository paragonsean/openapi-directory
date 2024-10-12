# AuthApi

All URIs are relative to *https://events.1password.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAuthIntrospect**](AuthApi.md#getAuthIntrospect) | **GET** /api/auth/introspect | Performs introspection of the provided Bearer JWT token |
| [**getAuthIntrospectV2**](AuthApi.md#getAuthIntrospectV2) | **GET** /api/v2/auth/introspect | Performs introspection of the provided Bearer JWT token |


<a id="getAuthIntrospect"></a>
# **getAuthIntrospect**
> Introspection getAuthIntrospect()

Performs introspection of the provided Bearer JWT token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.1password.com");
    
    // Configure HTTP bearer authorization: jwtsa
    HttpBearerAuth jwtsa = (HttpBearerAuth) defaultClient.getAuthentication("jwtsa");
    jwtsa.setBearerToken("BEARER TOKEN");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      Introspection result = apiInstance.getAuthIntrospect();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#getAuthIntrospect");
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

[**Introspection**](Introspection.md)

### Authorization

[jwtsa](../README.md#jwtsa)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Introspection object |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |
| **0** | Generic error |  -  |

<a id="getAuthIntrospectV2"></a>
# **getAuthIntrospectV2**
> IntrospectionV2 getAuthIntrospectV2()

Performs introspection of the provided Bearer JWT token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.1password.com");
    
    // Configure HTTP bearer authorization: jwtsa
    HttpBearerAuth jwtsa = (HttpBearerAuth) defaultClient.getAuthentication("jwtsa");
    jwtsa.setBearerToken("BEARER TOKEN");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      IntrospectionV2 result = apiInstance.getAuthIntrospectV2();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#getAuthIntrospectV2");
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

[**IntrospectionV2**](IntrospectionV2.md)

### Authorization

[jwtsa](../README.md#jwtsa)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Introspection v2 object |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |
| **0** | Generic error |  -  |

