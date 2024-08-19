# BackupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupsClone**](BackupsApi.md#backupsClone) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backups/{backupName}/elements/{elementName}/clone |  |
| [**backupsDelete**](BackupsApi.md#backupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backups/{backupName} |  |
| [**backupsListByDevice**](BackupsApi.md#backupsListByDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backups |  |
| [**backupsListByManager**](BackupsApi.md#backupsListByManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/backups |  |


<a id="backupsClone"></a>
# **backupsClone**
> backupsClone(deviceName, backupName, elementName, subscriptionId, resourceGroupName, managerName, apiVersion, cloneRequest)



Clones the given backup element to a new disk or share with given details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupsApi apiInstance = new BackupsApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String backupName = "backupName_example"; // String | The backup name.
    String elementName = "elementName_example"; // String | The backup element name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    CloneRequest cloneRequest = new CloneRequest(); // CloneRequest | The clone request.
    try {
      apiInstance.backupsClone(deviceName, backupName, elementName, subscriptionId, resourceGroupName, managerName, apiVersion, cloneRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupsApi#backupsClone");
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
| **backupName** | **String**| The backup name. | |
| **elementName** | **String**| The backup element name. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |
| **cloneRequest** | [**CloneRequest**](CloneRequest.md)| The clone request. | |

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
| **200** | Successfully cloned. |  -  |
| **202** | Accepted the request to clone. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="backupsDelete"></a>
# **backupsDelete**
> backupsDelete(deviceName, backupName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupsApi apiInstance = new BackupsApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String backupName = "backupName_example"; // String | The backup name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      apiInstance.backupsDelete(deviceName, backupName, subscriptionId, resourceGroupName, managerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupsApi#backupsDelete");
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
| **backupName** | **String**| The backup name. | |
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
| **202** | Accepted the request to delete the backup. |  -  |
| **204** | Successfully deleted the backup. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="backupsListByDevice"></a>
# **backupsListByDevice**
> BackupList backupsListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion, forFailover, $filter)



Retrieves all the backups in a device. Can be used to get the backups for failover also.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupsApi apiInstance = new BackupsApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    Boolean forFailover = true; // Boolean | Set to true if you need backups which can be used for failover.
    String $filter = "$filter_example"; // String | OData Filter options
    try {
      BackupList result = apiInstance.backupsListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion, forFailover, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupsApi#backupsListByDevice");
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
| **forFailover** | **Boolean**| Set to true if you need backups which can be used for failover. | [optional] |
| **$filter** | **String**| OData Filter options | [optional] |

### Return type

[**BackupList**](BackupList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of backups. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="backupsListByManager"></a>
# **backupsListByManager**
> BackupList backupsListByManager(subscriptionId, resourceGroupName, managerName, apiVersion, $filter)



Retrieves all the backups in a manager.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupsApi apiInstance = new BackupsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    String $filter = "$filter_example"; // String | OData Filter options
    try {
      BackupList result = apiInstance.backupsListByManager(subscriptionId, resourceGroupName, managerName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupsApi#backupsListByManager");
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
| **$filter** | **String**| OData Filter options | [optional] |

### Return type

[**BackupList**](BackupList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of backups. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

