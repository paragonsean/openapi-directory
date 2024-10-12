# InvoiceApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**invoiceNotification2**](InvoiceApi.md#invoiceNotification2) | **POST** /api/orders/pvt/document/{orderId}/invoices | Order invoice notification |


<a id="invoiceNotification2"></a>
# **invoiceNotification2**
> CancelOrder2200Response invoiceNotification2(contentType, accept, orderId, invoiceNotificationRequest)

Order invoice notification

Once the order is invoiced, the seller should use this request to send the invoice information to the marketplace.  We strongly recommend that you always send the object of the invoiced items. With this practice, rounding errors will be avoided.  It is not allowed to use the same &#x60;invoiceNumber&#x60; in more than one request to the Order Invoice Notification endpoint.  Be aware that this endpoint is also used by the seller to send the order tracking information. This, however, should be done in a separate moment, once the seller has the tracking information.    &gt; The &#x60;Notify invoice&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

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

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String orderId = "70caf3941s6df1"; // String | ID of the order.
    InvoiceNotificationRequest invoiceNotificationRequest = new InvoiceNotificationRequest(); // InvoiceNotificationRequest | 
    try {
      CancelOrder2200Response result = apiInstance.invoiceNotification2(contentType, accept, orderId, invoiceNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#invoiceNotification2");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **orderId** | **String**| ID of the order. | |
| **invoiceNotificationRequest** | [**InvoiceNotificationRequest**](InvoiceNotificationRequest.md)|  | |

### Return type

[**CancelOrder2200Response**](CancelOrder2200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **429** | Too many requests |  -  |

