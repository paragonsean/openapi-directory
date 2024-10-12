# TriggerApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**triggersGet**](TriggerApi.md#triggersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName} |  |


<a id="triggersGet"></a>
# **triggersGet**
> TriggerResource triggersGet(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion)



Gets a trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggerApi apiInstance = new TriggerApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String triggerName = "triggerName_example"; // String | The trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      TriggerResource result = apiInstance.triggersGet(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggerApi#triggersGet");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **triggerName** | **String**| The trigger name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**TriggerResource**](TriggerResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

