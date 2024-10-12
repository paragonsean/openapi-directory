# ProtectionPolicyOperationStatusesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protectionPolicyOperationStatusesGet**](ProtectionPolicyOperationStatusesApi.md#protectionPolicyOperationStatusesGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies/{policyName}/operations/{operationId} |  |


<a id="protectionPolicyOperationStatusesGet"></a>
# **protectionPolicyOperationStatusesGet**
> OperationStatus protectionPolicyOperationStatusesGet(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, operationId)



Provides the status of the asynchronous operations like backup, restore. The status can be in progress, completed  or failed. You can refer to the Operation Status enum for all the possible states of an operation. Some operations  create jobs. This method returns the list of jobs associated with operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectionPolicyOperationStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectionPolicyOperationStatusesApi apiInstance = new ProtectionPolicyOperationStatusesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String policyName = "policyName_example"; // String | Backup policy name whose operation's status needs to be fetched.
    String operationId = "operationId_example"; // String | Operation ID which represents an operation whose status needs to be fetched.
    try {
      OperationStatus result = apiInstance.protectionPolicyOperationStatusesGet(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectionPolicyOperationStatusesApi#protectionPolicyOperationStatusesGet");
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
| **policyName** | **String**| Backup policy name whose operation&#39;s status needs to be fetched. | |
| **operationId** | **String**| Operation ID which represents an operation whose status needs to be fetched. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

