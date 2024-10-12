# NameAvailabilityApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkNameAvailability**](NameAvailabilityApi.md#checkNameAvailability) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/checkNameAvailability | Check availability of EngagementFabric resource |


<a id="checkNameAvailability"></a>
# **checkNameAvailability**
> CheckNameAvailabilityResult checkNameAvailability(subscriptionId, resourceGroupName, apiVersion, parameters)

Check availability of EngagementFabric resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NameAvailabilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    NameAvailabilityApi apiInstance = new NameAvailabilityApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
    String apiVersion = "apiVersion_example"; // String | API version
    CheckNameAvailabilityParameter parameters = new CheckNameAvailabilityParameter(); // CheckNameAvailabilityParameter | Parameter describing the name to be checked
    try {
      CheckNameAvailabilityResult result = apiInstance.checkNameAvailability(subscriptionId, resourceGroupName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NameAvailabilityApi#checkNameAvailability");
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
| **subscriptionId** | **String**| Subscription ID | |
| **resourceGroupName** | **String**| Resource Group Name | |
| **apiVersion** | **String**| API version | |
| **parameters** | [**CheckNameAvailabilityParameter**](CheckNameAvailabilityParameter.md)| Parameter describing the name to be checked | |

### Return type

[**CheckNameAvailabilityResult**](CheckNameAvailabilityResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

