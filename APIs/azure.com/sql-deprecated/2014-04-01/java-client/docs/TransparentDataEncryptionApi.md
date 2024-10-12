# TransparentDataEncryptionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**transparentDataEncryptionConfigurationsListByDatabase**](TransparentDataEncryptionApi.md#transparentDataEncryptionConfigurationsListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption |  |


<a id="transparentDataEncryptionConfigurationsListByDatabase"></a>
# **transparentDataEncryptionConfigurationsListByDatabase**
> TransparentDataEncryptionListResult transparentDataEncryptionConfigurationsListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName)



Gets a list of a database&#39;s transparent data encryption configurations. There is only ever one element, named &#39;current&#39;, so GetTransparentDataEncryptionConfiguration should be used instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransparentDataEncryptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TransparentDataEncryptionApi apiInstance = new TransparentDataEncryptionApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database for which the transparent data encryption applies.
    try {
      TransparentDataEncryptionListResult result = apiInstance.transparentDataEncryptionConfigurationsListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransparentDataEncryptionApi#transparentDataEncryptionConfigurationsListByDatabase");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database for which the transparent data encryption applies. | |

### Return type

[**TransparentDataEncryptionListResult**](TransparentDataEncryptionListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

