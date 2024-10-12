# ReplicationRecoveryServicesProvidersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**replicationRecoveryServicesProvidersDelete**](ReplicationRecoveryServicesProvidersApi.md#replicationRecoveryServicesProvidersDelete) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationRecoveryServicesProviders/{providerName}/remove | Deletes provider from fabric. Note: Deleting provider for any fabric other than SingleHost is unsupported. To maintain backward compatibility for released clients the object \&quot;deleteRspInput\&quot; is used (if the object is empty we assume that it is old client and continue the old behavior). |
| [**replicationRecoveryServicesProvidersGet**](ReplicationRecoveryServicesProvidersApi.md#replicationRecoveryServicesProvidersGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationRecoveryServicesProviders/{providerName} | Gets the details of a recovery services provider. |
| [**replicationRecoveryServicesProvidersList**](ReplicationRecoveryServicesProvidersApi.md#replicationRecoveryServicesProvidersList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryServicesProviders | Gets the list of registered recovery services providers in the vault. This is a view only api. |
| [**replicationRecoveryServicesProvidersListByReplicationFabrics**](ReplicationRecoveryServicesProvidersApi.md#replicationRecoveryServicesProvidersListByReplicationFabrics) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationRecoveryServicesProviders | Gets the list of registered recovery services providers for the fabric. |
| [**replicationRecoveryServicesProvidersPurge**](ReplicationRecoveryServicesProvidersApi.md#replicationRecoveryServicesProvidersPurge) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationRecoveryServicesProviders/{providerName} | Purges recovery service provider from fabric |
| [**replicationRecoveryServicesProvidersRefreshProvider**](ReplicationRecoveryServicesProvidersApi.md#replicationRecoveryServicesProvidersRefreshProvider) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationRecoveryServicesProviders/{providerName}/refreshProvider | Refresh details from the recovery services provider. |


<a id="replicationRecoveryServicesProvidersDelete"></a>
# **replicationRecoveryServicesProvidersDelete**
> replicationRecoveryServicesProvidersDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName)

Deletes provider from fabric. Note: Deleting provider for any fabric other than SingleHost is unsupported. To maintain backward compatibility for released clients the object \&quot;deleteRspInput\&quot; is used (if the object is empty we assume that it is old client and continue the old behavior).

The operation to removes/delete(unregister) a recovery services provider from the vault

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryServicesProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryServicesProvidersApi apiInstance = new ReplicationRecoveryServicesProvidersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String providerName = "providerName_example"; // String | Recovery services provider name.
    try {
      apiInstance.replicationRecoveryServicesProvidersDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryServicesProvidersApi#replicationRecoveryServicesProvidersDelete");
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
| **providerName** | **String**| Recovery services provider name. | |

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

<a id="replicationRecoveryServicesProvidersGet"></a>
# **replicationRecoveryServicesProvidersGet**
> RecoveryServicesProvider replicationRecoveryServicesProvidersGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName)

Gets the details of a recovery services provider.

Gets the details of registered recovery services provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryServicesProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryServicesProvidersApi apiInstance = new ReplicationRecoveryServicesProvidersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String providerName = "providerName_example"; // String | Recovery services provider name
    try {
      RecoveryServicesProvider result = apiInstance.replicationRecoveryServicesProvidersGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryServicesProvidersApi#replicationRecoveryServicesProvidersGet");
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
| **providerName** | **String**| Recovery services provider name | |

### Return type

[**RecoveryServicesProvider**](RecoveryServicesProvider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationRecoveryServicesProvidersList"></a>
# **replicationRecoveryServicesProvidersList**
> RecoveryServicesProviderCollection replicationRecoveryServicesProvidersList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets the list of registered recovery services providers in the vault. This is a view only api.

Lists the registered recovery services providers in the vault

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryServicesProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryServicesProvidersApi apiInstance = new ReplicationRecoveryServicesProvidersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    try {
      RecoveryServicesProviderCollection result = apiInstance.replicationRecoveryServicesProvidersList(apiVersion, resourceName, resourceGroupName, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryServicesProvidersApi#replicationRecoveryServicesProvidersList");
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

[**RecoveryServicesProviderCollection**](RecoveryServicesProviderCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationRecoveryServicesProvidersListByReplicationFabrics"></a>
# **replicationRecoveryServicesProvidersListByReplicationFabrics**
> RecoveryServicesProviderCollection replicationRecoveryServicesProvidersListByReplicationFabrics(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName)

Gets the list of registered recovery services providers for the fabric.

Lists the registered recovery services providers for the specified fabric.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryServicesProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryServicesProvidersApi apiInstance = new ReplicationRecoveryServicesProvidersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name
    try {
      RecoveryServicesProviderCollection result = apiInstance.replicationRecoveryServicesProvidersListByReplicationFabrics(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryServicesProvidersApi#replicationRecoveryServicesProvidersListByReplicationFabrics");
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
| **fabricName** | **String**| Fabric name | |

### Return type

[**RecoveryServicesProviderCollection**](RecoveryServicesProviderCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationRecoveryServicesProvidersPurge"></a>
# **replicationRecoveryServicesProvidersPurge**
> replicationRecoveryServicesProvidersPurge(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName)

Purges recovery service provider from fabric

The operation to purge(force delete) a recovery services provider from the vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryServicesProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryServicesProvidersApi apiInstance = new ReplicationRecoveryServicesProvidersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String providerName = "providerName_example"; // String | Recovery services provider name.
    try {
      apiInstance.replicationRecoveryServicesProvidersPurge(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryServicesProvidersApi#replicationRecoveryServicesProvidersPurge");
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
| **providerName** | **String**| Recovery services provider name. | |

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

<a id="replicationRecoveryServicesProvidersRefreshProvider"></a>
# **replicationRecoveryServicesProvidersRefreshProvider**
> RecoveryServicesProvider replicationRecoveryServicesProvidersRefreshProvider(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName)

Refresh details from the recovery services provider.

The operation to refresh the information from the recovery services provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryServicesProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryServicesProvidersApi apiInstance = new ReplicationRecoveryServicesProvidersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String providerName = "providerName_example"; // String | Recovery services provider name.
    try {
      RecoveryServicesProvider result = apiInstance.replicationRecoveryServicesProvidersRefreshProvider(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryServicesProvidersApi#replicationRecoveryServicesProvidersRefreshProvider");
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
| **providerName** | **String**| Recovery services provider name. | |

### Return type

[**RecoveryServicesProvider**](RecoveryServicesProvider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

