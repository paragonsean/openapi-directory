# VirtualMachineScaleSetVmExtensionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualMachineScaleSetVMExtensionsCreateOrUpdate**](VirtualMachineScaleSetVmExtensionsApi.md#virtualMachineScaleSetVMExtensionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName} |  |
| [**virtualMachineScaleSetVMExtensionsDelete**](VirtualMachineScaleSetVmExtensionsApi.md#virtualMachineScaleSetVMExtensionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName} |  |
| [**virtualMachineScaleSetVMExtensionsGet**](VirtualMachineScaleSetVmExtensionsApi.md#virtualMachineScaleSetVMExtensionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName} |  |
| [**virtualMachineScaleSetVMExtensionsList**](VirtualMachineScaleSetVmExtensionsApi.md#virtualMachineScaleSetVMExtensionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions |  |
| [**virtualMachineScaleSetVMExtensionsUpdate**](VirtualMachineScaleSetVmExtensionsApi.md#virtualMachineScaleSetVMExtensionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName} |  |


<a id="virtualMachineScaleSetVMExtensionsCreateOrUpdate"></a>
# **virtualMachineScaleSetVMExtensionsCreateOrUpdate**
> VirtualMachineExtension virtualMachineScaleSetVMExtensionsCreateOrUpdate(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId, extensionParameters)



The operation to create or update the VMSS VM extension.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetVmExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetVmExtensionsApi apiInstance = new VirtualMachineScaleSetVmExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
    String vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualMachineExtension extensionParameters = new VirtualMachineExtension(); // VirtualMachineExtension | Parameters supplied to the Create Virtual Machine Extension operation.
    try {
      VirtualMachineExtension result = apiInstance.virtualMachineScaleSetVMExtensionsCreateOrUpdate(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId, extensionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetVmExtensionsApi#virtualMachineScaleSetVMExtensionsCreateOrUpdate");
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
| **vmScaleSetName** | **String**| The name of the VM scale set. | |
| **instanceId** | **String**| The instance ID of the virtual machine. | |
| **vmExtensionName** | **String**| The name of the virtual machine extension. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **extensionParameters** | [**VirtualMachineExtension**](VirtualMachineExtension.md)| Parameters supplied to the Create Virtual Machine Extension operation. | |

### Return type

[**VirtualMachineExtension**](VirtualMachineExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualMachineScaleSetVMExtensionsDelete"></a>
# **virtualMachineScaleSetVMExtensionsDelete**
> virtualMachineScaleSetVMExtensionsDelete(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId)



The operation to delete the VMSS VM extension.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetVmExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetVmExtensionsApi apiInstance = new VirtualMachineScaleSetVmExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
    String vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.virtualMachineScaleSetVMExtensionsDelete(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetVmExtensionsApi#virtualMachineScaleSetVMExtensionsDelete");
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
| **vmScaleSetName** | **String**| The name of the VM scale set. | |
| **instanceId** | **String**| The instance ID of the virtual machine. | |
| **vmExtensionName** | **String**| The name of the virtual machine extension. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualMachineScaleSetVMExtensionsGet"></a>
# **virtualMachineScaleSetVMExtensionsGet**
> VirtualMachineExtension virtualMachineScaleSetVMExtensionsGet(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId, $expand)



The operation to get the VMSS VM extension.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetVmExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetVmExtensionsApi apiInstance = new VirtualMachineScaleSetVmExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
    String vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $expand = "$expand_example"; // String | The expand expression to apply on the operation.
    try {
      VirtualMachineExtension result = apiInstance.virtualMachineScaleSetVMExtensionsGet(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetVmExtensionsApi#virtualMachineScaleSetVMExtensionsGet");
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
| **vmScaleSetName** | **String**| The name of the VM scale set. | |
| **instanceId** | **String**| The instance ID of the virtual machine. | |
| **vmExtensionName** | **String**| The name of the virtual machine extension. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$expand** | **String**| The expand expression to apply on the operation. | [optional] |

### Return type

[**VirtualMachineExtension**](VirtualMachineExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualMachineScaleSetVMExtensionsList"></a>
# **virtualMachineScaleSetVMExtensionsList**
> VirtualMachineExtensionsListResult virtualMachineScaleSetVMExtensionsList(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId, $expand)



The operation to get all extensions of an instance in Virtual Machine Scaleset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetVmExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetVmExtensionsApi apiInstance = new VirtualMachineScaleSetVmExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $expand = "$expand_example"; // String | The expand expression to apply on the operation.
    try {
      VirtualMachineExtensionsListResult result = apiInstance.virtualMachineScaleSetVMExtensionsList(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetVmExtensionsApi#virtualMachineScaleSetVMExtensionsList");
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
| **vmScaleSetName** | **String**| The name of the VM scale set. | |
| **instanceId** | **String**| The instance ID of the virtual machine. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$expand** | **String**| The expand expression to apply on the operation. | [optional] |

### Return type

[**VirtualMachineExtensionsListResult**](VirtualMachineExtensionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualMachineScaleSetVMExtensionsUpdate"></a>
# **virtualMachineScaleSetVMExtensionsUpdate**
> VirtualMachineExtension virtualMachineScaleSetVMExtensionsUpdate(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId, extensionParameters)



The operation to update the VMSS VM extension.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetVmExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetVmExtensionsApi apiInstance = new VirtualMachineScaleSetVmExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
    String vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualMachineExtensionUpdate extensionParameters = new VirtualMachineExtensionUpdate(); // VirtualMachineExtensionUpdate | Parameters supplied to the Update Virtual Machine Extension operation.
    try {
      VirtualMachineExtension result = apiInstance.virtualMachineScaleSetVMExtensionsUpdate(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId, extensionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetVmExtensionsApi#virtualMachineScaleSetVMExtensionsUpdate");
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
| **vmScaleSetName** | **String**| The name of the VM scale set. | |
| **instanceId** | **String**| The instance ID of the virtual machine. | |
| **vmExtensionName** | **String**| The name of the virtual machine extension. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **extensionParameters** | [**VirtualMachineExtensionUpdate**](VirtualMachineExtensionUpdate.md)| Parameters supplied to the Update Virtual Machine Extension operation. | |

### Return type

[**VirtualMachineExtension**](VirtualMachineExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

