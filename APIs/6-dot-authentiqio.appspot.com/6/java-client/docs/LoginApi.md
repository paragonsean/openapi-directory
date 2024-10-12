# LoginApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pushLoginRequest**](LoginApi.md#pushLoginRequest) | **POST** /login |  |


<a id="pushLoginRequest"></a>
# **pushLoginRequest**
> PushLoginRequest200Response pushLoginRequest(paramCallback, pushToken)



push sign-in request See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoginApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    LoginApi apiInstance = new LoginApi(defaultClient);
    String paramCallback = "paramCallback_example"; // String | URI App will connect to
    PushToken pushToken = new PushToken(); // PushToken | Push Token.
    try {
      PushLoginRequest200Response result = apiInstance.pushLoginRequest(paramCallback, pushToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoginApi#pushLoginRequest");
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
| **paramCallback** | **String**| URI App will connect to | |
| **pushToken** | [**PushToken**](PushToken.md)| Push Token. | |

### Return type

[**PushLoginRequest200Response**](PushLoginRequest200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **401** | Unauthorized for this callback audience &#x60;aud-error&#x60; or JWT should be self-signed &#x60;auth-error&#x60; |  -  |
| **0** | Error response |  -  |

