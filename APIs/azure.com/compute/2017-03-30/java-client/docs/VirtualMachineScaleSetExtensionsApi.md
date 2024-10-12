# VirtualMachineScaleSetExtensionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualMachineScaleSetExtensionsCreateOrUpdate**](VirtualMachineScaleSetExtensionsApi.md#virtualMachineScaleSetExtensionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName} |  |
| [**virtualMachineScaleSetExtensionsDelete**](VirtualMachineScaleSetExtensionsApi.md#virtualMachineScaleSetExtensionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName} |  |
| [**virtualMachineScaleSetExtensionsGet**](VirtualMachineScaleSetExtensionsApi.md#virtualMachineScaleSetExtensionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName} |  |
| [**virtualMachineScaleSetExtensionsList**](VirtualMachineScaleSetExtensionsApi.md#virtualMachineScaleSetExtensionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions |  |


<a id="virtualMachineScaleSetExtensionsCreateOrUpdate"></a>
# **virtualMachineScaleSetExtensionsCreateOrUpdate**
> VirtualMachineScaleSetExtension virtualMachineScaleSetExtensionsCreateOrUpdate(resourceGroupName, vmScaleSetName, vmssExtensionName, apiVersion, subscriptionId, extensionParameters)



The operation to create or update an extension.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetExtensionsApi apiInstance = new VirtualMachineScaleSetExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set where the extension should be create or updated.
    String vmssExtensionName = "vmssExtensionName_example"; // String | The name of the VM scale set extension.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualMachineScaleSetExtension extensionParameters = new VirtualMachineScaleSetExtension(); // VirtualMachineScaleSetExtension | Parameters supplied to the Create VM scale set Extension operation.
    try {
      VirtualMachineScaleSetExtension result = apiInstance.virtualMachineScaleSetExtensionsCreateOrUpdate(resourceGroupName, vmScaleSetName, vmssExtensionName, apiVersion, subscriptionId, extensionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetExtensionsApi#virtualMachineScaleSetExtensionsCreateOrUpdate");
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
| **vmScaleSetName** | **String**| The name of the VM scale set where the extension should be create or updated. | |
| **vmssExtensionName** | **String**| The name of the VM scale set extension. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **extensionParameters** | [**VirtualMachineScaleSetExtension**](VirtualMachineScaleSetExtension.md)| Parameters supplied to the Create VM scale set Extension operation. | |

### Return type

[**VirtualMachineScaleSetExtension**](VirtualMachineScaleSetExtension.md)

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

<a id="virtualMachineScaleSetExtensionsDelete"></a>
# **virtualMachineScaleSetExtensionsDelete**
> OperationStatusResponse virtualMachineScaleSetExtensionsDelete(resourceGroupName, vmScaleSetName, vmssExtensionName, apiVersion, subscriptionId)



The operation to delete the extension.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetExtensionsApi apiInstance = new VirtualMachineScaleSetExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set where the extension should be deleted.
    String vmssExtensionName = "vmssExtensionName_example"; // String | The name of the VM scale set extension.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineScaleSetExtensionsDelete(resourceGroupName, vmScaleSetName, vmssExtensionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetExtensionsApi#virtualMachineScaleSetExtensionsDelete");
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
| **vmScaleSetName** | **String**| The name of the VM scale set where the extension should be deleted. | |
| **vmssExtensionName** | **String**| The name of the VM scale set extension. | |
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

<a id="virtualMachineScaleSetExtensionsGet"></a>
# **virtualMachineScaleSetExtensionsGet**
> VirtualMachineScaleSetExtension virtualMachineScaleSetExtensionsGet(resourceGroupName, vmScaleSetName, vmssExtensionName, apiVersion, subscriptionId, $expand)



The operation to get the extension.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetExtensionsApi apiInstance = new VirtualMachineScaleSetExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set containing the extension.
    String vmssExtensionName = "vmssExtensionName_example"; // String | The name of the VM scale set extension.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $expand = "$expand_example"; // String | The expand expression to apply on the operation.
    try {
      VirtualMachineScaleSetExtension result = apiInstance.virtualMachineScaleSetExtensionsGet(resourceGroupName, vmScaleSetName, vmssExtensionName, apiVersion, subscriptionId, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetExtensionsApi#virtualMachineScaleSetExtensionsGet");
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
| **vmScaleSetName** | **String**| The name of the VM scale set containing the extension. | |
| **vmssExtensionName** | **String**| The name of the VM scale set extension. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$expand** | **String**| The expand expression to apply on the operation. | [optional] |

### Return type

[**VirtualMachineScaleSetExtension**](VirtualMachineScaleSetExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineScaleSetExtensionsList"></a>
# **virtualMachineScaleSetExtensionsList**
> VirtualMachineScaleSetExtensionListResult virtualMachineScaleSetExtensionsList(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Gets a list of all extensions in a VM scale set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineScaleSetExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineScaleSetExtensionsApi apiInstance = new VirtualMachineScaleSetExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set containing the extension.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualMachineScaleSetExtensionListResult result = apiInstance.virtualMachineScaleSetExtensionsList(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineScaleSetExtensionsApi#virtualMachineScaleSetExtensionsList");
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
| **vmScaleSetName** | **String**| The name of the VM scale set containing the extension. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualMachineScaleSetExtensionListResult**](VirtualMachineScaleSetExtensionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

