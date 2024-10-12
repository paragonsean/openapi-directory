# HealthApi

All URIs are relative to *http://otoroshi-api.oto.tools*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**health**](HealthApi.md#health) | **GET** /health | Return current Otoroshi health |


<a id="health"></a>
# **health**
> OtoroshiHealth health()

Return current Otoroshi health

Import the full state of Otoroshi as a file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      OtoroshiHealth result = apiInstance.health();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#health");
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

[**OtoroshiHealth**](OtoroshiHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **404** | Resource not found or does not exist |  -  |

