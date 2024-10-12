# ListServiceProvidersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**botConnectionListServiceProviders**](ListServiceProvidersApi.md#botConnectionListServiceProviders) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.BotService/listAuthServiceProviders |  |


<a id="botConnectionListServiceProviders"></a>
# **botConnectionListServiceProviders**
> ServiceProviderResponseList botConnectionListServiceProviders(apiVersion, subscriptionId)



Lists the available Service Providers for creating Connection Settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListServiceProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ListServiceProvidersApi apiInstance = new ListServiceProvidersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      ServiceProviderResponseList result = apiInstance.botConnectionListServiceProviders(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListServiceProvidersApi#botConnectionListServiceProviders");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |

### Return type

[**ServiceProviderResponseList**](ServiceProviderResponseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If resource is retrieved successfully, the service should return 200 (OK). |  -  |
| **0** | Error response describing why the operation failed |  -  |

