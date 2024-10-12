# ExpressRouteCircuitRoutesTableApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expressRouteCircuitsListRoutesTable**](ExpressRouteCircuitRoutesTableApi.md#expressRouteCircuitsListRoutesTable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/routeTables/{devicePath} |  |


<a id="expressRouteCircuitsListRoutesTable"></a>
# **expressRouteCircuitsListRoutesTable**
> ExpressRouteCircuitsRoutesTableListResult expressRouteCircuitsListRoutesTable(resourceGroupName, circuitName, peeringName, devicePath, apiVersion, subscriptionId)



Gets the currently advertised routes table associated with the express route circuit in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitRoutesTableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitRoutesTableApi apiInstance = new ExpressRouteCircuitRoutesTableApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the express route circuit.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String devicePath = "devicePath_example"; // String | The path of the device.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteCircuitsRoutesTableListResult result = apiInstance.expressRouteCircuitsListRoutesTable(resourceGroupName, circuitName, peeringName, devicePath, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitRoutesTableApi#expressRouteCircuitsListRoutesTable");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **circuitName** | **String**| The name of the express route circuit. | |
| **peeringName** | **String**| The name of the peering. | |
| **devicePath** | **String**| The path of the device. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ExpressRouteCircuitsRoutesTableListResult**](ExpressRouteCircuitsRoutesTableListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting ExpressRouteCircuitsRouteTable resource. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

