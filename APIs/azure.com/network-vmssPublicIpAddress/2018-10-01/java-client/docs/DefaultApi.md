# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**publicIPAddressesGetVirtualMachineScaleSetPublicIPAddress**](DefaultApi.md#publicIPAddressesGetVirtualMachineScaleSetPublicIPAddress) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines/{virtualmachineIndex}/networkInterfaces/{networkInterfaceName}/ipconfigurations/{ipConfigurationName}/publicipaddresses/{publicIpAddressName} |  |
| [**publicIPAddressesListVirtualMachineScaleSetPublicIPAddresses**](DefaultApi.md#publicIPAddressesListVirtualMachineScaleSetPublicIPAddresses) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/publicipaddresses |  |
| [**publicIPAddressesListVirtualMachineScaleSetVMPublicIPAddresses**](DefaultApi.md#publicIPAddressesListVirtualMachineScaleSetVMPublicIPAddresses) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines/{virtualmachineIndex}/networkInterfaces/{networkInterfaceName}/ipconfigurations/{ipConfigurationName}/publicipaddresses |  |


<a id="publicIPAddressesGetVirtualMachineScaleSetPublicIPAddress"></a>
# **publicIPAddressesGetVirtualMachineScaleSetPublicIPAddress**
> PublicIPAddressesGetVirtualMachineScaleSetPublicIPAddress200Response publicIPAddressesGetVirtualMachineScaleSetPublicIPAddress(resourceGroupName, virtualMachineScaleSetName, virtualmachineIndex, networkInterfaceName, ipConfigurationName, publicIpAddressName, apiVersion, subscriptionId, $expand)



Get the specified public IP address in a virtual machine scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualMachineScaleSetName = "virtualMachineScaleSetName_example"; // String | The name of the virtual machine scale set.
    String virtualmachineIndex = "virtualmachineIndex_example"; // String | The virtual machine index.
    String networkInterfaceName = "networkInterfaceName_example"; // String | The name of the network interface.
    String ipConfigurationName = "ipConfigurationName_example"; // String | The name of the IP configuration.
    String publicIpAddressName = "publicIpAddressName_example"; // String | The name of the public IP Address.
    String apiVersion = "2017-03-30"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $expand = "$expand_example"; // String | Expands referenced resources.
    try {
      PublicIPAddressesGetVirtualMachineScaleSetPublicIPAddress200Response result = apiInstance.publicIPAddressesGetVirtualMachineScaleSetPublicIPAddress(resourceGroupName, virtualMachineScaleSetName, virtualmachineIndex, networkInterfaceName, ipConfigurationName, publicIpAddressName, apiVersion, subscriptionId, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publicIPAddressesGetVirtualMachineScaleSetPublicIPAddress");
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
| **virtualMachineScaleSetName** | **String**| The name of the virtual machine scale set. | |
| **virtualmachineIndex** | **String**| The virtual machine index. | |
| **networkInterfaceName** | **String**| The name of the network interface. | |
| **ipConfigurationName** | **String**| The name of the IP configuration. | |
| **publicIpAddressName** | **String**| The name of the public IP Address. | |
| **apiVersion** | **String**| Client API version. | [enum: 2017-03-30] |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$expand** | **String**| Expands referenced resources. | [optional] |

### Return type

[**PublicIPAddressesGetVirtualMachineScaleSetPublicIPAddress200Response**](PublicIPAddressesGetVirtualMachineScaleSetPublicIPAddress200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting PublicIPAddress resource. |  -  |

<a id="publicIPAddressesListVirtualMachineScaleSetPublicIPAddresses"></a>
# **publicIPAddressesListVirtualMachineScaleSetPublicIPAddresses**
> PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response publicIPAddressesListVirtualMachineScaleSetPublicIPAddresses(resourceGroupName, virtualMachineScaleSetName, apiVersion, subscriptionId)



Gets information about all public IP addresses on a virtual machine scale set level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualMachineScaleSetName = "virtualMachineScaleSetName_example"; // String | The name of the virtual machine scale set.
    String apiVersion = "2017-03-30"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response result = apiInstance.publicIPAddressesListVirtualMachineScaleSetPublicIPAddresses(resourceGroupName, virtualMachineScaleSetName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publicIPAddressesListVirtualMachineScaleSetPublicIPAddresses");
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
| **virtualMachineScaleSetName** | **String**| The name of the virtual machine scale set. | |
| **apiVersion** | **String**| Client API version. | [enum: 2017-03-30] |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response**](PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of PublicIPInterface resources. |  -  |

<a id="publicIPAddressesListVirtualMachineScaleSetVMPublicIPAddresses"></a>
# **publicIPAddressesListVirtualMachineScaleSetVMPublicIPAddresses**
> PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response publicIPAddressesListVirtualMachineScaleSetVMPublicIPAddresses(resourceGroupName, virtualMachineScaleSetName, virtualmachineIndex, networkInterfaceName, ipConfigurationName, apiVersion, subscriptionId)



Gets information about all public IP addresses in a virtual machine IP configuration in a virtual machine scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualMachineScaleSetName = "virtualMachineScaleSetName_example"; // String | The name of the virtual machine scale set.
    String virtualmachineIndex = "virtualmachineIndex_example"; // String | The virtual machine index.
    String networkInterfaceName = "networkInterfaceName_example"; // String | The network interface name.
    String ipConfigurationName = "ipConfigurationName_example"; // String | The IP configuration name.
    String apiVersion = "2017-03-30"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response result = apiInstance.publicIPAddressesListVirtualMachineScaleSetVMPublicIPAddresses(resourceGroupName, virtualMachineScaleSetName, virtualmachineIndex, networkInterfaceName, ipConfigurationName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publicIPAddressesListVirtualMachineScaleSetVMPublicIPAddresses");
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
| **virtualMachineScaleSetName** | **String**| The name of the virtual machine scale set. | |
| **virtualmachineIndex** | **String**| The virtual machine index. | |
| **networkInterfaceName** | **String**| The network interface name. | |
| **ipConfigurationName** | **String**| The IP configuration name. | |
| **apiVersion** | **String**| Client API version. | [enum: 2017-03-30] |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response**](PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of PublicIPAddress resources. |  -  |

