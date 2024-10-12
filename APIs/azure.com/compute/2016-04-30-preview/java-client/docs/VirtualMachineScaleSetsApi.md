# VirtualMachineScaleSetsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualMachineScaleSetsCreateOrUpdate**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName} |  |
| [**virtualMachineScaleSetsDeallocate**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsDeallocate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/deallocate |  |
| [**virtualMachineScaleSetsDelete**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName} |  |
| [**virtualMachineScaleSetsDeleteInstances**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsDeleteInstances) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/delete |  |
| [**virtualMachineScaleSetsGet**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName} |  |
| [**virtualMachineScaleSetsGetInstanceView**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsGetInstanceView) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/instanceView |  |
| [**virtualMachineScaleSetsList**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets |  |
| [**virtualMachineScaleSetsListAll**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/virtualMachineScaleSets |  |
| [**virtualMachineScaleSetsListSkus**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsListSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/skus |  |
| [**virtualMachineScaleSetsPowerOff**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsPowerOff) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/poweroff |  |
| [**virtualMachineScaleSetsReimage**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsReimage) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/reimage |  |
| [**virtualMachineScaleSetsReimageAll**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsReimageAll) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/reimageall |  |
| [**virtualMachineScaleSetsRestart**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsRestart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/restart |  |
| [**virtualMachineScaleSetsStart**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/start |  |
| [**virtualMachineScaleSetsUpdateInstances**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsUpdateInstances) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/manualupgrade |  |


<a id="virtualMachineScaleSetsCreateOrUpdate"></a>
# **virtualMachineScaleSetsCreateOrUpdate**
> VirtualMachineScaleSet virtualMachineScaleSetsCreateOrUpdate(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, parameters)



Create or update a VM scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set to create or update.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualMachineScaleSet parameters = new VirtualMachineScaleSet(); // VirtualMachineScaleSet | The scale set object.
    try {
      VirtualMachineScaleSet result = apiInstance.virtualMachineScaleSetsCreateOrUpdate(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsCreateOrUpdate");
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
| **vmScaleSetName** | **String**| The name of the VM scale set to create or update. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**VirtualMachineScaleSet**](VirtualMachineScaleSet.md)| The scale set object. | |

### Return type

[**VirtualMachineScaleSet**](VirtualMachineScaleSet.md)

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

<a id="virtualMachineScaleSetsDeallocate"></a>
# **virtualMachineScaleSetsDeallocate**
> OperationStatusResponse virtualMachineScaleSetsDeallocate(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs)



Deallocates specific virtual machines in a VM scale set. Shuts down the virtual machines and releases the compute resources. You are not billed for the compute resources that this virtual machine scale set deallocates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualMachineScaleSetVMInstanceIDs vmInstanceIDs = new VirtualMachineScaleSetVMInstanceIDs(); // VirtualMachineScaleSetVMInstanceIDs | A list of virtual machine instance IDs from the VM scale set.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetsDeallocate(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsDeallocate");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceIDs**](VirtualMachineScaleSetVMInstanceIDs.md)| A list of virtual machine instance IDs from the VM scale set. | [optional] |

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="virtualMachineScaleSetsDelete"></a>
# **virtualMachineScaleSetsDelete**
> OperationStatusResponse virtualMachineScaleSetsDelete(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Deletes a VM scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetsDelete(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsDelete");
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

<a id="virtualMachineScaleSetsDeleteInstances"></a>
# **virtualMachineScaleSetsDeleteInstances**
> OperationStatusResponse virtualMachineScaleSetsDeleteInstances(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs)



Deletes virtual machines in a VM scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualMachineScaleSetVMInstanceRequiredIDs vmInstanceIDs = new VirtualMachineScaleSetVMInstanceRequiredIDs(); // VirtualMachineScaleSetVMInstanceRequiredIDs | A list of virtual machine instance IDs from the VM scale set.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetsDeleteInstances(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsDeleteInstances");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceRequiredIDs**](VirtualMachineScaleSetVMInstanceRequiredIDs.md)| A list of virtual machine instance IDs from the VM scale set. | |

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="virtualMachineScaleSetsGet"></a>
# **virtualMachineScaleSetsGet**
> VirtualMachineScaleSet virtualMachineScaleSetsGet(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Display information about a virtual machine scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualMachineScaleSet result = apiInstance.virtualMachineScaleSetsGet(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsGet");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualMachineScaleSet**](VirtualMachineScaleSet.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineScaleSetsGetInstanceView"></a>
# **virtualMachineScaleSetsGetInstanceView**
> VirtualMachineScaleSetInstanceView virtualMachineScaleSetsGetInstanceView(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Gets the status of a VM scale set instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualMachineScaleSetInstanceView result = apiInstance.virtualMachineScaleSetsGetInstanceView(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsGetInstanceView");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualMachineScaleSetInstanceView**](VirtualMachineScaleSetInstanceView.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineScaleSetsList"></a>
# **virtualMachineScaleSetsList**
> VirtualMachineScaleSetListResult virtualMachineScaleSetsList(resourceGroupName, apiVersion, subscriptionId)



Gets a list of all VM scale sets under a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualMachineScaleSetListResult result = apiInstance.virtualMachineScaleSetsList(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualMachineScaleSetListResult**](VirtualMachineScaleSetListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineScaleSetsListAll"></a>
# **virtualMachineScaleSetsListAll**
> VirtualMachineScaleSetListWithLinkResult virtualMachineScaleSetsListAll(apiVersion, subscriptionId)



Gets a list of all VM Scale Sets in the subscription, regardless of the associated resource group. Use nextLink property in the response to get the next page of VM Scale Sets. Do this till nextLink is null to fetch all the VM Scale Sets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualMachineScaleSetListWithLinkResult result = apiInstance.virtualMachineScaleSetsListAll(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsListAll");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualMachineScaleSetListWithLinkResult**](VirtualMachineScaleSetListWithLinkResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineScaleSetsListSkus"></a>
# **virtualMachineScaleSetsListSkus**
> VirtualMachineScaleSetListSkusResult virtualMachineScaleSetsListSkus(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Gets a list of SKUs available for your VM scale set, including the minimum and maximum VM instances allowed for each SKU.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualMachineScaleSetListSkusResult result = apiInstance.virtualMachineScaleSetsListSkus(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsListSkus");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualMachineScaleSetListSkusResult**](VirtualMachineScaleSetListSkusResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineScaleSetsPowerOff"></a>
# **virtualMachineScaleSetsPowerOff**
> OperationStatusResponse virtualMachineScaleSetsPowerOff(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs)



Power off (stop) one or more virtual machines in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualMachineScaleSetVMInstanceIDs vmInstanceIDs = new VirtualMachineScaleSetVMInstanceIDs(); // VirtualMachineScaleSetVMInstanceIDs | A list of virtual machine instance IDs from the VM scale set.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetsPowerOff(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsPowerOff");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceIDs**](VirtualMachineScaleSetVMInstanceIDs.md)| A list of virtual machine instance IDs from the VM scale set. | [optional] |

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="virtualMachineScaleSetsReimage"></a>
# **virtualMachineScaleSetsReimage**
> OperationStatusResponse virtualMachineScaleSetsReimage(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Reimages (upgrade the operating system) one or more virtual machines in a VM scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetsReimage(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsReimage");
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

<a id="virtualMachineScaleSetsReimageAll"></a>
# **virtualMachineScaleSetsReimageAll**
> OperationStatusResponse virtualMachineScaleSetsReimageAll(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Reimages all the disks ( including data disks ) in the virtual machines in a VM scale set. This operation is only supported for managed disks.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetsReimageAll(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsReimageAll");
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

<a id="virtualMachineScaleSetsRestart"></a>
# **virtualMachineScaleSetsRestart**
> OperationStatusResponse virtualMachineScaleSetsRestart(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs)



Restarts one or more virtual machines in a VM scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualMachineScaleSetVMInstanceIDs vmInstanceIDs = new VirtualMachineScaleSetVMInstanceIDs(); // VirtualMachineScaleSetVMInstanceIDs | A list of virtual machine instance IDs from the VM scale set.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetsRestart(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsRestart");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceIDs**](VirtualMachineScaleSetVMInstanceIDs.md)| A list of virtual machine instance IDs from the VM scale set. | [optional] |

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="virtualMachineScaleSetsStart"></a>
# **virtualMachineScaleSetsStart**
> OperationStatusResponse virtualMachineScaleSetsStart(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs)



Starts one or more virtual machines in a VM scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualMachineScaleSetVMInstanceIDs vmInstanceIDs = new VirtualMachineScaleSetVMInstanceIDs(); // VirtualMachineScaleSetVMInstanceIDs | A list of virtual machine instance IDs from the VM scale set.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetsStart(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsStart");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceIDs**](VirtualMachineScaleSetVMInstanceIDs.md)| A list of virtual machine instance IDs from the VM scale set. | [optional] |

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="virtualMachineScaleSetsUpdateInstances"></a>
# **virtualMachineScaleSetsUpdateInstances**
> OperationStatusResponse virtualMachineScaleSetsUpdateInstances(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs)



Upgrades one or more virtual machines to the latest SKU set in the VM scale set model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetsApi apiInstance = new VirtualMachineScaleSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualMachineScaleSetVMInstanceRequiredIDs vmInstanceIDs = new VirtualMachineScaleSetVMInstanceRequiredIDs(); // VirtualMachineScaleSetVMInstanceRequiredIDs | A list of virtual machine instance IDs from the VM scale set.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetsUpdateInstances(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetsApi#virtualMachineScaleSetsUpdateInstances");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceRequiredIDs**](VirtualMachineScaleSetVMInstanceRequiredIDs.md)| A list of virtual machine instance IDs from the VM scale set. | |

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

