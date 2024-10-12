# IndustriesApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**industriesGet**](IndustriesApi.md#industriesGet) | **GET** /industries |  |


<a id="industriesGet"></a>
# **industriesGet**
> EndpointGetIndustries industriesGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndustriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    IndustriesApi apiInstance = new IndustriesApi(defaultClient);
    try {
      EndpointGetIndustries result = apiInstance.industriesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndustriesApi#industriesGet");
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

[**EndpointGetIndustries**](EndpointGetIndustries.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

