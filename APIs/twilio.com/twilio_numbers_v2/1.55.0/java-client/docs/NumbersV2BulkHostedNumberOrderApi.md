# NumbersV2BulkHostedNumberOrderApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchBulkHostedNumberOrder**](NumbersV2BulkHostedNumberOrderApi.md#fetchBulkHostedNumberOrder) | **GET** /v2/HostedNumber/Orders/Bulk/{BulkHostingSid} |  |


<a id="fetchBulkHostedNumberOrder"></a>
# **fetchBulkHostedNumberOrder**
> NumbersV2BulkHostedNumberOrder fetchBulkHostedNumberOrder(bulkHostingSid, orderStatus)



Fetch a specific BulkHostedNumberOrder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2BulkHostedNumberOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2BulkHostedNumberOrderApi apiInstance = new NumbersV2BulkHostedNumberOrderApi(defaultClient);
    String bulkHostingSid = "bulkHostingSid_example"; // String | A 34 character string that uniquely identifies this BulkHostedNumberOrder.
    String orderStatus = "orderStatus_example"; // String | Order status can be used for filtering on Hosted Number Order status values. To see a complete list of order statuses, please check 'https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values'.
    try {
      NumbersV2BulkHostedNumberOrder result = apiInstance.fetchBulkHostedNumberOrder(bulkHostingSid, orderStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2BulkHostedNumberOrderApi#fetchBulkHostedNumberOrder");
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
| **bulkHostingSid** | **String**| A 34 character string that uniquely identifies this BulkHostedNumberOrder. | |
| **orderStatus** | **String**| Order status can be used for filtering on Hosted Number Order status values. To see a complete list of order statuses, please check &#39;https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values&#39;. | [optional] |

### Return type

[**NumbersV2BulkHostedNumberOrder**](NumbersV2BulkHostedNumberOrder.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

