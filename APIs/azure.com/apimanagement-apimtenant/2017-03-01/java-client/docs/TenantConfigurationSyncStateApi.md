# TenantConfigurationSyncStateApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tenantConfigurationGetSyncState**](TenantConfigurationSyncStateApi.md#tenantConfigurationGetSyncState) | **GET** /tenant/{configurationName}/syncState |  |


<a id="tenantConfigurationGetSyncState"></a>
# **tenantConfigurationGetSyncState**
> TenantConfigurationSyncStateContract tenantConfigurationGetSyncState(apiVersion, configurationName)



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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    TenantConfigurationSyncStateApi apiInstance = new TenantConfigurationSyncStateApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String configurationName = "configuration"; // String | The identifier of the Git Configuration Operation.
    try {
      TenantConfigurationSyncStateContract result = apiInstance.tenantConfigurationGetSyncState(apiVersion, configurationName);
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **configurationName** | **String**| The identifier of the Git Configuration Operation. | [enum: configuration] |

### Return type

[**TenantConfigurationSyncStateContract**](TenantConfigurationSyncStateContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sync state result. |  -  |

