# ReplicationProtectionContainersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**replicationProtectionContainersCreate**](ReplicationProtectionContainersApi.md#replicationProtectionContainersCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName} | Create a protection container. |
| [**replicationProtectionContainersDelete**](ReplicationProtectionContainersApi.md#replicationProtectionContainersDelete) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/remove | Removes a protection container. |
| [**replicationProtectionContainersDiscoverProtectableItem**](ReplicationProtectionContainersApi.md#replicationProtectionContainersDiscoverProtectableItem) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/discoverProtectableItem | Adds a protectable item to the replication protection container. |
| [**replicationProtectionContainersGet**](ReplicationProtectionContainersApi.md#replicationProtectionContainersGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName} | Gets the protection container details. |
| [**replicationProtectionContainersList**](ReplicationProtectionContainersApi.md#replicationProtectionContainersList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationProtectionContainers | Gets the list of all protection containers in a vault. |
| [**replicationProtectionContainersListByReplicationFabrics**](ReplicationProtectionContainersApi.md#replicationProtectionContainersListByReplicationFabrics) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers | Gets the list of protection container for a fabric. |
| [**replicationProtectionContainersSwitchProtection**](ReplicationProtectionContainersApi.md#replicationProtectionContainersSwitchProtection) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/switchprotection | Switches protection from one container to another or one replication provider to another. |


<a id="replicationProtectionContainersCreate"></a>
# **replicationProtectionContainersCreate**
> ProtectionContainer replicationProtectionContainersCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, creationInput)

Create a protection container.

Operation to create a protection container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectionContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectionContainersApi apiInstance = new ReplicationProtectionContainersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Unique fabric ARM name.
    String protectionContainerName = "protectionContainerName_example"; // String | Unique protection container ARM name.
    CreateProtectionContainerInput creationInput = new CreateProtectionContainerInput(); // CreateProtectionContainerInput | Creation input.
    try {
      ProtectionContainer result = apiInstance.replicationProtectionContainersCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, creationInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectionContainersApi#replicationProtectionContainersCreate");
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
| **fabricName** | **String**| Unique fabric ARM name. | |
| **protectionContainerName** | **String**| Unique protection container ARM name. | |
| **creationInput** | [**CreateProtectionContainerInput**](CreateProtectionContainerInput.md)| Creation input. | |

### Return type

[**ProtectionContainer**](ProtectionContainer.md)

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

<a id="replicationProtectionContainersDelete"></a>
# **replicationProtectionContainersDelete**
> replicationProtectionContainersDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName)

Removes a protection container.

Operation to remove a protection container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectionContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectionContainersApi apiInstance = new ReplicationProtectionContainersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Unique fabric ARM name.
    String protectionContainerName = "protectionContainerName_example"; // String | Unique protection container ARM name.
    try {
      apiInstance.replicationProtectionContainersDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectionContainersApi#replicationProtectionContainersDelete");
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
| **fabricName** | **String**| Unique fabric ARM name. | |
| **protectionContainerName** | **String**| Unique protection container ARM name. | |

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

<a id="replicationProtectionContainersDiscoverProtectableItem"></a>
# **replicationProtectionContainersDiscoverProtectableItem**
> ProtectionContainer replicationProtectionContainersDiscoverProtectableItem(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, discoverProtectableItemRequest)

Adds a protectable item to the replication protection container.

The operation to a add a protectable item to a protection container(Add physical server.)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectionContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectionContainersApi apiInstance = new ReplicationProtectionContainersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | The name of the fabric.
    String protectionContainerName = "protectionContainerName_example"; // String | The name of the protection container.
    DiscoverProtectableItemRequest discoverProtectableItemRequest = new DiscoverProtectableItemRequest(); // DiscoverProtectableItemRequest | The request object to add a protectable item.
    try {
      ProtectionContainer result = apiInstance.replicationProtectionContainersDiscoverProtectableItem(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, discoverProtectableItemRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectionContainersApi#replicationProtectionContainersDiscoverProtectableItem");
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
| **fabricName** | **String**| The name of the fabric. | |
| **protectionContainerName** | **String**| The name of the protection container. | |
| **discoverProtectableItemRequest** | [**DiscoverProtectableItemRequest**](DiscoverProtectableItemRequest.md)| The request object to add a protectable item. | |

### Return type

[**ProtectionContainer**](ProtectionContainer.md)

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

<a id="replicationProtectionContainersGet"></a>
# **replicationProtectionContainersGet**
> ProtectionContainer replicationProtectionContainersGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName)

Gets the protection container details.

Gets the details of a protection container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectionContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectionContainersApi apiInstance = new ReplicationProtectionContainersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    try {
      ProtectionContainer result = apiInstance.replicationProtectionContainersGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectionContainersApi#replicationProtectionContainersGet");
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
| **protectionContainerName** | **String**| Protection container name. | |

### Return type

[**ProtectionContainer**](ProtectionContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationProtectionContainersList"></a>
# **replicationProtectionContainersList**
> ProtectionContainerCollection replicationProtectionContainersList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets the list of all protection containers in a vault.

Lists the protection containers in a vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectionContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectionContainersApi apiInstance = new ReplicationProtectionContainersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    try {
      ProtectionContainerCollection result = apiInstance.replicationProtectionContainersList(apiVersion, resourceName, resourceGroupName, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectionContainersApi#replicationProtectionContainersList");
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

[**ProtectionContainerCollection**](ProtectionContainerCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationProtectionContainersListByReplicationFabrics"></a>
# **replicationProtectionContainersListByReplicationFabrics**
> ProtectionContainerCollection replicationProtectionContainersListByReplicationFabrics(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName)

Gets the list of protection container for a fabric.

Lists the protection containers in the specified fabric.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectionContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectionContainersApi apiInstance = new ReplicationProtectionContainersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    try {
      ProtectionContainerCollection result = apiInstance.replicationProtectionContainersListByReplicationFabrics(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectionContainersApi#replicationProtectionContainersListByReplicationFabrics");
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

### Return type

[**ProtectionContainerCollection**](ProtectionContainerCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationProtectionContainersSwitchProtection"></a>
# **replicationProtectionContainersSwitchProtection**
> ProtectionContainer replicationProtectionContainersSwitchProtection(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, switchInput)

Switches protection from one container to another or one replication provider to another.

Operation to switch protection from one container to another or one replication provider to another.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectionContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectionContainersApi apiInstance = new ReplicationProtectionContainersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Unique fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    SwitchProtectionInput switchInput = new SwitchProtectionInput(); // SwitchProtectionInput | Switch protection input.
    try {
      ProtectionContainer result = apiInstance.replicationProtectionContainersSwitchProtection(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, switchInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectionContainersApi#replicationProtectionContainersSwitchProtection");
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
| **fabricName** | **String**| Unique fabric name. | |
| **protectionContainerName** | **String**| Protection container name. | |
| **switchInput** | [**SwitchProtectionInput**](SwitchProtectionInput.md)| Switch protection input. | |

### Return type

[**ProtectionContainer**](ProtectionContainer.md)

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

