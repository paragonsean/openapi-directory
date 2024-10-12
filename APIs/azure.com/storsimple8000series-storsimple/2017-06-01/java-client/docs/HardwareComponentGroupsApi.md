# HardwareComponentGroupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hardwareComponentGroupsChangeControllerPowerState**](HardwareComponentGroupsApi.md#hardwareComponentGroupsChangeControllerPowerState) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/hardwareComponentGroups/{hardwareComponentGroupName}/changeControllerPowerState |  |
| [**hardwareComponentGroupsListByDevice**](HardwareComponentGroupsApi.md#hardwareComponentGroupsListByDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/hardwareComponentGroups |  |


<a id="hardwareComponentGroupsChangeControllerPowerState"></a>
# **hardwareComponentGroupsChangeControllerPowerState**
> hardwareComponentGroupsChangeControllerPowerState(deviceName, hardwareComponentGroupName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters)



Changes the power state of the controller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HardwareComponentGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HardwareComponentGroupsApi apiInstance = new HardwareComponentGroupsApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name
    String hardwareComponentGroupName = "hardwareComponentGroupName_example"; // String | The hardware component group name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    ControllerPowerStateChangeRequest parameters = new ControllerPowerStateChangeRequest(); // ControllerPowerStateChangeRequest | The controller power state change request.
    try {
      apiInstance.hardwareComponentGroupsChangeControllerPowerState(deviceName, hardwareComponentGroupName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling HardwareComponentGroupsApi#hardwareComponentGroupsChangeControllerPowerState");
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
| **deviceName** | **String**| The device name | |
| **hardwareComponentGroupName** | **String**| The hardware component group name. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |
| **parameters** | [**ControllerPowerStateChangeRequest**](ControllerPowerStateChangeRequest.md)| The controller power state change request. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted the request to change power state of the controller. |  -  |
| **204** | Successfully changed the power state of the controller. |  -  |

<a id="hardwareComponentGroupsListByDevice"></a>
# **hardwareComponentGroupsListByDevice**
> HardwareComponentGroupList hardwareComponentGroupsListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion)



Lists the hardware component groups at device-level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HardwareComponentGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HardwareComponentGroupsApi apiInstance = new HardwareComponentGroupsApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      HardwareComponentGroupList result = apiInstance.hardwareComponentGroupsListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HardwareComponentGroupsApi#hardwareComponentGroupsListByDevice");
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
| **deviceName** | **String**| The device name | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

### Return type

[**HardwareComponentGroupList**](HardwareComponentGroupList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully fetched hardware component groups. |  -  |

