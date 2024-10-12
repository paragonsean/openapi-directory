# TenantConfigurationSyncStateApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tenantConfigurationGetSyncState**](TenantConfigurationSyncStateApi.md#tenantConfigurationGetSyncState) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tenant/{configurationName}/syncState |  |


<a id="tenantConfigurationGetSyncState"></a>
# **tenantConfigurationGetSyncState**
> TenantConfigurationSyncStateContract tenantConfigurationGetSyncState(resourceGroupName, serviceName, apiVersion, subscriptionId, configurationName)



Gets the status of the most recent synchronization between the configuration database and the Git repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenantConfigurationSyncStateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TenantConfigurationSyncStateApi apiInstance = new TenantConfigurationSyncStateApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String configurationName = "configuration"; // String | The identifier of the Git Configuration Operation.
    try {
      TenantConfigurationSyncStateContract result = apiInstance.tenantConfigurationGetSyncState(resourceGroupName, serviceName, apiVersion, subscriptionId, configurationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenantConfigurationSyncStateApi#tenantConfigurationGetSyncState");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **configurationName** | **String**| The identifier of the Git Configuration Operation. | [enum: configuration] |

### Return type

[**TenantConfigurationSyncStateContract**](TenantConfigurationSyncStateContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sync state result. |  -  |

