# NegotiableQuoteDeclineApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteNegotiableQuoteManagementV1DeclinePost**](NegotiableQuoteDeclineApi.md#negotiableQuoteNegotiableQuoteManagementV1DeclinePost) | **POST** /V1/negotiableQuote/decline | negotiableQuote/decline |


<a id="negotiableQuoteNegotiableQuoteManagementV1DeclinePost"></a>
# **negotiableQuoteNegotiableQuoteManagementV1DeclinePost**
> Boolean negotiableQuoteNegotiableQuoteManagementV1DeclinePost(negotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest)

negotiableQuote/decline

Decline the B2B quote. All custom pricing will be removed from this quote. The buyer will be able to place an order using their standard catalog prices and discounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableQuoteDeclineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableQuoteDeclineApi apiInstance = new NegotiableQuoteDeclineApi(defaultClient);
    NegotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest negotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest = new NegotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest(); // NegotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest | 
    try {
      Boolean result = apiInstance.negotiableQuoteNegotiableQuoteManagementV1DeclinePost(negotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableQuoteDeclineApi#negotiableQuoteNegotiableQuoteManagementV1DeclinePost");
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
| **negotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest** | [**NegotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest**](NegotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest.md)|  | [optional] |

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

