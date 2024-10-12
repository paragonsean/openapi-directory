# DevicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**devicesCreateOrUpdate**](DevicesApi.md#devicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName} |  |
| [**devicesCreateOrUpdateSecuritySettings**](DevicesApi.md#devicesCreateOrUpdateSecuritySettings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/securitySettings/default/update |  |
| [**devicesDelete**](DevicesApi.md#devicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName} |  |
| [**devicesDownloadUpdates**](DevicesApi.md#devicesDownloadUpdates) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/downloadUpdates | Downloads the updates on a Data Box Edge/Data Box Gateway device. |
| [**devicesGet**](DevicesApi.md#devicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName} |  |
| [**devicesGetExtendedInformation**](DevicesApi.md#devicesGetExtendedInformation) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/getExtendedInformation |  |
| [**devicesGetNetworkSettings**](DevicesApi.md#devicesGetNetworkSettings) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/networkSettings/default |  |
| [**devicesGetUpdateSummary**](DevicesApi.md#devicesGetUpdateSummary) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/updateSummary/default | Gets information about the availability of updates based on the last scan of the device. It also gets information about any ongoing download or install jobs on the device. |
| [**devicesInstallUpdates**](DevicesApi.md#devicesInstallUpdates) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/installUpdates | Installs the updates on the Data Box Edge/Data Box Gateway device. |
| [**devicesListByResourceGroup**](DevicesApi.md#devicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices |  |
| [**devicesListBySubscription**](DevicesApi.md#devicesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices |  |
| [**devicesScanForUpdates**](DevicesApi.md#devicesScanForUpdates) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/scanForUpdates | Scans for updates on a Data Box Edge/Data Box Gateway device. |
| [**devicesUpdate**](DevicesApi.md#devicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName} |  |
| [**devicesUploadCertificate**](DevicesApi.md#devicesUploadCertificate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/uploadCertificate |  |


<a id="devicesCreateOrUpdate"></a>
# **devicesCreateOrUpdate**
> DataBoxEdgeDevice devicesCreateOrUpdate(deviceName, subscriptionId, resourceGroupName, apiVersion, dataBoxEdgeDevice)



Creates or updates a Data Box Edge/Data Box Gateway resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    DataBoxEdgeDevice dataBoxEdgeDevice = new DataBoxEdgeDevice(); // DataBoxEdgeDevice | The resource object.
    try {
      DataBoxEdgeDevice result = apiInstance.devicesCreateOrUpdate(deviceName, subscriptionId, resourceGroupName, apiVersion, dataBoxEdgeDevice);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesCreateOrUpdate");
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
| **deviceName** | **String**| The device name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |
| **dataBoxEdgeDevice** | [**DataBoxEdgeDevice**](DataBoxEdgeDevice.md)| The resource object. | |

### Return type

[**DataBoxEdgeDevice**](DataBoxEdgeDevice.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created or updated the resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="devicesCreateOrUpdateSecuritySettings"></a>
# **devicesCreateOrUpdateSecuritySettings**
> devicesCreateOrUpdateSecuritySettings(deviceName, subscriptionId, resourceGroupName, apiVersion, securitySettings)



Updates the security settings on a Data Box Edge/Data Box Gateway device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    SecuritySettings securitySettings = new SecuritySettings(); // SecuritySettings | The security settings.
    try {
      apiInstance.devicesCreateOrUpdateSecuritySettings(deviceName, subscriptionId, resourceGroupName, apiVersion, securitySettings);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesCreateOrUpdateSecuritySettings");
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
| **deviceName** | **String**| The device name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |
| **securitySettings** | [**SecuritySettings**](SecuritySettings.md)| The security settings. | |

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
| **202** | Accepted the request to update the security settings. |  -  |
| **204** | Updated the security settings. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="devicesDelete"></a>
# **devicesDelete**
> devicesDelete(deviceName, subscriptionId, resourceGroupName, apiVersion)



Deletes the Data Box Edge/Data Box Gateway device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.devicesDelete(deviceName, subscriptionId, resourceGroupName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesDelete");
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
| **deviceName** | **String**| The device name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

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
| **200** | Successfully deleted the resource. |  -  |
| **202** | Accepted the request to delete the resource. |  -  |
| **204** | The resource is already deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="devicesDownloadUpdates"></a>
# **devicesDownloadUpdates**
> devicesDownloadUpdates(deviceName, subscriptionId, resourceGroupName, apiVersion)

Downloads the updates on a Data Box Edge/Data Box Gateway device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.devicesDownloadUpdates(deviceName, subscriptionId, resourceGroupName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesDownloadUpdates");
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
| **deviceName** | **String**| The device name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

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
| **200** | Successfully downloaded the updates on the device. |  -  |
| **202** | Accepted the request to download the updates on the device. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="devicesGet"></a>
# **devicesGet**
> DataBoxEdgeDevice devicesGet(deviceName, subscriptionId, resourceGroupName, apiVersion)



Gets the properties of the Data Box Edge/Data Box Gateway device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      DataBoxEdgeDevice result = apiInstance.devicesGet(deviceName, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesGet");
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
| **deviceName** | **String**| The device name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**DataBoxEdgeDevice**](DataBoxEdgeDevice.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Data Box Edge/Data Box Gateway device. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="devicesGetExtendedInformation"></a>
# **devicesGetExtendedInformation**
> DataBoxEdgeDeviceExtendedInfo devicesGetExtendedInformation(deviceName, subscriptionId, resourceGroupName, apiVersion)



Gets additional information for the specified Data Box Edge/Data Box Gateway device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      DataBoxEdgeDeviceExtendedInfo result = apiInstance.devicesGetExtendedInformation(deviceName, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesGetExtendedInformation");
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
| **deviceName** | **String**| The device name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**DataBoxEdgeDeviceExtendedInfo**](DataBoxEdgeDeviceExtendedInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The additional information. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="devicesGetNetworkSettings"></a>
# **devicesGetNetworkSettings**
> NetworkSettings devicesGetNetworkSettings(deviceName, subscriptionId, resourceGroupName, apiVersion)



Gets the network settings of the specified Data Box Edge/Data Box Gateway device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      NetworkSettings result = apiInstance.devicesGetNetworkSettings(deviceName, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesGetNetworkSettings");
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
| **deviceName** | **String**| The device name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**NetworkSettings**](NetworkSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The device network settings. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="devicesGetUpdateSummary"></a>
# **devicesGetUpdateSummary**
> UpdateSummary devicesGetUpdateSummary(deviceName, subscriptionId, resourceGroupName, apiVersion)

Gets information about the availability of updates based on the last scan of the device. It also gets information about any ongoing download or install jobs on the device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      UpdateSummary result = apiInstance.devicesGetUpdateSummary(deviceName, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesGetUpdateSummary");
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
| **deviceName** | **String**| The device name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**UpdateSummary**](UpdateSummary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The update summary. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="devicesInstallUpdates"></a>
# **devicesInstallUpdates**
> devicesInstallUpdates(deviceName, subscriptionId, resourceGroupName, apiVersion)

Installs the updates on the Data Box Edge/Data Box Gateway device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.devicesInstallUpdates(deviceName, subscriptionId, resourceGroupName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesInstallUpdates");
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
| **deviceName** | **String**| The device name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

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
| **200** | Successfully installed updates on the device. |  -  |
| **202** | Accepted the request to install updates on the device. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="devicesListByResourceGroup"></a>
# **devicesListByResourceGroup**
> DataBoxEdgeDeviceList devicesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $expand)



Gets all the Data Box Edge/Data Box Gateway devices in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    String $expand = "$expand_example"; // String | Specify $expand=details to populate additional fields related to the resource or Specify $skipToken=<token> to populate the next page in the list.
    try {
      DataBoxEdgeDeviceList result = apiInstance.devicesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesListByResourceGroup");
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
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |
| **$expand** | **String**| Specify $expand&#x3D;details to populate additional fields related to the resource or Specify $skipToken&#x3D;&lt;token&gt; to populate the next page in the list. | [optional] |

### Return type

[**DataBoxEdgeDeviceList**](DataBoxEdgeDeviceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of Data Box Edge/Data Box Gateway devices. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="devicesListBySubscription"></a>
# **devicesListBySubscription**
> DataBoxEdgeDeviceList devicesListBySubscription(subscriptionId, apiVersion, $expand)



Gets all the Data Box Edge/Data Box Gateway devices in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String apiVersion = "apiVersion_example"; // String | The API version.
    String $expand = "$expand_example"; // String | Specify $expand=details to populate additional fields related to the resource or Specify $skipToken=<token> to populate the next page in the list.
    try {
      DataBoxEdgeDeviceList result = apiInstance.devicesListBySubscription(subscriptionId, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesListBySubscription");
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
| **apiVersion** | **String**| The API version. | |
| **$expand** | **String**| Specify $expand&#x3D;details to populate additional fields related to the resource or Specify $skipToken&#x3D;&lt;token&gt; to populate the next page in the list. | [optional] |

### Return type

[**DataBoxEdgeDeviceList**](DataBoxEdgeDeviceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of Data Box Edge/Data Box Gateway devices. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="devicesScanForUpdates"></a>
# **devicesScanForUpdates**
> devicesScanForUpdates(deviceName, subscriptionId, resourceGroupName, apiVersion)

Scans for updates on a Data Box Edge/Data Box Gateway device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.devicesScanForUpdates(deviceName, subscriptionId, resourceGroupName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesScanForUpdates");
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
| **deviceName** | **String**| The device name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

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
| **200** | Successfully scanned the device for updates. |  -  |
| **202** | Accepted the request to scan for updates on the device. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="devicesUpdate"></a>
# **devicesUpdate**
> DataBoxEdgeDevice devicesUpdate(deviceName, subscriptionId, resourceGroupName, apiVersion, parameters)



Modifies a Data Box Edge/Data Box Gateway resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    DataBoxEdgeDevicePatch parameters = new DataBoxEdgeDevicePatch(); // DataBoxEdgeDevicePatch | The resource parameters.
    try {
      DataBoxEdgeDevice result = apiInstance.devicesUpdate(deviceName, subscriptionId, resourceGroupName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesUpdate");
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
| **deviceName** | **String**| The device name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |
| **parameters** | [**DataBoxEdgeDevicePatch**](DataBoxEdgeDevicePatch.md)| The resource parameters. | |

### Return type

[**DataBoxEdgeDevice**](DataBoxEdgeDevice.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="devicesUploadCertificate"></a>
# **devicesUploadCertificate**
> UploadCertificateResponse devicesUploadCertificate(deviceName, subscriptionId, resourceGroupName, apiVersion, parameters)



Uploads registration certificate for the device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    UploadCertificateRequest parameters = new UploadCertificateRequest(); // UploadCertificateRequest | The upload certificate request.
    try {
      UploadCertificateResponse result = apiInstance.devicesUploadCertificate(deviceName, subscriptionId, resourceGroupName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesUploadCertificate");
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
| **deviceName** | **String**| The device name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |
| **parameters** | [**UploadCertificateRequest**](UploadCertificateRequest.md)| The upload certificate request. | |

### Return type

[**UploadCertificateResponse**](UploadCertificateResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully uploaded the registration certificate. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

