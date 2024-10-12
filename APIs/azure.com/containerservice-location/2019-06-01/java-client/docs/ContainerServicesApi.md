# ContainerServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**containerServicesListOrchestrators**](ContainerServicesApi.md#containerServicesListOrchestrators) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ContainerService/locations/{location}/orchestrators | Gets a list of supported orchestrators in the specified subscription. |


<a id="containerServicesListOrchestrators"></a>
# **containerServicesListOrchestrators**
> OrchestratorVersionProfileListResult containerServicesListOrchestrators(apiVersion, subscriptionId, location, resourceType)

Gets a list of supported orchestrators in the specified subscription.

Gets a list of supported orchestrators in the specified subscription. The operation returns properties of each orchestrator including version, available upgrades and whether that version or upgrades are in preview.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainerServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ContainerServicesApi apiInstance = new ContainerServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | The name of a supported Azure region.
    String resourceType = "resourceType_example"; // String | resource type for which the list of orchestrators needs to be returned
    try {
      OrchestratorVersionProfileListResult result = apiInstance.containerServicesListOrchestrators(apiVersion, subscriptionId, location, resourceType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainerServicesApi#containerServicesListOrchestrators");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| The name of a supported Azure region. | |
| **resourceType** | **String**| resource type for which the list of orchestrators needs to be returned | [optional] |

### Return type

[**OrchestratorVersionProfileListResult**](OrchestratorVersionProfileListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

