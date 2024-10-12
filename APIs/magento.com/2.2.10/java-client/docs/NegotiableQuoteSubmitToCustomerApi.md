# NegotiableQuoteSubmitToCustomerApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteNegotiableQuoteManagementV1AdminSendPost**](NegotiableQuoteSubmitToCustomerApi.md#negotiableQuoteNegotiableQuoteManagementV1AdminSendPost) | **POST** /V1/negotiableQuote/submitToCustomer | negotiableQuote/submitToCustomer |


<a id="negotiableQuoteNegotiableQuoteManagementV1AdminSendPost"></a>
# **negotiableQuoteNegotiableQuoteManagementV1AdminSendPost**
> Boolean negotiableQuoteNegotiableQuoteManagementV1AdminSendPost(negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest)

negotiableQuote/submitToCustomer

Submit the B2B quote to the customer. The quote status for the customer will be changed to &#39;Updated&#39;, and the customer can work with the quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableQuoteSubmitToCustomerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableQuoteSubmitToCustomerApi apiInstance = new NegotiableQuoteSubmitToCustomerApi(defaultClient);
    NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest = new NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest(); // NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest | 
    try {
      Boolean result = apiInstance.negotiableQuoteNegotiableQuoteManagementV1AdminSendPost(negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableQuoteSubmitToCustomerApi#negotiableQuoteNegotiableQuoteManagementV1AdminSendPost");
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
| **negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest** | [**NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest**](NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest.md)|  | [optional] |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

