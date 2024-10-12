# AuthApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authGet**](AuthApi.md#authGet) | **GET** /auth |  |


<a id="authGet"></a>
# **authGet**
> AuthResult authGet()



Request a JWT access token using your obono username and password.

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
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      AuthResult result = apiInstance.authGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authGet");
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

[**AuthResult**](AuthResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The JWT &#x60;accessToken&#x60; to use for accessing secured resourced as well as the &#x60;registrierkassenUuid&#x60; of the corresponding \&quot;Registrierkasse\&quot;. |  -  |

