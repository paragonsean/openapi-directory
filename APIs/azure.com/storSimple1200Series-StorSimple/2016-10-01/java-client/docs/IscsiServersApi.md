# IscsiServersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iscsiServersBackupNow**](IscsiServersApi.md#iscsiServersBackupNow) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/iscsiservers/{iscsiServerName}/backup |  |
| [**iscsiServersCreateOrUpdate**](IscsiServersApi.md#iscsiServersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/iscsiservers/{iscsiServerName} |  |
| [**iscsiServersDelete**](IscsiServersApi.md#iscsiServersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/iscsiservers/{iscsiServerName} |  |
| [**iscsiServersGet**](IscsiServersApi.md#iscsiServersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/iscsiservers/{iscsiServerName} |  |
| [**iscsiServersListByDevice**](IscsiServersApi.md#iscsiServersListByDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/iscsiservers |  |
| [**iscsiServersListByManager**](IscsiServersApi.md#iscsiServersListByManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/iscsiservers |  |
| [**iscsiServersListMetricDefinition**](IscsiServersApi.md#iscsiServersListMetricDefinition) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/iscsiservers/{iscsiServerName}/metricsDefinitions |  |
| [**iscsiServersListMetrics**](IscsiServersApi.md#iscsiServersListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/iscsiservers/{iscsiServerName}/metrics |  |


<a id="iscsiServersBackupNow"></a>
# **iscsiServersBackupNow**
> iscsiServersBackupNow(deviceName, iscsiServerName, subscriptionId, resourceGroupName, managerName, apiVersion)



Backup the iSCSI server now.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IscsiServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IscsiServersApi apiInstance = new IscsiServersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String iscsiServerName = "iscsiServerName_example"; // String | The iSCSI server name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      apiInstance.iscsiServersBackupNow(deviceName, iscsiServerName, subscriptionId, resourceGroupName, managerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IscsiServersApi#iscsiServersBackupNow");
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
| **iscsiServerName** | **String**| The iSCSI server name. | |
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
| **202** | Accepted the request to backup the iSCSI server. |  -  |
| **204** | Successfully completed backup of the iSCSI server. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="iscsiServersCreateOrUpdate"></a>
# **iscsiServersCreateOrUpdate**
> ISCSIServer iscsiServersCreateOrUpdate(deviceName, iscsiServerName, subscriptionId, resourceGroupName, managerName, apiVersion, iscsiServer)



Creates or updates the iSCSI server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IscsiServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IscsiServersApi apiInstance = new IscsiServersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String iscsiServerName = "iscsiServerName_example"; // String | The iSCSI server name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    ISCSIServer iscsiServer = new ISCSIServer(); // ISCSIServer | The iSCSI server.
    try {
      ISCSIServer result = apiInstance.iscsiServersCreateOrUpdate(deviceName, iscsiServerName, subscriptionId, resourceGroupName, managerName, apiVersion, iscsiServer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IscsiServersApi#iscsiServersCreateOrUpdate");
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
| **iscsiServerName** | **String**| The iSCSI server name. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |
| **iscsiServer** | [**ISCSIServer**](ISCSIServer.md)| The iSCSI server. | |

### Return type

[**ISCSIServer**](ISCSIServer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created or updated the iSCSI server. |  -  |
| **202** | Accepted the request to create or update the iSCSI server. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="iscsiServersDelete"></a>
# **iscsiServersDelete**
> iscsiServersDelete(deviceName, iscsiServerName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the iSCSI server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IscsiServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IscsiServersApi apiInstance = new IscsiServersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String iscsiServerName = "iscsiServerName_example"; // String | The iSCSI server name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      apiInstance.iscsiServersDelete(deviceName, iscsiServerName, subscriptionId, resourceGroupName, managerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IscsiServersApi#iscsiServersDelete");
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
| **iscsiServerName** | **String**| The iSCSI server name. | |
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
| **202** | Accepted the request to delete the iSCSI server. |  -  |
| **204** | Successfully deleted the iSCSI server. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="iscsiServersGet"></a>
# **iscsiServersGet**
> ISCSIServer iscsiServersGet(deviceName, iscsiServerName, subscriptionId, resourceGroupName, managerName, apiVersion)



Returns the properties of the specified iSCSI server name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IscsiServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IscsiServersApi apiInstance = new IscsiServersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String iscsiServerName = "iscsiServerName_example"; // String | The iSCSI server name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      ISCSIServer result = apiInstance.iscsiServersGet(deviceName, iscsiServerName, subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IscsiServersApi#iscsiServersGet");
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
| **iscsiServerName** | **String**| The iSCSI server name. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

### Return type

[**ISCSIServer**](ISCSIServer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The iSCSI server. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="iscsiServersListByDevice"></a>
# **iscsiServersListByDevice**
> ISCSIServerList iscsiServersListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves all the iSCSI in a device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IscsiServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IscsiServersApi apiInstance = new IscsiServersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      ISCSIServerList result = apiInstance.iscsiServersListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IscsiServersApi#iscsiServersListByDevice");
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

[**ISCSIServerList**](ISCSIServerList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of iSCSI servers. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="iscsiServersListByManager"></a>
# **iscsiServersListByManager**
> ISCSIServerList iscsiServersListByManager(subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves all the iSCSI servers in a manager.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IscsiServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IscsiServersApi apiInstance = new IscsiServersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      ISCSIServerList result = apiInstance.iscsiServersListByManager(subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IscsiServersApi#iscsiServersListByManager");
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

[**ISCSIServerList**](ISCSIServerList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of iSCSI servers. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="iscsiServersListMetricDefinition"></a>
# **iscsiServersListMetricDefinition**
> MetricDefinitionList iscsiServersListMetricDefinition(deviceName, iscsiServerName, subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves metric definitions for all metrics aggregated at iSCSI server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IscsiServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IscsiServersApi apiInstance = new IscsiServersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String iscsiServerName = "iscsiServerName_example"; // String | The iSCSI server name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      MetricDefinitionList result = apiInstance.iscsiServersListMetricDefinition(deviceName, iscsiServerName, subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IscsiServersApi#iscsiServersListMetricDefinition");
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
| **iscsiServerName** | **String**| The iSCSI server name. | |
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

<a id="iscsiServersListMetrics"></a>
# **iscsiServersListMetrics**
> MetricList iscsiServersListMetrics(deviceName, iscsiServerName, subscriptionId, resourceGroupName, managerName, apiVersion, $filter)



Gets the iSCSI server metrics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IscsiServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IscsiServersApi apiInstance = new IscsiServersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String iscsiServerName = "iscsiServerName_example"; // String | The iSCSI server name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    String $filter = "$filter_example"; // String | OData Filter options
    try {
      MetricList result = apiInstance.iscsiServersListMetrics(deviceName, iscsiServerName, subscriptionId, resourceGroupName, managerName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IscsiServersApi#iscsiServersListMetrics");
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
| **iscsiServerName** | **String**| The iSCSI server name. | |
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

