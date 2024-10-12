# ImpactedResourcesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**impactedResourcesListBySubscriptionId**](ImpactedResourcesApi.md#impactedResourcesListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ResourceHealth/impactedResources |  |


<a id="impactedResourcesListBySubscriptionId"></a>
# **impactedResourcesListBySubscriptionId**
> ImpactedResourceListResult impactedResourcesListBySubscriptionId(apiVersion, subscriptionId, $filter)



Lists the current availability status for impacted resources in the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImpactedResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ImpactedResourcesApi apiInstance = new ImpactedResourcesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
    try {
      ImpactedResourceListResult result = apiInstance.impactedResourcesListBySubscriptionId(apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImpactedResourcesApi#impactedResourcesListBySubscriptionId");
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
| **$filter** | **String**| The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN | [optional] |

### Return type

[**ImpactedResourceListResult**](ImpactedResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of current availability status for impacted resources in the subscription |  -  |
| **0** | DefaultErrorResponse |  -  |

