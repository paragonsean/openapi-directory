# StatusApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**none**](StatusApi.md#none) | **GET** /status | Check if Rudder is alive |


<a id="none"></a>
# **none**
> String none()

Check if Rudder is alive

An unauthenticated API to check if Rudder web application is up and running. Be careful: this API does not follow other Rudder&#39;s API convention:  - it is not versioned, so the path is just &#x60;/api/status&#x60;; - it returns a plain text message.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");

    StatusApi apiInstance = new StatusApi(defaultClient);
    try {
      String result = apiInstance.none();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#none");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK status message |  -  |

