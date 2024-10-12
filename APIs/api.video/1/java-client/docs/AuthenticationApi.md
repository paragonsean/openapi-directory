# AuthenticationApi

All URIs are relative to *https://ws.api.video*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pOSTAuthApiKey**](AuthenticationApi.md#pOSTAuthApiKey) | **POST** /auth/api-key | Authenticate |
| [**pOSTAuthRefresh**](AuthenticationApi.md#pOSTAuthRefresh) | **POST** /auth/refresh | Refresh token |


<a id="pOSTAuthApiKey"></a>
# **pOSTAuthApiKey**
> AccessToken pOSTAuthApiKey(authenticatePayload)

Authenticate

To get started, submit your API key in the body of your request. api.video returns an access token that is valid for one hour (3600 seconds). A refresh token is also returned. View a [tutorial](https://api.video/blog/tutorials/authentication-tutorial) on authentication. All tutorials using the [authentication endpoint](https://api.video/blog/endpoints/authenticate)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    AuthenticatePayload authenticatePayload = new AuthenticatePayload(); // AuthenticatePayload | 
    try {
      AccessToken result = apiInstance.pOSTAuthApiKey(authenticatePayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#pOSTAuthApiKey");
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
| **authenticatePayload** | [**AuthenticatePayload**](AuthenticatePayload.md)|  | [optional] |

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="pOSTAuthRefresh"></a>
# **pOSTAuthRefresh**
> AccessToken pOSTAuthRefresh(refreshTokenPayload)

Refresh token

Use the refresh endpoint with the refresh token you received when you first authenticated using the api-key endpoint. Send the refresh token in the body of your request. The api.video API returns a new access token that is valid for one hour (3600 seconds) and a new refresh token.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    RefreshTokenPayload refreshTokenPayload = new RefreshTokenPayload(); // RefreshTokenPayload | 
    try {
      AccessToken result = apiInstance.pOSTAuthRefresh(refreshTokenPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#pOSTAuthRefresh");
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
| **refreshTokenPayload** | [**RefreshTokenPayload**](RefreshTokenPayload.md)|  | [optional] |

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

