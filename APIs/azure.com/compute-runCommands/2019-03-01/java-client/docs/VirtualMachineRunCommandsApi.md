# VirtualMachineRunCommandsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualMachineRunCommandsGet**](VirtualMachineRunCommandsApi.md#virtualMachineRunCommandsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/runCommands/{commandId} |  |
| [**virtualMachineRunCommandsList**](VirtualMachineRunCommandsApi.md#virtualMachineRunCommandsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/runCommands |  |


<a id="virtualMachineRunCommandsGet"></a>
# **virtualMachineRunCommandsGet**
> RunCommandDocument virtualMachineRunCommandsGet(location, commandId, apiVersion, subscriptionId)



Gets specific run command for a subscription in a location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineRunCommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineRunCommandsApi apiInstance = new VirtualMachineRunCommandsApi(defaultClient);
    String location = "location_example"; // String | The location upon which run commands is queried.
    String commandId = "commandId_example"; // String | The command id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      RunCommandDocument result = apiInstance.virtualMachineRunCommandsGet(location, commandId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineRunCommandsApi#virtualMachineRunCommandsGet");
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
| **location** | **String**| The location upon which run commands is queried. | |
| **commandId** | **String**| The command id. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**RunCommandDocument**](RunCommandDocument.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineRunCommandsList"></a>
# **virtualMachineRunCommandsList**
> RunCommandListResult virtualMachineRunCommandsList(location, apiVersion, subscriptionId)



Lists all available run commands for a subscription in a location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineRunCommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineRunCommandsApi apiInstance = new VirtualMachineRunCommandsApi(defaultClient);
    String location = "location_example"; // String | The location upon which run commands is queried.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      RunCommandListResult result = apiInstance.virtualMachineRunCommandsList(location, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineRunCommandsApi#virtualMachineRunCommandsList");
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
| **location** | **String**| The location upon which run commands is queried. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**RunCommandListResult**](RunCommandListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

