# MonitoringApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05HeartbeatGet**](MonitoringApi.md#v05HeartbeatGet) | **GET** /v0.5/heartbeat | Get consent request status |


<a id="v05HeartbeatGet"></a>
# **v05HeartbeatGet**
> HeartbeatResponse v05HeartbeatGet()

Get consent request status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/cm");

    MonitoringApi apiInstance = new MonitoringApi(defaultClient);
    try {
      HeartbeatResponse result = apiInstance.v05HeartbeatGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitoringApi#v05HeartbeatGet");
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

[**HeartbeatResponse**](HeartbeatResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

