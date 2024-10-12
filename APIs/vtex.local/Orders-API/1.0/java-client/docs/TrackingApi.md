# TrackingApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateTrackingStatus**](TrackingApi.md#updateTrackingStatus) | **PUT** /api/oms/pvt/orders/{orderId}/invoice/{invoiceNumber}/tracking | Update order tracking status |


<a id="updateTrackingStatus"></a>
# **updateTrackingStatus**
> UpdateTrackingStatus updateTrackingStatus(contentType, accept, orderId, invoiceNumber, updateTrackingStatusRequest)

Update order tracking status

This endpoint sends a tracking event to an order that already has a tracking number registered to its invoice.    This request is not meant to send tracking number and URL to the invoice. If you wish to send tracking number and URL to an order, use the [Update order&#39;s partial invoice API request](https://developers.vtex.com/docs/api-reference/orders-api#patch-/api/oms/pvt/orders/-orderId-/invoice/-invoiceNumber-). You can also learn more about [Partial invoice](https://help.vtex.com/en/tracks/partial-invoices--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe) scenarios.     &gt; The &#x60;Notify invoice&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrackingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TrackingApi apiInstance = new TrackingApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String orderId = "1172452900788-01"; // String | Order ID is a unique code that identifies an order.
    String invoiceNumber = "000030711"; // String | Number that identifies the invoice.
    UpdateTrackingStatusRequest updateTrackingStatusRequest = new UpdateTrackingStatusRequest(); // UpdateTrackingStatusRequest | 
    try {
      UpdateTrackingStatus result = apiInstance.updateTrackingStatus(contentType, accept, orderId, invoiceNumber, updateTrackingStatusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrackingApi#updateTrackingStatus");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **orderId** | **String**| Order ID is a unique code that identifies an order. | |
| **invoiceNumber** | **String**| Number that identifies the invoice. | |
| **updateTrackingStatusRequest** | [**UpdateTrackingStatusRequest**](UpdateTrackingStatusRequest.md)|  | |

### Return type

[**UpdateTrackingStatus**](UpdateTrackingStatus.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Cache-Control -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

