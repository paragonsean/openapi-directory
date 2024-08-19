# EncryptionProtectorsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**encryptionProtectorsCreateOrUpdate**](EncryptionProtectorsApi.md#encryptionProtectorsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/encryptionProtector/{encryptionProtectorName} |  |
| [**encryptionProtectorsGet**](EncryptionProtectorsApi.md#encryptionProtectorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/encryptionProtector/{encryptionProtectorName} |  |
| [**encryptionProtectorsListByServer**](EncryptionProtectorsApi.md#encryptionProtectorsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/encryptionProtector |  |
| [**encryptionProtectorsRevalidate**](EncryptionProtectorsApi.md#encryptionProtectorsRevalidate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/encryptionProtector/{encryptionProtectorName}/revalidate |  |


<a id="encryptionProtectorsCreateOrUpdate"></a>
# **encryptionProtectorsCreateOrUpdate**
> EncryptionProtector encryptionProtectorsCreateOrUpdate(resourceGroupName, serverName, encryptionProtectorName, subscriptionId, apiVersion, parameters)



Updates an existing encryption protector.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EncryptionProtectorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EncryptionProtectorsApi apiInstance = new EncryptionProtectorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String encryptionProtectorName = "current"; // String | The name of the encryption protector to be updated.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    EncryptionProtector parameters = new EncryptionProtector(); // EncryptionProtector | The requested encryption protector resource state.
    try {
      EncryptionProtector result = apiInstance.encryptionProtectorsCreateOrUpdate(resourceGroupName, serverName, encryptionProtectorName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EncryptionProtectorsApi#encryptionProtectorsCreateOrUpdate");
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
| **serverName** | **String**| The name of the server. | |
| **encryptionProtectorName** | **String**| The name of the encryption protector to be updated. | [enum: current] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**EncryptionProtector**](EncryptionProtector.md)| The requested encryption protector resource state. | |

### Return type

[**EncryptionProtector**](EncryptionProtector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the encryption protector. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidKeyName - An invalid value was given for the server key name.   * 400 InvalidKeyType - The create server key type is not supported.   * 400 InvalidUpsertKeyType - Service Managed type keys are managed by Azure SQL. This key type does not support create or update by the user.   * 400 InvalidKeyUpsertRequest - The create server key request does not exist or has no properties object.   * 400 InvalidEncryptionProtectorName - The encryption protector key name is not supported.   * 400 SecurityAzureKeyVaultGeoChainError - Creating secondary of secondary (a process known as chaining) is not supported when enabling Transparent Data Encryption using Azure Key Vault (BYOK).   * 400 AzureKeyVaultInvalidExpirationDate - The operation could not be completed because the Azure Key Vault key expiration date is invalid.   * 400 SecurityAzureKeyVaultUrlNullOrEmpty - The operation could not be completed because the Azure Key Vault Uri is null or empty.   * 400 AzureKeyVaultInvalidUri - An invalid response from Azure Key Vault. Please use a valid Azure Key Vault URI.   * 400 SecurityAzureKeyVaultInvalidKeyName - The operation could not be completed because of an invalid Server Key name.   * 400 AzureKeyVaultMalformedVaultUri - The provided Key Vault uri is not valid.   * 400 SecurityAdalPrincipalCertExpiredError - The operation could not be completed because the Azure Key Vault principal certificate has expired.   * 400 SecurityInvalidAzureKeyVaultRecoveryLevel - The provided Key Vault uri is not valid.   * 400 KeyMaterialNotFoundOnRemoteServer - Remote server does not have access to key material used as a TDE protector.   * 400 AzureKeyVaultMismatchError - Unexpected Key Vault region found in the http response.   * 400 AzureKeyVaultRsaKeyNotSupported - The provided key vault uses unsupported RSA Key Size or Key Type. The supported RSA key size is 2048 and Key Type is RSA.   * 401 AzureKeyVaultKeyDisabled - The operation could not be completed on the server because the Azure Key Vault key is disabled.   * 401 AzureKeyVaultNoServerIdentity - The server identity is not correctly configured.   * 401 AzureKeyVaultMissingPermissions - The server is missing required permissions on the Azure Key Vault.    * 401 AdalGenericError - The operation could not be completed because an Azure Active Directory error was encountered.   * 401 AdalServicePrincipalNotFound - The operation could not be completed because an Azure Active Directory library Service Principal not found error was encountered.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found.   * 404 ServerKeyNotFound - The requested server key was not found on the current subscription.   * 409 ServerKeyNameAlreadyExists - The server key already exists on the server.   * 409 ServerKeyUriAlreadyExists - The server key URI already exists on the server.   * 409 ServerKeyDoesNotExists - The server key does not exist.   * 409 AzureKeyVaultKeyNameNotFound - The operation could not be completed because the Azure Key Vault Key name does not exist.   * 409 AzureKeyVaultKeyInUse - The key is currently being used by the server.   * 503 AzureKeyVaultConnectionFailed - The operation could not be completed on the server because attempts to connect to Azure Key Vault have failed   * 503 AzureKeyVaultGenericConnectionError - The operation could not be completed because an error was encountered when attempting to retrieve Key Vault information . |  -  |

<a id="encryptionProtectorsGet"></a>
# **encryptionProtectorsGet**
> EncryptionProtector encryptionProtectorsGet(resourceGroupName, serverName, encryptionProtectorName, subscriptionId, apiVersion)



Gets a server encryption protector.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EncryptionProtectorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EncryptionProtectorsApi apiInstance = new EncryptionProtectorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String encryptionProtectorName = "current"; // String | The name of the encryption protector to be retrieved.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      EncryptionProtector result = apiInstance.encryptionProtectorsGet(resourceGroupName, serverName, encryptionProtectorName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EncryptionProtectorsApi#encryptionProtectorsGet");
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
| **serverName** | **String**| The name of the server. | |
| **encryptionProtectorName** | **String**| The name of the encryption protector to be retrieved. | [enum: current] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**EncryptionProtector**](EncryptionProtector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified server encryption protector. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidKeyName - An invalid value was given for the server key name.   * 400 InvalidKeyType - The create server key type is not supported.   * 400 InvalidUpsertKeyType - Service Managed type keys are managed by Azure SQL. This key type does not support create or update by the user.   * 400 InvalidKeyUpsertRequest - The create server key request does not exist or has no properties object.   * 400 InvalidEncryptionProtectorName - The encryption protector key name is not supported.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="encryptionProtectorsListByServer"></a>
# **encryptionProtectorsListByServer**
> EncryptionProtectorListResult encryptionProtectorsListByServer(resourceGroupName, serverName, subscriptionId, apiVersion)



Gets a list of server encryption protectors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EncryptionProtectorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EncryptionProtectorsApi apiInstance = new EncryptionProtectorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      EncryptionProtectorListResult result = apiInstance.encryptionProtectorsListByServer(resourceGroupName, serverName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EncryptionProtectorsApi#encryptionProtectorsListByServer");
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
| **serverName** | **String**| The name of the server. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**EncryptionProtectorListResult**](EncryptionProtectorListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of server encryption protector. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidKeyName - An invalid value was given for the server key name.   * 400 InvalidKeyType - The create server key type is not supported.   * 400 InvalidUpsertKeyType - Service Managed type keys are managed by Azure SQL. This key type does not support create or update by the user.   * 400 InvalidKeyUpsertRequest - The create server key request does not exist or has no properties object.   * 400 InvalidEncryptionProtectorName - The encryption protector key name is not supported.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="encryptionProtectorsRevalidate"></a>
# **encryptionProtectorsRevalidate**
> encryptionProtectorsRevalidate(resourceGroupName, serverName, encryptionProtectorName, subscriptionId, apiVersion)



Revalidates an existing encryption protector.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EncryptionProtectorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EncryptionProtectorsApi apiInstance = new EncryptionProtectorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String encryptionProtectorName = "current"; // String | The name of the encryption protector to be updated.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.encryptionProtectorsRevalidate(resourceGroupName, serverName, encryptionProtectorName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EncryptionProtectorsApi#encryptionProtectorsRevalidate");
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
| **serverName** | **String**| The name of the server. | |
| **encryptionProtectorName** | **String**| The name of the encryption protector to be updated. | [enum: current] |
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
| **200** | Successfully revalidated the encryption protector. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidKeyName - An invalid value was given for the server key name.   * 400 InvalidKeyType - The create server key type is not supported.   * 400 InvalidUpsertKeyType - Service Managed type keys are managed by Azure SQL. This key type does not support create or update by the user.   * 400 InvalidKeyUpsertRequest - The create server key request does not exist or has no properties object.   * 400 InvalidEncryptionProtectorName - The encryption protector key name is not supported.   * 400 SecurityAzureKeyVaultGeoChainError - Creating secondary of secondary (a process known as chaining) is not supported when enabling Transparent Data Encryption using Azure Key Vault (BYOK).   * 400 AzureKeyVaultInvalidExpirationDate - The operation could not be completed because the Azure Key Vault key expiration date is invalid.   * 400 SecurityAzureKeyVaultUrlNullOrEmpty - The operation could not be completed because the Azure Key Vault Uri is null or empty.   * 400 AzureKeyVaultInvalidUri - An invalid response from Azure Key Vault. Please use a valid Azure Key Vault URI.   * 400 SecurityAzureKeyVaultInvalidKeyName - The operation could not be completed because of an invalid Server Key name.   * 400 AzureKeyVaultMalformedVaultUri - The provided Key Vault uri is not valid.   * 400 SecurityAdalPrincipalCertExpiredError - The operation could not be completed because the Azure Key Vault principal certificate has expired.   * 400 SecurityInvalidAzureKeyVaultRecoveryLevel - The provided Key Vault uri is not valid.   * 400 KeyMaterialNotFoundOnRemoteServer - Remote server does not have access to key material used as a TDE protector.   * 400 AzureKeyVaultMismatchError - Unexpected Key Vault region found in the http response.   * 400 AzureKeyVaultRsaKeyNotSupported - The provided key vault uses unsupported RSA Key Size or Key Type. The supported RSA key size is 2048 and Key Type is RSA.   * 401 AzureKeyVaultKeyDisabled - The operation could not be completed on the server because the Azure Key Vault key is disabled.   * 401 AzureKeyVaultNoServerIdentity - The server identity is not correctly configured.   * 401 AzureKeyVaultMissingPermissions - The server is missing required permissions on the Azure Key Vault.    * 401 AdalGenericError - The operation could not be completed because an Azure Active Directory error was encountered.   * 401 AdalServicePrincipalNotFound - The operation could not be completed because an Azure Active Directory library Service Principal not found error was encountered.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found.   * 404 ServerKeyNotFound - The requested server key was not found on the current subscription.   * 409 ServerKeyNameAlreadyExists - The server key already exists on the server.   * 409 ServerKeyUriAlreadyExists - The server key URI already exists on the server.   * 409 ServerKeyDoesNotExists - The server key does not exist.   * 409 AzureKeyVaultKeyNameNotFound - The operation could not be completed because the Azure Key Vault Key name does not exist.   * 409 AzureKeyVaultKeyInUse - The key is currently being used by the server.   * 503 AzureKeyVaultConnectionFailed - The operation could not be completed on the server because attempts to connect to Azure Key Vault have failed   * 503 AzureKeyVaultGenericConnectionError - The operation could not be completed because an error was encountered when attempting to retrieve Key Vault information . |  -  |

