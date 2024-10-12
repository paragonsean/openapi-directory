# ReplicationStorageClassificationMappingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**replicationStorageClassificationMappingsCreate**](ReplicationStorageClassificationMappingsApi.md#replicationStorageClassificationMappingsCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationStorageClassifications/{storageClassificationName}/replicationStorageClassificationMappings/{storageClassificationMappingName} | Create storage classification mapping. |
| [**replicationStorageClassificationMappingsDelete**](ReplicationStorageClassificationMappingsApi.md#replicationStorageClassificationMappingsDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationStorageClassifications/{storageClassificationName}/replicationStorageClassificationMappings/{storageClassificationMappingName} | Delete a storage classification mapping. |
| [**replicationStorageClassificationMappingsGet**](ReplicationStorageClassificationMappingsApi.md#replicationStorageClassificationMappingsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationStorageClassifications/{storageClassificationName}/replicationStorageClassificationMappings/{storageClassificationMappingName} | Gets the details of a storage classification mapping. |
| [**replicationStorageClassificationMappingsList**](ReplicationStorageClassificationMappingsApi.md#replicationStorageClassificationMappingsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationStorageClassificationMappings | Gets the list of storage classification mappings objects under a vault. |
| [**replicationStorageClassificationMappingsListByReplicationStorageClassifications**](ReplicationStorageClassificationMappingsApi.md#replicationStorageClassificationMappingsListByReplicationStorageClassifications) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationStorageClassifications/{storageClassificationName}/replicationStorageClassificationMappings | Gets the list of storage classification mappings objects under a storage. |


<a id="replicationStorageClassificationMappingsCreate"></a>
# **replicationStorageClassificationMappingsCreate**
> StorageClassificationMapping replicationStorageClassificationMappingsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName, storageClassificationMappingName, pairingInput)

Create storage classification mapping.

The operation to create a storage classification mapping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationStorageClassificationMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationStorageClassificationMappingsApi apiInstance = new ReplicationStorageClassificationMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String storageClassificationName = "storageClassificationName_example"; // String | Storage classification name.
    String storageClassificationMappingName = "storageClassificationMappingName_example"; // String | Storage classification mapping name.
    StorageClassificationMappingInput pairingInput = new StorageClassificationMappingInput(); // StorageClassificationMappingInput | Pairing input.
    try {
      StorageClassificationMapping result = apiInstance.replicationStorageClassificationMappingsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName, storageClassificationMappingName, pairingInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationStorageClassificationMappingsApi#replicationStorageClassificationMappingsCreate");
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
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **fabricName** | **String**| Fabric name. | |
| **storageClassificationName** | **String**| Storage classification name. | |
| **storageClassificationMappingName** | **String**| Storage classification mapping name. | |
| **pairingInput** | [**StorageClassificationMappingInput**](StorageClassificationMappingInput.md)| Pairing input. | |

### Return type

[**StorageClassificationMapping**](StorageClassificationMapping.md)

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

<a id="replicationStorageClassificationMappingsDelete"></a>
# **replicationStorageClassificationMappingsDelete**
> replicationStorageClassificationMappingsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName, storageClassificationMappingName)

Delete a storage classification mapping.

The operation to delete a storage classification mapping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationStorageClassificationMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationStorageClassificationMappingsApi apiInstance = new ReplicationStorageClassificationMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String storageClassificationName = "storageClassificationName_example"; // String | Storage classification name.
    String storageClassificationMappingName = "storageClassificationMappingName_example"; // String | Storage classification mapping name.
    try {
      apiInstance.replicationStorageClassificationMappingsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName, storageClassificationMappingName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationStorageClassificationMappingsApi#replicationStorageClassificationMappingsDelete");
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
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **fabricName** | **String**| Fabric name. | |
| **storageClassificationName** | **String**| Storage classification name. | |
| **storageClassificationMappingName** | **String**| Storage classification mapping name. | |

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

<a id="replicationStorageClassificationMappingsGet"></a>
# **replicationStorageClassificationMappingsGet**
> StorageClassificationMapping replicationStorageClassificationMappingsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName, storageClassificationMappingName)

Gets the details of a storage classification mapping.

Gets the details of the specified storage classification mapping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationStorageClassificationMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationStorageClassificationMappingsApi apiInstance = new ReplicationStorageClassificationMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String storageClassificationName = "storageClassificationName_example"; // String | Storage classification name.
    String storageClassificationMappingName = "storageClassificationMappingName_example"; // String | Storage classification mapping name.
    try {
      StorageClassificationMapping result = apiInstance.replicationStorageClassificationMappingsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName, storageClassificationMappingName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationStorageClassificationMappingsApi#replicationStorageClassificationMappingsGet");
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
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **fabricName** | **String**| Fabric name. | |
| **storageClassificationName** | **String**| Storage classification name. | |
| **storageClassificationMappingName** | **String**| Storage classification mapping name. | |

### Return type

[**StorageClassificationMapping**](StorageClassificationMapping.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationStorageClassificationMappingsList"></a>
# **replicationStorageClassificationMappingsList**
> StorageClassificationMappingCollection replicationStorageClassificationMappingsList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets the list of storage classification mappings objects under a vault.

Lists the storage classification mappings in the vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationStorageClassificationMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationStorageClassificationMappingsApi apiInstance = new ReplicationStorageClassificationMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    try {
      StorageClassificationMappingCollection result = apiInstance.replicationStorageClassificationMappingsList(apiVersion, resourceName, resourceGroupName, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationStorageClassificationMappingsApi#replicationStorageClassificationMappingsList");
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
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |

### Return type

[**StorageClassificationMappingCollection**](StorageClassificationMappingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationStorageClassificationMappingsListByReplicationStorageClassifications"></a>
# **replicationStorageClassificationMappingsListByReplicationStorageClassifications**
> StorageClassificationMappingCollection replicationStorageClassificationMappingsListByReplicationStorageClassifications(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName)

Gets the list of storage classification mappings objects under a storage.

Lists the storage classification mappings for the fabric.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationStorageClassificationMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationStorageClassificationMappingsApi apiInstance = new ReplicationStorageClassificationMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String storageClassificationName = "storageClassificationName_example"; // String | Storage classification name.
    try {
      StorageClassificationMappingCollection result = apiInstance.replicationStorageClassificationMappingsListByReplicationStorageClassifications(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationStorageClassificationMappingsApi#replicationStorageClassificationMappingsListByReplicationStorageClassifications");
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
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **fabricName** | **String**| Fabric name. | |
| **storageClassificationName** | **String**| Storage classification name. | |

### Return type

[**StorageClassificationMappingCollection**](StorageClassificationMappingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

