# TokensApi

All URIs are relative to *https://control.ably.net/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**meGet**](TokensApi.md#meGet) | **GET** /me | Get token details |


<a id="meGet"></a>
# **meGet**
> Me meGet()

Get token details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    TokensApi apiInstance = new TokensApi(defaultClient);
    try {
      Me result = apiInstance.meGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokensApi#meGet");
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

[**Me**](Me.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Token details |  -  |
| **401** | Authentication failed |  -  |
| **500** | Internal server error |  -  |

