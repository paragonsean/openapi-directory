# VaultsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vaultsCreateOrUpdate**](VaultsApi.md#vaultsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName} |  |
| [**vaultsDelete**](VaultsApi.md#vaultsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName} |  |
| [**vaultsGet**](VaultsApi.md#vaultsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName} |  |
| [**vaultsList**](VaultsApi.md#vaultsList) | **GET** /subscriptions/{subscriptionId}/resources |  |
| [**vaultsListByResourceGroup**](VaultsApi.md#vaultsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults |  |


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
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
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
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
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
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
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

