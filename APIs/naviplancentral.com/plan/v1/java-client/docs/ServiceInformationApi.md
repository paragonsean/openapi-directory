# ServiceInformationApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serviceInformationStatistics**](ServiceInformationApi.md#serviceInformationStatistics) | **GET** /api/ServiceInformation/Statistics | This resource can be used to check the status of the service. |


<a id="serviceInformationStatistics"></a>
# **serviceInformationStatistics**
> ServiceInformation serviceInformationStatistics()

This resource can be used to check the status of the service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    ServiceInformationApi apiInstance = new ServiceInformationApi(defaultClient);
    try {
      ServiceInformation result = apiInstance.serviceInformationStatistics();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceInformationApi#serviceInformationStatistics");
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

[**ServiceInformation**](ServiceInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Provides additional information about the service. |  -  |

