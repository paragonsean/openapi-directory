# AuthApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authTokenCreate**](AuthApi.md#authTokenCreate) | **POST** /auth/token |  |
| [**authTokenRefresh**](AuthApi.md#authTokenRefresh) | **POST** /auth/refresh |  |


<a id="authTokenCreate"></a>
# **authTokenCreate**
> AuthToken authTokenCreate(authTokenRequest)



Authenticate an API user identified by &#x60;api_key&#x60; and &#x60;api_secret&#x60;.

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
    defaultClient.setBasePath("/api/v2");

    AuthApi apiInstance = new AuthApi(defaultClient);
    AuthTokenRequest authTokenRequest = new AuthTokenRequest(); // AuthTokenRequest | AuthTokenRequest
    try {
      AuthToken result = apiInstance.authTokenCreate(authTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authTokenCreate");
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
| **authTokenRequest** | [**AuthTokenRequest**](AuthTokenRequest.md)| AuthTokenRequest | [optional] |

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | AuthToken |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |

<a id="authTokenRefresh"></a>
# **authTokenRefresh**
> AuthToken authTokenRefresh(refreshTokenRequest)



Reauthenticate the API user, issue a new &#x60;access_token&#x60; and &#x60;refresh_token&#x60; pair by providing the &#x60;refresh_token&#x60; in the request body.

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
    defaultClient.setBasePath("/api/v2");

    AuthApi apiInstance = new AuthApi(defaultClient);
    RefreshTokenRequest refreshTokenRequest = new RefreshTokenRequest(); // RefreshTokenRequest | RefreshTokenRequest
    try {
      AuthToken result = apiInstance.authTokenRefresh(refreshTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authTokenRefresh");
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
| **refreshTokenRequest** | [**RefreshTokenRequest**](RefreshTokenRequest.md)| RefreshTokenRequest | [optional] |

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | AuthToken |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |

