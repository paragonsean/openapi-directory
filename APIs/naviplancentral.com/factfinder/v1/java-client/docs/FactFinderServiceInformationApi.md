# FactFinderServiceInformationApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**factFinderServiceInformationGet**](FactFinderServiceInformationApi.md#factFinderServiceInformationGet) | **GET** /api/ServiceInformation |  |


<a id="factFinderServiceInformationGet"></a>
# **factFinderServiceInformationGet**
> ServiceInformationModel factFinderServiceInformationGet()



Description: This operation retrieves information statistics for the current service.&lt;br /&gt;                Purpose: Provides access to Service Information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactFinderServiceInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FactFinderServiceInformationApi apiInstance = new FactFinderServiceInformationApi(defaultClient);
    try {
      ServiceInformationModel result = apiInstance.factFinderServiceInformationGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactFinderServiceInformationApi#factFinderServiceInformationGet");
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

[**ServiceInformationModel**](ServiceInformationModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Object not found. |  -  |

