# CommerceApi

All URIs are relative to *https://management.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subscriberUsageAggregatesList**](CommerceApi.md#subscriberUsageAggregatesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Commerce/subscriberUsageAggregates |  |


<a id="subscriberUsageAggregatesList"></a>
# **subscriberUsageAggregatesList**
> UsageAggregatePage subscriberUsageAggregatesList(subscriptionId, apiVersion, reportedStartTime, reportedEndTime, aggregationGranularity, subscriberId, continuationToken)



Gets a collection of SubscriberUsageAggregates, which are UsageAggregates from direct tenants.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommerceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CommerceApi apiInstance = new CommerceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String apiVersion = "2015-06-01-preview"; // String | Client Api Version.
    OffsetDateTime reportedStartTime = OffsetDateTime.now(); // OffsetDateTime | The reported start time (inclusive).
    OffsetDateTime reportedEndTime = OffsetDateTime.now(); // OffsetDateTime | The reported end time (exclusive).
    String aggregationGranularity = "aggregationGranularity_example"; // String | The aggregation granularity.
    String subscriberId = "subscriberId_example"; // String | The tenant subscription identifier.
    String continuationToken = "continuationToken_example"; // String | The continuation token.
    try {
      UsageAggregatePage result = apiInstance.subscriberUsageAggregatesList(subscriptionId, apiVersion, reportedStartTime, reportedEndTime, aggregationGranularity, subscriberId, continuationToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommerceApi#subscriberUsageAggregatesList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-06-01-preview] |
| **reportedStartTime** | **OffsetDateTime**| The reported start time (inclusive). | |
| **reportedEndTime** | **OffsetDateTime**| The reported end time (exclusive). | |
| **aggregationGranularity** | **String**| The aggregation granularity. | [optional] |
| **subscriberId** | **String**| The tenant subscription identifier. | [optional] |
| **continuationToken** | **String**| The continuation token. | [optional] |

### Return type

[**UsageAggregatePage**](UsageAggregatePage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

