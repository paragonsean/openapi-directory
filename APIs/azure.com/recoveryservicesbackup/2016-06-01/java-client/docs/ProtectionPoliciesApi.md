# ProtectionPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protectionPoliciesCreateOrUpdate**](ProtectionPoliciesApi.md#protectionPoliciesCreateOrUpdate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies/{policyName} |  |
| [**protectionPoliciesDelete**](ProtectionPoliciesApi.md#protectionPoliciesDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies/{policyName} |  |
| [**protectionPoliciesGet**](ProtectionPoliciesApi.md#protectionPoliciesGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies/{policyName} |  |
| [**protectionPoliciesList**](ProtectionPoliciesApi.md#protectionPoliciesList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies |  |


<a id="protectionPoliciesCreateOrUpdate"></a>
# **protectionPoliciesCreateOrUpdate**
> ProtectionPolicyResource protectionPoliciesCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, resourceProtectionPolicy)



Creates or modifies a backup policy. This is an asynchronous operation. Use the GetPolicyOperationResult API to Get the operation status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectionPoliciesApi apiInstance = new ProtectionPoliciesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String policyName = "policyName_example"; // String | The backup policy to be created.
    ProtectionPolicyResource resourceProtectionPolicy = new ProtectionPolicyResource(); // ProtectionPolicyResource | The resource backup policy.
    try {
      ProtectionPolicyResource result = apiInstance.protectionPoliciesCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, resourceProtectionPolicy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectionPoliciesApi#protectionPoliciesCreateOrUpdate");
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
| **apiVersion** | **String**| Client API version. | |
| **vaultName** | **String**| The name of the Recovery Services vault. | |
| **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **policyName** | **String**| The backup policy to be created. | |
| **resourceProtectionPolicy** | [**ProtectionPolicyResource**](ProtectionPolicyResource.md)| The resource backup policy. | |

### Return type

[**ProtectionPolicyResource**](ProtectionPolicyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **202** | Accepted. |  -  |

<a id="protectionPoliciesDelete"></a>
# **protectionPoliciesDelete**
> protectionPoliciesDelete(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName)



Deletes the specified backup policy from your Recovery Services vault. This is an asynchronous operation. Use the GetPolicyOperationResult API to Get the operation status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectionPoliciesApi apiInstance = new ProtectionPoliciesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String policyName = "policyName_example"; // String | The name of the backup policy to be deleted.
    try {
      apiInstance.protectionPoliciesDelete(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectionPoliciesApi#protectionPoliciesDelete");
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
| **apiVersion** | **String**| Client API version. | |
| **vaultName** | **String**| The name of the Recovery Services vault. | |
| **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **policyName** | **String**| The name of the backup policy to be deleted. | |

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
| **200** | OK. |  -  |
| **204** | No content. |  -  |

<a id="protectionPoliciesGet"></a>
# **protectionPoliciesGet**
> ProtectionPolicyResource protectionPoliciesGet(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName)



Gets the details of the backup policy associated with the Recovery Services vault. This is an asynchronous operation. Use the GetPolicyOperationResult API to Get the operation status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectionPoliciesApi apiInstance = new ProtectionPoliciesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String policyName = "policyName_example"; // String | The backup policy name used in this GET operation.
    try {
      ProtectionPolicyResource result = apiInstance.protectionPoliciesGet(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectionPoliciesApi#protectionPoliciesGet");
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
| **apiVersion** | **String**| Client API version. | |
| **vaultName** | **String**| The name of the Recovery Services vault. | |
| **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **policyName** | **String**| The backup policy name used in this GET operation. | |

### Return type

[**ProtectionPolicyResource**](ProtectionPolicyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |

<a id="protectionPoliciesList"></a>
# **protectionPoliciesList**
> ProtectionPolicyResourceList protectionPoliciesList(apiVersion, vaultName, resourceGroupName, subscriptionId, $filter)



Lists the backup policies associated with the Recovery Services vault. The API provides parameters to Get scoped results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectionPoliciesApi apiInstance = new ProtectionPoliciesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String $filter = "$filter_example"; // String | The following equation can be used to filter the list of backup policies. backupManagementType eq {AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql}.
    try {
      ProtectionPolicyResourceList result = apiInstance.protectionPoliciesList(apiVersion, vaultName, resourceGroupName, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectionPoliciesApi#protectionPoliciesList");
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
| **apiVersion** | **String**| Client API version. | |
| **vaultName** | **String**| The name of the Recovery Services vault. | |
| **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **$filter** | **String**| The following equation can be used to filter the list of backup policies. backupManagementType eq {AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql}. | [optional] |

### Return type

[**ProtectionPolicyResourceList**](ProtectionPolicyResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |

