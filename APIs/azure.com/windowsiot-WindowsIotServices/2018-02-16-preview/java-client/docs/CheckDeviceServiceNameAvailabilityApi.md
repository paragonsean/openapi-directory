# CheckDeviceServiceNameAvailabilityApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicesCheckDeviceServiceNameAvailability**](CheckDeviceServiceNameAvailabilityApi.md#servicesCheckDeviceServiceNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.WindowsIoT/checkDeviceServiceNameAvailability |  |


<a id="servicesCheckDeviceServiceNameAvailability"></a>
# **servicesCheckDeviceServiceNameAvailability**
> DeviceServiceNameAvailabilityInfo servicesCheckDeviceServiceNameAvailability(apiVersion, subscriptionId, deviceServiceCheckNameAvailabilityParameters)



Check if a Windows IoT Device Service name is available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckDeviceServiceNameAvailabilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CheckDeviceServiceNameAvailabilityApi apiInstance = new CheckDeviceServiceNameAvailabilityApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    DeviceServiceCheckNameAvailabilityParameters deviceServiceCheckNameAvailabilityParameters = new DeviceServiceCheckNameAvailabilityParameters(); // DeviceServiceCheckNameAvailabilityParameters | Set the name parameter in the DeviceServiceCheckNameAvailabilityParameters structure to the name of the Windows IoT Device Service to check.
    try {
      DeviceServiceNameAvailabilityInfo result = apiInstance.servicesCheckDeviceServiceNameAvailability(apiVersion, subscriptionId, deviceServiceCheckNameAvailabilityParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckDeviceServiceNameAvailabilityApi#servicesCheckDeviceServiceNameAvailability");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **deviceServiceCheckNameAvailabilityParameters** | [**DeviceServiceCheckNameAvailabilityParameters**](DeviceServiceCheckNameAvailabilityParameters.md)| Set the name parameter in the DeviceServiceCheckNameAvailabilityParameters structure to the name of the Windows IoT Device Service to check. | |

### Return type

[**DeviceServiceNameAvailabilityInfo**](DeviceServiceNameAvailabilityInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | DefaultErrorResponse |  -  |

