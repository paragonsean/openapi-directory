# RecoveryPointsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recoveryPointsGet**](RecoveryPointsApi.md#recoveryPointsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId} |  |
| [**recoveryPointsList**](RecoveryPointsApi.md#recoveryPointsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints |  |


<a id="recoveryPointsGet"></a>
# **recoveryPointsGet**
> RecoveryPointResource recoveryPointsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId)



Provides the backup data for the RecoveryPointID. This is an asynchronous operation. To learn the status of the operation, call the GetProtectedItemOperationResult API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecoveryPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecoveryPointsApi apiInstance = new RecoveryPointsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String fabricName = "fabricName_example"; // String | The fabric name associated with backup item.
    String containerName = "containerName_example"; // String | The container name associated with backup item.
    String protectedItemName = "protectedItemName_example"; // String | The name of the backup item used in this GET operation.
    String recoveryPointId = "recoveryPointId_example"; // String | The RecoveryPointID associated with this GET operation.
    try {
      RecoveryPointResource result = apiInstance.recoveryPointsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecoveryPointsApi#recoveryPointsGet");
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
| **apiVersion** | **String**| Client API version. | |
| **vaultName** | **String**| The name of the Recovery Services vault. | |
| **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **fabricName** | **String**| The fabric name associated with backup item. | |
| **containerName** | **String**| The container name associated with backup item. | |
| **protectedItemName** | **String**| The name of the backup item used in this GET operation. | |
| **recoveryPointId** | **String**| The RecoveryPointID associated with this GET operation. | |

### Return type

[**RecoveryPointResource**](RecoveryPointResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |

<a id="recoveryPointsList"></a>
# **recoveryPointsList**
> RecoveryPointResourceList recoveryPointsList(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, $filter)



Lists the recovery points, or backup copies, for the specified backup item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecoveryPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecoveryPointsApi apiInstance = new RecoveryPointsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String fabricName = "fabricName_example"; // String | The fabric name associated with the backup item.
    String containerName = "containerName_example"; // String | The container name associated with the backup item.
    String protectedItemName = "protectedItemName_example"; // String | The name of backup item used in this GET operation.
    String $filter = "$filter_example"; // String | startDate eq {yyyy-mm-dd hh:mm:ss PM} and endDate { yyyy-mm-dd hh:mm:ss PM}.
    try {
      RecoveryPointResourceList result = apiInstance.recoveryPointsList(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecoveryPointsApi#recoveryPointsList");
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
| **apiVersion** | **String**| Client API version. | |
| **vaultName** | **String**| The name of the Recovery Services vault. | |
| **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **fabricName** | **String**| The fabric name associated with the backup item. | |
| **containerName** | **String**| The container name associated with the backup item. | |
| **protectedItemName** | **String**| The name of backup item used in this GET operation. | |
| **$filter** | **String**| startDate eq {yyyy-mm-dd hh:mm:ss PM} and endDate { yyyy-mm-dd hh:mm:ss PM}. | [optional] |

### Return type

[**RecoveryPointResourceList**](RecoveryPointResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |

