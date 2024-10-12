# StorageAccountsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageAccountsCreateOrUpdate**](StorageAccountsApi.md#storageAccountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/storageAccounts/{storageAccountName} | Creates a new StorageAccount or updates an existing StorageAccount on the device. |
| [**storageAccountsDelete**](StorageAccountsApi.md#storageAccountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/storageAccounts/{storageAccountName} |  |
| [**storageAccountsGet**](StorageAccountsApi.md#storageAccountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/storageAccounts/{storageAccountName} | Gets a StorageAccount by name. |
| [**storageAccountsListByDataBoxEdgeDevice**](StorageAccountsApi.md#storageAccountsListByDataBoxEdgeDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/storageAccounts | Lists all the storage accounts in a Data Box Edge/Data Box Gateway device. |


<a id="storageAccountsCreateOrUpdate"></a>
# **storageAccountsCreateOrUpdate**
> StorageAccount storageAccountsCreateOrUpdate(deviceName, storageAccountName, subscriptionId, resourceGroupName, apiVersion, storageAccount)

Creates a new StorageAccount or updates an existing StorageAccount on the device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageAccountsApi apiInstance = new StorageAccountsApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String storageAccountName = "storageAccountName_example"; // String | The StorageAccount name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    StorageAccount storageAccount = new StorageAccount(); // StorageAccount | The StorageAccount properties.
    try {
      StorageAccount result = apiInstance.storageAccountsCreateOrUpdate(deviceName, storageAccountName, subscriptionId, resourceGroupName, apiVersion, storageAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageAccountsApi#storageAccountsCreateOrUpdate");
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
| **storageAccountName** | **String**| The StorageAccount name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |
| **storageAccount** | [**StorageAccount**](StorageAccount.md)| The StorageAccount properties. | |

### Return type

[**StorageAccount**](StorageAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created or updated the StorageAccount. |  -  |
| **202** | Accepted the request to create or update the StorageAccount. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="storageAccountsDelete"></a>
# **storageAccountsDelete**
> storageAccountsDelete(deviceName, storageAccountName, subscriptionId, resourceGroupName, apiVersion)



Deletes the StorageAccount on the Data Box Edge/Data Box Gateway device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageAccountsApi apiInstance = new StorageAccountsApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String storageAccountName = "storageAccountName_example"; // String | The StorageAccount name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.storageAccountsDelete(deviceName, storageAccountName, subscriptionId, resourceGroupName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageAccountsApi#storageAccountsDelete");
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
| **storageAccountName** | **String**| The StorageAccount name. | |
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
| **202** | Accepted the request to delete the StorageAccount. |  -  |
| **204** | The StorageAccount is already deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="storageAccountsGet"></a>
# **storageAccountsGet**
> StorageAccount storageAccountsGet(deviceName, storageAccountName, subscriptionId, resourceGroupName, apiVersion)

Gets a StorageAccount by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageAccountsApi apiInstance = new StorageAccountsApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String storageAccountName = "storageAccountName_example"; // String | The storage account name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      StorageAccount result = apiInstance.storageAccountsGet(deviceName, storageAccountName, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageAccountsApi#storageAccountsGet");
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
| **storageAccountName** | **String**| The storage account name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**StorageAccount**](StorageAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The storage account details. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="storageAccountsListByDataBoxEdgeDevice"></a>
# **storageAccountsListByDataBoxEdgeDevice**
> StorageAccountList storageAccountsListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion)

Lists all the storage accounts in a Data Box Edge/Data Box Gateway device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageAccountsApi apiInstance = new StorageAccountsApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      StorageAccountList result = apiInstance.storageAccountsListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageAccountsApi#storageAccountsListByDataBoxEdgeDevice");
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

[**StorageAccountList**](StorageAccountList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of all the StorageAccounts on the device. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

