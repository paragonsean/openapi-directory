# HealthApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**healthApiV1HealthGet**](HealthApi.md#healthApiV1HealthGet) | **GET** /api/v1/health/ | Health |


<a id="healthApiV1HealthGet"></a>
# **healthApiV1HealthGet**
> healthApiV1HealthGet(idempotencyKey)

Health

Verify the API server is up and running.

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
    defaultClient.setBasePath("http://localhost");

    HealthApi apiInstance = new HealthApi(defaultClient);
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      apiInstance.healthApiV1HealthGet(idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#healthApiV1HealthGet");
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
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful Response |  -  |
| **422** | Validation Error |  -  |

