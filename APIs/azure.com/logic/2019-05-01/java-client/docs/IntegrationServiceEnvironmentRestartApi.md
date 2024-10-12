# IntegrationServiceEnvironmentRestartApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationServiceEnvironmentsRestart**](IntegrationServiceEnvironmentRestartApi.md#integrationServiceEnvironmentsRestart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}/restart |  |


<a id="integrationServiceEnvironmentsRestart"></a>
# **integrationServiceEnvironmentsRestart**
> integrationServiceEnvironmentsRestart(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion)



Restarts an integration service environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationServiceEnvironmentRestartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationServiceEnvironmentRestartApi apiInstance = new IntegrationServiceEnvironmentRestartApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroup = "resourceGroup_example"; // String | The resource group.
    String integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationServiceEnvironmentsRestart(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationServiceEnvironmentRestartApi#integrationServiceEnvironmentsRestart");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroup** | **String**| The resource group. | |
| **integrationServiceEnvironmentName** | **String**| The integration service environment name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Logic error response describing why the operation failed. |  -  |

