# BaselineApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metricBaselineCalculateBaseline**](BaselineApi.md#metricBaselineCalculateBaseline) | **POST** /{resourceUri}/providers/microsoft.insights/calculatebaseline |  |


<a id="metricBaselineCalculateBaseline"></a>
# **metricBaselineCalculateBaseline**
> CalculateBaselineResponse metricBaselineCalculateBaseline(resourceUri, apiVersion, timeSeriesInformation)



**Lists the baseline values for a resource**.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BaselineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BaselineApi apiInstance = new BaselineApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The identifier of the resource. It has the following structure: subscriptions/{subscriptionName}/resourceGroups/{resourceGroupName}/providers/{providerName}/{resourceName}. For example: subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/vms/providers/Microsoft.Compute/virtualMachines/vm1
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    TimeSeriesInformation timeSeriesInformation = new TimeSeriesInformation(); // TimeSeriesInformation | Information that need to be specified to calculate a baseline on a time series.
    try {
      CalculateBaselineResponse result = apiInstance.metricBaselineCalculateBaseline(resourceUri, apiVersion, timeSeriesInformation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BaselineApi#metricBaselineCalculateBaseline");
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
| **resourceUri** | **String**| The identifier of the resource. It has the following structure: subscriptions/{subscriptionName}/resourceGroups/{resourceGroupName}/providers/{providerName}/{resourceName}. For example: subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/vms/providers/Microsoft.Compute/virtualMachines/vm1 | |
| **apiVersion** | **String**| Client Api Version. | |
| **timeSeriesInformation** | [**TimeSeriesInformation**](TimeSeriesInformation.md)| Information that need to be specified to calculate a baseline on a time series. | |

### Return type

[**CalculateBaselineResponse**](CalculateBaselineResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get the list of metric values. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

