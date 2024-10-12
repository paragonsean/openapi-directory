# ManagedInstanceKeysApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managedInstanceKeysCreateOrUpdate**](ManagedInstanceKeysApi.md#managedInstanceKeysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/keys/{keyName} |  |
| [**managedInstanceKeysDelete**](ManagedInstanceKeysApi.md#managedInstanceKeysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/keys/{keyName} |  |
| [**managedInstanceKeysGet**](ManagedInstanceKeysApi.md#managedInstanceKeysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/keys/{keyName} |  |
| [**managedInstanceKeysListByInstance**](ManagedInstanceKeysApi.md#managedInstanceKeysListByInstance) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/keys |  |


<a id="managedInstanceKeysCreateOrUpdate"></a>
# **managedInstanceKeysCreateOrUpdate**
> ManagedInstanceKey managedInstanceKeysCreateOrUpdate(resourceGroupName, managedInstanceName, keyName, subscriptionId, apiVersion, parameters)



Creates or updates a managed instance key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedInstanceKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedInstanceKeysApi apiInstance = new ManagedInstanceKeysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String keyName = "keyName_example"; // String | The name of the managed instance key to be operated on (updated or created).
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    ManagedInstanceKey parameters = new ManagedInstanceKey(); // ManagedInstanceKey | The requested managed instance key resource state.
    try {
      ManagedInstanceKey result = apiInstance.managedInstanceKeysCreateOrUpdate(resourceGroupName, managedInstanceName, keyName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedInstanceKeysApi#managedInstanceKeysCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **managedInstanceName** | **String**| The name of the managed instance. | |
| **keyName** | **String**| The name of the managed instance key to be operated on (updated or created). | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**ManagedInstanceKey**](ManagedInstanceKey.md)| The requested managed instance key resource state. | |

### Return type

[**ManagedInstanceKey**](ManagedInstanceKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the managed instance key. |  -  |
| **201** | Successfully created the managed instance key. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidKeyName - An invalid value was given for the server key name.   * 400 InvalidKeyType - The create server key type is not supported.   * 400 InvalidUpsertKeyType - Service Managed type keys are managed by Azure SQL. This key type does not support create or update by the user.   * 400 InvalidKeyUpsertRequest - The create server key request does not exist or has no properties object.   * 400 AzureKeyVaultInvalidExpirationDate - The operation could not be completed because the Azure Key Vault key expiration date is invalid.   * 400 SecurityAzureKeyVaultUrlNullOrEmpty - The operation could not be completed because the Azure Key Vault Uri is null or empty.   * 400 AzureKeyVaultInvalidUri - An invalid response from Azure Key Vault. Please use a valid Azure Key Vault URI.   * 400 SecurityAzureKeyVaultInvalidKeyName - The operation could not be completed because of an invalid Server Key name.   * 400 AzureKeyVaultMalformedVaultUri - The provided Key Vault uri is not valid.   * 400 SecurityAdalPrincipalCertExpiredError - The operation could not be completed because the Azure Key Vault principal certificate has expired.   * 400 SecurityInvalidAzureKeyVaultRecoveryLevel - The provided Key Vault uri is not valid.   * 400 KeyMaterialNotFoundOnRemoteServer - Remote server does not have access to key material used as a TDE protector.   * 400 AzureKeyVaultMismatchError - Unexpected Key Vault region found in the http response.   * 400 AzureKeyVaultRsaKeyNotSupported - The provided key vault uses unsupported RSA Key Size or Key Type. The supported RSA key size is 2048 and Key Type is RSA.   * 401 AzureKeyVaultKeyDisabled - The operation could not be completed on the server because the Azure Key Vault key is disabled.   * 401 AzureKeyVaultNoServerIdentity - The server identity is not correctly configured.   * 401 AzureKeyVaultMissingPermissions - The server is missing required permissions on the Azure Key Vault.    * 401 AdalGenericError - The operation could not be completed because an Azure Active Directory error was encountered.   * 401 AdalServicePrincipalNotFound - The operation could not be completed because an Azure Active Directory library Service Principal not found error was encountered.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found.   * 409 ServerKeyNameAlreadyExists - The server key already exists on the server.   * 409 ServerKeyUriAlreadyExists - The server key URI already exists on the server.   * 409 ServerKeyDoesNotExists - The server key does not exist.   * 409 AzureKeyVaultKeyNameNotFound - The operation could not be completed because the Azure Key Vault Key name does not exist.   * 409 AzureKeyVaultKeyInUse - The key is currently being used by the server.   * 503 AzureKeyVaultConnectionFailed - The operation could not be completed on the server because attempts to connect to Azure Key Vault have failed   * 503 AzureKeyVaultGenericConnectionError - The operation could not be completed because an error was encountered when attempting to retrieve Key Vault information . |  -  |

<a id="managedInstanceKeysDelete"></a>
# **managedInstanceKeysDelete**
> managedInstanceKeysDelete(resourceGroupName, managedInstanceName, keyName, subscriptionId, apiVersion)



Deletes the managed instance key with the given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedInstanceKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedInstanceKeysApi apiInstance = new ManagedInstanceKeysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String keyName = "keyName_example"; // String | The name of the managed instance key to be deleted.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.managedInstanceKeysDelete(resourceGroupName, managedInstanceName, keyName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedInstanceKeysApi#managedInstanceKeysDelete");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **managedInstanceName** | **String**| The name of the managed instance. | |
| **keyName** | **String**| The name of the managed instance key to be deleted. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

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
| **200** | Successfully deleted the managed instance key. |  -  |
| **202** | Accepted |  -  |
| **204** | The specified managed instance key does not exist. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidKeyName - An invalid value was given for the server key name.   * 400 InvalidKeyType - The create server key type is not supported.   * 400 InvalidUpsertKeyType - Service Managed type keys are managed by Azure SQL. This key type does not support create or update by the user.   * 400 InvalidKeyUpsertRequest - The create server key request does not exist or has no properties object.   * 400 AzureKeyVaultInvalidExpirationDate - The operation could not be completed because the Azure Key Vault key expiration date is invalid.   * 400 SecurityAzureKeyVaultUrlNullOrEmpty - The operation could not be completed because the Azure Key Vault Uri is null or empty.   * 400 AzureKeyVaultInvalidUri - An invalid response from Azure Key Vault. Please use a valid Azure Key Vault URI.   * 400 SecurityAzureKeyVaultInvalidKeyName - The operation could not be completed because of an invalid Server Key name.   * 400 AzureKeyVaultMalformedVaultUri - The provided Key Vault uri is not valid.   * 400 SecurityAdalPrincipalCertExpiredError - The operation could not be completed because the Azure Key Vault principal certificate has expired.   * 400 SecurityInvalidAzureKeyVaultRecoveryLevel - The provided Key Vault uri is not valid.   * 400 KeyMaterialNotFoundOnRemoteServer - Remote server does not have access to key material used as a TDE protector.   * 400 AzureKeyVaultMismatchError - Unexpected Key Vault region found in the http response.   * 400 AzureKeyVaultRsaKeyNotSupported - The provided key vault uses unsupported RSA Key Size or Key Type. The supported RSA key size is 2048 and Key Type is RSA.   * 401 AzureKeyVaultKeyDisabled - The operation could not be completed on the server because the Azure Key Vault key is disabled.   * 401 AzureKeyVaultNoServerIdentity - The server identity is not correctly configured.   * 401 AzureKeyVaultMissingPermissions - The server is missing required permissions on the Azure Key Vault.    * 401 AdalGenericError - The operation could not be completed because an Azure Active Directory error was encountered.   * 401 AdalServicePrincipalNotFound - The operation could not be completed because an Azure Active Directory library Service Principal not found error was encountered.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found.   * 409 ServerKeyNameAlreadyExists - The server key already exists on the server.   * 409 ServerKeyUriAlreadyExists - The server key URI already exists on the server.   * 409 ServerKeyDoesNotExists - The server key does not exist.   * 409 AzureKeyVaultKeyNameNotFound - The operation could not be completed because the Azure Key Vault Key name does not exist.   * 409 AzureKeyVaultKeyInUse - The key is currently being used by the server.   * 503 AzureKeyVaultConnectionFailed - The operation could not be completed on the server because attempts to connect to Azure Key Vault have failed   * 503 AzureKeyVaultGenericConnectionError - The operation could not be completed because an error was encountered when attempting to retrieve Key Vault information . |  -  |

<a id="managedInstanceKeysGet"></a>
# **managedInstanceKeysGet**
> ManagedInstanceKey managedInstanceKeysGet(resourceGroupName, managedInstanceName, keyName, subscriptionId, apiVersion)



Gets a managed instance key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedInstanceKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedInstanceKeysApi apiInstance = new ManagedInstanceKeysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String keyName = "keyName_example"; // String | The name of the managed instance key to be retrieved.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ManagedInstanceKey result = apiInstance.managedInstanceKeysGet(resourceGroupName, managedInstanceName, keyName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedInstanceKeysApi#managedInstanceKeysGet");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **managedInstanceName** | **String**| The name of the managed instance. | |
| **keyName** | **String**| The name of the managed instance key to be retrieved. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ManagedInstanceKey**](ManagedInstanceKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified managed instance key. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidKeyName - An invalid value was given for the server key name.   * 400 InvalidKeyType - The create server key type is not supported.   * 400 InvalidUpsertKeyType - Service Managed type keys are managed by Azure SQL. This key type does not support create or update by the user.   * 400 InvalidKeyUpsertRequest - The create server key request does not exist or has no properties object.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="managedInstanceKeysListByInstance"></a>
# **managedInstanceKeysListByInstance**
> ManagedInstanceKeyListResult managedInstanceKeysListByInstance(resourceGroupName, managedInstanceName, subscriptionId, apiVersion, $filter)



Gets a list of managed instance keys.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedInstanceKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedInstanceKeysApi apiInstance = new ManagedInstanceKeysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String $filter = "$filter_example"; // String | An OData filter expression that filters elements in the collection.
    try {
      ManagedInstanceKeyListResult result = apiInstance.managedInstanceKeysListByInstance(resourceGroupName, managedInstanceName, subscriptionId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedInstanceKeysApi#managedInstanceKeysListByInstance");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **managedInstanceName** | **String**| The name of the managed instance. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **$filter** | **String**| An OData filter expression that filters elements in the collection. | [optional] |

### Return type

[**ManagedInstanceKeyListResult**](ManagedInstanceKeyListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of managed instance keys. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidKeyName - An invalid value was given for the server key name.   * 400 InvalidKeyType - The create server key type is not supported.   * 400 InvalidUpsertKeyType - Service Managed type keys are managed by Azure SQL. This key type does not support create or update by the user.   * 400 InvalidKeyUpsertRequest - The create server key request does not exist or has no properties object.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

