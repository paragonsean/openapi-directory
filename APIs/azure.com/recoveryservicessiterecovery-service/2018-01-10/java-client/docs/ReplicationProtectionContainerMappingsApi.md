# ReplicationProtectionContainerMappingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**replicationProtectionContainerMappingsCreate**](ReplicationProtectionContainerMappingsApi.md#replicationProtectionContainerMappingsCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectionContainerMappings/{mappingName} | Create protection container mapping. |
| [**replicationProtectionContainerMappingsDelete**](ReplicationProtectionContainerMappingsApi.md#replicationProtectionContainerMappingsDelete) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectionContainerMappings/{mappingName}/remove | Remove protection container mapping. |
| [**replicationProtectionContainerMappingsGet**](ReplicationProtectionContainerMappingsApi.md#replicationProtectionContainerMappingsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectionContainerMappings/{mappingName} | Gets a protection container mapping/ |
| [**replicationProtectionContainerMappingsList**](ReplicationProtectionContainerMappingsApi.md#replicationProtectionContainerMappingsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationProtectionContainerMappings | Gets the list of all protection container mappings in a vault. |
| [**replicationProtectionContainerMappingsListByReplicationProtectionContainers**](ReplicationProtectionContainerMappingsApi.md#replicationProtectionContainerMappingsListByReplicationProtectionContainers) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectionContainerMappings | Gets the list of protection container mappings for a protection container. |
| [**replicationProtectionContainerMappingsPurge**](ReplicationProtectionContainerMappingsApi.md#replicationProtectionContainerMappingsPurge) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectionContainerMappings/{mappingName} | Purge protection container mapping. |
| [**replicationProtectionContainerMappingsUpdate**](ReplicationProtectionContainerMappingsApi.md#replicationProtectionContainerMappingsUpdate) | **PATCH** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectionContainerMappings/{mappingName} | Update protection container mapping. |


<a id="replicationProtectionContainerMappingsCreate"></a>
# **replicationProtectionContainerMappingsCreate**
> ProtectionContainerMapping replicationProtectionContainerMappingsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName, creationInput)

Create protection container mapping.

The operation to create a protection container mapping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectionContainerMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectionContainerMappingsApi apiInstance = new ReplicationProtectionContainerMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String mappingName = "mappingName_example"; // String | Protection container mapping name.
    CreateProtectionContainerMappingInput creationInput = new CreateProtectionContainerMappingInput(); // CreateProtectionContainerMappingInput | Mapping creation input.
    try {
      ProtectionContainerMapping result = apiInstance.replicationProtectionContainerMappingsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName, creationInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectionContainerMappingsApi#replicationProtectionContainerMappingsCreate");
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
| **mappingName** | **String**| Protection container mapping name. | |
| **creationInput** | [**CreateProtectionContainerMappingInput**](CreateProtectionContainerMappingInput.md)| Mapping creation input. | |

### Return type

[**ProtectionContainerMapping**](ProtectionContainerMapping.md)

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

<a id="replicationProtectionContainerMappingsDelete"></a>
# **replicationProtectionContainerMappingsDelete**
> replicationProtectionContainerMappingsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName, removalInput)

Remove protection container mapping.

The operation to delete or remove a protection container mapping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectionContainerMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectionContainerMappingsApi apiInstance = new ReplicationProtectionContainerMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String mappingName = "mappingName_example"; // String | Protection container mapping name.
    RemoveProtectionContainerMappingInput removalInput = new RemoveProtectionContainerMappingInput(); // RemoveProtectionContainerMappingInput | Removal input.
    try {
      apiInstance.replicationProtectionContainerMappingsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName, removalInput);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectionContainerMappingsApi#replicationProtectionContainerMappingsDelete");
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
| **mappingName** | **String**| Protection container mapping name. | |
| **removalInput** | [**RemoveProtectionContainerMappingInput**](RemoveProtectionContainerMappingInput.md)| Removal input. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **204** | NoContent |  -  |

<a id="replicationProtectionContainerMappingsGet"></a>
# **replicationProtectionContainerMappingsGet**
> ProtectionContainerMapping replicationProtectionContainerMappingsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName)

Gets a protection container mapping/

Gets the details of a protection container mapping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectionContainerMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectionContainerMappingsApi apiInstance = new ReplicationProtectionContainerMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String mappingName = "mappingName_example"; // String | Protection Container mapping name.
    try {
      ProtectionContainerMapping result = apiInstance.replicationProtectionContainerMappingsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectionContainerMappingsApi#replicationProtectionContainerMappingsGet");
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
| **mappingName** | **String**| Protection Container mapping name. | |

### Return type

[**ProtectionContainerMapping**](ProtectionContainerMapping.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationProtectionContainerMappingsList"></a>
# **replicationProtectionContainerMappingsList**
> ProtectionContainerMappingCollection replicationProtectionContainerMappingsList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets the list of all protection container mappings in a vault.

Lists the protection container mappings in the vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectionContainerMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectionContainerMappingsApi apiInstance = new ReplicationProtectionContainerMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    try {
      ProtectionContainerMappingCollection result = apiInstance.replicationProtectionContainerMappingsList(apiVersion, resourceName, resourceGroupName, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectionContainerMappingsApi#replicationProtectionContainerMappingsList");
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

[**ProtectionContainerMappingCollection**](ProtectionContainerMappingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationProtectionContainerMappingsListByReplicationProtectionContainers"></a>
# **replicationProtectionContainerMappingsListByReplicationProtectionContainers**
> ProtectionContainerMappingCollection replicationProtectionContainerMappingsListByReplicationProtectionContainers(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName)

Gets the list of protection container mappings for a protection container.

Lists the protection container mappings for a protection container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectionContainerMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectionContainerMappingsApi apiInstance = new ReplicationProtectionContainerMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    try {
      ProtectionContainerMappingCollection result = apiInstance.replicationProtectionContainerMappingsListByReplicationProtectionContainers(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectionContainerMappingsApi#replicationProtectionContainerMappingsListByReplicationProtectionContainers");
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

[**ProtectionContainerMappingCollection**](ProtectionContainerMappingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationProtectionContainerMappingsPurge"></a>
# **replicationProtectionContainerMappingsPurge**
> replicationProtectionContainerMappingsPurge(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName)

Purge protection container mapping.

The operation to purge(force delete) a protection container mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectionContainerMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectionContainerMappingsApi apiInstance = new ReplicationProtectionContainerMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String mappingName = "mappingName_example"; // String | Protection container mapping name.
    try {
      apiInstance.replicationProtectionContainerMappingsPurge(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectionContainerMappingsApi#replicationProtectionContainerMappingsPurge");
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
| **mappingName** | **String**| Protection container mapping name. | |

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

<a id="replicationProtectionContainerMappingsUpdate"></a>
# **replicationProtectionContainerMappingsUpdate**
> ProtectionContainerMapping replicationProtectionContainerMappingsUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName, updateInput)

Update protection container mapping.

The operation to update protection container mapping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectionContainerMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectionContainerMappingsApi apiInstance = new ReplicationProtectionContainerMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String mappingName = "mappingName_example"; // String | Protection container mapping name.
    UpdateProtectionContainerMappingInput updateInput = new UpdateProtectionContainerMappingInput(); // UpdateProtectionContainerMappingInput | Mapping update input.
    try {
      ProtectionContainerMapping result = apiInstance.replicationProtectionContainerMappingsUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName, updateInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectionContainerMappingsApi#replicationProtectionContainerMappingsUpdate");
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
| **mappingName** | **String**| Protection container mapping name. | |
| **updateInput** | [**UpdateProtectionContainerMappingInput**](UpdateProtectionContainerMappingInput.md)| Mapping update input. | |

### Return type

[**ProtectionContainerMapping**](ProtectionContainerMapping.md)

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

