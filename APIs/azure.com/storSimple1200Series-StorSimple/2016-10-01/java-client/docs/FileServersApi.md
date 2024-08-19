# FileServersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fileServersBackupNow**](FileServersApi.md#fileServersBackupNow) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/fileservers/{fileServerName}/backup |  |
| [**fileServersCreateOrUpdate**](FileServersApi.md#fileServersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/fileservers/{fileServerName} |  |
| [**fileServersDelete**](FileServersApi.md#fileServersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/fileservers/{fileServerName} |  |
| [**fileServersGet**](FileServersApi.md#fileServersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/fileservers/{fileServerName} |  |
| [**fileServersListByDevice**](FileServersApi.md#fileServersListByDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/fileservers |  |
| [**fileServersListByManager**](FileServersApi.md#fileServersListByManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/fileservers |  |
| [**fileServersListMetricDefinition**](FileServersApi.md#fileServersListMetricDefinition) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/fileservers/{fileServerName}/metricsDefinitions |  |
| [**fileServersListMetrics**](FileServersApi.md#fileServersListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/fileservers/{fileServerName}/metrics |  |


<a id="fileServersBackupNow"></a>
# **fileServersBackupNow**
> fileServersBackupNow(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion)



Backup the file server now.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileServersApi apiInstance = new FileServersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String fileServerName = "fileServerName_example"; // String | The file server name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      apiInstance.fileServersBackupNow(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServersApi#fileServersBackupNow");
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
| **fileServerName** | **String**| The file server name. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

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
| **202** | Accepted the request to backup the file server. |  -  |
| **204** | Successfully completed backup of the file server. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="fileServersCreateOrUpdate"></a>
# **fileServersCreateOrUpdate**
> FileServer fileServersCreateOrUpdate(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion, fileServer)



Creates or updates the file server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileServersApi apiInstance = new FileServersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String fileServerName = "fileServerName_example"; // String | The file server name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    FileServer fileServer = new FileServer(); // FileServer | The file server.
    try {
      FileServer result = apiInstance.fileServersCreateOrUpdate(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion, fileServer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServersApi#fileServersCreateOrUpdate");
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
| **fileServerName** | **String**| The file server name. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |
| **fileServer** | [**FileServer**](FileServer.md)| The file server. | |

### Return type

[**FileServer**](FileServer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created or updated the file server. |  -  |
| **202** | Accepted the request to create or update the file server. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="fileServersDelete"></a>
# **fileServersDelete**
> fileServersDelete(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the file server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileServersApi apiInstance = new FileServersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String fileServerName = "fileServerName_example"; // String | The file server name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      apiInstance.fileServersDelete(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServersApi#fileServersDelete");
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
| **fileServerName** | **String**| The file server name. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

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
| **202** | Accepted the request to delete the file server. |  -  |
| **204** | Successfully deleted the file server. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="fileServersGet"></a>
# **fileServersGet**
> FileServer fileServersGet(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion)



Returns the properties of the specified file server name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileServersApi apiInstance = new FileServersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String fileServerName = "fileServerName_example"; // String | The file server name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      FileServer result = apiInstance.fileServersGet(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServersApi#fileServersGet");
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
| **fileServerName** | **String**| The file server name. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

### Return type

[**FileServer**](FileServer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The file server. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="fileServersListByDevice"></a>
# **fileServersListByDevice**
> FileServerList fileServersListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves all the file servers in a device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileServersApi apiInstance = new FileServersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      FileServerList result = apiInstance.fileServersListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServersApi#fileServersListByDevice");
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
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

### Return type

[**FileServerList**](FileServerList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of file servers. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="fileServersListByManager"></a>
# **fileServersListByManager**
> FileServerList fileServersListByManager(subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves all the file servers in a manager.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileServersApi apiInstance = new FileServersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      FileServerList result = apiInstance.fileServersListByManager(subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServersApi#fileServersListByManager");
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
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

### Return type

[**FileServerList**](FileServerList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of file servers. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="fileServersListMetricDefinition"></a>
# **fileServersListMetricDefinition**
> MetricDefinitionList fileServersListMetricDefinition(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves metric definitions of all metrics aggregated at the file server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileServersApi apiInstance = new FileServersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The name of the device.
    String fileServerName = "fileServerName_example"; // String | The name of the file server.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      MetricDefinitionList result = apiInstance.fileServersListMetricDefinition(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServersApi#fileServersListMetricDefinition");
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
| **deviceName** | **String**| The name of the device. | |
| **fileServerName** | **String**| The name of the file server. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

### Return type

[**MetricDefinitionList**](MetricDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of metric definitions. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="fileServersListMetrics"></a>
# **fileServersListMetrics**
> MetricList fileServersListMetrics(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion, $filter)



Gets the file server metrics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileServersApi apiInstance = new FileServersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The name of the device.
    String fileServerName = "fileServerName_example"; // String | The name of the file server name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    String $filter = "$filter_example"; // String | OData Filter options
    try {
      MetricList result = apiInstance.fileServersListMetrics(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServersApi#fileServersListMetrics");
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
| **deviceName** | **String**| The name of the device. | |
| **fileServerName** | **String**| The name of the file server name. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |
| **$filter** | **String**| OData Filter options | [optional] |

### Return type

[**MetricList**](MetricList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of metrics. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

