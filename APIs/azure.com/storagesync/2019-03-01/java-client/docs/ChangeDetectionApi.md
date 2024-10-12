# ChangeDetectionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudEndpointsTriggerChangeDetection_1**](ChangeDetectionApi.md#cloudEndpointsTriggerChangeDetection_1) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/triggerChangeDetection |  |


<a id="cloudEndpointsTriggerChangeDetection_1"></a>
# **cloudEndpointsTriggerChangeDetection_1**
> cloudEndpointsTriggerChangeDetection_1(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Triggers detection of changes performed on Azure File share connected to the specified Azure File Sync Cloud Endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangeDetectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ChangeDetectionApi apiInstance = new ChangeDetectionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
    String cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
    TriggerChangeDetectionParameters parameters = new TriggerChangeDetectionParameters(); // TriggerChangeDetectionParameters | Trigger Change Detection Action parameters.
    try {
      apiInstance.cloudEndpointsTriggerChangeDetection_1(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangeDetectionApi#cloudEndpointsTriggerChangeDetection_1");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | |
| **syncGroupName** | **String**| Name of Sync Group resource. | |
| **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | |
| **parameters** | [**TriggerChangeDetectionParameters**](TriggerChangeDetectionParameters.md)| Trigger Change Detection Action parameters. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **202** | Asynchronous Operation Status Location |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  * Location - Operation Status Location URI <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

