# ReplicationEligibilityResultsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**replicationEligibilityResultsGet**](ReplicationEligibilityResultsApi.md#replicationEligibilityResultsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{virtualMachineName}/providers/Microsoft.RecoveryServices/replicationEligibilityResults/default | Gets the validation errors in case the VM is unsuitable for protection. |
| [**replicationEligibilityResultsList**](ReplicationEligibilityResultsApi.md#replicationEligibilityResultsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{virtualMachineName}/providers/Microsoft.RecoveryServices/replicationEligibilityResults | Gets the validation errors in case the VM is unsuitable for protection. |


<a id="replicationEligibilityResultsGet"></a>
# **replicationEligibilityResultsGet**
> ReplicationEligibilityResults replicationEligibilityResultsGet(apiVersion, resourceGroupName, subscriptionId, virtualMachineName)

Gets the validation errors in case the VM is unsuitable for protection.

Validates whether a given VM can be protected or not in which case returns list of errors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationEligibilityResultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationEligibilityResultsApi apiInstance = new ReplicationEligibilityResultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String virtualMachineName = "virtualMachineName_example"; // String | Virtual Machine name.
    try {
      ReplicationEligibilityResults result = apiInstance.replicationEligibilityResultsGet(apiVersion, resourceGroupName, subscriptionId, virtualMachineName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationEligibilityResultsApi#replicationEligibilityResultsGet");
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
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **virtualMachineName** | **String**| Virtual Machine name. | |

### Return type

[**ReplicationEligibilityResults**](ReplicationEligibilityResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationEligibilityResultsList"></a>
# **replicationEligibilityResultsList**
> ReplicationEligibilityResultsCollection replicationEligibilityResultsList(apiVersion, resourceGroupName, subscriptionId, virtualMachineName)

Gets the validation errors in case the VM is unsuitable for protection.

Validates whether a given VM can be protected or not in which case returns list of errors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationEligibilityResultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationEligibilityResultsApi apiInstance = new ReplicationEligibilityResultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String virtualMachineName = "virtualMachineName_example"; // String | Virtual Machine name.
    try {
      ReplicationEligibilityResultsCollection result = apiInstance.replicationEligibilityResultsList(apiVersion, resourceGroupName, subscriptionId, virtualMachineName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationEligibilityResultsApi#replicationEligibilityResultsList");
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
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **virtualMachineName** | **String**| Virtual Machine name. | |

### Return type

[**ReplicationEligibilityResultsCollection**](ReplicationEligibilityResultsCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

