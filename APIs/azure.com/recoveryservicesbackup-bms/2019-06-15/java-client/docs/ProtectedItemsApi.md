# ProtectedItemsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protectedItemsCreateOrUpdate**](ProtectedItemsApi.md#protectedItemsCreateOrUpdate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName} |  |
| [**protectedItemsDelete**](ProtectedItemsApi.md#protectedItemsDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName} |  |
| [**protectedItemsGet**](ProtectedItemsApi.md#protectedItemsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName} |  |


<a id="protectedItemsCreateOrUpdate"></a>
# **protectedItemsCreateOrUpdate**
> ProtectedItemResource protectedItemsCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, parameters)



Enables backup of an item or to modifies the backup policy information of an already backed up item. This is an  asynchronous operation. To know the status of the operation, call the GetItemOperationResult API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectedItemsApi apiInstance = new ProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name associated with the backup item.
    String containerName = "containerName_example"; // String | Container name associated with the backup item.
    String protectedItemName = "protectedItemName_example"; // String | Item name to be backed up.
    ProtectedItemResource parameters = new ProtectedItemResource(); // ProtectedItemResource | resource backed up item
    try {
      ProtectedItemResource result = apiInstance.protectedItemsCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectedItemsApi#protectedItemsCreateOrUpdate");
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
| **apiVersion** | **String**| Client Api Version. | |
| **vaultName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **fabricName** | **String**| Fabric name associated with the backup item. | |
| **containerName** | **String**| Container name associated with the backup item. | |
| **protectedItemName** | **String**| Item name to be backed up. | |
| **parameters** | [**ProtectedItemResource**](ProtectedItemResource.md)| resource backed up item | |

### Return type

[**ProtectedItemResource**](ProtectedItemResource.md)

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

<a id="protectedItemsDelete"></a>
# **protectedItemsDelete**
> protectedItemsDelete(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName)



Used to disable backup of an item within a container. This is an asynchronous operation. To know the status of the  request, call the GetItemOperationResult API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectedItemsApi apiInstance = new ProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name associated with the backed up item.
    String containerName = "containerName_example"; // String | Container name associated with the backed up item.
    String protectedItemName = "protectedItemName_example"; // String | Backed up item to be deleted.
    try {
      apiInstance.protectedItemsDelete(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectedItemsApi#protectedItemsDelete");
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
| **apiVersion** | **String**| Client Api Version. | |
| **vaultName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **fabricName** | **String**| Fabric name associated with the backed up item. | |
| **containerName** | **String**| Container name associated with the backed up item. | |
| **protectedItemName** | **String**| Backed up item to be deleted. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **204** | NoContent |  -  |

<a id="protectedItemsGet"></a>
# **protectedItemsGet**
> ProtectedItemResource protectedItemsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, $filter)



Provides the details of the backed up item. This is an asynchronous operation. To know the status of the operation,  call the GetItemOperationResult API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectedItemsApi apiInstance = new ProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name associated with the backed up item.
    String containerName = "containerName_example"; // String | Container name associated with the backed up item.
    String protectedItemName = "protectedItemName_example"; // String | Backed up item name whose details are to be fetched.
    String $filter = "$filter_example"; // String | OData filter options.
    try {
      ProtectedItemResource result = apiInstance.protectedItemsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectedItemsApi#protectedItemsGet");
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
| **apiVersion** | **String**| Client Api Version. | |
| **vaultName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **fabricName** | **String**| Fabric name associated with the backed up item. | |
| **containerName** | **String**| Container name associated with the backed up item. | |
| **protectedItemName** | **String**| Backed up item name whose details are to be fetched. | |
| **$filter** | **String**| OData filter options. | [optional] |

### Return type

[**ProtectedItemResource**](ProtectedItemResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

