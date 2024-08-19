# VirtualMachineExtensionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualMachineExtensionsCreateOrUpdate**](VirtualMachineExtensionsApi.md#virtualMachineExtensionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions/{vmExtensionName} |  |
| [**virtualMachineExtensionsDelete**](VirtualMachineExtensionsApi.md#virtualMachineExtensionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions/{vmExtensionName} |  |
| [**virtualMachineExtensionsGet**](VirtualMachineExtensionsApi.md#virtualMachineExtensionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions/{vmExtensionName} |  |
| [**virtualMachineExtensionsUpdate**](VirtualMachineExtensionsApi.md#virtualMachineExtensionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions/{vmExtensionName} |  |
| [**virtualMachinesGetExtensions**](VirtualMachineExtensionsApi.md#virtualMachinesGetExtensions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions |  |


<a id="virtualMachineExtensionsCreateOrUpdate"></a>
# **virtualMachineExtensionsCreateOrUpdate**
> VirtualMachineExtension virtualMachineExtensionsCreateOrUpdate(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId, extensionParameters)



The operation to create or update the extension.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineExtensionsApi apiInstance = new VirtualMachineExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmName = "vmName_example"; // String | The name of the virtual machine where the extension should be created or updated.
    String vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualMachineExtension extensionParameters = new VirtualMachineExtension(); // VirtualMachineExtension | Parameters supplied to the Create Virtual Machine Extension operation.
    try {
      VirtualMachineExtension result = apiInstance.virtualMachineExtensionsCreateOrUpdate(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId, extensionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineExtensionsApi#virtualMachineExtensionsCreateOrUpdate");
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
| **vmName** | **String**| The name of the virtual machine where the extension should be created or updated. | |
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

<a id="virtualMachineExtensionsDelete"></a>
# **virtualMachineExtensionsDelete**
> OperationStatusResponse virtualMachineExtensionsDelete(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId)



The operation to delete the extension.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineExtensionsApi apiInstance = new VirtualMachineExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmName = "vmName_example"; // String | The name of the virtual machine where the extension should be deleted.
    String vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      OperationStatusResponse result = apiInstance.virtualMachineExtensionsDelete(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineExtensionsApi#virtualMachineExtensionsDelete");
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
| **vmName** | **String**| The name of the virtual machine where the extension should be deleted. | |
| **vmExtensionName** | **String**| The name of the virtual machine extension. | |
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

<a id="virtualMachineExtensionsGet"></a>
# **virtualMachineExtensionsGet**
> VirtualMachineExtension virtualMachineExtensionsGet(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId, $expand)



The operation to get the extension.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineExtensionsApi apiInstance = new VirtualMachineExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmName = "vmName_example"; // String | The name of the virtual machine containing the extension.
    String vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $expand = "$expand_example"; // String | The expand expression to apply on the operation.
    try {
      VirtualMachineExtension result = apiInstance.virtualMachineExtensionsGet(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineExtensionsApi#virtualMachineExtensionsGet");
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
| **vmName** | **String**| The name of the virtual machine containing the extension. | |
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

<a id="virtualMachineExtensionsUpdate"></a>
# **virtualMachineExtensionsUpdate**
> VirtualMachineExtension virtualMachineExtensionsUpdate(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId, extensionParameters)



The operation to update the extension.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineExtensionsApi apiInstance = new VirtualMachineExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmName = "vmName_example"; // String | The name of the virtual machine where the extension should be updated.
    String vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualMachineExtensionUpdate extensionParameters = new VirtualMachineExtensionUpdate(); // VirtualMachineExtensionUpdate | Parameters supplied to the Update Virtual Machine Extension operation.
    try {
      VirtualMachineExtension result = apiInstance.virtualMachineExtensionsUpdate(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId, extensionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineExtensionsApi#virtualMachineExtensionsUpdate");
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
| **vmName** | **String**| The name of the virtual machine where the extension should be updated. | |
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

<a id="virtualMachinesGetExtensions"></a>
# **virtualMachinesGetExtensions**
> VirtualMachineExtensionsListResult virtualMachinesGetExtensions(resourceGroupName, vmName, apiVersion, subscriptionId, $expand)



The operation to get all extensions of a Virtual Machine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineExtensionsApi apiInstance = new VirtualMachineExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String vmName = "vmName_example"; // String | The name of the virtual machine containing the extension.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $expand = "$expand_example"; // String | The expand expression to apply on the operation.
    try {
      VirtualMachineExtensionsListResult result = apiInstance.virtualMachinesGetExtensions(resourceGroupName, vmName, apiVersion, subscriptionId, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineExtensionsApi#virtualMachinesGetExtensions");
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
| **vmName** | **String**| The name of the virtual machine containing the extension. | |
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

