# VaultsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vaultsCheckNameAvailability**](VaultsApi.md#vaultsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.KeyVault/checkNameAvailability |  |
| [**vaultsCreateOrUpdate**](VaultsApi.md#vaultsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName} |  |
| [**vaultsDelete**](VaultsApi.md#vaultsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName} |  |
| [**vaultsGet**](VaultsApi.md#vaultsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName} |  |
| [**vaultsGetDeleted**](VaultsApi.md#vaultsGetDeleted) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.KeyVault/locations/{location}/deletedVaults/{vaultName} |  |
| [**vaultsList**](VaultsApi.md#vaultsList) | **GET** /subscriptions/{subscriptionId}/resources |  |
| [**vaultsListByResourceGroup**](VaultsApi.md#vaultsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults |  |
| [**vaultsListBySubscription**](VaultsApi.md#vaultsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.KeyVault/vaults |  |
| [**vaultsListDeleted**](VaultsApi.md#vaultsListDeleted) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.KeyVault/deletedVaults |  |
| [**vaultsPurgeDeleted**](VaultsApi.md#vaultsPurgeDeleted) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.KeyVault/locations/{location}/deletedVaults/{vaultName}/purge |  |
| [**vaultsUpdate**](VaultsApi.md#vaultsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName} |  |
| [**vaultsUpdateAccessPolicy**](VaultsApi.md#vaultsUpdateAccessPolicy) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/accessPolicies/{operationKind} |  |


<a id="vaultsCheckNameAvailability"></a>
# **vaultsCheckNameAvailability**
> CheckNameAvailabilityResult vaultsCheckNameAvailability(apiVersion, subscriptionId, vaultName)



Checks that the vault name is valid and is not already in use.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VaultsApi apiInstance = new VaultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VaultCheckNameAvailabilityParameters vaultName = new VaultCheckNameAvailabilityParameters(); // VaultCheckNameAvailabilityParameters | The name of the vault.
    try {
      CheckNameAvailabilityResult result = apiInstance.vaultsCheckNameAvailability(apiVersion, subscriptionId, vaultName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultsApi#vaultsCheckNameAvailability");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **vaultName** | [**VaultCheckNameAvailabilityParameters**](VaultCheckNameAvailabilityParameters.md)| The name of the vault. | |

### Return type

[**CheckNameAvailabilityResult**](CheckNameAvailabilityResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Operation to check the vault name availability was successful. |  -  |

<a id="vaultsCreateOrUpdate"></a>
# **vaultsCreateOrUpdate**
> Vault vaultsCreateOrUpdate(resourceGroupName, vaultName, apiVersion, subscriptionId, parameters)



Create or update a key vault in the specified subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VaultsApi apiInstance = new VaultsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the server belongs.
    String vaultName = "vaultName_example"; // String | Name of the vault
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VaultCreateOrUpdateParameters parameters = new VaultCreateOrUpdateParameters(); // VaultCreateOrUpdateParameters | Parameters to create or update the vault
    try {
      Vault result = apiInstance.vaultsCreateOrUpdate(resourceGroupName, vaultName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultsApi#vaultsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the server belongs. | |
| **vaultName** | **String**| Name of the vault | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**VaultCreateOrUpdateParameters**](VaultCreateOrUpdateParameters.md)| Parameters to create or update the vault | |

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created or updated vault |  -  |
| **201** | Created or updated vault |  -  |

<a id="vaultsDelete"></a>
# **vaultsDelete**
> vaultsDelete(resourceGroupName, vaultName, apiVersion, subscriptionId)



Deletes the specified Azure key vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VaultsApi apiInstance = new VaultsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
    String vaultName = "vaultName_example"; // String | The name of the vault to delete
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.vaultsDelete(resourceGroupName, vaultName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultsApi#vaultsDelete");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the vault belongs. | |
| **vaultName** | **String**| The name of the vault to delete | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK Response. |  -  |
| **204** | No Content. |  -  |

<a id="vaultsGet"></a>
# **vaultsGet**
> Vault vaultsGet(resourceGroupName, vaultName, apiVersion, subscriptionId)



Gets the specified Azure key vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VaultsApi apiInstance = new VaultsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      Vault result = apiInstance.vaultsGet(resourceGroupName, vaultName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultsApi#vaultsGet");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the vault belongs. | |
| **vaultName** | **String**| The name of the vault. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieved vault |  -  |

<a id="vaultsGetDeleted"></a>
# **vaultsGetDeleted**
> DeletedVault vaultsGetDeleted(vaultName, location, apiVersion, subscriptionId)



Gets the deleted Azure key vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VaultsApi apiInstance = new VaultsApi(defaultClient);
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String location = "location_example"; // String | The location of the deleted vault.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      DeletedVault result = apiInstance.vaultsGetDeleted(vaultName, location, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultsApi#vaultsGetDeleted");
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
| **vaultName** | **String**| The name of the vault. | |
| **location** | **String**| The location of the deleted vault. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**DeletedVault**](DeletedVault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieved information about the deleted vault. |  -  |

<a id="vaultsList"></a>
# **vaultsList**
> ResourceListResult vaultsList($filter, apiVersion, subscriptionId, $top)



The List operation gets information about the vaults associated with the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VaultsApi apiInstance = new VaultsApi(defaultClient);
    String $filter = "resourceType eq 'Microsoft.KeyVault/vaults'"; // String | The filter to apply on the operation.
    String apiVersion = "2015-11-01"; // String | Azure Resource Manager Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | Maximum number of results to return.
    try {
      ResourceListResult result = apiInstance.vaultsList($filter, apiVersion, subscriptionId, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultsApi#vaultsList");
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
| **$filter** | **String**| The filter to apply on the operation. | [enum: resourceType eq 'Microsoft.KeyVault/vaults'] |
| **apiVersion** | **String**| Azure Resource Manager Api Version. | [enum: 2015-11-01] |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| Maximum number of results to return. | [optional] |

### Return type

[**ResourceListResult**](ResourceListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get information about all key vaults in the subscription. |  -  |

<a id="vaultsListByResourceGroup"></a>
# **vaultsListByResourceGroup**
> VaultListResult vaultsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, $top)



The List operation gets information about the vaults associated with the subscription and within the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VaultsApi apiInstance = new VaultsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | Maximum number of results to return.
    try {
      VaultListResult result = apiInstance.vaultsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultsApi#vaultsListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the vault belongs. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| Maximum number of results to return. | [optional] |

### Return type

[**VaultListResult**](VaultListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get information about all key vaults in the specified resource group. |  -  |

<a id="vaultsListBySubscription"></a>
# **vaultsListBySubscription**
> VaultListResult vaultsListBySubscription(apiVersion, subscriptionId, $top)



The List operation gets information about the vaults associated with the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VaultsApi apiInstance = new VaultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | Maximum number of results to return.
    try {
      VaultListResult result = apiInstance.vaultsListBySubscription(apiVersion, subscriptionId, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultsApi#vaultsListBySubscription");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| Maximum number of results to return. | [optional] |

### Return type

[**VaultListResult**](VaultListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get information about all key vaults in the specified subscription. |  -  |

<a id="vaultsListDeleted"></a>
# **vaultsListDeleted**
> DeletedVaultListResult vaultsListDeleted(apiVersion, subscriptionId)



Gets information about the deleted vaults in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VaultsApi apiInstance = new VaultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      DeletedVaultListResult result = apiInstance.vaultsListDeleted(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultsApi#vaultsListDeleted");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**DeletedVaultListResult**](DeletedVaultListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieved information about all deleted key vaults in a subscription. |  -  |

<a id="vaultsPurgeDeleted"></a>
# **vaultsPurgeDeleted**
> vaultsPurgeDeleted(vaultName, location, apiVersion, subscriptionId)



Permanently deletes the specified vault. aka Purges the deleted Azure key vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VaultsApi apiInstance = new VaultsApi(defaultClient);
    String vaultName = "vaultName_example"; // String | The name of the soft-deleted vault.
    String location = "location_example"; // String | The location of the soft-deleted vault.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.vaultsPurgeDeleted(vaultName, location, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultsApi#vaultsPurgeDeleted");
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
| **vaultName** | **String**| The name of the soft-deleted vault. | |
| **location** | **String**| The location of the soft-deleted vault. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The vault is purged. |  -  |
| **202** | Vault is being purged. |  -  |

<a id="vaultsUpdate"></a>
# **vaultsUpdate**
> Vault vaultsUpdate(resourceGroupName, vaultName, apiVersion, subscriptionId, parameters)



Update a key vault in the specified subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VaultsApi apiInstance = new VaultsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the server belongs.
    String vaultName = "vaultName_example"; // String | Name of the vault
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VaultPatchParameters parameters = new VaultPatchParameters(); // VaultPatchParameters | Parameters to patch the vault
    try {
      Vault result = apiInstance.vaultsUpdate(resourceGroupName, vaultName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultsApi#vaultsUpdate");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the server belongs. | |
| **vaultName** | **String**| Name of the vault | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**VaultPatchParameters**](VaultPatchParameters.md)| Parameters to patch the vault | |

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Patched vault |  -  |
| **201** | Patched vault |  -  |

<a id="vaultsUpdateAccessPolicy"></a>
# **vaultsUpdateAccessPolicy**
> VaultAccessPolicyParameters vaultsUpdateAccessPolicy(resourceGroupName, vaultName, operationKind, apiVersion, subscriptionId, parameters)



Update access policies in a key vault in the specified subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VaultsApi apiInstance = new VaultsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
    String vaultName = "vaultName_example"; // String | Name of the vault
    String operationKind = "add"; // String | Name of the operation
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VaultAccessPolicyParameters parameters = new VaultAccessPolicyParameters(); // VaultAccessPolicyParameters | Access policy to merge into the vault
    try {
      VaultAccessPolicyParameters result = apiInstance.vaultsUpdateAccessPolicy(resourceGroupName, vaultName, operationKind, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultsApi#vaultsUpdateAccessPolicy");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the vault belongs. | |
| **vaultName** | **String**| Name of the vault | |
| **operationKind** | **String**| Name of the operation | [enum: add, replace, remove] |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**VaultAccessPolicyParameters**](VaultAccessPolicyParameters.md)| Access policy to merge into the vault | |

### Return type

[**VaultAccessPolicyParameters**](VaultAccessPolicyParameters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated access policies |  -  |
| **201** | The updated access policies |  -  |

