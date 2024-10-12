# ApiApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTest**](ApiApi.md#apiTest) | **GET** /api.test |  |


<a id="apiTest"></a>
# **apiTest**
> ApiTestSuccessSchema apiTest(error, foo)



Checks API calling code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ApiApi apiInstance = new ApiApi(defaultClient);
    String error = "error_example"; // String | Error response to return
    String foo = "foo_example"; // String | example property to return
    try {
      ApiTestSuccessSchema result = apiInstance.apiTest(error, foo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#apiTest");
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
| **error** | **String**| Error response to return | [optional] |
| **foo** | **String**| example property to return | [optional] |

### Return type

[**ApiTestSuccessSchema**](ApiTestSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Standard success response |  -  |
| **0** | Artificial error response |  -  |

