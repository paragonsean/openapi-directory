# Api20100401HealthCheckApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchHealthCheck**](Api20100401HealthCheckApi.md#fetchHealthCheck) | **GET** /healthcheck |  |


<a id="fetchHealthCheck"></a>
# **fetchHealthCheck**
> FetchHealthCheck200Response fetchHealthCheck()



API HealthCheck

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401HealthCheckApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");

    Api20100401HealthCheckApi apiInstance = new Api20100401HealthCheckApi(defaultClient);
    try {
      FetchHealthCheck200Response result = apiInstance.fetchHealthCheck();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401HealthCheckApi#fetchHealthCheck");
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

[**FetchHealthCheck200Response**](FetchHealthCheck200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

