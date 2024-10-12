# ReplicationNetworkMappingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**replicationNetworkMappingsCreate**](ReplicationNetworkMappingsApi.md#replicationNetworkMappingsCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationNetworks/{networkName}/replicationNetworkMappings/{networkMappingName} | Creates network mapping. |
| [**replicationNetworkMappingsDelete**](ReplicationNetworkMappingsApi.md#replicationNetworkMappingsDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationNetworks/{networkName}/replicationNetworkMappings/{networkMappingName} | Delete network mapping. |
| [**replicationNetworkMappingsGet**](ReplicationNetworkMappingsApi.md#replicationNetworkMappingsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationNetworks/{networkName}/replicationNetworkMappings/{networkMappingName} | Gets network mapping by name. |
| [**replicationNetworkMappingsList**](ReplicationNetworkMappingsApi.md#replicationNetworkMappingsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationNetworkMappings | Gets all the network mappings under a vault. |
| [**replicationNetworkMappingsListByReplicationNetworks**](ReplicationNetworkMappingsApi.md#replicationNetworkMappingsListByReplicationNetworks) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationNetworks/{networkName}/replicationNetworkMappings | Gets all the network mappings under a network. |
| [**replicationNetworkMappingsUpdate**](ReplicationNetworkMappingsApi.md#replicationNetworkMappingsUpdate) | **PATCH** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationNetworks/{networkName}/replicationNetworkMappings/{networkMappingName} | Updates network mapping. |


<a id="replicationNetworkMappingsCreate"></a>
# **replicationNetworkMappingsCreate**
> NetworkMapping replicationNetworkMappingsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName, input)

Creates network mapping.

The operation to create an ASR network mapping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationNetworkMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationNetworkMappingsApi apiInstance = new ReplicationNetworkMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Primary fabric name.
    String networkName = "networkName_example"; // String | Primary network name.
    String networkMappingName = "networkMappingName_example"; // String | Network mapping name.
    CreateNetworkMappingInput input = new CreateNetworkMappingInput(); // CreateNetworkMappingInput | Create network mapping input.
    try {
      NetworkMapping result = apiInstance.replicationNetworkMappingsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationNetworkMappingsApi#replicationNetworkMappingsCreate");
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
| **fabricName** | **String**| Primary fabric name. | |
| **networkName** | **String**| Primary network name. | |
| **networkMappingName** | **String**| Network mapping name. | |
| **input** | [**CreateNetworkMappingInput**](CreateNetworkMappingInput.md)| Create network mapping input. | |

### Return type

[**NetworkMapping**](NetworkMapping.md)

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

<a id="replicationNetworkMappingsDelete"></a>
# **replicationNetworkMappingsDelete**
> replicationNetworkMappingsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName)

Delete network mapping.

The operation to delete a network mapping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationNetworkMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationNetworkMappingsApi apiInstance = new ReplicationNetworkMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Primary fabric name.
    String networkName = "networkName_example"; // String | Primary network name.
    String networkMappingName = "networkMappingName_example"; // String | ARM Resource Name for network mapping.
    try {
      apiInstance.replicationNetworkMappingsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationNetworkMappingsApi#replicationNetworkMappingsDelete");
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
| **fabricName** | **String**| Primary fabric name. | |
| **networkName** | **String**| Primary network name. | |
| **networkMappingName** | **String**| ARM Resource Name for network mapping. | |

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

<a id="replicationNetworkMappingsGet"></a>
# **replicationNetworkMappingsGet**
> NetworkMapping replicationNetworkMappingsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName)

Gets network mapping by name.

Gets the details of an ASR network mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationNetworkMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationNetworkMappingsApi apiInstance = new ReplicationNetworkMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Primary fabric name.
    String networkName = "networkName_example"; // String | Primary network name.
    String networkMappingName = "networkMappingName_example"; // String | Network mapping name.
    try {
      NetworkMapping result = apiInstance.replicationNetworkMappingsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationNetworkMappingsApi#replicationNetworkMappingsGet");
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
| **fabricName** | **String**| Primary fabric name. | |
| **networkName** | **String**| Primary network name. | |
| **networkMappingName** | **String**| Network mapping name. | |

### Return type

[**NetworkMapping**](NetworkMapping.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationNetworkMappingsList"></a>
# **replicationNetworkMappingsList**
> NetworkMappingCollection replicationNetworkMappingsList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets all the network mappings under a vault.

Lists all ASR network mappings in the vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationNetworkMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationNetworkMappingsApi apiInstance = new ReplicationNetworkMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    try {
      NetworkMappingCollection result = apiInstance.replicationNetworkMappingsList(apiVersion, resourceName, resourceGroupName, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationNetworkMappingsApi#replicationNetworkMappingsList");
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

[**NetworkMappingCollection**](NetworkMappingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationNetworkMappingsListByReplicationNetworks"></a>
# **replicationNetworkMappingsListByReplicationNetworks**
> NetworkMappingCollection replicationNetworkMappingsListByReplicationNetworks(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName)

Gets all the network mappings under a network.

Lists all ASR network mappings for the specified network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationNetworkMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationNetworkMappingsApi apiInstance = new ReplicationNetworkMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Primary fabric name.
    String networkName = "networkName_example"; // String | Primary network name.
    try {
      NetworkMappingCollection result = apiInstance.replicationNetworkMappingsListByReplicationNetworks(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationNetworkMappingsApi#replicationNetworkMappingsListByReplicationNetworks");
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
| **fabricName** | **String**| Primary fabric name. | |
| **networkName** | **String**| Primary network name. | |

### Return type

[**NetworkMappingCollection**](NetworkMappingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationNetworkMappingsUpdate"></a>
# **replicationNetworkMappingsUpdate**
> NetworkMapping replicationNetworkMappingsUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName, input)

Updates network mapping.

The operation to update an ASR network mapping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationNetworkMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationNetworkMappingsApi apiInstance = new ReplicationNetworkMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Primary fabric name.
    String networkName = "networkName_example"; // String | Primary network name.
    String networkMappingName = "networkMappingName_example"; // String | Network mapping name.
    UpdateNetworkMappingInput input = new UpdateNetworkMappingInput(); // UpdateNetworkMappingInput | Update network mapping input.
    try {
      NetworkMapping result = apiInstance.replicationNetworkMappingsUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationNetworkMappingsApi#replicationNetworkMappingsUpdate");
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
| **fabricName** | **String**| Primary fabric name. | |
| **networkName** | **String**| Primary network name. | |
| **networkMappingName** | **String**| Network mapping name. | |
| **input** | [**UpdateNetworkMappingInput**](UpdateNetworkMappingInput.md)| Update network mapping input. | |

### Return type

[**NetworkMapping**](NetworkMapping.md)

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

