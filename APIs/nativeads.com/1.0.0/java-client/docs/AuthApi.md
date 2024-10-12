# AuthApi

All URIs are relative to *https://api.nativeads.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authDefaultLoginPost**](AuthApi.md#authDefaultLoginPost) | **POST** /auth/default/login |  |


<a id="authDefaultLoginPost"></a>
# **authDefaultLoginPost**
> AuthResponse authDefaultLoginPost(username, password)



Returns Native Ads Publisher API token

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
    defaultClient.setBasePath("https://api.nativeads.com");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String username = "username_example"; // String | Native Ads Publisher username
    String password = "password_example"; // String | Native Ads Publisher password
    try {
      AuthResponse result = apiInstance.authDefaultLoginPost(username, password);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authDefaultLoginPost");
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
| **username** | **String**| Native Ads Publisher username | |
| **password** | **String**| Native Ads Publisher password | |

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | authentication response |  -  |
| **400** | error message |  -  |

