# EventHubsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventHubsListByNamespace**](EventHubsApi.md#eventHubsListByNamespace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/eventhubs |  |


<a id="eventHubsListByNamespace"></a>
# **eventHubsListByNamespace**
> EventHubListResult eventHubsListByNamespace(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Gets all the Event Hubs in a service bus Namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventHubsApi apiInstance = new EventHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      EventHubListResult result = apiInstance.eventHubsListByNamespace(resourceGroupName, namespaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubsApi#eventHubsListByNamespace");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**EventHubListResult**](EventHubListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of Event Hubs. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

