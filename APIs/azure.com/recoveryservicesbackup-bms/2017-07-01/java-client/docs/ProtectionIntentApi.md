# ProtectionIntentApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protectionIntentCreateOrUpdate**](ProtectionIntentApi.md#protectionIntentCreateOrUpdate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/backupProtectionIntent/{intentObjectName} |  |
| [**protectionIntentDelete**](ProtectionIntentApi.md#protectionIntentDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/backupProtectionIntent/{intentObjectName} |  |
| [**protectionIntentGet**](ProtectionIntentApi.md#protectionIntentGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/backupProtectionIntent/{intentObjectName} |  |
| [**protectionIntentValidate**](ProtectionIntentApi.md#protectionIntentValidate) | **POST** /Subscriptions/{subscriptionId}/providers/Microsoft.RecoveryServices/locations/{azureRegion}/backupPreValidateProtection | It will validate followings  1. Vault capacity  2. VM is already protected  3. Any VM related configuration passed in properties. |


<a id="protectionIntentCreateOrUpdate"></a>
# **protectionIntentCreateOrUpdate**
> ProtectionIntentResource protectionIntentCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, intentObjectName, parameters)



Create Intent for Enabling backup of an item. This is a synchronous operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectionIntentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectionIntentApi apiInstance = new ProtectionIntentApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name associated with the backup item.
    String intentObjectName = "intentObjectName_example"; // String | Intent object name.
    ProtectionIntentResource parameters = new ProtectionIntentResource(); // ProtectionIntentResource | resource backed up item
    try {
      ProtectionIntentResource result = apiInstance.protectionIntentCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, intentObjectName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectionIntentApi#protectionIntentCreateOrUpdate");
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
| **intentObjectName** | **String**| Intent object name. | |
| **parameters** | [**ProtectionIntentResource**](ProtectionIntentResource.md)| resource backed up item | |

### Return type

[**ProtectionIntentResource**](ProtectionIntentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="protectionIntentDelete"></a>
# **protectionIntentDelete**
> protectionIntentDelete(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, intentObjectName)



Used to remove intent from an item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectionIntentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectionIntentApi apiInstance = new ProtectionIntentApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name associated with the intent.
    String intentObjectName = "intentObjectName_example"; // String | Intent to be deleted.
    try {
      apiInstance.protectionIntentDelete(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, intentObjectName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectionIntentApi#protectionIntentDelete");
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
| **fabricName** | **String**| Fabric name associated with the intent. | |
| **intentObjectName** | **String**| Intent to be deleted. | |

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
| **204** | NoContent |  -  |

<a id="protectionIntentGet"></a>
# **protectionIntentGet**
> ProtectionIntentResource protectionIntentGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, intentObjectName)



Provides the details of the protection intent up item. This is an asynchronous operation. To know the status of the operation,  call the GetItemOperationResult API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectionIntentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectionIntentApi apiInstance = new ProtectionIntentApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name associated with the backed up item.
    String intentObjectName = "intentObjectName_example"; // String | Backed up item name whose details are to be fetched.
    try {
      ProtectionIntentResource result = apiInstance.protectionIntentGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, intentObjectName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectionIntentApi#protectionIntentGet");
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
| **intentObjectName** | **String**| Backed up item name whose details are to be fetched. | |

### Return type

[**ProtectionIntentResource**](ProtectionIntentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="protectionIntentValidate"></a>
# **protectionIntentValidate**
> PreValidateEnableBackupResponse protectionIntentValidate(apiVersion, azureRegion, subscriptionId, parameters)

It will validate followings  1. Vault capacity  2. VM is already protected  3. Any VM related configuration passed in properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectionIntentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectionIntentApi apiInstance = new ProtectionIntentApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String azureRegion = "azureRegion_example"; // String | Azure region to hit Api
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    PreValidateEnableBackupRequest parameters = new PreValidateEnableBackupRequest(); // PreValidateEnableBackupRequest | Enable backup validation request on Virtual Machine
    try {
      PreValidateEnableBackupResponse result = apiInstance.protectionIntentValidate(apiVersion, azureRegion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectionIntentApi#protectionIntentValidate");
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
| **azureRegion** | **String**| Azure region to hit Api | |
| **subscriptionId** | **String**| The subscription Id. | |
| **parameters** | [**PreValidateEnableBackupRequest**](PreValidateEnableBackupRequest.md)| Enable backup validation request on Virtual Machine | |

### Return type

[**PreValidateEnableBackupResponse**](PreValidateEnableBackupResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

