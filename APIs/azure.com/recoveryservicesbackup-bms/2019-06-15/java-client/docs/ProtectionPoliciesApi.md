# ProtectionPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protectionPoliciesCreateOrUpdate**](ProtectionPoliciesApi.md#protectionPoliciesCreateOrUpdate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies/{policyName} |  |
| [**protectionPoliciesGet**](ProtectionPoliciesApi.md#protectionPoliciesGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies/{policyName} |  |


<a id="protectionPoliciesCreateOrUpdate"></a>
# **protectionPoliciesCreateOrUpdate**
> ProtectionPolicyResource protectionPoliciesCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, parameters)



Creates or modifies a backup policy. This is an asynchronous operation. Status of the operation can be fetched  using GetPolicyOperationResult API.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String policyName = "policyName_example"; // String | Backup policy to be created.
    ProtectionPolicyResource parameters = new ProtectionPolicyResource(); // ProtectionPolicyResource | resource backup policy
    try {
      ProtectionPolicyResource result = apiInstance.protectionPoliciesCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, parameters);
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
| **apiVersion** | **String**| Client Api Version. | |
| **vaultName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **policyName** | **String**| Backup policy to be created. | |
| **parameters** | [**ProtectionPolicyResource**](ProtectionPolicyResource.md)| resource backup policy | |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="protectionPoliciesGet"></a>
# **protectionPoliciesGet**
> ProtectionPolicyResource protectionPoliciesGet(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName)



Provides the details of the backup policies associated to Recovery Services Vault. This is an asynchronous  operation. Status of the operation can be fetched using GetPolicyOperationResult API.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String policyName = "policyName_example"; // String | Backup policy information to be fetched.
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
| **apiVersion** | **String**| Client Api Version. | |
| **vaultName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **policyName** | **String**| Backup policy information to be fetched. | |

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
| **200** | OK |  -  |

