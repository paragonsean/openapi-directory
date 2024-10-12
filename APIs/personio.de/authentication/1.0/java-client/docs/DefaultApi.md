# DefaultApi

All URIs are relative to *https://api.personio.de/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authPost**](DefaultApi.md#authPost) | **POST** /auth |  |


<a id="authPost"></a>
# **authPost**
> AuthenticationTokenResponse authPost(clientId, clientSecret)



Request Authentication Token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.personio.de/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String clientId = "clientId_example"; // String | Client id of the downloaded credentials file
    String clientSecret = "clientSecret_example"; // String | Client secret of the downloaded credentials file
    try {
      AuthenticationTokenResponse result = apiInstance.authPost(clientId, clientSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#authPost");
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
| **clientId** | **String**| Client id of the downloaded credentials file | |
| **clientSecret** | **String**| Client secret of the downloaded credentials file | |

### Return type

[**AuthenticationTokenResponse**](AuthenticationTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

