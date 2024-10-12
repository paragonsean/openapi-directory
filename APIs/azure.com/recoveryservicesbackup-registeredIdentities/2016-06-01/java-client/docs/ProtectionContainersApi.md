# ProtectionContainersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protectionContainersUnregister**](ProtectionContainersApi.md#protectionContainersUnregister) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/registeredIdentities/{identityName} |  |


<a id="protectionContainersUnregister"></a>
# **protectionContainersUnregister**
> protectionContainersUnregister(subscriptionId, resourceGroupName, vaultName, apiVersion, identityName)



Unregisters the given container from your Recovery Services vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectionContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectionContainersApi apiInstance = new ProtectionContainersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
    String vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String identityName = "identityName_example"; // String | Name of the protection container to unregister.
    try {
      apiInstance.protectionContainersUnregister(subscriptionId, resourceGroupName, vaultName, apiVersion, identityName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectionContainersApi#protectionContainersUnregister");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | |
| **vaultName** | **String**| The name of the Recovery Services vault. | |
| **apiVersion** | **String**| Client API version. | |
| **identityName** | **String**| Name of the protection container to unregister. | |

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

