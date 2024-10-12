# NegotiableQuoteQuoteIdShippingMethodApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPut**](NegotiableQuoteQuoteIdShippingMethodApi.md#negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPut) | **PUT** /V1/negotiableQuote/{quoteId}/shippingMethod | negotiableQuote/{quoteId}/shippingMethod |


<a id="negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPut"></a>
# **negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPut**
> Boolean negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPut(quoteId, negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest)

negotiableQuote/{quoteId}/shippingMethod

Updates the shipping method on a negotiable quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableQuoteQuoteIdShippingMethodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableQuoteQuoteIdShippingMethodApi apiInstance = new NegotiableQuoteQuoteIdShippingMethodApi(defaultClient);
    Integer quoteId = 56; // Integer | Negotiable Quote id
    NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest = new NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest(); // NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest | 
    try {
      Boolean result = apiInstance.negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPut(quoteId, negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableQuoteQuoteIdShippingMethodApi#negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPut");
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
| **quoteId** | **Integer**| Negotiable Quote id | |
| **negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest** | [**NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest**](NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest.md)|  | [optional] |

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
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

