# VirtualMachinesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualMachinesCreateOrUpdate**](VirtualMachinesApi.md#virtualMachinesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtualMachineName} | Implements virtual machine PUT method |
| [**virtualMachinesDelete**](VirtualMachinesApi.md#virtualMachinesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtualMachineName} | Implements virtual machine DELETE method |
| [**virtualMachinesGet**](VirtualMachinesApi.md#virtualMachinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtualMachineName} | Implements virtual machine GET method |
| [**virtualMachinesListByResourceGroup**](VirtualMachinesApi.md#virtualMachinesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/virtualMachines | Implements list virtual machine within RG method |
| [**virtualMachinesListBySubscription**](VirtualMachinesApi.md#virtualMachinesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/virtualMachines | Implements list virtual machine within subscription method |
| [**virtualMachinesStart**](VirtualMachinesApi.md#virtualMachinesStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtualMachineName}/start | Implements a start method for a virtual machine |
| [**virtualMachinesStop**](VirtualMachinesApi.md#virtualMachinesStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtualMachineName}/stop | Implements shutdown, poweroff, and suspend method for a virtual machine |
| [**virtualMachinesUpdate**](VirtualMachinesApi.md#virtualMachinesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtualMachineName} | Implements virtual machine PATCH method |


<a id="virtualMachinesCreateOrUpdate"></a>
# **virtualMachinesCreateOrUpdate**
> VirtualMachine virtualMachinesCreateOrUpdate(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion, virtualMachineRequest)

Implements virtual machine PUT method

Create Or Update Virtual Machine

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String referer = "referer_example"; // String | referer url
    String virtualMachineName = "virtualMachineName_example"; // String | virtual machine name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    VirtualMachine virtualMachineRequest = new VirtualMachine(); // VirtualMachine | Create or Update Virtual Machine request
    try {
      VirtualMachine result = apiInstance.virtualMachinesCreateOrUpdate(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion, virtualMachineRequest);
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
| **resourceGroupName** | **String**| The name of the resource group | |
| **referer** | **String**| referer url | |
| **virtualMachineName** | **String**| virtual machine name | |
| **apiVersion** | **String**| Client API version. | |
| **virtualMachineRequest** | [**VirtualMachine**](VirtualMachine.md)| Create or Update Virtual Machine request | |

### Return type

[**VirtualMachine**](VirtualMachine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If resource is created or updated successfully, 200 should be returned |  * Azure-AsyncOperation -  <br>  |
| **201** | If resource is created or updated successfully, 201 should be returned. provisionedState would of VirtualMachineProperties object would reflect the state of the resource |  * Azure-AsyncOperation -  <br>  |
| **0** | General Error |  -  |

<a id="virtualMachinesDelete"></a>
# **virtualMachinesDelete**
> virtualMachinesDelete(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion)

Implements virtual machine DELETE method

Delete virtual machine

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String referer = "referer_example"; // String | referer url
    String virtualMachineName = "virtualMachineName_example"; // String | virtual machine name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.virtualMachinesDelete(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion);
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
| **resourceGroupName** | **String**| The name of the resource group | |
| **referer** | **String**| referer url | |
| **virtualMachineName** | **String**| virtual machine name | |
| **apiVersion** | **String**| Client API version. | |

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
| **202** | accepted. the operation will complete asynchronously |  * Retry-After -  <br>  * Azure-AsyncOperation -  <br>  * Location -  <br>  |
| **204** | no content. resource does not exist and the request is well formed |  -  |
| **0** | General Error |  * Content-Type -  <br>  |

<a id="virtualMachinesGet"></a>
# **virtualMachinesGet**
> VirtualMachine virtualMachinesGet(subscriptionId, resourceGroupName, virtualMachineName, apiVersion)

Implements virtual machine GET method

Get virtual machine

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String virtualMachineName = "virtualMachineName_example"; // String | virtual machine name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      VirtualMachine result = apiInstance.virtualMachinesGet(subscriptionId, resourceGroupName, virtualMachineName, apiVersion);
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
| **resourceGroupName** | **String**| The name of the resource group | |
| **virtualMachineName** | **String**| virtual machine name | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**VirtualMachine**](VirtualMachine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

<a id="virtualMachinesListByResourceGroup"></a>
# **virtualMachinesListByResourceGroup**
> VirtualMachineListResponse virtualMachinesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter, $top, $skipToken)

Implements list virtual machine within RG method

Returns list of virtual machine within resource group

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String $filter = "$filter_example"; // String | The filter to apply on the list operation
    Integer $top = 56; // Integer | The maximum number of record sets to return
    String $skipToken = "$skipToken_example"; // String | to be used by nextLink implementation
    try {
      VirtualMachineListResponse result = apiInstance.virtualMachinesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter, $top, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group | |
| **apiVersion** | **String**| Client API version. | |
| **$filter** | **String**| The filter to apply on the list operation | [optional] |
| **$top** | **Integer**| The maximum number of record sets to return | [optional] |
| **$skipToken** | **String**| to be used by nextLink implementation | [optional] |

### Return type

[**VirtualMachineListResponse**](VirtualMachineListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

<a id="virtualMachinesListBySubscription"></a>
# **virtualMachinesListBySubscription**
> VirtualMachineListResponse virtualMachinesListBySubscription(subscriptionId, apiVersion, $filter, $top, $skipToken)

Implements list virtual machine within subscription method

Returns list virtual machine within subscription

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
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String $filter = "$filter_example"; // String | The filter to apply on the list operation
    Integer $top = 56; // Integer | The maximum number of record sets to return
    String $skipToken = "$skipToken_example"; // String | to be used by nextLink implementation
    try {
      VirtualMachineListResponse result = apiInstance.virtualMachinesListBySubscription(subscriptionId, apiVersion, $filter, $top, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachinesApi#virtualMachinesListBySubscription");
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
| **apiVersion** | **String**| Client API version. | |
| **$filter** | **String**| The filter to apply on the list operation | [optional] |
| **$top** | **Integer**| The maximum number of record sets to return | [optional] |
| **$skipToken** | **String**| to be used by nextLink implementation | [optional] |

### Return type

[**VirtualMachineListResponse**](VirtualMachineListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

<a id="virtualMachinesStart"></a>
# **virtualMachinesStart**
> virtualMachinesStart(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion)

Implements a start method for a virtual machine

Power on virtual machine

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String referer = "referer_example"; // String | referer url
    String virtualMachineName = "virtualMachineName_example"; // String | virtual machine name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.virtualMachinesStart(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion);
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
| **resourceGroupName** | **String**| The name of the resource group | |
| **referer** | **String**| referer url | |
| **virtualMachineName** | **String**| virtual machine name | |
| **apiVersion** | **String**| Client API version. | |

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
| **202** | Accepted. the operation will complete asynchronously |  * Retry-After -  <br>  * Azure-AsyncOperation -  <br>  * Location -  <br>  |
| **0** | General Error |  * Content-Type -  <br>  |

<a id="virtualMachinesStop"></a>
# **virtualMachinesStop**
> virtualMachinesStop(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion, mode, m)

Implements shutdown, poweroff, and suspend method for a virtual machine

Power off virtual machine, options: shutdown, poweroff, and suspend

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String referer = "referer_example"; // String | referer url
    String virtualMachineName = "virtualMachineName_example"; // String | virtual machine name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String mode = "reboot"; // String | query stop mode parameter (reboot, shutdown, etc...)
    VirtualMachineStopMode m = new VirtualMachineStopMode(); // VirtualMachineStopMode | body stop mode parameter (reboot, shutdown, etc...)
    try {
      apiInstance.virtualMachinesStop(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion, mode, m);
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
| **resourceGroupName** | **String**| The name of the resource group | |
| **referer** | **String**| referer url | |
| **virtualMachineName** | **String**| virtual machine name | |
| **apiVersion** | **String**| Client API version. | |
| **mode** | **String**| query stop mode parameter (reboot, shutdown, etc...) | [optional] [enum: reboot, suspend, shutdown, poweroff] |
| **m** | [**VirtualMachineStopMode**](VirtualMachineStopMode.md)| body stop mode parameter (reboot, shutdown, etc...) | [optional] |

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
| **202** | Accepted. the operation will complete asynchronously |  * Retry-After -  <br>  * Azure-AsyncOperation -  <br>  * Location -  <br>  |
| **0** | General Error |  * Content-Type -  <br>  |

<a id="virtualMachinesUpdate"></a>
# **virtualMachinesUpdate**
> VirtualMachine virtualMachinesUpdate(subscriptionId, resourceGroupName, virtualMachineName, apiVersion, virtualMachineRequest)

Implements virtual machine PATCH method

Patch virtual machine properties

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String virtualMachineName = "virtualMachineName_example"; // String | virtual machine name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    PatchPayload virtualMachineRequest = new PatchPayload(); // PatchPayload | Patch virtual machine request
    try {
      VirtualMachine result = apiInstance.virtualMachinesUpdate(subscriptionId, resourceGroupName, virtualMachineName, apiVersion, virtualMachineRequest);
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
| **resourceGroupName** | **String**| The name of the resource group | |
| **virtualMachineName** | **String**| virtual machine name | |
| **apiVersion** | **String**| Client API version. | |
| **virtualMachineRequest** | [**PatchPayload**](PatchPayload.md)| Patch virtual machine request | |

### Return type

[**VirtualMachine**](VirtualMachine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If resource is created or updated successfully, 200 should be returned |  -  |
| **0** | General Error |  -  |

