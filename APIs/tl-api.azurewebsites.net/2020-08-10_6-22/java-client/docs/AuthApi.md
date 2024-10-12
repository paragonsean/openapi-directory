# AuthApi

All URIs are relative to *https://tl-api.azurewebsites.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authLogin**](AuthApi.md#authLogin) | **POST** /api/Auth/login | Authenticate and provide token for autherizations.              |


<a id="authLogin"></a>
# **authLogin**
> File authLogin(loginDTO)

Authenticate and provide token for autherizations.             

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
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    AuthApi apiInstance = new AuthApi(defaultClient);
    LoginDTO loginDTO = new LoginDTO(); // LoginDTO | Login Credentials
    try {
      File result = apiInstance.authLogin(loginDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authLogin");
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
| **loginDTO** | [**LoginDTO**](LoginDTO.md)| Login Credentials | |

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authorizized with a new token or unauthorized request. |  -  |

