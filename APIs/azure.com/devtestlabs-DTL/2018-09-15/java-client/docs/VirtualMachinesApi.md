# VirtualMachinesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualMachinesAddDataDisk**](VirtualMachinesApi.md#virtualMachinesAddDataDisk) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name}/addDataDisk |  |
| [**virtualMachinesApplyArtifacts**](VirtualMachinesApi.md#virtualMachinesApplyArtifacts) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name}/applyArtifacts |  |
| [**virtualMachinesClaim**](VirtualMachinesApi.md#virtualMachinesClaim) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name}/claim |  |
| [**virtualMachinesCreateOrUpdate**](VirtualMachinesApi.md#virtualMachinesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name} |  |
| [**virtualMachinesDelete**](VirtualMachinesApi.md#virtualMachinesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name} |  |
| [**virtualMachinesDetachDataDisk**](VirtualMachinesApi.md#virtualMachinesDetachDataDisk) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name}/detachDataDisk |  |
| [**virtualMachinesGet**](VirtualMachinesApi.md#virtualMachinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name} |  |
| [**virtualMachinesGetRdpFileContents**](VirtualMachinesApi.md#virtualMachinesGetRdpFileContents) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name}/getRdpFileContents |  |
| [**virtualMachinesList**](VirtualMachinesApi.md#virtualMachinesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines |  |
| [**virtualMachinesListApplicableSchedules**](VirtualMachinesApi.md#virtualMachinesListApplicableSchedules) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name}/listApplicableSchedules |  |
| [**virtualMachinesRedeploy**](VirtualMachinesApi.md#virtualMachinesRedeploy) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name}/redeploy |  |
| [**virtualMachinesResize**](VirtualMachinesApi.md#virtualMachinesResize) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name}/resize |  |
| [**virtualMachinesRestart**](VirtualMachinesApi.md#virtualMachinesRestart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name}/restart |  |
| [**virtualMachinesStart**](VirtualMachinesApi.md#virtualMachinesStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name}/start |  |
| [**virtualMachinesStop**](VirtualMachinesApi.md#virtualMachinesStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name}/stop |  |
| [**virtualMachinesTransferDisks**](VirtualMachinesApi.md#virtualMachinesTransferDisks) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name}/transferDisks |  |
| [**virtualMachinesUnClaim**](VirtualMachinesApi.md#virtualMachinesUnClaim) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name}/unClaim |  |
| [**virtualMachinesUpdate**](VirtualMachinesApi.md#virtualMachinesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name} |  |


<a id="virtualMachinesAddDataDisk"></a>
# **virtualMachinesAddDataDisk**
> virtualMachinesAddDataDisk(subscriptionId, resourceGroupName, labName, name, apiVersion, dataDiskProperties)



Attach a new or existing data disk to virtual machine. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    DataDiskProperties dataDiskProperties = new DataDiskProperties(); // DataDiskProperties | Request body for adding a new or existing data disk to a virtual machine.
    try {
      apiInstance.virtualMachinesAddDataDisk(subscriptionId, resourceGroupName, labName, name, apiVersion, dataDiskProperties);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesAddDataDisk");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **dataDiskProperties** | [**DataDiskProperties**](DataDiskProperties.md)| Request body for adding a new or existing data disk to a virtual machine. | |

### Return type

null (empty response body)

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
| **0** | BadRequest |  -  |

<a id="virtualMachinesApplyArtifacts"></a>
# **virtualMachinesApplyArtifacts**
> virtualMachinesApplyArtifacts(subscriptionId, resourceGroupName, labName, name, apiVersion, applyArtifactsRequest)



Apply artifacts to virtual machine. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    ApplyArtifactsRequest applyArtifactsRequest = new ApplyArtifactsRequest(); // ApplyArtifactsRequest | Request body for applying artifacts to a virtual machine.
    try {
      apiInstance.virtualMachinesApplyArtifacts(subscriptionId, resourceGroupName, labName, name, apiVersion, applyArtifactsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesApplyArtifacts");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **applyArtifactsRequest** | [**ApplyArtifactsRequest**](ApplyArtifactsRequest.md)| Request body for applying artifacts to a virtual machine. | |

### Return type

null (empty response body)

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
| **0** | BadRequest |  -  |

<a id="virtualMachinesClaim"></a>
# **virtualMachinesClaim**
> virtualMachinesClaim(subscriptionId, resourceGroupName, labName, name, apiVersion)



Take ownership of an existing virtual machine This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    try {
      apiInstance.virtualMachinesClaim(subscriptionId, resourceGroupName, labName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesClaim");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |

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
| **0** | BadRequest |  -  |

<a id="virtualMachinesCreateOrUpdate"></a>
# **virtualMachinesCreateOrUpdate**
> LabVirtualMachine virtualMachinesCreateOrUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, labVirtualMachine)



Create or replace an existing virtual machine. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    LabVirtualMachine labVirtualMachine = new LabVirtualMachine(); // LabVirtualMachine | A virtual machine.
    try {
      LabVirtualMachine result = apiInstance.virtualMachinesCreateOrUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, labVirtualMachine);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **labVirtualMachine** | [**LabVirtualMachine**](LabVirtualMachine.md)| A virtual machine. | |

### Return type

[**LabVirtualMachine**](LabVirtualMachine.md)

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
| **0** | BadRequest |  -  |

<a id="virtualMachinesDelete"></a>
# **virtualMachinesDelete**
> virtualMachinesDelete(subscriptionId, resourceGroupName, labName, name, apiVersion)



Delete virtual machine. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    try {
      apiInstance.virtualMachinesDelete(subscriptionId, resourceGroupName, labName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesDelete");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |

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
| **0** | BadRequest |  -  |

<a id="virtualMachinesDetachDataDisk"></a>
# **virtualMachinesDetachDataDisk**
> virtualMachinesDetachDataDisk(subscriptionId, resourceGroupName, labName, name, apiVersion, detachDataDiskProperties)



Detach the specified disk from the virtual machine. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    DetachDataDiskProperties detachDataDiskProperties = new DetachDataDiskProperties(); // DetachDataDiskProperties | Request body for detaching data disk from a virtual machine.
    try {
      apiInstance.virtualMachinesDetachDataDisk(subscriptionId, resourceGroupName, labName, name, apiVersion, detachDataDiskProperties);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesDetachDataDisk");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **detachDataDiskProperties** | [**DetachDataDiskProperties**](DetachDataDiskProperties.md)| Request body for detaching data disk from a virtual machine. | |

### Return type

null (empty response body)

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
| **0** | BadRequest |  -  |

<a id="virtualMachinesGet"></a>
# **virtualMachinesGet**
> LabVirtualMachine virtualMachinesGet(subscriptionId, resourceGroupName, labName, name, apiVersion, $expand)



Get virtual machine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($expand=artifacts,computeVm,networkInterface,applicableSchedule)'
    try {
      LabVirtualMachine result = apiInstance.virtualMachinesGet(subscriptionId, resourceGroupName, labName, name, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesGet");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;artifacts,computeVm,networkInterface,applicableSchedule)&#39; | [optional] |

### Return type

[**LabVirtualMachine**](LabVirtualMachine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="virtualMachinesGetRdpFileContents"></a>
# **virtualMachinesGetRdpFileContents**
> RdpConnection virtualMachinesGetRdpFileContents(subscriptionId, resourceGroupName, labName, name, apiVersion)



Gets a string that represents the contents of the RDP file for the virtual machine

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    try {
      RdpConnection result = apiInstance.virtualMachinesGetRdpFileContents(subscriptionId, resourceGroupName, labName, name, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesGetRdpFileContents");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |

### Return type

[**RdpConnection**](RdpConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="virtualMachinesList"></a>
# **virtualMachinesList**
> LabVirtualMachineList virtualMachinesList(subscriptionId, resourceGroupName, labName, apiVersion, $expand, $filter, $top, $orderby)



List virtual machines in a given lab.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String apiVersion = "2018-09-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($expand=artifacts,computeVm,networkInterface,applicableSchedule)'
    String $filter = "$filter_example"; // String | The filter to apply to the operation. Example: '$filter=contains(name,'myName')
    Integer $top = 56; // Integer | The maximum number of resources to return from the operation. Example: '$top=10'
    String $orderby = "$orderby_example"; // String | The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
    try {
      LabVirtualMachineList result = apiInstance.virtualMachinesList(subscriptionId, resourceGroupName, labName, apiVersion, $expand, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;artifacts,computeVm,networkInterface,applicableSchedule)&#39; | [optional] |
| **$filter** | **String**| The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;) | [optional] |
| **$top** | **Integer**| The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39; | [optional] |
| **$orderby** | **String**| The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39; | [optional] |

### Return type

[**LabVirtualMachineList**](LabVirtualMachineList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="virtualMachinesListApplicableSchedules"></a>
# **virtualMachinesListApplicableSchedules**
> ApplicableSchedule virtualMachinesListApplicableSchedules(subscriptionId, resourceGroupName, labName, name, apiVersion)



Lists the applicable start/stop schedules, if any.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    try {
      ApplicableSchedule result = apiInstance.virtualMachinesListApplicableSchedules(subscriptionId, resourceGroupName, labName, name, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesListApplicableSchedules");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |

### Return type

[**ApplicableSchedule**](ApplicableSchedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="virtualMachinesRedeploy"></a>
# **virtualMachinesRedeploy**
> virtualMachinesRedeploy(subscriptionId, resourceGroupName, labName, name, apiVersion)



Redeploy a virtual machine This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    try {
      apiInstance.virtualMachinesRedeploy(subscriptionId, resourceGroupName, labName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesRedeploy");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |

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
| **0** | BadRequest |  -  |

<a id="virtualMachinesResize"></a>
# **virtualMachinesResize**
> virtualMachinesResize(subscriptionId, resourceGroupName, labName, name, apiVersion, resizeLabVirtualMachineProperties)



Resize Virtual Machine. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    ResizeLabVirtualMachineProperties resizeLabVirtualMachineProperties = new ResizeLabVirtualMachineProperties(); // ResizeLabVirtualMachineProperties | Request body for resizing a virtual machine.
    try {
      apiInstance.virtualMachinesResize(subscriptionId, resourceGroupName, labName, name, apiVersion, resizeLabVirtualMachineProperties);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesResize");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **resizeLabVirtualMachineProperties** | [**ResizeLabVirtualMachineProperties**](ResizeLabVirtualMachineProperties.md)| Request body for resizing a virtual machine. | |

### Return type

null (empty response body)

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
| **0** | BadRequest |  -  |

<a id="virtualMachinesRestart"></a>
# **virtualMachinesRestart**
> virtualMachinesRestart(subscriptionId, resourceGroupName, labName, name, apiVersion)



Restart a virtual machine. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    try {
      apiInstance.virtualMachinesRestart(subscriptionId, resourceGroupName, labName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesRestart");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |

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
| **0** | BadRequest |  -  |

<a id="virtualMachinesStart"></a>
# **virtualMachinesStart**
> virtualMachinesStart(subscriptionId, resourceGroupName, labName, name, apiVersion)



Start a virtual machine. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    try {
      apiInstance.virtualMachinesStart(subscriptionId, resourceGroupName, labName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesStart");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |

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
| **0** | BadRequest |  -  |

<a id="virtualMachinesStop"></a>
# **virtualMachinesStop**
> virtualMachinesStop(subscriptionId, resourceGroupName, labName, name, apiVersion)



Stop a virtual machine This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    try {
      apiInstance.virtualMachinesStop(subscriptionId, resourceGroupName, labName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesStop");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |

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
| **0** | BadRequest |  -  |

<a id="virtualMachinesTransferDisks"></a>
# **virtualMachinesTransferDisks**
> virtualMachinesTransferDisks(subscriptionId, resourceGroupName, labName, name, apiVersion)



Transfers all data disks attached to the virtual machine to be owned by the current user. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    try {
      apiInstance.virtualMachinesTransferDisks(subscriptionId, resourceGroupName, labName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesTransferDisks");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |

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
| **0** | BadRequest |  -  |

<a id="virtualMachinesUnClaim"></a>
# **virtualMachinesUnClaim**
> virtualMachinesUnClaim(subscriptionId, resourceGroupName, labName, name, apiVersion)



Release ownership of an existing virtual machine This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    try {
      apiInstance.virtualMachinesUnClaim(subscriptionId, resourceGroupName, labName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesUnClaim");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |

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
| **0** | BadRequest |  -  |

<a id="virtualMachinesUpdate"></a>
# **virtualMachinesUpdate**
> LabVirtualMachine virtualMachinesUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, labVirtualMachine)



Allows modifying tags of virtual machines. All other properties will be ignored.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachinesApi apiInstance = new VirtualMachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the virtual machine.
    String apiVersion = "2018-09-15"; // String | Client API version.
    LabVirtualMachineFragment labVirtualMachine = new LabVirtualMachineFragment(); // LabVirtualMachineFragment | A virtual machine.
    try {
      LabVirtualMachine result = apiInstance.virtualMachinesUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, labVirtualMachine);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the virtual machine. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **labVirtualMachine** | [**LabVirtualMachineFragment**](LabVirtualMachineFragment.md)| A virtual machine. | |

### Return type

[**LabVirtualMachine**](LabVirtualMachine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

