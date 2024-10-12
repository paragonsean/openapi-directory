# ProtectionPolicyOperationResultsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protectionPolicyOperationResultsGet**](ProtectionPolicyOperationResultsApi.md#protectionPolicyOperationResultsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies/{policyName}/operationResults/{operationId} |  |


<a id="protectionPolicyOperationResultsGet"></a>
# **protectionPolicyOperationResultsGet**
> ProtectionPolicyResource protectionPolicyOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, operationId)



Provides the result of an operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectionPolicyOperationResultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectionPolicyOperationResultsApi apiInstance = new ProtectionPolicyOperationResultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String policyName = "policyName_example"; // String | The backup policy name used in this GET operation.
    String operationId = "operationId_example"; // String | The ID associated with this GET operation.
    try {
      ProtectionPolicyResource result = apiInstance.protectionPolicyOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectionPolicyOperationResultsApi#protectionPolicyOperationResultsGet");
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
| **operationId** | **String**| The ID associated with this GET operation. | |

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

