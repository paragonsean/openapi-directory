# VirtualMachineScaleSetVmsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualMachineScaleSetVMsDeallocate**](VirtualMachineScaleSetVmsApi.md#virtualMachineScaleSetVMsDeallocate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualmachines/{instanceId}/deallocate |  |
| [**virtualMachineScaleSetVMsDelete**](VirtualMachineScaleSetVmsApi.md#virtualMachineScaleSetVMsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualmachines/{instanceId} |  |
| [**virtualMachineScaleSetVMsGet**](VirtualMachineScaleSetVmsApi.md#virtualMachineScaleSetVMsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualmachines/{instanceId} |  |
| [**virtualMachineScaleSetVMsGetInstanceView**](VirtualMachineScaleSetVmsApi.md#virtualMachineScaleSetVMsGetInstanceView) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualmachines/{instanceId}/instanceView |  |
| [**virtualMachineScaleSetVMsList**](VirtualMachineScaleSetVmsApi.md#virtualMachineScaleSetVMsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines |  |
| [**virtualMachineScaleSetVMsPowerOff**](VirtualMachineScaleSetVmsApi.md#virtualMachineScaleSetVMsPowerOff) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualmachines/{instanceId}/poweroff |  |
| [**virtualMachineScaleSetVMsReimage**](VirtualMachineScaleSetVmsApi.md#virtualMachineScaleSetVMsReimage) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualmachines/{instanceId}/reimage |  |
| [**virtualMachineScaleSetVMsRestart**](VirtualMachineScaleSetVmsApi.md#virtualMachineScaleSetVMsRestart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualmachines/{instanceId}/restart |  |
| [**virtualMachineScaleSetVMsStart**](VirtualMachineScaleSetVmsApi.md#virtualMachineScaleSetVMsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualmachines/{instanceId}/start |  |


<a id="virtualMachineScaleSetVMsDeallocate"></a>
# **virtualMachineScaleSetVMsDeallocate**
> OperationStatusResponse virtualMachineScaleSetVMsDeallocate(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId)



Deallocates a specific virtual machine in a VM scale set. Shuts down the virtual machine and releases the compute resources it uses. You are not billed for the compute resources of this virtual machine once it is deallocated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetVmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetVmsApi apiInstance = new VirtualMachineScaleSetVmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetVMsDeallocate(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetVmsApi#virtualMachineScaleSetVMsDeallocate");
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

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

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

<a id="virtualMachineScaleSetVMsDelete"></a>
# **virtualMachineScaleSetVMsDelete**
> OperationStatusResponse virtualMachineScaleSetVMsDelete(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId)



Deletes a virtual machine from a VM scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetVmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetVmsApi apiInstance = new VirtualMachineScaleSetVmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetVMsDelete(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetVmsApi#virtualMachineScaleSetVMsDelete");
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

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

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

<a id="virtualMachineScaleSetVMsGet"></a>
# **virtualMachineScaleSetVMsGet**
> VirtualMachineScaleSetVM virtualMachineScaleSetVMsGet(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId)



Gets a virtual machine from a VM scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetVmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetVmsApi apiInstance = new VirtualMachineScaleSetVmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualMachineScaleSetVM result = apiInstance.virtualMachineScaleSetVMsGet(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetVmsApi#virtualMachineScaleSetVMsGet");
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

### Return type

[**VirtualMachineScaleSetVM**](VirtualMachineScaleSetVM.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineScaleSetVMsGetInstanceView"></a>
# **virtualMachineScaleSetVMsGetInstanceView**
> VirtualMachineScaleSetVMInstanceView virtualMachineScaleSetVMsGetInstanceView(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId)



Gets the status of a virtual machine from a VM scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetVmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetVmsApi apiInstance = new VirtualMachineScaleSetVmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualMachineScaleSetVMInstanceView result = apiInstance.virtualMachineScaleSetVMsGetInstanceView(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetVmsApi#virtualMachineScaleSetVMsGetInstanceView");
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

### Return type

[**VirtualMachineScaleSetVMInstanceView**](VirtualMachineScaleSetVMInstanceView.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineScaleSetVMsList"></a>
# **virtualMachineScaleSetVMsList**
> VirtualMachineScaleSetVMListResult virtualMachineScaleSetVMsList(resourceGroupName, virtualMachineScaleSetName, apiVersion, subscriptionId, $filter, $select, $expand)



Gets a list of all virtual machines in a VM scale sets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetVmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetVmsApi apiInstance = new VirtualMachineScaleSetVmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualMachineScaleSetName = "virtualMachineScaleSetName_example"; // String | The name of the VM scale set.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | The filter to apply to the operation.
    String $select = "$select_example"; // String | The list parameters.
    String $expand = "$expand_example"; // String | The expand expression to apply to the operation.
    try {
      VirtualMachineScaleSetVMListResult result = apiInstance.virtualMachineScaleSetVMsList(resourceGroupName, virtualMachineScaleSetName, apiVersion, subscriptionId, $filter, $select, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetVmsApi#virtualMachineScaleSetVMsList");
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
| **virtualMachineScaleSetName** | **String**| The name of the VM scale set. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$filter** | **String**| The filter to apply to the operation. | [optional] |
| **$select** | **String**| The list parameters. | [optional] |
| **$expand** | **String**| The expand expression to apply to the operation. | [optional] |

### Return type

[**VirtualMachineScaleSetVMListResult**](VirtualMachineScaleSetVMListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineScaleSetVMsPowerOff"></a>
# **virtualMachineScaleSetVMsPowerOff**
> OperationStatusResponse virtualMachineScaleSetVMsPowerOff(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId)



Power off (stop) a virtual machine in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetVmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetVmsApi apiInstance = new VirtualMachineScaleSetVmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetVMsPowerOff(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetVmsApi#virtualMachineScaleSetVMsPowerOff");
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

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

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

<a id="virtualMachineScaleSetVMsReimage"></a>
# **virtualMachineScaleSetVMsReimage**
> OperationStatusResponse virtualMachineScaleSetVMsReimage(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId)



Reimages (upgrade the operating system) a specific virtual machine in a VM scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetVmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetVmsApi apiInstance = new VirtualMachineScaleSetVmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetVMsReimage(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetVmsApi#virtualMachineScaleSetVMsReimage");
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

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

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

<a id="virtualMachineScaleSetVMsRestart"></a>
# **virtualMachineScaleSetVMsRestart**
> OperationStatusResponse virtualMachineScaleSetVMsRestart(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId)



Restarts a virtual machine in a VM scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetVmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetVmsApi apiInstance = new VirtualMachineScaleSetVmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetVMsRestart(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetVmsApi#virtualMachineScaleSetVMsRestart");
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

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

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

<a id="virtualMachineScaleSetVMsStart"></a>
# **virtualMachineScaleSetVMsStart**
> OperationStatusResponse virtualMachineScaleSetVMsStart(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId)



Starts a virtual machine in a VM scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetVmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetVmsApi apiInstance = new VirtualMachineScaleSetVmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetVMsStart(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetVmsApi#virtualMachineScaleSetVMsStart");
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

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

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

